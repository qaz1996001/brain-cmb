# CMB Pipeline Modular Architecture Specification

## ADDED Requirements

### Requirement: ImageNormalizer Component
The system SHALL provide an ImageNormalizer component responsible for medical image preprocessing operations.

#### Scenario: Load and normalize SWAN volume
- **GIVEN** a SWAN NIfTI file path and target spacing parameters
- **WHEN** `load_and_normalize()` is called
- **THEN** the component SHALL return a normalized 3D NumPy array with intensity range [0, 1]
- **AND** the array SHALL be resampled to the target isotropic spacing
- **AND** the coordinate system SHALL be transformed from RAS to LPS orientation

#### Scenario: Load SynthSeg segmentation
- **GIVEN** a SynthSeg segmentation file path and target volume shape
- **WHEN** `load_synthseg_seg()` is called
- **THEN** the component SHALL return a uint16 label array matching the target shape
- **AND** the array SHALL preserve anatomical region labels from the SynthSeg output

#### Scenario: Normalize with brain mask
- **GIVEN** an image array and binary brain mask
- **WHEN** `normalize()` is called with percentile parameters
- **THEN** the component SHALL clip intensity to robust min/max percentiles
- **AND** SHALL linearly rescale to [0, 1] range using only positive voxels within mask

### Requirement: SlidingWindowInferenceEngine Component
The system SHALL provide a SlidingWindowInferenceEngine component for patch-based model inference with overlap handling.

#### Scenario: Initialize with Gaussian blending
- **GIVEN** patch size (64, 64, 64) and overlap 0.5
- **WHEN** the engine is constructed with `blend_mode="gaussian"`
- **THEN** it SHALL precompute a Gaussian importance kernel for smooth blending
- **AND** the kernel SHALL have shape (64, 64, 64) with sigma = 1/8 * patch_size

#### Scenario: Perform sliding window inference
- **GIVEN** a normalized 3D volume and trained TensorFlow model
- **WHEN** `infer()` is called with 50% overlap
- **THEN** the engine SHALL divide the volume into overlapping patches
- **AND** SHALL run the model on each patch independently
- **AND** SHALL blend predictions using Gaussian weighting to eliminate boundary artifacts
- **AND** SHALL return a prediction map with the same shape as the input volume

#### Scenario: Skip inference outside brain mask
- **GIVEN** a brain mask limiting the region of interest
- **WHEN** `infer()` is called with the mask parameter
- **THEN** the engine SHALL only process patches containing brain voxels
- **AND** SHALL skip empty patches to reduce computation time

### Requirement: ObjectAnalyzer Component
The system SHALL provide an ObjectAnalyzer component for connected component analysis and object classification.

#### Scenario: Watershed segmentation
- **GIVEN** a continuous prediction map and threshold value
- **WHEN** `get_watershed_label()` is called
- **THEN** the component SHALL apply watershed algorithm to separate touching objects
- **AND** SHALL use morphological peak detection with specified radius parameter
- **AND** SHALL return an integer label map with unique IDs for each detected object

#### Scenario: Per-object classification
- **GIVEN** labeled objects from segmentation and the original SWAN image
- **WHEN** `classify_objects()` is called with the second-stage model
- **THEN** the component SHALL extract 26³ patches centered on each object centroid
- **AND** SHALL run the classification model on each patch with Gaussian location prior
- **AND** SHALL return a DataFrame with columns: [Pred_label, Pred_diameter, TP_conf, CMB_prob, Pred_type]
- **AND** SHALL filter objects below the minimum confidence threshold (0.084)

#### Scenario: Map anatomical locations
- **GIVEN** a SynthSeg anatomical segmentation and detected CMB objects
- **WHEN** analyzing object locations
- **THEN** the component SHALL determine the most frequent anatomical label within each CMB
- **AND** SHALL map the label index to human-readable region name (e.g., "L. frontal", "R. basal ganglion")

### Requirement: OutputFormatter Component
The system SHALL provide an OutputFormatter component for saving results in standardized medical imaging formats.

#### Scenario: Save NIfTI prediction mask
- **GIVEN** an integer label map and original SWAN file metadata
- **WHEN** `save_nifti()` is called
- **THEN** the component SHALL resize the label map to match the original image dimensions
- **AND** SHALL transform coordinates from LPS back to RAS orientation
- **AND** SHALL save as NIfTI with the original affine matrix and spacing metadata
- **AND** SHALL preserve data type as uint16

