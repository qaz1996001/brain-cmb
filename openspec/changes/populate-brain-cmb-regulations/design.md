## Context

`brain-cmb` 專案作為一個醫療影像處理軟體（特別是針對腦部微出血偵測），必須嚴格遵守醫療器材開發相關標準。元框架（meta-framework）已經提供了標準範本，本計畫旨在將這些範本實例化為專案專屬的合規性文件。

## Goals / Non-Goals

- **Goals**:
  - 為每個適用標準建立專案專屬的合規性對照表。
  - 確保文檔編號與版本管理符合 `DOC-BRAIN-CMB-REG-XXX` 格式。
  - 在索引文件中建立清晰的導覽結構。

- **Non-Goals**:
  - 填寫具體的技術細節或測試數據（這些將在開發與測試階段完成）。
  - 修改元框架中的範本。

## Decisions

- **Decision: 文檔命名規範**
  - 使用 `{Standard}-Compliance-Mapping.md` 格式，與元框架範本名稱對應。
  - 編號系統將遵循 `00_REGULATIONS_INDEX.md` 中定義的邏輯。

- **Decision: 文檔存放位置**
  - 統一存放在 `docs/brain-cmb/regulations/` 目錄下，與索引文件在同一層級。

## Risks / Trade-offs

- **[Risk]** 文檔內容與實際開發進度脫節 → **Mitigation**: 在 OpenSpec 流程中加入定期審查任務。
- **[Risk]** 標準版本更新導致文檔失效 → **Mitigation**: 在文檔中明確標註所採用的標準版本。

## Open Questions

- 是否需要為每個標準建立獨立的子目錄？（目前決定先放在同一層級，若文檔過多再行重構）

