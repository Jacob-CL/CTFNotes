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
# Steps
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
# extended LDIF
#
# LDAPv3
# base <> with scope baseObject
# filter: (objectclass=*)
# requesting: ALL
#

#
dn:
domainFunctionality: 7
forestFunctionality: 7
domainControllerFunctionality: 7
rootDomainNamingContext: DC=PUPPY,DC=HTB
ldapServiceName: PUPPY.HTB:dc$@PUPPY.HTB
isGlobalCatalogReady: TRUE
supportedSASLMechanisms: GSSAPI
supportedSASLMechanisms: GSS-SPNEGO
supportedSASLMechanisms: EXTERNAL
supportedSASLMechanisms: DIGEST-MD5
supportedLDAPVersion: 3
supportedLDAPVersion: 2
supportedLDAPPolicies: MaxPoolThreads
supportedLDAPPolicies: MaxPercentDirSyncRequests
supportedLDAPPolicies: MaxDatagramRecv
supportedLDAPPolicies: MaxReceiveBuffer
supportedLDAPPolicies: MaxPreAuthReceiveBuffer
supportedLDAPPolicies: InitRecvTimeout
supportedLDAPPolicies: MaxConnections
supportedLDAPPolicies: MaxConnIdleTime
supportedLDAPPolicies: MaxPageSize
supportedLDAPPolicies: MaxBatchReturnMessages
supportedLDAPPolicies: MaxQueryDuration
supportedLDAPPolicies: MaxDirSyncDuration
supportedLDAPPolicies: MaxTempTableSize
supportedLDAPPolicies: MaxResultSetSize
supportedLDAPPolicies: MinResultSets
supportedLDAPPolicies: MaxResultSetsPerConn
supportedLDAPPolicies: MaxNotificationPerConn
supportedLDAPPolicies: MaxValRange
supportedLDAPPolicies: MaxValRangeTransitive
supportedLDAPPolicies: ThreadMemoryLimit
supportedLDAPPolicies: SystemMemoryLimitPercent
supportedControl: 1.2.840.113556.1.4.319
supportedControl: 1.2.840.113556.1.4.801
supportedControl: 1.2.840.113556.1.4.473
supportedControl: 1.2.840.113556.1.4.528
supportedControl: 1.2.840.113556.1.4.417
supportedControl: 1.2.840.113556.1.4.619
supportedControl: 1.2.840.113556.1.4.841
supportedControl: 1.2.840.113556.1.4.529
supportedControl: 1.2.840.113556.1.4.805
supportedControl: 1.2.840.113556.1.4.521
supportedControl: 1.2.840.113556.1.4.970
supportedControl: 1.2.840.113556.1.4.1338
supportedControl: 1.2.840.113556.1.4.474
supportedControl: 1.2.840.113556.1.4.1339
supportedControl: 1.2.840.113556.1.4.1340
supportedControl: 1.2.840.113556.1.4.1413
supportedControl: 2.16.840.1.113730.3.4.9
supportedControl: 2.16.840.1.113730.3.4.10
supportedControl: 1.2.840.113556.1.4.1504
supportedControl: 1.2.840.113556.1.4.1852
supportedControl: 1.2.840.113556.1.4.802
supportedControl: 1.2.840.113556.1.4.1907
supportedControl: 1.2.840.113556.1.4.1948
supportedControl: 1.2.840.113556.1.4.1974
supportedControl: 1.2.840.113556.1.4.1341
supportedControl: 1.2.840.113556.1.4.2026
supportedControl: 1.2.840.113556.1.4.2064
supportedControl: 1.2.840.113556.1.4.2065
supportedControl: 1.2.840.113556.1.4.2066
supportedControl: 1.2.840.113556.1.4.2090
supportedControl: 1.2.840.113556.1.4.2205
supportedControl: 1.2.840.113556.1.4.2204
supportedControl: 1.2.840.113556.1.4.2206
supportedControl: 1.2.840.113556.1.4.2211
supportedControl: 1.2.840.113556.1.4.2239
supportedControl: 1.2.840.113556.1.4.2255
supportedControl: 1.2.840.113556.1.4.2256
supportedControl: 1.2.840.113556.1.4.2309
supportedControl: 1.2.840.113556.1.4.2330
supportedControl: 1.2.840.113556.1.4.2354
supportedCapabilities: 1.2.840.113556.1.4.800
supportedCapabilities: 1.2.840.113556.1.4.1670
supportedCapabilities: 1.2.840.113556.1.4.1791
supportedCapabilities: 1.2.840.113556.1.4.1935
supportedCapabilities: 1.2.840.113556.1.4.2080
supportedCapabilities: 1.2.840.113556.1.4.2237
subschemaSubentry: CN=Aggregate,CN=Schema,CN=Configuration,DC=PUPPY,DC=HTB
serverName: CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configurat
 ion,DC=PUPPY,DC=HTB
schemaNamingContext: CN=Schema,CN=Configuration,DC=PUPPY,DC=HTB
namingContexts: DC=PUPPY,DC=HTB
namingContexts: CN=Configuration,DC=PUPPY,DC=HTB
namingContexts: CN=Schema,CN=Configuration,DC=PUPPY,DC=HTB
namingContexts: DC=DomainDnsZones,DC=PUPPY,DC=HTB
namingContexts: DC=ForestDnsZones,DC=PUPPY,DC=HTB
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
Now that I have the Domain name I can try to dump all data:
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
The error message indicates that anonymous searching of the directory is not allowed - you need to authenticate first. Gippity says to try NULL bind:
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
- NULL bind doesn't work: You attempted a NULL bind (sending empty username and password with -D "" -w "") and received the same operations error. This means the server requires actual credentials for authentication.
- Security is properly configured: The error message "In order to perform this operation a successful bind must be completed on the connection" confirms that the LDAP server has been configured to prevent unauthenticated access to the directory contents.
- Error code specifics: The "000004DC" error code is a hexadecimal Active Directory error code that translates to "LDAP_OPERATIONS_ERROR" (1244 in decimal), which is a generic error indicating the server can't process your request due to security restrictions.


# Working Steps
# Lessons
- Regular NMAP scan doesn't return anything - have to use `-Pn`  flag.  `-Pn: Treat all hosts as online -- skip host discovery`
