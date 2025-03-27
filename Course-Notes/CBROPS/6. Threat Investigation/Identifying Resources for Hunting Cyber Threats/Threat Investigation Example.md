— China Chopper Remote Access Trojan
# [[Quick Reference]]

Key Features

|Feature|Description|
|---|---|
|Command and Control|Allows attackers to conduct scans and brute force attacks on the infected server.|
|File Upload/Download|Attackers can upload additional malware or download sensitive data from the compromised server.|
|Language Support|Web shells can be written in various languages, including PHP, ASP, Perl, and Python.|
|Small Size|The web shell application is typically under 4KB, making it difficult to detect.|
 
Key Investigation Steps

- **Alert**: Initial detection of suspicious activity, often triggered by specific commands like 'id' on UNIX systems.
- **Detect**: Investigate HTTP activities between the attacker’s client and the web shell to identify queries and commands.
- **Confirm**: Verify the existence of the web shell on the compromised server and assess the extent of the attack.
- **Remediate**: Implement actions to neutralize the compromise, often involving re-imaging the affected system.
- **Resolve**: Monitor for further signs of compromise and ensure that remediation steps have been completed.

Key Tools

- **Wireshark**: A network protocol analyzer used to capture and analyze HTTP traffic between the attacker’s client and the web shell.
- **Snort**: An intrusion detection system that can trigger alerts based on specific rules related to suspicious commands and traffic.
- **Bro**: A network analysis framework used to log and analyze network traffic, aiding in the investigation of security events.

Key Recommendations

- **Re-image Compromised Systems**: The best course of action to ensure that the compromise has been neutralized.
- **Monitor for Further Compromise**: Continuous monitoring is essential to detect any signs of re-infection or further attacks.
- **Coordinate with Responsible Departments**: Senior analysts should work with the departments responsible for the compromised systems to ensure proper remediation.

Facts to Memorize

- China Chopper RAT is a widely used backdoor for remote access.
- The caidao.exe client is the attacker's interface for China Chopper.
- Common web shell languages include PHP, ASP, Perl, Ruby, Python, and UNIX shell scripts.
- The X-Forwarded-For HTTP header is used to identify the originating IP address of a client.
- The id command is commonly used on UNIX systems to check current process privileges.

Reference Information

- Snort rules can be used to detect China Chopper traffic.
- Wireshark can analyze HTTP traffic to reveal suspicious activities.
- Bro logs can be queried for event correlation during investigations.

Concept Comparisons

|Concept|Description|Key Differences|
|---|---|---|
|Backdoor|An undocumented way to access a system, bypassing normal authentication.|Can be placed by original programmers or through system compromises.|
|Web Shell|A script that allows remote access to a web server.|Can be written in various languages and delivered through exploits or weaknesses.|
|Command and Control (C2)|A method for attackers to communicate with compromised systems.|Often involves specific protocols and can be encrypted, complicating detection.|

Problem-Solving Steps

1. **Alert Detection**: Monitor for unusual network activity or specific commands that trigger alerts (e.g., id command).
2. **Traffic Analysis**: Use tools like Wireshark to analyze HTTP traffic and identify suspicious requests.
3. **Event Correlation**: Check Bro logs for related events to confirm the nature of the security incident.
4. **Compromise Confirmation**: Access the compromised server to locate and inspect the web shell file (e.g., webshell.php).
5. **Remediation Recommendation**: Suggest actions such as re-imaging the system to ensure the threat is neutralized.
6. **Resolution Monitoring**: After remediation, continue monitoring for any signs of further compromise.

# Overview of Backdoors and Remote Access Trojans

### Definition of Backdoors

- A backdoor is an undocumented method for bypassing normal authentication mechanisms to access a system.
- Backdoors can be intentionally created by developers or introduced through system compromises, such as malware.
- They allow attackers to maintain persistent access to compromised systems, facilitating further exploitation.

### Introduction to China Chopper RAT

- China Chopper is a widely used Remote Access Trojan (RAT) that enables attackers to remotely control compromised web servers.
- It consists of two main components: the attacker's client interface (caidao.exe) and the web shell file deployed on the compromised server.
- The primary goal of China Chopper is to steal sensitive data, including account credentials and financial information.

### Features of China Chopper

- Command and Control (C2) capabilities allow attackers to scan for vulnerabilities and execute brute force attacks.
- Attackers can upload or download files, including additional malware, to and from the infected system.
- The web shell can be written in various programming languages, with PHP and ASP being the most common.

![11](/Course-Notes/.assets/Pasted_image_20241130163301.png)
# Threat Investigation Process

![10](/Course-Notes/.assets/Pasted_image_20241130163312.png)
### Alert

