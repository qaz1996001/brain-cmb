# Design: RFC 2119 Integration

## Context
RFC 2119 is a technical specification that defines keywords for use in other specifications. In the context of this meta-framework, it serves as the foundational language for all requirements.

## Decisions

### 1. Standard Keyword Definitions
The guide will strictly follow RFC 2119 definitions:
- **MUST / SHALL**: Absolute requirement.
- **MUST NOT / SHALL NOT**: Absolute prohibition.
- **SHOULD**: Recommended, but valid reasons may exist to ignore.
- **SHOULD NOT**: Recommended against, but valid reasons may exist.
- **MAY**: Optional.

### 2. Integration with ISO/IEC/IEEE 29148
RFC 2119 keywords will be the primary mechanism for satisfying the "unambiguous" and "singular" attributes required by 29148.

### 3. Implementation in Templates
All requirement templates will be updated to include a standard RFC 2119 boilerplate section.

## Risks
- Overuse of "MUST" can lead to over-engineering.
- Misunderstanding "SHOULD" as "MAY" by junior developers or AI.

