# Information gathering  - Web Edition
- Identify Assets
- Discovering Hidden Information
- Anlaysing Attack Surface
- Gathering Intellignce

Active:
- Port Scanning
- Vuln Scanningf
- Network Mapping
- Banner Grabbing
- OS Fingerprinting
- Service Enumeration
- Web Spidering

Passive:
- Search Engine Queries
- WHOIS Lookups
- DNS
- WebArchive Analysis
- Social Media Analysis
- Code Repos

## WHOIS
WHOIS is a widely used query and response protocol designed to access databases that store information about registered internet resources. Primarily associated with domain names, WHOIS can also provide details about IP address blocks and autonomous systems. Think of it as a giant phonebook for the internet, letting you look up who owns or is responsible for various online assets. You can find:
- Domain Name
- Registrar
- Registrant Contact
- Administrative Contact
- Technical Contact
- Creation and Expiration Dates
- Name Servers

Allowing you to identify key personnel, network infrastructure and histroical data analysis. Useful in phishing investigations, malware analysis and threat intelligence


## DNS
- Much like how GPS translates a destination name into latitude and longitude for navigation, DNS translates human-readable domain names (like www.example.com) into the numerical IP addresses (like 192.0.2.1) that computers use to communicate.
- Rather than naming locations, it would be like giving someone longtitude and latitude coordinates to a destination - DNS solves this.
- Behaves a little like a relay race

1. DNS Query - Computer first checks it's cache (Not quite `etc/hosts` because that maps direct IPs to domains, it's a direct override rather than a cached resolution) to see if it has it stored somewhere, otherwise it reaches out to a DNS resolver, usually provided by your internet service provider (ISP) to find the IP address of `www.example.com`
1. Recursive Lookup - The DNS Resolver Checks its Map, the resolver also has a cache, and if it doesn't find the IP address there, it starts a journey through the DNS hierarchy. It begins by asking a root name server, which is like the librarian of the internet.
1. Root Name Server Points the Way: The root server doesn't know the exact address but knows who does – the Top-Level Domain (TLD) name server responsible for the domain's ending (e.g., .com, .org). It points the resolver in the right direction.
1. TLD Name Server Narrows It Down: The TLD name server is like a regional map. It knows which authoritative name server is responsible for the specific domain you're looking for (e.g., example.com) and sends the resolver there.
1. Authoritative Name Server Delivers the Address: The authoritative name server is the final stop. It's like the street address of the website you want. It holds the correct IP address and sends it back to the resolver.
1. The DNS Resolver Returns the Information: The resolver receives the IP address and gives it to your computer. It also remembers it for a while (caches it), in case you want to revisit the website soon.
1. Your Computer Connects: Now that your computer knows the IP address, it can connect directly to the web server hosting the website, and you can start browsing.

## hosts file
- Windows = `C:\Windows\System32\drivers\etc\hosts`
- Linux = `/etc/hosts`

## Key DNS Concepts
- In DNS, a zone (a text file residing on a DNS server) is a distinct part of the domain namespace that a specific entity or administrator manages. Think of it as a virtual container for a set of domain names. For example, example.com and all its subdomains (like mail.example.com or blog.example.com) would typically belong to the same DNS zone.
- This file defines the authoritative name servers (NS records), mail server (MX record), and IP addresses (A records) for various hosts within the example.com domain

| DNS Concept | Description | Example |
|-------------|-------------|---------|
| `Domain Name` | A human-readable label for a website or other internet resource. | `www.example.com` |
| `IP Address` | A unique numerical identifier assigned to each device connected to the internet. | `192.0.2.1` |
| `DNS Resolver` | A server that translates domain names into IP addresses. | Your ISP's DNS server or public resolvers like Google DNS (`8.8.8.8`) |
| `Root Name Server` | The top-level servers in the DNS hierarchy. | There are 13 root servers worldwide, named A-M: `a.root-servers.net` |
| `TLD Name Server` | Servers responsible for specific top-level domains (e.g., .com, .org). | Verisign for `.com`, PIR for `.org` |
| `Authoritative Name Server` | The server that holds the actual IP address for a domain. | Often managed by hosting providers or domain registrars. |
| `DNS Record Types` | Different types of information stored in DNS. | A, AAAA, CNAME, MX, NS, TXT, etc. |

