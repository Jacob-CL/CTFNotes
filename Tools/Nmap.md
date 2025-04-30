# Nmap
- Ippsec: `nmap -sV -sC -oA <FILENAME> <TARGETIP>`
- Manual confirmation might be necessary - if a port doesn't respond within a specific time, it's considered closed, filtered or unknown.
- The most effective host discovery method is to use ICMP echo requests.
- Scan a network range: `sudo nmap 10.129.2.0/24 -sn -oA tnet | grep for | cut -d" " -f5`
- Scan a file of hosts: `sudo nmap -sn -oA tnet -iL hosts.lst | grep for | cut -d" " -f5` where file is `hosts.lst`
- Scan multiple IPs: `sudo nmap -sn -oA tnet 10.129.2.18 10.129.2.19 10.129.2.20| grep for | cut -d" " -f5` or `sudo nmap -sn -oA tnet 10.129.2.18-20| grep for | cut -d" " -f5`
- 6 different states a port can be:
| **State** | **Description** |
|-----------|-----------------|
| `open` | This indicates that the connection to the scanned port has been established. These connections can be **TCP connections**, **UDP datagrams** as well as **SCTP associations**. |
| `closed` | When the port is shown as closed, the TCP protocol indicates that the packet we received back contains an `RST` flag. This scanning method can also be used to determine if our target is alive or not. |
| `filtered` | Nmap cannot correctly identify whether the scanned port is open or closed because either no response is returned from the target for the port or we get an error code from the target. |
| `unfiltered` | This state of a port only occurs during the **TCP-ACK** scan and means that the port is accessible, but it cannot be determined whether it is open or closed. |
| `open filtered` | If we do not get a response for a specific port, `Nmap` will set it to that state. This indicates that a firewall or packet filter may protect the port. |
| `closed filtered` | This state only occurs in the **IP ID idle** scans and indicates that it was impossible to determine if the scanned port is closed or filtered by a firewall. |
- Default Nmap only scans top 1000 ports
- When a port is filtered, in most cases firewalls have certain rules set to handle specific connections.
- To be able to track how our sent packets are handled, we deactivate the ICMP echo requests (-Pn), DNS resolution (-n), and ARP ping scan (--disable-arp-ping): `sudo nmap 10.129.2.28 -p 139 --packet-trace -n --disable-arp-ping -Pn`
- Since UDP is a stateless protocol and does not require a three-way handshake like TCP. We do not receive any acknowledgment. Consequently, the timeout is much longer, making the whole UDP scan (-sU) much slower than the TCP scan (-sS). If a UDP port is open, we only get a response if the application is configured to do so.

`nmap.sh`

```bash
#!/bin/bash

# Check if both parameters are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <filename> <target_ip>"
    exit 1
fi

# Assign parameters to variables
FILENAME=$1
TARGET_IP=$2

# Run the nmap command
echo "Running nmap scan on $TARGET_IP with output to $FILENAME..."
nmap -sV -sC -oA "$FILENAME" "$TARGET_IP"

# Check if the command was successful
if [ $? -eq 0 ]; then
    echo "Scan completed successfully."
    echo "Output files created: $FILENAME.nmap, $FILENAME.gnmap, $FILENAME.xml"
else
    echo "Scan failed with error code $?"
fi
```

Example usage: `./nmap.sh myscan 192.168.1.1`

---

### Nmap Scan Types
| Scan Type | Description |
|:-----------|:-------------|
| -sn | Ping scan /Disables port scanning |
| -sS | Syn scan |
| -sT | Connect scan |
| -sU | UDP scan |
| -sO | IP protocol scan |
| -sC | Default scripts |
| -sV | Enables version detection |

---

### Nmap Scan Options
| Scan Option | Description |
|:-------------|:-------------|
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

---

### Nmap Output/Input Options
| Output/Input Option | Description |
|:---------------------|:-------------|
| -oX <FILE_PATH> | Write to XML file |
| -oG <FILE_PATH> | Write to grep file |
| -oA <FILE_PATH> | Save as all 3 formats |
| -iL <FILE_PATH> | Read hosts/IPs from file |
| --excludefile <FILE_PATH> | Excludes hosts in file |

---

### Nmap Firewall evasion options
| Firewall Evasion Option | Description |
|:-------------------------|:-------------|
| -f | Fragment packets |
| -S <IP_ADDRESS> | Spoof source IP |
| -g <PORT> | Spoof source port |
| -D <IP_ADDRESS>,<IP_ADDRESS> | Scan with decoys |
| --mtu <MTU> | Set MTU size |
| --spoof-mac <MAC> | Spoof MAC address |
| --data-length <SIZE> | Append random data |
| --scan-delay <TIME> | Scan delay |

---

### Nmap Misc
| Misc Flags | Description |
|:------------|:-------------|
| xsltproc <INPUT_NMAP_XML>.xml –o <OUTPUT_PATH>.html | Convert Nmap XML file to HTML |
| nmap –sP –n –oX out.xml <IP_CIDR> \| grep "Nmap" \| cut –d " " –f 5 > <OUTPUT_PATH>.txt | Generate live host file |
| ndiff <FILE_PATH1>.xml <FILE_PATH2>.xml | Compare Nmap results |
| nmap –R –sL –dns-server <DNS_SERVER_IP> <IP_CIDR> | DNS reverse lookup on IP range |

---

# PORTS
| Port # | Service |
|--------|---------|
| 20 | FTP (Data Connection) |
| 21 | FTP (Control Connection) |
| 22 | SSH/SCP |
| 23 | Telnet |
| 25 | SMTP |
| 49 | TACACS |
| 53 | DNS |
| 67-68 | DHCP/BOOTP |
| 69 | TFTP (UDP) |
| 80 | HTTP |
| 88 | Kerberos |
| 110 | POP3 |
| 111 | RPC |
| 123 | NTP (UDP) |
| 135 | Windows RPC |
| 137-138 | NetBIOS |
| 139 | SMB |
| 143 | IMAP4 |
| 161-162 | SNMP (UDP) |
| 179 | BGP |
| 201 | AppleTalk |
| 389 | LDAP |
| 443 | HTTPS |
| 445 | SMB |
| 500 | ISAKMP (UDP) |
| 514 | Syslog |
| 520 | RIP |
| 546-547 | DHCPv6 |
| 587 | SMTP |
| 902 | VMWare Server |
| 1080 | Socks Proxy |
| 1194 | Open VPN |
| 1433-1434 | MS-SQL |
| 1521 | Oracle |
| 2049 | NFS |
| 3128 | Squid Proxy |
| 3306 | MySQL |
| 3389 | RDP |
| 5060 | SIP |
| 5222-5223 | XMPP/Jabber |
| 5432 | Postgres SQL |
| 5666 | Nagios |
| 5900 | VNC |
| 6000-6063 | X11 |
| 6129 | DameWare |
| 6133 | DameWare |
| 6665-6669 | IRC |
| 9001 | Tor |
| 9001 | HSQL |
| 9090-9091 | Openfire |
| 9100 | HP JetDirect |
