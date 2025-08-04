# WINDOWS FIELD MANUAL
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

