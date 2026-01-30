# Change: Analyze and Generate Brain CMB Documentation

## Why
Current documentation for `brain-cmb` is insufficient for a system of such clinical importance. It lacks the "literate" quality that explains the *reasoning* behind the algorithms and architecture. Following Donald Knuth's philosophy, we must treat the code as literature, explaining the "why" and "how" with mathematical rigor and aesthetic clarity to ensure long-term maintainability and correctness.

## What Changes
- **Analysis**: Reverse-engineer the existing codebase (`src/brain_cmb`) to extract implicit requirements and design patterns.
- **Documentation**: Generate a suite of documents in `docs/brain-cmb/`:
    - **PRD (Product Requirements Document)**: Clinical context, user scenarios, and "The Why".
    - **SR (System Requirements)**: Strict I/O contracts, performance bounds, and "The What".
    - **SD (System Design)**: Algorithmic analysis, data flow, architecture, and "The How".
    - **Regulatory Compliance**: Map these documents to IEC 62304/62366 standards where applicable.
- **Specification**: Formalize the behavior in `specs/brain-cmb-pipeline/spec.md`.

## Impact
- **Affected Specs**: `brain-cmb-pipeline` (New).
- **Affected Docs**: `docs/brain-cmb/requirements/`, `docs/brain-cmb/architecture/`.
- **Affected Code**: None (Documentation only).
