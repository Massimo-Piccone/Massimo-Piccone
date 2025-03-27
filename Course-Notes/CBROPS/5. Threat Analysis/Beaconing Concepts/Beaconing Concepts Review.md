%% #review [[Complete Study]]%%
# [[Overview of Beaconing]]
![16](/Course-Notes/.assets/Pasted_image_20241128125537.png)
- Commonly used in ransomware attacks and botnets, to issue commands remotely.
- The Mandiant M-Trends 2022 report highlights that many advanced persistent threat (APT) groups utilize beaconing for communication with compromised hosts.
- Detecting beaconing activity can indicate that an organization is under threat and may already be compromised.
### Visual Representation of Beaconing
![15](/Course-Notes/.assets/Pasted_image_20241128125348.png)

- Beaconing is a key feature in botnets, where compromised devices communicate with a command-and-control (C2) server.
- The C2 server issues commands to the botnet, which can be used for illicit activities like DDoS attacks and data exfiltration.
- The MITRE ATT&CK framework identifies 32 distinct C2 techniques and protocols that utilize beaconing for communication.

#### Beaconing in the attack kill chain

- After the initial access, the adversary executes the exploit to load the beaconing malware, establishing a communication channel.
- The compromised host sends outbound beacons to the adversary's C2 server, indicating readiness for further instructions.
- The initial payload may include functions for maintaining a covert backdoor communication channel.
![14](/Course-Notes/.assets/Pasted_image_20241128125618.png)
#### Beaconing in Botnet Operations

- Compromised devices send regular beacons to the C2 server, which blends in with benign network traffic.
- The frequency of these beacons can increase when the adversary is preparing for an attack, indicating readiness for action.
- The C2 server can issue commands to the botnet, instructing devices to perform tasks aligned with the adversary's objectives.

### Characteristics of Beaconing Malware
- Designed to establish covert connections using common protocols.
- It can encapsulate malicious traffic within legitimate network communications
- Flexibility of beaconing malware allows custom payloads based on reconnaissance data.

![13](/Course-Notes/.assets/Pasted_image_20241128125738.png)
### Types of Beacons and Their Functionality

| **Key Point**                               | **Description**                                                                                                                                             |
|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Communication Methods**                   | Beacons may use **encrypted channels** to avoid detection by security systems.                                                                             |
| **Bypassing Firewall Rules**                | Beacons can use **nonstandard ports** to bypass firewall rules and improve the chances of successful communication.                                          |
| **Exploitation of Common Services**        | Services like **Dropbox** and **Twitter** can be exploited for beaconing, allowing malware to communicate covertly.                                           |
| **Encapsulation in Regular Traffic**       | Beacons can hide within **regular traffic** (e.g., DNS queries) to blend in with legitimate network activity, making detection harder.                        |
| **Traffic Tunneling via Standard Protocols**| Beaconing can tunnel traffic through **standard protocols** (e.g., DNS or HTTP) to improve stealth during communication.                                      |
| **Example of Beaconing Messages**          | **DNS queries** can be used to receive malicious commands from an adversary-controlled domain, enabling beaconing malware to execute actions.                |
![12](/Course-Notes/.assets/Pasted_image_20241128125750.png)
# Beaconing Communication Mechanisms
| **Key Point**                             | **Description**                                                                                                                                             |
|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reliable Beaconing Channel**            | A **reliable communication channel** is used by adversaries to maintain continuous control over compromised systems.                                        |
| **Channel Components**                    | The beaconing channel consists of a **service** on the compromised host and a **listener** on the adversary's system to handle incoming connections.          |
| **Use of Common Protocols**               | **Common protocols** like **HTTP** and **DNS** are used to ensure the communication channel is compatible with different systems.                             |
| **Presence Verification**                 | The communication channel must **verify** that the compromised host is still present to ensure continued control by the attacker.                           |
| **Redundancy for Stealth**                | Adversaries often implement **redundancy** in their beaconing methods to avoid detection and maintain access.                                                |
| **Encrypted Communication**               | **Encrypted communication** is used to evade detection by **intrusion prevention systems (IPS)**, making it harder for security tools to spot the beaconing traffic. |
Https Beacon
![11](/Course-Notes/.assets/Pasted_image_20241128125810.png)
DNS Beacon
![10](/Course-Notes/.assets/Pasted_image_20241128125914.png)
### Payload Types: Staged vs. Nonstaged
| **Key Point**                        | **Description**                                                                                                                              |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Payload Categories**               | **Nonstaged (inline)** or **composite**                                                                                                      |
| **Nonstaged Payloads**               | **Nonstaged payloads** are self-contained, performing all tasks (e.g., communication, command execution) in one package.                     |
| **Composite Payloads**               | **Composite payloads** consist of a **stager** and **stages**, allowing for **modular functionality** and **smaller initial payload sizes**. |
| **Stager Payloads**                  | **Stager payloads** are designed to establish the **communication channel**, setting the stage for further payload execution.                |
| **Staged Payloads**                  | **Staged payloads** execute specific tasks or objectives once the communication channel is established by the stager.                        |
| **Choosing Payload Types**           | The choice between **nonstaged** and **composite payloads** depends on the **adversary's strategy** and the **operational environment**.     |
| **Complexity of Nonstaged Payloads** | **Nonstaged payloads** are typically **larger** and **more complex** because they contain all necessary functionality in one package.        |

