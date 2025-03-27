
## Attack Surface - Sum of Vulnerabilities

![6](/Course-Notes/.assets/Pasted_image_20241113115837.png)

#### The **network** attack surface.
> All vulnerabilities that are related to ports, protocols, channels, devices (smart phones, laptops, routers, and firewalls), services, network applications (SaaS), and even firmware interfaces. 
- Some network protocols are inherently more insecure than others as they pass data over the network unencrypted. These protocols include Telnet, FTP, HTTP, and SMTP. Many Network File Systems, such as NFS and SMB, pass information over the network unencrypted. Remote memory dump services, such as netdump, also pass the contents of memory over the network unencrypted. 
- Memory dumps can contain passwords or, even worse, database entries and other sensitive information. Other services, such as `finger` and `rwhod`, reveal information about users of the system. Network printers are also the target of a wide array of attacks from hackers because the operating system driver, management tools, and the printer’s software make them vulnerable. Printers can be attacked via the web-based administrative interface, SMTP, FTP, and SNMP.

#### The **software** attack surface.
> Profile of all functions in any code that is running in a given system that is available to an unauthenticated user. 
- An attacker or a piece of malware can use various exploits to gain access and run code on the target machine. The software attack surface is calculated across many different kinds of code, including applications, email services, configurations, compliance policy, databases, executables, DLLs, web pages, mobile apps, device OS, and so on. 
- Unpatched software, such as Java, Adobe Reader, and Adobe Flash, also provide greater software attack surface because they are widely used. 

#### The **physical** attack surface. 
> The security vulnerabilities in a given system that are available to an attacker in the same location as the target. 
- The physical attack surface is exploitable through inside threats such as rogue employees, social engineering ploys, and intruders who are posing as service workers. 
- External threats include password retrieval from carelessly discarded hardware, passwords on sticky notes, and physical break-ins. Also, consider a scenario where an intruder steals or downloads the information from an entire drive and extracts the target data in the future.

#### The **social engineering** attack surface.
> Human psychology: the desire for something free, the susceptibility to distraction, or the desire to be liked or to be helpful. 
- A few examples of human social engineering attacks are fake calls to IT, where the attacker is posing as an employee to get a password; or media drops where an employee might find a flash drive in the parking lot, and when they use that device, they inadvertently execute automatic running code leading to a data breach. 
- Socially engineered Trojans provide another method of attack. An end user browses to a website that is usually trusted, which prompts the end user to run a Trojan. Most of the time the website is a legitimate, innocent victim that has been temporarily compromised by hackers. 
- Another very popular method is an APT attacker sends a very specific phishing campaign, which is known as spear-phishing, to multiple employees' email addresses. The phishing email contains a Trojan attachment, which at least one employee is tricked into running. After the initial execution and first computer takeover, an APT attacker can compromise an entire enterprise in a short time.

## Attack Vectors - Path to gaining access.

#### **Reconnaissance:** 
- The attacker attempts to gather information about targeted computers or networks that can be used as a preliminary step toward a further attack seeking to exploit the target system. For example, what operating system is on the target systems? Is there a firewall? Which ports are available? Which content management system (CMS) does the system run? There are also sources of information such as Facebook, Twitter, and Google that can be used to gather information about organizations or persons that are being targeted.

#### **Known vulnerabilities:** 
- The attacker finds weaknesses in hardware and software and then exploits those vulnerabilities.Several online resources publish information about vulnerabilities that have been discovered in different systems. Often, a proof-of-concept attack code will be provided with the vulnerability disclosure. Each platform has its own strengths and weakness. Once the target system is identified, it is simply a matter of trying out the different attacks for the targeted system to see which attacks work.

#### **SQL injection:** 
- This attack works by manipulating the SQL database queries that the web application sends. An application can be vulnerable if it does not sanitize user input properly, or uses untrusted parameter values in database queries without validation. According to research from U.S.-based cloud service provider Akamai in its _State of The Internet_ report, SQL injection attacks accounted for 65 percent of web-based attack vectors from November 2017 to March 2019. In its report, Akamai noted that “The growth of SQLi as an attack vector over the last two years should concern website owners. In the first quarter of 2017, SQLi accounted for 44% of application layer attacks. This actually represented a rather large drop from the previous baseline, which was historically slightly over 50%."

