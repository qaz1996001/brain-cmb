# GitHub Pull Request 管理指南 / GitHub PR Management Guide

## 概述 / Overview

本指南說明如何使用 GitHub CLI (`gh`) 和 Web 介面管理 Pull Requests，確保高效的程式碼審核與協作流程。

This guide explains how to manage Pull Requests using GitHub CLI (`gh`) and web interface for efficient code review and collaboration.

---

## 前置準備 / Prerequisites

### 安裝 GitHub CLI / Install GitHub CLI

```bash
# macOS
brew install gh

# Linux (Debian/Ubuntu)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Windows (via Winget)
winget install GitHub.cli
```

### 驗證 GitHub CLI / Authenticate GitHub CLI

```bash
# 登入 GitHub 帳號
# Login to GitHub account
gh auth login

# 選擇選項：
# Select options:
# - GitHub.com
# - HTTPS
# - Login with web browser

# 驗證身份狀態
# Verify authentication status
gh auth status
```

---

## Pull Request 生命週期 / PR Lifecycle

### 1. 建立 Pull Request / Create Pull Request

#### 方法 A：使用 GitHub CLI（推薦）/ Method A: Using GitHub CLI (Recommended)

```bash
# 確保在功能分支並已推送變更
# Ensure on feature branch with pushed changes
git checkout feature/your-feature
git push -u origin feature/your-feature

# 建立 PR（互動式）
# Create PR (interactive)
gh pr create

# 建立 PR（指定參數）
# Create PR (with parameters)
gh pr create \
  --title "Feature: Add CMB detection enhancement" \
  --body "$(cat <<'EOF'
## 摘要 / Summary
新增 CMB 檢測功能增強，提升檢測準確度與效能。
Add CMB detection enhancement to improve accuracy and performance.

## 變更項目 / Changes
- 實作新的檢測演算法 / Implement new detection algorithm
- 新增配置選項 / Add configuration options
- 更新文件與測試 / Update documentation and tests

## 測試計畫 / Test Plan
- [x] 單元測試通過 / Unit tests pass
- [x] 整合測試完成 / Integration tests completed
- [x] 效能基準測試 / Performance benchmarks
- [ ] 手動驗證 / Manual verification

## 相關議題 / Related Issues
Closes #123
Relates to #456

## 檢查清單 / Checklist
- [x] 程式碼遵循風格指南 / Code follows style guide
- [x] 文件已更新 / Documentation updated
- [x] 測試覆蓋率充足 / Test coverage adequate
- [x] 無破壞性變更 / No breaking changes

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)" \
  --base main \
  --head feature/your-feature

# 建立草稿 PR
# Create draft PR
gh pr create --draft --title "WIP: Feature in progress"

# 建立 PR 並指派審核者
# Create PR with reviewers
gh pr create --reviewer @username1,@username2

# 建立 PR 並加上標籤
# Create PR with labels
gh pr create --label "enhancement,documentation"
```

#### 方法 B：使用 Git + GitHub CLI / Method B: Using Git + GitHub CLI

```bash
# 推送分支
# Push branch
git push -u origin feature/your-feature

# 建立 PR 使用範本
# Create PR using template
gh pr create --fill
```

### 2. 列出與檢視 Pull Requests / List and View PRs

```bash
# 列出所有開放的 PR
# List all open PRs
gh pr list

# 列出特定狀態的 PR
# List PRs with specific status
gh pr list --state open
gh pr list --state closed
gh pr list --state merged

# 列出自己建立的 PR
# List PRs created by you
gh pr list --author @me

# 列出指派給自己的 PR
# List PRs assigned to you
gh pr list --assignee @me

# 檢視特定 PR 詳情
# View specific PR details
gh pr view 123

# 在瀏覽器中開啟 PR
# Open PR in browser
gh pr view 123 --web

# 檢視 PR 差異
# View PR diff
gh pr diff 123

# 檢視 PR 檢查狀態
# View PR check status
gh pr checks 123
```

### 3. 審核 Pull Request / Review Pull Request

#### 檢出 PR 進行本地測試 / Checkout PR for Local Testing

```bash
# 檢出 PR 分支
# Checkout PR branch
gh pr checkout 123

# 或使用分支名稱
# Or use branch name
gh pr checkout feature/your-feature

# 執行測試
# Run tests
pytest tests/
ruff check src/

# 驗證功能
# Verify functionality
python -m brain_cmb
```

#### 提交審核意見 / Submit Review Comments

