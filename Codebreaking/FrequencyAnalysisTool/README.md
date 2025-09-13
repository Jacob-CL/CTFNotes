# Frequency Analysis Tool
Usage:
```
python freq_analyzer.py filename
```
```
┌──(root㉿kali)-[/CTFNotes/Codebreaking/FrequencyAnalysisTool]
└─# python freq_analyzer.py -h      
usage: freq_analyzer.py [-h] [--case-sensitive] [--all-chars] [--sort {frequency,alphabetical}] file

Analyze character frequency in text files

positional arguments:
  file                  Path to the text file to analyze

options:
  -h, --help            show this help message and exit
  --case-sensitive      Treat uppercase and lowercase letters as different
  --all-chars           Count all characters including punctuation and whitespace
  --sort {frequency,alphabetical}
                        Sort results alphabetically (default) or by frequency

Examples:
  python freq_analyzer.py document.txt
  python freq_analyzer.py text.txt --case-sensitive
```
Example output:
```
┌──(root㉿kali)-[/CTFNotes/Codebreaking/FrequencyAnalysisTool]
└─# python freq_analyzer.py test.txt 

Character Frequency Analysis
========================================
Total characters analyzed: 24
----------------------------------------
Char   Count    Percentage   Bar
----------------------------------------
a      2        8.33    %    ████
b      1        4.17    %    ██
c      1        4.17    %    ██
e      2        8.33    %    ████
h      1        4.17    %    ██
i      1        4.17    %    ██
j      1        4.17    %    ██
l      3        12.50   %    ██████
m      4        16.67   %    ████████
n      1        4.17    %    ██
o      2        8.33    %    ████
s      2        8.33    %    ████
u      2        8.33    %    ████
y      1        4.17    %    ██
```