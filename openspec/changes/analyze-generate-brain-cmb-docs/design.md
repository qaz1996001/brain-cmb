## Context
The `brain-cmb` module is a sophisticated pipeline for detecting Cerebral Microbleeds (CMB) in SWAN MRI sequences. It orchestrates deep learning models (U-Net, ResNet) with classical image processing (Watershed, Gaussian blending) and integrates with a medical imaging platform via DICOM standards.

## Goals / Non-Goals
- **Goals**:
    - **Literate Explanation**: Explain the code to humans first.
    - **Mathematical Rigor**: Document the sliding window inference ($O(V)$), Gaussian importance sampling ($\sigma=1/8$), and false-positive reduction logic ($P(CMB) > 0.084$).
    - **Aesthetic Structure**: Organize documentation to mirror the clean separation of concerns: Service (Logic) vs. Pipeline (Orchestration) vs. Builder (Data).
- **Non-Goals**:
    - Refactoring code (unless bugs are found).
    - optimizing models.

## Design Principles (Knuthian Analysis)

### 1. Algorithm Analysis
> "People who analyze algorithms have double happiness."

- **Detection**: A 3D Sliding Window approach is used to handle large volumes.
    - *Complexity*: Linear with volume size, but constant memory footprint due to patch-based processing $(64^3)$.
    - *Elegance*: The `blend_mode="gaussian"` minimizes edge artifacts between patches, a mathematically sound approach to image reconstruction.
- **Segmentation**: Watershed algorithm converts the continuous probability map into discrete regions.
    - *Intuition*: Treating the probability map as terrain to find catchment basins.
- **Classification**: A secondary "False Positive Reduction" step ($P(CMB) > 0.357$) acts as a high-precision filter, acknowledging that segmentation models are often overly sensitive.

### 2. Data Structure Design
> "The psychological profiling of a programmer is mostly the ability to shift levels of abstraction."

- **Core**: NIfTI volumes (NumPy arrays) for efficient matrix operations.
- **Interface**: Pydantic models (`CMBMaskRequest`) enforce a strict schema for the external world, translating the "fuzzy" world of probability maps into the "rigid" world of DICOM tags.

### 3. Documentation Structure
We will adopt a layered approach:
1.  **Narrative (PRD)**: The clinical story.
2.  **Contract (SR)**: The mathematical boundaries.
3.  **Implementation (SD)**: The code as literature.

## Decisions
- **Decision 1**: Documentation will be generated in `docs/brain-cmb/` following the existing meta-framework templates.
- **Decision 2**: We will explicitly document "Magic Numbers" (e.g., `0.5175`, `0.084`) as "Empirical Constants" to encourage future rigorous derivation or externalization.

## Risks
- **Risk**: Misinterpreting the intent of legacy "magic numbers".
    - **Mitigation**: Mark them clearly as "inferred from code" if the derivation is unknown.
