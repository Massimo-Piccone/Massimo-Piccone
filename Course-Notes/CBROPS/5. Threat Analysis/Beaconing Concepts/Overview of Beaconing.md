### Definition and Purpose of Beaconing

| **Topic**                | **Description**                                                                                                                                                                                                 |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Definition of Beaconing** | Beaconing is a communication pattern in networking where small data packets are transmitted at regular or variable intervals.                                                                                  |
| **Purpose of Beaconing**  | - **Service Discovery**: Helps devices find available services in a network. <br> - **Device Presence Checking**: Confirms whether a device is still active or connected. <br> - **User Activity Tracking**: Used for tracking user or device activities in certain systems. |
| **Wireless Network Beaconing**  | In wireless networks, access points use beaconing to announce their **presence** and **capabilities** (e.g., supported speeds, security protocols).                                                       |
| **Bluetooth Beaconing**  | Bluetooth devices use beaconing for **location awareness**, helping with proximity detection or navigation.                                                                                                    |
| **Wired Network Beaconing** | In wired networks, protocols use beaconing for periodic **message exchanges** to synchronize client-server communications or to check the availability of services.                                               |


![11](/Course-Notes/.assets/Pasted_image_20241128125537.png)
### Beaconing in Cybersecurity

- Beaconing is also a characteristic of malicious activities, where compromised devices communicate with adversaries' systems.
- It is commonly used in ransomware attacks and botnets, allowing adversaries to issue commands remotely.
- The Mandiant M-Trends 2022 report highlights that many advanced persistent threat (APT) groups utilize beaconing for communication with compromised hosts.
- Detecting beaconing activity can indicate that an organization is under threat and may already be compromised.

### Visual Representation of Beaconing

- The following figure illustrates the communication flow between a compromised host and adversary-controlled resources, highlighting the beaconing process.

![10](/Course-Notes/.assets/Pasted_image_20241128125348.png)

- SOC analysts must conduct beacon analysis to identify and mitigate malware threats in their networks.

# Beaconing Functionality

### Technical Aspects of Beaconing

- Beaconing can occur at all layers of the TCP/IP protocol stack, serving as a keepalive mechanism for various protocols.
- Common communication protocols utilize beaconing-like exchanges for tasks such as data synchronization and service discovery.
- In web applications, beaconing is used to create repeated requests for system inventory and user activity tracking.

### Malicious Usage of Beaconing

- Beaconing is a key feature in botnets, where compromised devices communicate with a command-and-control (C2) server.
- The C2 server issues commands to the botnet, which can be used for illicit activities like DDoS attacks and data exfiltration.
- The MITRE ATT&CK framework identifies 32 distinct C2 techniques and protocols that utilize beaconing for communication.

# Beaconing in the Attack Kill Chain

![9](/Course-Notes/.assets/Pasted_image_20241128125618.png)
### Phases of the Attack Kill Chain

- Beaconing is most evident in the command-and-control (C2) phase of the attack kill chain.
- The adversary must first gain access to the target system and execute beaconing malware to establish communication.
- The kill chain phases include reconnaissance, weaponization, delivery, exploitation, installation, C2, and action-on-objective.

### Establishing Communication Channels

- After the initial access, the adversary executes the exploit to load the beaconing malware, establishing a communication channel.
- The compromised host sends outbound beacons to the adversary's C2 server, indicating readiness for further instructions.
- The initial payload may include functions for maintaining a covert backdoor communication channel.

# Case Study: Botnets and Beaconing

### Understanding Botnets

- A botnet consists of a network of compromised devices controlled by an adversary, often used for malicious activities.
- Devices in a botnet communicate with a C2 server, sending beacons to indicate their status and readiness for commands.
- The term 'botnet' combines 'robot' and 'network', reflecting the external control over the devices.

### Beaconing in Botnet Operations

- Compromised devices send regular beacons to the C2 server, which blends in with benign network traffic.
- The frequency of these beacons can increase when the adversary is preparing for an attack, indicating readiness for action.
- The C2 server can issue commands to the botnet, instructing devices to perform tasks aligned with the adversary's objectives.

# Overview of Beaconing Malware and C2 Communication

### Understanding Command & Control (C2) Servers

- C2 servers are malicious servers controlled by adversaries, often located remotely to evade detection.
- They facilitate communication with compromised devices, allowing adversaries to send commands and receive data.
- The establishment of a communication channel is crucial for the adversary to maintain control over the botnet.
- C2 servers can be disguised as legitimate services, making it difficult for security systems to identify malicious activity.
- The use of multiple C2 servers can enhance redundancy and resilience against takedown efforts.
- Historical examples include the Mirai botnet, which utilized a C2 server to orchestrate DDoS attacks.

### Characteristics of Beaconing Malware

- Beaconing malware is designed to establish covert connections using common protocols like DNS, HTTP, and HTTPS.
- It can encapsulate malicious traffic within legitimate network communications, making detection challenging.
- The term 'Beacon' is often associated with Cobalt Strike, a popular penetration testing tool that includes beaconing capabilities.
- Beaconing malware can execute arbitrary code and shell commands on compromised hosts, increasing its threat level.
- The malware family is frequently used in cyberattacks, as reported in the M-Trends 2022 report.
- The flexibility of beaconing malware allows adversaries to customize their payloads based on reconnaissance data.

