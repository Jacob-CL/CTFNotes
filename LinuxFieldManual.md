# LINUX BASICS

Do we have write permissions on cron jobs?
  - `/etc/crontab`
  - `/etc/cron.d`
  - `/var/spool/cron/crontabs/root`

### Linux Basic Commands
| Description | Basic Commands |
|-------------|----------------|
| List Directory | `ls` |
| Change Directory | `cd` |
| Move File | `mv` |
| Manual Pages | `man` |
| Make Directory | `mkdir` |
| Remove Directory | `rmdir` |
| Make Empty File | `touch` |
| Remove File | `rm` |
| Locate File | `locate` |
| Print Working Directory | `pwd` |
| Print Contents | `cat` |
| Copy | `cp` |
| Link | `ln` |
| Super User Do | `sudo` |
| Display Header of File | `head` |
| Display Tail of File | `tail` |
| change permissions | `chmod` |

---

### Linux Administrative Commands
| Description | Administrative Commands |
|-------------|-------------------------|
| get HTML of webpage | `curl <url>` |
| retrieve file | `wget <url>` |
| Remote desktop | `rdesktop <ip>` |
| Secure Shell | `ssh <ip>` |
| Put File | `scp <directory> <user>@<ip>:<directory>` |
| Get File | `scp <user>@<ip>:<directory> <directory>` |
| Add User | `useradd <username>` |
| Change User Password | `passwd <user>` |
| Remove User | `rmuser <user>` |
| Record Shell | `script -a <outfile>` |
| Search Man Pages for Topic | `apropos <topic>` |
| Show users bash history | `history` |
| Executes from number in history | `! <number>` |
| Environment Variables | `env` |
| Shows top processes | `top` |
| Shows ip address | `ifconfig` |
| Files associated with application | `lsof` |

---

### Linux Directories
| Description | Directory |
|:-------------|:-----------|
| Anchor and root of the filesystem | `/` |
| User binaries | `/bin` |
| Boot-up related files | `/boot` |
| Interface for system devices | `/dev` |
| System configuration files | `/etc` |
| Base directory for user files | `/home` |
| Critical software libraries | `/lib` |
| Third party software | `/opt` |
| System and running programs | `/proc` |
| Home directory of root user | `/root` |
| System administrator binaries | `/sbin` |
| Temporary files | `/tmp` |
| Contains all the system files. Less critical files | `/usr` |
| Variable system files | `/var` |

---

### Im### Important Linux Files and Directories
| Description | Important Files + Directories |
|:-------------|:----------------|
| User account information and password hashes | `/etc/shadow` |
| User account information | `/etc/passwd` |
| Group names | `/etc/group` |
| Startup services (rc0.d-rc6.d) | `/etc/rc.d` |
| Contains startup/stop scripts | `/etc/init.d` |
| Hardcoded hostname and IP combinations | `/etc/hosts` |
| Full hostname with domain | `/etc/hostname` |
| Network configuration | `/etc/network/interfaces` or `/etc/netplan` |
| System environment variables | `/etc/profile` |
| Debian package source | `/etc/apt/sources.list` |
| DNS configuration | `/etc/resolv.conf` |
| User Bash history | `/home/<USER>/.bash_history` |
| Vendor-MAC lookup (Kali Linux) | `/usr/share/wireshark/manuf` |
| SSH keystore | `~/.ssh/` |
| System log files (most Linux) | `/var/log` |
| System log files (Unix) | `/var/adm` |
| List cron files | `/var/spool/cron` |
| Apache connection log | `/var/log/apache2/access.log` |
| Contains local and network configured mounts and shares | `/etc/fstab` |

---

### Get Linux OS Information
| Description | Operating System Information |
|:-------------|:---------|
| Disk usage | `df -h` |
| Kernel version & CPU information | `uname -a` |
| Display OS information | `cat /etc/issue` |
| Display OS version information | `cat /etc/*release*` |
| Display kernel information | `cat /proc/version` |
| Locate the executable files or location of each shell on the system (Can search: tscsh, csh, ksh, bash, etc.) | `which <SHELL_NAME>` |
| Display connected drives | `fdisk -l` |
| get Hostname for IP address | `host <ip>` |
| get the Current User | `who am i` |
| Show logged in users | `w` |
|  | `who -a` |
| User login history | `last -a` |
| running processes | `ps` |
| Display free disk space | `df` |
| show mounted drives | `mount` |
| Get entries in passwd(users) | `getent passwd` |
| Add to the PATH variable | `PATH=$PATH:/<directory>` |
| kills process with pid ID | `kill <pid>` |
| force kill process | `kill -9 <pid>` |
| install rpm package | `rpm -i *.rpm` |
| show installed packages | `rpm -qa` |
| install deb package | `dpkg -i *.deb` |
| show installed packages/software | `dpkg --get-selections` |
| solaris show installed packages | `pkginfo` |
| show location of shell executables | `cat /etc/shells` |
| make shell/file nonexecutable | `chmod -x <shell dir>` |
| See what sudo perms you have, you might have perms over other users and can then run: `sudo -u user2 /bin/bash /home/user2/flag.txt` if you see you have `/bin/bash/` execution as user2. If another user can use bash but you can't then run all bash commands as that user | `sudo -l` |
| Running bash as another user in SSH shell | `sudo -u user2 bash -c 'ls -la'` OR `sudo -u user2 bash -c 'ls -al /root'` |
| Switch to root user | `sudo su -` |

