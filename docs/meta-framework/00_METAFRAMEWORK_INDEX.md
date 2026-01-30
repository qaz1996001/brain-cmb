# 00 — 元框架索引（MetaFramework Index）

**文件 ID**: META-INDEX-001  
**標題**: 通用產品與軟體開發元框架 — 文檔系統索引  
**版本**: v1.1.0  
**狀態**: Stable  
**建立日期**: 2025-12-22  
**最後更新**: 2025-12-24  
**適用領域**: 軟體開發、韌體開發、產品設計、系統工程

---

## 1. 元框架目的（Purpose of MetaFramework）

本元框架提供一套**通用的、標準化的文檔結構與開發流程**，可套用於：

- **軟體產品開發**（Web、行動應用、桌面軟體）
- **韌體與嵌入式系統**（IoT、工控設備、消費電子）
- **硬體產品**（需配合軟韌體的實體產品）
- **系統整合專案**（多系統協作、企業解決方案）
- **研究與創新專案**（概念驗證、技術探索）

### 1.1 核心理念

- **人機協作**：人類負責決策與審核（PRD、SR、SD），AI 負責執行與實作（遵循規範完成開發）
- **標準合規**：內建 ISO 13485 (醫療器材 QMS)、IEC 62304 (醫療軟體生命週期)、ISO 14971 (風險管理)、ISO 27001 (資安) 等國際標準對應
- **追溯性管理**：需求、設計、實作、測試與風險控制之間建立明確的雙向追溯關係
- **漸進式演進**：支援分階段開發（Phase 1, 2, 3...），每階段獨立驗證
- **OpenSpec 整合**：與 OpenSpec 變更管理系統無縫整合，實現提案→審核→實作→歸檔的閉環
- **規範性語言**：使用 RFC 2119 定義的關鍵字（MUST/SHALL, SHOULD, MAY）確保需求明確無歧義

---

## 2. 文檔架構總覽（Documentation Architecture）

```
docs/
├── resource/
│   ├── 01/                     # 具體專案實例（可作為範本）
│   └── 02/                     # 本元框架（通用抽象層）
│       ├── 00_METAFRAMEWORK_INDEX.md       # 本文件
│       ├── 01_FRAMEWORK_OVERVIEW.md        # 框架總體說明
│       ├── requirements/                    # 需求文檔範本與指南
│       │   ├── 00_REQUIREMENTS_INDEX.md
│       │   ├── TEMPLATE_SYSTEM_PRD_SR_SD.md
│       │   ├── TEMPLATE_SUBSYSTEM_PRD_SR_SD.md
│       │   └── HOWTO_WRITE_REQUIREMENTS.md
│       ├── regulations/                     # 標準合規範本
│       │   ├── 00_REGULATIONS_INDEX.md
│       │   ├── ISO-IEC-IEEE-29148/
│       │   │   ├── compliance-mapping-template.md
│       │   │   ├── requirements-quality-checklist.md
│       │   │   └── stakeholder-requirements-guide.md
│       │   └── ISO-20816/
│       │       ├── compliance-mapping-template.md
│       │       ├── measurement-system-template.md
│       │       ├── algorithm-validation-guide.md
│       │       └── calibration-procedure-template.md
│       ├── architecture/                    # 架構設計範本
│       │   ├── 00_ARCHITECTURE_INDEX.md
│       │   ├── TEMPLATE_SYSTEM_ARCHITECTURE.md
│       │   └── TEMPLATE_MODULE_DESIGN.md
│       ├── openspec-integration/            # OpenSpec 整合指南
│       │   ├── 00_OPENSPEC_INTEGRATION.md
│       │   ├── HOWTO_CREATE_PROPOSAL.md
│       │   └── HOWTO_ARCHIVE_CHANGE.md
│       └── guides/                          # 流程與最佳實踐
│           ├── 00_GUIDES_INDEX.md
│           ├── PHASE_BASED_DEVELOPMENT.md
│           ├── TRACEABILITY_MANAGEMENT.md
│           ├── AI_COLLABORATION_PATTERNS.md
│           └── VALIDATION_AND_TESTING.md
```

---

## 3. 框架核心概念（Core Concepts）

### 3.1 分層文檔模型（Layered Documentation Model）

本框架採用**三層文檔結構**，確保從願景到實作的完整覆蓋：

| 層級 | 文檔類型 | 讀者對象 | AI 角色 |
|------|---------|---------|--------|
| **Layer 1: 系統層（System Level）** | SYSTEM_PRD_SR_SD.md | 產品經理、專案負責人、利害關係人 | 理解總體目標，規劃變更提案 |
| **Layer 2: 子系統層（Subsystem Level）** | FRONTEND_PRD_SR_SD.md, BACKEND_PRD_SR_SD.md, FIRMWARE_PRD_SR_SD.md 等 | 領域工程師（前端、後端、韌體等） | 依據規範實作具體功能 |
| **Layer 3: 模組層（Module Level）** | 具體模組設計文檔（API、資料庫、元件等） | 開發人員 | 生成程式碼、測試、文檔 |

