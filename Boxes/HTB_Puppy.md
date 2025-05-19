# Puppy
## NMAP
```
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
```
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
```
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
```
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
```
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
```
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

```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ldapsearch -x -H ldap://10.10.11.70 -D "levi.james@PUPPY.HTB" -w "KingofAkron2025!" -b "dc=PUPPY,dc=HTB"
- Output far to large to copy here but there's a lot of info.
```
Tried grepping with context
```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# ldapsearch -x -H ldap://10.10.11.70 -D "levi.james@PUPPY.HTB" -w "KingofAkron2025!" -b "dc=PUPPY,dc=HTB" | grep -i -C 2 admin                                      
 ,DC=PUPPY,DC=HTB

# AdminSDHolder, System, PUPPY.HTB
dn: CN=AdminSDHolder,CN=System,DC=PUPPY,DC=HTB
objectClass: top
objectClass: container
cn: AdminSDHolder
distinguishedName: CN=AdminSDHolder,CN=System,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114511.0Z
--
uSNChanged: 12768
showInAdvancedViewOnly: TRUE
name: AdminSDHolder
objectGUID:: k7aHsM48YUK7uzf98Shx1g==
systemFlags: -1946157056
--
dn: CN=TPM Devices,DC=PUPPY,DC=HTB

# Administrator, Users, PUPPY.HTB
dn: CN=Administrator,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Administrator
description: Built-in account for administering the computer/domain
distinguishedName: CN=Administrator,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114512.0Z
--
uSNCreated: 8196
memberOf: CN=Group Policy Creator Owners,CN=Users,DC=PUPPY,DC=HTB
memberOf: CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB
memberOf: CN=Enterprise Admins,CN=Users,DC=PUPPY,DC=HTB
memberOf: CN=Schema Admins,CN=Users,DC=PUPPY,DC=HTB
memberOf: CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB
uSNChanged: 147540
name: Administrator
objectGUID:: dz7raIuZRUSHbobwIRQqfg==
userAccountControl: 1114624
--
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiH9AEAAA==
adminCount: 1
accountExpires: 9223372036854775807
logonCount: 103
sAMAccountName: Administrator
sAMAccountType: 805306368
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=PUPPY,DC=HTB
--
dSCorePropagationData: 16010101000416.0Z

# Administrators, Builtin, PUPPY.HTB
dn: CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Administrators
description: Administrators have complete and unrestricted access to the compu
 ter/domain
member: CN=Stephen A. Cooper_adm,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
member: CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB
member: CN=Enterprise Admins,CN=Users,DC=PUPPY,DC=HTB
member: CN=Administrator,CN=Users,DC=PUPPY,DC=HTB
distinguishedName: CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114512.0Z
--
uSNCreated: 8199
uSNChanged: 45139
name: Administrators
objectGUID:: yYAcjBJMd0i77HDE3kPxDA==
objectSid:: AQIAAAAAAAUgAAAAIAIAAA==
adminCount: 1
sAMAccountName: Administrators
sAMAccountType: 536870912
systemFlags: -1946157056
--
objectClass: group
cn: Print Operators
description: Members can administer printers installed on domain controllers
distinguishedName: CN=Print Operators,CN=Builtin,DC=PUPPY,DC=HTB
instanceType: 4
--
objectGUID:: XSuB2a9kOEONPtXgYuUO6g==
objectSid:: AQIAAAAAAAUgAAAAJgIAAA==
adminCount: 1
sAMAccountName: Print Operators
sAMAccountType: 536870912
--
objectGUID:: PBC1w1rRiUeuahxouNU+1w==
objectSid:: AQIAAAAAAAUgAAAAJwIAAA==
adminCount: 1
sAMAccountName: Backup Operators
sAMAccountType: 536870912
--
objectGUID:: K9cr4qG1fkCKiiNg6fOPSw==
objectSid:: AQIAAAAAAAUgAAAAKAIAAA==
adminCount: 1
sAMAccountName: Replicator
sAMAccountType: 536870912
--
objectClass: group
cn: Network Configuration Operators
description: Members in this group can have some administrative privileges to 
 manage configuration of networking features
distinguishedName: CN=Network Configuration Operators,CN=Builtin,DC=PUPPY,DC=H
--
objectClass: group
cn: RDS Management Servers
description: Servers in this group can perform routine administrative actions 
 on servers running Remote Desktop Services. This group needs to be populated 
 on all servers in a Remote Desktop Services deployment. The servers running t
--
dSCorePropagationData: 16010101000001.0Z

# Hyper-V Administrators, Builtin, PUPPY.HTB
dn: CN=Hyper-V Administrators,CN=Builtin,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Hyper-V Administrators
description: Members of this group have complete and unrestricted access to al
 l features of Hyper-V.
distinguishedName: CN=Hyper-V Administrators,CN=Builtin,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114512.0Z
--
uSNCreated: 8229
uSNChanged: 8229
name: Hyper-V Administrators
objectGUID:: 63aTeCZY10GRvMWNBRxzZw==
objectSid:: AQIAAAAAAAUgAAAAQgIAAA==
sAMAccountName: Hyper-V Administrators
sAMAccountType: 536870912
systemFlags: -1946157056
--
 otocols (such as WS-Management via the Windows Remote Management service). Th
 is applies only to WMI namespaces that grant access to the user.
member: CN=Stephen W. Cooper,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
member: CN=Adam D. Silver,CN=Users,DC=PUPPY,DC=HTB
distinguishedName: CN=Remote Management Users,CN=Builtin,DC=PUPPY,DC=HTB
--
dSCorePropagationData: 16010101000001.0Z

# Storage Replica Administrators, Builtin, PUPPY.HTB
dn: CN=Storage Replica Administrators,CN=Builtin,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Storage Replica Administrators
description: Members of this group have complete and unrestricted access to al
 l features of Storage Replica.
distinguishedName: CN=Storage Replica Administrators,CN=Builtin,DC=PUPPY,DC=HT
 B
instanceType: 4
--
uSNCreated: 8232
uSNChanged: 8232
name: Storage Replica Administrators
objectGUID:: 54mKMy9Qhk6zOyrEpLg7PA==
objectSid:: AQIAAAAAAAUgAAAARgIAAA==
sAMAccountName: Storage Replica Administrators
sAMAccountType: 536870912
systemFlags: -1946157056
--
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiH9gEAAA==
adminCount: 1
accountExpires: 9223372036854775807
logonCount: 0
sAMAccountName: krbtgt
sAMAccountType: 805306368
servicePrincipalName: kadmin/changepw
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=PUPPY,DC=HTB
isCriticalSystemObject: TRUE
--
objectGUID:: pIVbZHobtEOTyyrCY8k9pw==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHBAIAAA==
adminCount: 1
sAMAccountName: Domain Controllers
sAMAccountType: 268435456
--
dSCorePropagationData: 16010101000416.0Z

# Schema Admins, Users, PUPPY.HTB
dn: CN=Schema Admins,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Schema Admins
description: Designated administrators of the schema
member: CN=Administrator,CN=Users,DC=PUPPY,DC=HTB
distinguishedName: CN=Schema Admins,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114615.0Z
--
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=PUPPY,DC=HTB
uSNChanged: 12775
name: Schema Admins
objectGUID:: +ZC7JiItOUeuy6Oqc9S6Ng==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHBgIAAA==
adminCount: 1
sAMAccountName: Schema Admins
sAMAccountType: 268435456
groupType: -2147483640
--
dSCorePropagationData: 16010101000416.0Z

# Enterprise Admins, Users, PUPPY.HTB
dn: CN=Enterprise Admins,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Enterprise Admins
description: Designated administrators of the enterprise
member: CN=Administrator,CN=Users,DC=PUPPY,DC=HTB
distinguishedName: CN=Enterprise Admins,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114615.0Z
--
uSNCreated: 12339
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=PUPPY,DC=HTB
memberOf: CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB
uSNChanged: 12769
name: Enterprise Admins
objectGUID:: Ubm0KwjSA0uLAColHaIDSg==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHBwIAAA==
adminCount: 1
sAMAccountName: Enterprise Admins
sAMAccountType: 268435456
groupType: -2147483640
--
dSCorePropagationData: 16010101000001.0Z

# Domain Admins, Users, PUPPY.HTB
dn: CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Domain Admins
description: Designated administrators of the domain
member: CN=Administrator,CN=Users,DC=PUPPY,DC=HTB
distinguishedName: CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114615.0Z
--
uSNCreated: 12345
memberOf: CN=Denied RODC Password Replication Group,CN=Users,DC=PUPPY,DC=HTB
memberOf: CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB
uSNChanged: 12774
name: Domain Admins
objectGUID:: 48PriZzm6kKsowUrkuZOug==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHAAIAAA==
adminCount: 1
sAMAccountName: Domain Admins
sAMAccountType: 268435456
groupType: -2147483646
--
cn: Group Policy Creator Owners
description: Members in this group can modify group policy for the domain
member: CN=Administrator,CN=Users,DC=PUPPY,DC=HTB
distinguishedName: CN=Group Policy Creator Owners,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
--
objectClass: group
cn: Server Operators
description: Members can administer domain servers
distinguishedName: CN=Server Operators,CN=Builtin,DC=PUPPY,DC=HTB
instanceType: 4
--
objectGUID:: htMyJkfWbkCWzStGhzZ86g==
objectSid:: AQIAAAAAAAUgAAAAJQIAAA==
adminCount: 1
sAMAccountName: Server Operators
sAMAccountType: 536870912
--
objectClass: group
cn: Account Operators
description: Members can administer domain user and group accounts
distinguishedName: CN=Account Operators,CN=Builtin,DC=PUPPY,DC=HTB
instanceType: 4
--
objectGUID:: umWLS8w55kmTB/ZHzIsF4Q==
objectSid:: AQIAAAAAAAUgAAAAJAIAAA==
adminCount: 1
sAMAccountName: Account Operators
sAMAccountType: 536870912
--
member: CN=Read-only Domain Controllers,CN=Users,DC=PUPPY,DC=HTB
member: CN=Group Policy Creator Owners,CN=Users,DC=PUPPY,DC=HTB
member: CN=Domain Admins,CN=Users,DC=PUPPY,DC=HTB
member: CN=Cert Publishers,CN=Users,DC=PUPPY,DC=HTB
member: CN=Enterprise Admins,CN=Users,DC=PUPPY,DC=HTB
member: CN=Schema Admins,CN=Users,DC=PUPPY,DC=HTB
member: CN=Domain Controllers,CN=Users,DC=PUPPY,DC=HTB
member: CN=krbtgt,CN=Users,DC=PUPPY,DC=HTB
--
objectGUID:: Nv35nyjbfU+WrTL7iLcrtg==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHCQIAAA==
adminCount: 1
sAMAccountName: Read-only Domain Controllers
sAMAccountType: 268435456
--
dSCorePropagationData: 16010101000001.0Z

# Key Admins, Users, PUPPY.HTB
dn: CN=Key Admins,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Key Admins
description: Members of this group can perform administrative actions on key o
 bjects within the domain.
distinguishedName: CN=Key Admins,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114616.0Z
--
uSNCreated: 12450
uSNChanged: 12772
name: Key Admins
objectGUID:: krvpFbpgS0+EgAJG8sCSIQ==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHDgIAAA==
adminCount: 1
sAMAccountName: Key Admins
sAMAccountType: 268435456
groupType: -2147483646
--
dSCorePropagationData: 16010101000416.0Z

# Enterprise Key Admins, Users, PUPPY.HTB
dn: CN=Enterprise Key Admins,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: Enterprise Key Admins
description: Members of this group can perform administrative actions on key o
 bjects within the forest.
distinguishedName: CN=Enterprise Key Admins,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114616.0Z
--
uSNCreated: 12453
uSNChanged: 12773
name: Enterprise Key Admins
objectGUID:: vaym7QggzkalzYc2xril7w==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHDwIAAA==
adminCount: 1
sAMAccountName: Enterprise Key Admins
sAMAccountType: 268435456
groupType: -2147483640
--
dSCorePropagationData: 16010101000000.0Z

# DnsAdmins, Users, PUPPY.HTB
dn: CN=DnsAdmins,CN=Users,DC=PUPPY,DC=HTB
objectClass: top
objectClass: group
cn: DnsAdmins
description: DNS Administrators Group
distinguishedName: CN=DnsAdmins,CN=Users,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219114655.0Z
--
uSNCreated: 12486
uSNChanged: 12488
name: DnsAdmins
objectGUID:: 45QpVsa2ykKwxtGh1r5XGA==
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHTQQAAA==
sAMAccountName: DnsAdmins
sAMAccountType: 536870912
groupType: -2147483644
--
 C5EggBQ3R4U2hhZG9344Cw44Cw44Cw44CwKgIBQ3R4TWluRW5jcnlwdGlvbkxldmVs44Sw
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHUQQAAA==
adminCount: 1
accountExpires: 9223372036854775807
logonCount: 6
--
lastLogonTimestamp: 133856002855431158

# PUPPY ADMINS, PUPPY.HTB
dn: OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
objectClass: top
objectClass: organizationalUnit
ou: PUPPY ADMINS
distinguishedName: OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219121952.0Z
--
uSNCreated: 12831
uSNChanged: 12832
name: PUPPY ADMINS
objectGUID:: +TB2SYQs2kuP1EgSvIlrmQ==
objectCategory: CN=Organizational-Unit,CN=Schema,CN=Configuration,DC=PUPPY,DC=
--
dSCorePropagationData: 16010101000000.0Z

# Stephen W. Cooper, PUPPY ADMINS, PUPPY.HTB
dn: CN=Stephen W. Cooper,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
objectClass: top
objectClass: person
--
givenName: Stephen
initials: W
distinguishedName: CN=Stephen W. Cooper,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250219122100.0Z
--
dn: CN=BCKUPKEY_PREFERRED Secret,CN=System,DC=PUPPY,DC=HTB

# Stephen A. Cooper_adm, PUPPY ADMINS, PUPPY.HTB
dn: CN=Stephen A. Cooper_adm,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
objectClass: top
objectClass: person
--
givenName: Stephen
initials: A
distinguishedName: CN=Stephen A. Cooper_adm,OU=PUPPY ADMINS,DC=PUPPY,DC=HTB
instanceType: 4
whenCreated: 20250308155040.0Z
--
displayName: Stephen A. Cooper
uSNCreated: 45124
memberOf: CN=Administrators,CN=Builtin,DC=PUPPY,DC=HTB
uSNChanged: 94259
name: Stephen A. Cooper_adm
--
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAAQ9CwWJ8ZBW3HmPiHVwQAAA==
adminCount: 1
accountExpires: 9223372036854775807
logonCount: 0
```