![9](/Course-Notes/.assets/Pasted_image_20241128125955.png)
# Security Implications and Countermeasures
### Challenges in Detecting Beaconing Malware

| **Key Point**                                 | **Description**                                                                                                                                             |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Use of Common Protocols**                   | **Beaconing** can use **common protocols** (e.g., HTTP, DNS), making it difficult for security systems to distinguish between **legitimate** and **malicious** traffic. |
| **Encrypted Communications**                  | **Encrypted communications** can bypass traditional security measures, making it harder for detection systems to identify **malicious traffic**.               |
| **Nonstandard Ports**                         | **Nonstandard ports** complicate **firewall configurations** and increase the likelihood of **undetected communication** from beaconing malware.                |
| **Social Engineering Tactics**                | **Social engineering** may be used to gain access to **legitimate services** (e.g., cloud platforms) for **beaconing purposes**, making detection harder.       |
| **Continuous Monitoring**                     | **Ongoing monitoring** and analysis of **network traffic** are crucial for identifying potential **beaconing activity** and catching threats early.            |
| **Need for Advanced Detection Systems**       | **Historical incidents** highlight the importance of implementing **advanced threat detection** systems to deal with evolving **malware techniques**.         |
### Recommended Security Practices

| **Key Point**                                   | **Description**                                                                                                                                             |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Strict Firewall Rules**                       | **Implementing strict firewall rules** to limit outbound traffic to **trusted services** reduces the risk of beaconing by controlling external communication. |
| **Regular System Updates**                      | **Regularly updating and patching systems** helps **mitigate vulnerabilities** that adversaries exploit to gain initial access.                              |
| **Network Segmentation**                        | **Network segmentation** helps **contain potential breaches** and **limit malware spread** by separating critical systems from less-secure ones.              |
| **Advanced Threat Detection Tools**             | Using **advanced threat detection tools** that analyze **traffic patterns** improves the identification of **beaconing activity** and suspicious behaviors.    |
| **Security Training for Employees**             | **Regular security training** helps employees recognize and prevent **social engineering attacks**, which are commonly used to gain access to systems.         |
| **Collaboration with Threat Intelligence**      | **Collaborating with threat intelligence services** provides **insights into emerging threats** and effective countermeasures, improving proactive defense.     |
# Understanding Stager Payload

![8](/Course-Notes/.assets/Pasted_image_20241128134225.png)

