## 1. Analysis & Planning
- [ ] 1.1 Analyze `src/brain_cmb/core/cmb.py` to map the exact mathematical operations (normalization, inference, post-processing).
- [ ] 1.2 Analyze `src/brain_cmb/pipeline_cmb_tensorflow.py` to map the configuration space (ENV vars) and failure modes.
- [ ] 1.3 Analyze `src/brain_cmb/dicomseg/` to map the data schema and DICOM tag generation logic.

## 2. Documentation Generation
- [ ] 2.1 Create `docs/brain-cmb/requirements/PRD.md`:
    - Define User Personas (Radiologist, AI Researcher).
    - Define Clinical Workflows (SWAN Input -> CMB Detection -> Review).
- [ ] 2.2 Create `docs/brain-cmb/requirements/SR.md`:
    - Define Functional Requirements (Input formats, Output files).
    - Define Performance Requirements (GPU usage, Time constraints).
    - Document "Empirical Constants" found in code.
- [ ] 2.3 Create `docs/brain-cmb/architecture/SD.md`:
    - Diagram the Pipeline Architecture (Orchestrator pattern).
    - Explain the "Sliding Window Inference" algorithm with mathematical notation.
    - Document the Data Flow (NIfTI -> Numpy -> JSON -> DICOM).

## 3. Specification & Validation
- [ ] 3.1 Update `specs/brain-cmb-pipeline/spec.md` to match the rigorous findings from the analysis.
- [ ] 3.2 Verify that the generated documentation traces back to the code (Literate check).
- [ ] 3.3 Run `openspec validate analyze-generate-brain-cmb-docs --strict`.