---

# SMB Enum (445)
- List shares anonmously:
```
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
```
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
```
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

# RPC Enum (125)
- Try null session with rpcclient
```
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
```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# dig @10.10.11.70 PUPPY.HTB axfr

; <<>> DiG 9.20.7-1-Debian <<>> @10.10.11.70 PUPPY.HTB axfr
; (1 server found)
;; global options: +cmd
; Transfer failed.
```
- Resolve hostnames - seem to be having connection issues? or DC not responding to me
```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# nslookup dc.PUPPY.HTB 10.10.11.70                                                                                                                                  
Server:         10.10.11.70
Address:        10.10.11.70#53

Name:   dc.PUPPY.HTB
Address: 10.10.11.70
;; communications error to 10.10.11.70#53: timed out

```
- Check for SRV records:
```
  ┌──(root㉿kali)-[/home/jacob/Desktop]
└─# nslookup -type=SRV _ldap._tcp.PUPPY.HTB 10.10.11.70                                                                                                                
Server:         10.10.11.70
Address:        10.10.11.70#53

_ldap._tcp.PUPPY.HTB    service = 0 100 389 dc.puppy.htb.

```
- Look for other potential subdomains
```
┌──(root㉿kali)-[/home/jacob/Desktop]
└─# fierce --domain PUPPY.HTB --dns-servers 10.10.11.70                                                                                                                
NS: failure
SOA: failure
Failed to lookup NS/SOA, Domain does not exist
```
# Kerberos Enum (88)
```


```
---

# Working Steps
# Lessons
- Regular NMAP scan doesn't return anything - have to use `-Pn`  flag.  `-Pn: Treat all hosts as online -- skip host discovery`
- Try specifying the domain when enumerating SMB/LDAP
- A timeout could just be a VPN thing dude
