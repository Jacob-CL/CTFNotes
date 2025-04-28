# START
## Nmap
Ippsec: `nmap -sV -sC -oA <FILENAME.txt> <TARGETIP>`

<div align="center">
  
| Scan Type | Description |
|:-----------|:-------------|
| -sn | Ping scan |
| -sS | Syn scan |
| -sT | Connect scan |
| -sU | UDP scan |
| -sO | IP protocol scan |
| -sC | Default scripts |
| -sV | Enables version detection |

| Scan Option | Description |
|-------------|-------------|
| -p <PORT_RANGES> | Ports |
| -T[0-5] | Speed presets: 0 Slowest, 5 fastest |
| -n | No DNS resolution |
| -O | OS Detection |
| -A | Aggressive Scan |
| -sV | Service/Version detection |
| -Pn | No ping nmap scan |
| -6 | IPv6 Scan |
| --randomize-hosts | Randomizes target hosts (will not scan each host in sequence) |
| --traceroute | Run traceroute against host |
| --ttl <TTL_VALUE> | Set TTL |
| --script <SCRIPT_NAME> | Execute script against host |
| --script-args <ARGUMENTS> | Set script arguments |

| Output/Input Option | Description |
|---------------------|-------------|
| -oX <FILE_PATH> | Write to XML file |
| -oG <FILE_PATH> | Write to grep file |
| -oA <FILE_PATH> | Save as all 3 formats |
| -iL <FILE_PATH> | Read hosts/IPs from file |
| --excludefile <FILE_PATH> | Excludes hosts in file |

| Firewall Evasion Option | Description |
|-------------------------|-------------|
| -f | Fragment packets |
| -S <IP_ADDRESS> | Spoof source IP |
| -g <PORT> | Spoof source port |
| -D <IP_ADDRESS>,<IP_ADDRESS> | Scan with decoys |
| --mtu <MTU> | Set MTU size |
| --spoof-mac <MAC> | Spoof MAC address |
| --data-length <SIZE> | Append random data |
| --scan-delay <TIME> | Scan delay |

| Misc Flags | Description |
|------------|-------------|
| xsltproc <INPUT_NMAP_XML>.xml –o <OUTPUT_PATH>.html | Convert Nmap XML file to HTML |
| nmap –sP –n –oX out.xml <IP_CIDR> \| grep "Nmap" \| cut –d " " –f 5 > <OUTPUT_PATH>.txt | Generate live host file |
| ndiff <FILE_PATH1>.xml <FILE_PATH2>.xml | Compare Nmap results |
| nmap –R –sL –dns-server <DNS_SERVER_IP> <IP_CIDR> | DNS reverse lookup on IP range |

</div>
---
## Ports
### 20/21 - FTP (Data Connection / Control Connection)

### 22 - SSH/SCP

### 23 - TELNET

### 25 - SMTP

### 49 - TACAS

### 53 - DNS

### 67/68 - DHCP/BOOTP

### 69 - TFTP (UDP)

### 80/443 - HTTP / HTTPS
- OWASP Projects
  - [OWASP Web Security Testing Guide (WSTG)](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/)
  - [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/index.html)
     [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/)
 
### 88 - KERBEROS

### 110 - POP3

### 111 - RPC

### 123 - NTP (UDP)

### 135 - Windows RPC

### 137/138 - NetBIOS

### 139 - SMB

### 143 - IMAP4

### 161/162 - SNMP (UDP)

### 179 - BGP

### 201 - AppleTalk

### 389 - LDAP

### 445 - SMB

### 500 - ISAKMP (UDP)

### 514 - SYSLOG

#### 520 - RIP

### 546/547 - DHCPv6

### 587 - SMTP

### 902 - VMWare Server

### 1080 - Socks Proxy

### 1194 - OpenVPN

### 1433/1434 - MSSQL

### 1521 - Oracle

### 2049 - NFS

### 3128 - Squid Proxy

### 3306 - MySQL

### 3389 - RDP

#### 5060 - SIP

### 5222/5223 - XMP/Jabber

### 5432 - Postgres SQL

### 5666 - Nagios

### 5900 - VNC

### 6000 --> 6063 - X11

### 6129/6133 - DameWare

### 6665 --> 6669 - IRC

### 9001 - Tor / HSQL

### 9090/9091 - Openfire

### 9100 - HP JetDirect


# TESTING + VALIDATING

# ATTACKS

# CODE SNIPPETS