| Record Type | Full Name | Description | Zone File Example |
|-------------|-----------|-------------|-------------------|
| `A` | Address Record | Maps a hostname to its IPv4 address. | `www.example.com.` IN A `192.0.2.1` |
| `AAAA` | IPv6 Address Record | Maps a hostname to its IPv6 address. | `www.example.com.` IN AAAA `2001:db8:85a3::8a2e:370:7334` |
| `CNAME` | Canonical Name Record | Creates an alias for a hostname, pointing it to another hostname. | `blog.example.com.` IN CNAME `webserver.example.net.` |
| `MX` | Mail Exchange Record | Specifies the mail server(s) responsible for handling email for the domain. | `example.com.` IN MX 10 `mail.example.com.` |
| `NS` | Name Server Record | Delegates a DNS zone to a specific authoritative name server. | `example.com.` IN NS `ns1.example.com.` |
| `TXT` | Text Record | Stores arbitrary text information, often used for domain verification or security policies. | `example.com.` IN TXT `"v=spf1 mx -all"` (SPF record) |
| `SOA` | Start of Authority Record | Specifies administrative information about a DNS zone, including the primary name server, responsible person's email, and other parameters. | `example.com.` IN SOA `ns1.example.com. admin.example.com. 2024060301 10800 3600 604800 86400` |
| `SRV` | Service Record | Defines the hostname and port number for specific services. | `_sip._udp.example.com.` IN SRV 10 5 5060 `sipserver.example.com.` |
| `PTR` | Pointer Record | Used for reverse DNS lookups, mapping an IP address to a hostname. | `1.2.0.192.in-addr.arpa.` IN PTR `www.example.com.` |

## Why does DNS matter for recon?
It's a critical component of a target's infrastructure that can be leveraged to uncover vulnerabilities and gain access during a penetration test:
- Uncovering Assets
- Mapping the Network Infrastructure
- Monitoring for changes

## Subdomains
Subdomains are extensions of the main domain, often created to organise and separate different sections or functionalities of a website. For instance, a company might use blog.example.com for its blog, shop.example.com for its online store, or mail.example.com for its email services. Useful for finding:
- Dev and staging environments
- Hidden Login Portals
- Legacy Apps
- Sensitive information

### Active Subdomain Enumeration
- DNS zone transfer
- dnsenum / ffuf / gobuster / fierce / amass 

### Passive Subdomain Enumeration
- Certificate Trasnparency (CT) logs
- Search Engines

## DNS Zone Transfers
- Less invasive and potentially more efficient method for uncovering subdomains 
- A DNS zone transfer is essentially a wholesale copy of all DNS records within a zone (a domain and its subdomains) from one name server to another. This process is essential for maintaining consistency and redundancy across DNS servers. However, if not adequately secured, unauthorised parties can download the entire zone file, revealing a complete list of subdomains, their associated IP addresses, and other sensitive DNS data.
- While zone transfers are essential for legitimate DNS management, a misconfigured DNS server can transform this process into a significant security vulnerability. The core issue lies in the access controls governing who can initiate a zone transfer.
- Even if unsuccessful, the attempt can reveal information about the DNS server's configuration and security posture.
- Request a zone trasnfer `dig axfr @nsztm1.digi.ninja zonetransfer.me`
- If the server is misconfigured and allows the transfer, you'll receive a complete list of DNS records for the domain, including all subdomains.
- `zonetransfer.me` is a service specifically setup to demonstrate the risks of zone transfers so that the dig command will return the full zone record.

Claude's dumb version for me:
- Think of DNS like a giant phone book for the internet. When you type "google.com" into your browser, DNS servers look up the actual IP address (like 172.217.164.142) so your computer knows where to go.
Now, a DNS zone is basically one section of that phone book - like all the entries for a particular company or domain. For example, all the DNS records for "example.com" and its subdomains would be in one zone.
- A zone transfer is literally copying that entire section of the phone book from one DNS server to another. It's like photocopying pages 150-200 of the phone book and giving them to someone else.
- Why?
	- Backup and redundancy: You don't want just ONE phone book in the entire city, right? If that building burns down, nobody can look up phone numbers. Same with DNS - if the main DNS server goes down, you need backup servers that have copies of all the same information.
	- Load distribution: If millions of people are trying to look up "google.com" at the same time, you want multiple servers around the world that can answer those requests, rather than everyone hitting the same single server.
	- Geographic distribution: It's faster to look up a phone number at the library down the street than to call someone across the country. DNS servers closer to you can answer faster.
	- Administrative updates: When a company changes their phone number (IP address), they need a way to update all the copies of the phone book efficiently.
- The zone transfer process lets the "master" DNS server (the authoritative source) push updates to all the "slave" servers automatically, keeping everything in sync. Without this, the internet's phone book system would be unreliable and slow.

## Virtual Hosts
- At the core of virtual hosting is the ability of web servers to distinguish between multiple websites or applications sharing the same IP address. This is achieved by leveraging the HTTP Host header, a piece of information included in every HTTP request sent by a web browser.
- The key difference between VHosts and subdomains is their relationship to the Domain Name System (DNS) and the web server's configuration:
	- Subdomains: These are extensions of a main domain name (e.g., blog.example.com is a subdomain of example.com). Subdomains typically have their own DNS records, pointing to either the same IP address as the main domain or a different one. They can be used to organise different sections or services of a website.
	- Virtual Hosts (VHosts): Virtual hosts are configurations within a web server that allow multiple websites or applications to be hosted on a single server. They can be associated with top-level domains (e.g., example.com) or subdomains (e.g., dev.example.com). Each virtual host can have its own separate configuration, enabling precise control over how requests are handled.
	
