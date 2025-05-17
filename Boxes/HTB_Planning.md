# NMAP Scan
- Port 22 and 80 --> planning.htb added to `etc/hosts`

# Gobuster 
## File scan
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
## DNS Scan
```
┌──(root㉿kali)-[/usr/share/wordlists/seclists/Discovery/DNS]
└─# gobuster dns -d planning.htb -w subdomains-top1million-20000.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Domain:     planning.htb
[+] Threads:    10
[+] Timeout:    1s
[+] Wordlist:   subdomains-top1million-20000.txt
===============================================================
Starting gobuster in DNS enumeration mode
===============================================================
Progress: 19966 / 19967 (99.99%)
===============================================================
Finished
===============================================================
```
# Ffuf
## File scan
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
## Subdomain Scan
```
┌──(root㉿kali)-[/usr/share/wordlists/seclists/Discovery/DNS]
└─# ffuf -w subdomains-top1million-20000.txt -u http://planning.htb/ -H "Host: FUZZ.planning.htb" -mc all -fs 178

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://planning.htb/
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt
 :: Header           : Host: FUZZ.planning.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
 :: Filter           : Response size: 178
________________________________________________

#www                    [Status: 400, Size: 166, Words: 6, Lines: 8, Duration: 169ms]
#mail                   [Status: 400, Size: 166, Words: 6, Lines: 8, Duration: 180ms]
:: Progress: [19966/19966] :: Job [1/1] :: 195 req/sec :: Duration: [0:01:40] :: Errors: 0 ::
```
# SSH
```
┌──(root㉿kali)-[/usr/share/wordlists/seclists/Discovery/Web-Content]
└─# ssh admin@10.10.11.68
The authenticity of host '10.10.11.68 (10.10.11.68)' can't be established.
ED25519 key fingerprint is SHA256:iDzE/TIlpufckTmVF0INRVDXUEu/k2y3KbqA/NDvRXw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.11.68' (ED25519) to the list of known hosts.
admin@10.10.11.68's password: 
Permission denied, please try again.
```



