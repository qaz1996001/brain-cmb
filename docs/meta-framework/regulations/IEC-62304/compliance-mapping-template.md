# IEC 62304 合規性對照範本

**文件 ID**: COMP-IEC-62304-001  
**標題**: IEC 62304 醫療器材軟體生命週期合規性對照表  
**版本**: v1.0.0  
**狀態**: Template  
**建立日期**: 2025-01-XX

---

## 1. 目的與範圍

本文件提供 IEC 62304:2006+AMD1:2015 標準要求與專案文檔的對照表，用於證明專案符合醫療器材軟體生命週期流程的要求。

## 2. 軟體安全分類

**軟體安全分類**: Class [A/B/C]（待確定）

- **Class A**: 無法造成傷害
- **Class B**: 可能造成傷害但不嚴重
- **Class C**: 可能造成死亡或嚴重傷害

## 3. 標準要求對照

| IEC 62304 條款 | 標準要求 | 專案對應文檔 | 狀態 | 備註 |
|---------------|---------|------------|------|------|
| 5.1 | 軟體開發規劃 | `docs/brain-cmb/requirements/software-development-plan.md` | ⏳ 待建立 | |
| 5.2 | 軟體需求分析 | `docs/brain-cmb/requirements/` | ⏳ 待建立 | |
| 5.3 | 軟體架構設計 | `docs/brain-cmb/design/system-architecture.md` | ⏳ 待建立 | |
| 5.4 | 軟體詳細設計 | `docs/brain-cmb/design/module-design.md` | ⏳ 待建立 | |
| 5.5 | 軟體單元實作與驗證 | `src/` + `docs/brain-cmb/testing/unit-tests.md` | ⏳ 待建立 | |
| 5.6 | 軟體整合與整合測試 | `docs/brain-cmb/testing/integration-tests.md` | ⏳ 待建立 | |
| 5.7 | 軟體系統測試 | `docs/brain-cmb/testing/system-tests.md` | ⏳ 待建立 | |
| 5.8 | 軟體發布 | `docs/brain-cmb/compliance/release-notes.md` | ⏳ 待建立 | |
| 6.1 | 軟體維護規劃 | `docs/brain-cmb/compliance/maintenance-plan.md` | ⏳ 待建立 | |
| 7.1 | 軟體問題解決 | `openspec/changes/` | ✅ 已建立 | OpenSpec 變更管理 |
| 8.1 | 軟體組態管理 | Git + OpenSpec | ✅ 已建立 | |
| 9.1 | 軟體風險管理 | `docs/brain-cmb/compliance/risk-management.md` | ⏳ 待建立 | ISO 14971 |

## 4. 文檔要求

### 4.1 軟體需求規格（SRS）

- [ ] 功能需求
- [ ] 性能需求
- [ ] 介面需求
- [ ] 安全需求

### 4.2 軟體設計規格（SDD）

- [ ] 軟體架構設計
- [ ] 軟體詳細設計
- [ ] 介面設計

### 4.3 軟體測試規格

- [ ] 單元測試規格
- [ ] 整合測試規格
- [ ] 系統測試規格

## 5. 合規性證明

- [ ] 軟體安全分類已確定
- [ ] 軟體開發流程已建立
- [ ] 軟體維護流程已建立
- [ ] 軟體問題解決流程已建立
- [ ] 軟體組態管理已建立
- [ ] 軟體風險管理已整合（ISO 14971）

---

**文檔版本**: v1.0.0  
**最後更新**: 2025-01-XX

