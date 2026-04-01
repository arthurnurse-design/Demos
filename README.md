# Demos

Infinite 3D canvas demo (Three.js). Source: [arthurnurse-design/Demos](https://github.com/arthurnurse-design/Demos).

## Run locally

From this folder:

```bash
python3 serve.py
```

Open [http://127.0.0.1:8789/index.html](http://127.0.0.1:8789/index.html).

## Git workflow

This folder is a Git repo with `main` as the default branch.

1. Set your identity once (use your GitHub **noreply** email if you like):

   ```bash
   cd /path/to/Demos
   git config user.name "Your Name"
   git config user.email "your.email@example.com"
   ```

2. **Upstream** (original project) is already configured as `upstream`:

   ```bash
   git remote -v
   ```

3. When you are ready to **push your own copy**, create a new empty repository on GitHub (or fork), then:

   ```bash
   git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
   git push -u origin main
   ```

   If you already use `origin` for something else, pick another remote name (e.g. `mydemo`).

4. Optional — pull updates from the original (only if histories are compatible; you may need merge/rebase):

   ```bash
   git fetch upstream
   ```

## If `git` errors on `.git`

Some tools block the `.git` pointer file. In **Terminal.app** (not inside a restricted sandbox), from this directory, either run `git` normally or use:

```bash
export GIT_DIR="$(pwd)/.git"
# if .git is a file pointing elsewhere, Git still resolves it when GIT_DIR is unset —
# otherwise use the directory Git created, e.g. sibling `Demos.git`, with:
export GIT_DIR=/path/to/Demos.git GIT_WORK_TREE=/path/to/Demos
git status
```

After cloning or fixing permissions, a standard single `.git` directory should work everywhere.
