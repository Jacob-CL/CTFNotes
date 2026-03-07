# hashcrack
1. Find hash type with hashcat `--identify`
2. Save hash to file `echo "xyz" > file.txt`
3. Crack with John `--wordlist=/home/dumlum/Downloads/Pwdb_top-1000000.txt --format=raw-sha256 file.txt`

```
hashcat --identify 482c811da5d5b4bc6d497ffa98491e38
echo "482c811da5d5b4bc6d497ffa98491e38" > 1sthash.txt
john --wordlist=/home/dumlum/Downloads/Pwdb_top-1000000.txt --format=raw-sha256 1sthash.txt
```
hash = password123
```
hashcat --identify b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
echo "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3" > 2ndhash.txt
john --wordlist=/home/dumlum/Downloads/Pwdb_top-1000000.txt --format=raw=sha1 2ndhash.txt
```
hash = letmein
```
hashcat --identify 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
echo "916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745" > 3rdhash.txt
john --wordlist=/home/dumlum/Downloads/Pwdb_top-1000000.txt --format=raw-sha256 3rdhash.txt
```
hash = qwerty098

FLAG = `picoCTF{UseStr0nG_h@shEs_&PaSswDs!_5b836723}`


```
    ~/CTFNotes/Cryptography/PicoCTF/hashcrack    main  nc verbal-sleep.picoctf.net 63965                                                                 INT ✘ 
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: letmein  
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: qwerty098
Correct! You've cracked the SHA-256 hash with a secret found. 
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_5b836723}
```
