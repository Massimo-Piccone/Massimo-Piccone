- ==Purpose==: Enables tunneling of another protocol through DNS for command and control, data exfiltration, or IP traffic tunneling.
- ==Setup==: To create a DNS tunnel, the attacker sets up a DNS server that resolves a domain name for the attack (acaerlxwsr.badguydomain .bad). The DNS tunneling server has a special logical interface configured with a DNS tunneling tool like Iodine. The target system also has a logical interface for tunneling IP traffic to the Internet. The DNS tunneling server is the authoritative name server for the attack domain, an Internet-accessible server controlled by the attacker.
- ==Mechanism==: Uses a malicious server as the authoritative name server for a specific domain to establish a tunnel between an infected client and the attacker-controlled server through the DNS resolver.
- ==Characteristics==: Often unmonitored and doesn’t require stealth, utilizing DNS for data transmission.

![1](/Course-Notes/.assets/Pasted_image_20241120111013.png)


- ==Benefit==: Difficult to detect due to the normal and expected nature of DNS traffic on a network.
- ==Drawback==: Slow speed and limited communication capabilities, as it typically doesn’t allow server-to-client communication.

**Detection:**
- ==Methods==: Examining payloads, packet size, frequency of requests, and unusual hostnames.
- ==Patterns==: Attackers may use a large bandwidth footprint or throttle usage to blend in with normal DNS traffic.

