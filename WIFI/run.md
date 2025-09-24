```
iwconfig
```
```
ifconfig wlan0 down
```
```
iwconfig wlan0 txpower 30
```
```
ifconfig wlan0 up
```
```
sudo airmon-ng start wlan0
```
```
sudo airodump-ng wlan0mon --band abg -w dump
```
