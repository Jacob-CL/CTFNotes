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

| Operating System Information | Description |
|:---------|:-------------|
| df -h | Disk usage |
| uname -a | Kernel version & CPU information |
| cat /etc/issue | Display OS information |
| cat /etc/*release* | Display OS version information |
| cat /proc/version | Display kernel information |
| which <SHELL_NAME> | Locate the executable files or location of each shell on the system (Can search: tscsh, csh, ksh, bash, etc.) |
| fdisk -l | Display connected drives |

---

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

---

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

| #### File Hashing | Description |
|:----------------------------------|:--------------------------------------------------|
| md5sum <FILE_PATH> | Generate MD5 hash of a file |
| echo "<STRING>" \| md5sum | Generate MD5 hash of a string |
| sha1sum <FILE_PATH> | Generate SHA1 hash of a file |

---

</div>

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

