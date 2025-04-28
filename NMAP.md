# Nmap

Ippsec: `nmap -sV -sC -oA filename targetip`

- `sV`: Enables version detection. It attempts to determine the version of the services running on open ports.
- `sC`: Tells nmap to run a set of default scripts. These scripts are part of the Nmap Scripting Engine (NSE) and are used to gather more information about the target.
- `oA`: Used for output. preceeds `filename`.
