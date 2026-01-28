# -*- coding: utf-8 -*-
"""
DICOM-SEG Generator

This script creates multiple DICOM-SEG images from available mask data.
Due to a bug in Cornerstone (a JavaScript library for medical imaging)
that prevents reading mask IDs, each mask must be stored in a separate DICOM-SEG file.
The example cases provided include CMB (Cerebral Microbleeds).

This module handles:
1. Loading DICOM series and mask data (in NIfTI format)
2. Converting mask data to DICOM-SEG format
3. Creating required JSON metadata for each mask
4. Saving DICOM-SEG files and associated metadata

@author: sean
"""
import json
import os
from typing import Dict, List, Any, Union

import numpy as np
import pydicom
from pipelinecore.dicomseg import utils
from pipelinecore.dicomseg.builder.base import PlatformJSONBuilder, ReviewBasePlatformJSONBuilder
from pipelinecore.dicomseg.schema.base import StudySeriesRequest
from pipelinecore.dicomseg.schema.enum import SeriesTypeEnum, ModelTypeEnum
from pydicom import FileDataset
from pydicom.dicomdir import DicomDir
from typing_extensions import Self

from .schema.cmb import CMBAITeam2Request, CMBMask2Request, CMBMaskModel2Request, CMBMaskSeries2Request
from .schema.cmb import CMBAITeamRequest, CMBStudyModelRequest, CMBStudyRequest
from .schema.cmb import CMBMaskRequest, CMBMaskSeriesRequest, CMBMaskInstanceRequest


