# Web Proxies
- Web proxies are specialized tools that can be set up between a browser/mobile application and a back-end server to capture and view all the web requests being sent between both ends, essentially acting as man-in-the-middle (MITM) tools. While other Network Sniffing applications, like Wireshark, operate by analyzing all local traffic to see what is passing through a network, Web Proxies mainly work with web ports such as, but not limited to, HTTP/80 and HTTPS/443.
- Zap + BurpSuite are a web-proxies
- Useful for Web application vulnerability scanning, Web fuzzing, Web crawling, Web application mapping, Web request analysis, Web configuration testing + Code reviews

Once we intercept a request, we can test for:
    - SQL injections
    - Command injections
    - Upload bypass
    - Authentication bypass
    - XSS
    - XXE
    - Error handling
    - Deserialization
    - IDOR

## [Proxychains](https://github.com/haad/proxychains)
- Routes all traffic coming from any command-line tool to any proxy we specify. Proxychains adds a proxy to any command-line tool and is hence the simplest and easiest method to route web traffic of command-line tools through our web proxies.
- Now NMAP commands (or any other) are proxied

## Metasploit
- Try proxy web traffic by Metasploit to better investigate and understand them - need the `PROXIES` flag

## Web Proxy Extensions
- BApp Store for BurpSuite extensions
- ZAP Marketplace for ZAP extensions

## Forward / Reverse Proxies
The key difference is who the proxy is acting on behalf of - the client or the server.
- Forward = Forwards your request (acts for you: Client → Forward Proxy → Internet → Server)
- Reverse = Reverses the normal flow (acts for the server: Client → Internet → Reverse Proxy → Backend Server(s))
