# SQL Injection Fundamentals
- A SQL injection occurs when a malicious user attempts to pass input that changes the final SQL query sent by the web application to the database, enabling the user to perform other unintended SQL queries directly against the database.
- Caused by poorly coded web apps, poorly secured back-end servers or DB privs
- Structured Query Language (SQL)
- Database Management Systems (DBMS)
- User --> Client App (tier 1) --> App server (tier 2) --> DBMS
- The relationship between tables within a database is called a Schema.

## Relational DBs
- Structured data in tables with rows and columns
- Fixed schema (predefined structure)
- Use SQL for queries
- ACID compliance (reliable transactions)
- Scale vertically (more powerful hardware)
- Great for complex relationships and consistent data
- Examples: MySQL, PostgreSQL, Oracle

## Non-relational DBs
- A non-relational database (also called a NoSQL database) does not use tables, rows, and columns or prime keys, relationships, or schemas. Instead, a NoSQL database stores data using various storage models, depending on the type of data stored. 
- Flexible data formats (documents, key-value, graphs)
- Dynamic schema (structure can change)
- Various query languages
- Eventually consistent (prioritizes availability)
- Scale horizontally (add more servers)
- Great for rapid development and large-scale applications
- Examples: MongoDB, Redis, Cassandra

## mysql
- The mysql utility is used to authenticate to and interact with a MySQL/MariaDB database.
- `mysql -u root -p` | `mysql -u root -p<password>` (NOTE: no space between -p and password)
- We can view which privileges we have using the SHOW GRANTS command (https://dev.mysql.com/doc/refman/8.0/en/show-grants.html)
- Other useful commands:
	- https://dev.mysql.com/doc/refman/5.7/en/create-database.html
	- https://dev.mysql.com/doc/refman/8.0/en/show-databases.html
	- https://dev.mysql.com/doc/refman/8.0/en/describe.html
	
## SQL Injection
- Payloads for auth bypass: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/SQL%20Injection#authentication-bypass
- If we use user-input within an SQL query, and if not securely coded, we might have a SQL Injection vulnerability.
- NOTE: In some cases, we may have to use the URL encoded version of the payload. An example of this is when we put our payload directly in the URL 'i.e. HTTP GET request'.
- In SQL, using two dashes only is not enough to start a comment. So, there has to be an empty space after them, so the comment starts with (-- ), with a space at the end. This is sometimes URL encoded as (--+), as spaces in URLs are encoded as (+). To make it clear, we will add another (-) at the end (-- -), to show the use of a space character.
- The # symbol can be used as well for SQL comments
- Don't forget you can UNION your way to other data
- When filling other columns with junk data, we must ensure that the data type matches the columns data type, otherwise the query will return an error. For the sake of simplicity, we will use numbers as our junk data, which will also become handy for tracking our payloads positions.
- For advanced SQL injection, we may want to simply use 'NULL' to fill other columns, as 'NULL' fits all data types.

## Database Enumeration
The following queries and their output will tell us that we are dealing with MySQL:
| Payload | When to Use | Expected Output | Wrong Output |
|---------|-------------|-----------------|--------------|
| `SELECT @@version` | When we have full query output | MySQL Version 'i.e. `10.3.22-MariaDB-1ubuntu1`' | In MSSQL it returns MSSQL version. Error with other DBMS. |
| `SELECT POW(1,1)` | When we only have numeric output | `1` | Error with other DBMS |
| `SELECT SLEEP(5)` | Blind/No Output | Delays page response for 5 seconds and returns `0`. | Will not delay response with other DBMS |

- The INFORMATION_SCHEMA database contains metadata about the databases and tables present on the server (https://dev.mysql.com/doc/refman/8.0/en/information-schema-introduction.html)
- to reference a table present in another DB, we can use the dot ‘.’ operator. For example, to SELECT a table users present in a database named my_database, we can use: `SELECT * FROM my_database.users`
- See what DBs are available: `SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA;`
- The COLUMNS table contains information about all columns present in all the databases. 

## Reading / Writing files
- To be able to find our current DB user, we can use any of the following queries:
```
SELECT USER()
SELECT CURRENT_USER()
SELECT user from mysql.user
```
- See if we have super admin: `SELECT super_priv FROM mysql.user` (SUPER is the role)
- Supposedly we can list privs with this command: `cn' UNION SELECT 1, grantee, privilege_type, 4 FROM information_schema.uer_privileges-- -`
- Load file commands (if perms allow): `SELECT LOAD_FILE('/etc/passwd');` We will only be able to read the file if the OS user running MySQL has enough privileges to read it.
- To be able to write files to the back-end server using a MySQL database, we require three things:
    - User with FILE privilege enabled
    - MySQL global secure_file_priv variable not enabled
    - Write access to the location we want to write to on the back-end server
- The secure_file_priv variable is used to determine where to read/write files from (https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#secure_file_priv)
- An empty value lets us read files from the entire file system. Otherwise, if a certain directory is set, we can only read from the folder specified by the variable. On the other hand, NULL means we cannot read/write from any directory. MariaDB has this variable set to empty by default, which lets us read/write to any file if the user has the FILE privilege. 
- Once confirmed we can write files to back-end server,  the SELECT INTO OUTFILE statement can be used to write data from select queries into files. 
- `SELECT * from users INTO OUTFILE '/tmp/credentials';`
- We can also SELECT strings into files: `SELECT 'this is a test' INTO OUTFILE '/tmp/test.txt';`
- To write a web shell, we must know the base web directory for the web server (i.e. web root). One way to find it is to use load_file to read the server configuration, like Apache's configuration found at /etc/apache2/apache2.conf, Nginx's configuration at /etc/nginx/nginx.conf, or IIS configuration at %WinDir%\System32\Inetsrv\Config\ApplicationHost.config, or we can search online for other possible configuration locations. Furthermore, we may run a fuzzing scan and try to write files to different possible web roots, using this wordlist for Linux or this wordlist for Windows. Finally, if none of the above works, we can use server errors displayed to us and try to find the web directory that way.
	- https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-linux.txt
	- https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/default-web-root-directory-windows.txt



