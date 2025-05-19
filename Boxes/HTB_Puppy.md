# Puppy
## Findings
- Stephen as admin account (step.cooper_adm)
- Adam is a developer and account is blocked/disabled
- /lvRxjnmZBA is empty, UltFsQYRGg.txt is empty, GptTmpl.inf, 

## NMAP
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# nmap -sV -sC -Pn 10.10.11.70                                                                                                                           
Starting Nmap 7.95 ( https://nmap.org ) at 2025-05-18 14:31 AEST
Nmap scan report for 10.10.11.70
Host is up (0.20s latency).
Not shown: 985 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-05-18 11:31:31Z)
111/tcp  open  rpcbind?
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: PUPPY.HTB0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
2049/tcp open  rpcbind
3260/tcp open  iscsi?
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: PUPPY.HTB0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 187.14 seconds
```

---

# LDAP Enum (389)
- Ran `ldapdomaindump` with little luck:
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ldapdomaindump 10.10.11.70                                                                                                                                         
[*] Connecting as anonymous user, dumping will probably fail. Consider specifying a username/password to login with
[*] Connecting to host...
[*] Binding to host
[+] Bind OK
[*] Starting domain dump
[+] Domain dump finished
```
- Ran enum4linux also with very little luck, but got the domain:
```py 
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# enum4linux -a 10.10.11.70                                                                                                     
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun May 18 14:48:47 2025
--Cut short becuause it's very verbose--

 =================================( Getting domain SID for 10.10.11.70 )=================================
                  
Domain Name: PUPPY                                                                                                                                                     
Domain Sid: S-1-5-21-1487982659-1829050783-2281216199

[+] Host is part of a domain (not a workgroup)     
```
- `ldapsearch` turned up some stuff I think
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ldapsearch -x -H ldap://10.10.11.70 -b "" -s base                                                                                                                  
---SNIP---

isSynchronized: TRUE
highestCommittedUSN: 172163
dsServiceName: CN=NTDS Settings,CN=DC,CN=Servers,CN=Default-First-Site-Name,CN
 =Sites,CN=Configuration,DC=PUPPY,DC=HTB
dnsHostName: DC.PUPPY.HTB
defaultNamingContext: DC=PUPPY,DC=HTB
currentTime: 20250518115159.0Z
configurationNamingContext: CN=Configuration,DC=PUPPY,DC=HTB

# search result
search: 2
result: 0 Success

# numResponses: 2
# numEntries: 1
```
- Now that I have the Domain name I can try to dump all data anonymously:
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ldapsearch -x -H ldap://10.10.11.70 -b "dc=PUPPY,dc=HTB"                                                                                                   
# extended LDIF
#
# LDAPv3
# base <dc=PUPPY,dc=HTB> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090DA9, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4f7c

# numResponses: 1

```
- The error message indicates that anonymous searching of the directory is not allowed - you need to authenticate first. Gippity says to try NULL bind:
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ldapsearch -x -H ldap://10.10.11.70 -D "" -w "" -b "dc=PUPPY,dc=HTB"                                                                                               
# extended LDIF
#
# LDAPv3
# base <dc=PUPPY,dc=HTB> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090DA9, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4f7c

# numResponses: 1
```
- NULL bind doesn't work (sending empty username and password with -D "" -w ""), and received the same operations error. This means the server requires actual credentials for authentication.
- Security is properly configured: LDAP server has been configured to prevent unauthenticated access to the directory contents.
- "000004DC" error code is a hexadecimal Active Directory error code that translates to "LDAP_OPERATIONS_ERROR" (1244 in decimal), which is a generic error indicating the server can't process your request due to security restrictions.

Perhaps LDAP is not the entry point?

How about we try those handy credentials: 

```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ldapsearch -x -H ldap://10.10.11.70 -D "levi.james@PUPPY.HTB" -w "KingofAkron2025!" -b "dc=PUPPY,dc=HTB"
- Output far to large to copy here but there's a lot of info.
```
 
- IMPORTANT: Tried windapsearch.py with different flags but kept getting 'invalid credentials', windapsearch.py is super super fussy so make sure the syntax is correct - look at below carefully - same command but structured differently - but one with a slightly misleading error message:
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --computers
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james

[+] Enumerating all AD computers
[+]     Found 1 computers: 

cn: DC
operatingSystem: Windows Server 2022 Standard
operatingSystemVersion: 10.0 (20348)
dNSHostName: DC.PUPPY.HTB

[*] Bye!

┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -d PUPPY.HTB -u levi.james -p "KingofAkron2025!" --computers
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[!] Error: invalid credentials

```
- Ran `--da` flag for domain admins
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --da
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james
[+] Attempting to enumerate all Domain Admins
[+] Using DN: CN=Domain Admins,CN=Users.CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB
[+]     Found 1 Domain Admins:

