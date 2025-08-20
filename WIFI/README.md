# WI-FI CODE SNIPPETS
```
iwconfig
```
Start interface in monitor mode:
```
 sudo airmon-ng start wlan0
```
Stop monitor mode:
```
sudo airmon-ng stop wlan0mon
```
If things are weird:
```
sudo airmon-ng check
```
```
sudo airmon-ng check kill
```
List networks:
```
sudo iwlist wlan0 s | grep 'Cell\|Quality\|ESSID\|IEEE'
```
Rasberry Pi MAC address ranges:
```
28:CD:C1:xx:xx:xx
B8:27:EB:xx:xx:xx
D8:3A:DD:xx:xx:xx
DC:A6:32:xx:xx:xx
E4:5F:01:xx:xx:xx
```

Put `wlan1` into Monitor mode:
```
sudo ip link set wlan1 down
```
```
sudo iw dev wlan1 set type monitor
```
```
sudo ip link set wlan1 up
```
OR:
```
sudo airmon-ng start wlan1
```
And to stop it:
```
sudo airmon-ng stop wlan1mon
```

---

Configuring the Alpha AWUS036ACH Wi-Fi Adapter - [Link](https://medium.com/@wicked_picker/configuring-the-alpha-awus036ach-wi-fi-adapter-on-kali-linux-eb5ec2826713)
See available USBs:
```
lsusb
```
See it NOT here:
```
iwconfig
```
Install the Realtek drivers:
```
sudo apt-get install realtek-rtl88xxau-dkms
```
Install dkms:
```
sudo apt-get install dkms
```
Download the rtl8812au drivers from GitHub
```
git clone https://github.com/aircrack-ng/rtl8812au
```
```
cd rtl8812au
```
Preemptively fix the error:
```
sudo apt-get install linux-headers-$(uname -r)
```
```
make
```
```
sudo make install
```
```
reboot
```
```
iwconfig
```

---


