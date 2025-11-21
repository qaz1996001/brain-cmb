# Git 工作流程指南 / Git Workflow Guide

## 概述 / Overview

本專案使用功能分支工作流程（Feature Branch Workflow），確保主分支穩定性並支援團隊協作開發。

This project uses Feature Branch Workflow to ensure main branch stability and support team collaboration.

---

## 分支策略 / Branch Strategy

### 主要分支 / Main Branches

- **`main`**: 生產穩定分支，僅接受經過審核的合併
  - Production-stable branch, only accepts reviewed merges
- **`develop`**: 開發整合分支（如需要）
  - Development integration branch (if needed)

### 功能分支 / Feature Branches

功能分支命名規範：
Feature branch naming convention:

```
feature/<feature-name>      # 新功能 / New features
bugfix/<bug-description>    # 錯誤修復 / Bug fixes
hotfix/<issue-description>  # 緊急修復 / Hotfixes
docs/<doc-topic>           # 文件更新 / Documentation
refactor/<refactor-scope>  # 重構 / Refactoring
test/<test-scope>          # 測試 / Testing
```

---

## 工作流程步驟 / Workflow Steps

### 1. 檢查當前狀態 / Check Current Status

開始任何工作前，先檢查 Git 狀態：
Before starting any work, check Git status:

```bash
# 檢查當前分支和狀態
# Check current branch and status
git status
git branch

# 確保在最新的主分支
# Ensure on latest main branch
git checkout main
git pull origin main
```

### 2. 建立功能分支 / Create Feature Branch

```bash
# 從 main 分支建立新的功能分支
# Create new feature branch from main
git checkout -b feature/your-feature-name

# 驗證分支建立成功
# Verify branch creation
git branch
```

### 3. 開發與提交 / Development and Commits

#### 提交規範 / Commit Convention

使用慣例式提交（Conventional Commits）格式：
Use Conventional Commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**類型 / Types:**
- `feat`: 新功能 / New feature
- `fix`: 錯誤修復 / Bug fix
- `docs`: 文件變更 / Documentation
- `style`: 格式調整 / Code style
- `refactor`: 重構 / Refactoring
- `test`: 測試 / Testing
- `chore`: 維護任務 / Maintenance

**範例 / Examples:**

```bash
# 新增功能
# Add feature
git add src/brain_cmb/core/new_feature.py
git commit -m "feat(core): add CMB detection enhancement

- Implement new detection algorithm
- Add configuration options
- Update documentation"

# 修復錯誤
# Fix bug
git add src/brain_cmb/dicomseg/builder.py
git commit -m "fix(dicomseg): correct DICOM-SEG metadata export

Fixes issue where patient orientation was incorrectly encoded"

# 文件更新
# Documentation update
git add docs/i18n/README.md
git commit -m "docs(i18n): add English and Traditional Chinese README"
```

#### 增量提交 / Incremental Commits

頻繁提交小的邏輯單元，而非大型單一提交：
Commit small logical units frequently, not large monolithic commits:

```bash
# 提交前檢視變更
# Review changes before commit
git diff

# 分階段新增檔案
# Stage files incrementally
git add <file1> <file2>
git commit -m "descriptive message"
```

### 4. 保持同步 / Stay Synchronized

定期從主分支同步變更：
Regularly sync changes from main branch:

```bash
# 切換到主分支並更新
# Switch to main and update
git checkout main
git pull origin main

# 回到功能分支並合併
# Return to feature branch and merge
git checkout feature/your-feature-name
git merge main

# 或使用 rebase（保持線性歷史）
# Or use rebase (maintains linear history)
git rebase main
```

### 5. 推送到遠端 / Push to Remote

```bash
# 首次推送（設定上游分支）
# First push (set upstream)
git push -u origin feature/your-feature-name

# 後續推送
# Subsequent pushes
git push
```

---

## 建立 Pull Request / Create Pull Request

### 使用 GitHub CLI (`gh`)

