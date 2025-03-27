### Characteristics of Beaconing Traffic

- Beaconing traffic is characterized by periodic message exchanges that create repetitive traffic patterns, making it easier to identify.
- The payload data in beacon messages is typically small and consistent, which helps in distinguishing between benign and malicious traffic.
- False positives are a significant challenge in detecting beaconing, as many legitimate network protocols exhibit similar periodic behavior.
- Common protocols like NTP, OSPF, and BGP can generate false positives due to their inherent beaconing characteristics.
- Applications such as stock trading, email clients, and social media platforms also engage in periodic communication, mimicking beaconing behavior.
- Adversaries often disguise malicious beaconing within these common protocols to evade detection by security devices.

### Challenges in Detecting Beaconing

- Detecting beaconing traffic can be complex due to the prevalence of false positives, which require thorough analysis to confirm legitimacy.
- Many network protocols have built-in periodic communication, complicating the identification of malicious activity.
- Security analysts must differentiate between benign and malicious beaconing by understanding the context and behavior of the traffic.
- False positives can lead to alert fatigue, where analysts may overlook genuine threats due to the volume of benign alerts.
- Continuous monitoring and analysis are essential to improve detection accuracy and reduce false positives.
- Familiarity with both benign and malicious use cases enhances the efficiency of SOC analysts in identifying threats.

# Benign Beaconing Use Cases

### Network Time Protocol (NTP)

- NTP is a widely used protocol for synchronizing the clocks of networked devices, ensuring accurate timekeeping across systems.
- It operates on a client-server model, where clients request the current time from an NTP server at regular intervals, typically between 15 to 60 minutes.
- The data exchanged during NTP communication is fixed in size, making it easy for analysts to recognize as benign.
- NTP uses UDP port 123, which is commonly allowed through firewalls, further complicating detection efforts.
- The consistent nature of NTP traffic helps SOC analysts quickly categorize it as benign, reducing false positive alerts.
- Understanding NTP behavior is crucial for analysts to differentiate it from potential malicious beaconing.

![9](/Course-Notes/.assets/Pasted_image_20241128145646.png)
### Microsoft Update Services

- Microsoft devices regularly check for updates to maintain performance and security, generating periodic beaconing-like traffic.
- Updates can include critical patches, which are applied immediately, or less severe updates that follow a defined schedule.
- The amount of data exchanged during updates varies based on the type of update, from small files to larger software components.
- Windows Update Orchestrator manages update requests, sending periodic messages to the WSUS to avoid overwhelming the server.
- Analysts must recognize this behavior to filter out benign traffic when monitoring for malicious activity.
- Regular updates are essential for maintaining the security posture of devices in a network.

![8](/Course-Notes/.assets/Pasted_image_20241128145754.png)
# Additional Benign Beaconing Examples

### Security Device Updates

- Network and endpoint security devices perform regular updates to maintain their effectiveness against threats.
- These updates can include software patches, IPS signature updates, and threat intelligence feeds, generating beaconing-like traffic.
- The frequency of updates is often determined by the criticality of the information being updated, with more critical updates occurring more frequently.
- Analysts should filter out this regular update traffic to focus on identifying genuine threats.
- Scheduling updates during low network usage periods can optimize performance and reduce bandwidth consumption.
- Understanding the update behavior of security devices is vital for accurate threat detection.

### File Synchronization

- File synchronization applications, such as OneDrive and Dropbox, use periodic polling to check for changes in files across different locations.
- This polling behavior can resemble beaconing, as it involves regular communication to ensure data consistency.
- Efficient file synchronization minimizes bandwidth usage while ensuring timely updates across user devices.
- The computing power required for polling can be significant compared to push-based synchronization methods.
- Analysts must be aware of file sync behaviors to distinguish them from potential malicious beaconing activities.
- Recognizing the characteristics of file synchronization helps in reducing false positives in network traffic analysis.

![7](/Course-Notes/.assets/Pasted_image_20241128145954.png)
# File Synchronization Systems

### Polling Mechanism

- File synchronization systems utilize polling to check for changes at predetermined intervals, which can be seen as a form of beaconing.
- Polling is resource-intensive compared to push-based synchronization, requiring significant computing power.
- The periodic nature of polling helps reduce the time taken for file uploads and downloads, optimizing bandwidth usage.
- Example: A file synchronization system that checks for updates every 5 minutes versus a push system that updates in real-time.

### Licensing Management with Cisco Secure Firewall

