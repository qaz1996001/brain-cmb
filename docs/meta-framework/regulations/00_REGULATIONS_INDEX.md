# 規範與合規性文檔索引（Regulations and Compliance Index）

**文件 ID**: REG-META-001  
**標題**: 元框架規範與合規性文檔索引  
**版本**: v1.0.0  
**狀態**: Stable  
**建立日期**: 2025-12-22  

---

## 1. 目的與範圍（Purpose and Scope）

本目錄 (`docs/meta-framework/regulations/`) 提供**通用的標準合規性範本**，幫助專案符合國際醫療器材軟體開發與資訊安全管理的標準要求。

### 1.1 適用標準

本框架主要參考以下國際標準：

| 標準 | 全稱 | 適用領域 | 本框架支援 |
|------|------|---------|-----------|
| **ISO/IEC/IEEE 29148:2018** | Systems and software engineering — Requirements engineering | 需求工程 | ✅ 完整支援 |
| **ISO 13485:2016** | Medical devices — Quality management systems | 醫療器材品質管理系統 | ✅ 完整支援 |
| **IEC 62304:2006+AMD1:2015** | Medical device software — Software life cycle processes | 醫療器材軟體生命週期流程 | ✅ 完整支援 |
| **ISO 14971:2019** | Medical devices — Application of risk management to medical devices | 醫療器材風險管理 | ✅ 完整支援 |
| **IEC 62366-1:2015** | Medical devices — Part 1: Application of usability engineering to medical devices | 醫療器材可用性工程 | ✅ 完整支援 |
| **ISO/IEC 27001:2022** | Information security management systems — Requirements | 資訊安全管理系統 | ✅ 完整支援 |
| **ISO/IEC 23894:2023** | Information technology — Artificial intelligence — Guidance on risk management | AI 風險管理 | ✅ 完整支援 |

---

## 2. 文檔結構（Document Structure）

```
regulations/
├── 00_REGULATIONS_INDEX.md                 # 本文件
├── ISO-IEC-IEEE-29148/                     # 需求工程標準（通用）
│   ├── compliance-mapping-template.md      # 合規性對照範本
│   ├── requirements-quality-checklist.md   # 需求品質檢查清單
│   └── stakeholder-requirements-guide.md   # 利害關係人需求指南
├── ISO-13485/                              # 醫療器材品質管理系統
│   ├── compliance-mapping-template.md      # 合規性對照範本
│   └── quality-management-guide.md         # 品質管理指南
├── IEC-62304/                              # 醫療器材軟體生命週期
│   ├── compliance-mapping-template.md      # 合規性對照範本
│   ├── software-lifecycle-template.md      # 軟體生命週期範本
│   └── software-safety-classification-guide.md  # 軟體安全分類指南
├── ISO-14971/                             # 醫療器材風險管理
│   ├── compliance-mapping-template.md      # 合規性對照範本
│   ├── risk-management-process-guide.md    # 風險管理流程指南
│   └── risk-analysis-template.md           # 風險分析範本
├── IEC-62366/                             # 醫療器材可用性工程
│   ├── compliance-mapping-template.md      # 合規性對照範本
│   └── usability-engineering-process-guide.md  # 可用性工程流程指南
├── ISO-27001/                             # 資訊安全管理系統
│   ├── compliance-mapping-template.md      # 合規性對照範本
│   └── information-security-management-guide.md  # 資訊安全管理指南
├── ISO-IEC-23894/                         # AI 風險管理
│   ├── compliance-mapping-template.md      # 合規性對照範本
│   └── ai-risk-management-guide.md          # AI 風險管理指南
└── RFC-2119/                               # 需求關鍵字規範
    ├── requirement-keywords-guide.md       # 需求關鍵字指南
    └── compliance-checklist.md             # 合規性檢查清單
```

---

## 3. ISO/IEC/IEEE 29148:2018（需求工程）

### 3.1 標準概述

**ISO/IEC/IEEE 29148:2018** 規範需求工程的流程（獲取、分析、規格）與需求文件的品質標準。此標準為通用需求工程標準，適用於所有類型的軟體專案。

**關鍵要求**：
- **Stakeholder Requirements**：利害關係人需求（StRS）
- **System Requirements Specification**：系統需求規格（SyRS）
- **Software Requirements Specification**：軟體需求規格（SRS）
- **Requirements Traceability**：需求追溯性
- **Requirements Quality Attributes**：需求品質屬性（完整性、一致性、可驗證性等）