```bash
# 批准 PR
# Approve PR
gh pr review 123 --approve --body "LGTM! 程式碼品質良好，測試完整。"

# 請求變更
# Request changes
gh pr review 123 --request-changes --body "請修正以下問題：
1. 函式命名不符合規範
2. 缺少單元測試
3. 文件需要更新"

# 提供評論（不批准也不拒絕）
# Provide comment (neither approve nor reject)
gh pr review 123 --comment --body "整體方向正確，有幾個小建議：
- 考慮提取重複的邏輯
- 新增錯誤處理
- 效能可以進一步優化"

# 在特定檔案行數新增評論
# Add comment on specific file line
gh pr review 123 --comment --body "這裡應該使用常數而非硬編碼" \
  --file src/brain_cmb/core/detection.py --line 42
```

### 4. 更新 Pull Request / Update Pull Request

```bash
# 切換到 PR 分支
# Switch to PR branch
gh pr checkout 123

# 進行修改
# Make changes
# ... edit files ...

# 提交變更
# Commit changes
git add .
git commit -m "fix: address review comments

- Refactor duplicated logic
- Add error handling
- Update documentation"

# 推送更新
# Push updates
git push

# PR 會自動更新
# PR updates automatically
```

### 5. 合併 Pull Request / Merge Pull Request

#### 使用 GitHub CLI 合併 / Merge Using GitHub CLI

```bash
# 合併 PR（squash merge）
# Merge PR (squash merge)
gh pr merge 123 --squash --delete-branch

# 合併 PR（merge commit）
# Merge PR (merge commit)
gh pr merge 123 --merge --delete-branch

# 合併 PR（rebase）
# Merge PR (rebase)
gh pr merge 123 --rebase --delete-branch

# 自動合併（當檢查通過時）
# Auto-merge (when checks pass)
gh pr merge 123 --auto --squash --delete-branch

# 合併並自訂提交訊息
# Merge with custom commit message
gh pr merge 123 --squash --body "Merged feature: CMB detection enhancement

This PR adds improved CMB detection capabilities with:
- Enhanced algorithm accuracy
- Better performance
- Comprehensive testing"
```

#### 合併策略選擇 / Merge Strategy Selection

| 策略 / Strategy | 何時使用 / When to Use | 歷史記錄 / History |
|----------------|----------------------|-------------------|
| **Squash** | 多個小提交合併為單一提交 / Multiple small commits merged into one | 線性、簡潔 / Linear, clean |
| **Merge** | 保留完整提交歷史 / Preserve complete commit history | 分支清晰 / Branch visible |
| **Rebase** | 保持線性歷史 / Maintain linear history | 線性、無合併節點 / Linear, no merge nodes |

**推薦 / Recommended**:
- 功能開發使用 **Squash** / Use **Squash** for feature development
- 重要里程碑使用 **Merge** / Use **Merge** for important milestones
- 小修復使用 **Rebase** / Use **Rebase** for small fixes

### 6. 關閉 Pull Request / Close Pull Request

```bash
# 關閉 PR 但不合併
# Close PR without merging
gh pr close 123 --comment "此 PR 不再需要，相關功能已在其他 PR 實作。
This PR is no longer needed, functionality implemented in another PR."

# 重新開啟已關閉的 PR
# Reopen closed PR
gh pr reopen 123
```

---

## 進階 PR 管理 / Advanced PR Management

### PR 標籤管理 / PR Label Management

```bash
# 新增標籤到 PR
# Add labels to PR
gh pr edit 123 --add-label "enhancement,high-priority"

# 移除標籤
# Remove labels
gh pr edit 123 --remove-label "wip"

# 列出可用標籤
# List available labels
gh label list
```

### PR 指派與審核者 / PR Assignees and Reviewers

```bash
# 指派 PR
# Assign PR
gh pr edit 123 --add-assignee @username

# 請求審核
# Request review
gh pr edit 123 --add-reviewer @reviewer1,@reviewer2

# 移除審核者
# Remove reviewer
gh pr edit 123 --remove-reviewer @reviewer1
```

### PR 里程碑管理 / PR Milestone Management

```bash
# 設定里程碑
# Set milestone
gh pr edit 123 --milestone "v0.2.0"

# 列出里程碑
# List milestones
gh api repos/:owner/:repo/milestones
```

### PR 範本 / PR Templates

建立 `.github/pull_request_template.md`：
Create `.github/pull_request_template.md`:

