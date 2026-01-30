# DICOM-SEG Builder Refactoring Specification

## MODIFIED Requirements

### Requirement: ReviewCMBPlatformJSONBuilder Template Method Architecture
The system SHALL refactor ReviewCMBPlatformJSONBuilder to eliminate code duplication through template method pattern with hook-based customization.

#### Scenario: Generate mask instances with forward slice indexing
- **GIVEN** a list of source DICOM images and segmentation results
- **AND** prediction JSON data with mask metadata
- **WHEN** `get_mask_instance()` is called on ReviewCMBPlatformJSONBuilder
- **THEN** the method SHALL use forward slice indexing (default behavior)
- **AND** SHALL return a list of MaskInstance objects
- **AND** SHALL delegate slice calculation to `_transform_main_seg_slice()` hook method
- **AND** the hook SHALL return raw_slice unchanged for forward indexing

#### Scenario: Efficient prediction data lookup
- **GIVEN** n segmentation results and m prediction data items
- **WHEN** `get_mask_instance()` is called
- **THEN** the method SHALL precompute a dictionary mapping label# → prediction data
- **AND** SHALL perform O(1) dictionary lookups instead of O(m) filter operations
- **AND** the total time complexity SHALL be O(n + m) instead of O(n * m)
- **AND** SHALL require O(m) additional space for the lookup dictionary

#### Scenario: Load DICOM-SEG dataset
- **GIVEN** a valid DICOM-SEG file path
- **WHEN** loading the DICOM dataset
- **THEN** the method SHALL use `_load_dicom_seg()` helper method
- **AND** SHALL return a pydicom FileDataset object
- **AND** SHALL handle file I/O errors appropriately

#### Scenario: Find prediction data by mask index
- **GIVEN** a mask index and precomputed prediction lookup dictionary
- **WHEN** `_find_prediction_data()` is called
- **THEN** the method SHALL return the matching prediction data dict if found
- **AND** SHALL return None if mask index is not in the dictionary
- **AND** SHALL perform the lookup in O(1) constant time

## ADDED Requirements

### Requirement: Slice Index Transformation Hook
The system SHALL provide a protected hook method for subclasses to customize slice index calculation based on coordinate system requirements.

#### Scenario: Default forward slice indexing (parent class)
- **GIVEN** a raw slice index and list of source images
- **WHEN** `_transform_main_seg_slice()` is called on ReviewCMBPlatformJSONBuilder
- **THEN** the method SHALL return the raw slice index unchanged
- **AND** SHALL maintain anterior-to-posterior slice ordering
- **AND** SHALL execute in O(1) constant time

#### Scenario: Reversed slice indexing (child class override)
- **GIVEN** a raw slice index and list of source images
- **WHEN** `_transform_main_seg_slice()` is called on NewReviewCMBPlatformJSONBuilder
- **THEN** the method SHALL calculate reversed index as: len(source_images) - raw_slice
- **AND** SHALL transform anterior-to-posterior to posterior-to-anterior ordering
- **AND** SHALL preserve backward compatibility with legacy DICOM viewers
- **AND** SHALL execute in O(1) constant time

#### Scenario: Literate documentation for coordinate transformation
- **GIVEN** the hook method implementation
- **WHEN** reading the source code
- **THEN** the docstring SHALL explain the mathematical basis for transformation
- **AND** SHALL include the formula: new_index = n - old_index for 0-based indexing
- **AND** SHALL document time complexity as O(1)
- **AND** SHALL provide a concrete example calculation
- **AND** SHALL explain WHY the transformation is needed (DICOM coordinate systems)

### Requirement: Code Duplication Elimination
The system SHALL eliminate duplicate code between parent and child builder classes through proper abstraction.

#### Scenario: Parent class method length reduction
- **GIVEN** the original 35-line get_mask_instance() method
- **WHEN** refactoring is applied
- **THEN** the main method body SHALL be reduced to ≤ 20 lines
- **AND** SHALL delegate to helper methods for single-responsibility operations
- **AND** SHALL maintain identical output for all test cases

#### Scenario: Child class method elimination
- **GIVEN** the child class NewReviewCMBPlatformJSONBuilder
- **WHEN** refactoring is applied
- **THEN** the duplicate get_mask_instance() method (lines 270-309) SHALL be deleted
- **AND** SHALL override only the _transform_main_seg_slice() hook method
- **AND** the child class implementation SHALL be ≤ 10 lines (hook override only)
- **AND** SHALL maintain identical output for all test cases

#### Scenario: Lines of code reduction verification
- **GIVEN** the refactored codebase
- **WHEN** measuring code lines for both classes
- **THEN** total lines SHALL be reduced from ~140 to ~80 lines
- **AND** code reduction percentage SHALL be ≥ 40%
- **AND** functional behavior SHALL remain unchanged

### Requirement: Helper Method Extraction
The system SHALL extract focused helper methods following Fowler's Extract Method refactoring pattern.

#### Scenario: Extract prediction data lookup
- **GIVEN** the inline filter operation for finding prediction data
- **WHEN** _find_prediction_data() helper is extracted
- **THEN** the method SHALL accept mask_index and pred_json_map parameters
- **AND** SHALL return Dict | None (prediction data or None)
- **AND** SHALL have a single responsibility: dictionary lookup
- **AND** SHALL be independently unit testable

#### Scenario: Extract DICOM dataset loading
- **GIVEN** the inline pydicom.dcmread() call
- **WHEN** _load_dicom_seg() helper is extracted
- **THEN** the method SHALL accept dcm_seg_path parameter
- **AND** SHALL return FileDataset object
- **AND** SHALL document I/O complexity in docstring
- **AND** SHALL be independently unit testable