#### **Phishing:** 
- The attacker sends out spam email to thousands of recipients. The email contains a link to a malicious site that has been set up to look like, for instance, a regular bank’s site. When the user enters their credentials in the login form, it actually is captured by the malicious site and then used to impersonate that user on the real site. Spear phishing is another variation of the phishing attack, in which the attacker usually targets specific persons. The RSA breach in 2011, which resulted in unspecified data that are related to their SecurID product being stolen, started with a spear phishing attack.

#### **Advanced Persistent Threat:** 
- An advanced persistent threat (APT) is a covert cyber attack on a computer network where the attacker gains and maintains unauthorized access to the targeted network, and remains undetected for a significant period. Between infection and remediation, the hacker will often monitor, intercept, and exfiltrate sensitive data from the network. APTs intend to exfiltrate or steal data, and not cause a network outage, cause a denial of service, or infect systems with malware. APTs often use social engineering tactics or exploit software vulnerabilities, and usually target organizations with high value information.

#### **Malware:** 
- Short for malicious software, malware may be computer viruses, worms, Trojan horses, dishonest spyware, and malicious rootkits.

#### **Weak authentication:** 
- These exploits occur because of poorly designed or poorly implemented authentication mechanisms. Weak authentication usually means one or more of the following: weak, guessable passwords are allowed, no lockout enforcement after a specific number of invalid login attempts, or the password reset methods are not secure.

## Security Risks and Challenges

As stated in a previous Cisco Annual Security Report, Cisco conducted a study to assess IT decision-makers’ perceptions of their security risks and challenges. Sixty-eight percent of the respondents to the study identified malware as the top external security challenge that their organization faces. Phishing and APTs rounded out the top three responses: 54 percent and 43 percent, respectively.

![5](/Course-Notes/.assets/Pasted_image_20241113115914.png)

# Network 
## Reconnaissance Attacks

>An attempt to learn more about the intended victim before attempting a more intrusive attack.
- IP addresses, sub-domains, and related information on a target network
- Accessible UDP and TCP ports on target systems
- The operating system on target systems

Four main subcategories or methods for gathering network data:

- **Packet sniffers:** Packet sniffing, or packet analysis, is the process of capturing any data that are passed over the local network and looking for any information that may be useful to an attacker. The packet sniffer may be either a software program or a piece of hardware with software installed in it that captures traffic that is sent over the network, which is then decoded and analyzed by the sniffer. Tools, such as Wireshark, Ettercap, or NetworkMiner, give anyone the ability to sniff network traffic with a little practice or training.

- **Ping sweeps:** A ping sweep is another kind of network probe. In a ping sweep, the attacker sends a set of ICMP echo packets to a network of machines, usually specified as a range of IP addresses, and sees which ones respond. The idea is to determine which machines are alive and which aren't. Once the attacker knows which machines are alive, he can focus on which machines to attack and work from there. The `fping` command is one of the many tools that can be used to conduct ping sweeps.

- **Port scans:** A port scanner is a software program that surveys a host network for open ports. As ports are associated with applications, the attacker can use the port and application information to determine a way to attack the network. The attacker can then plan an attack on any vulnerable service that they find. Examples of insecure services, protocols, or ports include but are not limited to port 21 (FTP), port 23 (Telnet), port 110 (POP3), 143 (IMAP), and port 161 (SNMPv1 and SNMPv2) because protocols using these ports do not provide authenticity, integrity, and confidentiality. NMAP is one of the many tools that can be used for conducting port scans.

- **Information queries:** Information queries can be sent via the Internet to resolve hostnames from IP addresses or vice versa. One of the most commonly used queries is the `nslookup` command. You can use `nslookup` by opening a Windows or Linux command prompt window on your computer and entering the `nslookup` command, followed by the IP address or hostname that you are attempting to resolve.

### Passive and Active Reconnaissance

#### Passive
Initially, an attacker attempts to gain information about targeted computers or networks that can be used as a preliminary step toward a further attack seeking to exploit the target system. A reconnaissance attack can be active or passive.

![4](/Course-Notes/.assets/Pasted_image_20241113124843.png)

