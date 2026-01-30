## 1. 準備工作
- [x] 1.1 備份現有 regulations 目錄結構（如需保留 ISO-20816 範本）
- [x] 1.2 確認新標準的適用範圍與要求

## 2. 更新元框架 regulations 索引
- [x] 2.1 更新 `docs/meta-framework/regulations/00_REGULATIONS_INDEX.md`
  - [x] 移除 ISO-20816 標準說明
  - [x] 新增 ISO 13485、IEC 62304、ISO 14971、IEC 62366、ISO 27001、ISO/IEC 23894 標準說明
  - [x] 更新標準對照表與適用領域
- [x] 2.2 更新 `docs/meta-framework/00_METAFRAMEWORK_INDEX.md` § 5（標準合規性章節）
- [x] 2.3 更新 `docs/meta-framework/01_FRAMEWORK_OVERVIEW.md` § 2.3（標準合規性框架）
- [x] 2.4 更新 `docs/meta-framework/README.md` § 4（國際標準支援）

## 3. 創建新標準範本目錄結構
- [x] 3.1 創建 `docs/meta-framework/regulations/ISO-13485/` 目錄
  - [x] 3.1.1 創建 `compliance-mapping-template.md`
  - [x] 3.1.2 創建 `quality-management-guide.md`
- [x] 3.2 創建 `docs/meta-framework/regulations/IEC-62304/` 目錄
  - [x] 3.2.1 創建 `compliance-mapping-template.md`
  - [x] 3.2.2 創建 `software-lifecycle-template.md`
  - [x] 3.2.3 創建 `software-safety-classification-guide.md`
- [x] 3.3 創建 `docs/meta-framework/regulations/ISO-14971/` 目錄
  - [x] 3.3.1 創建 `compliance-mapping-template.md`
  - [x] 3.3.2 創建 `risk-management-process-guide.md`
  - [x] 3.3.3 創建 `risk-analysis-template.md`
- [x] 3.4 創建 `docs/meta-framework/regulations/IEC-62366/` 目錄
  - [x] 3.4.1 創建 `compliance-mapping-template.md`
  - [x] 3.4.2 創建 `usability-engineering-process-guide.md`
- [x] 3.5 創建 `docs/meta-framework/regulations/ISO-27001/` 目錄
  - [x] 3.5.1 創建 `compliance-mapping-template.md`
  - [x] 3.5.2 創建 `information-security-management-guide.md`
- [x] 3.6 創建 `docs/meta-framework/regulations/ISO-IEC-23894/` 目錄
  - [x] 3.6.1 創建 `compliance-mapping-template.md`
  - [x] 3.6.2 創建 `ai-risk-management-guide.md`

## 4. 建立 brain-cmb 文件管理系統
- [x] 4.1 創建 `docs/brain-cmb/README.md` - 文件管理系統說明
- [x] 4.2 創建 `docs/brain-cmb/requirements/` 目錄
  - [x] 4.2.1 創建 `README.md` - 需求文檔索引
- [x] 4.3 創建 `docs/brain-cmb/design/` 目錄
  - [x] 4.3.1 創建 `README.md` - 設計文檔索引
- [x] 4.4 創建 `docs/brain-cmb/traceability/` 目錄
  - [x] 4.4.1 創建 `README.md` - 追溯性文檔索引
- [x] 4.5 創建 `docs/brain-cmb/compliance/` 目錄
  - [x] 4.5.1 創建 `README.md` - 合規性文檔索引
- [x] 4.6 創建 `docs/brain-cmb/testing/` 目錄
  - [x] 4.6.1 創建 `README.md` - 測試文檔索引

## 5. 驗證與測試
- [x] 5.1 驗證所有新創建的目錄結構正確
- [x] 5.2 驗證索引文件中的連結正確
- [x] 5.3 執行 `openspec validate update-medical-device-standards --strict`
- [x] 5.4 檢查文檔格式一致性

