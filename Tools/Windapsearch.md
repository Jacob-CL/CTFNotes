# Windapsearch
1. `python3 -m venv v-env`
2. `source v-env/bin/activate`
3. `pip3 install python-ldap`
4. `git clone https://github.com/ropnop/windapsearch.git`
5. `python3 windapsearch.py --dc-ip [ip] -u [user@domain.htb/com] -p "[password]"`

To append to the above command:

| Category | Option | Description |
|----------|--------|-------------|
| **Computer Enumeration** | `--computers` | Enumerate domain computers |
| **User Enumeration** | `--users` | All domain users |
| | `--privileged-users` | Users with elevated privileges |
| | `--admin-count` | Users with adminCount=1 (high privilege indicator) |
| | `--passwd-not-required` | Accounts that don't require passwords |
| | `--da` | Domain admins |
| **Group Enumeration** | `--groups` | All domain groups |
| | `--members "Group Name"` | Members of specific group (e.g., "Administrators") |
| | `--members "Domain Admins"` | Members of Domain Admins group |
| | `--members "Enterprise Admins"` | Members of Enterprise Admins group |
| | `--members "Schema Admins"` | Members of Schema Admins group |
| | `--members "Backup Operators"` | Members of Backup Operators group |
| **Security Assessment** | `--unconstrained` | Accounts with unconstrained delegation |
| | `--asrep` | Accounts vulnerable to AS-REP roasting |
| | `--kerberoast` | Accounts vulnerable to Kerberoasting |
| | `--spns` | Service Principal Names |
| | `--trusts` | Domain trust relationships |
| **Infrastructure** | `--gpos` | Group Policy Objects |
| | `--dns-dump` | Dump DNS records |
| | `--functionality` | Domain functional level |
| **Custom/Advanced** | `--custom "filter"` | Custom LDAP filter |
| | `--attrs "attr1,attr2"` | Specify specific attributes to return |
| | `--full` | Return all attributes (verbose output) |
