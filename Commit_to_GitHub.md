# How to Commit and Push Changes to GitHub

Guide for pushing code changes to the GitHub repository.

---

## Workflow to Push Changes to GitHub

### Step 1: Check What Changed
```bash
cd /home/nesha/scripts/cp_downloads2comics/
git status
```

**Output shows:**
- New files (Untracked)
- Modified files (Modified)
- Deleted files (Deleted)

### Step 2: Stage the Changes
```bash
# Stage all changes
git add .

# Or stage specific files
git add matching_analysis_generator.py comic_mover.py
```

### Step 3: Commit the Changes
```bash
git commit -m "Description of what changed"
```

**Example commit messages:**
```bash
git commit -m "Fix: Exclude non-comic files from source scan"
git commit -m "Feature: Add publisher folder matching (Cinebook, Fantagraphics)"
git commit -m "Refactor: Improve series name extraction for volume handling"
```

### Step 4: Push to GitHub
```bash
git push origin main
```

---

## Example: Full Workflow

```bash
# 1. Make changes to files
# ... edit matching_analysis_generator.py ...

# 2. Check status
git status
# Shows: modified: matching_analysis_generator.py

# 3. Stage changes
git add matching_analysis_generator.py

# 4. Commit with message
git commit -m "Fix: Change copy to move for file operations"

# 5. Push to GitHub
git push origin main
```

---

## For Release Updates (Release v1.1, v2.0, etc.)

When you want to **create a new release version:**

```bash
# 1. Make and commit all changes
git add .
git commit -m "Feature: Add support for PDF files - v1.1"

# 2. Create a new tag
git tag -a v1.1 -m "Release v1.1 - PDF support added"

# 3. Push both commit AND tag
git push origin main
git push origin v1.1
```

Then go to GitHub → **Releases** → Edit v1.1 release notes.

---

## Useful Commands

```bash
# See commit history
git log --oneline

# See what will be pushed
git diff origin/main

# Undo last commit (keep changes)
git reset --soft HEAD~1

# View current status
git status
```

---

## Quick Reference

```bash
git add .                    # Stage all changes
git commit -m "Message"      # Create commit
git push origin main         # Push to GitHub
```

---

## SSH Key Setup (if needed)

If you get a passphrase prompt and want to avoid it:

```bash
# Load SSH key into agent (ask once per session)
ssh-add ~/.ssh/id_ed25519
# Enter passphrase once, then no more prompts for this session
```

To verify SSH connection works:
```bash
ssh -T git@github.com
# Should show: Hi garoviks! You've successfully authenticated...
```

---

## Troubleshooting

### "fatal: not a git repository"
```bash
# Initialize git if this is a new project
git init
git remote add origin git@github.com:garoviks/cp_downloads2comics.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### "Repository not found"
- Check that the repository exists on GitHub
- Verify SSH key is added to GitHub settings
- Test connection: `ssh -T git@github.com`

### "Permission denied (publickey)"
- SSH key not added to GitHub or not loaded
- Run: `ssh-add ~/.ssh/id_ed25519`
- Check key on GitHub: Settings → SSH and GPG keys

---

## Commit Message Style

Keep messages clear and descriptive:

```bash
# Good
git commit -m "Fix: Exclude non-comic files from source scan"

# Good (with details)
git commit -m "Feature: Add publisher folder matching

- Support Cinebook, Fantagraphics, Humanoids, Soleil
- Check publisher name before series matching
- Adds new PUBLISHER confidence type"

# Avoid (too vague)
git commit -m "Updates"
git commit -m "Bug fix"
```

---

## When to Create a New Release

Create a new release tag when:
- ✅ Major feature complete
- ✅ Bug fix for critical issue
- ✅ Significant performance improvement
- ✅ Version number bump (v1.0 → v1.1 → v2.0)

```bash
git tag -a v1.1 -m "Release v1.1 - Description here"
git push origin v1.1
```
