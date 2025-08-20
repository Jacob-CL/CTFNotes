# WI-FI CODE SNIPPETS
```
iwconfig
```
Start interface in monitor mode:
```
 sudo airmon-ng start wlan0
```
List networks:
```
sudo iwlist wlan0 s | grep 'Cell\|Quality\|ESSID\|IEEE'
```