![8](/Course-Notes/.assets/Pasted_image_20241128125738.png)
### Types of Beacons and Their Functionality

- Beacons can vary in their communication methods, including encrypted channels to evade detection by security systems.
- They can utilize nonstandard ports to bypass firewall rules, increasing the likelihood of successful communication.
- Common services like Dropbox and Twitter can be exploited as communication channels for beaconing malware.
- The encapsulation of commands within regular traffic (e.g., DNS queries) allows adversaries to blend in with legitimate network activity.
- The ability to tunnel traffic through standard protocols enhances the stealth of beaconing operations.
- Examples of beaconing messages include DNS queries that return malicious commands from an adversary-controlled domain.

![7](/Course-Notes/.assets/Pasted_image_20241128125750.png)
# Beaconing Communication Mechanisms
### Establishing Beaconing Communication Channels

- Continuous control over compromised systems is achieved through a reliable beaconing communication channel.
- The channel consists of a service on the compromised host and a listener on the adversary's system to handle incoming connections.
- Common protocols (e.g., HTTP, DNS) are used to facilitate communication, ensuring compatibility between systems.
- The communication channel must verify the presence of the compromised host to maintain control.
- Adversaries often implement redundancy in their communication methods to avoid detection and maintain access.
- The use of encrypted communication can hinder detection by intrusion prevention systems (IPS).

![6](/Course-Notes/.assets/Pasted_image_20241128125810.png)
DNS Beaconing:
![5](/Course-Notes/.assets/Pasted_image_20241128125914.png)
### Payload Types: Staged vs. Nonstaged

- Payloads can be categorized as nonstaged (inline) or composite, each serving different operational needs.
- Nonstaged payloads are self-contained and perform all necessary tasks, including establishing communication and executing commands.
- Composite payloads consist of a stager and one or more stages, allowing for modular functionality and smaller initial payload sizes.
- Stager payloads are designed to establish the communication channel, while staged payloads execute specific adversarial objectives.
- The choice between payload types depends on the adversary's strategy and the operational environment.
- Nonstaged payloads are generally larger and more complex due to their comprehensive capabilities.

![4](/Course-Notes/.assets/Pasted_image_20241128125955.png)
# Security Implications and Countermeasures

### Challenges in Detecting Beaconing Malware

- The use of common protocols for beaconing makes it difficult for security systems to distinguish between legitimate and malicious traffic.
- Encrypted communications can bypass traditional security measures, leaving organizations vulnerable to attacks.
- The ability to use nonstandard ports complicates firewall configurations and increases the risk of undetected communication.
- Social engineering tactics may be employed to gain access to legitimate services for beaconing purposes.
- Continuous monitoring and analysis of network traffic are essential to identify potential beaconing activity.
- Historical incidents highlight the need for advanced threat detection systems to combat evolving malware techniques.

### Recommended Security Practices

- Implementing strict firewall rules to limit outbound traffic to known and trusted services can reduce the risk of beaconing.
- Regularly updating and patching systems can mitigate vulnerabilities that adversaries exploit for initial access.
- Employing network segmentation can help contain potential breaches and limit the spread of malware.
- Utilizing advanced threat detection tools that analyze traffic patterns can enhance the identification of beaconing activity.
- Conducting regular security training for employees can help prevent social engineering attacks that lead to compromises.
- Collaborating with threat intelligence services can provide insights into emerging threats and effective countermeasures.

# Understanding Stager Payloads

### Definition and Purpose of Stager Payloads

- A stager payload is significantly smaller than a nonstaged (inline) payload, designed to establish a communication channel between the target and the adversary.
- Its primary tasks include facilitating the transfer and execution of the staged payload and maintaining the communication channel post-execution.
- Stager payloads are crucial for complex attacks, often requiring multiple stages to achieve the adversary's objectives.

### Characteristics of Stage Payloads

- Stage payloads perform the main objectives of an attack, fitting within the resource constraints of the target system.
- They can be executed in sequence, allowing for flexibility in attack strategies.
- Examples of stager payloads include Metasploit's bind_tcp, reverse_tcp, and reverse_http, with Meterpreter as a notable stage payload.

### Advantages of Staging

- **Flexibility**: Adversaries can combine one stager with multiple stages, adapting to various scenarios.
- **Stealthiness**: Smaller payloads are less likely to be detected by security measures, enhancing the attack's success rate.
- **Efficacy**: By dividing payloads into smaller stages, adversaries can bypass limitations of disk and memory space on the target system.

![3](/Course-Notes/.assets/Pasted_image_20241128134225.png)
### Exploitation Frameworks

- Metasploit is a prominent exploitation framework that offers both self-contained (nonstaged) and composite payloads, known as singles.
- Cobalt Strike provides stagers like the HTTP stager and DNS TXT stager, which can be inferred from their names based on the network protocol used.
- Understanding these frameworks is essential for recognizing how adversaries deploy their attacks.