### 3.2 本框架的對應

| 標準要求 | 本框架對應 | 文檔位置 |
|---------|-----------|---------|
| Stakeholder Requirements (StRS) | 使用者需求（UR-xxx） | `requirements/TEMPLATE_SYSTEM_PRD_SR_SD.md` § 3 |
| System Requirements (SyRS) | 系統需求（SYS-SR-xxx） | `requirements/TEMPLATE_SYSTEM_PRD_SR_SD.md` § 4 |
| Software Requirements (SRS) | 子系統需求（FE-SR-xxx, BE-SR-xxx） | `requirements/TEMPLATE_SUBSYSTEM_PRD_SR_SD.md` |
| Traceability | 追溯矩陣（Traceability Matrix） | `requirements/TEMPLATE_SYSTEM_PRD_SR_SD.md` § 6 |
| Quality Attributes | 需求品質檢查清單 | `regulations/ISO-IEC-IEEE-29148/requirements-quality-checklist.md` |

### 3.3 範本與指南

- [`compliance-mapping-template.md`](ISO-IEC-IEEE-29148/compliance-mapping-template.md)
  - 合規性對照範本：如何證明符合標準要求
- [`requirements-quality-checklist.md`](ISO-IEC-IEEE-29148/requirements-quality-checklist.md)
  - 需求品質檢查清單：自我審查用
- [`stakeholder-requirements-guide.md`](ISO-IEC-IEEE-29148/stakeholder-requirements-guide.md)
  - 利害關係人需求撰寫指南

---

## 4. ISO 13485:2016（醫療器材品質管理系統）

### 4.1 標準概述

**ISO 13485:2016** 規範醫療器材品質管理系統的要求，確保醫療器材在整個生命週期內符合法規要求與客戶需求。

**關鍵要求**：
- **Quality Management System**：品質管理系統建立與維護
- **Management Responsibility**：管理階層責任
- **Resource Management**：資源管理
- **Product Realization**：產品實現（設計開發、採購、生產）
- **Measurement, Analysis and Improvement**：量測、分析與改進
- **Documentation Control**：文檔控制
- **Risk Management Integration**：風險管理整合（與 ISO 14971 整合）

### 4.2 本框架的對應

| 標準要求 | 本框架對應 | 文檔位置 |
|---------|-----------|---------|
| Quality Management System | 元框架文檔結構 + OpenSpec 變更管理 | `docs/meta-framework/` + `openspec/` |
| Documentation Control | 文檔版本控制與追溯性 | `requirements/`, `design/`, `traceability/` |
| Design and Development | PRD/SR/SD 文檔 + 設計文檔 | `requirements/TEMPLATE_SYSTEM_PRD_SR_SD.md` |
| Risk Management | ISO 14971 風險管理流程 | `regulations/ISO-14971/` |
| Validation and Verification | 測試文檔與驗證記錄 | `testing/` |

### 4.3 範本與指南

- [`compliance-mapping-template.md`](ISO-13485/compliance-mapping-template.md)
  - 合規性對照範本：如何證明符合 ISO 13485 要求
- [`quality-management-guide.md`](ISO-13485/quality-management-guide.md)
  - 品質管理指南：品質管理系統建立與維護

---

## 5. IEC 62304:2006+AMD1:2015（醫療器材軟體生命週期）

### 5.1 標準概述

**IEC 62304** 規範醫療器材軟體的開發、維護與風險管理流程，定義軟體生命週期的活動與文檔要求。

**關鍵要求**：
- **Software Safety Classification**：軟體安全分類（Class A/B/C）
- **Software Development Process**：軟體開發流程
- **Software Maintenance**：軟體維護流程
- **Software Risk Management**：軟體風險管理（與 ISO 14971 整合）
- **Software Configuration Management**：軟體組態管理
- **Software Problem Resolution**：軟體問題解決流程
- **Documentation Requirements**：文檔要求（SRS, SDD, Test Reports）

### 5.2 本框架的對應

