# Change: Refactor CMBServiceTF to Use pipelinecore BasePipeline Architecture

## Why

CMBServiceTF currently exists as a monolithic service class with 450+ lines mixing concerns:
- Model loading and inference logic
- Image processing operations
- File I/O and data transformations
- Statistical analysis and object detection

This violates Martin Fowler's Single Responsibility Principle and lacks the template method structure already established in `CmbPipeline`. The refactoring will:

1. **Improve Readability** (Fowler): Extract cohesive methods for human comprehension
2. **Enable Testability** (Fowler): Separate concerns allow isolated unit testing
3. **Achieve Elegance** (Knuth): Create mathematically clear data flow with proper abstraction layers
4. **Facilitate Evolution** (Fowler): Make future modifications safer through established patterns

## What Changes

- **Decompose CMBServiceTF**: Extract discrete responsibilities into focused classes:
  - `ImageNormalizer`: Handles volume normalization and preprocessing
  - `SlidingWindowInferenceEngine`: Manages patch-based model inference
  - `ObjectAnalyzer`: Performs watershed segmentation and object classification
  - `OutputFormatter`: Handles NIfTI and JSON output generation

- **Strengthen CmbPipeline**: Integrate extracted components into template method hooks:
  - `prepare()`: Input validation + preprocessing
  - `run_inference()`: Two-stage model execution (segmentation + classification)
  - `postprocess()`: Object analysis + output formatting

- **Preserve Public API**: Maintain `pipeline_cmb()` function signature for backward compatibility

- **Add Test Coverage**: Unit tests for each extracted component following self-testing code principles

## Impact

**Affected specs:**
- `cmb-pipeline`: New spec defining modular CMB processing architecture

**Affected code:**
- `src/brain_cmb/core/cmb.py`: Will be refactored into multiple focused modules
- `src/brain_cmb/pipeline_cmb_tensorflow.py`: Enhanced with better separation of concerns
- New test files under `tests/` for each component

**Breaking changes:** None - public API preserved

**Migration:** Transparent to existing consumers of `pipeline_cmb()`