- Cisco Secure Firewall Management Center (formerly Cisco Firepower Management Center) manages multiple Cisco Secure Firewall devices.
- It aggregates network traffic information and performance data, providing centralized monitoring and management.
- Licensing is managed through periodic communication with the Cisco Smart Software Manager (SSM) portal, requiring registration with the License Authority.
- The default reporting interval for license usage is every 15 minutes, with a 30-day authorization reporting interval.

# Investigating and Hunting Malicious Beaconing

### Characteristics of Beaconing

- Beaconing traffic has unique timing and packet size traits that differentiate it from normal network traffic.
- Analysts must identify and filter out legitimate traffic to focus on potential threats, reducing data for analysis.
- The concept of 'jitter' is introduced, where adversaries randomize beacon intervals to evade detection, complicating the detection process.

![6](/Course-Notes/.assets/Pasted_image_20241128150150.png)
### Evasion Techniques

- Adversaries employ various techniques to hide beaconing, such as changing beacon intervals during idle and active phases of an attack.
- Prolonging the interval between beacons can help avoid detection during threat-hunting exercises, as analysts typically review logs over limited periods.
- The absence of a fixed formula for beaconing intervals makes detection challenging, as adversaries can set intervals to suit their objectives.

![5](/Course-Notes/.assets/Pasted_image_20241128150246.png)

![4](/Course-Notes/.assets/Pasted_image_20241128150520.png)

# Real-World Examples and Case Studies

### Case Study: Cobalt Strike in Myanmar

- In September 2021, Cisco Talos uncovered a campaign using Cobalt Strike beacons deployed via a Meterpreter stager.
- Cobalt Strike is a tool for adversary simulation, featuring a flexible C2 server and a post-exploitation agent called Beacon.
- The attack utilized domain fronting, leveraging a legitimate domain owned by the Myanmar government to conceal malicious activities.

### DNS Evasion Techniques

- Adversaries use Domain Generation Algorithms (DGA) to create numerous C2 server domain names, complicating detection efforts.
- The DNS-based fast flux technique allows rapid changes in the mapping of a C2 server’s domain name to multiple IP addresses, making IP-based detection ineffective.
- Mitigation strategies for DNS fast fluxing include requesting domain registrars to disable malicious domains, though this is often met with resistance.

# Overview of Cobalt Strike and Adversary Simulation
%%[[Complete Study]] [[Overview.pdf]] [[Background Information.pdf]]%%
### Introduction to Cobalt Strike

- Cobalt Strike is a commercial tool designed for adversary simulation and red team operations, allowing security professionals to mimic real-world attacks.
- It features a customizable Command and Control (C2) server and a post-exploitation agent known as Beacon, which facilitates covert communication.
- The software is widely used for penetration testing and assessing the security posture of organizations.

![3](/Course-Notes/.assets/Pasted_image_20241128150732.png)
### Domain Fronting Technique

- Domain fronting is a method used by threat actors to mask malicious activities by routing traffic through legitimate domains.
- In the Myanmar attack, the adversary utilized a domain owned by the Myanmar government to conceal their C2 server.
- This technique exploits the trust associated with high-reputation domains to bypass security controls that monitor for suspicious activity.

### Beaconing Mechanism

- The Cobalt Strike beacon is executed on a victim's system, generating traffic based on an embedded configuration file.
- The configuration file contains critical information such as the C2 server's domain name and HTTP request parameters.
- The beaconing process involves periodic communication with the C2 server, which can be difficult to detect due to its use of legitimate domains.

# Detection Techniques for Beaconing

### Cisco Secure Firewall

- Cisco Secure Firewall is equipped to detect botnet beacons by monitoring traffic between inside and outside zones.
- It utilizes the Cisco Secure IPS Snort engine to identify known vulnerabilities and suspicious activities.
- The Security Intelligence events page allows SOC analysts to pinpoint compromised hosts and filter by the BOT keyword for quick identification.

![2](/Course-Notes/.assets/Pasted_image_20241128153530.png)
### Cisco Secure Network Analytics

- This tool provides comprehensive visibility and analysis of network traffic, leveraging telemetry from existing infrastructure.
- It employs advanced behavioral analytics to establish a baseline of normal activity and detect anomalies.
- The system correlates multiple security events to identify potential attacks and affected devices, enhancing threat detection capabilities.

![1](/Course-Notes/.assets/Pasted_image_20241128153546.png)
### Open-Source Tools for Beacon Detection

