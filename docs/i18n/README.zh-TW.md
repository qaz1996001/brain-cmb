# brain-cmb

## 概述

**brain-cmb** 是一個用於神經影像中腦微出血（CMB）檢測和分析的 Python 套件，整合了 DICOM-SEG 標準，支援臨床工作流程。

## 主要特色

- **CMB 檢測管線**：自動化檢測腦部 MRI 掃描中的腦微出血
- **DICOM-SEG 整合**：以標準化 DICOM-SEG 格式匯出分割結果
- **PipelineCore 架構**：基於模組化管線框架構建，具備高度擴展性
- **臨床工作流程支援**：直接整合醫學影像系統

## 安裝

### 系統需求

- Python >= 3.10
- 使用 `uv` 套件管理器管理相依性

### 從原始碼安裝

```bash
# 複製儲存庫
git clone https://github.com/yourusername/brain-cmb.git
cd brain-cmb

# 使用 uv 安裝相依性
uv sync

# 安裝套件
uv pip install -e .
```

## 快速開始

### 基本使用

```python
from brain_cmb import main

# 執行 CMB 檢測管線
main()
```

### 命令列介面

```bash
# 執行 brain-cmb 管線
brain-cmb
```

## 專案結構

```
brain-cmb/
├── src/
│   └── brain_cmb/
│       ├── core/           # 核心 CMB 檢測邏輯
│       ├── dicomseg/       # DICOM-SEG 匯出功能
│       │   ├── builder.py  # DICOM-SEG 建構器
│       │   └── schema/     # CMB 分割模式定義
│       └── pipeline_cmb_tensorflow.py  # 基於 TensorFlow 的管線
├── docs/                   # 文件
│   ├── i18n/              # 國際化文件
│   ├── workflows/         # 開發工作流程
│   └── releases/          # 版本發布管理
├── tests/                  # 測試套件
└── pyproject.toml         # 專案配置
```

## 相依套件

核心相依套件包括：
- `pipelinecore`：模組化管線框架
- `pydicom-seg`：DICOM-SEG 格式支援
- `nibabel`：神經影像資料輸入輸出
- `tensorflow`：深度學習框架
- `pandas`、`matplotlib`、`tqdm`：資料處理與視覺化

## 文件

- [English Documentation](./README.md) - 英文文件
- [開發工作流程](../workflows/) - Git 與 GitHub 工作流程
- [版本發布管理](../releases/) - 版本控制與發布流程

## 開發

### 設定開發環境

```bash
# 安裝開發相依性
uv sync --dev

# 執行測試
pytest tests/

# 執行程式碼檢查
ruff check src/
```

### Git 工作流程

本專案遵循功能分支工作流程。詳細說明請參閱 [Git 工作流程指南](../workflows/git-workflow.md)。

### 貢獻指南

1. Fork 此儲存庫
2. 建立功能分支（`git checkout -b feature/your-feature`）
3. 遵循慣例式提交規範提交變更
4. 推送至您的 Fork 並建立 Pull Request
5. 確保 CI/CD 檢查通過

## 版本歷史

目前版本：**0.1.0**

詳細版本歷史請參閱 [CHANGELOG.md](../../CHANGELOG.md)。

## 授權

[請在此指定授權方式]

## 聯絡資訊

- 作者：user
- Email：a03440@tmu.edu.tw

## 致謝

本專案基於 [PipelineCore](https://github.com/yourusername/pipelinecore) 框架構建。

---

**語言**：[English](./README.md) | [繁體中文](./README.zh-TW.md)