### 3.2 需求追溯鏈（Requirement Traceability Chain）

```
[利害關係人需求 Stakeholder Requirements]
          ↓
    [使用者需求 User Requirements: UR-xxx]
          ↓
    [系統需求 System Requirements: SYS-SR-xxx]
          ↓
    [子系統需求 Subsystem Requirements: FE-SR-xxx, BE-SR-xxx, FW-SR-xxx]
          ↓
    [設計規格 Design Specifications: API-xxx, DB-xxx, UI-xxx]
          ↓
    [實作 Implementation: Code, Config, Assets]
          ↓
    [驗證 Verification: Test Cases, Validation Reports]
```

每一層都必須明確標註：
- **對應的上層需求 ID**（Traces to）
- **對應的下層實作或設計 ID**（Traced by）
- **驗證方式**（Verification Method: Test/Inspection/Analysis/Demo）

### 3.3 階段式開發（Phase-Based Development）

將大型專案拆分為多個階段（Phase），每階段：
- 有明確的**範圍界定**（Scope）
- 有獨立的**驗收標準**（Acceptance Criteria）
- 有專屬的**需求文檔版本**（如 v1.0.0-Phase1）
- 可獨立交付與驗證

**範例**：
- Phase 1: 基礎功能與 MVP（8週）
- Phase 2: 進階功能與整合（12週）
- Phase 3: 優化與規模化（8週）

---

## 4. 與 OpenSpec 的整合（OpenSpec Integration）

本框架與 OpenSpec 變更管理系統深度整合：

### 4.1 角色分工

| OpenSpec 階段 | 人類職責 | AI 職責 |
|--------------|---------|--------|
| **Stage 1: 提案創建** | 審核提案的商業價值與技術可行性 | 撰寫 proposal.md, tasks.md, design.md，產生 spec deltas |
| **Stage 2: 實作執行** | 驗收功能、進行整合測試 | 依據 tasks.md 完成開發、測試、文檔 |
| **Stage 3: 變更歸檔** | 最終審核與部署決策 | 歸檔變更、更新 specs/、更新追溯矩陣 |

### 4.2 OpenSpec 變更提案與 PRD/SR/SD 的關係

- **OpenSpec Changes**：描述**如何改變**現有系統（增量變更）
- **PRD/SR/SD**：描述**系統應該是什麼樣**（當前狀態的完整描述）
- **同步機制**：每次歸檔變更時，必須同步更新 PRD/SR/SD 文檔中的對應章節

---

## 5. 標準合規性（Standards Compliance）

本框架內建以下國際標準的合規性支援：

### 5.1 ISO/IEC/IEEE 29148:2018（需求工程）

- **Stakeholder Requirements**：利害關係人需求（UR-xxx）
- **System Requirements Specification (SyRS)**：系統需求規格（SYS-SR-xxx）
- **Software Requirements Specification (SRS)**：軟體需求規格（FE-SR-xxx, BE-SR-xxx）
- **Traceability**：雙向追溯矩陣

詳見：[`regulations/ISO-IEC-IEEE-29148/compliance-mapping-template.md`](regulations/ISO-IEC-IEEE-29148/compliance-mapping-template.md)

### 5.2 ISO 13485:2016（醫療器材品質管理系統）

- **Quality Management System**：品質管理系統建立與維護
- **Design and Development**：設計與開發流程
- **Risk Management Integration**：風險管理整合（與 ISO 14971 整合）

詳見：[`regulations/ISO-13485/compliance-mapping-template.md`](regulations/ISO-13485/compliance-mapping-template.md)

### 5.3 IEC 62304:2006+AMD1:2015（醫療器材軟體生命週期）

- **Software Safety Classification**：軟體安全分類（Class A/B/C）
- **Software Development Process**：軟體開發流程
- **Software Maintenance**：軟體維護流程
- **Software Risk Management**：軟體風險管理

詳見：[`regulations/IEC-62304/compliance-mapping-template.md`](regulations/IEC-62304/compliance-mapping-template.md)

### 5.4 ISO 14971:2019（醫療器材風險管理）

- **Risk Management Process**：風險管理流程
- **Risk Analysis**：風險分析
- **Risk Control**：風險控制措施

詳見：[`regulations/ISO-14971/compliance-mapping-template.md`](regulations/ISO-14971/compliance-mapping-template.md)