# Malware Staging in Ransomware Attacks

![2](/Course-Notes/.assets/Pasted_image_20241128134204.png)
### Delivery Methods of Malware

- Adversaries can deliver malware in two ways: as a single package (nonstaged) or through a staging technique.
- Nonstaged malware is less common due to high detection risks; for example, sending full malware files as email attachments.
- Staging techniques are stealthier, allowing adversaries to deliver malware in phases, reducing the chance of detection.

### Phases of a Ransomware Attack

- ****Initiation****: A dropper is delivered, acting as a vehicle to drop other malware into the system, often through phishing emails or drive-by attacks.
- ****Infection****: The stager uses the established communication channel to download ransomware, which may remain inactive until activated by the adversary.
- ****Staging****: The adversary activates the ransomware through the C2 channel, allowing the compromised system to communicate with the C2 server.

### Ransomware Functionality

- **Scan**: The malware scans the system for files to encrypt, determining permissions and searching for cloud-stored data.
- **Encrypt**: Ransomware encrypts files using cryptographic methods like RSA or AES, potentially encrypting vast amounts of data quickly.
- **Payday**: After encryption, a ransom demand is displayed, leveraging the victim's urgency to recover their data.

# Beaconing and Risk Factors

### Understanding Beaconing

- Beaconing refers to the communication established by malware with a command and control (C2) server, indicating a confirmed threat.
- The likelihood of beaconing suggests a medium probability of hosts being infected with beaconing malware, which is often highly visible.
- SOC analysts must prioritize detecting and mitigating beaconing threats to protect organizational assets.

### Risk Assessment of C2 Beaconing

- Business Impact: The negative effects on operations and customer trust are high, necessitating immediate attention from security teams.
- Complexity: The medium complexity of detecting C2 beaconing requires sophisticated monitoring and analysis tools.
- Combining these factors positions malicious beaconing as a top risk, warranting proactive hunting and mitigation efforts by SOC analysts.

![1](/Course-Notes/.assets/Pasted_image_20241128134124.png)

Fundamental Theories

|Theory/Model|Description|
|---|---|
|**Cyber Kill Chain**|A model that outlines the stages of a cyber attack, from initial reconnaissance to execution and maintenance of control over compromised systems. Beaconing is primarily associated with the command-and-control phase.|
|**Malware Staging**|A method of delivering malware in stages to evade detection, where an initial stager payload establishes a communication channel and downloads the main payload.|

Key Risks

- **Likelihood of Beaconing**: Medium probability of hosts being infected with beaconing malware, which is often visible in network traffic.
- **Business Impact**: High negative impact on operations and customer trust due to potential data breaches or service disruptions caused by beaconing activities.
- **Complexity of Detection**: Medium difficulty in detecting beaconing activities, necessitating active monitoring and analysis by security teams.

Seminal Studies

- **Mandiant M-Trends 2022 Report**: Highlights the prevalence of beaconing in advanced persistent threat (APT) groups, indicating that many use beaconing channels for communication with compromised hosts.
- **Splunk’s SURGe Team Analysis**: Analyzed ransomware strains and their ability to encrypt large amounts of data quickly, emphasizing the importance of detecting early signs of beaconing communication.

Key People

- **Adversaries**: Individuals or groups that exploit vulnerabilities in systems to gain unauthorized access and control, often using techniques like beaconing to maintain that control.

Facts to Memorize

- Beaconing is a communication pattern in networking.
- Beaconing can indicate both benign and malicious activities.
- The command-and-control (C2) phase is critical in the attack kill chain.
- Botnets are groups of compromised devices controlled by adversaries.
- Cobalt Strike's Beacon is a well-known example of beaconing malware.

Reference Information

- Common protocols used in beaconing: DNS, HTTP, HTTPS, and SSH.
- The MITRE ATT&CK framework identifies 32 distinct C2 techniques and protocols.
- Ransomware can use RSA and AES for encryption.
- The term 'stager' refers to a payload that establishes a communication channel.

Concept Comparisons

|Concept|Description|Example|
|---|---|---|
|Nonstaged Payload|A self-contained payload that performs all tasks required by the adversary.|Full malware delivered in one go|
|Staged Payload|A composite payload consisting of a stager and one or more stages.|Ransomware delivered in parts|
|Beaconing|Regular transmission of data packets for communication.|Access points announcing networks|
|Command-and-Control (C2)|A phase in the attack kill chain where adversaries control compromised hosts.|Botnet communication with C2|

Cause and Effect

| Cause                                    | Effect                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------ |
| Initial access gained by adversaries     | Compromised systems can be controlled through beaconing.                       |
| Use of reconnaissance phase information  | Adversaries select appropriate exploits for delivery and execution.            |
| Establishment of a communication channel | Adversaries can send commands and maintain control over compromised systems.   |
| Detection of malicious beacons           | Indicates that an organization is under threat and may already be compromised. |
