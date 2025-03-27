%% #review %%
# [[Common TCP - IP Attacks]]
#### ARP 
Use Ethertype **0x0806**
0x0800 indicates IPv4,
0x86DD indicates IPv6.
	Arp poisoning
#### Legacy TCP/IP Vulnerabilities
TCP/IP protocol suite (RFC 793)
TCP - IP - UDP - ICMP

Designed to work in a trusted environment
- ﻿﻿Early TCP/IP protocols are insecure  
    Susceptible to password sniffing and DoS attacks
    Example: r-utilities, rlogin, rop, rsh

## IP Vulnerabilities

| Attack Type                 | Description                                                             | Details                                                                                                      |
| --------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Man-in-the-middle attack    | Intercepts communication between two systems.                           | Attacker inserts a device to grab packets, modify them, and forward them.                                    |
| Session hijacking           | Gains physical access, initiates MITM, and hijacks the session.         | Gains physical access, initiates MITM, and hijacks the session.                                              |
| IP address spoofing         | Attacker spoofs the source IP address in an IP packet.                  | Used for inspection (nonblind) or in DoS attacks (blind).                                                    |
| DoS attack                  | Prevents legitimate users from accessing information or services.       | Targets computers and networks to disrupt email, websites, online accounts, and other services.              |
| DDoS attack                 | A DoS attack from multiple source machines simultaneously.              | Best-known example is the ‘smurf’ attack, launched using programs like Trinoo, TFN, TFN2K, and Stacheldraht. |
| Resource exhaustion attacks | Consumes server or network resources to disrupt service.<br>FORM OF DOS | Targets IP routers, affecting CPU, packet memory, route memory, network bandwidth, and vty lines.            |
| Smurf attack                | Exploits IP broadcast addressing to create a DoS.                       | Uses ICMP ping to overwhelm a hacked machine with responses from broadcast ping messages.                    |
## ICMP Vulnerabilities

| **Reconnaissance and scanning** | Description                                                                   | Potential Impact                                                                         |
| ------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| ICMP unreachables               | Used for network reconnaissance, revealing protocol/port availability.        | Attackers can gather information about the target network.                               |
| ICMP mask reply                 | Used to map IP networks by revealing subnet mask information.                 | Malicious actors can map the target’s IP network.                                        |
| ICMP redirects                  | Used to notify senders of better routes, potentially leading to MITM attacks. | Attackers can redirect traffic through their routers, intercepting communications.       |
| ICMP router discovery           | Allows hosts to locate routers, but lacks authentication.                     | MITM attacks and spoofed route entries are possible, leading to potential DoS.           |
| Firewalk                        | An active reconnaissance technique to analyze gateway ACL filters.            | Attackers can map out the target’s network by analyzing ICMP responses to packet probes. |
Other

| Technique                        | Description                                                                                                                                                                                                                        | Example                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **ICMP tunneling**               | Establishes a covert connection between two remote computers using ICMP echo requests and reply packets.                                                                                                                           | LOKI program uses ICMP for a covert channel to transmit data secretly.                                       |
| **ICMP-based OS fingerprinting** | Uses ICMP to determine the operating system running on a device.                                                                                                                                                                   | TTL value of 128 in ICMP reply indicates a Windows machine; TTL value of 64 indicates a Linux-based machine. |
| **ICMP flood attack**            | Overwhelms the targeted resource with ICMP echo request (ping) packets, large ICMP packets, and other ICMP types to saturate and slow down the victim’s network infrastructure.                                                    | ![15](/Course-Notes/.assets/Pasted_image_20241112165721.png)                                                                         |
| **Smurf attack**                 | Broadcasts many ICMP echo request packets using a spoofed source IP address (the victim’s IP address) to a network using an IP broadcast address. This leads to congestion of the victim’s network with ICMP echo replies traffic. | ![14](/Course-Notes/.assets/Pasted_image_20241112165744.png)                                                                         |
# TCP Vulnerabilities

