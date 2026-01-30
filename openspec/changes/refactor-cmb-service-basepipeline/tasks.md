# Implementation Tasks

## 1. Extract ImageNormalizer Component
- [ ] 1.1 Create `src/brain_cmb/core/image_normalizer.py`
- [ ] 1.2 Extract `load_volume()`, `resize_volume()`, `custom_normalize_1()` as class methods
- [ ] 1.3 Write unit tests for each method with fixtures
- [ ] 1.4 Extract `load_synthseg_seg()` into normalizer
- [ ] 1.5 Validate against existing test cases (same outputs)

## 2. Extract SlidingWindowInferenceEngine Component
- [ ] 2.1 Create `src/brain_cmb/core/sliding_window_engine.py`
- [ ] 2.2 Extract `get_window_slices()`, `get_importance_kernel()` as initialization logic
- [ ] 2.3 Extract `sliding_window_inference()` as main `infer()` method
- [ ] 2.4 Write unit tests with mock TensorFlow models
- [ ] 2.5 Validate inference outputs match original implementation

## 3. Extract ObjectAnalyzer Component
- [ ] 3.1 Create `src/brain_cmb/core/object_analyzer.py`
- [ ] 3.2 Extract `get_watershed_label()`, `center_crop()` as utility methods
- [ ] 3.3 Extract `object_analysis()` as main analysis pipeline
- [ ] 3.4 Write unit tests with synthetic prediction maps
- [ ] 3.5 Validate analysis outputs (DataFrame structure, predictions)

## 4. Extract OutputFormatter Component
- [ ] 4.1 Create `src/brain_cmb/core/output_formatter.py`
- [ ] 4.2 Extract `save_nii_trio()` and `save_label_table()` as formatter methods
- [ ] 4.3 Write unit tests with temporary file fixtures
- [ ] 4.4 Validate NIfTI and JSON outputs match original format
- [ ] 4.5 Add validation for file permissions and error handling

## 5. Create Utility Module
- [ ] 5.1 Create `src/brain_cmb/core/cmb_utils.py`
- [ ] 5.2 Move pure functions: `get_histogram_xy()`, coordinate transforms
- [ ] 5.3 Document mathematical basis for each utility (Knuth literate style)
- [ ] 5.4 Write unit tests for mathematical correctness
- [ ] 5.5 Add complexity analysis comments (O notation)

## 6. Refactor CmbPipeline Integration
- [ ] 6.1 Update `CmbPipeline.__init__()` to instantiate components
- [ ] 6.2 Refactor `prepare()` to use ImageNormalizer
- [ ] 6.3 Refactor `run_inference()` to use SlidingWindowInferenceEngine
- [ ] 6.4 Refactor `postprocess()` to use ObjectAnalyzer + OutputFormatter
- [ ] 6.5 Ensure all existing integration tests pass

## 7. Create Backward-Compatible Wrapper
- [ ] 7.1 Keep `CMBServiceTF` class as thin wrapper delegating to components
- [ ] 7.2 Add deprecation warning to `cmb_classify()` method
- [ ] 7.3 Ensure old import path still works: `from brain_cmb.core.cmb import CMBServiceTF`
- [ ] 7.4 Update internal users to use new pipeline directly
- [ ] 7.5 Document migration path in docstrings

## 8. Comprehensive Testing
- [ ] 8.1 Write integration test covering full pipeline with real data
- [ ] 8.2 Add property-based tests for numerical stability
- [ ] 8.3 Test edge cases: empty images, single-voxel objects, extreme spacings
- [ ] 8.4 Performance regression test (confirm <1% overhead)
- [ ] 8.5 Test backward compatibility with old API

## 9. Documentation & Code Quality
- [ ] 9.1 Add module-level docstrings explaining Fowler's design patterns used
- [ ] 9.2 Add Knuth-style literate comments explaining mathematical foundations
- [ ] 9.3 Document complexity analysis for each component
- [ ] 9.4 Create architecture diagram showing component relationships
- [ ] 9.5 Update README with refactoring rationale and migration guide

## 10. Final Validation & Cleanup
- [ ] 10.1 Run full test suite (unit + integration + end-to-end)
- [ ] 10.2 Code coverage report (target: >90% for new modules)
- [ ] 10.3 Static analysis: mypy, pylint, black formatting
- [ ] 10.4 Performance benchmarking vs original implementation
- [ ] 10.5 Remove deprecated `CMBServiceTF` wrapper (after validation period)

---

**Dependencies:**
- Tasks 1-5 can be executed in parallel (independent extractions)
- Task 6 depends on Tasks 1-5 completion
- Task 7 depends on Task 6
- Tasks 8-10 depend on all previous tasks

**Estimated Effort:**
- Extraction (Tasks 1-5): 3-4 days
- Integration (Tasks 6-7): 2 days
- Testing & Quality (Tasks 8-10): 2-3 days
- **Total: 7-9 days**