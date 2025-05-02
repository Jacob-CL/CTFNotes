# Vim / Vi
- [Vim CheatSheet](https://vimsheet.com/)
Once we are finished editing a file, we can hit the escape key esc to get out of insert mode, back into normal mode. When we are in normal mode, we can use the following keys to perform some useful shortcuts:

| Command | Description |
|---------|-------------|
| `x` | Cut character |
| `dw` | Cut word |
| `dd` | Cut full line |
| `yw` | Copy word |
| `yy` | Copy full line |
| `p` | Paste |

We can multiply any command to run multiple times by adding a number before it. For example, '4yw' would copy 4 words instead of one, and so on.

If we want to save a file or quit Vim, we have to press: to go into command mode. Once we do, we will see any commands we type at the bottom of the vim window: 

| Command | Description |
|---------|-------------|
| `:1` | Go to line number 1. |
| `:w` | Write the file, save |
| `:q` | Quit |
| `:q!` | Quit without saving |
| `:wq` | Write and quit |
