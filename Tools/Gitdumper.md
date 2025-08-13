# Gitdumper

## Install (w venv)
```
┌──(root㉿kali)-[/home/jacob/Desktop/dog]
└─# python3 -m venv v-env; source v-env/bin/activate;

pip install git-dumper
git-dumper -h
```
## Example usage:
```
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/dog]
└─# git-dumper http://10.129.231.223:80/.git/ output
```
## Notes
- Will take a while depending on the size of the repo