# Tomb Watcher

As is common in real life Windows pentests, you will start the TombWatcher box with credentials for the following account: henry / H3nry_987TGV!

## NMAP.sh results
(`nmap -sV -sC -oA "$FILENAME" "$TARGET_IP"`)
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ./nmap.sh tombwatcher 10.10.11.72
Running nmap scan on 10.10.11.72 with output to tombwatcher...
Starting Nmap 7.95 ( https://nmap.org ) at 2025-06-09 13:56 AEST
Nmap scan report for 10.10.11.72
Host is up (0.19s latency).
Not shown: 987 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-06-09 07:56:30Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-06-09T07:57:54+00:00; +3h59m22s from scanner time.
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-06-09T07:57:55+00:00; +3h59m21s from scanner time.
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-06-09T07:57:54+00:00; +3h59m22s from scanner time.
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: tombwatcher.htb0., Site: Default-First-Site-Name)
|_ssl-date: 2025-06-09T07:57:55+00:00; +3h59m21s from scanner time.
| ssl-cert: Subject: commonName=DC01.tombwatcher.htb
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:DC01.tombwatcher.htb
| Not valid before: 2024-11-16T00:47:59
|_Not valid after:  2025-11-16T00:47:59
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-06-09T07:57:17
|_  start_date: N/A
|_clock-skew: mean: 3h59m21s, deviation: 0s, median: 3h59m20s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 103.95 seconds
Scan completed successfully.
Output files created: tombwatcher.nmap, tombwatcher.gnmap, tombwatcher.xml
```
# LDAP
- Authenticated ldapsearch gave me too much info - all good but difficult to look through.
- Asked for specifics with windapsearch - see "Tools/windapsearch"
## Windapsearch
Domain admins:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.72 -u henry@tombwatcher.htb -p "H3nry_987TGV!" --da
[+] Using Domain Controller at: 10.10.11.72
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=tombwatcher,DC=htb
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:TOMBWATCHER\Henry
[+] Attempting to enumerate all Domain Admins
[+] Using DN: CN=Domain Admins,CN=Users.CN=Domain Admins,CN=Users,DC=tombwatcher,DC=htb
[+]     Found 1 Domain Admins:

cn: Administrator

[+] Using DN: CN=Domain Admins,CN=Users.CN=Domain Admins,CN=Users,DC=tombwatcher,DC=htb
[+]     Found 1 Domain Admins:

cn: Administrator


[*] Bye!
```
Users:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.72 -u henry@tombwatcher.htb -p "H3nry_987TGV!" --users
[+] Using Domain Controller at: 10.10.11.72
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=tombwatcher,DC=htb
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:TOMBWATCHER\Henry

[+] Enumerating all AD users
[+]     Found 7 users: 

cn: Administrator

cn: Guest

cn: krbtgt

cn: Henry

cn: Alfred

cn: sam

cn: john