- If a virtual host does not have a DNS record, you can still access it by modifying the hosts file on your local machine. The `hosts` file allows you to map a domain name to an IP address manually, bypassing DNS resolution.
- Websites often have subdomains that are not public and won't appear in DNS records. These subdomains are only accessible internally or through specific configurations. VHost fuzzing is a technique to discover public and non-public subdomains and VHosts by testing various hostnames against a known IP address.
1. Browser Requests a Website
1. Host Header Reveals the Domain
1. Web Server Determines the Virtual Host
1. Serving the Right Content

- In essence, the Host header functions as a switch, enabling the web server to dynamically determine which website to serve based on the domain name requested by the browser.

Different types:
- Name-based Virtual Hosting
- IP-based Virtual Hosting
- Port-based Virtual Hosting

## VHost Discovery Tools
- Gobuster / Feroxbuster / ffuf

## Certificate Transparency Logs
- At the heart of SSL/TLS lies the digital certificate, a small file that verifies a website's identity and allows for secure, encrypted communication.
- Certificate Transparency (CT) logs are public, append-only ledgers that record the issuance of SSL/TLS certificates. Whenever a Certificate Authority (CA) issues a new certificate, it must submit it to multiple CT logs. Independent organisations maintain these logs and are open for anyone to inspect. Think of CT logs as a global registry of certificates
- CT logs provide a reliable and efficient way to discover subdomains without the need for exhaustive brute-forcing or relying on the completeness of wordlists. They offer a unique window into a domain's history and can reveal subdomains that might otherwise remain hidden, significantly enhancing your reconnaissance capabilities.
- Go to: `crt.sh` | `Censys`

### crt.ssh
- Has an API: `curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[] | select(.name_value | contains("dev")) | .name_value' | sort -u`


## Fingerprinting
- Fingerprinting focuses on extracting technical details about the technologies powering a website or web application. 
- Identify misconfigs, prioritise targets, build a comprehensive profile by banner grabbing, analysing HTTP headers, probing for specific responses, analyse page content
- Wappalyzer / BuiltWith / WhatWeb / NMAP / Netcraft / wafw00f / Nikto

## Crawlng
- Often called spidering, is the automated process of systematically browsing the World Wide Web.
- Breadth-first crawling prioritizes exploring a website's width before going deep. 
- In contrast, depth-first crawling prioritizes depth over breadth.

## robots.txt
- File that contains instructions in the form of "directives" that tell bots which parts of the website they can and cannot crawl.
- Optional, most don't have it. Most seen in large commercial websites, sites with heavy bot traffic, any site where SEO is a priority etc
- This directive tells all user-agents (* is a wildcard) that they are not allowed to access any URLs that start with /private/:

```
User-agent: *
Disallow: /private/
```
| Directive | Description | Example |
|-----------|-------------|---------|
| `Disallow` | Specifies paths or patterns that the bot should not crawl. | `Disallow: /admin/` (disallow access to the admin directory) |
| `Allow` | Explicitly permits the bot to crawl specific paths or patterns, even if they fall under a broader `Disallow` rule. | `Allow: /public/` (allow access to the public directory) |
| `Crawl-delay` | Sets a delay (in seconds) between successive requests from the bot to avoid overloading the server. | `Crawl-delay: 10` (10-second delay between requests) |
| `Sitemap` | Provides the URL to an XML sitemap for more efficient crawling. | `Sitemap: https://www.example.com/sitemap.xml` |

- As a web crawler.. why respect it? Avoids overburdening servers, protecting sensitvie information, legal and ethical compliance.
- Where is it useful? uncovering hidden directories, mapping website structure, detecting crawler traps.

## Well-known URIs
- https://datatracker.ietf.org/doc/html/rfc8615
- The `.well-known` standard, defined in RFC 8615, serves as a standardized directory within a website's root domain. This designated location, typically accessible via the /.well-known/ path on a web server, centralizes a website's critical metadata, including configuration files and information related to its services, protocols, and security mechanisms.

| URI Suffix | Description | Status | Reference |
|------------|-------------|--------|-----------|
| `security.txt` | Contains contact information for security researchers to report vulnerabilities. | Permanent | RFC 9116 |
| `/.well-known/change-password` | Provides a standard URL for directing users to a password change page. | Provisional | https://w3c.github.io/webappsec-change-password-url/#the-change-password-well-known-uri |
| `openid-configuration` | Defines configuration details for OpenID Connect, an identity layer on top of the OAuth 2.0 protocol. | Permanent | http://openid.net/specs/openid-connect-discovery-1_0.html |
| `assetlinks.json` | Used for verifying ownership of digital assets (e.g., apps) associated with a domain. | Permanent | https://github.com/google/digitalassetlinks/blob/master/well-known/specification.md |
| `mta-sts.txt` | Specifies the policy for SMTP MTA Strict Transport Security (MTA-STS) to enhance email security. | Permanent | RFC 8461 |