cn: Administrator

[+] Using DN: CN=Domain Admins,CN=Users.CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB
[+]     Found 1 Domain Admins:

cn: Administrator -------------------------------

[*] Bye!

```
Asked windapsearch to enumerate all members of Administrators group (`--members Administrators`)
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --members Administrators                                                 
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james
[+] Attempting to enumerate full DN for group: Administrators
[+]      Using DN: CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB

[+]      Found 4 members:

b'CN=Stephen A. Cooper_adm,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB' ---------------------------------
b'CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB'
b'CN=Enterprise Admins,CN=Users,DC=PUPPY,DC=HTB'
b'CN=Administrator,CN=Users,DC=PUPPY,DC=HTB'

[*] Bye!

```
- For GPOS
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --gpos
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james
[+] Attempting to enumerate all group policy objects
[+]     Found 3 GPOs:

displayName: Default Domain Policy
gPCFileSysPath: \\PUPPY.HTB\sysvol\PUPPY.HTB\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}

displayName: Default Domain Controllers Policy
gPCFileSysPath: \\PUPPY.HTB\sysvol\PUPPY.HTB\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}

displayName: DisableDefender
gPCFileSysPath: \\PUPPY.HTB\SysVol\PUPPY.HTB\Policies\{841B611C-9F3B-4090-BA0C-2AE4D6C02AF8}


[*] Bye!
```
- For all admin objects
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --admin-objects
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james
[+] Attempting to enumerate all admin (protected) objects
[+]     Found 17 Admin Objects:

CN=Administrator,CN=Users,DC=PUPPY,DC=HTB

CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB

CN=Print Operators,CN=Builtin,DC=PUPPY,DC=HTB

CN=Backup Operators,CN=Builtin,DC=PUPPY,DC=HTB

CN=Replicator,CN=Builtin,DC=PUPPY,DC=HTB

CN=krbtgt,CN=Users,DC=PUPPY,DC=HTB

CN=Domain Controllers,CN=Users,DC=PUPPY,DC=HTB

CN=Schema Admins,CN=Users,DC=PUPPY,DC=HTB

CN=Enterprise Admins,CN=Users,DC=PUPPY,DC=HTB

CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB

CN=Server Operators,CN=Builtin,DC=PUPPY,DC=HTB

CN=Account Operators,CN=Builtin,DC=PUPPY,DC=HTB

CN=Read-only Domain Controllers,CN=Users,DC=PUPPY,DC=HTB

CN=Key Admins,CN=Users,DC=PUPPY,DC=HTB

CN=Enterprise Key Admins,CN=Users,DC=PUPPY,DC=HTB

CN=Adam D. Silver,CN=Users,DC=PUPPY,DC=HTB ----------------------------------------

CN=Stephen A. Cooper_adm,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB -----------------------------------


[*] Bye!
```
- For users
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --users
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james

[+] Enumerating all AD users
[+]     Found 9 users: 

cn: Administrator

cn: Guest

cn: krbtgt

cn: Levi B. James
userPrincipalName: levi.james@PUPPY.HTB

cn: Anthony J. Edwards
userPrincipalName: ant.edwards@PUPPY.HTB

cn: Adam D. Silver
userPrincipalName: adam.silver@PUPPY.HTB

cn: Jamie S. Williams
userPrincipalName: jamie.williams@PUPPY.HTB

cn: Stephen W. Cooper
userPrincipalName: steph.cooper@PUPPY.HTB

cn: Stephen A. Cooper_adm
userPrincipalName: steph.cooper_adm@PUPPY.HTB