```markdown
## 摘要 / Summary
<!-- 簡述此 PR 的變更內容 -->
<!-- Brief description of changes in this PR -->

## 變更類型 / Type of Change
<!-- 勾選適用項目 -->
<!-- Check applicable items -->
- [ ] 🐛 錯誤修復 / Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ 新功能 / New feature (non-breaking change which adds functionality)
- [ ] 💥 破壞性變更 / Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 文件更新 / Documentation update
- [ ] 🎨 程式碼重構 / Code refactoring
- [ ] ⚡ 效能改善 / Performance improvement
- [ ] ✅ 測試 / Tests

## 變更項目 / Changes
<!-- 列出主要變更 -->
<!-- List main changes -->
-
-
-

## 測試計畫 / Test Plan
<!-- 說明如何測試這些變更 -->
<!-- Explain how to test these changes -->
- [ ] 單元測試通過 / Unit tests pass
- [ ] 整合測試完成 / Integration tests completed
- [ ] 手動測試驗證 / Manual testing verified

## 相關議題 / Related Issues
<!-- 連結相關議題 -->
<!-- Link related issues -->
Closes #
Relates to #

## 截圖 / Screenshots
<!-- 如適用，新增截圖 -->
<!-- If applicable, add screenshots -->

## 檢查清單 / Checklist
- [ ] 程式碼遵循專案風格指南 / Code follows project style guide
- [ ] 自我審閱變更 / Self-reviewed changes
- [ ] 註解清晰（特別是複雜區域）/ Comments clear (especially in complex areas)
- [ ] 文件已更新 / Documentation updated
- [ ] 無新的警告產生 / No new warnings generated
- [ ] 測試覆蓋率充足 / Test coverage adequate
- [ ] 相依套件已更新 / Dependencies updated

## 額外資訊 / Additional Information
<!-- 任何其他相關資訊 -->
<!-- Any other relevant information -->

---
🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

---

## CI/CD 整合 / CI/CD Integration

### 檢視 CI/CD 狀態 / View CI/CD Status

```bash
# 檢視 PR 檢查狀態
# View PR check status
gh pr checks 123

# 等待檢查完成
# Wait for checks to complete
gh pr checks 123 --watch

# 檢視特定檢查的日誌
# View specific check logs
gh run view <run-id>

# 重新執行失敗的檢查
# Re-run failed checks
gh run rerun <run-id>
```

### 自動化工作流程範例 / Automated Workflow Example

建立 `.github/workflows/pr-checks.yml`：
Create `.github/workflows/pr-checks.yml`:

```yaml
name: PR Checks