#### Scenario: Extract mask instance dictionary building
- **GIVEN** the inline dict.update() operation with multiple fields
- **WHEN** _build_mask_instance_dict() helper is extracted
- **THEN** the method SHALL accept result, filter_cmd, dcm_seg, dicom_uid, source_images parameters
- **AND** SHALL return completed mask instance dictionary
- **AND** SHALL use the hook method for slice transformation
- **AND** SHALL be independently unit testable

### Requirement: Performance Optimization
The refactored system SHALL maintain or improve computational performance through algorithmic optimization.

#### Scenario: Algorithmic complexity improvement
- **GIVEN** the original O(n*m) nested iteration implementation
- **WHEN** refactoring is applied with dictionary optimization
- **THEN** the time complexity SHALL be O(n + m)
- **AND** for typical case (n=50, m=50): operations reduced from 2500 to 100
- **AND** performance improvement SHALL be measurable in benchmarks

#### Scenario: Memory overhead validation
- **GIVEN** the dictionary optimization requiring O(m) additional space
- **WHEN** m = 50 typical predictions
- **THEN** additional memory SHALL be < 10KB
- **AND** SHALL be negligible compared to total process memory (< 0.01%)
- **AND** SHALL not cause memory pressure or allocation issues

#### Scenario: Hook method call overhead
- **GIVEN** the polymorphic hook method call in loop
- **WHEN** profiling refactored implementation
- **THEN** method call overhead SHALL be < 1% of total runtime
- **AND** Python method dispatch SHALL add < 200 nanoseconds per call
- **AND** total overhead SHALL be unmeasurable in production context

### Requirement: Backward Compatibility
The refactored system SHALL maintain complete backward compatibility with existing API contracts.

#### Scenario: Public API signature preservation
- **GIVEN** existing code calling get_mask_instance()
- **WHEN** refactoring is applied
- **THEN** method signature SHALL remain unchanged
- **AND** parameter names, types, and order SHALL be identical
- **AND** return type SHALL remain List[MaskInstance]
- **AND** no caller code changes SHALL be required

#### Scenario: Output equivalence validation
- **GIVEN** test cases with known inputs and expected outputs
- **WHEN** comparing original vs refactored implementation outputs
- **THEN** outputs SHALL be byte-identical for all test cases
- **AND** DICOM-SEG file structure SHALL match exactly
- **AND** JSON metadata SHALL match exactly
- **AND** no regression in correctness SHALL be introduced

#### Scenario: Integration test preservation
- **GIVEN** existing integration tests for builder classes
- **WHEN** refactoring is complete
- **THEN** all existing tests SHALL pass without modification
- **AND** no test behavior changes SHALL be required
- **AND** test coverage SHALL remain ≥ 90%

### Requirement: Code Quality Standards
The refactored code SHALL adhere to Fowler's refactoring principles, Linus's "good taste", and Knuth's literate programming standards.

#### Scenario: Single Responsibility compliance (Fowler)
- **GIVEN** each extracted helper method
- **WHEN** reviewing method responsibilities
- **THEN** each method SHALL have exactly one reason to change
- **AND** method names SHALL clearly describe their single purpose
- **AND** no method SHALL exceed 15 lines of code

#### Scenario: Elimination of special cases (Linus "good taste")
- **GIVEN** the refactored implementation
- **WHEN** reviewing control flow logic
- **THEN** the code SHALL use polymorphic dispatch instead of conditionals
- **AND** SHALL eliminate nested filter/lambda special case syntax
- **AND** data structures (dictionary, hook) SHALL drive behavior
- **AND** no unnecessary complexity SHALL remain

#### Scenario: Literate documentation (Knuth)
- **GIVEN** any algorithmic component (hook method, optimization)
- **WHEN** reading the source code
- **THEN** docstrings SHALL explain the mathematical basis and WHY
- **AND** SHALL document time/space complexity using Big-O notation
- **AND** SHALL include concrete examples for clarity
- **AND** SHALL reference DICOM standards where applicable

#### Scenario: Static analysis compliance
- **GIVEN** the refactored codebase
- **WHEN** running static analysis tools
- **THEN** mypy SHALL report zero type errors
- **AND** pylint score SHALL be ≥ 9.0
- **AND** black formatting SHALL be applied consistently
- **AND** no unused imports or variables SHALL remain

### Requirement: Comprehensive Testing
The system SHALL include comprehensive unit and integration tests validating refactoring correctness.

#### Scenario: Unit test coverage for hook method
- **GIVEN** the _transform_main_seg_slice() hook method
- **WHEN** writing unit tests
- **THEN** tests SHALL cover default behavior (parent class)
- **AND** tests SHALL cover override behavior (child class)
- **AND** tests SHALL verify O(1) complexity (single operation)
- **AND** tests SHALL validate edge cases (empty list, single element)

#### Scenario: Unit test coverage for helper methods
- **GIVEN** extracted helper methods
- **WHEN** writing unit tests
- **THEN** each helper SHALL have ≥ 3 test cases
- **AND** tests SHALL cover success paths, failure paths, edge cases
- **AND** tests SHALL use mocks to isolate dependencies
- **AND** helper tests SHALL run independently of main method

#### Scenario: Integration test validation
- **GIVEN** the complete refactored pipeline
- **WHEN** running integration tests
- **THEN** tests SHALL validate end-to-end behavior with real data
- **AND** tests SHALL compare outputs against original implementation
- **AND** tests SHALL verify DICOM-SEG file correctness
- **AND** all existing integration tests SHALL pass without changes

#### Scenario: Code coverage requirement
- **GIVEN** the completed refactoring
- **WHEN** running coverage analysis
- **THEN** line coverage SHALL be ≥ 90% for modified methods
- **AND** branch coverage SHALL be ≥ 85%
- **AND** untested code paths SHALL be documented and justified
