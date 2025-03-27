Gaining access to and control of a host may seem impossible. But, It only takes a one weakness.

Common Methods: 
- Phishing campaigns, 
- Malware collection, and 
- Directing users to fake login portals.
- Data leaks
- Exfiltration 
- Exploiting weak services
- Credential staffing
- Online misconfigurations.
Targets: 
- Employee credentials for remote network access.
Alternaitves:
- Password Brute-Forcing (Offliine)
- Password Spraying (Avoids Lockout)
Metigation:
- Changing default credentials
- Limiting attack surface public-facing systems
- Enforcing strong password policies
- Regularly auditing password policies

If attackers can gain access to an endpoint, they can also gain control of the endpoint and use it to launch more wide-spread attacks
- Pivoting
- Installation
- Exfiltration
- Botnet Control

Botnets:
Bots can log keystrokes, gather passwords, capture packets, financial information, launch DoS attacks, relay spam, and open back doors. 

1. A botnet operator sends self-propagating malware designed connect victim to C&C servers. 
2. They exploit back doors opened by worms and viruses. Bots are more versatile than worms in  infection vectors and can be modified quickly. 
3. The newly infected host logs into the CnC server and awaits commands. 
4. Instructions from the CnC server to each bot in the botnet execute actions. 
5. When the zombies receive the instructions, they generate malicious traffic aimed at the victim.

DDoS:
- An attacker controls zombies to launch a DDoS attack against the victim’s infrastructure.
- Zombies use a covert channel to communicate with the CnC server controlled by the attacker.
- ==Communication== often occurs over IRC, encrypted channels, bot-specific peer-to-peer networks, and even Twitter.

![1](/Course-Notes/.assets/Pasted_image_20241124142551.png)
## Nyetya Ransomware Event

- Target: Organizations in Ukraine and multinational corporations with operations in Ukraine.
- Attack Vector: Supply chain attack through M.E.Doc software, utilizing stolen credentials and exploiting vulnerabilities like EternalBlue and PsExec.

Mechanisms:
- **EternalBlue:** The same exploit used by WannaCry,
- **EternalRomance:** An SMBv1 exploit leaked by "ShadowBrokers,"
- **PsExec:** A legitimate Windows administration tool.
- **WMI:** Windows Management Instrumentation, a legitimate Windows component.

- Malware Functionality: Attempts to install and execute perfc.dat on other devices for lateral spread.
- Attack Nature: "Destructive" - Cisco Talos.
- Impact: Broad-reaching, with over 2000 affected companies in Ukraine.

