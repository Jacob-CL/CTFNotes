# Netcat / ncat / nc
- Used for interacting with TCP/UDP ports, predominantly for connecting to shells.
- Can be used to connect to any listening port and interact with the service running on that port.
- e.g SSH is programmed to handle connections over port 22 to send all data and keys. We can connect to TCP port 22 with netcat: `netcat 10.10.10.10 22`
- Netcat comes pre-installed in most Linux distributions