| 標準要求 | 本框架對應 | 文檔位置 |
|---------|-----------|---------|
| Software Safety Classification | 軟體安全分類指南 | `regulations/IEC-62304/software-safety-classification-guide.md` |
| Software Development Process | PRD/SR/SD + 設計文檔 | `requirements/`, `design/` |
| Software Maintenance | OpenSpec 變更管理 | `openspec/changes/` |
| Software Risk Management | ISO 14971 風險管理 | `regulations/ISO-14971/` |
| Software Configuration Management | Git + OpenSpec | `openspec-integration/00_OPENSPEC_INTEGRATION.md` |
| Documentation Requirements | 完整文檔結構 | `docs/brain-cmb/` |

### 5.3 範本與指南

- [`compliance-mapping-template.md`](IEC-62304/compliance-mapping-template.md)
  - 合規性對照範本：如何證明符合 IEC 62304 要求
- [`software-lifecycle-template.md`](IEC-62304/software-lifecycle-template.md)
  - 軟體生命週期範本：開發、維護、問題解決流程
- [`software-safety-classification-guide.md`](IEC-62304/software-safety-classification-guide.md)
  - 軟體安全分類指南：Class A/B/C 分類標準與要求

---

## 6. ISO 14971:2019（醫療器材風險管理）

### 6.1 標準概述

**ISO 14971:2019** 提供醫療器材風險管理的框架，規範風險分析、風險評估、風險控制與風險監控的流程。

**關鍵要求**：
- **Risk Management Process**：風險管理流程
- **Risk Analysis**：風險分析（危害識別、危害情境、風險估計）
- **Risk Evaluation**：風險評估（風險可接受性判斷）
- **Risk Control**：風險控制（風險控制措施、剩餘風險評估）
- **Risk Management Review**：風險管理審查
- **Production and Post-Production Activities**：生產與上市後活動

### 6.2 本框架的對應

| 標準要求 | 本框架對應 | 文檔位置 |
|---------|-----------|---------|
| Risk Management Process | 風險管理流程指南 | `regulations/ISO-14971/risk-management-process-guide.md` |
| Risk Analysis | 風險分析範本 | `regulations/ISO-14971/risk-analysis-template.md` |
| Risk Control | 風險控制措施追溯 | `traceability/` + 需求文檔 |
| Risk Management Review | 合規性審計 | `compliance/` |

### 6.3 範本與指南

- [`compliance-mapping-template.md`](ISO-14971/compliance-mapping-template.md)
  - 合規性對照範本：如何證明符合 ISO 14971 要求
- [`risk-management-process-guide.md`](ISO-14971/risk-management-process-guide.md)
  - 風險管理流程指南：風險管理活動與文檔要求
- [`risk-analysis-template.md`](ISO-14971/risk-analysis-template.md)
  - 風險分析範本：危害識別、風險估計、風險控制措施

---

## 7. IEC 62366-1:2015（醫療器材可用性工程）

### 7.1 標準概述

**IEC 62366-1:2015** 規範醫療器材可用性工程的流程，確保醫療器材的使用者介面設計符合可用性要求，降低使用錯誤風險。

**關鍵要求**：
- **Usability Engineering Process**：可用性工程流程
- **User Interface Specification**：使用者介面規格
- **Usability Testing**：可用性測試
- **Use Error Risk Management**：使用錯誤風險管理（與 ISO 14971 整合）
- **Usability Engineering File**：可用性工程檔案

### 7.2 本框架的對應

| 標準要求 | 本框架對應 | 文檔位置 |
|---------|-----------|---------|
| Usability Engineering Process | 可用性工程流程指南 | `regulations/IEC-62366/usability-engineering-process-guide.md` |
| User Interface Specification | UI/UX 設計文檔 | `design/` |
| Usability Testing | 可用性測試報告 | `testing/` |
| Use Error Risk Management | ISO 14971 風險管理 | `regulations/ISO-14971/` |

### 7.3 範本與指南

- [`compliance-mapping-template.md`](IEC-62366/compliance-mapping-template.md)
  - 合規性對照範本：如何證明符合 IEC 62366 要求
- [`usability-engineering-process-guide.md`](IEC-62366/usability-engineering-process-guide.md)
  - 可用性工程流程指南：可用性工程活動與文檔要求

---

## 8. ISO/IEC 27001:2022（資訊安全管理系統）

### 8.1 標準概述

**ISO/IEC 27001:2022** 規範資訊安全管理系統（ISMS）的要求，確保組織的資訊資產得到適當保護，適用於處理敏感醫療資料的專案。

