# [[Quick Reference]]

Key Techniques

|Technique|Description|
|---|---|
|**DNS Sinkhole**|Blocks suspicious DNS queries by domain names to prevent access to malicious sites.|
|**BGP Black-holing**|Quickly blocks IP addresses across the enterprise to mitigate threats in seconds.|
|**Device Quarantine**|Isolates compromised devices using IAM security devices to prevent further network access.|
|**Firewall Rules**|Implements rules to block specific attacks or malicious traffic at the network perimeter.|

Key Challenges

- **Detection Delays**: Weak or slow detection capabilities can allow attackers to steal high-value data.
- **Operational Experience**: The need for human critical thinking in analyzing events, which cannot be fully replaced by automated systems.
- **Information Sharing**: The importance of sharing IOCs and having a robust information management infrastructure.

Key Tools

- **Classic Security Products**: Tools like antivirus, HIPS, IPS, and NGFW that provide foundational security measures.
- **Advanced Malware Protection**: Tools that analyze file SHA-256 values to detect malware.
- **Email Security Appliances**: Tools designed to detect and mitigate email-based threats.

Key Strategies

- **Defense in Depth**: Utilizing multiple layers of security tools to detect various types of events.
- **Continuous Review of Playbooks**: Regularly updating and reviewing playbooks to ensure they adapt to new threats and improve response efficiency.

Facts to Memorize

- Security analytics is essential for detecting attacks quickly and reconstructing incidents.
- Common detection tools include antivirus, HIPS, IPS, NGFW, and email security appliances.
- A DNS sinkhole blocks suspicious DNS queries by domain names.
- BGP black-holing can block IP addresses across the enterprise in seconds.
- Device quarantine can be achieved using IAM security devices like Cisco ISE.

Reference Information

- SOC (Security Operations Center) processes millions of log events daily.
- IOCs (Indicators of Compromise) need to be classified, stored, and shared effectively.
- Playbooks are collections of repeatable plays for incident detection and response.

Concept Comparisons

|Concept|Description|Key Differences|
|---|---|---|
|Detection Tools|Tools used to identify security events (e.g., antivirus, firewalls)|Different tools are specialized for different types of threats (e.g., DNS, malware).|
|Mitigation Techniques|Short-term methods to stop threats (e.g., DNS sinkhole, BGP black-holing)|Focus on immediate response to threats versus long-term security architecture changes.|
|Remediation Strategies|Medium- to long-term fixes (e.g., updating security controls)|Involves collaboration with IT and may require architectural changes.|

Problem-Solving Steps

1. **Identify the Incident**: Monitor logs and alerts to detect suspicious activity.
2. **Analyze the Data**: Use detection tools to correlate events and identify the source.
3. **Mitigate the Threat**: Implement short-term solutions like DNS sinkholes or BGP black-holing to stop the attack.
4. **Document the Incident**: Record all findings and actions taken for future reference.
5. **Remediate**: Work with IT to update security controls and review the security architecture.

# Understanding Security Analytics

![1](/Course-Notes/.assets/Pasted_image_20241201151959.png)
### Overview of Security Analytics

- Security analytics focuses on detecting and responding to cyber threats as quickly as possible, aiming to minimize the time between network compromise and threat detection.
- The increasing complexity of networks, including cloud, Software-Defined Networking (SDN), and Internet of Things (IoT) architectures, necessitates advanced analytics to manage vast amounts of security data.
- The primary goals of security analytics include rapid attack detection, stopping ongoing attacks, and providing detailed information for post-incident analysis.

### Importance of Detection Capabilities

- Complete prevention of breaches is nearly impossible; thus, organizations must prioritize detection capabilities to identify and respond to threats.
- Weak or slow detection allows attackers to exploit vulnerabilities and steal high-value data assets, emphasizing the need for robust analytics.
- Security Operations Centers (SOCs) process millions of log events daily, requiring analysts to discern which events warrant further investigation.

# Data Collection and Analysis

### Sources of Event Data

- Event data for security analytics can originate from various sources, including traditional security products (e.g., antivirus, Intrusion Prevention Systems) and less obvious sources (e.g., email servers, DNS servers).
- Experienced analysts are often needed to mine and interpret data from these less obvious sources, highlighting the importance of operational experience in security analytics.
- Understanding the context of events, such as why a client resolves domains on a blocked list, is crucial for effective threat detection.

### Role of Human Analysts

- Despite advancements in automated machine-learning systems, human critical thinking remains essential in interpreting security events and making informed decisions.
- Analysts must be trained to recognize significant events and understand the implications of various indicators of compromise (IOCs).
- The combination of automated tools and human expertise creates a more effective security posture for organizations.

# Information Sharing and Management

### Information Sharing Practices

- Sharing information about discovered IOCs is vital for enhancing the overall security posture of an organization.
- A robust information management infrastructure is necessary for classifying, storing, and exporting IOCs to security devices.
- Effective information sharing can lead to quicker detection and response to emerging threats.

### Network Services and Detection Tools

- Network services must be flexible, scalable, and reliable to support organizational missions and security needs.
- Different detection tools are required for various types of threats, such as Command and Control (CnC) communications and malware detection.
- Tools should be capable of consuming IOC information from other sources, enhancing their detection capabilities.

# Incident Response and Mitigation Strategies

### Playbooks in Security Analytics

- A playbook is a collection of repeatable processes and methods designed to detect and respond to security incidents.
- Playbooks should undergo a quality assurance process before being integrated into production to ensure effectiveness.
- Regular reviews and updates of playbooks by security analysts help adapt responses to evolving threats.

### Mitigation and Remediation Techniques

- Short-term mitigation strategies include DNS sinkholes, BGP black-holing, device quarantine, and firewall rules to block attacks.
- Long-term remediation requires collaboration with IT and network teams to update security controls and review security architecture.
- Continuous improvement of security measures is essential to adapt to new threats and vulnerabilities.