on:
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v5
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install uv
      run: pip install uv

    - name: Install dependencies
      run: uv sync

    - name: Run tests
      run: uv run pytest tests/ --cov=brain_cmb --cov-report=xml

    - name: Run linting
      run: uv run ruff check src/

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"

    - name: Build package
      run: |
        pip install uv
        uv build

    - name: Verify package
      run: |
        pip install dist/*.whl
        python -c "import brain_cmb; print(brain_cmb.__version__)"
```

---

## PR 審核最佳實踐 / PR Review Best Practices

### 審核者檢查清單 / Reviewer Checklist

#### 程式碼品質 / Code Quality
- [ ] 程式碼可讀性良好 / Code is readable
- [ ] 變數與函式命名有意義 / Variables and functions are well-named
- [ ] 註解清晰且必要 / Comments are clear and necessary
- [ ] 無重複程式碼 / No code duplication
- [ ] 遵循 DRY、SOLID 原則 / Follows DRY, SOLID principles

#### 功能性 / Functionality
- [ ] 實作符合需求 / Implementation meets requirements
- [ ] 邊界條件已處理 / Edge cases handled
- [ ] 錯誤處理完善 / Error handling is comprehensive
- [ ] 無明顯的錯誤 / No obvious bugs

#### 測試 / Testing
- [ ] 測試覆蓋率充足 / Test coverage is adequate
- [ ] 測試案例有意義 / Test cases are meaningful
- [ ] 測試通過 / Tests pass
- [ ] 邊界案例已測試 / Edge cases tested

#### 效能 / Performance
- [ ] 無明顯效能問題 / No obvious performance issues
- [ ] 演算法複雜度合理 / Algorithm complexity is reasonable
- [ ] 資源使用效率 / Efficient resource usage

#### 安全性 / Security
- [ ] 無 SQL 注入風險 / No SQL injection risks
- [ ] 輸入驗證完善 / Input validation comprehensive
- [ ] 敏感資料已保護 / Sensitive data protected
- [ ] 無硬編碼密碼 / No hardcoded credentials

#### 文件 / Documentation
- [ ] 公開 API 有文件 / Public APIs documented
- [ ] README 已更新 / README updated
- [ ] 範例程式碼正確 / Example code is correct
- [ ] 變更日誌已更新 / Changelog updated

### 審核評論範本 / Review Comment Templates

#### 批准 / Approval
```
✅ LGTM!

這個 PR 品質良好：
This PR looks great:

- 程式碼清晰易讀 / Code is clean and readable
- 測試覆蓋完整 / Test coverage is comprehensive
- 文件詳盡 / Documentation is thorough
- 符合專案規範 / Follows project standards

感謝您的貢獻！
Thanks for your contribution!
```

#### 請求變更 / Request Changes
```
🔍 請修正以下問題 / Please address the following issues:

1. **程式碼品質 / Code Quality**
   - [ ] `detection.py:42` 建議提取魔術數字為常數
   - [ ] Suggest extracting magic number to constant in `detection.py:42`

2. **測試 / Testing**
   - [ ] 缺少邊界條件測試
   - [ ] Missing edge case tests

3. **文件 / Documentation**
   - [ ] `build_segment()` 函式需要 docstring
   - [ ] `build_segment()` function needs docstring

修正後請再次請求審核。
Please request review again after addressing these.
```

#### 建議改進 / Suggestion for Improvement
```
💡 整體方向正確，有些改進建議 / Overall direction is good, some suggestions:

**非阻擋性建議 / Non-blocking suggestions:**
- 考慮重構重複的邏輯 / Consider refactoring duplicated logic
- 可以新增更多日誌以利除錯 / Could add more logging for debugging
- 效能可進一步優化 / Performance could be further optimized

這些建議可以在後續 PR 處理。
These can be addressed in follow-up PRs.
```

---

## 常見情境處理 / Common Scenarios

### 情境 1：解決合併衝突 / Scenario 1: Resolve Merge Conflicts

```bash
# 檢出 PR 分支
# Checkout PR branch
gh pr checkout 123

# 從主分支更新
# Update from main branch
git fetch origin main
git merge origin/main

# 手動解決衝突
# Manually resolve conflicts
# ... edit conflicted files ...

# 標記為已解決
# Mark as resolved
git add <conflicted-files>
git commit -m "fix: resolve merge conflicts with main"

# 推送更新
# Push updates
git push

# 衝突已解決，PR 可以合併
# Conflicts resolved, PR can be merged
```

### 情境 2：拆分大型 PR / Scenario 2: Split Large PR

```bash
# 建立新分支保存原始工作
# Create new branch to save original work
git checkout feature/large-pr
git checkout -b feature/large-pr-backup

# 回到原始分支
# Return to original branch
git checkout feature/large-pr

# 重置到分支起點
# Reset to branch start
git reset --soft $(git merge-base main HEAD)

# 分階段提交變更
# Commit changes in stages
git add src/brain_cmb/core/detection.py
git commit -m "feat(core): add detection algorithm"

git add tests/test_detection.py
git commit -m "test(core): add detection tests"

# 推送第一部分
# Push first part
git push -f origin feature/large-pr

# 建立第二個 PR 分支
# Create second PR branch
git checkout -b feature/large-pr-part2 feature/large-pr-backup
git rebase -i main  # 移除第一部分的提交
git push -u origin feature/large-pr-part2
```

### 情境 3：更新過時的 PR / Scenario 3: Update Stale PR

```bash
# 檢出過時的 PR
# Checkout stale PR
gh pr checkout 123

# 從主分支重新基底
# Rebase from main
git fetch origin main
git rebase origin/main

# 解決任何衝突
# Resolve any conflicts
# ... if conflicts occur ...

# 強制推送更新
# Force push updates
git push -f origin feature/stale-branch

# 請求重新審核
# Request re-review
gh pr review 123 --request-changes --body "已更新並解決衝突，請重新審核。
Updated and resolved conflicts, please re-review."
```

### 情境 4：回復已合併的 PR / Scenario 4: Revert Merged PR

```bash
# 找到要回復的 PR 合併提交
# Find merge commit of PR to revert
git log --oneline --merges

# 建立回復 PR
# Create revert PR
git checkout main
git pull origin main
git checkout -b revert/pr-123
git revert -m 1 <merge-commit-hash>
git push -u origin revert/pr-123

# 建立回復 PR
# Create revert PR
gh pr create --title "Revert: PR #123 - Reason for revert" \
  --body "This reverts PR #123 due to:
- Critical bug found in production
- Incompatibility with other features
- Need to redesign approach"
```

---

## PR 效率工具 / PR Efficiency Tools

### GitHub CLI 別名 / GitHub CLI Aliases

建立 `~/.config/gh/config.yml`：
Create `~/.config/gh/config.yml`:

```yaml
aliases:
  # 快速建立 PR
  # Quick create PR
  prc: pr create --fill

  # 列出我的 PR
  # List my PRs
  prm: pr list --author @me

  # 檢視 PR 並在瀏覽器開啟
  # View PR and open in browser
  prv: pr view --web

  # 批准並合併 PR
  # Approve and merge PR
  prm-approve: '!gh pr review "$1" --approve && gh pr merge "$1" --squash --delete-branch'

  # 檢出最新 PR
  # Checkout latest PR
  prc-latest: '!gh pr list --limit 1 --json number --jq ".[0].number" | xargs gh pr checkout'
```

使用別名：
Use aliases:

```bash
gh prc                    # 建立 PR
gh prm                    # 列出我的 PR
gh prv 123                # 在瀏覽器檢視 PR 123
gh prm-approve 123        # 批准並合併 PR 123
```

### PR 檢查腳本 / PR Check Script

建立 `scripts/pr-check.sh`：
Create `scripts/pr-check.sh`:

```bash
#!/bin/bash
# PR 提交前檢查腳本
# Pre-PR submission check script

set -e

echo "🔍 執行 PR 提交前檢查 / Running pre-PR checks..."

# 1. 程式碼格式檢查 / Code formatting check
echo "📝 檢查程式碼格式 / Checking code format..."
uv run ruff check src/

# 2. 型別檢查 / Type checking
echo "🔤 執行型別檢查 / Running type checks..."
uv run mypy src/

# 3. 單元測試 / Unit tests
echo "🧪 執行單元測試 / Running unit tests..."
uv run pytest tests/ --cov=brain_cmb --cov-report=term-missing

# 4. 建置測試 / Build test
echo "📦 測試建置 / Testing build..."
uv build

# 5. Git 狀態檢查 / Git status check
echo "📊 檢查 Git 狀態 / Checking Git status..."
if ! git diff-index --quiet HEAD --; then
    echo "⚠️  警告：有未提交的變更 / Warning: Uncommitted changes detected"
    git status --short
fi

echo "✅ 所有檢查通過！可以建立 PR / All checks passed! Ready to create PR"
```

使用腳本：
Use script:

```bash
chmod +x scripts/pr-check.sh
./scripts/pr-check.sh

# 檢查通過後建立 PR
# Create PR after checks pass
gh pr create
```

---

## 疑難排解 / Troubleshooting

### PR 無法合併 / PR Cannot Merge

**原因 / Cause**: 合併衝突或 CI/CD 檢查失敗
**Reason**: Merge conflicts or CI/CD check failures

```bash
# 檢查衝突
# Check conflicts
gh pr view 123

# 檢查 CI/CD 狀態
# Check CI/CD status
gh pr checks 123

# 解決方案：更新並解決衝突
# Solution: Update and resolve conflicts
gh pr checkout 123
git fetch origin main
git merge origin/main
# ... resolve conflicts ...
git push
```

### GitHub CLI 認證問題 / GitHub CLI Auth Issues

```bash
# 重新登入
# Re-login
gh auth logout
gh auth login

# 刷新令牌
# Refresh token
gh auth refresh

# 檢查權限
# Check permissions
gh auth status
```

### PR 標籤或審核者無法指派 / Cannot Assign Labels or Reviewers

```bash
# 檢查儲存庫權限
# Check repository permissions
gh api repos/:owner/:repo/collaborators/:username/permission

# 確保有足夠權限（write 或 admin）
# Ensure sufficient permissions (write or admin)
```

---

## 相關文件 / Related Documentation

- [Git 工作流程指南](./git-workflow.md) / Git Workflow Guide
- [版本發布流程](./release-workflow.md) / Release Workflow
- [GitHub CLI 文件](https://cli.github.com/manual/) / GitHub CLI Documentation
- [GitHub PR 最佳實踐](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) / GitHub PR Best Practices

---

**語言 / Languages**: [繁體中文](#) | [English](#)