**關鍵要求**：
- **Information Security Management System**：資訊安全管理系統建立與維護
- **Risk Assessment and Treatment**：風險評估與處理
- **Security Controls**：安全控制措施（93 項控制措施）
- **Continuous Improvement**：持續改進
- **Documentation Requirements**：文檔要求

### 8.2 本框架的對應

| 標準要求 | 本框架對應 | 文檔位置 |
|---------|-----------|---------|
| ISMS Establishment | 資訊安全管理指南 | `regulations/ISO-27001/information-security-management-guide.md` |
| Risk Assessment | ISO 14971 風險管理 + 資訊安全風險 | `regulations/ISO-14971/` + `regulations/ISO-27001/` |
| Security Controls | 安全控制措施文檔 | `compliance/` |
| Documentation | 文檔管理系統 | `docs/brain-cmb/` |

### 8.3 範本與指南

- [`compliance-mapping-template.md`](ISO-27001/compliance-mapping-template.md)
  - 合規性對照範本：如何證明符合 ISO 27001 要求
- [`information-security-management-guide.md`](ISO-27001/information-security-management-guide.md)
  - 資訊安全管理指南：ISMS 建立與維護

---

## 9. ISO/IEC 23894:2023（AI 風險管理）

### 9.1 標準概述

**ISO/IEC 23894:2023** 提供 AI 系統風險管理的指南，適用於使用 AI/ML 技術的醫療器材軟體專案。

**關鍵要求**：
- **AI Risk Management Process**：AI 風險管理流程
- **AI Risk Identification**：AI 風險識別（偏見、透明度、可解釋性等）
- **AI Risk Assessment**：AI 風險評估
- **AI Risk Treatment**：AI 風險處理
- **AI Risk Monitoring**：AI 風險監控

### 9.2 本框架的對應

| 標準要求 | 本框架對應 | 文檔位置 |
|---------|-----------|---------|
| AI Risk Management Process | AI 風險管理指南 | `regulations/ISO-IEC-23894/ai-risk-management-guide.md` |
| AI Risk Identification | AI 風險分析文檔 | `compliance/` |
| AI Risk Assessment | ISO 14971 風險管理 + AI 特定風險 | `regulations/ISO-14971/` + `regulations/ISO-IEC-23894/` |

### 9.3 範本與指南

- [`compliance-mapping-template.md`](ISO-IEC-23894/compliance-mapping-template.md)
  - 合規性對照範本：如何證明符合 ISO/IEC 23894 要求
- [`ai-risk-management-guide.md`](ISO-IEC-23894/ai-risk-management-guide.md)
  - AI 風險管理指南：AI 風險管理活動與文檔要求

---

## 10. RFC 2119（需求關鍵字規範）

### 10.1 標準概述

**RFC 2119** 定義了一組用於表示需求層級的關鍵字（MUST, SHOULD, MAY 等）。這是確保需求無歧義、可測試的基礎語言規範。

### 10.2 本框架的對應

| 關鍵字 | 意義 | 使用情境 |
|-------|------|---------|
| MUST / SHALL | 絕對要求 | 核心功能、安全要求、法規要求 |
| SHOULD | 推薦做法 | 最佳實踐、優化項、非核心功能 |
| MAY | 完全可選 | 擴充功能、UI 裝飾、使用者偏好 |

### 10.3 範本與指南

- [`requirement-keywords-guide.md`](RFC-2119/requirement-keywords-guide.md)
  - 定義關鍵字與使用語境
- [`compliance-checklist.md`](RFC-2119/compliance-checklist.md)
  - 需求撰寫自我檢查清單

---

## 11. 如何使用本框架達成合規（How to Achieve Compliance）

### 11.1 選擇適用標準

**步驟 1：識別專案性質**

| 專案類型 | 建議標準 |
|---------|---------|
| 一般軟體專案 | ISO/IEC/IEEE 29148（需求工程）+ RFC 2119 |
| 醫療器材軟體（Class A） | IEC 62304 + ISO 13485 + ISO 14971 + RFC 2119 |
| 醫療器材軟體（Class B） | IEC 62304 + ISO 13485 + ISO 14971 + IEC 62366 + RFC 2119 |
| 醫療器材軟體（Class C） | IEC 62304 + ISO 13485 + ISO 14971 + IEC 62366 + ISO 27001 + RFC 2119 |
| AI/ML 醫療器材軟體 | 上述標準 + ISO/IEC 23894 |
| 處理敏感資料的醫療軟體 | 上述標準 + ISO 27001 |

