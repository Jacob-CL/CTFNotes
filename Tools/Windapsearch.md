# Windapsearch
1. `python3 -m venv v-env`
2. `source v-env/bin/activate`
3. `pip3 install python-ldap`
4. `git clone https://github.com/ropnop/windapsearch.git`
5. `python3 windapsearch.py --dc-ip [ip] -u [user@domain.htb/com] -p "[password]"`

To append to the above command:
| Option | Description |
|--------|-------------|
| `--functionality` | Enumerate Domain Functionality level. Possible through anonymous bind |
| `-G, --groups` | Enumerate all AD Groups |
| `-U, --users` | Enumerate all AD Users |
| `-PU, --privileged-users` | Enumerate All privileged AD Users. Performs recursive lookups for nested members. |
| `-C, --computers` | Enumerate all AD Computers |
| `-m, --members GROUP_NAME` | Enumerate all members of a group |
| `--da` | Shortcut for enumerate all members of group 'Domain Admins'. Performs recursive lookups for nested members. |
| `--admin-objects` | Enumerate all objects with protected ACLs (i.e. admins) |
| `--user-spns` | Enumerate all users objects with Service Principal Names (for kerberoasting) |
| `--unconstrained-users` | Enumerate all user objects with unconstrained delegation |
| `--unconstrained-computers` | Enumerate all computer objects with unconstrained delegation |
| `--gpos` | Enumerate Group Policy Objects |
| `-s, --search SEARCH_TERM` | Fuzzy search for all matching LDAP entries |
| `-l, --lookup DN` | Search through LDAP and lookup entry. Works with fuzzy search. Defaults to printing all attributes, but honors '--attrs' |
| `--custom CUSTOM_FILTER` | Perform a search with a custom object filter. Must be valid LDAP filter syntax |
