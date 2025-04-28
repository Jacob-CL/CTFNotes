# Nmap
Ippsec: `nmap -sV -sC -oA <FILENAME> <TARGETIP>`

---

### Nmap Scan Types
| Scan Type | Description |
|:-----------|:-------------|
| -sn | Ping scan |
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
