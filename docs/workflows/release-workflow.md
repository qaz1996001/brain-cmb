# 版本發布工作流程 / Release Workflow

## 概述 / Overview

本指南說明如何管理 `brain-cmb` 專案的版本發布流程，包括語義化版本控制、變更日誌維護、GitHub Releases 建立與版本號更新。

This guide explains how to manage the release workflow for the `brain-cmb` project, including semantic versioning, changelog maintenance, GitHub Releases creation, and version number updates.

---

## 語義化版本控制 / Semantic Versioning

本專案遵循 [語義化版本 2.0.0](https://semver.org/) 規範。

This project follows [Semantic Versioning 2.0.0](https://semver.org/) specification.

### 版本格式 / Version Format

```
MAJOR.MINOR.PATCH

範例 / Example: 0.1.0, 1.0.0, 1.2.3
```

### 版本號規則 / Version Number Rules

- **MAJOR (主版本號)**: 不相容的 API 變更 / Incompatible API changes
  - 範例：`1.0.0` → `2.0.0`

- **MINOR (次版本號)**: 向下相容的功能新增 / Backward-compatible new features
  - 範例：`1.0.0` → `1.1.0`

- **PATCH (修訂號)**: 向下相容的錯誤修復 / Backward-compatible bug fixes
  - 範例：`1.0.0` → `1.0.1`

### 預發布版本 / Pre-release Versions

```
MAJOR.MINOR.PATCH-alpha.N    # Alpha 版本
MAJOR.MINOR.PATCH-beta.N     # Beta 版本
MAJOR.MINOR.PATCH-rc.N       # Release Candidate

範例 / Examples:
0.1.0-alpha.1
0.1.0-beta.1
0.1.0-rc.1
```

---

## 發布流程 / Release Process

### 步驟 1：準備發布 / Step 1: Prepare Release

#### 1.1 確認版本類型 / Determine Version Type

```bash
# 檢視自上次發布以來的變更
# Review changes since last release
git log $(git describe --tags --abbrev=0)..HEAD --oneline

# 分析變更類型決定版本號
# Analyze change types to determine version number
# - 破壞性變更 → MAJOR bump
# - 新功能 → MINOR bump
# - 錯誤修復 → PATCH bump
```

#### 1.2 建立發布分支 / Create Release Branch

```bash
# 從 main 分支建立發布分支
# Create release branch from main
git checkout main
git pull origin main
git checkout -b release/v0.2.0

# 或使用自動化腳本
# Or use automation script
./scripts/prepare-release.sh 0.2.0
```

### 步驟 2：更新版本號 / Step 2: Update Version Numbers

需要更新的檔案：
Files to update:

#### 2.1 更新 `pyproject.toml`

```bash
# 使用 sed 更新版本號
# Update version number using sed
sed -i 's/version = "0.1.0"/version = "0.2.0"/' pyproject.toml

# 或手動編輯
# Or edit manually
```

**pyproject.toml** (src/brain_cmb/pyproject.toml):1-3
```toml
[project]
name = "brain-cmb"
version = "0.2.0"
```

#### 2.2 更新 `src/brain_cmb/__init__.py`

```python
"""brain-cmb: Cerebral Microbleed Detection and DICOM-SEG Integration"""

__version__ = "0.2.0"
__author__ = "user"
__email__ = "a03440@tmu.edu.tw"

# ... rest of the file
```

#### 2.3 更新 `docs/i18n/README.md` 和 `docs/i18n/README.zh-TW.md`

```markdown
## Version History

Current version: **0.2.0**

See [CHANGELOG.md](../../CHANGELOG.md) for detailed version history.
```

### 步驟 3：更新變更日誌 / Step 3: Update Changelog

#### 3.1 建立或更新 `CHANGELOG.md`

```bash
# 如果不存在則建立
# Create if not exists
touch CHANGELOG.md
```

#### 3.2 變更日誌格式 / Changelog Format

遵循 [Keep a Changelog](https://keepachangelog.com/) 格式：
Follow [Keep a Changelog](https://keepachangelog.com/) format:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0] - 2025-01-15

### Added
- 新的 CMB 檢測演算法，提升準確度 15% / New CMB detection algorithm with 15% accuracy improvement
- DICOM-SEG 匯出功能支援多序列影像 / DICOM-SEG export support for multi-sequence images
- 配置檔案支援 YAML 格式 / Configuration file support for YAML format

### Changed
- 重構管線架構以提升模組化 / Refactored pipeline architecture for better modularity
- 更新相依套件至最新穩定版本 / Updated dependencies to latest stable versions

### Fixed
- 修復 DICOM-SEG builder 記憶體洩漏問題 / Fixed memory leak in DICOM-SEG builder
- 修正多執行緒環境下的競態條件 / Corrected race condition in multi-threaded environment

### Deprecated
- `old_detection_method()` 將在 v0.3.0 移除 / will be removed in v0.3.0

### Removed
- 移除已棄用的 legacy API / Removed deprecated legacy API

### Security
- 修復 CVE-2024-XXXXX 安全漏洞 / Fixed CVE-2024-XXXXX security vulnerability

## [0.1.0] - 2024-12-01

### Added
- 初始發布 / Initial release
- 基本 CMB 檢測功能 / Basic CMB detection functionality
- DICOM-SEG 整合 / DICOM-SEG integration

[Unreleased]: https://github.com/yourusername/brain-cmb/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/yourusername/brain-cmb/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/yourusername/brain-cmb/releases/tag/v0.1.0
```

#### 3.3 自動產生變更日誌 / Auto-generate Changelog

```bash
# 使用 git log 產生變更摘要
# Generate change summary using git log
git log $(git describe --tags --abbrev=0)..HEAD --pretty=format:"- %s" --reverse

# 或使用 GitHub CLI
# Or use GitHub CLI
gh api repos/:owner/:repo/compare/v0.1.0...main | jq -r '.commits[].commit.message'
```

### 步驟 4：提交版本變更 / Step 4: Commit Version Changes

```bash
# 新增所有版本相關變更
# Add all version-related changes
git add pyproject.toml src/brain_cmb/__init__.py CHANGELOG.md docs/

# 提交版本更新
# Commit version update
git commit -m "chore(release): prepare v0.2.0 release

- Update version numbers across project files
- Update CHANGELOG.md with release notes
- Update documentation with new version

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"

# 推送發布分支
# Push release branch
git push -u origin release/v0.2.0
```

### 步驟 5：建立發布 PR / Step 5: Create Release PR

```bash
# 建立發布 PR
# Create release PR
gh pr create \
  --title "Release v0.2.0" \
  --body "$(cat <<'EOF'
## 🚀 Release v0.2.0

### 變更摘要 / Change Summary
此版本包含重要功能增強與錯誤修復。
This release includes significant feature enhancements and bug fixes.

### 新功能 / New Features
- 新的 CMB 檢測演算法 / New CMB detection algorithm
- DICOM-SEG 多序列支援 / DICOM-SEG multi-sequence support
- YAML 配置檔支援 / YAML configuration support

### 錯誤修復 / Bug Fixes
- DICOM-SEG builder 記憶體洩漏 / DICOM-SEG builder memory leak
- 多執行緒競態條件 / Multi-threading race condition

### 測試計畫 / Test Plan
- [x] 所有單元測試通過 / All unit tests pass
- [x] 整合測試完成 / Integration tests completed
- [x] 效能基準測試 / Performance benchmarks
- [x] 文件審閱 / Documentation review

### 檢查清單 / Checklist
- [x] 版本號已更新 / Version numbers updated
- [x] CHANGELOG.md 已更新 / CHANGELOG.md updated
- [x] 文件已更新 / Documentation updated
- [x] 測試通過 / Tests pass
- [x] 無破壞性變更（或已記錄）/ No breaking changes (or documented)

### 發布後步驟 / Post-Release Steps
- [ ] 合併到 main 分支 / Merge to main branch
- [ ] 建立 GitHub Release / Create GitHub Release
- [ ] 發布到 PyPI / Publish to PyPI
- [ ] 更新文件網站 / Update documentation site
- [ ] 公告發布 / Announce release

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
EOF
)" \
  --base main \
  --head release/v0.2.0 \
  --label "release"

# 指派審核者
# Assign reviewers
gh pr edit --add-reviewer @reviewer1,@reviewer2
```

### 步驟 6：審核與合併 / Step 6: Review and Merge

```bash
# 等待審核通過
# Wait for review approval

# 執行最終檢查
# Perform final checks
gh pr checks

# 合併發布 PR
# Merge release PR
gh pr merge --squash --delete-branch
```

### 步驟 7：建立 Git 標籤 / Step 7: Create Git Tag

```bash
# 切換到已更新的 main 分支
# Switch to updated main branch
git checkout main
git pull origin main

# 建立帶註解的標籤
# Create annotated tag
git tag -a v0.2.0 -m "Release v0.2.0

Major improvements in CMB detection and DICOM-SEG integration.

See CHANGELOG.md for detailed release notes."

# 推送標籤到遠端
# Push tag to remote
git push origin v0.2.0

# 驗證標籤建立
# Verify tag creation
git tag -l
gh release list
```

### 步驟 8：建立 GitHub Release / Step 8: Create GitHub Release

#### 8.1 使用 GitHub CLI 建立 Release

```bash
# 建立 GitHub Release
# Create GitHub Release
gh release create v0.2.0 \
  --title "brain-cmb v0.2.0" \
  --notes "$(cat <<'EOF'
# brain-cmb v0.2.0

## 🎉 重點功能 / Highlights

### ✨ 新功能 / New Features
- **增強型 CMB 檢測演算法**：準確度提升 15%
  - **Enhanced CMB Detection Algorithm**: 15% accuracy improvement
- **DICOM-SEG 多序列支援**：支援複雜的多序列影像
  - **DICOM-SEG Multi-sequence Support**: Support for complex multi-sequence images
- **YAML 配置檔**：更靈活的配置管理
  - **YAML Configuration**: More flexible configuration management

### 🐛 錯誤修復 / Bug Fixes
- 修復 DICOM-SEG builder 記憶體洩漏問題
  - Fixed memory leak in DICOM-SEG builder
- 修正多執行緒環境下的競態條件
  - Corrected race condition in multi-threaded environment

### 📝 文件更新 / Documentation Updates
- 新增完整的 i18n 文件（英文與繁體中文）
  - Added comprehensive i18n documentation (English and Traditional Chinese)
- 更新 API 文件與使用範例
  - Updated API documentation and usage examples

## 📦 安裝 / Installation

```bash
pip install brain-cmb==0.2.0
```

## 🔗 完整變更日誌 / Full Changelog
查看完整變更日誌：[CHANGELOG.md](https://github.com/yourusername/brain-cmb/blob/v0.2.0/CHANGELOG.md)
View full changelog: [CHANGELOG.md](https://github.com/yourusername/brain-cmb/blob/v0.2.0/CHANGELOG.md)

## 📊 統計 / Statistics
- Commits: 47
- Contributors: 3
- Files changed: 23

## 🙏 致謝 / Acknowledgments
感謝所有貢獻者的辛勤工作！
Thanks to all contributors for their hard work!

---
**完整比較 / Full Comparison**: [v0.1.0...v0.2.0](https://github.com/yourusername/brain-cmb/compare/v0.1.0...v0.2.0)
EOF
)" \
  --latest

# 或從 CHANGELOG.md 提取發布說明
# Or extract release notes from CHANGELOG.md
gh release create v0.2.0 \
  --title "brain-cmb v0.2.0" \
  --notes-file <(sed -n '/## \[0.2.0\]/,/## \[0.1.0\]/p' CHANGELOG.md | head -n -1)
```

#### 8.2 附加發布資產 / Attach Release Assets

```bash
# 建置發布套件
# Build release package
uv build

# 附加輪子檔案到 Release
# Attach wheel file to Release
gh release upload v0.2.0 dist/brain_cmb-0.2.0-py3-none-any.whl

# 附加原始碼壓縮檔
# Attach source archives
gh release upload v0.2.0 dist/brain-cmb-0.2.0.tar.gz

# 驗證 Release 資產
# Verify Release assets
gh release view v0.2.0
```

### 步驟 9：發布到 PyPI / Step 9: Publish to PyPI

#### 9.1 配置 PyPI 憑證 / Configure PyPI Credentials

```bash
# 建立 ~/.pypirc
# Create ~/.pypirc
cat > ~/.pypirc <<EOF
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_API_TOKEN_HERE

[testpypi]
username = __token__
password = pypi-YOUR_TEST_API_TOKEN_HERE
EOF

chmod 600 ~/.pypirc
```

#### 9.2 發布到 TestPyPI（測試）/ Publish to TestPyPI (Test)

```bash
# 建置套件
# Build package
uv build

# 上傳到 TestPyPI
# Upload to TestPyPI
uv publish --repository testpypi

# 測試安裝
# Test installation
pip install --index-url https://test.pypi.org/simple/ brain-cmb==0.2.0
```

#### 9.3 發布到正式 PyPI / Publish to Production PyPI

```bash
# 上傳到 PyPI
# Upload to PyPI
uv publish

# 驗證安裝
# Verify installation
pip install brain-cmb==0.2.0
python -c "import brain_cmb; print(brain_cmb.__version__)"
```

### 步驟 10：發布後任務 / Step 10: Post-Release Tasks

```bash
# 1. 更新文件網站（如果有）
# Update documentation site (if applicable)
# cd docs && mkdocs gh-deploy

# 2. 在社交媒體或論壇公告
# Announce on social media or forums

# 3. 更新專案 README.md 徽章
# Update project README.md badges

# 4. 建立下一個開發版本
# Create next development version
git checkout main
git checkout -b develop
sed -i 's/version = "0.2.0"/version = "0.3.0-dev"/' pyproject.toml
git add pyproject.toml
git commit -m "chore: bump version to 0.3.0-dev"
git push -u origin develop
```

---

## 發布自動化 / Release Automation

### 自動化發布腳本 / Automated Release Script

建立 `scripts/release.sh`：
Create `scripts/release.sh`:

```bash
#!/bin/bash
# 自動化發布腳本 / Automated release script

set -e

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "使用方式 / Usage: $0 <version>"
    echo "範例 / Example: $0 0.2.0"
    exit 1
fi

echo "🚀 準備發布 v${VERSION} / Preparing release v${VERSION}"

# 1. 確認在 main 分支
# Ensure on main branch
git checkout main
git pull origin main

# 2. 建立發布分支
# Create release branch
git checkout -b release/v${VERSION}

# 3. 更新版本號
# Update version numbers
echo "📝 更新版本號 / Updating version numbers..."
sed -i "s/version = \".*\"/version = \"${VERSION}\"/" pyproject.toml
sed -i "s/__version__ = \".*\"/__version__ = \"${VERSION}\"/" src/brain_cmb/__init__.py

# 4. 更新文件中的版本
# Update version in documentation
find docs -name "*.md" -exec sed -i "s/Current version: \*\*.*\*\*/Current version: **${VERSION}**/" {} \;

# 5. 產生變更日誌條目（需手動編輯）
# Generate changelog entry (requires manual editing)
echo "📋 請手動更新 CHANGELOG.md / Please manually update CHANGELOG.md"
echo "Press Enter to continue after updating CHANGELOG.md..."
read

# 6. 提交變更
# Commit changes
git add .
git commit -m "chore(release): prepare v${VERSION} release

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"

# 7. 推送分支
# Push branch
git push -u origin release/v${VERSION}

# 8. 建立 PR
# Create PR
gh pr create \
    --title "Release v${VERSION}" \
    --body "Automated release preparation for v${VERSION}" \
    --label "release"

echo "✅ 發布準備完成 / Release preparation complete!"
echo "請審核並合併 PR，然後執行 / Please review and merge PR, then run:"
echo "  ./scripts/create-release.sh ${VERSION}"
```

### 建立 Release 腳本 / Create Release Script

建立 `scripts/create-release.sh`：
Create `scripts/create-release.sh`:

```bash
#!/bin/bash
# 建立 GitHub Release 腳本 / Create GitHub Release script

set -e

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "使用方式 / Usage: $0 <version>"
    echo "範例 / Example: $0 0.2.0"
    exit 1
fi

echo "🏷️  建立 Release v${VERSION} / Creating Release v${VERSION}"

# 1. 確認在 main 分支並已更新
# Ensure on main branch and updated
git checkout main
git pull origin main

# 2. 建立標籤
# Create tag
echo "📌 建立 Git 標籤 / Creating Git tag..."
git tag -a v${VERSION} -m "Release v${VERSION}"
git push origin v${VERSION}

# 3. 建置套件
# Build package
echo "📦 建置套件 / Building package..."
uv build

# 4. 從 CHANGELOG 提取發布說明
# Extract release notes from CHANGELOG
RELEASE_NOTES=$(sed -n "/## \[${VERSION}\]/,/## \[/p" CHANGELOG.md | head -n -1)

# 5. 建立 GitHub Release
# Create GitHub Release
echo "🎉 建立 GitHub Release / Creating GitHub Release..."
gh release create v${VERSION} \
    --title "brain-cmb v${VERSION}" \
    --notes "${RELEASE_NOTES}" \
    --latest \
    dist/brain_cmb-${VERSION}-py3-none-any.whl \
    dist/brain-cmb-${VERSION}.tar.gz

# 6. 發布到 PyPI
# Publish to PyPI
echo "📤 發布到 PyPI / Publishing to PyPI..."
uv publish

echo "✅ Release v${VERSION} 建立完成！ / Release v${VERSION} created successfully!"
echo "🔗 檢視 Release / View Release: https://github.com/yourusername/brain-cmb/releases/tag/v${VERSION}"
```

### GitHub Actions 自動發布 / GitHub Actions Automated Release

建立 `.github/workflows/release.yml`：
Create `.github/workflows/release.yml`:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install uv
        run: pip install uv

      - name: Build package
        run: uv build

      - name: Extract release notes
        id: extract_notes
        run: |
          VERSION=${GITHUB_REF#refs/tags/v}
          NOTES=$(sed -n "/## \[${VERSION}\]/,/## \[/p" CHANGELOG.md | head -n -1)
          echo "notes<<EOF" >> $GITHUB_OUTPUT
          echo "${NOTES}" >> $GITHUB_OUTPUT
          echo "EOF" >> $GITHUB_OUTPUT

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          body: ${{ steps.extract_notes.outputs.notes }}
          files: |
            dist/*.whl
            dist/*.tar.gz
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: |
          pip install twine
          twine upload dist/*
```

---

## 版本管理最佳實踐 / Version Management Best Practices

### ✅ 建議做法 / Recommended

1. **語義化版本控制** / Semantic Versioning
   - 嚴格遵循 SemVer 規範
   - Strictly follow SemVer specification

2. **詳盡的變更日誌** / Detailed Changelog
   - 每次發布更新 CHANGELOG.md
   - Update CHANGELOG.md for every release

3. **帶註解的標籤** / Annotated Tags
   - 使用 `git tag -a` 而非 `git tag`
   - Use `git tag -a` instead of `git tag`

4. **發布檢查清單** / Release Checklist
   - 建立並遵循發布檢查清單
   - Create and follow release checklist

5. **自動化測試** / Automated Testing
   - CI/CD 必須通過才能發布
   - CI/CD must pass before release

### ❌ 避免做法 / Avoid

1. **跳過版本號** / Skipping Versions
   - 不要跳過版本號（如 0.1.0 → 0.3.0）
   - Don't skip version numbers (e.g., 0.1.0 → 0.3.0)

2. **直接推送標籤** / Pushing Tags Directly
   - 先測試再建立標籤
   - Test before creating tags

3. **無發布說明** / No Release Notes
   - 每個 Release 必須有說明
   - Every Release must have notes

4. **未更新版本號** / Not Updating Version Numbers
   - 確保所有檔案版本一致
   - Ensure version consistency across files

---

## 常見問題 / FAQ

### Q1: 如何回滾錯誤的發布？ / How to rollback a bad release?

```bash
# 1. 刪除遠端標籤
# Delete remote tag
git push --delete origin v0.2.0

# 2. 刪除本地標籤
# Delete local tag
git tag -d v0.2.0

# 3. 刪除 GitHub Release
# Delete GitHub Release
gh release delete v0.2.0 --yes

# 4. 從 PyPI 移除（需聯繫 PyPI 管理員）
# Remove from PyPI (contact PyPI admins)
# 無法直接刪除，只能標記為 yanked
# Cannot delete directly, can only mark as yanked
```

### Q2: 如何處理預發布版本？ / How to handle pre-release versions?

```bash
# 建立預發布版本
# Create pre-release version
gh release create v0.2.0-beta.1 \
    --title "brain-cmb v0.2.0-beta.1" \
    --notes "Beta release for testing" \
    --prerelease

# 測試後升級到正式版本
# Upgrade to stable after testing
gh release create v0.2.0 \
    --title "brain-cmb v0.2.0" \
    --notes "Stable release" \
    --latest
```

### Q3: 如何維護多個版本分支？ / How to maintain multiple version branches?

```bash
# 建立維護分支
# Create maintenance branch
git checkout -b maint/v0.1.x v0.1.0

# 在維護分支上修復錯誤
# Fix bugs on maintenance branch
git checkout maint/v0.1.x
# ... make fixes ...
git commit -m "fix: critical bug in v0.1.x"

# 發布修訂版本
# Release patch version
./scripts/release.sh 0.1.1
```

---

## 發布檢查清單 / Release Checklist

### 發布前 / Pre-Release
- [ ] 所有測試通過 / All tests pass
- [ ] CI/CD 管線成功 / CI/CD pipeline succeeds
- [ ] 版本號已更新 / Version numbers updated
- [ ] CHANGELOG.md 已更新 / CHANGELOG.md updated
- [ ] 文件已審閱 / Documentation reviewed
- [ ] 無未完成的 TODO / No outstanding TODOs
- [ ] 安全漏洞已修復 / Security vulnerabilities fixed

### 發布中 / During Release
- [ ] 發布 PR 已建立 / Release PR created
- [ ] PR 已審核並批准 / PR reviewed and approved
- [ ] PR 已合併 / PR merged
- [ ] Git 標籤已建立 / Git tag created
- [ ] GitHub Release 已建立 / GitHub Release created
- [ ] 套件已上傳到 PyPI / Package uploaded to PyPI

### 發布後 / Post-Release
- [ ] Release 安裝測試 / Release installation tested
- [ ] 文件網站已更新 / Documentation site updated
- [ ] 發布公告已發送 / Release announcement sent
- [ ] 下一版本已準備 / Next version prepared
- [ ] Release 標籤已驗證 / Release tag verified

---

## 相關文件 / Related Documentation

- [Git 工作流程指南](./git-workflow.md) / Git Workflow Guide
- [GitHub PR 管理指南](./github-pr-guide.md) / GitHub PR Management Guide
- [語義化版本規範](https://semver.org/) / Semantic Versioning Specification
- [Keep a Changelog](https://keepachangelog.com/) / Keep a Changelog

---

**語言 / Languages**: [繁體中文](#) | [English](#)