| **Key Point**                              | **Description**                                                                                                                                                 |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Stager Payload Definition**              | A **stager payload** is smaller than a nonstaged payload and is designed to establish a **communication channel** between the target and the adversary.         |
| **Primary Tasks of Stager Payloads**       | The main tasks of a stager include facilitating the transfer and execution of the **staged payload** and maintaining the communication channel after execution. |
| **Role in Complex Attacks**                | **Stager payloads** are crucial for **complex attacks**, often requiring multiple stages to accomplish the adversary's objectives.                              |
| **Characteristics of Stage Payloads**      | **Stage payloads** perform the main objectives of the attack, fitting within the target system's **resource constraints**.                                      |
| **Sequential Execution of Stage Payloads** | **Stage payloads** can be executed in **sequence**, providing flexibility in attack strategies.                                                                 |
| **Examples of Stager Payloads**            | **Examples** of stager payloads include **Metasploit’s bind_tcp**, **reverse_tcp**, **reverse_http**, with **Meterpreter** as a notable **stage payload**.      |
| **Advantages of Staging**                  |                                                                                                                                                                 |
| **- Flexibility**                          | One stager can combine with **multiple stages**, adapting to various attack scenarios.                                                                          |
| **- Stealthiness**                         | Smaller **stager payloads** are **less likely** to be detected by security systems, increasing the attack's chances of success.                                 |
| **- Efficacy**                             | Dividing payloads into **smaller stages** allows adversaries to bypass **disk** and **memory space** limitations on the target system.                          |
| **Exploitation Frameworks**                |                                                                                                                                                                 |
| **- Metasploit**                           | **Metasploit** offers **both self-contained (nonstaged)** and **composite payloads**, also known as **singles**.                                                |
| **- Cobalt Strike**                        | **Cobalt Strike** provides **stagers** like **HTTP stager** and **DNS TXT stager**, identified by the protocol they use.                                        |
# Malware Staging in Ransomware Attacks

![7](/Course-Notes/.assets/Pasted_image_20241128134204.png)

| **Key Point**                     | **Description**                                                                                                                                                 |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Delivery Methods of Malware**   | Malware can be delivered in **two main ways**: as a **single package** (nonstaged) or via **staging techniques**.                                               |
| **Nonstaged Malware**             | **Nonstaged malware** is **less common** due to its high detection risk. **Example**: malware delivered as email attachments.                                   |
| **Staging Techniques**            | **Staging techniques** allow malware to be delivered in **phases**, making it more **stealthy** and reducing the likelihood of detection.                       |
| **Phases of a Ransomware Attack** |                                                                                                                                                                 |
| **- Initiation**                  | The attack begins with a **dropper** delivered, often via **phishing emails** or **drive-by attacks**, to drop other malicious payloads.                        |
| **- Infection**                   | The **stager** payload uses the **communication channel** to **download ransomware**, which may remain **inactive** until activated by the adversary.           |
| **- Staging**                     | The adversary activates the ransomware through the **C2 (command and control)** channel, allowing the compromised system to **communicate** with the C2 server. |
| **Ransomware Functionality**      |                                                                                                                                                                 |
| **- Scan**                        | Ransomware scans the system for files to encrypt, checking **permissions** and looking for **cloud-stored data** to target.                                     |
| **- Encrypt**                     | It uses cryptographic methods like **RSA** or **AES** to encrypt **vast amounts of data** quickly and efficiently.                                              |
| **- Payday**                      | After encryption, the ransomware demands a **ransom**, leveraging the victim's **urgency** to recover their files.                                              |

# [[Detecting Beacons]]

Problem-Solving Steps

1. Identify the traffic patterns in your logs.
2. Distinguish between benign and malicious beaconing by analyzing the timing and size of packets.
3. Use tools like Cisco Secure Firewall or RITA to automate detection.
4. Filter out known benign traffic to reduce false positives.
5. Investigate any anomalies or irregular patterns in the remaining traffic.

### Characteristics of Beaconing Traffic

| Characteristics                                 | **Description**                                                                                                                                            |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Periodic Message Exchanges**                  | **Beaconing traffic** is characterized by **repetitive** message exchanges, creating identifiable **traffic patterns**.                                    |
| **Small and Consistent Payloads**               | The **payload** in beaconing messages is typically **small** and **consistent**, which helps distinguish **benign** from **malicious traffic**.            |
| **False Positives Challenge**                   | **False positives** are common when detecting beaconing, as many legitimate network protocols show **similar periodic behavior**.                          |
| **Common Protocols Generating False Positives** | Protocols like **NTP**, **OSPF**, and **BGP** may generate **false positives** due to their inherent **beaconing characteristics**.                        |
| **Legitimate Applications Mimicking Beaconing** | Applications such as **stock trading**, **email clients**, and **social media platforms** also engage in **periodic communication**, resembling beaconing. |
| **Disguising Beaconing to Evade Detection**     | Adversaries often hide malicious **beaconing traffic** within **common protocols** to evade detection by **security devices**.                             |
### Challenges in Detecting Beaconing