| TCP SYN Flooding    | Description                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| Definition          | DoS attack exploiting a TCP characteristic (SYN, SYN-ACK, ACK) to overwhelm server processes.          |
| Vulnerable Services | Any service binding to and listening on a TCP socket.                                                  |
| Attack Mechanism    | Creates numerous half-open connections, exhausting the finite data structure for tracking connections. |
| Connection State    | Half-open connections, initiated but not completed.                                                    |
| Network Traffic     | SYN->/<-SYN-ACK. If the handshake is not completed, the connection remains in the half-open state.     |
| Impact              | Server becomes disabled if enough half-open connections are created to fill the data structure.        |
| Mitigation          | Set a time limit for half-open connections and delete them after the timeout.                          |
| Attacker’s Goal     | Disrupt the victim’s ability to accept new incoming legitimate TCP connections.                        |
| Spoofed Address     | May belong to a connected host, which will send a reset to end the handshake.                          |
Variations

| Attack Type           | Description                                                                       | Attack Mechanism                                                                          | Prevention                                                                                         | Defense                                              |
| --------------------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Direct attack         | Attackers rapidly send SYN segments ==without spoofing their IP== source address. | Multiple TCP connect() calls, preventing SYN-RECEIVED to maintain connection.             | Firewall rules to filter outgoing packets to the listener or incoming SYN-ACKs.                    | Block packets with the attacker’s source IP address. |
| Spoofing-based attack | Attacker ==spoofes and injects raw IP== packets with valid IP and TCP headers.    | Spoofing many different source addresses, assuming some will be unresponsive to SYN-ACKs. | Machines at spoofed source addresses must not respond to SYN-ACKs.                                 | Not specified                                        |
| Distributed attack    | Attacker ==uses Botnet== flood the target.                                        | Each drone uses a spoofing attack with multiple spoofed addresses.                        | Challenging due to the dynamic nature of botnets (IP address changes, machine additions/removals). | Not specified                                        |
## TCP Session Hijacking

| Attack Type                   | Description                                                         | Methods                                 | Tools                                  |
| ----------------------------- | ------------------------------------------------------------------- | --------------------------------------- | -------------------------------------- |
| TCP Session Hijacking         | Attacker predicts or obtains TCP ISN to spoof as the original host. | Predict ISN, send spoofed ACK packet    | N/A                                    |
| Application Session Hijacking | Hijack existing or create new sessions using stolen data.           | Sniff HTTP packets to obtain session ID | Juggernaut, Hunt, TTY Watcher, T-Sight |

| Type               | Description                                              | Difficulty     | Notes                                                      |
| ------------------ | -------------------------------------------------------- | -------------- | ---------------------------------------------------------- |
| Non-blind spoofing | Attacker ==can see traffic== between host and target.    | Easiest        | Requires packet capture between the two machines.          |
| Blind spoofing     | Attacker ==cannot see traffic== between host and target. | Most difficult | Nearly impossible to correctly guess TCP sequence numbers. |
## TCP Reset Attack

| Method           | Description                                                                      | Effect                                        | Usage                                                                                         |
| ---------------- | -------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------- |
| FIN Bit          | Sends a packet with the FIN bit set.                                             | Closes the connection after proper handshake. | Regular way to terminate a TCP connection.                                                    |
| RST Bit          | Sets the RST bit to 1 in the TCP flags field.                                    | Immediately terminates the connection.        | Abrupt way to close a connection. Commonly seen when sending data to a closed port or server. |
| TCP Reset Attack | Sends a spoofed packet with the RST bit set, pretending to be from a valid host. | Disrupts the TCP connection.                  | Maliciously terminates a connection between two hosts.                                        |
![13](/Course-Notes/.assets/Pasted_image_20241112182648.png)
# UDP Vulnerabilities

| Protocol    | Vulnerability                | Description                                                                                                           | Impact                                                                     | Examples                                                  |
| ----------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------- |
| UDP         | Optional checksum            | Lack of verification management makes it easy to recompute checksums, allowing alterations to application data.       | Data tampering, potential for unauthorized access or manipulation.         | NFS, SNMP, DNS, TFTP, online games, streaming media, VoIP |
| SNMPv1, DNS | Eavesdropping                | Attackers can intercept and modify messages if they are not encrypted and the attacker knows the message format.      | Information disclosure, potential for unauthorized access or manipulation. | SNMPv1, DNS                                               |
| UDP         | Resource exhaustion          | Attacks target shared resources like buffers or link capacity, leading to system crashes or other insecure behaviour. | Denial of service, potential for unauthorized access or manipulation.      | UDP flood (UDP Unicorn attacks)                           |
| UDP         | Protocol implementation bugs | Exploiting bugs in UDP protocol implementations can lead to various security issues.                                  | Depends on the specific bug being exploited.                               | Various                                                   |
# [[Attack Surface and Attack Vectors]]

