**SSL Vulnerability:** SSL v3.0 is insecure due to the POODLE vulnerability, leading to its widespread disablement.

## HTTPS
- ==Purpose==: Provides secure communication between clients and servers over the internet.
- ==Operations==: Uses TLS/SSL handshake for secure connection, authenticates web servers using digital certificates, and encrypts data transmission.
- ==Security Analysts==: Understanding HTTPS is crucial for identifying and mitigating attacks that exploit its features.
- ==Traffic Inspection==: Organizations can inspect HTTPS traffic by deploying next-generation firewalls or web proxies that act as MITMs to decrypt, inspect, and re-encrypt SSL/TLS traffic.
- ==Security Analyst’s Role==: Security analysts investigating security incidents involving HTTPS traffic often need to inspect logs from next-generation firewalls or web proxies to analyze SSL/TLS decryption events.
- ==Compliance Considerations==: Organizations performing SSL/TLS decryption must ensure they comply with relevant government regulations regarding data confidentiality.

## Web Server Digital Certificate

- ==DC Purpose==: Communicates web service host ownership to clients, preventing impersonation.
- ==CA Role==: Issues signed digital certificates on behalf of web service owners.
- ==HTTPS Validation==: Web browsers trust certificate authorities to ensure secure connections.

![2](/Course-Notes/.assets/Pasted_image_20241118173746.png)

- ==Certificate Warning==: The browser warns the user about an untrusted digital certificate.
- ==User Decision==: The user can accept the risk and continue or ignore the warning.
- ==Impact==: Ignoring the warning and visiting a malicious website breaks HTTPS security and allows attackers to impersonate the web server.

![1](/Course-Notes/.assets/Pasted_image_20241118173858.png)