```bash
# 確保在功能分支上
# Ensure on feature branch
git checkout feature/your-feature-name

# 推送變更
# Push changes
git push -u origin feature/your-feature-name

# 建立 PR
# Create PR
gh pr create --title "Feature: Your Feature Description" --body "$(cat <<'EOF'
## 摘要 / Summary
[簡述此 PR 的變更內容]
[Brief description of changes in this PR]

## 變更項目 / Changes
- [變更項目 1]
- [變更項目 2]

## 測試計畫 / Test Plan
- [ ] 單元測試通過 / Unit tests pass
- [ ] 整合測試完成 / Integration tests completed
- [ ] 手動測試驗證 / Manual testing verified

## 相關議題 / Related Issues
Closes #[issue-number]

🤖 Generated with Claude Code
EOF
)"
```

### PR 標題規範 / PR Title Convention

使用描述性標題，說明變更的目的：
Use descriptive titles that explain the purpose of changes:

```
Feature: Add CMB detection enhancement
Fix: Correct DICOM-SEG metadata export
Docs: Add i18n documentation
Refactor: Improve pipeline modularity
```

### PR 檢查清單 / PR Checklist

提交 PR 前確認：
Before submitting PR, verify:

- [ ] 程式碼遵循專案風格指南 / Code follows project style guide
- [ ] 所有測試通過 / All tests pass
- [ ] 文件已更新 / Documentation updated
- [ ] 無合併衝突 / No merge conflicts
- [ ] CI/CD 檢查通過 / CI/CD checks pass
- [ ] 已審閱自己的變更 / Self-reviewed changes

---

## 審核與合併 / Review and Merge

### 審核流程 / Review Process

1. **程式碼審核** / Code Review
   - 至少一位團隊成員審核
   - At least one team member review

2. **自動化檢查** / Automated Checks
   - CI/CD 管線必須通過
   - CI/CD pipeline must pass

3. **衝突解決** / Conflict Resolution
   - 解決任何合併衝突
   - Resolve any merge conflicts

### 合併策略 / Merge Strategy

```bash
# 使用 GitHub CLI 合併 PR
# Merge PR using GitHub CLI
gh pr merge <PR-number> --squash --delete-branch

# 或使用標準 Git 命令
# Or use standard Git commands
git checkout main
git merge --no-ff feature/your-feature-name
git push origin main

# 刪除本地功能分支
# Delete local feature branch
git branch -d feature/your-feature-name
```

---

## 緊急修復流程 / Hotfix Process

針對生產環境的緊急問題：
For urgent production issues:

```bash
# 從 main 建立 hotfix 分支
# Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-issue-description

# 修復問題並測試
# Fix issue and test
# ... make changes ...

# 提交並推送
# Commit and push
git add .
git commit -m "hotfix: fix critical issue description"
git push -u origin hotfix/critical-issue-description

# 建立緊急 PR
# Create urgent PR
gh pr create --title "Hotfix: Critical Issue Description" --label "urgent"

# 合併後同步到開發分支（如果有）
# After merge, sync to develop branch (if applicable)
git checkout develop
git merge main
git push origin develop
```

---

## Git 命令速查 / Git Command Quick Reference

### 常用命令 / Common Commands

```bash
# 狀態檢查 / Status check
git status                          # 檢視工作目錄狀態
git log --oneline --graph --all    # 檢視提交歷史圖形

# 分支操作 / Branch operations
git branch                          # 列出本地分支
git branch -a                       # 列出所有分支（含遠端）
git checkout -b <branch-name>      # 建立並切換分支
git branch -d <branch-name>        # 刪除本地分支

# 同步操作 / Sync operations
git fetch origin                    # 取得遠端變更（不合併）
git pull origin <branch>           # 取得並合併遠端變更
git push origin <branch>           # 推送本地變更到遠端

# 撤銷操作 / Undo operations
git restore <file>                 # 撤銷工作目錄中的變更
git restore --staged <file>        # 取消暫存檔案
git reset --soft HEAD~1            # 撤銷最後一次提交（保留變更）
git reset --hard HEAD~1            # 撤銷最後一次提交（丟棄變更）

# 變更檢視 / View changes
git diff                           # 檢視未暫存的變更
git diff --staged                  # 檢視已暫存的變更
git diff main..feature-branch      # 比較分支差異
```

