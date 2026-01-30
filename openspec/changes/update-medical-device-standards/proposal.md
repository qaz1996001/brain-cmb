# Change: 更新元框架標準為醫療器材與資訊安全標準

## Why

現有的 `docs/meta-framework` 框架目前支援 ISO/IEC/IEEE 29148（需求工程）和 ISO 20816（機械振動監測）標準，但 brain-cmb 專案需要符合醫療器材軟體開發的國際標準要求。根據醫療器材軟體開發的最佳實踐，需要導入以下標準：

- **ISO 13485**：醫療器材品質管理系統
- **IEC 62304**：醫療器材軟體生命週期流程
- **ISO 14971**：醫療器材風險管理
- **IEC 62366**：醫療器材可用性工程
- **ISO 27001**：資訊安全管理系統（處理敏感醫療資料）
- **ISO/IEC 23894**：AI 風險管理（適用於 AI/ML 醫療軟體）

同時需要在 `docs/brain-cmb` 建立專案專屬的文件管理系統，以支援符合標準的開發流程。

## What Changes

- **MODIFIED**: `docs/meta-framework/regulations/00_REGULATIONS_INDEX.md` - 更新標準索引，移除 ISO-20816，新增醫療器材標準
- **MODIFIED**: `docs/meta-framework/00_METAFRAMEWORK_INDEX.md` - 更新標準合規性章節
- **MODIFIED**: `docs/meta-framework/01_FRAMEWORK_OVERVIEW.md` - 更新標準支援說明
- **MODIFIED**: `docs/meta-framework/README.md` - 更新標準列表
- **ADDED**: `docs/meta-framework/regulations/ISO-13485/` - ISO 13485 合規性範本目錄
- **ADDED**: `docs/meta-framework/regulations/IEC-62304/` - IEC 62304 合規性範本目錄
- **ADDED**: `docs/meta-framework/regulations/ISO-14971/` - ISO 14971 合規性範本目錄
- **ADDED**: `docs/meta-framework/regulations/IEC-62366/` - IEC 62366 合規性範本目錄
- **ADDED**: `docs/meta-framework/regulations/ISO-27001/` - ISO 27001 合規性範本目錄
- **ADDED**: `docs/meta-framework/regulations/ISO-IEC-23894/` - ISO/IEC 23894 合規性範本目錄
- **ADDED**: `docs/brain-cmb/` - brain-cmb 專案文件管理系統根目錄
- **ADDED**: `docs/brain-cmb/README.md` - brain-cmb 文件管理系統說明
- **ADDED**: `docs/brain-cmb/requirements/` - 需求文檔目錄
- **ADDED**: `docs/brain-cmb/design/` - 設計文檔目錄
- **ADDED**: `docs/brain-cmb/traceability/` - 追溯性文檔目錄
- **ADDED**: `docs/brain-cmb/compliance/` - 合規性文檔目錄
- **ADDED**: `docs/brain-cmb/testing/` - 測試文檔目錄

## Impact

- **Affected specs**: `meta-framework-regulations`（新增 capability）
- **Affected code**: 無（僅文檔變更）
- **Affected docs**: 
  - `docs/meta-framework/regulations/` 目錄結構重組
  - `docs/meta-framework/` 多個索引文件更新
  - `docs/brain-cmb/` 新建文件管理系統
- **Breaking changes**: 無（向後相容，舊標準範本可保留供參考）

## Notes

- ISO/IEC/IEEE 29148 標準範本保留（仍為通用需求工程標準）
- ISO-20816 標準範本可移至 archive 或保留供參考
- 新標準範本將遵循現有範本結構（compliance-mapping-template.md, traceability-guide.md 等）
- brain-cmb 文件管理系統將與 OpenSpec 變更管理系統整合