**步驟 2：複製對應範本**

```bash
# 範例：醫療器材軟體專案（Class B）
cp docs/meta-framework/regulations/IEC-62304/compliance-mapping-template.md \
   <your-project>/docs/regulations/IEC-62304-compliance.md

cp docs/meta-framework/regulations/ISO-14971/risk-analysis-template.md \
   <your-project>/docs/regulations/risk-analysis.md

cp docs/meta-framework/regulations/RFC-2119/compliance-checklist.md \
   <your-project>/docs/regulations/RFC-2119-compliance.md
```

**步驟 3：填寫合規性對照表**

在 `compliance-mapping-template.md` 中，逐條對應標準要求與專案文檔。

### 11.2 建立證明文件包（Evidence Package）

合規性稽核時，需提供以下文件：

```
evidence-package/
├── requirements/
│   ├── 01_SYSTEM_PRD_SR_SD.md
│   ├── 02_FRONTEND_PRD_SR_SD.md
│   └── 03_BACKEND_PRD_SR_SD.md
├── design/
│   ├── SYSTEM_ARCHITECTURE.md
│   └── MODULE_DESIGN.md
├── traceability/
│   └── TRACEABILITY_MATRIX.md
├── testing/
│   ├── TEST_PLAN.md
│   └── TEST_REPORTS.md
├── configuration-management/
│   ├── openspec/changes/archive/（所有歸檔變更）
│   └── VERSION_CONTROL.md
├── risk-management/
│   ├── RISK_ANALYSIS.md
│   └── RISK_CONTROLS.md
└── regulations/
    ├── ISO-13485-compliance.md
    ├── IEC-62304-compliance.md
    ├── ISO-14971-compliance.md
    ├── IEC-62366-compliance.md
    ├── ISO-27001-compliance.md（若適用）
    ├── ISO-IEC-23894-compliance.md（若適用）
    └── RFC-2119-compliance.md
```

### 11.3 定期合規性審計

**每季度審計檢查清單**：

```markdown
## RFC 2119 檢查項目
- [ ] 關鍵字（MUST, SHOULD, MAY）是否正確大寫
- [ ] 需求描述是否無歧義
- [ ] 所有 MUST 需求都有對應測試案例

## ISO/IEC/IEEE 29148 檢查項目
- [ ] 所有 UR 都有對應的 SYS-SR
- [ ] 所有 SYS-SR 都有對應的子系統 SR
- [ ] 追溯矩陣完整無斷鏈
- [ ] 需求符合品質屬性（SMART 原則）

## IEC 62304 檢查項目
- [ ] 軟體安全分類已確定（Class A/B/C）
- [ ] 軟體需求規格（SRS）完整
- [ ] 軟體架構設計文檔完整
- [ ] 軟體詳細設計文檔完整
- [ ] 追溯性覆蓋到風險控制措施
- [ ] 組態管理記錄完整（OpenSpec 歸檔）
- [ ] 問題解決流程有記錄
- [ ] 驗證與測試記錄完整

## ISO 14971 檢查項目
- [ ] 風險管理計劃已建立
- [ ] 風險分析文檔完整
- [ ] 風險控制措施已實施並驗證
- [ ] 剩餘風險已評估並可接受

## IEC 62366 檢查項目（若適用）
- [ ] 可用性工程計劃已建立
- [ ] 使用者介面規格完整
- [ ] 可用性測試已完成
- [ ] 使用錯誤風險已識別與控制

## ISO 27001 檢查項目（若適用）
- [ ] 資訊安全管理系統（ISMS）已建立
- [ ] 資訊安全風險評估已完成
- [ ] 安全控制措施已實施
- [ ] 資訊安全文檔完整

## ISO/IEC 23894 檢查項目（若適用）
- [ ] AI 風險管理計劃已建立
- [ ] AI 風險已識別與評估
- [ ] AI 風險控制措施已實施
- [ ] AI 模型可解釋性文檔完整
```

---

## 12. 與 OpenSpec 的整合（OpenSpec Integration）

### 12.1 變更管理與合規性

OpenSpec 的變更管理機制天然支援 IEC 62304 的「軟體組態管理」要求：