#### Scenario: Save JSON results table
- **GIVEN** a DataFrame of detected objects with predictions
- **WHEN** `save_json()` is called
- **THEN** the component SHALL serialize the DataFrame to JSON with 'records' orientation
- **AND** SHALL include metadata: [label#, class_name, type, type_name, pred_diameter, CMB_prob, c-time]
- **AND** SHALL format creation time as 'YYYY/MM/DD HH:MM'
- **AND** SHALL write to the specified output path with UTF-8 encoding

### Requirement: CmbPipeline Template Method Integration
The system SHALL integrate extracted components into the BasePipeline template method hooks.

#### Scenario: Prepare phase
- **GIVEN** input payload with SWAN file and T1 template paths
- **WHEN** `prepare()` is executed
- **THEN** the pipeline SHALL validate file existence
- **AND** SHALL use ImageNormalizer to load and preprocess the SWAN volume
- **AND** SHALL return PreparedData containing normalized array and metadata

#### Scenario: Inference phase
- **GIVEN** prepared data from the prepare phase
- **WHEN** `run_inference()` is executed
- **THEN** the pipeline SHALL call external SynthSeg command for anatomical segmentation
- **AND** SHALL use SlidingWindowInferenceEngine with model1 for CMB segmentation
- **AND** SHALL return InferenceArtifacts containing segmentation map and original image

#### Scenario: Postprocess phase
- **GIVEN** inference artifacts from the inference phase
- **WHEN** `postprocess()` is executed
- **THEN** the pipeline SHALL use ObjectAnalyzer to classify detected CMBs
- **AND** SHALL use OutputFormatter to save NIfTI and JSON results
- **AND** SHALL return OutputArtifacts with file paths

### Requirement: Backward Compatibility Wrapper
The system SHALL maintain backward compatibility with existing CMBServiceTF API.

#### Scenario: Legacy API usage
- **GIVEN** existing code calling `CMBServiceTF().cmb_classify()`
- **WHEN** the legacy method is invoked
- **THEN** the wrapper SHALL delegate to the new component-based implementation
- **AND** SHALL emit a deprecation warning to encourage migration
- **AND** SHALL return identical results to the original implementation

#### Scenario: Legacy import path
- **GIVEN** code importing `from brain_cmb.core.cmb import CMBServiceTF`
- **WHEN** the import statement is executed
- **THEN** the module SHALL successfully import without error
- **AND** SHALL log a deprecation message recommending pipeline usage

### Requirement: Component Testability
The system SHALL design all components to support comprehensive unit testing.

#### Scenario: Mock TensorFlow models
- **GIVEN** a unit test for SlidingWindowInferenceEngine
- **WHEN** creating test fixtures
- **THEN** the test SHALL be able to inject mock TensorFlow models via constructor
- **AND** SHALL verify correct patch extraction without requiring GPU

#### Scenario: Test with synthetic data
- **GIVEN** a unit test for ObjectAnalyzer
- **WHEN** testing watershed segmentation
- **THEN** the test SHALL use synthetic prediction maps with known ground truth
- **AND** SHALL assert correct connected component detection

#### Scenario: Isolated file I/O testing
- **GIVEN** a unit test for OutputFormatter
- **WHEN** testing NIfTI save functionality
- **THEN** the test SHALL use temporary file fixtures
- **AND** SHALL validate output format without requiring real medical images

### Requirement: Performance Preservation
The refactored system SHALL maintain computational performance within 1% of the original implementation.

#### Scenario: End-to-end runtime benchmark
- **GIVEN** a standardized test dataset with 10 SWAN volumes
- **WHEN** comparing original vs refactored pipeline execution time
- **THEN** the median runtime difference SHALL be ≤ 1%
- **AND** the 95th percentile runtime SHALL not exceed 2% overhead

#### Scenario: Memory usage validation
- **GIVEN** processing a typical 512x512x128 SWAN volume
- **WHEN** monitoring peak memory usage
- **THEN** the refactored implementation SHALL not increase peak memory by >5%

### Requirement: Code Quality Standards
The system SHALL adhere to Fowler's refactoring principles and Knuth's literate programming style.

#### Scenario: Single Responsibility compliance
- **GIVEN** any extracted component class
- **WHEN** reviewing class methods
- **THEN** all methods SHALL relate to a single, cohesive responsibility
- **AND** no class SHALL exceed 150 lines of code

#### Scenario: Literate documentation
- **GIVEN** any algorithmic component (e.g., watershed segmentation)
- **WHEN** reading the source code
- **THEN** the module SHALL include literate comments explaining the mathematical basis
- **AND** SHALL document time/space complexity using Big-O notation
- **AND** SHALL explain the *why* before the *how*

#### Scenario: Test coverage requirement
- **GIVEN** the completed refactoring
- **WHEN** running code coverage analysis
- **THEN** unit test coverage for new components SHALL be ≥ 90%
- **AND** integration tests SHALL cover all template method hooks
