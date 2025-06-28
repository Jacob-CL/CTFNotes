# Introduction to Web Applications
## Web Applications vs. Websites
![website_vs_webapps](https://github.com/user-attachments/assets/6bcb4ae5-f79d-44b0-9c76-71cff3f19da3)
- Websites --> Web1.0
- Web Apps --> Web2.0
- Decentralized Web apps --> Web3.0

## Web Application Infrastrcuture
Keep in mind the following when getting responses back from servers:

Client Server:
![client-server-model](https://github.com/user-attachments/assets/9753e945-f883-4365-8ad6-b19c55110940)

One Server: 
![one-server-arch](https://github.com/user-attachments/assets/bc94af71-4291-4ae7-9e58-adcacdae8e1f)

Many Servers - One DB:
![many-server-one-db-arch](https://github.com/user-attachments/assets/4d24b77a-3443-49f2-82c4-e3f83377c61f)

Many Servers - Many DBs:
![many-server-many-db-arch](https://github.com/user-attachments/assets/335396e2-225d-45a0-93f7-78114f154f11)

## Web Application Components
1. Client
2. Server (WebServer, Web Application Logic, Database)
3. Services / Microservices (3rd Party + Web App Integrations). The use of microservices is considered service-oriented architecture (SOA), built as a collection of different automated functions focused on a single business goal. 
4. Functions (Serverless/Cloud)

## Front End Vulnerabilities - Sensitive Data Exposure
- Can be good for finding low hanging fruit
  - Page Source: `Ctrl + u`
  - Dev Tools: `Ctrl + Shft + i`
  
3 types - HTML injection, JavaScript Injection (XSS) and Cross-Site Request Forgery (CSRF).
 
 Check for lack of input santization for front end vulns:
  - [HTML injection](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/03-Testing_for_HTML_Injection)
  - [JavaScript Injection / XSS](https://owasp.org/www-community/attacks/xss/)
  - [Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf)
  
XSS is very similar to HTML Injection in practice. However, XSS involves the injection of JavaScript code to perform more advanced attacks on the client-side, instead of merely injecting HTML code. There are three main types of XSS:

| Type | Description |
|------|-------------|
| `Reflected XSS` | Occurs when user input is displayed on the page after processing (e.g., search result or error message). |
| `Stored XSS` | Occurs when user input is stored in the back end database and then displayed upon retrieval (e.g., posts or comments). |
| `DOM XSS` | Occurs when user input is directly shown in the browser and is written to an `HTML` DOM object (e.g., vulnerable username or page title). |

- CSRF takes XSS one step further but utilizing XSS vulnerabilities to perform certain queries, and API calls on a web application that the victim is currently authenticated to.

- A common CSRF attack to gain higher privileged access to a web application is to craft a JavaScript payload that automatically changes the victim's password to the value set by the attacker. 
 
 - Keep in mind these 3 types are independant of each other but can work in conjunction - whether one works or not is contextual of the user input and where the output appears.
 
 ## Back End Servers
 Typical/possible main components:
 - Web Server
 - Database
 - Development Framework
 - Hypervisors
 - COntainers 
 - WAFs
 
 There are many popular web stacks, read them here: https://en.wikipedia.org/wiki/Solution_stack
 
 ### Apache
 - Open Source
 - Most common (40% of all internet websites)
 - Preinstalled on Linux4
 - Usually PHP but also supports .Net, Python, Perl and Bash/CGI.
 
 ### NGINX
 - Open Source
 - Second most common (30% of all internet websites)
 - 60% of top 100,000 websites because of low memory and CPU load - makes it very reliable.
 
 ### [ISS - Internet Information Services](https://en.wikipedia.org/wiki/Internet_Information_Services)
 - 3rd most common with 15%,
 - Developed and maintained by Microsoft and mainly runs on Microsoft Servers - therefore well optimized for AD
 
 ### Others
 - [Apache Tomcat](https://tomcat.apache.org/)
 - [Node.js](https://nodejs.org/en/) for Web Apps using JavaScript
 
 ## Databases
 ### Relational (SQL)
 - Relational (SQL) databases store their data in tables, rows, and columns. Each table can have unique keys, which can link tables together and create relationships between tables.
 - The relationship between tables within a database is called a Schema.
 
 | Type | Description |
|------|-------------|
| MySQL | The most commonly used database around the internet. It is an open-source database and can be used completely free of charge |
| MSSQL | Microsoft's implementation of a relational database. Widely used with Windows Servers and IIS web servers |
| Oracle | A very reliable database for big businesses, and is frequently updated with innovative database solutions to make it faster and more reliable. It can be costly, even for big businesses |
| PostgreSQL | Another free and open-source relational database. It is designed to be easily extensible, enabling adding advanced new features without needing a major change to the initial database design |

### Non Relational (NoSQL)
- https://en.wikipedia.org/wiki/NoSQL
- A non-relational database does not use tables, rows, columns, primary keys, relationships, or schemas. Instead, a NoSQL database stores data using various storage models, depending on the type of data stored.
- There are 4 common storage models for NoSQL databases:
    - Key-Value
    - Document-Based
    - Wide-Column
    - Graph
    
- Each of the above models has a different way of storing data. For example, the Key-Value model usually stores data in JSON or XML, and has a key for each pair, storing all of its data as its value

| Type | Description |
|------|-------------|
| MongoDB | The most common `NoSQL` database. It is free and open-source, uses the `Document-Based` model, and stores data in `JSON` objects |
| ElasticSearch | Another free and open-source `NoSQL` database. It is optimized for storing and analyzing huge datasets. As its name suggests, searching for data within this database is very fast and efficient |
| Apache Cassandra | Also free and open-source. It is very scalable and is optimized for gracefully handling faulty values |

## Development Frameworks & APIs
In addition to web servers that can host web applications in various languages, there are many common web development frameworks that help in developing core web application files and functionality. As most web applications share common functionality -such as user registration-, web development frameworks make it easy to quickly implement this functionality and link them to the front end components, making a fully functional web application. Some of the most common web development frameworks include:
    - Laravel (PHP): usually used by startups and smaller companies, as it is powerful yet easy to develop for.
    - Express (Node.JS): used by PayPal, Yahoo, Uber, IBM, and MySpace.
    - Django (Python): used by Google, YouTube, Instagram, Mozilla, and Pinterest.
    - Rails (Ruby): used by GitHub, Hulu, Twitch, Airbnb, and even Twitter in the past.
    
It must be noted that popular websites usually utilize a variety of frameworks and web servers, rather than just one.

- APIs connect the front end and back end - typically with GET and POST requests

### SOAP (API type)
- Specific protocol/standard for building APIs
- [SOAP](https://en.wikipedia.org/wiki/SOAP)
- The SOAP (Simple Objects Access) standard shares data through XML, where the request is made in XML through an HTTP request, and the response is also returned in XML. Front end components are designed to parse this XML output properly.

### REST (API type
- Specific protocol/standard for building APIs
- [REST](https://en.wikipedia.org/wiki/REST)
- The REST (Representational State Transfer) standard shares data through the URL path 'i.e. search/users/1', and usually returns the output in JSON format 'i.e. userid 1'.
- REST uses various HTTP methods to perform different actions on the web application:
    - GET request to retrieve data
    - POST request to create data (non-idempotent)
    - PUT request to create or replace existing data (idempotent)
    - DELETE request to remove data
    
## Public Vulns
- https://www.exploit-db.com/
- https://www.rapid7.com/db/
- https://www.vulnerability-lab.com/
- https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System
- https://nvd.nist.gov/


 
 