[*] Bye!
```
Groups:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.72 -u henry@tombwatcher.htb -p "H3nry_987TGV!" -G
[+] Using Domain Controller at: 10.10.11.72
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=tombwatcher,DC=htb
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:TOMBWATCHER\Henry

[+] Enumerating all AD groups
[+]     Found 49 groups: 

cn: Administrators
distinguishedName: CN=Administrators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Users
distinguishedName: CN=Users,CN=Builtin,DC=tombwatcher,DC=htb

cn: Guests
distinguishedName: CN=Guests,CN=Builtin,DC=tombwatcher,DC=htb

cn: Print Operators
distinguishedName: CN=Print Operators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Backup Operators
distinguishedName: CN=Backup Operators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Replicator
distinguishedName: CN=Replicator,CN=Builtin,DC=tombwatcher,DC=htb

cn: Remote Desktop Users
distinguishedName: CN=Remote Desktop Users,CN=Builtin,DC=tombwatcher,DC=htb

cn: Network Configuration Operators
distinguishedName: CN=Network Configuration Operators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Performance Monitor Users
distinguishedName: CN=Performance Monitor Users,CN=Builtin,DC=tombwatcher,DC=htb

cn: Performance Log Users
distinguishedName: CN=Performance Log Users,CN=Builtin,DC=tombwatcher,DC=htb

cn: Distributed COM Users
distinguishedName: CN=Distributed COM Users,CN=Builtin,DC=tombwatcher,DC=htb

cn: IIS_IUSRS
distinguishedName: CN=IIS_IUSRS,CN=Builtin,DC=tombwatcher,DC=htb

cn: Cryptographic Operators
distinguishedName: CN=Cryptographic Operators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Event Log Readers
distinguishedName: CN=Event Log Readers,CN=Builtin,DC=tombwatcher,DC=htb

cn: Certificate Service DCOM Access
distinguishedName: CN=Certificate Service DCOM Access,CN=Builtin,DC=tombwatcher,DC=htb

cn: RDS Remote Access Servers
distinguishedName: CN=RDS Remote Access Servers,CN=Builtin,DC=tombwatcher,DC=htb

cn: RDS Endpoint Servers
distinguishedName: CN=RDS Endpoint Servers,CN=Builtin,DC=tombwatcher,DC=htb

cn: RDS Management Servers
distinguishedName: CN=RDS Management Servers,CN=Builtin,DC=tombwatcher,DC=htb

cn: Hyper-V Administrators
distinguishedName: CN=Hyper-V Administrators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Access Control Assistance Operators
distinguishedName: CN=Access Control Assistance Operators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Remote Management Users
distinguishedName: CN=Remote Management Users,CN=Builtin,DC=tombwatcher,DC=htb

cn: Storage Replica Administrators
distinguishedName: CN=Storage Replica Administrators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Domain Computers
distinguishedName: CN=Domain Computers,CN=Users,DC=tombwatcher,DC=htb

cn: Domain Controllers
distinguishedName: CN=Domain Controllers,CN=Users,DC=tombwatcher,DC=htb

cn: Schema Admins
distinguishedName: CN=Schema Admins,CN=Users,DC=tombwatcher,DC=htb

cn: Enterprise Admins
distinguishedName: CN=Enterprise Admins,CN=Users,DC=tombwatcher,DC=htb

cn: Cert Publishers
distinguishedName: CN=Cert Publishers,CN=Users,DC=tombwatcher,DC=htb

cn: Domain Admins
distinguishedName: CN=Domain Admins,CN=Users,DC=tombwatcher,DC=htb

cn: Domain Users
distinguishedName: CN=Domain Users,CN=Users,DC=tombwatcher,DC=htb

cn: Domain Guests
distinguishedName: CN=Domain Guests,CN=Users,DC=tombwatcher,DC=htb

cn: Group Policy Creator Owners
distinguishedName: CN=Group Policy Creator Owners,CN=Users,DC=tombwatcher,DC=htb

cn: RAS and IAS Servers
distinguishedName: CN=RAS and IAS Servers,CN=Users,DC=tombwatcher,DC=htb

cn: Server Operators
distinguishedName: CN=Server Operators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Account Operators
distinguishedName: CN=Account Operators,CN=Builtin,DC=tombwatcher,DC=htb

cn: Pre-Windows 2000 Compatible Access
distinguishedName: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=tombwatcher,DC=htb

cn: Incoming Forest Trust Builders
distinguishedName: CN=Incoming Forest Trust Builders,CN=Builtin,DC=tombwatcher,DC=htb

cn: Windows Authorization Access Group
distinguishedName: CN=Windows Authorization Access Group,CN=Builtin,DC=tombwatcher,DC=htb

cn: Terminal Server License Servers
distinguishedName: CN=Terminal Server License Servers,CN=Builtin,DC=tombwatcher,DC=htb

cn: Allowed RODC Password Replication Group
distinguishedName: CN=Allowed RODC Password Replication Group,CN=Users,DC=tombwatcher,DC=htb

cn: Denied RODC Password Replication Group
distinguishedName: CN=Denied RODC Password Replication Group,CN=Users,DC=tombwatcher,DC=htb

cn: Read-only Domain Controllers
distinguishedName: CN=Read-only Domain Controllers,CN=Users,DC=tombwatcher,DC=htb

cn: Enterprise Read-only Domain Controllers
distinguishedName: CN=Enterprise Read-only Domain Controllers,CN=Users,DC=tombwatcher,DC=htb

cn: Cloneable Domain Controllers
distinguishedName: CN=Cloneable Domain Controllers,CN=Users,DC=tombwatcher,DC=htb

cn: Protected Users
distinguishedName: CN=Protected Users,CN=Users,DC=tombwatcher,DC=htb

cn: Key Admins
distinguishedName: CN=Key Admins,CN=Users,DC=tombwatcher,DC=htb

cn: Enterprise Key Admins
distinguishedName: CN=Enterprise Key Admins,CN=Users,DC=tombwatcher,DC=htb

cn: DnsAdmins
distinguishedName: CN=DnsAdmins,CN=Users,DC=tombwatcher,DC=htb

cn: DnsUpdateProxy
distinguishedName: CN=DnsUpdateProxy,CN=Users,DC=tombwatcher,DC=htb

cn: Infrastructure
distinguishedName: CN=Infrastructure,CN=Users,DC=tombwatcher,DC=htb


[*] Bye!
```
Computers:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.72 -u henry@tombwatcher.htb -p "H3nry_987TGV!" --computers                                                                
[+] Using Domain Controller at: 10.10.11.72
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=tombwatcher,DC=htb
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:TOMBWATCHER\Henry

[+] Enumerating all AD computers
[+]     Found 4 computers: 

cn: DC01
operatingSystem: Windows Server 2019 Standard
operatingSystemVersion: 10.0 (17763)
dNSHostName: DC01.tombwatcher.htb

