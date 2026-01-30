# Change: 完善 brain-cmb 專案的標準合規性文檔

## Why

目前 `docs/brain-cmb/regulations/` 目錄僅包含一個索引文件，缺乏實際的合規性證明文檔。為了符合醫療器材軟體開發的要求（如 ISO 13485, IEC 62304 等），需要根據 `docs/meta-framework/regulations/` 中的範本，為 brain-cmb 專案建立具體的合規性對照表與指南。

## What Changes

- **ADDED**: `docs/brain-cmb/regulations/ISO-13485-Compliance-Mapping.md` - ISO 13485 合規性對照表
- **ADDED**: `docs/brain-cmb/regulations/IEC-62304-Compliance-Mapping.md` - IEC 62304 合規性對照表
- **ADDED**: `docs/brain-cmb/regulations/ISO-14971-Compliance-Mapping.md` - ISO 14971 合規性對照表
- **ADDED**: `docs/brain-cmb/regulations/IEC-62366-Compliance-Mapping.md` - IEC 62366 合規性對照表
- **ADDED**: `docs/brain-cmb/regulations/ISO-27001-Compliance-Mapping.md` - ISO 27001 合規性對照表
- **ADDED**: `docs/brain-cmb/regulations/ISO-IEC-23894-Compliance-Mapping.md` - ISO/IEC 23894 合規性對照表
- **MODIFIED**: `docs/brain-cmb/regulations/00_REGULATIONS_INDEX.md` - 更新文檔清單，納入上述新建立的合規性文檔

## Impact

- **Affected specs**: `brain-cmb-regulations` (新能力)
- **Affected code**: 無（僅文檔變更）
- **Affected docs**: 
  - `docs/brain-cmb/regulations/` 目錄內容擴充
  - `docs/brain-cmb/regulations/00_REGULATIONS_INDEX.md` 內容更新