## Attack Surface - Sum of Vulnerabilities
#### The **network** attack surface.

| Component            | Description                                                    | Example                                           |
| -------------------- | -------------------------------------------------------------- | ------------------------------------------------- |
| Ports                | Open ports on devices that can be exploited.                   | Port 21 (FTP)                                     |
| Protocols            | Network communication standards with inherent vulnerabilities. | Telnet, FTP, HTTP, SMTP                           |
| Channels             | Data transmission pathways that can be intercepted.            | Unencrypted network connections                   |
| Devices              | Smartphones, laptops, routers, firewalls, etc.                 | Unpatched smartphone with a known vulnerability   |
| Services             | Network-accessible services that can be attacked.              | SSH server with weak authentication               |
| Network Applications | Software running on remote servers.                            | Vulnerable web application in a cloud environment |
| Firmware Interfaces  | Software that controls devices.                                | Printer firmware with a buffer overflow flaw      |
#### The **software** attack surface.

| Component          | Description                                                                  |
| ------------------ | ---------------------------------------------------------------------------- |
| Applications       | Software applications running on the system.                                 |
| Email Services     | Email services and protocols.                                                |
| Configurations     | System configurations and settings.                                          |
| Compliance Policy  | Compliance policies and regulations.                                         |
| Databases          | Database systems and data.                                                   |
| Executables        | Executable files and programs.                                               |
| DLLs               | Dynamic Link Libraries (DLLs).                                               |
| Web Pages          | Web pages and web applications.                                              |
| Mobile Apps        | Mobile applications.                                                         |
| Device OS          | Operating system of the device.                                              |
| Unpatched Software | Software with known vulnerabilities (e.g., Java, Adobe Reader, Adobe Flash). |
#### The **physical** attack surface. 

| Threat Type      | Example                                                                        |
| ---------------- | ------------------------------------------------------------------------------ |
| Inside Threats   | Rogue employee steals sensitive data.                                          |
| ''               | Social engineering attack tricks an employee into revealing login credentials. |
| ''               | Intruder posing as a service worker gains unauthorized access to a system.     |
| External Threats | Attacker retrieves passwords from discarded hardware.                          |
| ''               | Attacker obtains passwords from sticky notes left in plain sight.              |
| ''               | Physical break-in allows unauthorized access to sensitive information.         |
| ''               | Attacker steals or downloads an entire drive, extracting sensitive data later. |
#### The **social engineering** attack surface.

| Attack Type                 | Description                                                        | Example                                                                                              |
| --------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Fake Calls to IT            | Poses as an employee to obtain a password.                         | Attacker calls IT support, pretending to be a lost employee.                                         |
| Media Drops                 | Infected media (e.g., flash drive) in a public area.               | An employee finds a flash drive in the parking lot and plugs it into their work computer.            |
| Socially Engineered Trojans | Tricks user into running a Trojan on a trusted website.            | User visits a compromised website that prompts them to download a seemingly legitimate update.       |
| Spear-Phishing              | APT attacker sends targeted phishing emails to multiple employees. | An employee receives an email appearing to be from a trusted sender, containing a Trojan attachment. |
## Attack Vectors - Path to gaining access.

| Attack Type                      | Description                                                                        |
| -------------------------------- | ---------------------------------------------------------------------------------- |
| Reconnaissance                   | Gathering information about targeted computers or networks.                        |
| Known vulnerabilities            | Exploiting weaknesses in hardware and software.                                    |
| SQL injection                    | Manipulating SQL database queries to gain unauthorized access.                     |
| Phishing                         | Sending spam email with malicious links to trick users into revealing credentials. |
| Spear phishing                   | Targeted phishing attacks aimed at specific individuals.                           |
| Advanced Persistent Threat (APT) | Covert cyber attacks to gain and maintain unauthorized access to a network.        |
| Malware                          | Malicious software such as viruses, worms, Trojans, spyware, and rootkits.         |
| Weak authentication              | Exploiting poorly designed or implemented authentication mechanisms.               |
## Security Risks and Challenges
![12](/Course-Notes/.assets/Pasted_image_20241113115914.png)
# Network
## Reconnaissance Attacks

