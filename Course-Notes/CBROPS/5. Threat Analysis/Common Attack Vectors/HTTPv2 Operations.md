- ==Development==: Developed by IETF from the SPDY protocol.
- ==Features==: Uses header field compression, allows concurrent exchanges, and enables server push.

HTTP/2 also introduces an unsolicited push of data from the server to the client.

- HTTP/2 was developed by IETF from the SPDY protocol (Google).
- Uses the same URI schemes as HTTP/1.1.
- Reduces latency.
- Uses header field compression.
- Allows concurrent HTTP request/response exchanges onto the same TCP connection.
- Allows unsolicited push of data from server to client.

## HTTP/2 Streams

- HTTP/2 Streams: Independent, bidirectional sequences of frames exchanged between client and server over a single TCP connection.
- Stream Multiplexing: Each HTTP request/response exchange is assigned its own stream, allowing concurrent processing and preventing blocking issues.
- Stream Prioritization: Clients can assign priorities to streams to influence resource allocation and transmission order, but it’s not a guarantee.

Independent, bidirectional sequence of frames exchanged between the client and server.

- Flow control is through window_update frame, and cannot be disabled.
- Client assigns priority.

![3](/Course-Notes/.assets/Pasted_image_20241118174348.png)

## HTTP/2 Version Identification

The string h2 identifies HTTP/2’s use of Transport Layer Security (TLS). h2c indicates HTTP/2 over cleartext TCP.

  ```
GET / HTTP/1.1
Host: server.example.com
Connection: Upgrade, HTTP2-Settings
Upgrade: h2c
HTTP2-Settings: < HTTP/2 SETTINGS payload>
```

Clients making HTTP/2 requests without prior knowledge of server support use the HTTP upgrade mechanism. They send an HTTP/1.1 request with an upgrade header field containing h2c.

```
HTTP/1.1 200 OK
Content-Length: 243
Content-Type: text/html
```

Web servers that don’t support HTTP/2 ignore the upgrade header. Servers that do accept it with a 101 Switching Protocols response, after which they can send HTTP/2 frames.

```
HTTP/1.1 101 Switching Protocols
Connection: Upgrade
==Upgrade: h2c==

HTTP/2 frames ...
```

Application-Layer Protocol Negotiation (ALPN) is a TLS extension that lets the application layer negotiate secure connection protocols. Clients using HTTP/2 to an HTTP URI use TLS with ALPN, specifying h2 as the ALPN Next Protocol.

![2](/Course-Notes/.assets/Pasted_image_20241118174851.png)

## Other Features of HTTP/2

- ==Request Prioritization==: HTTP/2 allows prioritization of requests, improving performance by completing more important requests first.
- ==Server Push==: HTTP/2 enables servers to push responses to clients, potentially reducing latency by sending anticipated data.
- ==Header Compression==: HTTP/2 uses HPACK, a stateful header compression mechanism, to reduce redundant data in HTTP headers.

- ==HTTP/2 Message Processing==: Uses binary message framing for efficient processing, unlike HTTP 1.1’s plaintext messages.
- ==HTTP/2 Frame Composition==: Both headers and body are in binary format, collectively called a frame.
- ==Important HTTP/2 Frames==: Headers frame (Type = 0x1) and data frame (Type = 0x0), corresponding to HTTP/1.1 header and body.

## HTTP/2 PCAP Example

![1](/Course-Notes/.assets/Pasted_image_20241118175158.png)

The following observations can be made about this example PCAP output:

1. The Wireshark display filter is http2.
2. Under the HTTP decode, the 139.162.123.124 server supports HTTP/2. It accepted the upgrade to HTTP/2 with a 101 Switching Protocols response with the **h2c** protocol identifier in the upgrade header field. The string **h2c** indicates that HTTP/2 is run over cleartext TCP.
3. Under the HTTP/2 decode, the stream ID is 0, indicating that it is a connection control message. Settings are specified, including the maximum concurrent streams and initial window size.
4. Flow control is achieved through the window_update frame.

## HTTP/2 Vulnerabilities

- ==Vulnerabilities==: HTTP/2 implementations are vulnerable to denial-of-service (DoS) attacks.
- ==Impact==: Attacks can consume excessive system resources and lead to distributed DoS (DDoS) attacks.
- ==Recommendation==: Review CERT/CC’s Vulnerability Note VU#605641 and contact vendors for updates.