---

### Get Linux Situational Awareness
| Description | Situational Awareness & Process Manipulation |
|:-------------|:---------|
| Displays current user/group information | `id` |
| List logged on users and what they are doing | `w` |
| Show currently logged in users | `who -a` |
| Show past and current login and system boot information | `last -a` |
| Process listing | `ps -ef` |
| List mounted drives | `mount` or `findmnt` |
| Force kill processes with specific PID | `kill -9 <PID>` |
| Kill all processes matching a specific name | `killall <PROCESS_NAME>` |
| Show all processes sorting by most active | `top` |
| List configured persistent mounts | `cat /etc/fstab` |

---
### Get Linux account enumeration and config
| Description | User Account Enumeration & Configuration |
|:-----------------------------------------------|:---------------------------------------|
| Display user and service accounts | `getent passwd` |
| Add a user | `useradd –m <USERNAME>` |
| Add user to group | `usermod -g <GROUPNAME> <USERNAME>` |
| Change user password | `passwd <USERNAME>` |
| Lock user account | `usermod --expiredate 1 --lock --shell /bin/nologin <USERNAME>` |
| Unlock user account | `usermod --expiredate 99999 --unlock --shell /bin/bash <USERNAME>` |
| Enumerate user account details | `chage –l <USERNAME>` |
| Delete user | `userdel <USERNAME>` |

---

### Get Linux Network config
| Description | Network Configuration |
|:--------------------------------------------------|:----------------------------------|
| List all listening, established, and connected TCP sockets every 3 seconds | `watch --interval 3 ss -t --all` |
| List all listening TCP and UDP sockets with associated PID/program name | `netstat -tulpn` |
| List all network activity associated to a specific user | `lsof –i –u <USERNAME> -a` |
| Set IP and NETMASK | `ifconfig <INTERFACE_NAME> <NEW_IP> netmask <NEW_SUBNET_MASK>` or `ip addr add <NEW_IP> dev <INTERFACE_NAME>` |
| Add second IP to existing interface | `ifconfig <INTERFACE_NAME>:<NEW_INTERFACE_NAME> <NEW_IP>` or `ip addr add <NEW_IP>/<CIDR> dev <INTERFACE_NAME>` |
| Set gateway | `route add default gw <IP_ADDRESS> <INTERFACE_NAME>` or `ip route add <IP_ADDRESS>/<CIDR> via <GATEWAY_IP> dev <INTERFACE_NAME>` |
| Change MTU size | `ifconfig <INTERFACE_NAME> mtu <SIZE>` or `ip link set dev <INTERFACE_NAME> mtu <SIZE>` |
| Change MAC address | `ifconfig <INTERFACE_NAME> hw ether <MAC_ADDRESS>` or `ip link set dev <INTERFACE_NAME> down ip link set dev <INTERFACE_NAME> address <MAC_ADDRESS> ip link set dev <INTERFACE_NAME> up` |
| Built-in Wi-Fi Scanner | `iwlist <INTERFACE_NAME> scan` |
| List DHCP assignments | `cat /var/log/messages \| grep DHCP` |
| Kills TCP connections running over specific port number | `tcpkill host <IP_ADDRESS> and port <PORT>` |
| Enable on IP Forwarding | `echo "1" > /proc/sys/net/ipv4/ip_forward` |
| Add DNS server | `echo "nameserver <IP_ADDRESS>" >> /etc/resolv.conf` |

---