### 5.5 IEC 62366-1:2015（醫療器材可用性工程）

- **Usability Engineering Process**：可用性工程流程
- **User Interface Specification**：使用者介面規格
- **Usability Testing**：可用性測試

詳見：[`regulations/IEC-62366/compliance-mapping-template.md`](regulations/IEC-62366/compliance-mapping-template.md)

### 5.6 ISO/IEC 27001:2022（資訊安全管理系統）

- **Information Security Management System**：資訊安全管理系統
- **Risk Assessment and Treatment**：風險評估與處理
- **Security Controls**：安全控制措施

詳見：[`regulations/ISO-27001/compliance-mapping-template.md`](regulations/ISO-27001/compliance-mapping-template.md)

### 5.7 ISO/IEC 23894:2023（AI 風險管理）

- **AI Risk Management Process**：AI 風險管理流程
- **AI Risk Identification**：AI 風險識別
- **AI Risk Assessment**：AI 風險評估

詳見：[`regulations/ISO-IEC-23894/compliance-mapping-template.md`](regulations/ISO-IEC-23894/compliance-mapping-template.md)

### 5.3 RFC 2119（需求層級關鍵字）

- **MUST / SHALL**：絕對要求，必須實作
- **SHOULD**：強烈建議，除非有正當理由否則應實作
- **MAY / COULD**：可選，實作者自行決定
- **MUST NOT / SHALL NOT**：絕對禁止

詳見：[`requirements/HOWTO_WRITE_REQUIREMENTS.md`](requirements/HOWTO_WRITE_REQUIREMENTS.md) § 4.1

### 5.4 其他標準（可選）

- **ISO 9001**：品質管理系統
- **ISO 13374**：機械狀態監測與診斷
- **ISO 18436**：狀態監測人員資格要求
- **CMMI**：能力成熟度整合模型

---

## 6. 使用指南（Usage Guide）

### 6.1 啟動新專案

1. **複製範本**：從 `docs/resource/02/requirements/` 複製範本到專案的 `docs/requirements/`
2. **填寫基本資訊**：專案名稱、階段、版本、狀態
3. **定義利害關係人需求**：訪談、需求收集、編寫 UR-xxx
4. **建立系統層 PRD/SR/SD**：`SYSTEM_PRD_SR_SD.md`
5. **拆解為子系統層 PRD/SR/SD**：`FRONTEND_PRD_SR_SD.md`, `BACKEND_PRD_SR_SD.md` 等
6. **建立追溯矩陣**：確保每個需求都有來源與去向
7. **初始化 OpenSpec**：`openspec init` 並創建第一個變更提案

### 6.2 日常開發流程

1. **需求變更**：由產品經理/負責人更新 PRD/SR
2. **創建 OpenSpec 提案**：AI 根據需求變更創建變更提案（proposal.md）
3. **人類審核**：技術負責人審核提案的可行性與完整性
4. **AI 實作**：根據 tasks.md 完成開發、測試、文檔
5. **人類驗收**：功能測試、整合測試、驗收測試
6. **歸檔變更**：OpenSpec archive，更新 specs/ 與 PRD/SR/SD
7. **更新追溯矩陣**：確保追溯鏈完整

### 6.3 階段驗收流程

1. **需求覆蓋率檢查**：所有 SR 都有對應的設計與實作
2. **追溯性檢查**：追溯鏈無斷裂
3. **合規性檢查**：符合選定的國際標準要求
4. **功能驗證**：所有需求都通過測試
5. **文檔完整性**：PRD/SR/SD/測試報告齊全
6. **階段驗收報告**：產出階段完成報告，開始下一階段

---

## 7. 文檔清單（Document Catalog）

### 7.1 核心文檔（必須）

| 文檔 | 說明 | 適用對象 |
|------|------|---------|
| [`01_FRAMEWORK_OVERVIEW.md`](01_FRAMEWORK_OVERVIEW.md) | 框架總體說明，快速入門 | 所有人 |
| [`requirements/00_REQUIREMENTS_INDEX.md`](requirements/00_REQUIREMENTS_INDEX.md) | 需求文檔索引 | 產品經理、工程師 |
| [`regulations/00_REGULATIONS_INDEX.md`](regulations/00_REGULATIONS_INDEX.md) | 標準合規性索引 | QA、法規人員 |
| [`openspec-integration/00_OPENSPEC_INTEGRATION.md`](openspec-integration/00_OPENSPEC_INTEGRATION.md) | OpenSpec 整合指南 | AI、工程師 |

### 7.2 範本文檔（Templates）

