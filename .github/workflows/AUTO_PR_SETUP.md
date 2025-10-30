# Auto PR to ComfyUI Setup Guide

This document explains how to set up and use the automated PR workflow that syncs `embedded-docs` version updates to the ComfyUI repository.

## 🎯 What This Workflow Does

When you bump the version in `pyproject.toml` on the `main` branch, this workflow automatically:

1. ✅ Detects the version change
2. ✅ Generates a changelog from commits and merged PRs
3. ✅ Updates `requirements.txt` in your ComfyUI fork
4. ✅ Creates a new branch with format: `update-docs-{VERSION}-{TIMESTAMP}`
5. ✅ Submits a **draft PR** to `comfyanonymous/ComfyUI`
6. ✅ Sends you a GitHub notification

## 🔧 Setup Instructions

### 1. Create a GitHub Personal Access Token (PAT)

You need a PAT with permissions to:
- Push to `comfyui-wiki/ComfyUI` (your fork)
- Create PRs on `comfyanonymous/ComfyUI` (target repository)

**Steps:**
1. Go to: https://github.com/settings/tokens/new
2. Select **Fine-grained tokens** (recommended) or **Classic token**
3. Configure the token:
   - **Name**: `ComfyUI Auto PR Token`
   - **Expiration**: Choose based on your preference
   - **Repository access**: 
     - Select "Only select repositories"
     - Add: `comfyui-wiki/ComfyUI`
   - **Permissions**:
     - Repository permissions:
       - Contents: Read and write
       - Pull requests: Read and write
       - Metadata: Read-only (automatic)

4. Click **Generate token** and copy it immediately (you won't see it again!)

### 2. Add the Token to Repository Secrets

1. Go to your `embedded-docs` repository
2. Navigate to: **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add the secret:
   - **Name**: `COMFYUI_FORK_TOKEN`
   - **Value**: Paste your PAT from step 1
5. Click **Add secret**

### 3. Verify the Workflow File

The workflow file is located at: `.github/workflows/auto-pr-to-comfyui.yml`

Make sure these values are correct:
- Fork repository: `comfyui-wiki/ComfyUI`
- Target repository: `comfyanonymous/ComfyUI`
- Target branch: `master`
- Requirements file: `requirements.txt`

## 📋 How to Use

### Normal Workflow

1. Make your changes to documentation
2. Update the version in `pyproject.toml`
3. Commit and push to `main` branch
4. The workflow triggers automatically
5. You'll receive a GitHub notification when the draft PR is created
6. Review the draft PR at: https://github.com/comfyanonymous/ComfyUI/pulls

### Manual Trigger

Currently, the workflow only triggers on version changes. If you need to manually trigger it, you can add this to the workflow:

```yaml
on:
  workflow_dispatch:  # Add this line
  push:
    branches: [main]
    paths:
      - "pyproject.toml"
```

## 📬 Notifications

You will automatically receive GitHub notifications when:
- ✅ A draft PR is created
- ✅ Someone comments on the PR
- ✅ The PR status changes

**To ensure you receive notifications:**
1. Go to: https://github.com/settings/notifications
2. Make sure these are enabled:
   - ✅ Email notifications
   - ✅ Pull requests
   - ✅ Participating (for PRs you created)

## 🔍 Troubleshooting

### Problem: Workflow doesn't trigger

**Solutions:**
- Check that the file changed is exactly `pyproject.toml`
- Verify you pushed to the `main` branch
- Check workflow runs at: `https://github.com/Comfy-Org/embedded-docs/actions`

### Problem: Authentication failed

**Solutions:**
- Verify the `COMFYUI_FORK_TOKEN` secret is set correctly
- Check that your PAT hasn't expired
- Ensure the PAT has the correct permissions

### Problem: PR creation fails

**Solutions:**
- Verify that `comfyui-wiki/ComfyUI` fork exists
- Check that the fork is up to date with upstream
- Ensure `requirements.txt` exists in the fork

### Problem: No notifications received

**Solutions:**
- Check your GitHub notification settings
- Look at: https://github.com/notifications
- Verify email settings in your GitHub profile

## 📝 PR Content Structure

The generated draft PR includes:

```markdown
## Update embedded docs to v{VERSION}

### 📦 Package Information
- **PyPI**: https://pypi.org/project/comfyui-embedded-docs/{VERSION}/
- **Release**: https://github.com/Comfy-Org/embedded-docs/releases/tag/v{VERSION}

### 📝 Changes since v{PREV_VERSION}

#### Merged Pull Requests
- PR #123: Add documentation for new nodes
- PR #124: Fix typos in CLIPLoader docs

#### Commits
- abc1234: Update Spanish translations
- def5678: Add images for flux nodes

---
*This is an automated draft PR created by the embedded-docs sync workflow.*
```

## 🔐 Security Notes

- ⚠️ **Never commit tokens directly** to the repository
- ✅ Always use GitHub Secrets for sensitive data
- ✅ Use fine-grained tokens with minimal required permissions
- ✅ Regularly rotate your tokens (every 6-12 months)
- ✅ Audit token usage in GitHub settings

## 📊 Workflow Visualization

```
Version Bump in pyproject.toml
         ↓
   Workflow Triggers
         ↓
   Extract Version Info
         ↓
   Generate Changelog
         ↓
   Clone ComfyUI Fork
         ↓
   Update requirements.txt
         ↓
   Create New Branch
         ↓
   Push to Fork
         ↓
   Create Draft PR
         ↓
   GitHub Notification Sent
```

## 🆘 Support

If you encounter issues:
1. Check the workflow logs in GitHub Actions
2. Verify all settings in this guide
3. Test with a minor version bump first (e.g., 0.3.0 → 0.3.1)

## 📚 Related Files

- Workflow: `.github/workflows/auto-pr-to-comfyui.yml`
- Publish workflow: `.github/workflows/publish.yml`
- Version file: `pyproject.toml`
- Target file: `requirements.txt` (in ComfyUI fork)