### Linux file manipulation
| Description | File Manipulation |
|:--------------------------------------------------|:----------------------------------|
| Compare files | `diff <FILE_PATH_A> <FILE_PATH_B>` |
| Force recursive deletion of directory | `rm –rf <FILE_PATH>` |
| Secure file deletion | `shred –f –u <FILE_PATH>` |
| Modify timestamp to match another file | `touch –r <ORIGINAL_FILE_PATH> <MOD_FILE_PATH>` |
| Modify file timestamp | `touch –t <YYYYMMDDHHMM> <FILE>` |
| Count lines containing specific string | `grep –c "<STRING>" <FILE_PATH>` |
| Convert Linux formatted file to Windows compatible text file | `awk 'sub("$", "\r")' <SOURCE_FILE_PATH> > <OUTPUT_FILE_PATH>` |
| Convert Windows formatted file to Linux compatible text file | `dos2unix <FILE_PATH>` |
| Search current and all subdirectories for all files that end with a specific extension | `find . –type f -name "*.<FILE_EXTENSION>"` |
| Search all files (binary and regular files) in current and all subdirectories for a case insensitive phrase | `grep -Ria "<SEARCH_PHRASE>"` |
| Return the line count of a target file | `wc -l <FILE_PATH>` |
| Search for setuid files | `find / -perm -4000 -exec ls -ld {} \;` |
| Determine file type | `file <FILE_PATH>` |
| Set immutable file | `chattr +i <FILE_PATH>` |
| Unset immutable file | `chattr –i <FILE_PATH>` |
| Generate random file (example 3M file) | `dd if=/dev/urandom of=<OUTPUT_FILE_PATH> bs=3145728 count=100` |

---

### Linux File Hashing
| Description | File Hashing |
|:--------------------------------------------------|:----------------------------------|
| Generate MD5 hash of a file | `md5sum <FILE_PATH>` |
| Generate MD5 hash of a string | `echo "<STRING>" \| md5sum` |
| Generate SHA1 hash of a file | `sha1sum <FILE_PATH>` |

---
### Linux Service Manipulation
| Description | Service Manipulation |
|--------------------------------------------------|----------------------------------|
| List existing services and run status | `systemctl list-unit-files --type=service` |
| Check single service status | `systemctl list-unit-files --type=service \| grep httpd` |
| List all services [+] Service is running [-] Service is not running | `service --status-all` |
| Start a service | `service <SERVICE_NAME> start` |
| Stop a service | `service <SERVICE_NAME> stop` |
| Check status of a service | `service <SERVICE_NAME> status` |
| Disable service so it will not auto start | `systemctl disable <SERVICE_NAME>` |
| Enable service so it will auto start on reboot | `systemctl enable <SERVICE_NAME>` |

---

### Linux Wi-Fi Commands
| Description | Linux Wi-Fi Commands |
|--------------------------------------------------|----------------------------------|
| Display wireless interface configuration | `iwconfig` |
| List current state of wireless devices | `rfkill list` |
| Turn on wireless interface | `rfkill unblock all` |
| Monitor all interfaces | `airodump –ng <INTERFACE_NAME>` |
| Connect to unsecured Wi-Fi | `iwconfig ath0 essid <BSSID> ifconfig ath0 up dhclient ath0` |
| Connect to WEP Wi-Fi network | `iwconfig ath0 essid <BSSID> key <WEB_KEY> ifconfig ath0 up dhclient ath0` |
| Connect to WPA-PSK Wi-Fi network | `iwconfig ath0 essid <BSSID> ifconfig ath0 up wpa_supplicant –B –i ath0 –c wpa-psk.conf dhclient ath0` |

---

### Linux Wi-Fi Testing
| Description | Linux Wi-Fi Testing |
|--------------------------------------------------|----------------------------------|
| Stop monitor mode interface | `airmon-ng stop <INTERFACE_NAME>` |
| Start monitor mode interface | `airmon-ng start <INTERFACE_NAME> iwconfig <INTERFACE_NAME> channel <CHANNEL>` |
| Capture traffic | `airodump-ng –c <CHANNEL> --bssid <BSSID> –w file <OUTPUT_PATH>` |
| Force client de-auth | `aireplay-ng -0 10 –a <BSSID> –c <VICTIM_MAC> <INTERFACE_NAME>` |
| Brute force handshake | `#WPA-PSK aircrack-ng –w <WORDLIST_PATH> <CAPTURED_HANDSHAKE_FILE_PATH>` |
| Brute force handshake | `#EAP-MD5 eapmd5pass –r <CAPTURED_HANDSHAKE_FILE_PATH> –w <WORDLIST_PATH>` |

---

### Linux Bluetooth Commands
| Description | Linux Bluetooth |
|--------------------------------------------------|----------------------------------|
| Turn on Bluetooth interface | `hciconfig <INTERFACE_NAME> up` |
| Scan for Bluetooth devices | `hcitool –i <INTERFACE_NAME> scan --flush –all` |
| List open services | `sdptool browse <INTERFACE_NAME>` |
| Set as discoverable | `hciconfig <INTERFACE_NAME> name "<BLUETOOTH_NAME>" class 0x520204   piscan` |
| Clear pand sessions | `pand –K` |