| Challenges                                       | **Description**                                                                                                                                     |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Complexity in Detection**                      | Detecting **beaconing traffic** is challenging due to the prevalence of **false positives**, requiring **thorough analysis** to confirm legitimacy. |
| **Built-in Periodic Communication in Protocols** | Many network protocols have **inherent periodic communication**, complicating the identification of **malicious activity**.                         |
| **Differentiating Benign vs. Malicious Traffic** | Security analysts must understand the **context** and **behavior** of traffic to distinguish between **benign** and **malicious beaconing**.        |
| **False Positives and Alert Fatigue**            | High volumes of **false positives** can lead to **alert fatigue**, where analysts may overlook genuine threats.                                     |
| **Continuous Monitoring for Accuracy**           | **Ongoing monitoring** and analysis are essential to improve **detection accuracy** and minimize false positives.                                   |
| **Familiarity with Use Cases**                   | Knowledge of both **benign and malicious** use cases enhances the **efficiency** of SOC analysts in identifying threats.                            |
# Benign Beaconing Use Cases

Network Time Protocol (NTP)
- client-server model
- clients request the current time from an NTP server
- between 15 to 60 minutes.
- fixed in size
- uses UDP port 123

Microsoft Update Services
- checks for updates
- data exchanged varies
- WUO periodically contacts WSUS server to avoid overwhelming it
![6](/Course-Notes/.assets/Pasted_image_20241128145754.png)

Security Device Updates
- Maintains effectiveness against threats
- Frequency: Depends on the criticality of updates 
- Importance: Understanding update behavior is vital for accurate threat detection

File Synchronization
- **Applications**: OneDrive, Dropbox, etc.
- **Polling Behavior**: Periodic polling to check for changes in files across locations
- **Resemblance to Beaconing**: Regular communication for data consistency
- **Efficiency**: Minimizes bandwidth usage while ensuring timely updates
- **Computing Power**: Requires significant resources compared to push-based methods
- **Analyst Consideration**: Must distinguish file sync from potential malicious beaconing
- **Benefit**: Helps reduce false positives in network traffic analysis

![5](/Course-Notes/.assets/Pasted_image_20241128145954.png)
# File Synchronization Systems
#### Polling Mechanism

- **Polling**: Periodic checks for changes at predetermined intervals, resembling beaconing.
- **Resource Usage**: More resource-intensive than push-based synchronization, requiring significant computing power.
- **Optimization**: Reduces time for file uploads and downloads, optimizing bandwidth usage.
- **Example**: Polling every 5 minutes vs. push-based updates in real-time.
### Licensing Management with Cisco Secure Firewall

- **System**: Cisco Secure Firewall Management Center (formerly Cisco Firepower Management Center)
- **Function**: Manages multiple Cisco Secure Firewall devices, aggregates network traffic and performance data for centralized monitoring.
- **Licensing**: Managed via periodic communication with Cisco Smart Software Manager (SSM) portal, requiring registration with the License Authority.
- **Reporting Intervals**:
    - Default: Every 15 minutes for license usage.
    - Authorization: Every 30 days for authorization reporting.

# Investigating and Hunting Malicious Beaconing

| **Aspect**              | **Details**                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Beaconing Traffic**   | Unique timing and packet size traits differentiate it from normal traffic   |
| **Analyst Task**        | Identify and filter out legitimate traffic to focus on potential threats    |
| **Jitter**              | Adversaries randomize beacon intervals to evade detection                   |
| **Detection Challenge** | Jitter complicates the detection process due to randomization of intervals  |

