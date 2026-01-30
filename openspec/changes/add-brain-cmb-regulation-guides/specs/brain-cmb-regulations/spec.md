## ADDED Requirements

### Requirement: brain-cmb 專案實作指南集
brain-cmb 專案 SHALL 建立一組具體的實作指南，包含品質管理、軟體生命週期、風險管理、可用性工程、資訊安全及 AI 風險管理，以引導開發團隊符合法規要求。

#### Scenario: 參考品質管理指南
- **WHEN** 開發團隊需要瞭解如何執行品質控制
- **THEN** SHALL 在 `docs/brain-cmb/regulations/ISO-13485-Quality-Management-Guide.md` 找到具體過程定義

#### Scenario: 確認軟體安全分類
- **WHEN** 進行軟體設計與開發規劃
- **THEN** SHALL 參考 `docs/brain-cmb/regulations/IEC-62304-Software-Safety-Classification.md` 中的分類依據

#### Scenario: 執行 AI 風險分析
- **WHEN** 針對腦部微出血偵測模型進行風險評估
- **THEN** SHALL 使用 `docs/brain-cmb/regulations/ISO-14971-Risk-Analysis-Report.md` 範本並遵循 `ISO-IEC-23894-AI-Risk-Management-Guide.md`

### Requirement: 完善的法規索引導覽
brain-cmb 專案 SHALL 在索引文件中提供對照表與實作指南之間的清晰連結。

#### Scenario: 查詢特定標準的指南
- **WHEN** 使用者在 `00_REGULATIONS_INDEX.md` 中查看某一標準（如 ISO 14971）
- **THEN** 索引表 SHALL 同時列出其合規性對照表與對應的過程指南文件

