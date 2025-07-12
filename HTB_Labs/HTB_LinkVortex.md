# Link Vortex
- https://www.youtube.com/watch?v=SoPIw2flzFQ&t=1269s
- https://0xdf.gitlab.io/2025/04/12/htb-linkvortex.html#

## NMAP
```
┌──(root㉿kali)-[/home/jacob/Desktop/LinkVortex]
└─# ./nmap.sh linkvortex 10.129.231.194                                                                                                                                
Running nmap scan on 10.129.231.194 with output to linkvortex...
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-12 14:28 AEST
Nmap scan report for 10.129.231.194
Host is up (0.23s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 3e:f8:b9:68:c8:eb:57:0f:cb:0b:47:b9:86:50:83:eb (ECDSA)
|_  256 a2:ea:6e:e1:b6:d7:e7:c5:86:69:ce:ba:05:9e:38:13 (ED25519)
80/tcp open  http    Apache httpd
|_http-server-header: Apache
|_http-title: Did not follow redirect to http://linkvortex.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 59.47 seconds
Scan completed successfully.
Output files created: linkvortex.nmap, linkvortex.gnmap, linkvortex.xml
```
## Guided Mode
1. How many open TCP ports are listening on LinkVortex? 
2

2. What subdomain of `linkvortex.htb` returns a differt application from the main site?
- FFUF command:
```
┌──(root㉿kali)-[/home/jacob/Desktop/LinkVortex]
└─# ffuf -u http://10.129.231.194 -H "Host:FUZZ.linkvortex.htb" -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.129.231.194
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.linkvortex.htb
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

dev                     [Status: 200, Size: 2538, Words: 670, Lines: 116, Duration: 204ms]
:: Progress: [19966/19966] :: Job [1/1] :: 195 req/sec :: Duration: [0:01:46] :: Errors: 0 ::
```
- Remember to add it to etc/hosts!

3. What is the name of the directory that is exposed on the dev subdomain that allows access to the site's source code?
Once you've enumerated with ffuf time to enumerate directories, remember it's a slightly different ffuf command (No -H):
```
┌──(root㉿kali)-[/home/jacob/Desktop/LinkVortex]
└─# ffuf -u http://dev.linkvortex.htb/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt -ac

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://dev.linkvortex.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : true
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.git                    [Status: 301, Size: 239, Words: 14, Lines: 8, Duration: 199ms]
.git/config             [Status: 200, Size: 201, Words: 14, Lines: 9, Duration: 190ms]
.git/HEAD               [Status: 200, Size: 41, Words: 1, Lines: 2, Duration: 199ms]
.git/logs/              [Status: 200, Size: 868, Words: 59, Lines: 16, Duration: 190ms]
.git/index              [Status: 200, Size: 707577, Words: 2171, Lines: 2172, Duration: 807ms]
index.html              [Status: 200, Size: 2538, Words: 670, Lines: 116, Duration: 191ms]
:: Progress: [4744/4744] :: Job [1/1] :: 228 req/sec :: Duration: [0:00:23] :: Errors: 0 ::
```

4. What is the bob user's password for the Ghost admin panel?
- Since it's git, you can dump the directory to our local machine and explore it further with `gitdumper`
