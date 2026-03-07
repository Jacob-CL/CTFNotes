# Manjaro XFCE — Crypto CTF Setup Guide
> Fresh install reference. If your laptop dies, work through this top to bottom.

---

## Table of Contents
1. [System Update & Package Setup](#1-system-update--package-setup)
2. [pyenv — Python Version Manager](#2-pyenv--python-version-manager)
3. [crypto-env — Python Virtual Environment](#3-crypto-env--python-virtual-environment)
4. [System CTF Tools](#4-system-ctf-tools)
5. [Useful Tools & Shortcuts](#5-useful-tools--shortcuts)
6. [Recommended Folder Structure](#6-recommended-folder-structure)
7. [Verification Checklist](#7-verification-checklist)

---

## 1. System Update & Package Setup

Manjaro is a rolling release — there may be significant updates pending since the ISO was built.

### Update the system
```bash
sudo pacman -Syu
```
> ⚠️ If the kernel or core system components are updated, reboot afterward.

### Optimise mirrors for fastest download speeds
```bash
sudo pacman-mirrors --fasttrack && sudo pacman -Syy
```

### Install AUR helper and base dev tools
Many CTF tools live in the AUR. `yay` lets you access them. `base-devel` and `git` are needed to compile packages.
```bash
sudo pacman -S yay
sudo pacman -S base-devel git
```

---

## 2. pyenv — Python Version Manager

`pyenv` lets you install and switch between multiple Python versions. Useful when CTF tools require a specific version.

> **pyenv** = which Python | **venv** = which packages. These are separate concerns.

### Install pyenv
```bash
yay -S pyenv
```

### Add pyenv to your shell
Add these lines to the bottom of `~/.zshrc`:
```bash
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Reload your shell:
```bash
source ~/.zshrc
```

### pyenv commands reference

```bash
pyenv install --list        # see all available versions
pyenv install 3.12.0        # install a specific version
pyenv global 3.12.0         # set default version everywhere
pyenv local 3.10.5          # set version for current folder (saves .python-version file)
pyenv shell 3.8.18          # set version for this terminal session only (temporary)
pyenv version               # show currently active version
pyenv versions              # show all installed versions with * next to active
```

> Priority order if multiple are set: `shell` → `local` → `global`

### Per-challenge version example
If a challenge needs a specific Python version:
```bash
cd ~/ctf/challenge-name
pyenv local 3.10.5
```
This creates a `.python-version` file. pyenv will auto-switch whenever you `cd` into that folder.

---

## 3. crypto-env — Python Virtual Environment

A persistent venv with your core crypto CTF toolkit. Activate it for most challenges. Only create per-challenge venvs when you need conflicting or unusual dependencies.

### Install system dependencies first
These must be installed before the Python packages or some will fail to build.
```bash
sudo pacman -S cmake        # required for unicorn
sudo pacman -S gmp          # required for gmpy2
```

### Create and activate the venv
```bash
cd ~
python3 -m venv crypto-env
source ~/crypto-env/bin/activate
```

### Add a convenience alias to `~/.zshrc`
So you can just type `crypto` to activate the environment:
```bash
echo 'alias crypto="source ~/crypto-env/bin/activate"' >> ~/.zshrc
```
Reload after adding:
```bash
source ~/.zshrc
```


### Create `requirements.txt` and install
```bash
cat > requirements.txt << EOF
pycryptodome
cryptography
gmpy2
sympy
z3-solver
pwntools
ecdsa
jupyter
rsa
requests
numpy
matplotlib
EOF

pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. System CTF Tools

These are system-level applications — install them **outside** the venv with pacman/yay.

### SageMath
> ⚠️ The package is `sagemath`, not `sage`. Use `--noconfirm` to avoid interactive prompt issues in the terminal.
```bash
yay -S sagemath --noconfirm
```

### Core tools
```bash
sudo pacman -S openssl hashcat john --noconfirm
```

### RsaCtfTool — manual install from GitHub
> ⚠️ The AUR package `rsactftool-git` is broken — it installs but points to a missing file. Install manually instead.
```bash
cd ~
git clone https://github.com/RsaCtfTool/RsaCtfTool.git
cd RsaCtfTool
crypto                              # activate your venv first
pip install -r requirements.txt
```

Add an alias to `~/.zshrc` so you can call it from anywhere:
```bash
alias rsactftool="python ~/RsaCtfTool/RsaCtfTool.py"
```

Reload and test:
```bash
source ~/.zshrc
rsactftool --help
```

### Verify all installs
```bash
sage --version
openssl version
hashcat --version
john                                # john prints usage with no flags — no --version flag
rsactftool --help
```

### SageMath usage
Sage ships with its own Python interpreter. Use it alongside your venv — use the venv for scripting, use Sage for heavy maths (lattices, ECC, number theory).
```bash
sage                        # interactive Sage shell
sage -python yourscript.py  # run a script with Sage's Python
```

---

## 5. Useful Tools & Shortcuts

### Flameshot — screenshot tool
```bash
sudo pacman -S flameshot
```
Rebind `Print Screen` in **Settings → Keyboard → Application Shortcuts** to:
```
flameshot gui
```

| Shortcut | Action |
|----------|--------|
| `Print Screen` | Full screen |
| `Alt + Print Screen` | Active window |
| `Shift + Print Screen` | Select region |

### Terminator — split-pane terminal
```bash
sudo pacman -S terminator
```

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+E` | Split vertically |
| `Ctrl+Shift+O` | Split horizontally |
| `Ctrl+Shift+T` | New tab |
| `Alt+Arrow` | Move between panes |

### XFCE window shortcuts

| Shortcut | Action |
|----------|--------|
| `Super + Left` | Snap window left |
| `Super + Right` | Snap window right |
| `Super + Up` | Maximise |
| `Super + Down` | Restore / minimise |

### xfce4-terminal tab shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+T` | New tab |
| `Ctrl+Shift+W` | Close tab |
| `Ctrl+Page Up/Down` | Switch tabs |

---

## 6. Recommended Folder Structure

```
~/ctf/
  challenge-name/
    .venv/        ← only if the challenge needs isolated deps
    solve.py
    notes.md
```

> Most of the time just run `crypto` to activate crypto-env. Only create a per-challenge venv when a tool has conflicting dependencies.

---

## 7. Verification Checklist

Run these after setup to confirm everything is working.

### System
```bash
sudo pacman -Syu            # should say "nothing to do" if up to date
yay --version
git --version
cmake --version
```

### pyenv
```bash
pyenv --version
pyenv versions              # should show * system or an installed version
python --version
```

### crypto-env
```bash
crypto                      # prompt should change to show (crypto-env)

python -c "import Crypto; print('pycryptodome OK')"
python -c "import sympy; print('sympy OK')"
python -c "import z3; print('z3 OK')"
python -c "import gmpy2; print('gmpy2 OK')"
python -c "import pwn; print('pwntools OK')"
python -c "import numpy; print('numpy OK')"
```

### System CTF tools
```bash
sage --version
openssl version
hashcat --version
john                    # prints usage with no flags
rsactftool --help
flameshot --version
```

---

## Quick Reference Card

```bash
# Activate crypto environment
crypto

# Start a new challenge
mkdir ~/ctf/challenge-name && cd ~/ctf/challenge-name

# Check active Python
python --version
pyenv version

# Deactivate venv
deactivate
```