[*] Bye!
```
- Stephen has a user account and an admin account
- Password policy
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --custom "(objectClass=domainDNS)" --attrs pwdProperties,lockoutThreshold,minPwdLength,maxPwdAge,minPwdAge,lockoutDuration,pwdHistoryLength
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james
[+] Performing custom lookup with filter: "(objectClass=domainDNS)"
[+]     Found 1 results:

DC=PUPPY,DC=HTB
lockoutDuration: -18000000000
lockoutThreshold: 0
maxPwdAge: -36288000000000
minPwdAge: -864000000000
minPwdLength: 7
pwdProperties: 1
pwdHistoryLength: 24

[*] Bye!

```
- No threshold = brute force stephen/adam?
- Vulnerable to kerberoasting (Have an SPN, User Accounts / Not computer and hopefully weak passwords
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# python3 windapsearch.py --dc-ip 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!" --custom "(&(objectClass=user)(servicePrincipalName=*)(!(sAMAccountName=krbtgt)))" --attrs sAMAccountName,servicePrincipalName,description,memberOf 
[+] Using Domain Controller at: 10.10.11.70
[+] Getting defaultNamingContext from Root DSE
[+]     Found: DC=PUPPY,DC=HTB
[+] Attempting bind
[+]     ...success! Binded as: 
[+]      u:PUPPY\levi.james
[+] Performing custom lookup with filter: "(&(objectClass=user)(servicePrincipalName=*)(!(sAMAccountName=krbtgt)))"
[+]     Found 1 results:

CN=DC,OU=Domain Controllers,DC=PUPPY,DC=HTB
sAMAccountName: DC$
servicePrincipalName: iSCSITarget/DC
servicePrincipalName: iSCSITarget/DC.PUPPY.HTB
servicePrincipalName: TERMSRV/DC
servicePrincipalName: TERMSRV/DC.PUPPY.HTB
servicePrincipalName: Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/DC.PUPPY.HTB
servicePrincipalName: ldap/DC.PUPPY.HTB/ForestDnsZones.PUPPY.HTB
servicePrincipalName: ldap/DC.PUPPY.HTB/DomainDnsZones.PUPPY.HTB
servicePrincipalName: DNS/DC.PUPPY.HTB
servicePrincipalName: GC/DC.PUPPY.HTB/PUPPY.HTB
servicePrincipalName: RestrictedKrbHost/DC.PUPPY.HTB
servicePrincipalName: RestrictedKrbHost/DC
servicePrincipalName: RPC/2bea3ff3-b80d-42a2-8a63-39ee389db252._msdcs.PUPPY.HTB
servicePrincipalName: HOST/DC/PUPPY
servicePrincipalName: HOST/DC.PUPPY.HTB/PUPPY
servicePrincipalName: HOST/DC
servicePrincipalName: HOST/DC.PUPPY.HTB
servicePrincipalName: HOST/DC.PUPPY.HTB/PUPPY.HTB
servicePrincipalName: E3514235-4B06-11D1-AB04-00C04FC2DCD2/2bea3ff3-b80d-42a2-8a63-39ee389db252/PUPPY.HTB
servicePrincipalName: ldap/DC/PUPPY
servicePrincipalName: ldap/2bea3ff3-b80d-42a2-8a63-39ee389db252._msdcs.PUPPY.HTB
servicePrincipalName: ldap/DC.PUPPY.HTB/PUPPY
servicePrincipalName: ldap/DC
servicePrincipalName: ldap/DC.PUPPY.HTB
servicePrincipalName: ldap/DC.PUPPY.HTB/PUPPY.HTB
```
- Doesn't look like anything or anyone interesting to kerberoast
---

# WinRM (5985)
- Try for shell with 3 different variations of commands but levi doesn't seem to have authZ
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# evil-winrm -i 10.10.11.70 -u levi.james@PUPPY.HTB -p "KingofAkron2025!"                                                                                            
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
                                        
Error: Exiting with code 1

┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# evil-winrm -i 10.10.11.70 -u levi.james -p "KingofAkron2025!"
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
                                        
Error: Exiting with code 1

┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# evil-winrm -i 10.10.11.70 -u PUPPY\\levi.james -p "KingofAkron2025!"                                                                                               
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
                                        
Error: Exiting with code 1

```
- Hail mary attempt at stephens admin account 
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# evil-winrm -i 10.10.11.70 -u steph.cooper_adm@PUPPY.HTB -p "KingofAkron2025!"                                                                                      
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
                                        
Error: Exiting with code 1
```

# SMB Enum (445)
- List shares anonmously:
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# smbclient -L //10.10.11.70 -N                                                                                                                                      
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.70 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
- also specifying the domain:
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# smbclient -L //10.10.11.70 -N -W PUPPY                                                                                                        
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.70 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

```
- Check for NULL sessions:
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# smbmap -H 10.10.11.70 -u "" -p ""                                                                                                                                  

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

[*] Detected 0 hosts serving SMB                                                                                                  
[*] Closed 0 connections 
```

---

Now let's try those creds baby
```py
┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbclient -L //10.10.11.70 -U "levi.james%KingofAkron2025!"                                                                                                        

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        DEV             Disk      DEV-SHARE for PUPPY-DEVS
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.70 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
- Access to ADMIN$ + C$ denied, but not for others.
```py
┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbclient //10.10.11.70/ADMIN$ -U "levi.james%KingofAkron2025!"                                                                                                    
tree connect failed: NT_STATUS_ACCESS_DENIED

┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbclient //10.10.11.70/SYSVOL -U "levi.james%KingofAkron2025!"                                                                                                    
Try "help" to get a list of possible commands.
smb: \> 
```
- DEV seems to have permissions over commands?
```py
┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbclient //10.10.11.70/DEV -U "levi.james%KingofAkron2025!"                                                                                                    
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_ACCESS_DENIED listing \*
```
- SMBMAP was a lot clearer
```py
┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbmap -H 10.10.11.70 -u "levi.james" -p "KingofAkron2025!" -d PUPPY.HTB                                                                                           

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
                                                                                                                             
[+] IP: 10.10.11.70:445 Name: 10.10.11.70               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        DEV                                                     NO ACCESS       DEV-SHARE for PUPPY-DEVS
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections
```
- God dam SMBMAP has a depth flag - this is SYSLOG
```py
┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbmap -H 10.10.11.70 -u "levi.james" -p "KingofAkron2025!" -d PUPPY.HTB -r SYSVOL --depth 10

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
                                                                                                                             
[+] IP: 10.10.11.70:445 Name: 10.10.11.70               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        DEV                                                     NO ACCESS       DEV-SHARE for PUPPY-DEVS
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
        ./SYSVOL
        dr--r--r--                0 Fri Mar 21 16:33:44 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        dr--r--r--                0 Fri Mar 21 16:33:44 2025    lvRxjnmZBA
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    PUPPY.HTB
        fr--r--r--                0 Fri Mar 21 16:33:44 2025    UltFsQYRGg.txt
        ./SYSVOL//PUPPY.HTB
        dr--r--r--                0 Wed Feb 19 22:46:56 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        dr--r--r--                0 Mon May 19 22:06:14 2025    DfsrPrivate
        dr--r--r--                0 Wed May 14 09:42:57 2025    Policies
        dr--r--r--                0 Fri Mar 21 16:33:44 2025    scripts
        ./SYSVOL//PUPPY.HTB/Policies
        dr--r--r--                0 Wed May 14 09:42:57 2025    .
        dr--r--r--                0 Wed Feb 19 22:46:56 2025    ..
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    {31B2F340-016D-11D2-945F-00C04FB984F9}
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    {6AC1786C-016F-11D2-945F-00C04fB984F9}
        dr--r--r--                0 Wed May 14 09:42:57 2025    {841B611C-9F3B-4090-BA0C-2AE4D6C02AF8}
        ./SYSVOL//PUPPY.HTB/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    .
        dr--r--r--                0 Wed May 14 09:42:57 2025    ..
        fr--r--r--               22 Wed Feb 19 22:49:00 2025    GPT.INI
        dr--r--r--                0 Wed Feb 19 22:49:00 2025    MACHINE
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    USER
        ./SYSVOL//PUPPY.HTB/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE
        dr--r--r--                0 Thu May 15 02:54:14 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    Microsoft
        fr--r--r--             2786 Wed Feb 19 22:49:00 2025    Registry.pol
        dr--r--r--                0 Thu May 15 02:54:14 2025    Scripts
        ./SYSVOL//PUPPY.HTB/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    .
        dr--r--r--                0 Thu May 15 02:54:14 2025    ..
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    Windows NT
        ./SYSVOL//PUPPY.HTB/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    SecEdit
        ./SYSVOL//PUPPY.HTB/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Microsoft/Windows NT/SecEdit
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        fr--r--r--             1098 Wed Feb 19 22:45:20 2025    GptTmpl.inf
        ./SYSVOL//PUPPY.HTB/Policies/{31B2F340-016D-11D2-945F-00C04FB984F9}/MACHINE/Scripts
        dr--r--r--                0 Thu May 15 02:54:14 2025    .
        dr--r--r--                0 Thu May 15 02:54:14 2025    ..
        dr--r--r--                0 Thu May 15 02:54:14 2025    Shutdown
        dr--r--r--                0 Thu May 15 02:54:14 2025    Startup
        ./SYSVOL//PUPPY.HTB/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    .
        dr--r--r--                0 Wed May 14 09:42:57 2025    ..
        fr--r--r--               23 Thu May 15 02:53:36 2025    GPT.INI
        dr--r--r--                0 Tue May 13 09:50:46 2025    MACHINE
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    USER
        ./SYSVOL//PUPPY.HTB/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE
        dr--r--r--                0 Tue May 13 09:50:46 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        dr--r--r--                0 Tue May 13 12:03:29 2025    Applications
        fr--r--r--              554 Tue May 13 09:50:46 2025    comment.cmtx
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    Microsoft
        fr--r--r--              984 Tue May 13 09:50:46 2025    Registry.pol
        dr--r--r--                0 Tue May 13 09:27:17 2025    Scripts
        ./SYSVOL//PUPPY.HTB/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    .
        dr--r--r--                0 Tue May 13 09:50:46 2025    ..
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    Windows NT
        ./SYSVOL//PUPPY.HTB/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        dr--r--r--                0 Tue May 13 09:27:41 2025    SecEdit --------------------------------------------
        ./SYSVOL//PUPPY.HTB/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Microsoft/Windows NT/SecEdit
        dr--r--r--                0 Thu May 15 02:53:36 2025    .
        dr--r--r--                0 Wed Feb 19 22:45:20 2025    ..
        fr--r--r--             4382 Thu May 15 02:53:36 2025    GptTmpl.inf
        ./SYSVOL//PUPPY.HTB/Policies/{6AC1786C-016F-11D2-945F-00C04fB984F9}/MACHINE/Scripts
        dr--r--r--                0 Tue May 13 09:27:17 2025    .
        dr--r--r--                0 Tue May 13 09:50:46 2025    ..
        dr--r--r--                0 Tue May 13 09:27:17 2025    Shutdown
        dr--r--r--                0 Tue May 13 09:27:17 2025    Startup
        ./SYSVOL//PUPPY.HTB/Policies/{841B611C-9F3B-4090-BA0C-2AE4D6C02AF8}
        dr--r--r--                0 Wed May 14 09:42:57 2025    .
        dr--r--r--                0 Wed May 14 09:42:57 2025    ..
        fr--r--r--               59 Wed May 14 09:48:05 2025    GPT.INI
        dr--r--r--                0 Wed May 14 09:48:05 2025    Machine
        dr--r--r--                0 Wed May 14 09:42:57 2025    User
        ./SYSVOL//PUPPY.HTB/Policies/{841B611C-9F3B-4090-BA0C-2AE4D6C02AF8}/Machine
        dr--r--r--                0 Wed May 14 09:48:05 2025    .
        dr--r--r--                0 Wed May 14 09:42:57 2025    ..
        fr--r--r--              888 Wed May 14 09:48:05 2025    Registry.pol
[*] Closed 1 connections
```
- Scripts dir is empty, weird.txtfile is empty, Registry.pol just talks about disbaling defender, comment.cmtx is some XML describing defender
- This is NETLOGON
```py
┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbmap -H 10.10.11.70 -u "levi.james" -p "KingofAkron2025!" -d PUPPY.HTB -r NETLOGON --depth 10                                                                    

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
                                                                                                                             
[+] IP: 10.10.11.70:445 Name: 10.10.11.70               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        DEV                                                     NO ACCESS       DEV-SHARE for PUPPY-DEVS
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                READ ONLY       Logon server share 
        ./NETLOGON
        dr--r--r--                0 Fri Mar 21 16:33:44 2025    .
        dr--r--r--                0 Wed Feb 19 22:46:56 2025    ..
        SYSVOL                                                  READ ONLY       Logon server share 
[*] Closed 1 connections                                                                                                     
```
- And this is IPC$
```py
┌──(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# smbmap -H 10.10.11.70 -u "levi.james" -p "KingofAkron2025!" -d PUPPY.HTB -r IPC$ --depth 10                                                                    

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
                                                                                                                             
[+] IP: 10.10.11.70:445 Name: 10.10.11.70               Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        DEV                                                     NO ACCESS       DEV-SHARE for PUPPY-DEVS
        IPC$                                                    READ ONLY       Remote IPC
        ./IPC$
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    InitShutdown
        fr--r--r--                4 Mon Jan  1 10:04:52 1601    lsass
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    ntsvcs
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    scerpc
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-2b4-0
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-3a0-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    epmapper
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-218-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    LSM_API_service
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-374-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    eventlog
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-354-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    atsvc
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-1b4-0
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-2b4-1
        fr--r--r--                5 Mon Jan  1 10:04:52 1601    wkssvc
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    RpcProxy\49670
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    8df8d00805df4a69
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    RpcProxy\593
        fr--r--r--                4 Mon Jan  1 10:04:52 1601    srvsvc
        fr--r--r--                4 Mon Jan  1 10:04:52 1601    netdfs
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    vgauth-service
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    tapsrv
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-2a4-0
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    ROUTER
        fr--r--r--                3 Mon Jan  1 10:04:52 1601    W32TIME_ALT
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-838-0
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
        fr--r--r--                1 Mon Jan  1 10:04:52 1601    Winsock2\CatalogChangeListener-830-0
        NETLOGON                                                READ ONLY       Logon server share 
        SYSVOL                                                  READ ONLY       Logon server share 
```
  


# RPC Enum (125)
- Try null session with rpcclient
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# rpcclient -U "" -N 10.10.11.70                                                                                                                                     
rpcclient $> enumdomusers
result was NT_STATUS_ACCESS_DENIED
rpcclient $> administrator
command not found: administrator
rpcclient $> lookupnames
Usage: lookupnames [name1 [name2 [...]]]
rpcclient $> lookupnames administrator
result was NT_STATUS_ACCESS_DENIED
rpcclient $> 
```

---

# DNS Enum
- Attempt zone transfer
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# dig @10.10.11.70 PUPPY.HTB axfr

; <<>> DiG 9.20.7-1-Debian <<>> @10.10.11.70 PUPPY.HTB axfr
; (1 server found)
;; global options: +cmd
; Transfer failed.
```
- Resolve hostnames - seem to be having connection issues? or DC not responding to me
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# nslookup dc.PUPPY.HTB 10.10.11.70                                                                                                                                  
Server:         10.10.11.70
Address:        10.10.11.70#53

Name:   dc.PUPPY.HTB
Address: 10.10.11.70
;; communications error to 10.10.11.70#53: timed out

```
- Check for SRV records:
```py
  ┌──(root㉿kali)-[/home/jacob/Desktop]
└─# nslookup -type=SRV _ldap._tcp.PUPPY.HTB 10.10.11.70                                                                                                                
Server:         10.10.11.70
Address:        10.10.11.70#53

_ldap._tcp.PUPPY.HTB    service = 0 100 389 dc.puppy.htb.

```
- Look for other potential subdomains
```py
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# fierce --domain PUPPY.HTB --dns-servers 10.10.11.70                                                                                                                
NS: failure
SOA: failure
Failed to lookup NS/SOA, Domain does not exist
```
# Kerberos Enum (88)
users.txt 
```
administrator
levi.james
ant.edwards
adam.silver
jamie.williams
steph.cooper
steph.cooper_adm
```

- Kerbrute 
```py
┌──(v-env)(root㉿kali)-[/home/jacob/Desktop/Boxes/Puppy/windapsearch]
└─# kerbrute -dc-ip 10.10.11.70 -domain PUPPY.HTB -users users.txt                                                                                          
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Valid user => administrator
[*] Valid user => levi.james
[*] Valid user => ant.edwards
[*] Blocked/Disabled user => adam.silver
[*] Valid user => jamie.williams
[*] Valid user => steph.cooper
[*] Valid user => steph.cooper_adm
[*] No passwords were discovered :'(
```
- Why is adam blocked
---

# Working Steps
# Lessons
- Regular NMAP scan doesn't return anything - have to use `-Pn`  flag.  `-Pn: Treat all hosts as online -- skip host discovery`
- Try specifying the domain when enumerating SMB/LDAP
- A timeout could just be a VPN thing dude
- windapsearch.py is super fussy about it's command syntax. It'll say 'invalid crednetials' if it's not happy with you and you're 90% confident you have the right perms
- Don't forget that linux commands wont work in SMB lol
