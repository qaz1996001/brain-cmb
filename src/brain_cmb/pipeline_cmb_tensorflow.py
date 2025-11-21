#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TensorFlow CMB pipeline with template-method based orchestration.
"""
from __future__ import annotations

import glob
import os
import shutil
import subprocess
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

# warnings.filterwarnings("ignore")  # 忽略警告输出
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from .core.cmb import CMBServiceTF
from pipelinecore import (
    BasePipeline,
    GPUMemoryError,
    GpuResourceManager,
    LogManager,
    PipelineContext,
    PipelinePaths,
    TensorflowPipelineMixin,
)


@dataclass(frozen=True)
class CmbInputs:
    swan_file: Path
    t1_template: Path


@dataclass(frozen=True)
class CmbInferenceArtifacts:
    swan_file: Path
    synthseg_path: Path


@dataclass(frozen=True)
class CmbOutputArtifacts:
    synthseg_copy: Path
    prediction_mask: Path
    prediction_json: Path


def _read_float_env(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


def _read_int_env(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, default))
    except (TypeError, ValueError):
        return default


def _read_bool_env(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _build_gpu_manager(gpu_index: int) -> GpuResourceManager:
    return GpuResourceManager(
        gpu_index,
        usage_threshold=_read_float_env("GPU_USAGE_THRESHOLD", 0.9),
        check_interval=_read_float_env("GPU_USAGE_CHECK_INTERVAL", 5.0),
        max_checks=_read_int_env("GPU_USAGE_MAX_CHECKS", 3),
        usage_check_enabled=_read_bool_env("GPU_USAGE_CHECK_ENABLED", False),
    )


class CmbPipeline(
    TensorflowPipelineMixin,
    BasePipeline[CmbInputs, CmbInputs, CmbInferenceArtifacts, CmbOutputArtifacts],
):
    def __init__(
        self,
        context: PipelineContext,
        gpu_manager: GpuResourceManager,
        cmb_service: CMBServiceTF | None = None,
    ) -> None:
        TensorflowPipelineMixin.__init__(self, gpu_manager)
        BasePipeline.__init__(self, context)
        self._cmb_service = cmb_service or CMBServiceTF()

    def prepare(self, payload: CmbInputs) -> CmbInputs:
        for path in (payload.swan_file, payload.t1_template):
            if not path.exists():
                raise FileNotFoundError(path)
        return payload

    def run_inference(self, prepared: CmbInputs) -> CmbInferenceArtifacts:
        command = [
            PYTHON3,
            str(Path(__file__).with_name("main.py")),
            "-i",
            str(prepared.swan_file),
            "--template",
            str(prepared.t1_template),
            "--output",
            str(self.context.paths.process_dir),
            "--all",
            "False",
            "--CMB",
            "TRUE",
        ]
        self.context.logger.info("Running SynthSeg command: %s", " ".join(command))
        subprocess.run(command, check=True, capture_output=True, text=True)

        matches = sorted(
            glob.glob(f"{self.context.paths.process_dir}/synthseg_*SWAN_original_CMB*.nii.gz")
        )
        if not matches:
            raise FileNotFoundError("SynthSeg output not found in process directory.")
        synthseg_path = Path(matches[0])
        return CmbInferenceArtifacts(
            swan_file=prepared.swan_file,
            synthseg_path=synthseg_path,
        )

    def postprocess(self, inference_result: CmbInferenceArtifacts) -> CmbOutputArtifacts:
        output_dir = self.context.paths.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        normalized_name = self._normalize_filename(inference_result.synthseg_path.name)
        synthseg_copy = output_dir / normalized_name
        shutil.copy2(inference_result.synthseg_path, synthseg_copy)

        pred_mask = output_dir / "Pred_CMB.nii.gz"
        pred_json = output_dir / "Pred_CMB.json"

        self._cmb_service.cmb_classify(
            swan_path_str=str(inference_result.swan_file),
            temp_path_str=str(inference_result.synthseg_path),
            output_nii_path_str=str(pred_mask),
            output_json_path_str=str(pred_json),
        )
        self.context.logger.info("%s CMB inference finished.", self.context.pipeline_id)
        return CmbOutputArtifacts(
            synthseg_copy=synthseg_copy,
            prediction_mask=pred_mask,
            prediction_json=pred_json,
        )

    @staticmethod
    def _normalize_filename(file_name: str) -> str:
        study_id = get_study_id(file_name)
        if study_id:
            return file_name.replace(study_id, "").replace("__", "_").lstrip("_")
        return file_name


def pipeline_cmb(
    ID: str,
    swan_file: str,
    t1_file: str,
    path_output: str,
    path_code: str = "/mnt/d/wsl_ubuntu/pipeline/sean/code/",
    path_processModel: str = "/mnt/d/wsl_ubuntu/pipeline/sean/process/Deep_CMB/",
    path_json: str = "/mnt/d/wsl_ubuntu/pipeline/sean/json/",
    path_log: str = "/mnt/d/wsl_ubuntu/pipeline/sean/log/",
    path_synthseg: str = "/mnt/d/wsl_ubuntu/pipeline_synthseg/",
    gpu_n: int = 0,
) -> Tuple[str | None, str | None, str | None]:
    del path_code, path_json, path_synthseg  # kept for backward compatibility
    paths = PipelinePaths(
        process_dir=Path(path_processModel) / ID,
        output_dir=Path(path_output) / ID,
        log_dir=Path(path_log),
    )
    logger = LogManager(paths.log_dir).create_logger()
    context = PipelineContext(pipeline_id=ID, paths=paths, logger=logger)
    pipeline = CmbPipeline(context=context, gpu_manager=_build_gpu_manager(gpu_n))
    try:
        artifacts = pipeline.execute(
            CmbInputs(swan_file=Path(swan_file), t1_template=Path(t1_file))
        )
        return (
            str(artifacts.synthseg_copy),
            str(artifacts.prediction_mask),
            str(artifacts.prediction_json),
        )
    except GPUMemoryError as exc:
        logger.error("GPU insufficient for %s: %s", ID, exc)
    except subprocess.CalledProcessError as exc:
        logger.error("SynthSeg command failed: %s", exc, exc_info=True)
    except Exception:  # noqa: BLE001 - need to log unexpected exceptions
        logger.error("CMB pipeline failed for %s", ID, exc_info=True)
    return None, None, None


if __name__ == "__main__":
    load_dotenv()
    print('os.environ',os.environ)
    parser = pipeline_parser()
    args = parser.parse_args()

    ID = str(args.ID)
    Inputs = args.Inputs
    InputsDicomDir = args.InputsDicomDir
    path_output = str(args.Output_folder)

    path_process = os.getenv("PATH_PROCESS")
    print('path_process',path_process)
    path_processModel = os.path.join(path_process, "Deep_CMB")
    print('path_processModel',path_processModel)
    path_log = os.getenv("PATH_LOG")
    print('path_log',path_log)

    gpu_n = int(os.getenv("GPU_N", 0))
    swan_path_str = Inputs[0]
    t1_path_str = Inputs[1]

    _, output_nii_path_str, output_json_path_str = pipeline_cmb(
        ID,
        swan_path_str,
        t1_path_str,
        path_output,
        path_processModel=path_processModel,
        path_log=path_log,
        gpu_n=gpu_n,
    )
    if output_nii_path_str is not None:
        stdout, stderr = dicom_seg_cmb_file(ID, InputsDicomDir, output_nii_path_str, path_output)
        upload_dicom_seg(path_output, output_nii_path_str)
        upload_json(ID, InferenceEnum.CMB)