### GitHub CLI 命令 / GitHub CLI Commands

```bash
# PR 操作 / PR operations
gh pr create                       # 建立 PR（互動式）
gh pr list                         # 列出 PR
gh pr view <number>               # 檢視 PR 詳情
gh pr checkout <number>           # 檢出 PR 分支
gh pr merge <number>              # 合併 PR

# 議題操作 / Issue operations
gh issue create                    # 建立議題
gh issue list                      # 列出議題
gh issue view <number>            # 檢視議題

# 儲存庫操作 / Repository operations
gh repo view                       # 檢視儲存庫資訊
gh repo clone <repo>              # 複製儲存庫
```

---

## 最佳實踐 / Best Practices

### ✅ 建議做法 / Recommended

1. **頻繁提交** / Commit frequently
   - 每個邏輯變更獨立提交
   - Each logical change as separate commit

2. **描述性訊息** / Descriptive messages
   - 提交訊息說明「為什麼」而非「什麼」
   - Commit messages explain "why" not "what"

3. **保持同步** / Stay synchronized
   - 定期從主分支更新功能分支
   - Regularly update feature branch from main

4. **審閱變更** / Review changes
   - 提交前使用 `git diff` 審閱
   - Use `git diff` to review before commit

5. **測試優先** / Test first
   - 提交前確保測試通過
   - Ensure tests pass before commit

### ❌ 避免做法 / Avoid

1. **直接在 main 分支工作** / Working directly on main
   - 永遠使用功能分支
   - Always use feature branches

2. **巨型提交** / Giant commits
   - 將變更拆分為邏輯單元
   - Split changes into logical units

3. **無意義的提交訊息** / Meaningless commit messages
   - 避免「fix」、「update」等模糊訊息
   - Avoid vague messages like "fix", "update"

4. **未測試的提交** / Untested commits
   - 提交前執行測試
   - Run tests before committing

5. **強制推送** / Force push
   - 避免 `git push --force` 除非絕對必要
   - Avoid `git push --force` unless absolutely necessary

---

## 疑難排解 / Troubleshooting

### 合併衝突 / Merge Conflicts

```bash
# 當合併產生衝突時
# When merge produces conflicts

# 1. 檢視衝突檔案
# View conflicted files
git status

# 2. 手動編輯衝突標記
# Manually edit conflict markers
# <<<<<<<, =======, >>>>>>>

# 3. 標記為已解決
# Mark as resolved
git add <resolved-file>

# 4. 完成合併
# Complete merge
git commit
```

### 撤銷錯誤變更 / Undo Mistakes

```bash
# 撤銷工作目錄變更
# Undo working directory changes
git restore <file>

# 撤銷暫存
# Unstage files
git restore --staged <file>

# 撤銷最後一次提交但保留變更
# Undo last commit but keep changes
git reset --soft HEAD~1

# 完全撤銷最後一次提交
# Completely undo last commit
git reset --hard HEAD~1
```

### 清理本地分支 / Clean Local Branches

```bash
# 列出已合併的分支
# List merged branches
git branch --merged

# 刪除已合併的本地分支
# Delete merged local branches
git branch -d <branch-name>

# 清理遠端追蹤分支
# Clean up remote tracking branches
git fetch --prune
```

---

## 相關文件 / Related Documentation

- [GitHub PR 管理指南](./github-pr-guide.md) / GitHub PR Management Guide
- [版本發布流程](./release-workflow.md) / Release Workflow
- [慣例式提交規範](https://www.conventionalcommits.org/) / Conventional Commits Specification

---

**語言 / Languages**: [繁體中文](#) | [English](#)