- Initial connections to the web shell may not trigger alerts unless specific detection rules are in place.
- Analysts may rely on monitoring or specific commands that generate alerts, such as the UNIX 'id' command.
- Snort rules can be configured to detect plaintext outputs of commands traversing the network.

![9](/Course-Notes/.assets/Pasted_image_20241130163341.png)
![8](/Course-Notes/.assets/Pasted_image_20241130163349.png)

### Confirming the Security Event

- Investigate HTTP activities between caidao.exe and the web shell to identify queried web pages.
- Tools like Wireshark can be used to analyze captured HTTP traffic and follow TCP streams for detailed insights.
- The X-Forwarded-For header can reveal the attacker's spoofed IP address, indicating potential obfuscation tactics.

The security event has occurred. Investigate HTTP activities between the caidao.exe client and the web shell to determine which web page was queried. Wireshark can capture HTTP traffic and reveal the HTTP session by following the TCP stream.

![7](/Course-Notes/.assets/Pasted_image_20241130163425.png)
![6](/Course-Notes/.assets/Pasted_image_20241130163433.png)
![5](/Course-Notes/.assets/Pasted_image_20241130163436.png)
### Correlating Event Data

- Higher-tier analysts can use tools like ELSA to correlate events and confirm the nature of the security incident.
- Searching through Bro logs can provide additional context and confirm HTTP transactions between the client and web shell.
- Correlation of data helps in establishing a timeline and understanding the attack vector.

![4](/Course-Notes/.assets/Pasted_image_20241130163730.png)
![3](/Course-Notes/.assets/Pasted_image_20241130163736.png)

- Web Server Compromise Confirmation: The analyst needs to confirm if the 192.168.233.129 web server is compromised.
- Webshell Location and Analysis: The analyst should locate the webshell.php file on the web server and analyze its contents to understand the attacker’s actions.
- Initial Vector Identification: The analyst should determine the initial vector that allowed the attacker to place the webshell.php script on the web server.

![2](/Course-Notes/.assets/Pasted_image_20241130163841.png)

The figure below shows the webshell.php file in the web server root directory was created in 2016-11-10, whereas the index.php file was created on 2013-12-28.

![1](/Course-Notes/.assets/Pasted_image_20241130163853.png)
# Remediation and Resolution

### Confirming Compromise

- Analysts should access the compromised web server to locate and inspect the web shell file (e.g., webshell.php).
- Examination of the file's creation date and contents can provide insights into the attacker's actions and methods of entry.
- Understanding the initial vector of compromise is crucial for preventing future incidents.

### Remediation Actions

- Remediation may involve formatting and re-imaging the compromised system to ensure complete neutralization of the threat.
- The choice of remediation steps depends on the criticality of the systems and organizational policies.
- Continuous monitoring for signs of further compromise is essential post-remediation.

### Incident Resolution

- The incident is considered resolved once the recommended remediation steps are implemented and verified.
- Coordination with the responsible department is necessary to ensure comprehensive recovery and security.
- Senior analysts typically oversee the resolution process to ensure adherence to security protocols.

# Additional Resources

### Blogs and Feeds for Security Analysts
- [http://blogs.cisco.com/security/](http://blogs.cisco.com/security/)
- [http://malware-traffic-analysis.net/](http://malware-traffic-analysis.net/)
- [http://malware.dontneedcoffee.com/](http://malware.dontneedcoffee.com/)
- [http://myonlinesecurity.co.uk/](http://myonlinesecurity.co.uk/)
- [http://krebsonsecurity.com/](http://krebsonsecurity.com/)
- [http://blog.dynamoo.com/](http://blog.dynamoo.com/)
- [http://sanesecurity.blogspot.co.uk/](http://sanesecurity.blogspot.co.uk/)
- [http://blog.0x3a.com/](http://blog.0x3a.com/)
- [http://blog.trendmicro.com/trendlabs-security-intelligence/](http://blog.trendmicro.com/trendlabs-security-intelligence/)
- [https://techhelplist.com/index.php/spam-list](https://techhelplist.com/index.php/spam-list)
- [https://www.virustotal.com/en/community/](https://www.virustotal.com/en/community/)
- [http://blog.didierstevens.com/](http://blog.didierstevens.com/)
- [http://www.securiteam.com](http://www.securiteam.com/)
- [http://isc.sans.edu](http://isc.sans.edu/)
- [http://www.darknet.org.uk/](http://www.darknet.org.uk/)
- [http://www.newsnow.co.uk/h/Technology/Security](http://www.newsnow.co.uk/h/Technology/Security)
- [https://threatcrowd.org](https://threatcrowd.org/)
