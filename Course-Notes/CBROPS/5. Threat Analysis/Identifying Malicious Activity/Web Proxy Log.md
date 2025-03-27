- Malware Spread: Often spread through web browser vulnerabilities and uses HTTP/HTTPS for CnC communication.
- Web Proxy Functionality: Decrypts SSL/TLS traffic for inspection, logs HTTP/HTTPS traffic, and provides precise browsing session logs.
- Web Proxy Log Analysis: Helps investigate web-based attacks, such as identifying potential data exfiltration or malware droppers based on suspicious traffic patterns.

```
! Squid Web Proxy Access Log Example

1265529266.756 261 192.168.1.45 TCP_TUNNEL/200 3511 CONNECT services.example.com:443 - HIER_DIRECT/209.165.200.235
1265529273.873 8 192.168.1.254 TCP_HIT/200 1563 GET http://www.example.com/en-us/default/layout/previous.gif - NONE/- image/gif
1265529273.881 12 192.168.1.254 TCP_HIT/200 2961 GET http://www.example.com/gif/lightning-100x60.jpg - NONE/- image/jpeg
1364222662.246 90 192.168.0.6 TCP_MISS/200 619 GET http://www.example.com/pagead/conversion/? - DIRECT/172.16.0.152 image/gif
1364222662.257 85 192.168.0.6 TCP_MISS/200 2347 GET http://www.example.com/pagead/conversion/? - DIRECT/172.16.0.152 image/gif
1364222675.456 15 192.168.2.1 TCP_MISS/200 141159 GET http://spotlight2.com/system/logs/k1.exe 
1364222689.532 77 192.168.2.1 TCP_MISS/200 36098 GET http://spotlight2.com/module/4c06c7a4c2bd4567139df133455
```

- Log Entry Format: Describes the HTTP request or response, including timestamp, client information, and request details.
- Timestamp Format: Epoch time, representing the number of seconds since January 1, 1970, at midnight GMT.
- Epoch Time Conversion: Can be converted to a more familiar format using online converters.

- Log Entry Fields: IP address, HTTP method, URL, HTTP status code, and caching status.
- Caching Status: TCP_HIT (cached in web proxy cache), TCP_MEM_HIT (cached in RAM), or TCP_TUNNEL (traffic tunneled to the web server).
- TCP_TUNNEL Explanation: Squid proxy doesn’t understand or interpret tunneled traffic, such as encrypted HTTPS traffic.

- Suspicious Activity: Two GET requests for downloading an .exe followed by a suspicious filename.
- Malicious Website: http://spotlight2.com may be malicious based on Virustotal scan results.
- Virustotal Scan Results: 9 out of 68 URL scanners found the website to be malicious.

![1](/Course-Notes/.assets/Pasted_image_20241122140820.png)

- Malware Investigation: Investigate the k1.exe file, which is related to the Vawtrak malware.
- HTTP Event Analysis: Recognize common HTTP request methods and status codes, such as URL redirection.
- URL Redirection Attack: An attack where a victim’s browser is redirected from a legitimate to an attacker’s web page with exploit code, often due to unvalidated URL redirects in web applications.

- Phishing Attack Mechanism: An attacker sends a link that appears to be from a legitimate site, but redirects to a malicious site after the user enters their credentials.
- User Experience: Users are tricked into entering their credentials on a fake login page, which are then captured by the attacker.
- Attack Goal: The attacker aims to obtain valid credentials for accessing the legitimate site.

- URL Redirect Definition: A response with a status code beginning with 3 that causes a browser to display a different web page.
- Purpose of Status Codes: To indicate the purpose of the URL redirect, how to handle caching, and which request method to use for the subsequent request.
- Common HTTP Status Codes: Provided in the tables.
### **HTTP Status Codes**

|**Transaction/Error**|**Status**|**Description**|
|---|---|---|
|**Successful Transactions**|200|OK|
||201|Created|
||202|Accepted|
|**Redirected Transactions**|301|Moved permanently|
||302|Moved temporarily|
||304|Not modified|
|**Client-Side Errors**|400|Bad request|
||401|Unauthorized|
||403|Forbidden|
||404|Not found|
|**Server-Side Errors**|500|Internal server error|
||501|Not implemented|
||502|Bad gateway|
||503|Service unavailable|

---

### **Common HTTP Request Methods (from RFC 2616)**

| **Request Method**                           | **Definition**                   |
| -------------------------------------------- | -------------------------------- |
| **Common, Legitimate Requests**              |                                  |
| GET                                          | Retrieval and simple searches    |
| POST                                         | Submit data-query                |
| PUT                                          | Upload data-files                |
| **Uncommon, Potentially Malicious Requests** |                                  |
| HEAD                                         | Metadata retrieval               |
| DELETE                                       | Remove resource                  |
| TRACE                                        | Application layer trace of route |
| OPTIONS                                      | Request available methods        |
| CONNECT                                      | Tunnel SSL connection            |
| PROPFIND                                     | Retrieve properties of an object |
