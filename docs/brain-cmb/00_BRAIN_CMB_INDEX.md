# brain-cmb 文件管理系統

**文件 ID**: DOC-BRAIN-CMB-001  
**標題**: brain-cmb 專案文件管理系統  
**版本**: v1.3.0  
**狀態**: ✅ Active  
**建立日期**: 2025-12-24

---

## 1. 目的與範圍

本文件管理系統為 brain-cmb 專案提供符合醫療器材軟體開發標準的文檔結構與管理流程。所有專案參與者與 AI 代理 **MUST** 遵循本系統定義的規範。

## 2. 文檔結構

```
docs/brain-cmb/
├── 00_BRAIN_CMB_INDEX.md        # ⭐ 專案文檔系統索引 (本文件)
├── README.md                    # 🚀 快速開始指南
├── requirements/                 # 📋 需求文檔 (00_REQUIREMENTS_INDEX.md)
├── architecture/                # 🏗️ 架構與設計 (00_ARCHITECTURE_INDEX.md)
├── regulations/                 # ⚖️ 規範與合規性 (00_REGULATIONS_INDEX.md)
├── traceability/                # 🔗 追溯性管理 (00_TRACEABILITY_INDEX.md)
├── testing/                     # ✅ 測試與驗證 (00_TESTING_INDEX.md)
├── openspec-integration/        # 🔄 OpenSpec 整合 (00_OPENSPEC_INTEGRATION_INDEX.md)
└── guides/                      # 📚 專案指南 (00_GUIDES_INDEX.md)
```

## 3. 適用標準

本文件管理系統 **MUST** 支援並遵循以下標準：

- **RFC 2119**: 需求關鍵字規範 (基礎規範)
- **ISO 13485**: 醫療器材品質管理系統
- **IEC 62304**: 醫療器材軟體生命週期
- **ISO 14971**: 醫療器材風險管理
- **IEC 62366**: 醫療器材可用性工程
- **ISO 27001**: 資訊安全管理系統
- **ISO/IEC 23894**: AI 風險管理

## 4. 文檔管理原則

### 4.1 版本控制

- 所有文檔 **MUST** 使用 Git 進行版本控制。
- 重大變更 **MUST** 使用 OpenSpec 變更管理流程。
- 文檔版本號 **SHALL** 遵循語意化版本規範。

### 4.2 文檔追溯性

- 需求文檔 **MUST** 追溯至利害關係人需求。
- 架構與設計文檔 **MUST** 追溯至需求文檔。
- 測試文檔 **MUST** 追溯至需求與架構文檔。
- 規範與合規性文檔 **MUST** 追溯至相關標準要求。

### 4.3 文檔審核

- 所有文檔 **MUST** 經過審核與批准。
- 審核記錄 **SHALL** 保存在 OpenSpec 變更記錄中。

## 5. 與 OpenSpec 整合

本文件管理系統與 OpenSpec 變更管理系統深度整合：

- **變更提案**: **MUST** 使用 OpenSpec 創建變更提案。
- **變更實作**: **SHALL** 依據 tasks.md 完成開發與文檔更新。
- **變更歸檔**: 歸檔變更時 **MUST** 同步更新相關文檔。

## 6. 快速開始

1. 閱讀 [`requirements/00_REQUIREMENTS_INDEX.md`](requirements/00_REQUIREMENTS_INDEX.md) 了解需求文檔結構。
2. 閱讀 [`architecture/00_ARCHITECTURE_INDEX.md`](architecture/00_ARCHITECTURE_INDEX.md) 了解架構文檔結構。
3. 閱讀 [`regulations/00_REGULATIONS_INDEX.md`](regulations/00_REGULATIONS_INDEX.md) 了解規範要求。
4. 參考 [`guides/00_GUIDES_INDEX.md`](guides/00_GUIDES_INDEX.md) 遵循 AI 協作模式。

---

**文檔版本**: v1.3.0  
**最後更新**: 2025-12-24

