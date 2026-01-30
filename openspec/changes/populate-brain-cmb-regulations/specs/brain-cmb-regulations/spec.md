## ADDED Requirements

### Requirement: brain-cmb 專案合規性文檔集
brain-cmb 專案 SHALL 建立一組完整的合規性證明文檔，涵蓋 ISO 13485, IEC 62304, ISO 14971, IEC 62366, ISO 27001 與 ISO/IEC 23894 標準。

#### Scenario: 建立 ISO 13485 合規性文件
- **WHEN** 專案需要證明符合品質管理系統要求
- **THEN** SHALL 在 `docs/brain-cmb/regulations/ISO-13485-Compliance-Mapping.md` 找到對應的對照表

#### Scenario: 建立 IEC 62304 合規性文件
- **WHEN** 專案需要證明符合軟體生命週期要求
- **THEN** SHALL 在 `docs/brain-cmb/regulations/IEC-62304-Compliance-Mapping.md` 找到對應的對照表

#### Scenario: 建立 ISO 14971 合規性文件
- **WHEN** 專案需要證明符合風險管理要求
- **THEN** SHALL 在 `docs/brain-cmb/regulations/ISO-14971-Compliance-Mapping.md` 找到對應的對照表

#### Scenario: 建立 IEC 62366 合規性文件
- **WHEN** 專案需要證明符合可用性工程要求
- **THEN** SHALL 在 `docs/brain-cmb/regulations/IEC-62366-Compliance-Mapping.md` 找到對應的對照表

#### Scenario: 建立 ISO 27001 合規性文件
- **WHEN** 專案需要證明符合資訊安全要求
- **THEN** SHALL 在 `docs/brain-cmb/regulations/ISO-27001-Compliance-Mapping.md` 找到對應的對照表

#### Scenario: 建立 ISO/IEC 23894 合規性文件
- **WHEN** 專案需要證明符合 AI 風險管理要求
- **THEN** SHALL 在 `docs/brain-cmb/regulations/ISO-IEC-23894-Compliance-Mapping.md` 找到對應的對照表

### Requirement: 專案合規性索引自動化管理
brain-cmb 專案 SHALL 在 `docs/brain-cmb/regulations/00_REGULATIONS_INDEX.md` 中維護一份最新的合規性文檔清單。

#### Scenario: 更新文檔清單
- **WHEN** 新的合規性文檔被建立
- **THEN** SHALL 同步更新索引文件中的「文檔清單」章節，包含文檔 ID、標題、版本與狀態