| Subcategory         | Description                                                        | Example                           |
| ------------------- | ------------------------------------------------------------------ | --------------------------------- |
| Packet sniffers     | Capture and analyze network traffic for useful information.        | Wireshark, Ettercap, NetworkMiner |
| Ping sweeps         | Determine which machines on a network are alive and reachable.     | fping command                     |
| Port scans          | Identify open ports and associated applications on a host network. | NMAP                              |
| Information queries | Resolve hostnames from IP addresses or vice versa.                 | nslookup command                  |
### Passive and Active Reconnaissance

| Attack Type            | Description                                                         | Tools/Techniques                                                                  |
| ---------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Passive Reconnaissance | Gathering information without directly interacting with the target. | Whois, nslookup, dig, Shodan Search Engine                                        |
| Active Reconnaissance  | Interacting with the target to gather information.                  | Ping sweeps, traceroutes, port scans, operating system fingerprinting, traceroute |

## Access Attacks

| Attack Type                  | Description                                                                                                  | Impact                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| Password attack              | Used to obtain system access                                                                                 | Unauthorized access to read, modify, or delete data, and add, modify, or remove network resources |
| Spoofing/masquerading attack | One person or program successfully masquerades as another by falsifying data and gaining illegitimate access | Unauthorized access to sensitive information or resources                                         |
| Session hijacking            | The session established by the client to the server is taken over by a malicious person or process           | Unauthorized access to sensitive information or resources                                         |
| Malware                      | Used to infect the victim’s system with malicious software                                                   | System compromise, data theft, or other malicious activities                                      |
#### Security Recommendations

- ﻿﻿Filter unwanted IP access using ACLs
- ﻿﻿Use Multifactor authentication when possible  
    SMS
- ﻿﻿Use WPA2 for wireless networks
- ﻿﻿IDS/IPS
- ﻿﻿Use real-time password generators
- ﻿﻿Enforce AAA  
    CISCO ISE
## Man-in-the-Middle Attacks

| OSI Layer         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Physical layer    | Tap someone’s physical connection, and send all packets to the MITM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Data link layer   | Use ARP poisoning to cause victims to send all their packets to the MITM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Network layer     | Manipulate packet routing to route all the packets to the MITM                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Session layer     | SSL/TLS MITM de-crypts, examines, then re-encrypts the HTTP over SSL/TLS traffic. For this attack to work, the victim’s web browser must trust the certificate that is presented by the SSL/TLS MITM which can be caused by first injecting some malware into the victim’s web browser.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Application layer | Man-in-the-browser attack. Like most attacks, man-in-the-browser begins with a malware infection. The malware injects itself into the victim’s web browser, and waits in stealth mode until the user visits a specific website. At that point, the malware goes into action, tricking the user into entering sensitive information on the web page. Different types of malware typically have different attack targets hardcoded into its code. For example, Zeus generally targets banking sites. When the malware is activated, it may manipulate the web page being loaded by injecting extra fields into the web page to collect sensitive pieces of information, or act as a keylogger to intercept the data. The idea is that no matter how careful you are about scrutinizing URLs and ensuring that you go to the correct website, the web browser cannot be trusted because it has been compromised. |

