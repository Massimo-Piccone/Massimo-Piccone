## HTTP Protocol Fundamentals

HTTP is a stateless client/server protocol where the web browser is the client and the web server is the server. The default port for HTTP is TCP port 80, but other ports can be used.

A client’s web browser sends an HTTP request to the web server, which consists of three parts:
1. The HTTP request method, URI, and protocol name and version
2. HTTP request headers that define the transaction parameters and provide client information
3. HTTP request body

The web server responds with three parts:
1. HTTP protocol name and version, and the status code (e.g., 200 for successful processing)
2. HTTP response headers that define the transaction parameters and provide server information
3. HTTP response body

## URI and URL

A URI identifies a resource by location or name, 
A URL specifies its location and retrieval method. The “access mechanism/protocol” or “network location,” such as ==http==://, ==https==://, or ==ftp==://, distinguishes a URL from a URI.

For instance, http://www.example.com/index.html requests the file named index.html in the root directory of the www.example.com web server.

Below is an example URL with descriptions of each part:

`http://www.example.cisco.com:80/video?docid=96673783583808&hl=en#00h01m15s`

- Protocol: http (can also be https, ftp, etc.
- Host: www.example.cisco.com
- Host (or Prefix): www. Subdomain: example.cisco.com. Domain: cisco.com. Top-Level Domain: .com.
- Port: If not specified, port 80 is assumed.
- Path: /video. Path refers to a file or location on the web server, akin to a directory structure.
- Parameters: ?docid=96673783583808&hl=en. The docid parameter refers to a specific video file, while the hl=en parameter sets the video subtitle to English.

URL parameters, also called “query strings,” are key-value pairs that provide extra information in URLs. They start with a question mark (?) and are separated by an ampersand (&).

Fragments, or named anchors, are used to refer to internal sections within a web document. For example, \#00h01m15s means skip to 1 minute and 15 seconds into the video.

Some characters, like spaces, cannot be part of a URL, while others have special meanings. URL encoding is used to handle these issues, for instance, a space can be encoded as a plus sign (+) or %20.


## HTTP Request Methods

HTTP defines different request methods to indicate the desired action to be performed on the identified resource. The common HTTP request methods include GET, HEAD, POST, PUT, and DELETE, to name a few.

- The ==GET== method retrieves data from the specified resource.
- The ==HEAD== method asks for a response identical to that of a GET request, but without the response body
- The ==POST== method creates data on the specified resource.
- The ==PUT== method request is used to update data on the specified resource.
- The ==DELETE== method deletes the specified resource.

## HTTP Request and Response Packets Capture Example

Wireshark screenshot shows HTTP packets, with client requests in red and server responses in blue.

![4](/Course-Notes/.assets/Pasted_image_20241118153201.png)

**User Agent** 
- ==Functionality==: Identifies the web browser, version, and operating system to the web server.
- ==Usage==: Websites use it to adjust page design, while attackers manipulate it for malicious purposes.
- ==Example==: In the provided example, the user agent string indicates Firefox version 48.0 running on Windows 7.

```
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0
```

**HTTP Response**
- ==Status==: 200, indicating the request was successful.
- ==Headers==: Contain information about the web server (Apache/2.2.22) and content type (text/HTML).
- ==Body==: Contains the requested web page content, which is the default page indicating the server is running but no content has been added.

```
It works!
This is the default web page for this server.
The web server software is running but no content has been added, yet.
```

![3](/Course-Notes/.assets/Pasted_image_20241118153445.png)

## HTTP Status Codes

The HTTP server responses are classified by a numerical status code. Status codes indicate the reasons behind successful and failed HTTP requests. The IANA maintains the official registry of the HTTP status codes.

Status codes starting with 1xx are Informational, 2xx are Success, 3xx are Redirection, 4xx are Client Error, and 5xx are Server Error.

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

- ==Definition==: Small pieces of data sent from web servers and stored in browsers to remember stateful information or browsing activity.
- ==Usage==: Used to store information like shopping cart items, login credentials, and browsing history.
- ==Security==: Access to browser cookies grants access to stored information, making them a potential security risk.

![2](/Course-Notes/.assets/Pasted_image_20241118154324.png)


Cookies are passed between the web server and web browser using the **Set-Cookie** HTTP header field in the HTTP response, and the **Cookie** HTTP header in the HTTP request.

The web server sends the following to the web browser in the HTTP response header to create a cookie on the web browser:

```
Set-Cookie: <_name_>=<_value_>[; <_name_>=<_value_>]...
[; expires=<_date_>][; domain=<_domain_name_>]
[; path=<_some_path_>][; secure][; httponly]
```

The web browser sends the cookie information back to the web server in the HTTP request header:

```
Cookie: <_name_>=<_value_> [;<_name_>=<_value_>]...
```

For example, the web browser sends its first HTTP request to **www.example.org**:

```
GET /index.html HTTP/1.1
Host: http://www.example.org
```

The web server responds with two **Set-Cookie** headers:

```
HTTP/1.0 200 OK
Content-type: text/html
==Set-Cookie: theme=light
Set-Cookie: sessionToken=abc123; Expires=Wed, 01 Jun 2020 10:00:00 GMT==
```

The web browser sends another HTTP request to visit the **ccna.html** page on the website. This HTTP request contains the two cookies that the web server instructed the web browser to set:

```
GET /ccna.html HTTP/1.1
Host: http://www.example.org
==Cookie: theme=light; sessionToken=abc123==
```

- Session Token Cookie Function: Identifies a particular session for the web server to track and manage user requests.
- Cookie-Based Session Hijacking: Attackers can impersonate users by stealing and using their cookies, allowing them to perform actions on behalf of the victim’s session.
- Mitigating Cookie Hijacking: Use HTTPS to encrypt web server and browser communications, and set the Secure flag on cookies to ensure they are only transmitted over encrypted connections.

## HTTP Referer

- Referer Header Definition: The address of the previous web page from which a link to the currently requested page was followed.
- Referer Header Usage: Indicates the last page that the user was on when clicking a link.
- Referer Header Example: In an HTTP GET request, the referer header might contain “http://www.cisco.com” if the user clicked a link from the www.cisco.com home page.

![1](/Course-Notes/.assets/Pasted_image_20241118155710.png)