- ==RITA== 
	- ==Functionality==: An open-source framework that computes statistical relations for connection intervals and session sizes, aiding in C2 detection.
	- ==Beaconing Detection==: RITA features dedicated beaconing filters that assign a beacon score (0.000 to 1) to each connection, indicating the probability of beaconing communication.
		- ==DNS-based C2 Tunnel Detection==

- **==Flare==** 
	- Integrates with Elasticsearch and Suricata 
	- ==Purpose==: Identify C2 beaconing by analyzing Elasticsearch flow data.
	- ==Components==: Written in Python, utilizes Elasticsearch and Suricata.
	- ==Suricata’s Functionality==: Combines IDS, IPS, NSM, and PCAP processing for threat detection.

# Mitigation Strategies Against C2 Beaconing

### Early Detection and Response

- Prompt detection of beaconing activity is crucial to prevent threat actors from achieving their objectives.
- Analysts should utilize automated tools to identify patterns in beacon communications and respond accordingly.
- Implementing security information and event management (SIEM) and security orchestration, automation, and response (SOAR) platforms can enhance detection capabilities.

### Incident Response Procedures

- Upon detecting a beaconing device, immediate actions should include removing unapproved applications and stopping suspicious processes.
- Quarantine the infected device to prevent further network communication and potential spread of malware.
- Establish firewall rules to block traffic to and from suspicious C2 servers, and apply the principle of least privilege to limit damage.

### Threat Intelligence and Continuous Improvement

- Subscribing to threat intelligence sources like Cisco Talos and CISA can aid in threat attribution and proactive defence.
- Utilizing raw IPs for firewall block lists from reputable sources can enhance network security.
- Continuous monitoring and updating of security measures are essential to adapt to evolving threats.

# [[Quick Reference]]

Key Characteristics of Beaconing Traffic

| Characteristic  | Description                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| Periodicity     | Beacon messages are sent at regular intervals, creating a repetitive traffic pattern.                |
| Payload Size    | Beacon messages typically contain small and consistent amounts of data.                              |
| False Positives | Common network protocols may exhibit beaconing behavior, leading to alerts that need to be analyzed. |

Key Examples of Benign Beaconing

- **Network Time Protocol (NTP)**: Used for time synchronization among devices, sending messages at intervals of 15 to 60 minutes.
- **Microsoft Update**: Devices check for updates at regular intervals to ensure security and performance.
- **File Synchronization**: Applications like OneDrive and Dropbox use periodic polling to sync files, resembling beaconing behavior.

Key Evasion Techniques

- **Randomized Timing**: Adversaries introduce randomness (jitter) to beacon intervals to avoid detection.
- **Variable Message Size**: Unlike normal traffic, beacon messages may have consistent or insignificantly varying sizes, making them easier to identify.
- **Domain Generation Algorithms (DGA)**: Used to generate multiple domain names for C2 servers, complicating detection efforts.

Key Tools for Detection

- **Cisco Secure Firewall**: Utilizes Snort IPS engine to detect and block connections to known C2 servers.
- **Cisco Secure Network Analytics**: Monitors network traffic and applies behavioral analytics to detect anomalous beaconing activity.
- **Open-Source Tools**: Tools like RITA and Flare help analyze network traffic for beaconing patterns.

Facts to Memorize

- NTP uses UDP port 123.
- The default authorization reporting interval for Cisco Secure Firewall Management Center is every 30 days.
- The frequency of updates for security devices depends on the criticality of the information.

Reference Information

- Common benign applications exhibiting beaconing: stock trading applications, email clients, gaming applications, Microsoft update services.
- Tools for detecting malicious beacons: Cisco Secure Firewall, Cisco Secure Network Analytics, RITA, Flare.

Concept Comparisons

|Concept|Benign Beaconing|Malicious Beaconing|
|---|---|---|
|Purpose|Regular updates and synchronization|Command and control communication|
|Traffic Pattern|Consistent intervals, predictable payload sizes|Variable intervals, may use jitter to evade detection|
|Examples|NTP, Microsoft updates, file synchronization|Malware contacting C2 servers|
|Detection Difficulty|Easier to identify due to regularity|More challenging due to evasion techniques|

Problem-Solving Steps

1. Identify the traffic patterns in your logs.
2. Distinguish between benign and malicious beaconing by analyzing the timing and size of packets.
3. Use tools like Cisco Secure Firewall or RITA to automate detection.
4. Filter out known benign traffic to reduce false positives.
5. Investigate any anomalies or irregular patterns in the remaining traffic.