| Attack Type                   | Description                                                                                                                        | Details                                                                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| ARP Poisoning                 | Attacker spoofs MAC addresses, poisoning ARP caches of two devices.                                                                | Victim devices send packets to the attacker, allowing interception.                                  |
| ICMP-based MITM               | Attacker spoofs ICMP redirect messages, routing victim traffic through an attacker-controlled router.                              | Threat mitigated by routers with static routes or those that ignore ICMP redirects.                  |
| DNS-based MITM (DNS Spoofing) | Attacker supplies false DNS information, redirecting victims to attacker-controlled websites[.](https://www.xyzbank.com/)          | [Used](https://www.xyzbank.com/) to steal sensitive information, such as online banking credentials. |
| DHCP-based MITM               | Attacker intercepts DHCP queries and responses, gaining network information (hostnames, MAC addresses, IP addresses, DNS servers). | Can be combined with DoS attacks on the real DHCP server to increase success.                        |
#### Securing Against MITM

- ﻿﻿VPN
- ﻿﻿Digital Certificates for Authentication
- ﻿﻿Strong Passwords and Multifactor Authentication
- ﻿﻿Dynamic ARP Inspection
- ﻿﻿IP Spoofing Detection
- ﻿﻿DHCP Snooping
## DoS & DDoS

| Attack Type                          | Description                                                                                             | Details                                                                                                                                                                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TCP SYN Flood Attack (DoS)**         | Exploits TCP three-way handshake by sending SYN packets with fake source addresses.                     | Victim’s connection table fills with incomplete connections, denying legitimate TCP services. Hard to trace due to source IP spoofing.                                                                        |
| Ping of Death (DoS)                  | Uses oversized packet fragments to crash systems by exceeding IP’s maximum packet size limit.           | Exploits vulnerabilities in IP processing, with variations targeting protocols like SNMP, syslog, DNS. Largely mitigated in modern systems, especially IPv4; IPv6 versions persist.                           |
| ICMP and UDP Floods (DoS)            | ICMP Flood: Overloads network with echo requests to slow down services.                                 | UDP Flood: Sends numerous UDP packets, draining target resources and slowing legitimate operations.                                                                                                           |
| Distributed Denial of Service (DDoS) | Attack coordinated from multiple sources, often via botnets (networks of compromised “zombie” systems). | Botnet Structure: Zombies receive commands from a central CnC server (IRC, DNS, HTTP, or HTTPS). Bots perform various malicious activities, such as logging keystrokes, relaying spam, and launching attacks. |
## Reflection and Amplification Attacks
![11](/Course-Notes/.assets/Pasted_image_20241113141119.png)
Metigation

| Command                    | Description                                                         | Default Setting                               |
| -------------------------- | ------------------------------------------------------------------- | --------------------------------------------- |
| `no ip directed-broadcast` | Drops broadcasts destined for the subnet attached to the interface. | Default since Cisco IOS Software Release 12.0 |
## Spoofing Attacks

| Spoofing Type                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| IP address spoofing             | Attackers use source IP addresses different from their real IP addresses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DNS spoofing                    | Hacker changes hostname to IP mapping by compromising a DNS server<br><br>Attacks spoofs responses from DNS server, after upon successful packet sniffing the attacker can guess the sequence numbers<br><br>The attacker sends false replies to the server by poisoning a DNS cache                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MAC address spoofing            | Attackers use MAC addresses that are not their own. MAC address spoofing is generally used to exploit weakness at Layer 2 of the network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Email Spoofing                  | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Application or service spoofing | One example is DHCP spoofing, which can be done with either the DHCP server or the DHCP client. To perform DHCP server spoofing, the attacker enables a rogue DHCP server on a network. When a victim host requests a DHCP configuration, the rogue DHCP server responds before the authentic DHCP server. The victim is assigned an attacker-defined IP configuration. From the client side, an attacker can spoof many DHCP client requests, specifying a unique MAC address per request. The DHCP server’s IP address pool may become exhausted, leading to a DoS against valid DHCP client requests. Another simple example of spoofing at the application layer is an email from an attacker which appears to have been sourced from a trusted email account. |
| Land attack                     | The attack is named for the name of the file, land.c, used for the original source code that is compiled into an attack tool. In a land attack, the attacker sends a TCP SYN request using the same IP address and port as both the source and destination IP address and port. The IP address and port combination that is used is that of the target system. The target system replies to itself and, if the system is vulnerable, the response leads to a system crash.                                                                                                                                                                                                                                                                                         |
## DHCP Attacks
![10](/Course-Notes/.assets/Pasted_image_20241113153845.png)

DHCP server spoofing attack process:

1. An attacker activates a malicious DHCP server on the attacker port.
2. The client broadcasts a DHCP configuration request.
3. The DHCP server of the attacker responds before the legitimate DHCP server can respond, assigning attacker-defined IP configuration information.
4. Host packets are redirected to the attacker address because it emulates the default gateway that it provided to the client.

##### **DHCP starvation:** 
A DHCP starvation attack works by the broadcasting of DHCP requests with spoofed MAC addresses. If enough requests are sent, the network attacker can exhaust the address space available to the DHCP servers in a time period. The network attacker can then set up a rogue DHCP server. However, the exhaustion of all the DHCP addresses is not required to introduce a rogue DHCP server.

Cisco switch features such as DHCP Snooping and IP Source Guard can be used to defend against DHCP attacks.
___
# [[IPS Technology and Rules]]

## Intrusion Detection and Prevention
IPS/IDS
![9](/Course-Notes/.assets/Pasted_image_20241114113745.png)
### Detection versus Prevention
![8](/Course-Notes/.assets/Pasted_image_20241114113941.png)
![7](/Course-Notes/.assets/Pasted_image_20241114113955.png)
### Detection Methods
![6](/Course-Notes/.assets/Pasted_image_20241114114306.png)

| Method                                 | Description                                                                                       | Pros                                         | Cons                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------- |
| Anomaly-based detection                | Learns normal network activity patterns and compares live traffic to the baseline.                | Identifies deviations from normal behaviour. | Can generate false alarms due to changing user workflows. |
| Signature-based (rule-based) detection | Analyzes live traffic using a database of IPS rules (signatures) to identify suspicious activity. | Recognizes attacks based on known patterns.  | Requires regular updates to stay effective.               |
### IPS Roles and Features
![5](/Course-Notes/.assets/Pasted_image_20241114114529.png)

| Feature                             | Description                                                                       |
| ----------------------------------- | --------------------------------------------------------------------------------- |
| Layer 2 to Layer 7 Traffic Analysis | Analyzes traffic controlling Layer 2 to Layer 3 mappings (ARP, DHCP).             |
| Protocol Verification               | Ensures packets follow correct protocol formats (IP, TCP, UDP, ICMP).             |
| Payload Analysis                    | Identifies suspicious activities and malware within packet payloads.              |
| Deployment Options                  | Standalone hardware or virtual appliance, or alongside NGFW and other appliances. |
| Alerting                            | Sends alerts for detected events, integrating with syslog, SNMP, or SIEM.         |
## Types of IPSs
![4](/Course-Notes/.assets/Pasted_image_20241114115129.png)

| Type                                        | Description                                                       | Functionality                                                                        |
| ------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| Network Intrusion Prevention System (NIPS)  | Monitors network traffic for malicious activity.                  | Can inspect traffic inline (active) or analyze traffic forwarded to it (passive).    |
| Wireless Intrusion Prevention System (WIPS) | Scans for rogue access points and unauthorized wireless networks. | Prevents unauthorized access and potential MITM or DoS attacks.                      |
| Host Intrusion Prevention System (HIPS)     | Installed on endpoints to protect against malware.                | Prevents viruses, worms, trojans, ransomware, spyware, adware, and fileless malware. |
## NIPS Placement Within the Network
NIPS must be implemented correctly 
![3](/Course-Notes/.assets/Pasted_image_20241114115509.png)

| Placement             | Description                                           | Pros                                 | Cons                                           |
| --------------------- | ----------------------------------------------------- | ------------------------------------ | ---------------------------------------------- |
| Internet Edge         | Inspects traffic to and from the internet.            | Blocks external threats.             | Does not inspect internal traffic.             |
| Data Center Perimeter | Protects the data center from specific threats.       | Tailored protection for data center. | May not cover broader network threats.         |
| Multiple IPSs         | Deploys multiple IPSs for different network segments. | Defense-in-depth approach.           | Requires careful configuration and management. |
![2](/Course-Notes/.assets/Pasted_image_20241114120332.png)

| IPS Placement     | Purpose                                   | Threat Protection                                                                   |
| ----------------- | ----------------------------------------- | ----------------------------------------------------------------------------------- |
| Network Perimeter | Protects the entire network               | Outside threats                                                                     |
| Data Center       | Protects resources within the data center | Internal and external threats, including malware proliferation and lateral movement |
# Common Threat Detection and Prevention Systems
## Snort

| Feature                                            | Description                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Launched                                           | 1998                                                                                                                                                                                                                                                                                                                                                     |
| Type                                               | Free and open-source IDS and IPS system                                                                                                                                                                                                                                                                                                                  |
| Acquisition                                        | Cisco acquired Sourcefire in 2013                                                                                                                                                                                                                                                                                                                        |
| Current Status                                     | Incorporated into multiple Cisco product lines                                                                                                                                                                                                                                                                                                           |
| Supported Platforms                                | Linux, Windows, or dedicated network appliances                                                                                                                                                                                                                                                                                                          |
| NIDS Mode                                          | Performs detection and analysis of network traffic, and can act as an IPS                                                                                                                                                                                                                                                                                |
| Rule-based System                                  | Uses predefined rules (signatures) for intrusion detection                                                                                                                                                                                                                                                                                               |
| Rule Sets                                          | Subscriber Ruleset (developed by Cisco Talos) and Community Ruleset                                                                                                                                                                                                                                                                                      |
| Opperation Mode                                    | Description                                                                                                                                                                                                                                                                                                                                              |
| **Sniffer**                                        | Reads the network data stream (captures packets) and displays the packet information on the console, behaving similarly to the TCPdump program.                                                                                                                                                                                                          |
| **Logger**                                         | Writes each captured packet to a separate file, similar to TCPdump used with the -w option. Writing output to a binary file is recommended for high-bandwidth networks, as it stores the data in a TCPdump format. This format allows the file to be viewed with packet analyzer tools, such as Wireshark.                                               |
| **Network Intrusion Detection System (NIDS) mode** | This is where Snort performs detection and analysis of network traffic and if configured, acts as an IPS. This is the most feature-rich mode but at the same time the most complex of all three, requiring a configuration file. The configuration file references the set of Snort rules, which are used to detect suspicious and malicious activities. |
### Building Blocks of Snort Rules
![1](/Course-Notes/.assets/Pasted_image_20241114141638.png)

| Section     | Description                                                                       |
| ----------- | --------------------------------------------------------------------------------- |
| Rule Header | Defines the “who and where” of a packet and the action to take.                   |
| Rule Body   | Contains rule options that form the core of the Snort intrusion detection engine. |
#### Rule Header:

| Rule Header             | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| Action                  | Specifies the action to be taken when a packet matches the rule. |
| Protocol                | Specifies the network protocol to be matched.                    |
| Source IP and Port      | Specifies the source IP address and port to be matched.          |
| Operator                | Specifies the direction of the traffic to be matched.            |
| Destination IP and Port | Specifies the destination IP address and port to be matched.     |
#### Rule Body:

| Rule Body      | Description                                                             | Example                                                                                                          |
| -------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| General        | Provide general information about the rule but do not affect detection. | msg: The message to display associated to the Snort rule; sid: The Snort ID; rev: The revision of the Snort rule |
| Payload        | Look for data within the packet payload.                                | content: Search for specific content in the packet payload                                                       |
| Non-payload    | Look for non-payload data.                                              | flow: Allows a rule to only be applied to certain directions of the traffic flow                                 |
| Post-detection | Rule-specific triggers that happen after the rule was matched.          | replace: An inline feature which causes Snort to replace the prior matching content with some given string       |

## Zeek

Passive network traffic analysis and a packet recorder. 
aggregates data into formatted log files. 
provides its own scripting language
3 main components:
	- Event Engine (Collects raw Data)
	- Policy Script Interpreter (interperpates events)
	- Event Handlers (Executes appropriate scripts)
Uses UID to track conversations
Creates details logs containing:
	- Source and destination IP addresses
	- Which protocol and application created the connection
	- When the conversation happened and how long it lasted 
	- Packet and data statistics
## Suricata

| Feature                | Description                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| Type                   | Free, open-source IDS/IPS                                                                |
| Protocol Support       | HTTP, DNS, TLS, SMB (over nonstandard ports)                                             |
| Inspection Level       | Packet-level (deep packet analysis)                                                      |
| Rule-based             | Yes, using signatures or rules                                                           |
| Rule Components        | Rule definition, header, action                                                          |
| Alert Format           | Timestamp, source and destination IPs, Suricata signature                                |
| Advanced Functionality | Lua scripts for detecting malicious activities                                           |
| Modes                  | Network security monitoring (NSM), Intrusion detection (IDS), Intrusion prevention (IPS) |
## Cisco IPS Solutions
**Cisco Secure Firewall Threat Defense - Key Features**

| Feature                    | Description                                                                                                                                                                                                                                                                                                          |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Security Intelligence (SI) | Acts as the first line of defense using Cisco Talos intelligence. Identifies and blocks known malicious IPs, URLs, and domain names automatically. Reduces Snort engine workload by dropping flagged traffic immediately.                                                                                            |
| URL Filtering              | Allows for blocking specific URLs or categories of websites. Useful for preventing access to inappropriate or harmful sites.                                                                                                                                                                                         |
| File and Malware Analysis  | Uses Cisco Secure Malware Analytics (formerly ThreatGRID) for sandboxed malware analysis. Supports both on-box and cloud-based analysis for enhanced security.                                                                                                                                                       |
| TLS/SSL Traffic Inspection | Can inspect encrypted web traffic to block old or insecure protocols (e.g., SSL) and weak cipher suites. Detects threats hidden within encrypted connections, like malware and data exfiltration. Supports TLS/SSL decryption for inbound and outbound traffic, acting as a proxy to inspect connections thoroughly. |
| Deployment Flexibility     | Available as a physical appliance or virtual machine. Compatible with virtualization platforms (VMware vSphere, KVM) and public cloud services (Microsoft Azure, AWS).                                                                                                                                               |

| Feature                      | Description                                                                |
| ---------------------------- | -------------------------------------------------------------------------- |
| Security Intelligence        | Up-to-date threat information for effective threat detection.              |
| URL Filtering                | Blocks access to malicious and inappropriate websites.                     |
| Malware Analysis             | Identifies and neutralizes malware threats in traffic.                     |
| Encrypted Traffic Inspection | Scans encrypted traffic for hidden threats without compromising privacy.   |
| Deployment Options           | Flexible deployment, including physical, virtual, and cloud-based options. |
Cisco Secure Firewall devices can be managed using:
- Cisco Secure Firewall Device Management (FDM), which is a single device manager
- Cisco Secure Firewall Management Center, which can manage multiple devices and can be implemented as a physical or virtual appliance    
- Cisco Defense Orchestrator, which is a cloud-based manager that can manage different types of devices such as Cisco Secure Firewall ASA, Cisco Secure Firewall Threat Defense, Cisco Meraki, Cisco Umbrella, and more.
- Cloud Delivered FMC

## Cisco Umbrella Cloud Delivered Firewall
Cisco Umbrella comprises many different security services, including:
- Secure Web Gateway (SWG)
- cloud access security broker
- DNS layer security
- cloud-delivered firewall (CDFW)
- data loss prevention
- threat Intelligence

| Component                         | Description                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Secure Web Gateway (SWG)          | Acts as an HTTP/HTTPS proxy. Inspects and filters web traffic based on domain or category (URL filtering).                                                                                                                                                                                                                                                                                 |
| DNS Layer Security                | Functions as an upstream DNS server. Blocks access to domains associated with malware, phishing, botnets, and other high-risk threats.                                                                                                                                                                                                                                                     |
| Cisco Distributed Firewall (CDFW) | Provides visibility and control over client-to-internet traffic. Supports rule-based blocking at Layers 3, 4 (IP, port, protocol), Layer 7 (application visibility and control), and IPS rules. Logs all activity and blocks traffic based on defined firewall policies. Traffic is forwarded to the CDFW through an IPsec tunnel between the network device and the Cisco Umbrella cloud. |

| Component                                                                                          | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Traffic Initialization                                                                             | LAN traffic reaches Cisco Umbrella via an IPsec tunnel from an on-premises device (router or firewall) to the Cisco cloud. |
| Traffic is encrypted over the internet to secure the connection.                                   | Traffic is encrypted over the internet to secure the connection.                                                           |
| Decryption and DNS Resolution                                                                      | Upon reaching Cisco Umbrella, the traffic is decrypted.                                                                    |
| DNS resolver checks the domain for malicious or restricted content per DNS policy.                 | DNS resolver checks the domain for malicious or restricted content per DNS policy.                                         |
| Approved traffic moves to the CDFW for further inspection.                                         | Approved traffic moves to the CDFW for further inspection.                                                                 |
| CDFW Filtering                                                                                     | CDFW blocks or allows traffic based on firewall policies.                                                                  |
| Permitted web traffic then proceeds to SWG for web-specific inspection.                            | Permitted web traffic then proceeds to SWG for web-specific inspection.                                                    |
| SWG Inspection (Web Traffic Only)                                                                  | SWG examines approved web traffic per the Web Policy.                                                                      |
| It decides to accept or drop traffic based on the content filter.                                  | It decides to accept or drop traffic based on the content filter.                                                          |
| Network Address Translation (NAT)                                                                  | Approved traffic is sent to NAT, which replaces the original source address with the Cisco Umbrella address.               |
| Ensures return traffic re-enters Cisco Umbrella for reverse inspection before reaching the source. | Ensures return traffic re-enters Cisco Umbrella for reverse inspection before reaching the source.                         |
| Non-Web Traffic Handling                                                                           | Non-web traffic allowed by CDFW bypasses SWG and proceeds directly to NAT processing.                                      |
# Summary
- Describe and differentiate between intrusion detection and intrusion prevention.
- Explain detection rules.
- Differentiate between rule-based and anomaly-based intrusion detection.
- Describe Snort, Zeek, and Suricata detection solutions.
- Describe the structuring of a Snort rule and rule elements.
- Describe how to mitigate a high-risk threat using Cisco Secure Firewall Threat Defense.
- List Cisco IPS solutions and describe their features.