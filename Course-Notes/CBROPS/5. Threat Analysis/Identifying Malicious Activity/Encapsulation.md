- Definition: The process of encapsulating the payload with an additional header for tunneling through intermediate networks.
- Keeping outsiders from getting in was the focus but now insider threats are increasing more and more.
- Insider Threat Detection: Identifying anomalies in data exfiltration to detect insider threats.

Lifecycle of an insider exfiltration:

1. Identify places where sensitive data is stored.
2. Retrieve the data from the location.
3. Move the data within the organization to prepare for exfiltration.
4. Transfer the data outside the organization.

- ==Protocol Tunneling==: (EG HTTPS/HTTP/DNS) Encapsulates data packets inside a different protocol to bypass firewalls during Exfiltration.
- ==Detection==: Performing anomalous behaviors on outbound traffic can detect data leaking using tunneling.

- ==DNS Tunneling==: Uses the DNS protocol to communicate non-DNS traffic over port 53 by encapsulating non-DNS data inside DNS queries and responses.
- Attacks like Morto and Feederbot added better stealth to CnC callbacks.

- ==DNS Exfiltration==: Attackers manipulate DNS requests to exfiltrate data from a compromised system.
- ==CnC DNS Manipulation==: DNS responses are manipulated for Command and Control (CnC) callbacks from the attacker’s infrastructure to a compromised system.
- ==Vulnerability==: Enterprise network firewalls allow DNS traffic over port 53.

	Many free tunneling software packages. EG: [Iodine](https://code.kryo.se/iodine/) 

## DNS Tunnels

Manual DNS Review is Challenging and time consuming.
Instead we use Baselines and Abnormality for visibility.

- Unusual DNS Request: Malware could encode stolen data as the subdomain part of a DNS lookup for a domain where the name server is controlled by an attacker.
- Data Exfiltration via DNS: Malware can tunnel out data by encoding it as a subdomain and sending a DNS lookup request to a domain controlled by the attacker.
- Data Encoding Methods: Two common encoding methods used to avoid detection are Base32 and Base64 encoding.

![2](/Course-Notes/.assets/Pasted_image_20241124145600.png)

- DNS Traffic Trends: Big and complex packets will become more common with future DNS protocol extensions.
- DNS Security Challenges: Traditional detection techniques may not be sufficient to prevent data leaks over DNS.
- DNS Security Solution: Adding a security solution that inspects and filters DNS traffic can help contain botnets.

Countermeasures:
- Monitor the DNS log for suspicious activities such as DNS queries with unusually long and suspicious domain names.
- Deploy a solution such as Cisco Umbrella to block the DNS tunneling traffic from going out to malicious domains.

![1](/Course-Notes/.assets/Pasted_image_20241124145634.png)

## Other Tunnels

 FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel.

Adversaries may leverage various operating system utilities to exfiltrate data over an alternative protocol.

