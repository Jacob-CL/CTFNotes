# SNMP
- SNMP Community strings provide information and statistics about a router or device, helping us gain access to it. The manufacturer default community strings of public and private are often unchanged. In SNMP versions 1 and 2c, access is controlled using a plaintext community string, and if we know the name, we can gain access to it.
- Encryption and authentication were only added in SNMP version 3.
- Examination of process parameters might reveal credentials passed on the command line, which might be possible to reuse for other externally accessible services given the prevalence of password reuse in enterprise environments. Routing information, services bound to additional interfaces, and the version of installed software can also be revealed.
- `snmpwalk -v 2c -c public 10.129.42.253 1.3.6.1.2.1.1.5.0` | `snmpwalk -v 2c -c private  10.129.42.253 `
- A tool such as onesixtyone can be used to brute force the community string names using a dictionary file of common community strings such as the dict.txt file included in the GitHub repo for the tool: `onesixtyone -c dict.txt 10.129.42.254`