| IEC 62304 要求 | OpenSpec 對應 |
|---------------|--------------|
| 變更請求記錄 | proposal.md |
| 變更影響評估 | proposal.md § Impact |
| 變更審核記錄 | Pull Request Review |
| 變更實作記錄 | tasks.md + Git Commits |
| 變更驗證記錄 | Test Reports + 驗收記錄 |
| 變更追溯性 | spec deltas + 追溯矩陣更新 |
| 軟體問題解決 | proposal.md + tasks.md（問題追蹤） |

### 12.2 歸檔變更 = 合規性證明

每次歸檔 OpenSpec 變更時，自動產生：
- 變更歷史記錄（`changes/archive/`）
- 需求追溯更新（PRD/SR/SD 同步）
- 設計文檔更新（design.md）
- 風險管理更新（ISO 14971 風險分析）

這些記錄可直接用於合規性稽核。

---

## 13. 常見問題（FAQ）

### Q1: 我的專案不是醫療器材軟體，需要這些標準嗎?

**A**: 不需要。這些標準主要適用於醫療器材軟體專案。一般軟體專案可僅使用 ISO/IEC/IEEE 29148（需求工程）與 RFC 2119。

### Q2: 合規性框架會增加多少開發成本？

**A**: 
- **初期投入**：建立文檔框架（約 1-2 週）
- **日常成本**：每次變更多 10-20% 時間（撰寫文檔、更新追溯）
- **長期收益**：減少返工、提升品質、便於維護、合規性認證更快

### Q3: 如何證明我們符合標準？

**A**: 使用合規性對照表（compliance-mapping）：
1. 列出標準的所有要求
2. 對應每個要求到專案文檔
3. 提供證明材料（文檔、測試報告、稽核記錄）
4. 定期審計確保一致性

### Q4: 可以部分採用框架嗎？

**A**: 可以。根據專案需求選擇：
- **最小集**：需求文檔（PRD/SR） + OpenSpec 變更管理 + RFC 2119
- **標準集**：最小集 + 追溯矩陣 + 設計文檔
- **完整集**：標準集 + 合規性文檔 + 風險管理（若需認證）
- **醫療器材集**：完整集 + IEC 62304 + ISO 14971 + ISO 13485

---

## 14. 延伸閱讀（Further Reading）

### 官方標準文件

- **RFC 2119**：可從 IETF 官網免費閱讀
- **ISO/IEC/IEEE 29148:2018**：可從 ISO 官網購買
- **ISO 13485:2016**：可從 ISO 官網購買
- **IEC 62304:2006+AMD1:2015**：可從 IEC 官網購買
- **ISO 14971:2019**：可從 ISO 官網購買
- **IEC 62366-1:2015**：可從 IEC 官網購買
- **ISO/IEC 27001:2022**：可從 ISO 官網購買
- **ISO/IEC 23894:2023**：可從 ISO 官網購買
- **FDA Guidance on Software as a Medical Device**：免費下載（美國 FDA 官網）
- **EU MDR 2017/745**：歐盟醫療器材法規（免費）

### 推薦書籍

- **"Software Requirements" by Karl Wiegers**：需求工程經典
- **"Medical Device Software Development" by David Vogel**：IEC 62304 實務指南
- **"Mastering Software Requirements" by IREB**：需求工程認證參考
- **"Risk Management for Medical Devices" by Bijan Elahi**：ISO 14971 實務指南

### 線上資源

- **IREB (International Requirements Engineering Board)**：需求工程認證
- **AAMI (Association for the Advancement of Medical Instrumentation)**：醫療器材標準組織
- **ISO/TC 210**：ISO 醫療器材技術委員會
- **IEC/SC 62A**：IEC 醫療器材軟體技術委員會

---

## 15. 下一步（Next Steps）

### 開始使用合規性框架

1. ✅ 閱讀本索引（完成！）
2. 📋 選擇適用標準（根據專案類型）
3. 📄 複製對應範本到專案
4. ✍️ 填寫合規性對照表
5. 🔍 進行首次合規性自我審計

### 進階主題

- 📚 風險管理整合（ISO 14971）
- 🏭 品質管理系統（ISO 13485）
- 🔒 資訊安全管理（ISO 27001）
- 🤖 AI 風險管理（ISO/IEC 23894）
- 📝 需求工程最佳實踐 (RFC 2119)

---

**文檔版本**: v2.1.0  
**維護團隊**: MetaFramework Core Team  
**最後更新**: 2025-12-24  
**變更說明**: 納入 RFC 2119 需求關鍵字規範，並優化合規性路徑指引。

