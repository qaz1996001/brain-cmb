## ADDED Requirements

### Requirement: CMB Detection Pipeline
The system SHALL accept a SWAN MRI series and a T1-weighted template to produce a segmentation mask of Cerebral Microbleeds (CMB).

#### Scenario: Standard Inference
- **WHEN** a valid SWAN NIfTI file and T1 template are provided
- **THEN** the system generates a `Pred_CMB.nii.gz` file containing binary masks of detected CMBs
- **AND** the system generates a `Pred_CMB.json` file with structured metadata for each detected lesion

### Requirement: False Positive Reduction
The system SHALL apply a secondary classification stage to filter initial candidates.

#### Scenario: Filtering
- **WHEN** candidates are detected by the primary segmentation model
- **THEN** a secondary model evaluates each candidate
- **AND** candidates with a probability score below `0.084` (min_th) are discarded
- **AND** candidates with a probability score below `0.357` (FP_reduction_th) are classified as 'other'

### Requirement: DICOM-SEG Generation
The system SHALL convert the NIfTI prediction results into DICOM-SEG format compliant with the study's metadata.

#### Scenario: Mask Conversion
- **WHEN** prediction files (`Pred_CMB.nii.gz`, `Pred_CMB.json`) are generated
- **THEN** the system creates a DICOM-SEG series
- **AND** each distinct lesion is encapsulated in a manner compatible with the target viewer (e.g., separate files if required by viewer constraints)