#### Whois, nslookup & dig
Attackers passively start using standard networking command-line tools such as `dig`(Lin) , `nslookup`, and `whois`(Win&Lin) to gather public information about a target network from DNS registries.

#### Shodan Search Engine
Another innocuous tool is the Shodan search engine with metadata filter capabilities that can help an attacker identify a specific device, such as a computer, router, and server. For example, an attacker can search for a specific system, such as a Cisco 3945 router, running a certain version of the software, and then explore further vulnerabilities.

### Active
Ping sweeps, traceroutes, port scans, or operating system fingerprinting to actually send packets to discover the target systems. One of the tools that can be used is `traceroute` to find out the IP addresses of routers and firewalls that protect victim hosts. Ping sweeps of the addresses can present a picture of the live hosts in a particular environment. After a list of live hosts is generated, the attacker can probe further by running port scans on the live hosts. The attacker can use this information to determine the easiest way to exploit a vulnerability.

## Access Attacks

Many attacks can lead to a system being compromised, and allow the attacker to gain unauthorized access to the system. The following are some prominent types of attacks:

- **Password attack** is typically used to obtain system access. When access is obtained, the attacker is able to read, modify, or delete data, and add, modify, or remove network resources. For example, tools like "John the ripper," and "Cain and Abel" are password cracker tools.
- **Spoofing/masquerading** attack is a situation in which one person or program successfully masquerades as another by falsifying data and gaining illegitimate access.    
- **Session hijacking** is an attack in which the session established by the client to the server is taken over by a malicious person or process.
- **Malware** is used to infect the victim's system with malicious software.

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

Examples of OSI layer MITM attacks include the following:

- **Physical layer:** Tap someone's physical connection, and send all packets to the MITM
    
- **Data link layer:** Use ARP poisoning to cause victims to send all their packets to the MITM
    
- **Network layer:** Manipulate packet routing to route all the packets to the MITM
    
- **Session layer:** The SSL/TLS MITM de-crypts, examines, then re-encrypts the HTTP over SSL/TLS traffic. For this attack to work, the victim's web browser must trust the certificate that is presented by the SSL/TLS MITM which can be caused by first injecting some malware into the victim's web browser.
    
- **Application layer:** Man-in-the-browser attack. Like most attacks, man-in-the-browser begins with a malware infection. The malware injects itself into the victim's web browser, and waits in stealth mode until the user visits a specific website. At that point, the malware goes into action, tricking the user into entering sensitive information on the web page. Different types of malware typically have different attack targets hardcoded into its code. For example, Zeus generally targets banking sites. When the malware is activated, it may manipulate the web page being loaded by injecting extra fields into the web page to collect sensitive pieces of information, or act as a keylogger to intercept the data. The idea is that no matter how careful you are about scrutinizing URLs and ensuring that you go to the correct website, the web browser cannot be trusted because it has been compromised.
    
- **ARP poisoning:** An ARP-based MITM attack is achieved when an attacker poisons the ARP cache of two devices with the MAC address of the attacker's network interface card (NIC). Once the ARP caches have been successfully poisoned, each victim device sends all its packets to the attacker when communicating to the other device and puts the attacker in the middle of the communications path between the two victim devices. It allows an attacker to easily monitor all communication between victim devices. The intent is to intercept and view the information being passed between the two victim devices and potentially introduce sessions and traffic between the two victim devices.    

![3](/Course-Notes/.assets/Pasted_image_20241113132114.png)
    The figure illustrates an ARP-based MITM attack. The attacker poisons the ARP caches of hosts A and B so that each host will send all its packets to the attacker when communicating to the other host.

An MITM attack can be passive or active. In passive attacks, attackers steal confidential information. In active attacks, attackers modify data in transit or inject data of their own. ARP cache poisoning attacks often target a host and the host’s default gateway. ARP cache poisoning puts the attacker as a MITM between the host and all other systems outside of the local subnet.
    
- **ICMP**-**based MITM attack:** An ICMP MITM attack is accomplished by spoofing an ICMP redirect message to any router that is in the path between the victim client and server. An ICMP redirect message is typically used to notify routers of a better route; however, it can be abused to effectively route the victim's traffic through an attacker-controlled router. The threat of this attack is mitigated by routers that have static routes and routers that do not accept/process ICMP redirect packets.
    