| **Evasion Technique**                  | **Details**                                                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Changing Beacon Intervals**          | Adversaries alter beacon intervals during idle and active phases of an attack                                                |
| **Prolonging Beacon Interval**         | Helps avoid detection during threat-hunting by making beacons less frequent                                                  |
| **Lack of Fixed Interval**             | No standard formula for beaconing intervals, making detection more challenging                                               |
| **Randomized Timing**                  | Adversaries introduce randomness (jitter) to beacon intervals to avoid detection.                                            |
| **Variable Message Size**              | Unlike normal traffic, beacon messages may have consistent or insignificantly varying sizes, making them easier to identify. |
| **Domain Generation Algorithms (DGA)** | Used to generate multiple domain names for C2 servers, complicating detection efforts.                                       |

![4](/Course-Notes/.assets/Pasted_image_20241128150246.png)![3](/Course-Notes/.assets/Pasted_image_20241128150520.png)Concept Comparisons

|Concept|Benign Beaconing|Malicious Beaconing|
|---|---|---|
|Purpose|Regular updates and synchronization|Command and control communication|
|Traffic Pattern|Consistent intervals, predictable payload sizes|Variable intervals, may use jitter to evade detection|
|Examples|NTP, Microsoft updates, file synchronization|Malware contacting C2 servers|
|Detection Difficulty|Easier to identify due to regularity|More challenging due to evasion techniques|

# Detection Techniques for Beaconing

| Cisco Secure Firewall          | **Details**                                                                                                |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Botnet Beacon Detection**    | Monitors traffic between inside and outside zones to detect botnet beacons                                 |
| **Snort Engine**               | Uses Cisco Secure IPS Snort engine to identify known vulnerabilities and suspicious activities             |
| **Security Intelligence Page** | Allows SOC analysts to pinpoint compromised hosts and filter by the "BOT" keyword for quick identification |
![2](/Course-Notes/.assets/Pasted_image_20241128153530.png)

| Cisco Secure Network Analytics | **Details**                                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| **Comprehensive Visibility**   | Provides visibility and analysis of network traffic using telemetry from existing infrastructure                                |
| **Behavioral Analytics**       | Uses advanced analytics to establish a baseline of normal activity and detect anomalies                                         |
| **Event Correlation**          | Correlates multiple security events to identify potential attacks and affected devices, enhancing threat detection capabilities |
![1](/Course-Notes/.assets/Pasted_image_20241128153546.png)

### Open-Source Tools for Beacon Detection

| **Tool**   | **Feature**                       | **Details**                                                                 |
|------------|-----------------------------------|-----------------------------------------------------------------------------|
| **RITA**   | **Functionality**                 | Open-source framework that computes statistical relations for connection intervals and session sizes, aiding in C2 detection |
|            | **Beaconing Detection**           | Features dedicated beaconing filters that assign a beacon score (0.000 to 1) to each connection, indicating probability of beaconing |
|            | **DNS-based C2 Tunnel Detection** | Detects DNS-based C2 tunnels as part of beaconing detection                |
| **Flare**  | **Purpose**                       | Identifies C2 beaconing by analyzing Elasticsearch flow data                |
|            | **Components**                    | Written in Python, integrates with Elasticsearch and Suricata               |
|            | **Suricata’s Functionality**      | Combines IDS, IPS, NSM, and PCAP processing for threat detection            |
# Mitigation Strategies Against C2 Beaconing


| **Mitigation Strategy**               | **Details**                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------|
| **Early Detection and Response**      | - Prompt detection of beaconing activity is crucial to prevent threats.      |
|                                       | - Automated tools can identify patterns in beacon communications.           |
|                                       | - SIEM and SOAR platforms enhance detection capabilities.                    |
| **Incident Response Procedures**      | - Immediate actions: remove unapproved apps, stop suspicious processes.     |
|                                       | - Quarantine infected devices to prevent further spread of malware.         |
|                                       | - Establish firewall rules to block C2 server traffic, apply least privilege principle. |
| **Threat Intelligence and Continuous Improvement** | - Subscribe to threat intelligence sources (e.g., Cisco Talos, CISA) for proactive defense. |
|                                       | - Use raw IPs for firewall block lists from reputable sources.              |
|                                       | - Continuous monitoring and updates are essential to stay ahead of evolving threats. |
