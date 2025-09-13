# Word Length Organizer
Usage:
```
python word_organizer.py test.txt
```
Makes a folder `word_length_output` that contains several files organized by word length.
```
┌──(root㉿kali)-[/CTFNotes/Codebreaking/WordLengthOrganizer]
└─# python word_organizer.py -h      
usage: word_organizer.py [-h] [-d DELIMITER] [-o OUTPUT_DIR] [--base-name BASE_NAME] [--keep-punctuation] [--case-sensitive] [--keep-duplicates] input_file

Organize words from a file into separate files based on word length

positional arguments:
  input_file            Path to the input text file

options:
  -h, --help            show this help message and exit
  -d, --delimiter DELIMITER
                        Delimiter to split words by (default: space)
  -o, --output-dir OUTPUT_DIR
                        Output directory for organized files (default: word_length_output)
  --base-name BASE_NAME
                        Base name for output files (default: words)
  --keep-punctuation    Keep punctuation in words (default: remove punctuation)
  --case-sensitive      Preserve case in words (default: convert to lowercase)
  --keep-duplicates     Keep duplicate words in output files (default: remove duplicates)

Examples:
  python word_organizer.py input.txt
  python word_organizer.py text.txt -d "|" -o results/
  python word_organizer.py file.txt --keep-punctuation --case-sensitive
  python word_organizer.py data.txt -d "," --keep-duplicates
```
Example Output:
```
┌──(root㉿kali)-[/CTFNotes/Codebreaking/WordLengthOrganizer]
└─# python word_organizer.py test.txt                                                   
Processing file: test.txt
Using delimiter: ' '

Word Length Organization Complete!
==================================================
Total words processed: 5
Files created: 3
--------------------------------------------------
words_length_2.txt        |   2 words (2 letters each)
words_length_4.txt        |   1 words (4 letters each)
words_length_5.txt        |   2 words (5 letters each)
--------------------------------------------------
```