
- ==DNS Activity Importance==: DNS logs are crucial for incident reconstruction and understanding attacker behavior, especially in detecting malware CnC using DGAs or fast-flux DNS.
- ==DNS Resolution Process==: Clients resolve domain names into IP addresses by sending requests to recursive name servers, which retrieve and return the information.
- ==Security Aspects of DNS==: Monitoring DNS queries and answers reveals who is accessing services and who is providing them, aiding in identifying potential security incidents.

- ==DNS Logging Challenges==: Difficult to analyze logs from various name servers with different logging capabilities and formats, and high volume of DNS queries.
- ==DNS Traffic Monitoring Solution==: Passively capture all DNS activity on the wire at major network choke-points and store them in a compressed format.
- ==Malicious DNS Request Identification==: Compare observed DNS activity with a baseline or model of normality to identify unusual patterns.

- ==Malicious DNS Requests==: Malware can use DNS requests to encode commands or exfiltrate data.
- ==Malware Example==: Multigrain: Multigrain malware steals credit and debit card information, using domains like dojfgj.com with hundreds of sub-domains for exfiltration.
- ==DNS Lookup Investigation==: Investigating unusual DNS requests, such as those with long sub-domains or those directed to suspicious domains, can reveal malware activity.

![3](/Course-Notes/.assets/Pasted_image_20241122135632.png)
![2](/Course-Notes/.assets/Pasted_image_20241122135637.png)
- ==Data Exfiltration Method==: The attacker used DNS queries to exfiltrate credit card data encoded in hexadecimal format.
- ==Data Encoding==: Credit card data was encoded in hexadecimal format and prepended to the sub-domain.
- ==Attacker’s Goal==: The attacker aimed to decode the data remotely and send sensitive information out of the network.

DNS query logging is disabled by default on most DNS servers and should be enabled.

- ==DNS Logging in Windows==: Enabled by checking checkboxes and selecting request/response logging.
- ==Logging Format==: Can log requests and responses together in a single entry.
- ==Log Size==: Can grow rapidly, especially on large networks, due to detailed logging designed for debugging.

![1](/Course-Notes/.assets/Pasted_image_20241122135721.png)

