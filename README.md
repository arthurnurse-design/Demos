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

## Git storage note

If `git status` fails in an IDE but works in **Terminal.app**, permissions or a split layout (`gitdir:`) may be the cause. To use a normal `.git` folder only, run in Terminal from the parent of this project:

```bash
GIT_DATA="$HOME/Demos.git"
test -d "$GIT_DATA" && mv "$GIT_DATA" Demos/.git-repo && rm -f Demos/.git && mv Demos/.git-repo Demos/.git
```

(Only if you still have a separate `$HOME/Demos.git` from an earlier setup; skip if `Demos/.git` is already a directory.)