- **DNS**-**based MITM attack:** DNS spoofing is an MITM technique that is used to supply false DNS information to a host so that when they attempt to browse, for example, https://www.xyzbank.com at the IP address XXX.XX.XX.XX, the host is actually sent to an imposter https://www.xyzbank.com that is residing at IP address YYY.YY.YY.YY, which an attacker has created to steal online banking credentials and account information from unsuspecting users.
    
- **DHCP**-**based MITM attack:** Similar to the DNS attack, DHCP server queries and responses are intercepted. This interception helps the attacker gain complete knowledge of the network, such as hostnames, MAC addresses, IP addresses, and the DNS servers. This information is further used to plant advanced attacks to steal the information. An attacker can initiate a DoS attack on a real DHCP server to keep it busy, and meanwhile spoof and respond to the DHCP host queries by itself.


#### Securing Against MITM

- ﻿﻿VPN
- ﻿﻿Digital Certificates for Authentication
- ﻿﻿Strong Passwords and Multifactor Authentication
- ﻿﻿Dynamic ARP Inspection
- ﻿﻿IP Spoofing Detection
- ﻿﻿DHCP Snooping

## DoS & DDoS

### **TCP SYN Flood Attack (DoS)**

• Exploits TCP three-way handshake by sending SYN packets with fake source addresses.
• Victim’s connection table fills with incomplete connections, denying legitimate TCP services.
• Hard to trace due to source IP spoofing.

### **Ping of Death (DoS)**

• Uses oversized packet fragments to crash systems by exceeding IP’s maximum packet size limit.
• Exploits vulnerabilities in IP processing, with variations targeting protocols like SNMP, syslog, DNS.
• Largely mitigated in modern systems, especially IPv4; IPv6 versions persist.

### **ICMP and UDP Floods (DoS)**

• **ICMP Flood**: Overloads network with echo requests to slow down services.
• **UDP Flood**: Sends numerous UDP packets, draining target resources and slowing legitimate operations.

### **Distributed Denial of Service (DDoS)**

• Attack coordinated from multiple sources, often via botnets (networks of compromised “zombie” systems).
• **Botnet Structure**: Zombies receive commands from a central CnC server (IRC, DNS, HTTP, or HTTPS).
• Bots perform various malicious activities, such as logging keystrokes, relaying spam, and launching attacks.

### **DDoS Trends and Case Studies**

• **Increasing Threat**: Rising in volume and impact; affects ISPs and industries like finance and energy.

• **Notable Attacks**:

• _Operation Ababil_: Targeted financial institutions, often politically motivated.
• _Imperva Attack (2019)_: 13-day application layer DDoS with 292,000 RPS targeting a streaming service.
• _Spamhaus Attack_: Retaliatory DDoS targeting Spamhaus due to its anti-spam activities.

• **Cybercriminal Trends**: Increased expertise in compromising hosting servers boosts attack capacity.

• **DarkSeoul Attack (2013)**:
	• Involved wiper malware, potentially for cyberwarfare or financial gain.
	• Targeted South Korean banks and media, likely concealing financial theft under DDoS cover.
	• Tied to evolving cybercrime methods aiming at bank account fraud while disrupting networks.

**Summary**

Denial-of-service (DoS) and distributed denial-of-service (DDoS) attacks use network traffic floods and malware to disrupt services, often concealing other malicious activities. With advancements in DDoS techniques and botnet sophistication, these attacks pose significant threats to industries, and large-scale incidents highlight their financial and operational risks.

## Reflection and Amplification Attacks

### Smurf attack.
Attacker sends numerous ICMP echo-request packets to the broadcast address of a large network. These packets contain the victim's address as the source IP address. Every host that belongs to the large network responds by sending ICMP echo-reply packets to the victim. The victim is flooded with unsolicited ICMP echo-reply packets.
 
