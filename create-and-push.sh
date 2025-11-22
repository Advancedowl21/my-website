#!/usr/bin/env bash
set -euo pipefail

REPO="Advancedowl21/my-website"
BRANCH="main"

# Ensure gh is installed
if ! command -v gh >/dev/null 2>&1; then
  echo "The GitHub CLI 'gh' is required. Install it: https://cli.github.com/"
  exit 1
fi

# Initialize git if needed
if [ ! -d .git ]; then
  git init
fi

git add .
git commit -m "Initial site + Dockerfile + CI" || true
git branch -M ${BRANCH}

# Create the repo and push (private)
# --source=. --remote=origin --push will push the current directory
gh repo create ${REPO} --private --source=. --remote=origin --push --confirm

echo ""
echo "Repository ${REPO} created and pushed."
echo "Open: https://github.com/${REPO}"
echo ""
echo "Next: In the repository Settings → Actions → General → Workflow permissions set to 'Read and write permissions' so the workflow can push images to ghcr.io."
echo "Then push any changes to main; CI will build and publish to ghcr.io/${REPO##*/}."