- The openid-configuration URI is part of the OpenID Connect Discovery protocol, an identity layer built on top of the OAuth 2.0 protocol. When a client application wants to use OpenID Connect for authentication, it can retrieve the OpenID Connect Provider's configuration by accessing the https://example.com/.well-known/openid-configuration endpoint. This endpoint returns a JSON document containing metadata about the provider's endpoints, supported authentication methods, token issuance, and more.

## Popular Crawlers
- Burp Suite / OWASP ZAP / Scrapy / Apache Nutch

## Search Operators
| Operator | Description | Example | Example Description |
|----------|-------------|---------|-------------------|
| `site:` | Limits results to a specific website or domain. | `site:example.com` | Find all publicly accessible pages on example.com. |
| `inurl:` | Finds pages with a specific term in the URL. | `inurl:login` | Search for login pages on any website. |
| `filetype:` | Searches for files of a particular type. | `filetype:pdf` | Find downloadable PDF documents. |
| `intitle:` | Finds pages with a specific term in the title. | `intitle:"confidential report"` | Look for documents titled "confidential report" or similar variations. |
| `intext:` or `inbody:` | Searches for a term within the body text of pages. | `intext:"password reset"` | Identify webpages containing the term "password reset". |
| `cache:` | Displays the cached version of a webpage (if available). | `cache:example.com` | View the cached version of example.com to see its previous content. |
| `link:` | Finds pages that link to a specific webpage. | `link:example.com` | Identify websites linking to example.com. |
| `related:` | Finds websites related to a specific webpage. | `related:example.com` | Discover websites similar to example.com. |
| `info:` | Provides a summary of information about a webpage. | `info:example.com` | Get basic details about example.com, such as its title and description. |
| `define:` | Provides definitions of a word or phrase. | `define:phishing` | Get a definition of "phishing" from various sources. |
| `numrange:` | Searches for numbers within a specific range. | `site:example.com numrange:1000-2000` | Find pages on example.com containing numbers between 1000 and 2000. |
| `allintext:` | Finds pages containing all specified words in the body text. | `allintext:admin password reset` | Search for pages containing both "admin" and "password reset" in the body text. |
| `allinurl:` | Finds pages containing all specified words in the URL. | `allinurl:admin panel` | Look for pages with "admin" and "panel" in the URL. |
| `allintitle:` | Finds pages containing all specified words in the title. | `allintitle:confidential report 2023` | Search for pages with "confidential," "report," and "2023" in the title. |
| `AND` | Narrows results by requiring all terms to be present. | `site:example.com AND (inurl:admin OR inurl:login)` | Find admin or login pages specifically on example.com. |
| `OR` | Broadens results by including pages with any of the terms. | `"linux" OR "ubuntu" OR "debian"` | Search for webpages mentioning Linux, Ubuntu, or Debian. |
| `NOT` | Excludes results containing the specified term. | `site:bank.com NOT inurl:login` | Find pages on bank.com excluding login pages. |
| `*` (wildcard) | Represents any character or word. | `site:socialnetwork.com filetype:pdf user* manual` | Search for user manuals (user guide, user handbook) in PDF format on socialnetwork.com. |
| `..` (range search) | Finds results within a specified numerical range. | `site:ecommerce.com "price" 100..500` | Look for products priced between 100 and 500 on an e-commerce website. |
| `" "` (quotation marks) | Searches for exact phrases. | `"information security policy"` | Find documents mentioning the exact phrase "information security policy". |
| `-` (minus sign) | Excludes terms from the search results. | `site:news.com -inurl:sports` | Search for news articles on news.com excluding sports-related content. |


## Google Dorking
- https://www.exploit-db.com/google-hacking-database

- Finding Login Pages:
        - site:example.com inurl:login
        - site:example.com (inurl:login OR inurl:admin)
- Identifying Exposed Files:
        - site:example.com filetype:pdf
        - site:example.com (filetype:xls OR filetype:docx)
- Uncovering Configuration Files:
        - site:example.com inurl:config.php
        - site:example.com (ext:conf OR ext:cnf) (searches for extensions commonly used for configuration files)
- Locating Database Backups:
        - site:example.com inurl:backup
        - site:example.com filetype:sql
        
## Web Archives
- WayBack Machine: http://web.archive.org/

## Automated Recon
- FinalRecon / Recon-ng / theHarvester / SpiderFoot / OSINT Framework