| 範本 | 說明 |
|------|------|
| `TEMPLATE_SYSTEM_PRD_SR_SD.md` | 系統層 PRD/SR/SD 範本 |
| `TEMPLATE_SUBSYSTEM_PRD_SR_SD.md` | 子系統層 PRD/SR/SD 範本 |
| `TEMPLATE_SYSTEM_ARCHITECTURE.md` | 系統架構設計範本 |
| `TEMPLATE_MODULE_DESIGN.md` | 模組詳細設計範本 |

### 7.3 指南文檔（Guides）

| 指南 | 說明 |
|------|------|
| `HOWTO_WRITE_REQUIREMENTS.md` | 需求撰寫指南 |
| `HOWTO_CREATE_PROPOSAL.md` | OpenSpec 提案創建指南 |
| `PHASE_BASED_DEVELOPMENT.md` | 階段式開發最佳實踐 |
| `TRACEABILITY_MANAGEMENT.md` | 追溯性管理指南 |
| `AI_COLLABORATION_PATTERNS.md` | 人機協作模式 |

---

## 8. 成功標準（Success Criteria）

一個成功的元框架應用應該滿足：

### 8.1 文檔品質

- ✅ 所有需求都有唯一 ID 與版本號
- ✅ 需求撰寫符合 SMART 原則（Specific, Measurable, Achievable, Relevant, Testable）
- ✅ 追溯矩陣完整無斷裂
- ✅ 設計文檔與實作一致

### 8.2 流程效率

- ✅ 需求變更到實作的週期 ≤ 2 週（視複雜度調整）
- ✅ OpenSpec 提案通過率 > 80%（表示提案品質高）
- ✅ AI 實作正確率 > 90%（減少返工）

### 8.3 合規性

- ✅ 符合選定的國際標準要求（ISO 13485, IEC 62304, ISO 14971 等）
- ✅ 定期合規性審計無重大缺失
- ✅ 文檔可追溯、可稽核

### 8.4 團隊協作

- ✅ 人類與 AI 的職責清晰
- ✅ 文檔更新及時（變更後 24 小時內）
- ✅ 知識傳承有效（新成員 ≤ 1 週熟悉框架）

---

## 9. 維護與演進（Maintenance and Evolution）

### 9.1 框架版本管理

本元框架採用語意化版本號：
- **Major (1.x.x)**：核心概念或結構變更
- **Minor (x.1.x)**：新增範本或指南
- **Patch (x.x.1)**：修正錯誤或澄清說明

### 9.2 更新機制

- **定期審查**：每季度審查一次框架適用性
- **社群回饋**：收集使用者回饋，持續改進
- **案例研究**：將成功專案案例整理為範例

### 9.3 擴展方向

- 支援更多領域（雲端服務、區塊鏈、AI/ML 系統）
- 整合更多標準（AUTOSAR、DO-178C 等）
- 提供自動化工具（需求驗證、追溯性檢查）

---

## 10. 快速開始（Quick Start）

### 第一次使用本框架？

1. 閱讀 [`01_FRAMEWORK_OVERVIEW.md`](01_FRAMEWORK_OVERVIEW.md) 了解整體概念
2. 查看 [`requirements/00_REQUIREMENTS_INDEX.md`](requirements/00_REQUIREMENTS_INDEX.md) 選擇合適的範本
3. 參考 [`guides/PHASE_BASED_DEVELOPMENT.md`](guides/PHASE_BASED_DEVELOPMENT.md) 規劃專案階段
4. 使用 [`openspec-integration/HOWTO_CREATE_PROPOSAL.md`](openspec-integration/HOWTO_CREATE_PROPOSAL.md) 創建第一個提案
5. 依循 [`guides/AI_COLLABORATION_PATTERNS.md`](guides/AI_COLLABORATION_PATTERNS.md) 與 AI 協作開發

### 已有現存專案想導入框架？

1. 閱讀 [`guides/MIGRATION_GUIDE.md`](guides/MIGRATION_GUIDE.md)（待創建）
2. 進行需求與設計文檔的現狀評估
3. 建立追溯矩陣，補齊缺失文檔
4. 漸進式導入 OpenSpec 變更管理
5. 逐步建立合規性證明文件

---

## 11. 支援與貢獻（Support and Contribution）

### 11.1 問題回報

如發現框架缺陷或不清楚之處，請：
1. 檢查 FAQ（待建立）
2. 搜尋現有議題
3. 創建新議題，描述問題與建議

### 11.2 貢獻指南

歡迎貢獻：
- 新的範本文檔
- 案例研究
- 最佳實踐
- 工具腳本

提交前請確保：
- 遵循現有文檔格式
- 提供清晰的說明與範例
- 通過內部審查

---

**文檔版本**: v1.0.0  
**維護團隊**: MetaFramework Core Team  
**最後審核**: 2025-12-22


