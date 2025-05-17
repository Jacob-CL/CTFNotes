# NMAP Scan
- Port 22 and 80 --> planning.htb added to `etc/hosts`

# Gobuster scan
```
┌──(root㉿kali)-[/usr/share/wordlists/seclists/Discovery/Web-Content]
└─# gobuster dir -u planning.htb -w common.txt                                                                                                                         
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://planning.htb
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/css                  (Status: 301) [Size: 178] [--> http://planning.htb/css/]
/img                  (Status: 301) [Size: 178] [--> http://planning.htb/img/]
/index.php            (Status: 200) [Size: 23914]
/js                   (Status: 301) [Size: 178] [--> http://planning.htb/js/]
/lib                  (Status: 301) [Size: 178] [--> http://planning.htb/lib/]
Progress: 4744 / 4745 (99.98%)
```
# Ffuf scan
```
┌──(root㉿kali)-[/usr/share/wordlists/seclists/Discovery/Web-Content]
└─# ffuf -u http://planning.htb/FUZZ -w common.txt

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://planning.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

css                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 205ms]
img                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 204ms]
index.php               [Status: 200, Size: 23914, Words: 8236, Lines: 421, Duration: 204ms]
js                      [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 181ms]
lib                     [Status: 301, Size: 178, Words: 6, Lines: 8, Duration: 205ms]
:: Progress: [4744/4744] :: Job [1/1] :: 195 req/sec :: Duration: [0:00:25] :: Errors: 0 ::

```
All 403 except index.php (home page)
