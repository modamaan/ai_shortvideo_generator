# Fix Git Secret Exposure - Quick Guide

## Problem

GitHub is blocking your push because `.env` file with API keys is in commit history.

## Solution: Reset and Recommit

### Step 1: Update .gitignore

Make sure `.gitignore` includes:

```
.env
*.mp4
*.wav
*.mp3
audio_tts.*
```

### Step 2: Remove .env from all commits

```bash
# Go back before the first commit
git reset --soft HEAD~2

# Remove .env from staging
git rm --cached .env

# Add .gitignore update
git add .gitignore .env.example

# Commit everything except .env
git add .
git commit -m "Initial commit - Text-To-Video AI with Gemini/Groq integration"
```

### Step 3: Force push to GitHub

```bash
git push -f origin main
```

## Alternative: Allow the Secret (Quick Fix)

If you want to push immediately:

1. Click the GitHub link in the error message
2. Click "Allow secret"
3. Push again

**⚠️ Warning**: This exposes your API keys publicly. You should:

- Regenerate all API keys after pushing
- Update your local `.env` with new keys

## Recommended: Fresh Start

```bash
# Delete the repo on GitHub
# Create a new empty repo
# Then:

git rm -r --cached .
git add .
git commit -m "Initial commit"
git push -u origin main
```

Your `.env` file will stay local and won't be pushed.
