# Netcat / ncat / nc
- Used for interacting with TCP/UDP ports, predominantly for connecting to shells.
- Can be used to connect to any listening port and interact with the service running on that port.
- e.g SSH is programmed to handle connections over port 22 to send all data and keys. We can connect to TCP port 22 with netcat: `netcat 10.10.10.10 22`
- Netcat comes pre-installed in most Linux distributions
- Get service version info by connecting directly with Netcat
- Netcat listener `nc -lvnp 1234`

| **Description** | **Command** |
|-----------------|-------------|
| Listen mode, to wait for a connection to connect to us | `-l` |
| Verbose mode, so that we know when we receive a connection | `-v` |
| Disable DNS resolution and only connect from/to IPs, to speed up the connection | `-n` |
| Port number `netcat` is listening on, and the reverse connection should be sent to | `-p 1234` |