Note the differentials in bandwidth of the Internet connections. The attacker has a very small, 56 kbps dial-up connection. The target has a much larger T1 connection (1.544 Mbps). The reflector network has an even larger DS-3 connection (45 Mbps). The small 56K stream of echo requests with the spoofed source address of victim 10.1.1.5 is sent to the broadcast addresses of the large network. As a result, thousands of echo replies are sent to 10.1.1.5 for each spoofed echo, and the target T1 is fully consume
![2](/Course-Notes/.assets/Pasted_image_20241113141119.png)Smurf attacks can easily be mitigated on a Cisco IOS device by using the `no ip directed-broadcast` interface configuration command, which has been the default setting in Cisco IOS Software since Release 12.0. With the `no ip directed-broadcast` command configured for an interface, broadcasts destined for the subnet to which that interface is attached will be dropped, rather than being broadcast.

## Spoofing Attacks

##### **IP address spoofing:** 
- IP address spoofing is the most common type of spoofing. To perform IP address spoofing, attackers use source IP addresses that are different than their real IP addresses.
	**Mitigating IP spoofing**
	- Access control list to restrict private IP's on personal downstream interface
	- ﻿﻿RFC 1918
	- ﻿﻿Bogon addresses

##### **DNS spoofing**:
- ﻿﻿Hacker changes hostname to IP mapping by compromising a DNS server
- ﻿﻿Attacks spoofs responses from DNS server, after upon successful packet sniffing the attacker can guess the sequence numbers
- ﻿﻿The attacker sends false replies to the server by poisoning a DNS cache
	Mitigating DNS Spoofing
	- Use DNSSEC; adds digital signatures and security certificates for authentication

##### **MAC address spoofing:** 
- To perform MAC address spoofing, attackers use MAC addresses that are not their own. MAC address spoofing is generally used to exploit weakness at Layer 2 of the network.

##### Email Spoofing:
Protecting Against Email Spoofing
	- ﻿﻿Spam filtering
	- ﻿﻿Cross check email headers to see where it came from and what it consists of
	- ﻿﻿Do not click unknown links or download attachments unless you are aware of the sender
	- ﻿﻿Digital certificates, strong passwords, email signatures adds extra protection

##### **Application or service spoofing:** 
- One example is DHCP spoofing, which can be done with either the DHCP server or the DHCP client. To perform DHCP server spoofing, the attacker enables a rogue DHCP server on a network. When a victim host requests a DHCP configuration, the rogue DHCP server responds before the authentic DHCP server. The victim is assigned an attacker-defined IP configuration. From the client side, an attacker can spoof many DHCP client requests, specifying a unique MAC address per request. The DHCP server's IP address pool may become exhausted, leading to a DoS against valid DHCP client requests. Another simple example of spoofing at the application layer is an email from an attacker which appears to have been sourced from a trusted email account.

##### **Land attack.** 
The attack is named for the name of the file, land.c, used for the original source code that is compiled into an attack tool. In a land attack, the attacker sends a TCP SYN request using the same IP address and port as both the source and destination IP address and port. The IP address and port combination that is used is that of the target system. The target system replies to itself and, if the system is vulnerable, the response leads to a system crash.

## DHCP Attacks

**DHCP server spoofing:** The attacker runs DHCP server software and replies to DHCP requests from legitimate clients. As a rogue DHCP server, the attacker can cause a DoS by providing invalid IP information. The attacker can also perform confidentiality or integrity breaches via a man-in-the-middle attack. The attacker can assign itself as the default gateway or DNS server in the DHCP replies, later intercepting IP communications from the configured hosts to the rest of the network.

![1](/Course-Notes/.assets/Pasted_image_20241113153845.png)

The following is the DHCP server spoofing attack process:

1. An attacker activates a malicious DHCP server on the attacker port.
2. The client broadcasts a DHCP configuration request.
3. The DHCP server of the attacker responds before the legitimate DHCP server can respond, assigning attacker-defined IP configuration information.
4. Host packets are redirected to the attacker address because it emulates the default gateway that it provided to the client.

- **DHCP starvation:** A DHCP starvation attack works by the broadcasting of DHCP requests with spoofed MAC addresses. If enough requests are sent, the network attacker can exhaust the address space available to the DHCP servers in a time period. The network attacker can then set up a rogue DHCP server. However, the exhaustion of all the DHCP addresses is not required to introduce a rogue DHCP server.

Cisco switch features such as DHCP Snooping and IP Source Guard can be used to defend against DHCP attacks.