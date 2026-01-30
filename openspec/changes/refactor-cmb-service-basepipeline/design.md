# Design: CMB Service Refactoring

## Context

CMBServiceTF is a 450+ line class that violates multiple software engineering principles:

**Current Issues (Fowler's Code Smells):**
- **Long Class**: 450+ lines with 20+ methods
- **Long Methods**: `cmb_classify()` (35 lines), `sliding_window_inference()` (40 lines)
- **Feature Envy**: Methods accessing more data from NumPy/TensorFlow than from self
- **Primitive Obsession**: Heavy use of path strings and array manipulations without domain objects

**Architectural Gaps:**
- No separation between algorithm (mathematical operations) and infrastructure (I/O, model loading)
- Difficult to test individual operations in isolation
- Hard to understand data flow without tracing through entire execution

**Knuth's Perspective:**
The current implementation lacks "literate" structure - readers must reverse-engineer the algorithm from code rather than reading a clear narrative of *why* each step exists.

## Goals / Non-Goals

### Goals
1. **Decompose into focused components** with clear single responsibilities (Fowler)
2. **Achieve literate program structure** where code reads as algorithm documentation (Knuth)
3. **Enable comprehensive testing** through dependency injection and mocking
4. **Preserve backward compatibility** - existing API unchanged
5. **Maintain or improve performance** - no algorithmic changes, only structural

### Non-Goals
1. NOT changing the ML model architecture or training process
2. NOT modifying the underlying algorithms (watershed, sliding window, etc.)
3. NOT adding new features or capabilities
4. NOT changing the external CLI interface

## Decisions

### Decision 1: Component Extraction Strategy

**What:** Extract four cohesive components from CMBServiceTF

**Why (Fowler):** Each extracted class has a single, testable responsibility:

```
ImageNormalizer
├─ load_volume()         # I/O + coordinate transformation
├─ resize_volume()       # Spatial resampling
└─ normalize()           # Intensity normalization

SlidingWindowInferenceEngine
├─ get_window_slices()   # Geometry calculation
├─ get_importance_kernel() # Gaussian weighting
└─ infer()               # Patch-based prediction

ObjectAnalyzer
├─ get_watershed_label() # Segmentation
├─ center_crop()         # ROI extraction
└─ classify_objects()    # Per-object classification

OutputFormatter
├─ save_nifti()          # Medical imaging output
└─ save_json()           # Structured results
```

**Why (Knuth):** Each component represents a mathematically coherent operation:
- `ImageNormalizer`: Linear transformations and interpolation theory
- `SlidingWindowInferenceEngine`: Discrete convolution with overlap-add method
- `ObjectAnalyzer`: Connected component analysis + statistical modeling
- `OutputFormatter`: Data serialization (no algorithmic complexity)

**Alternatives Considered:**
- **Partial extraction**: Only extract inference engine → Rejected: Still leaves 300+ line class
- **Functional decomposition**: Pure functions without classes → Rejected: Loses state encapsulation for model caching
- **Single refactoring**: One "CMBCore" class → Rejected: Violates single responsibility

### Decision 2: Integration with BasePipeline Template Method

**What:** Map extracted components to pipeline hooks:

```python
class CmbPipeline(BasePipeline):
    def prepare(self, payload):
        # Use ImageNormalizer
        normalized = self.normalizer.load_and_normalize(payload.swan_file)
        return PreparedData(normalized, payload.t1_template)

    def run_inference(self, prepared):
        # Use SlidingWindowInferenceEngine
        seg_map = self.seg_engine.infer(prepared.image, model1)
        return InferenceResult(seg_map, prepared.image)

    def postprocess(self, inference):
        # Use ObjectAnalyzer + OutputFormatter
        objects = self.analyzer.analyze(inference.seg_map)
        paths = self.formatter.save(objects)
        return OutputArtifacts(paths)
```

**Why (Fowler):**
- Template method is already established pattern in codebase
- Hooks provide natural seams for testing
- Reduces coupling between pipeline orchestration and domain logic

**Why (Knuth):**
- Creates literate narrative: "First we prepare, then we infer, then we post-process"
- Each hook represents a well-defined mathematical transformation
- Complexity is layered: High-level flow is trivial, details are in leaf components

### Decision 3: Dependency Injection for Testability

**What:** Components receive dependencies via constructor:

```python
class SlidingWindowInferenceEngine:
    def __init__(self, patch_size=(64,64,64), overlap=0.5, blend_mode="gaussian"):
        self.patch_size = patch_size
        self.overlap = overlap
        self.importance_kernel = self._build_kernel(blend_mode)

    def infer(self, volume, model):
        # No I/O, no global state - pure transformation
        ...
```

**Why (Fowler):**
- Enables unit testing without GPU or filesystem
- Makes dependencies explicit (better documentation)
- Facilitates future evolution (can inject different models)

**Why (Knuth):**
- Parameters are mathematical constants defining the algorithm
- Function signature documents preconditions
- Pure functions are easier to prove correct

### Decision 4: Preserve Existing Module-Level Functions

**What:** Keep `@classmethod` utilities as module-level pure functions:

```python
# Before (in CMBServiceTF)
@classmethod
def resize_volume(cls, arr, spacing=None, target_spacing=None, ...):
    ...

# After (in image_utils.py)
def resize_volume(arr, spacing=None, target_spacing=None, ...):
    ...
```

**Why (Fowler):**
- These are stateless utility functions, not class behavior
- Eliminates fake "service" class that's just a namespace
- Easier to import and reuse

**Why (Knuth):**
- Mathematical functions should be mathematical functions, not methods
- Clear signature documents algorithm inputs/outputs
- Easier to reason about correctness without class context

## Risks / Trade-offs

### Risk 1: Increased File Count
- **Current:** 1 file (`cmb.py`)
- **Proposed:** 5+ files (normalizer, engine, analyzer, formatter, utils)
- **Mitigation:**
  - Clear naming convention: `cmb_*.py` prefix
  - Single public API entry point preserved
  - Documentation explains module structure

### Risk 2: Performance Impact from Additional Abstraction
- **Concern:** Extra function calls and object creation
- **Analysis:**
  - Computation is dominated by TensorFlow model inference (seconds)
  - Python function call overhead is nanoseconds
  - Negligible impact (<0.1% of runtime)
- **Mitigation:** Profile before/after to confirm

### Risk 3: Breaking Changes to Internal Imports
- **Concern:** Other code might import `CMBServiceTF` directly
- **Analysis:**
  - Grep shows only `pipeline_cmb_tensorflow.py` imports it
  - That file is under our control
- **Mitigation:**
  - Provide backward-compatible import path:
    ```python
    # Old import still works
    from brain_cmb.core.cmb import CMBServiceTF  # Deprecated wrapper
    ```

## Migration Plan

### Phase 1: Extract Without Breaking (Week 1)
1. Create new modules alongside `cmb.py`
2. Extract one component at a time
3. Write unit tests for each
4. `CMBServiceTF` delegates to new components
5. Run integration tests - must pass

### Phase 2: Integrate with Pipeline (Week 2)
1. Refactor `CmbPipeline` to use extracted components
2. Remove delegation from `CMBServiceTF`
3. Add `CMBServiceTF` deprecation warning
4. Update documentation

### Phase 3: Complete Migration (Week 3)
1. Remove `CMBServiceTF` class (keep backward-compat import)
2. Clean up tests
3. Update all documentation
4. Performance benchmarking confirms no regression

### Rollback Strategy
- Each phase is atomic and reversible
- Git tag at each phase boundary
- If tests fail, revert phase commit
- Component extraction doesn't break existing code until Phase 2

## Open Questions

1. **Q:** Should we extract `label_index_name_mapping_dict` to a configuration file?
   **A (Deferred):** Keep as module constant for now. If it needs versioning, extract later.

2. **Q:** Should MODEL1_PATH and MODEL2_PATH be configurable per-instance?
   **A:** Yes - constructor parameters with environment variable defaults:
   ```python
   def __init__(self, model1_path=None, model2_path=None):
       self.model1_path = model1_path or os.getenv(...) or DEFAULT
   ```

3. **Q:** How do we handle TensorFlow session management across components?
   **A:** Components should be stateless w.r.t. TF. Models loaded once by pipeline, passed to components.