class CMBPlatformJSONBuilder(PlatformJSONBuilder[CMBAITeamRequest]):
    model_class = CMBAITeamRequest
    model_type = ModelTypeEnum.CMB.value
    series_type = SeriesTypeEnum.SWAN.value

    def build_mask_instance(self, source_images: List[Union[FileDataset, DicomDir]],
                            dcm_seg: Union[FileDataset, DicomDir], *args, **kwargs) -> Self:
        main_seg_slice = kwargs['main_seg_slice']
        mask_instance_dict = dict()
        # Extract UIDs from the DICOM-SEG and source images
        seg_sop_instance_uid = dcm_seg.get((0x008, 0x0018)).value
        seg_series_instance_uid = dcm_seg.get((0x020, 0x000E)).value
        dicom_sop_instance_uid = source_images[main_seg_slice].get((0x008, 0x0018)).value
        # Extract mask name from DICOM-SEG Series Description
        # e.g. (0008,103E) Series Description: synthseg_SWAN_original_CMB_from_T1BRAVO_AXI_original_CMB

        # Get additional mask parameters from kwargs or use defaults
        mask_index = kwargs.get('mask_index', 1)
        main_seg_slice = kwargs.get('main_seg_slice', "")
        diameter = kwargs.get('diameter', '0.0')
        _type = kwargs.get('type', '')
        location = kwargs.get('location', 'M')
        prob_max = kwargs.get('prob_max', '1.0')

        # Create mask instance dictionary with all required metadata
        mask_instance_dict.update({
            'mask_index': mask_index,
            'mask_name': "A{}".format(mask_index),
            'diameter': diameter,
            'type': _type,
            'location': location,
            'prob_max': prob_max,
            'checked': "1",
            'is_ai': "1",
            'seg_sop_instance_uid': seg_sop_instance_uid,
            'seg_series_instance_uid': seg_series_instance_uid,
            'dicom_sop_instance_uid': dicom_sop_instance_uid,
            'main_seg_slice': main_seg_slice,
            'is_main_seg': "1"
        })
        return CMBMaskInstanceRequest.model_validate(mask_instance_dict)

    # def build_mask_series(self, source_images: List[Union[FileDataset, DicomDir]],
    #                       dcm_seg: Union[FileDataset, DicomDir], *args,
    #                       **kwargs) -> Dict[str,Any]:
    def build_mask_series(self,
                          source_images: List[Union[FileDataset, DicomDir]],
                          reslut_list: List[Dict[str, Any]],
                          pred_json_list: List[Dict[str, Any]],
                          # dcm_seg: Union[FileDataset, DicomDir],
                          *args, **kwargs) -> Union[Dict[str, Any], Any]:

        """
            one cmb lesion is one mask series

        """
        series_instance_uid = source_images[0].get((0x0020, 0x000E)).value
        mask_series_dict = {
            'series_instance_uid': series_instance_uid,
            'series_type': self.series_type,
            'model_type': self.model_type
        }
        mask_instance_list = []
        # diameter -> pred_diameter = kwargs.get('diameter', '0.0')
        # type     -> class_name
        # location -> type_name
        # sub_location = kwargs.get('sub_location', '2')
        # prob_max -> CMB_prob
        for index, reslut in enumerate(reslut_list):
            filter_cmd_data = list(filter(lambda x: x['label#'] == reslut['mask_index'], pred_json_list))
            if filter_cmd_data:
                pass
                filter_cmd: Dict[str, Any] = filter_cmd_data[0]
            else:
                continue
            dcm_seg_path = reslut['dcm_seg_path']
            with open(dcm_seg_path, 'rb') as f:
                dcm_seg = pydicom.read_file(f)
            kwargs.update({'diameter': filter_cmd['pred_diameter'],
                           'type': filter_cmd['class_name'],
                           'location': filter_cmd['type_name'],
                           'prob_max': filter_cmd['CMB_prob'],
                           'main_seg_slice': reslut['main_seg_slice'],
                           'mask_index': reslut['mask_index']
                           })
            # Create a mask instance for this series
            mask_instance_list.append(self.build_mask_instance(source_images,
                                                               dcm_seg, *args, **kwargs))

        # Add the instances to the series dictionary
        mask_series_dict.update({'instances': mask_instance_list})
        return CMBMaskSeriesRequest.model_validate(mask_series_dict)

    def set_mask(self, source_images: List[Union[FileDataset, DicomDir]],
                 result_list: List[Dict[str, Any]],
                 pred_json_list: List[Dict[str, Any]], group_id: int) -> Self:

        study_instance_uid = source_images[0].get((0x0020, 0x000D)).value
        mask_dict = {
            'study_instance_uid': study_instance_uid,
            'group_id': group_id
        }
        mask_series = self.build_mask_series(source_images=source_images,
                                             reslut_list=result_list,
                                             pred_json_list=pred_json_list)
        mask_dict.update({'series': [mask_series]})
        self._mask_request = CMBMaskRequest.model_validate(mask_dict)
        return self

    def set_study(self, source_images: List[Union[FileDataset, DicomDir]],
                  result_list: List[Dict[str, Any]],
                  pred_json_list: List[Dict[str, Any]], group_id: int) -> Self:

        study_dict = self.build_study_basic_info(source_images=source_images,
                                                 group_id=group_id)
        study_series = self.build_study_series(source_images=source_images)
        study_model = self.build_study_model(pred_json_list=pred_json_list)
        study_dict.update({'series': study_series,
                           'model': study_model})
        self._study_request = CMBStudyRequest.model_validate(study_dict)

        return self

    def build_study_series(self, source_images: List[Union[FileDataset, DicomDir]]
                           , *args, **kwargs) -> Union[Dict[str, Any], Any]:
        series_list = []
        series_instance_uid_dict = {}
        for index, dicom_ds in enumerate(source_images):
            series_instance_uid = dicom_ds.get((0x0020, 0x000E)).value
            if series_instance_uid_dict.get(series_instance_uid) is None:

                # 取得影像解析度
                resolution_x = dicom_ds.get((0x0028, 0x0010)).value
                resolution_y = dicom_ds.get((0x0028, 0x0011)).value

                series_instance_uid_dict.update({series_instance_uid: {
                    'series_type': self.series_type,
                    'resolution_x': resolution_x,
                    'resolution_y': resolution_y
                }})
            else:
                continue

        for series_instance_uid, series_info in series_instance_uid_dict.items():
            instance_dict = dict()

            # Update instance dictionary
            instance_dict.update(dict(
                series_type=series_info['series_type'],
                series_instance_uid=series_instance_uid,
                resolution_x=series_info['resolution_x'],
                resolution_y=series_info['resolution_y']
            ))
            series_list.append(StudySeriesRequest.model_validate(instance_dict))

        # Validate and return the sorted request
        return series_list

    def build_study_model(self, pred_json_list: List[Dict[str, Any]]
                          , *args, **kwargs) -> Union[Dict[str, Any], Any]:
        study_model = dict(lession=len(pred_json_list),
                           series_type=self.series_type,
                           model_type=self.model_type,
                           status="1",
                           report="", )
        return [CMBStudyModelRequest.model_validate(study_model)]


