# Proposal: Add RFC 2119 Requirement Keywords Regulation

## Why
RFC 2119 provides standardized terminology (MUST, SHOULD, MAY, etc.) for defining requirement levels. Incorporating this into the meta-framework ensures that all requirement documents (PRD, SR, SD) are unambiguous and consistent, which is critical for both human understanding and AI execution, as well as for compliance with higher-level standards like ISO/IEC/IEEE 29148.

## What Changes
- Add RFC 2119 regulation directory and guide in `docs/meta-framework/regulations/RFC-2119/`.
- Update `docs/meta-framework/regulations/00_REGULATIONS_INDEX.md` to include RFC 2119.
- Update `docs/brain-cmb/regulations/00_REGULATIONS_INDEX.md` to reference RFC 2119.
- Create project-specific RFC 2119 compliance document in `docs/brain-cmb/regulations/`.

## Impact
- **Specs**: Updates meta-framework regulation spec.
- **Docs**: New guidance and updated indexes.
- **Process**: Developers and AI will use standardized keywords in all future requirement updates.

