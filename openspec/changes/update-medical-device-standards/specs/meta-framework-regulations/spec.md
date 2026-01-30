## ADDED Requirements

### Requirement: 支援醫療器材品質管理系統標準（ISO 13485）
元框架 SHALL 提供 ISO 13485 醫療器材品質管理系統的合規性範本與指南，以支援醫療器材軟體專案的品質管理需求。

#### Scenario: 專案需要 ISO 13485 合規性範本
- **WHEN** 專案需要建立 ISO 13485 合規性證明文件
- **THEN** 可在 `docs/meta-framework/regulations/ISO-13485/` 找到合規性對照範本與品質管理指南

### Requirement: 支援醫療器材軟體生命週期標準（IEC 62304）
元框架 SHALL 提供 IEC 62304 醫療器材軟體生命週期流程的合規性範本與指南，包括軟體安全分類、軟體生命週期流程、軟體維護等要求。

#### Scenario: 專案需要 IEC 62304 合規性範本
- **WHEN** 專案需要建立 IEC 62304 合規性證明文件
- **THEN** 可在 `docs/meta-framework/regulations/IEC-62304/` 找到合規性對照範本、軟體生命週期範本與安全分類指南

### Requirement: 支援醫療器材風險管理標準（ISO 14971）
元框架 SHALL 提供 ISO 14971 醫療器材風險管理的合規性範本與指南，包括風險分析、風險評估、風險控制措施等要求。

#### Scenario: 專案需要 ISO 14971 風險管理範本
- **WHEN** 專案需要建立 ISO 14971 風險管理文件
- **THEN** 可在 `docs/meta-framework/regulations/ISO-14971/` 找到合規性對照範本、風險管理流程指南與風險分析範本

### Requirement: 支援醫療器材可用性工程標準（IEC 62366）
元框架 SHALL 提供 IEC 62366 醫療器材可用性工程的合規性範本與指南，以支援使用者介面設計與可用性測試。

#### Scenario: 專案需要 IEC 62366 可用性工程範本
- **WHEN** 專案需要建立 IEC 62366 可用性工程文件
- **THEN** 可在 `docs/meta-framework/regulations/IEC-62366/` 找到合規性對照範本與可用性工程流程指南

### Requirement: 支援資訊安全管理系統標準（ISO 27001）
元框架 SHALL 提供 ISO 27001 資訊安全管理系統的合規性範本與指南，以支援處理敏感醫療資料的專案。

#### Scenario: 專案需要 ISO 27001 資訊安全管理範本
- **WHEN** 專案需要建立 ISO 27001 資訊安全管理文件
- **THEN** 可在 `docs/meta-framework/regulations/ISO-27001/` 找到合規性對照範本與資訊安全管理指南

### Requirement: 支援 AI 風險管理標準（ISO/IEC 23894）
元框架 SHALL 提供 ISO/IEC 23894 AI 風險管理的合規性範本與指南，以支援使用 AI/ML 技術的醫療器材軟體專案。

#### Scenario: 專案需要 ISO/IEC 23894 AI 風險管理範本
- **WHEN** 專案需要建立 ISO/IEC 23894 AI 風險管理文件
- **THEN** 可在 `docs/meta-framework/regulations/ISO-IEC-23894/` 找到合規性對照範本與 AI 風險管理指南

### Requirement: brain-cmb 專案文件管理系統
brain-cmb 專案 SHALL 擁有獨立的文件管理系統，包含需求文檔、設計文檔、追溯性文檔、合規性文檔與測試文檔目錄，以支援符合醫療器材標準的開發流程。

#### Scenario: 專案需要建立需求文檔
- **WHEN** 專案需要建立需求文檔
- **THEN** 可在 `docs/brain-cmb/requirements/` 目錄建立與管理需求文檔

#### Scenario: 專案需要建立設計文檔
- **WHEN** 專案需要建立設計文檔
- **THEN** 可在 `docs/brain-cmb/design/` 目錄建立與管理設計文檔

#### Scenario: 專案需要建立追溯性文檔
- **WHEN** 專案需要建立追溯性矩陣
- **THEN** 可在 `docs/brain-cmb/traceability/` 目錄建立與管理追溯性文檔

#### Scenario: 專案需要建立合規性文檔
- **WHEN** 專案需要建立合規性證明文件
- **THEN** 可在 `docs/brain-cmb/compliance/` 目錄建立與管理合規性文檔

#### Scenario: 專案需要建立測試文檔
- **WHEN** 專案需要建立測試計劃與測試報告
- **THEN** 可在 `docs/brain-cmb/testing/` 目錄建立與管理測試文檔

## MODIFIED Requirements

### Requirement: 規範與合規性文檔索引
元框架 SHALL 在 `docs/meta-framework/regulations/00_REGULATIONS_INDEX.md` 中提供所有支援標準的索引，包括 ISO 13485、IEC 62304、ISO 14971、IEC 62366、ISO 27001、ISO/IEC 23894 等醫療器材與資訊安全標準，以及 ISO/IEC/IEEE 29148 需求工程標準。

#### Scenario: 使用者查詢支援的標準
- **WHEN** 使用者查詢元框架支援的標準
- **THEN** 可在 `docs/meta-framework/regulations/00_REGULATIONS_INDEX.md` 找到完整的標準列表與說明

#### Scenario: 使用者選擇適用標準
- **WHEN** 使用者需要選擇適用於醫療器材軟體專案的標準
- **THEN** 索引文件提供標準選擇指南與適用領域說明