cn: ansible_dev
dNSHostName: TOMBWATCHER.HTB

cn: MYPC

cn: ControlledComputer
dNSHostName: ControlledComputer.tombwatcher.htb


[*] Bye!
```
# SMB
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# smbmap -H 10.10.11.72 -u "henry" -p "H3nry_987TGV!" -d tombwatcher.htb

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB                                                                                                  
[*] Established 1 SMB connections(s) and 1 authenticated session(s)                                                          
                                                                                                                             
[+] IP: 10.10.11.72:445 Name: 10.10.11.72               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections
```
Exploring IPC$:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# smbmap -H 10.10.11.72 -u "henry" -p "H3nry_987TGV!" -d tombwatcher.htb -r IPC$ --depth 10
\
    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB                                                                                                  
[*] Established 1 SMB connections(s) and 1 authenticated session(s)                                                          
                                                                                                                             
[+] IP: 10.10.11.72:445 Name: 10.10.11.72               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        ./IPC$
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    InitShutdown
        fr--r--r--                4 Mon Jan  1 10:04:52 1601    lsass
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    ntsvcs
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    scerpc
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-3ac-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    epmapper
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-1d0-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    LSM_API_service
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    eventlog
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-1c8-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    atsvc
        fr--r--r--                4 Mon Jan  1 10:04:52 1601    wkssvc
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-270-0
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-270-1
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-524-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    RpcProxy\49685
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    27417691dad3b958
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    RpcProxy\593
        fr--r--r--                4 Mon Jan  1 10:04:52 1601    srvsvc
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    efsrpc
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    netdfs
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    vgauth-service
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-25c-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    W32TIME_ALT
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-918-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    cert
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-89c-0
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-8e4-0
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections 
```
Exploring NETLOGON:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# smbmap -H 10.10.11.72 -u "henry" -p "H3nry_987TGV!" -d tombwatcher.htb -r NETLOGON --depth 10                                                                      

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB                                                                                                  
[*] Established 1 SMB connections(s) and 1 authenticated session(s)                                                          
                                                                                                                             
[+] IP: 10.10.11.72:445 Name: 10.10.11.72               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        ./NETLOGON
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections
```
Exploring SYSVOL:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/TombWatcher/windapsearch]
└─# smbmap -H 10.10.11.72 -u "henry" -p "H3nry_987TGV!" -d tombwatcher.htb -r SYSVOL --depth 10                                                                        

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB                                                                                                  
[*] Established 1 SMB connections(s) and 1 authenticated session(s)                                                          
                                                                                                                             
[+] IP: 10.10.11.72:445 Name: 10.10.11.72               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
        ./SYSVOL
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    tombwatcher.htb
        ./SYSVOL//tombwatcher.htb
        dr--r--r--                0 Sat Nov 16 11:08:10 2024    .
        dr--r--r--                0 Sat Nov 16 11:08:10 2024    ..
        dr--r--r--                0 Mon Jun  9 13:13:27 2025    DfsrPrivate
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    Policies
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    scripts
        ./SYSVOL//tombwatcher.htb/Policies
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    {31B2F340-016D-11D2-945F-00C04FB984F9}
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    {6AC1786C-016F-11D2-945F-00C04fB984F9}
        ./SYSVOL//tombwatcher.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        fr--r--r--               22 Sat Apr 26 00:57:04 2025    GPT.INI
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    MACHINE
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    USER
        ./SYSVOL//tombwatcher.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    Microsoft
        ./SYSVOL//tombwatcher.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    Windows NT
        ./SYSVOL//tombwatcher.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Sat Apr 26 00:57:04 2025    SecEdit
        ./SYSVOL//tombwatcher.htb/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit
        dr--r--r--                0 Sat Apr 26 00:57:04 2025    .
        dr--r--r--                0 Sat Apr 26 00:57:04 2025    ..
        fr--r--r--             1098 Sat Apr 26 00:57:04 2025    GptTmpl.inf
        ./SYSVOL//tombwatcher.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        fr--r--r--               22 Mon Jun  9 14:09:42 2025    GPT.INI
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    MACHINE
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    USER
        ./SYSVOL//tombwatcher.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    Microsoft
        ./SYSVOL//tombwatcher.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    Windows NT
        ./SYSVOL//tombwatcher.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    .
        dr--r--r--                0 Sat Nov 16 11:01:46 2024    ..
        dr--r--r--                0 Mon Jun  9 14:09:42 2025    SecEdit
        ./SYSVOL//tombwatcher.htb/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit
        dr--r--r--                0 Mon Jun  9 14:09:42 2025    .
        dr--r--r--                0 Mon Jun  9 14:09:42 2025    ..
        fr--r--r--             4920 Mon Jun  9 14:09:42 2025    GptTmpl.inf
[*] Closed 1 connections  
```