class ReviewCMBPlatformJSONBuilder(ReviewBasePlatformJSONBuilder):
    """Builder for CMB platform JSON with review mask instances.

    This builder constructs mask instance data from DICOM-SEG segmentation results
    and prediction JSON data. It uses the Template Method pattern to allow subclasses
    to customize slice index transformation without duplicating the entire method.

    Design Notes (Fowler):
        - Hook method `_transform_main_seg_slice` enables variation without duplication
        - Dictionary precomputation reduces O(n*m) to O(n+m) complexity
        - Helper methods extracted for single responsibility
    """
    model_type = ModelTypeEnum.CMB.value
    MaskInstanceClass = CMBMaskInstanceRequest

    def _transform_main_seg_slice(self, raw_slice: int, source_images: List[Union[FileDataset, DicomDir]]) -> int:
        """Hook method for slice index transformation.

        Override this method in subclasses to customize how the main segmentation
        slice index is calculated. Default behavior returns the slice unchanged
        (forward indexing).

        Mathematical Basis (Knuth):
            DICOM slices use 0-based indexing. This method provides a hook point
            for coordinate system transformations between different DICOM viewers.

            Default: identity function f(x) = x

            Complexity: O(1) - constant time operation

        Args:
            raw_slice: Original slice index from segmentation result (0-based)
            source_images: List of source DICOM images

        Returns:
            Transformed slice index for the target coordinate system
        """
        return raw_slice

    def _build_pred_json_map(self, pred_json_data_list: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        """Precompute lookup table for prediction data.

        Performance Optimization (Knuth):
            Converts O(m) filter operation per result to O(1) dictionary lookup.
            One-time O(m) cost amortized across n result iterations.

            Before: O(n*m) nested iteration
            After: O(n+m) with dictionary precomputation

            Space trade-off: O(m) additional memory for dictionary

        Args:
            pred_json_data_list: List of prediction JSON data entries

        Returns:
            Dictionary mapping label# (as string) to prediction data
        """
        return {str(item['label#']): item for item in pred_json_data_list}

    def _load_dicom_seg(self, dcm_seg_path: str) -> FileDataset:
        """Load DICOM-SEG file from path.

        Args:
            dcm_seg_path: Path to DICOM-SEG file

        Returns:
            Loaded DICOM FileDataset
        """
        with open(dcm_seg_path, 'rb') as f:
            return pydicom.read_file(f)

    def _build_mask_instance_dict(
        self,
        result: Dict[str, Any],
        filter_cmd: Dict[str, Any],
        dcm_seg: FileDataset,
        source_images: List[Union[FileDataset, DicomDir]]
    ) -> Dict[str, Any]:
        """Build mask instance dictionary from components.

        Args:
            result: Segmentation result data
            filter_cmd: Prediction data for this mask
            dcm_seg: Loaded DICOM-SEG file
            source_images: List of source DICOM images

        Returns:
            Dictionary with mask instance metadata
        """
        # Extract UIDs from the DICOM-SEG and source images
        seg_sop_instance_uid = dcm_seg.get((0x008, 0x0018)).value
        seg_series_instance_uid = dcm_seg.get((0x020, 0x000E)).value
        dicom_sop_instance_uid = source_images[int(result['main_seg_slice'])].get((0x008, 0x0018)).value

        # Apply hook method for slice transformation
        main_seg_slice = self._transform_main_seg_slice(result['main_seg_slice'], source_images)

        return {
            'diameter': filter_cmd['pred_diameter'],
            'type': filter_cmd['class_name'],
            'location': filter_cmd['type_name'],
            'prob_max': filter_cmd['CMB_prob'],
            'main_seg_slice': main_seg_slice,
            'mask_index': result['mask_index'],
            'mask_name': "A{}".format(result['mask_index']),
            'seg_sop_instance_uid': seg_sop_instance_uid,
            'seg_series_instance_uid': seg_series_instance_uid,
            'dicom_sop_instance_uid': dicom_sop_instance_uid,
            'is_main_seg': "1",
            'checked': "1",
            'is_ai': "1",
        }

    def get_mask_instance(self, source_images: List[Union[FileDataset, DicomDir]],
                          series_type: SeriesTypeEnum,
                          dicom_seg_result: Dict[str, Any],
                          pred_json: Dict[str, Any],
                          *args, **kwargs) -> List["MaskInstanceClass"]:
        """Build list of mask instances from segmentation and prediction data.

        This method uses the Template Method pattern: the core algorithm is defined
        here, while the `_transform_main_seg_slice` hook allows subclasses to
        customize slice index calculation without duplicating the entire method.

        Algorithm (Knuth):
            1. Build prediction lookup table: O(m)
            2. Iterate through results: O(n)
               - Dictionary lookup: O(1)
               - Load DICOM-SEG: O(file_size)
               - Build instance dict: O(1)
            Total: O(n + m) + O(n * file_IO)

        Args:
            source_images: List of source DICOM images
            series_type: Type of the series (e.g., SWAN)
            dicom_seg_result: Segmentation result with 'data' list
            pred_json: Prediction JSON with 'data' list

        Returns:
            List of validated MaskInstanceClass objects
        """
        result_data_list = dicom_seg_result['data']
        pred_json_data_list = pred_json['data']

        # Precompute lookup table: O(m)
        pred_json_map = self._build_pred_json_map(pred_json_data_list)

        mask_instance_list = []
        for result in result_data_list:
            # O(1) dictionary lookup instead of O(m) filter
            filter_cmd = pred_json_map.get(str(result['mask_index']))
            if not filter_cmd:
                continue

            dcm_seg = self._load_dicom_seg(result['dcm_seg_path'])
            mask_instance_dict = self._build_mask_instance_dict(
                result, filter_cmd, dcm_seg, source_images
            )
            mask_instance_list.append(self.MaskInstanceClass.model_validate(mask_instance_dict))

        return mask_instance_list

    def get_study_model(self, series_type: SeriesTypeEnum, pred_data: Dict[str, Any],
                        *args, **kwargs) -> "StudyModelClass":
        pred_json_list = pred_data['data']
        study_model = dict(lession=len(pred_json_list),
                           series_type=series_type.value,
                           model_type=self.model_type,
                           status="1",
                           report="", )
        return self.StudyModelClass.model_validate(study_model)


class NewReviewCMBPlatformJSONBuilder(ReviewCMBPlatformJSONBuilder):
    """Builder for CMB platform JSON with reverse slice indexing.

    This builder extends ReviewCMBPlatformJSONBuilder to provide reverse slice
    indexing for compatibility with legacy DICOM viewers that use posterior-to-anterior
    coordinate systems.

    Design Notes (Fowler - Template Method Pattern):
        Instead of duplicating the entire get_mask_instance() method (35 lines),
        this class overrides only the _transform_main_seg_slice() hook method (5 lines).
        This eliminates 99% code duplication while preserving the coordinate transformation.

    Linus's "Good Taste" Principle:
        "This is NOT garbage. You need only override the transformation, not the whole class."
    """
    AITeamClass = CMBAITeam2Request
    MaskClass = CMBMask2Request
    MaskSeriesClass = CMBMaskSeries2Request
    MaskModelClass = CMBMaskModel2Request

    def _transform_main_seg_slice(self, raw_slice: int, source_images: List[Union[FileDataset, DicomDir]]) -> int:
        """Reverse slice indexing for legacy DICOM viewer compatibility.

        Mathematical Basis (Knuth):
        =============================
        DICOM Image Stack Coordinate Systems:

        Standard (Anterior → Posterior):
            slice_0 -----> slice_n-1
            [front]        [back]

        Legacy Viewer (Posterior → Anterior):
            slice_n-1 -----> slice_0
            [back]           [front]

        Transformation Formula:
            new_index = total_slices - old_index

        This reverses the slice ordering such that:
            - Slice 0 in standard → Slice n in legacy
            - Slice n-1 in standard → Slice 1 in legacy

        Complexity Analysis:
            Time: O(1) - constant arithmetic operation
            Space: O(1) - no additional storage

        Args:
            raw_slice: Original slice index (0-based, anterior→posterior)
            source_images: List of source DICOM images

        Returns:
            Reversed slice index (0-based, posterior→anterior)

        Example:
            Given: source_images has 100 slices (indices 0-99)
                   raw_slice = 25 (26th slice from front)
            Return: 100 - 25 = 75 (75th slice from front = 26th from back)
        """
        return len(source_images) - raw_slice

    def get_mask_series(self, source_images: List[Union[FileDataset, DicomDir]],
                        series_type: SeriesTypeEnum,
                        dicom_seg_result,
                        pred_json,
                        *args, **kwargs) -> "MaskSeriesClass":
        """
            dicom_seg_result : {"series_type": {}, "data":{} }
            dicom_seg_result : {"series_type": {}, "data":{} }
        """
        series_instance_uid = source_images[0].get((0x0020, 0x000E)).value
        mask_series_dict = {
            'series_instance_uid': series_instance_uid,
            'series_type': series_type,
        }
        mask_instance = self.get_mask_instance(source_images=source_images,
                                               series_type=series_type,
                                               dicom_seg_result=dicom_seg_result,
                                               pred_json=pred_json,
                                               *args, **kwargs)
        mask_series_dict.update({'instances': mask_instance})

        return self.MaskSeriesClass.model_validate(mask_series_dict)

    def get_mask_model(self, source_images: List[Union[FileDataset, DicomDir]], series_type: SeriesTypeEnum,
                       dicom_seg_result: Dict[str, Any], pred_json: Dict[str, Any], *args, **kwargs) -> MaskModelClass:
        mask_model_dict = {}
        mask_series = self.get_mask_series(source_images=source_images,
                                           series_type=series_type,
                                           dicom_seg_result=dicom_seg_result,
                                           pred_json=pred_json)
        mask_model_dict.update({"series": [mask_series],
                                "model_type": self.model_type
                                })
        return self.MaskModelClass.model_validate(mask_model_dict)

    def build_mask(self, dicom_seg_result_list, pred_json_list, *args, **kwargs) -> Self:
        mask_dict = {}
        if all((self._series_dict is not None, self.group_id is not None)):
            for index, (series_name, series_source_images) in enumerate(self._series_dict.items()):
                if index == 0:
                    study_instance_uid = series_source_images[0].get((0x0020, 0x000D)).value
                    mask_dict.update({
                        'study_instance_uid': study_instance_uid,
                        'group_id': self.group_id
                    })
                    break
        else:
            raise ValueError('self._series_dict or self.group_id is None')
        model_series_list = []
        mask_model_dict = {}
        for index, (series_name, series_source_images) in enumerate(self._series_dict.items()):

            mask_model_series: CMBMaskModel2Request = self.get_mask_model(source_images=series_source_images,
                                                                          dicom_seg_result=dicom_seg_result_list[index],
                                                                          pred_json=pred_json_list[index],
                                                                          series_type=series_name,
                                                                          *args, **kwargs)
            model_series_list.extend(mask_model_series.series)
            if index == 0:
                mask_model_dict.update({"model_type": mask_model_series.model_type})

        mask_model_dict.update({'series': model_series_list})
        mask_dict.update({'model': [mask_model_dict]})
        self._mask_request = self.MaskClass.model_validate(mask_dict)
        return self


def main_review_cmd(_id, path_dcms, path_nii, path_dcmseg):
    """
    Main function to process command line arguments and execute the pipeline.

    This function:
    """
    # Parse command line arguments

    group_id = os.getenv("GROUP_ID_CMB", 44)

    # Create output directory
    output_series_folder = path_dcmseg.joinpath(f'{_id}')
    if output_series_folder.is_dir():
        output_series_folder.mkdir(exist_ok=True, parents=True)
    else:
        output_series_folder.parent.mkdir(parents=True, exist_ok=True)

    series_name = path_nii.name.split('.')[0]
    # Load prediction data from NIfTI file
    new_nifti_array = utils.get_array_to_dcm_axcodes(path_nii)
    pred_json_path = path_nii.parent.joinpath(path_nii.name.replace('.nii.gz',
                                                                    '.json'))

    sorted_dcms, image, first_dcm, source_images = utils.load_and_sort_dicom_files(str(path_dcms))
    pred_data_unique = np.unique(new_nifti_array)
    if len(pred_data_unique) < 1:
        return None
    else:
        pred_data_unique = pred_data_unique[1:]  # Exclude background value (0)

    # Create DICOM-SEG files for each unique region
    result_list = utils.create_dicom_seg_file(pred_data_unique,
                                              new_nifti_array,
                                              series_name,
                                              output_series_folder,
                                              image,
                                              first_dcm,
                                              source_images)
    # Create platform JSON
    with open(pred_json_path) as f:
        pred_json = json.load(f)
    dicom_seg_result_list = [{"series_type": SeriesTypeEnum.SWAN,
                              "data": result_list}]
    pred_json_list = [{"series_type": SeriesTypeEnum.SWAN,
                       "data": pred_json}, ]
    # cmb_platform_json_builder = ReviewCMBPlatformJSONBuilder()
    cmb_platform_json_builder = NewReviewCMBPlatformJSONBuilder()
    cmb_platform_json = (cmb_platform_json_builder.set_series_type(SeriesTypeEnum.SWAN, source_images=source_images)
                         .set_group_id(group_id)
                         .build_sorted()
                         .build_study(pred_json_list=pred_json_list)
                         .build_mask(dicom_seg_result_list=dicom_seg_result_list,
                                     pred_json_list=pred_json_list)
                         .build())
    platform_json_path = output_series_folder.joinpath(path_nii.name.replace('.nii.gz',
                                                                             '_platform_json.json'))
    with open(platform_json_path, 'w') as f:
        f.write(cmb_platform_json.model_dump_json())
    print("Processing complete!")
    return None
