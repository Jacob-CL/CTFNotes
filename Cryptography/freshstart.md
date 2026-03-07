```
sudo pacman -Syu
```

```
sudo pacman -S yay
```

```
sudo pacman -S base-devel git
```

```
sudo pacman-mirrors --fasttrack && sudo pacman -Syy
```
```
yay -S pyenv
```
Add this to ~/.bashrc or ~/.zshrc
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
Then install a python version:
```
pyenv install 3.12.0
etc
etc
```
TO use a particular python shell (Temporary — gone when you close the terminal.)
```
pyenv shell 3.8.18
```
To use a version for a specific folder: (saves a .python-version file there)
```
pyenv local 3.10.5
```
E.g for a challenge, make a folder and:
```
cd ~/ctf/challenge-name
pyenv local 3.10.5
```
This creates a .python-version file in that folder. Whenever you cd into it, pyenv automatically switches to that version.

```
pyenv install --list          # see all available versions
pyenv install 3.12.0          # install one
pyenv global 3.12.0           # set it as your default
```
```
pyenv versions
```

Screenshot tool:
```
sudo pacman -S flameshot
```
Then you can rebind Print Screen to Flameshot in **Settings → Keyboard → Application Shortcuts**, adding:
```
flameshot gui
```


```
```

```
```

```
```

```
```

```
```

```
```
