# [[Quick Reference]]

Key Types of Threat Intelligence

| Type                                | Description                                                                                            |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Strategic Threat Intelligence**   | High-level information for business decision-makers, including adversary trends and financial impacts. |
| **Tactical Threat Intelligence**    | Technical information related to adversary tactics, techniques, and procedures (TTPs).                 |
| **Operational Threat Intelligence** | Focuses on specific threats or attack campaigns, often used by government organizations.               |
| **Technical Threat Intelligence**   | Detailed technical information about tools and resources used by adversaries in attacks.               |

Key Components of Cyber Threat Intelligence

- **Data Exchange**: Collecting and sharing findings with the security community to prepare for threats.
- **Data Analysis**: Applying methods to collected data to create usable technical indicators and patterns.
- **Predictive Analysis**: Using historical threat data enhanced with machine learning to anticipate future attacks.

Key Activities in Threat Intelligence

- **Collecting Information**: Gathering data about adversaries and threats from various sources.
- **Analyzing Data**: Evaluating collected threat data to generate actionable insights.
- **Sharing Indicators**: Distributing threat indicators with other teams or organizations to enhance collective defense.

Key Threat Intelligence Formats

|Format|Description|
|---|---|
|**Open Indicator of Compromise**|XML-based format for describing indicators with predefined terms.|
|**Cyber Observable Expression**|Standard for defining measurable events and properties for automated sharing of security information.|
|**Structured Threat Information eXpression (STIX)**|Structured language for defining threats and their context, widely used in CTI.|
|**Trusted Automated eXchange of Indicator Information (TAXII)**|Protocol for sharing CTI over HTTPS, designed to support STIX data exchange.|

Facts to Memorize

- Types of Cyber Threat Intelligence (CTI): Strategic, Tactical, Operational, Technical.
- Key components of actionable threat intelligence: Historical threat data, Machine learning and artificial intelligence, Cyber threat analysis.
- Traffic Light Protocol (TLP) colors: Red (restricted), Amber (limited disclosure), Green (community sharing), White (unlimited disclosure).

Reference Information

- Indicators of Compromise (IOCs) and Indicators of Attack (IOAs) are crucial for identifying and responding to threats.
- Common formats for sharing threat intelligence: Open IOC, CybOX, STIX, TAXII.
- The CTI lifecycle includes eight phases: Planning, Collecting, Sorting, Vetting, Sensitivity, Analyzing, Reporting, Feedback.

Concept Comparisons

|Concept|Indicators of Compromise (IOCs)|Indicators of Attack (IOAs)|
|---|---|---|
|Definition|Artifacts indicating evidence of an intrusion or breach|Early warning signs of an intrusion or attack|
|Purpose|Confirm malicious activity|Detect potential attacks in progress|
|Nature|Static and known threats|Dynamic and contextual, based on normal activity|
|Examples|File hashes, IP addresses, email indicators|Network scans, unusual logins, abnormal commands|

Key Terms/Concepts

- **Cyber Threat Intelligence (CTI)**: Knowledge and information about existing or emerging threats that organizations can use to proactively respond to those threats.
- **Indicators of Compromise (IOCs)**: Digital forensic artifacts indicating evidence of an intrusion or data breach, used to detect malicious activity.
- **Indicators of Attack (IOAs)**: Early warning signs of an intrusion or attack, focusing on the actions an adversary must perform for an attack to succeed.

# Overview of Cyber Threat Intelligence (CTI)

### Definition and Importance of CTI

- Cyber Threat Intelligence (CTI) refers to knowledge about existing or emerging threats that organizations can use to proactively respond to potential cyber threats.
- CTI is derived from the analysis of data collected from various internal and external sources, including human interactions, electromagnetic signals, and open-source intelligence (OSINT).
- The primary goal of CTI is to anticipate attacks and reduce risks associated with cyber threats, enhancing the overall security posture of an organization.
- Actionable information within CTI includes Indicators of Attack (IOA) and Indicators of Compromise (IOC), which help in understanding threat actors' behaviors, motives, and targets.
- Effective CTI requires continuous improvement of threat detection systems, including tuning rules and signatures to adapt to evolving malware.
- Organizations leverage CTI to make informed security decisions, improving the fidelity of alerts and providing greater context for security incidents.

![16](/Course-Notes/.assets/Pasted_image_20241202201632.png)
### Processes Involved in Creating CTI

- ****Data Exchange:**** Involves collecting input data from various sources and sharing findings with the security community to enhance collective defense.
- ****Data Analysis and Synthesis:**** After data collection, threat intelligence teams analyze the data to create usable technical indicators and patterns.
- The data collection process includes gathering information on adversaries' past activities, geographic locations, and behavior patterns.
- Successful intelligence sharing relies on effective threat descriptions and standardized data exchange formats and protocols.
- Predictive analysis using machine learning and AI enhances existing threat history data, allowing organizations to defend proactively rather than reactively.
- Activities involved in CTI include collecting information, analyzing data, generating indicators, extracting threat information, and creating reports for stakeholders.

# Types of Threat Intelligence

### Categories of Threat Intelligence

- There are four main categories of threat intelligence: strategic, tactical, operational, and technical, each serving different organizational goals and objectives.
- ****Strategic Threat Intelligence:**** Aimed at business decision-makers, providing high-level insights on adversaries, attack trends, and financial impacts, guiding budget allocations and resource planning.
- ****Tactical Threat Intelligence:**** Focuses on technical information related to adversary tactics, techniques, and procedures (TTPs), helping SOC managers and IT staff make informed defensive decisions.
- ****Operational Threat Intelligence:**** Used primarily by government organizations, this type gathers specific information on threats or attack campaigns, requiring more resources for in-depth analysis.
- ****Technical Threat Intelligence:**** Involves detailed technical data about tools and resources used by adversaries, such as file hashes and IP addresses, utilized daily by SOC and incident response teams.

### Detailed Examples of Threat Intelligence

- ****Strategic Example:**** A report detailing the latest trends in ransomware attacks across various industries, helping executives allocate resources effectively. (upper management and high-level executives)
- ****Tactical Example:**** An analysis of a recent phishing campaign that identifies the tools and techniques used by attackers, allowing SOC teams to update detection rules accordingly. (TTPs)
- ****Operational Example:**** A government agency investigating a specific cyber espionage campaign, gathering intelligence on the adversaries' methods and motivations. 
- ****Technical Example:**** A database of known malware file hashes and associated IP addresses that SOC analysts use to identify and mitigate threats in real-time. (Spacifics)

![15](/Course-Notes/.assets/Pasted_image_20241202201936.png)
# Understanding Cyber Threat Intelligence
### Definition and Types of Threat Intelligence

- **Technical Threat Intelligence:** Refers to specific data points such as filenames, file hashes, and URLs related to malware. It is used daily by Security Operations Center (SOC) staff and incident response teams.
- **Tactical Threat Intelligence**: Involves broader information about malware, such as its purpose and how it is used in attacks. It has a longer lifespan compared to technical threat intelligence. 
- **Comparison**: While both types are crucial, technical threat intelligence focuses on immediate, actionable data, whereas tactical threat intelligence provides context and understanding of threats.

### Importance of Cyber Threat Intelligence

- Organizations leverage threat intelligence to defend against sophisticated cyber threats, making it a critical component of modern cybersecurity strategies.
- Outdated methodologies without threat intelligence can lead to vulnerabilities, as they fail to adapt to evolving threats.
- Investing in Cyber Threat Intelligence (CTI) allows access to extensive threat databases, enhancing the effectiveness of security solutions.
- CTI aids in predicting adversary moves, enabling proactive defense measures and incident response.

![14](/Course-Notes/.assets/Pasted_image_20241202220535.png)
### Value Across Organizations

- CTI benefits various teams, including SOC, Network Operations Center (NOC), Digital Forensics and Incident Response (DFIR), and executive management.
- Understanding adversaries' motives and tactics helps organizations stay ahead of potential threats and respond swiftly to incidents.
- CTI is applicable across all sectors, enhancing security posture regardless of industry type.

![13](/Course-Notes/.assets/Pasted_image_20241202220602.png)
# Indicators of Compromise (IOCs) and Indicators of Attack (IOAs)

### Overview of IOCs and IOAs

- **Indicators of Compromise (IOCs):** Digital forensic artifacts that indicate evidence of an intrusion or data breach, shared in threat intelligence reports.
- ****Indicators of Attack (IOAs)**:** Focus on the behavior and tactics of attackers, providing insights into their methods and objectives.

### Types of IOCs

- ****Atomic IOCs****: Specific artifacts left on a system post-intrusion, such as file hashes, IP addresses, and filenames.
- ****Behavioral IOCs****: Traits and behaviors indicative of malicious activity, including network traffic patterns and registry activities.
- ****Detection****: Identifying IOCs is crucial for confirming system compromises and proactively defending assets.

![12](/Course-Notes/.assets/Pasted_image_20241202220726.png)
### The Pyramid of Pain

- David Bianco's Pyramid of Pain illustrates the varying effectiveness of IOCs in threat investigations.
- At the base are less effective atomic IOCs, while the apex includes adversary Tactics, Techniques, and Procedures (TTPs), which are harder for attackers to change.
- Focusing on TTPs provides deeper insights into adversary behavior and enhances detection capabilities.

![11](/Course-Notes/.assets/Pasted_image_20241202220734.png)
# Challenges and Limitations of IOCs

### Limitations of IOCs

- IOCs can lead to false positives, especially when relying on outdated or unreliable indicators.
- They are not effective against zero-day threats or morphing malware, as they depend on known signatures.
- Continuous research and updates are necessary to maintain the relevance of IOCs in threat detection.

### Categories of IOCs

- **Email Indicators**: Include sender addresses, email subjects, attachments, and links used in phishing attempts.
- **Network Indicators**: URLs, domain names, and IP addresses that signal command and control activities.
- **Endpoint Indicators**: Artifacts found on user devices, such as filenames, file hashes, and registry keys.

![10](/Course-Notes/.assets/Pasted_image_20241202220749.png)
# Understanding Indicators of Compromise (IOCs)

### Definition and Importance of IOCs

- IOCs are artifacts observed on a network or in operating system files that indicate a potential intrusion or compromise. They serve as critical tools for identifying and responding to cyber threats.
- Common types of IOCs include file hashes, IP addresses, domain names, and registry keys, which help in detecting malicious activities.
- IOCs are essential for threat hunting, allowing security teams to proactively search for signs of compromise within their environments.
- They provide a basis for forensic investigations, helping teams trace back the actions of attackers and understand the methods used in an attack.
- IOCs can be shared among organizations to enhance collective defense against cyber threats, making them a vital component of threat intelligence.
- The effectiveness of IOCs can vary, with some being more prone to false positives than others, necessitating careful evaluation.

### Behavioral Indicators of Malicious Activities

- Behavioral indicators are specific events that suggest malicious activities, such as code injection or abnormal use of system services, often referred to as Living off the Land (LotL).
- Examples of behavioral indicators include executing PowerShell scripts, running remote commands, and modifying registry keys.
- These indicators help in identifying sophisticated attacks that leverage legitimate tools and processes to evade detection.
- Understanding behavioral indicators is crucial for developing effective detection strategies and improving incident response.
- Security teams must continuously monitor for these indicators to adapt to evolving threat landscapes.
- Case studies of successful detections using behavioral indicators highlight their importance in modern cybersecurity practices.

### Types and Effectiveness of IOCs

- IOCs can be ranked based on their effectiveness and susceptibility to false positives, with file hashes being the most reliable and IP addresses being the least.
- The ranking of IOCs is as follows: 1) File hashes, 2) URLs, 3) Domain names, 4) Registry keys, 5) IP addresses.
- File hashes are unique identifiers for files, making them highly effective for detecting known malware.
- URLs and domain names can indicate malicious web activity but may lead to false positives due to legitimate use.
- Registry keys can signal changes made by malware but require context to assess their significance accurately.
- IP addresses are often dynamic and can change, making them less reliable as indicators of compromise.

# Threat Intelligence Formats for Sharing IOCs

### Importance of Standardized Formats

- Standardized formats for sharing threat intelligence are crucial for effective communication and collaboration among organizations.
- They enable the consistent representation of IOCs, making it easier for security teams to understand and respond to threats.
- Using standardized formats allows for automated sharing of threat intelligence, enhancing the speed and efficiency of threat detection.
- Organizations can better anticipate and respond to attacks by leveraging shared threat intelligence in a structured manner.
- The adoption of standardized formats fosters a collaborative security community, improving overall cybersecurity posture.
- Examples of standardized formats include Open IOC, CybOX, STIX, and TAXII, each serving specific purposes in threat intelligence sharing.

![9](/Course-Notes/.assets/Pasted_image_20241202220831.png)
### Overview of Threat Intelligence Formats

- **Open Indicator of Compromise (Open IOC):** Utilizes XML to describe indicators with predefined terms, allowing for complex definitions using Boolean logic.
- **Cyber Observable Expression (CybOX):** A standard for defining observable events and properties, facilitating automated sharing of security information.
- **Structured Threat Information eXpression (STIX):** A structured language using XML or JSON to define threats, widely used for its comprehensive object definitions.
- **Trusted Automated eXchange of Indicator Information (TAXII):** A transport protocol for sharing CTI over HTTPS, designed to work with STIX.
- Each format has its strengths, with STIX being the most popular among security analysts for its detailed threat context.
- The collaboration between organizations like MITRE and Oasis has led to the development of these formats, ensuring they meet industry needs.
![8](/Course-Notes/.assets/Pasted_image_20241202220852.png)
![7](/Course-Notes/.assets/Pasted_image_20241202221039.png)
# Advantages and Limitations of IOCs

![6](/Course-Notes/.assets/Pasted_image_20241202221049.png)
### Advantages of Using IOCs

- IOCs facilitate proactive threat sharing among organizations, enhancing collective defense against cyber threats.
- They are vital for threat hunting, enabling SOC analysts to identify stealthy threats that may evade traditional security measures.
- Forensics teams utilize IOCs to trace attacker activities and gather evidence during investigations.
- IOCs can improve incident response times by providing clear indicators of compromise that teams can act upon quickly.
- The ability to share IOCs across platforms and organizations enhances situational awareness and threat intelligence.
- IOCs can be integrated into security tools and SIEM solutions for automated detection and response.

![5](/Course-Notes/.assets/Pasted_image_20241202221104.png)
### Limitations of IOCs

- IOCs are static and primarily identify known threats, making them less effective against new or modified attacks.
- The open nature of IOC sharing can lead to the proliferation of low-quality or irrelevant indicators, requiring skilled analysts to validate their applicability.
- There is a lack of consensus on how to document and report IOCs, leading to inconsistencies in threat intelligence sharing.
- IOCs may not provide context about the threat, limiting their effectiveness in understanding the broader attack landscape.
- Over-reliance on IOCs can lead to complacency, as organizations may overlook other critical security measures.
- Continuous updates and maintenance of IOC databases are necessary to ensure their relevance and effectiveness.

# Understanding Indicators of Compromise (IOCs) and Indicators of Attack (IOAs)

### Definition and Importance of IOCs

- IOCs are artifacts observed on a network or in operating system files that indicate a potential intrusion. They are crucial for identifying and responding to security incidents.
- IOCs can include IP addresses, domain names, URLs, file hashes, and other data points that signify malicious activity.
- The effectiveness of IOCs is contingent upon their timely identification and accurate documentation, which often requires skilled analysts.
- IOCs are often transitory, meaning their relevance diminishes over time as threats evolve, necessitating continuous updates and validation.
- A lack of consensus on how to document and report IOCs can lead to inconsistencies in threat intelligence sharing among organizations.
- Case studies, such as the Target data breach, highlight the importance of IOCs in identifying and mitigating threats.

### Definition and Role of IOAs

- IOAs are indicators that help detect the behavior and intentions of adversaries during an attack, focusing on the actions taken rather than just the artifacts left behind.
- Unlike IOCs, IOAs provide early warning signs of potential intrusions, allowing for proactive defense measures.
- IOAs require a baseline of normal activity to distinguish between legitimate and suspicious behavior, making context crucial for their effectiveness.
- Examples of IOA activities include unusual network scans, simultaneous logins from different locations, and non-privileged users executing administrative commands.
- IOAs can generate more false positives than IOCs, necessitating thorough investigation and analysis.
- The dynamic nature of IOAs makes them valuable for real-time threat detection and response.

### Comparison of IOCs and IOAs

| Aspect          | IOCs                                       | IOAs                                |
| --------------- | ------------------------------------------ | ----------------------------------- |
| Definition      | Artifacts indicating a potential intrusion | Behavioral indicators of an attack  |
| Purpose         | Identify and respond to incidents          | Detect ongoing or potential attacks |
| Context         | Static and often historical                | Dynamic and context-dependent       |
| False Positives | Generally lower                            | Generally higher                    |
| Examples        | IP addresses, file hashes                  | Network scans, unusual logins       |
| Usage           | Post-incident analysis                     | Real-time monitoring and detection  |

# Cyber Threat Intelligence Lifecycle

### Overview of the CTI Lifecycle

- The CTI lifecycle is a structured process that transforms raw data into actionable intelligence for decision-making by security teams.
- It consists of eight iterative phases that guide CTI teams in optimizing resources and responding to threats effectively.
- Each phase builds upon the previous one, ensuring a comprehensive approach to threat intelligence.
- The lifecycle emphasizes the importance of collaboration and information sharing among security professionals.
- Historical context: The evolution of threat intelligence has led to the establishment of formalized processes like the CTI lifecycle to address growing cybersecurity challenges.
- Case studies, such as the WannaCry ransomware attack, illustrate the need for a robust CTI lifecycle to mitigate threats.

![4](/Course-Notes/.assets/Pasted_image_20241202221122.png)
### Phases of the CTI Lifecycle

1. ****Planning and Preparation:**** Establishes objectives and methodologies for the CTI operation, including identifying adversaries and their motivations.
2. ****Collecting and Gathering:**** Involves gathering information from various sources, such as threat feeds and blogs, to build a comprehensive understanding of threats.
3. ****Sorting and Processing:**** Organizes collected data into manageable formats, facilitating analysis and inspection of IOCs and IOAs.
4. ****Vetting and Validation:**** Ensures the accuracy of collected indicators by cross-checking against multiple sources to reduce false positives.
5. ****Sensitivity and Prioritization:**** Assigns sensitivity levels to IOCs using the Traffic Light Protocol (TLP) to control information sharing and protect sensitive data.
6. ****Analysis and Production:**** Involves analyzing the validated indicators to produce actionable intelligence for stakeholders.
7. ****Dissemination:**** Shares the produced intelligence with relevant parties while adhering to the established sensitivity levels.
8. ****Feedback and Review:**** Collects feedback on the intelligence provided to improve future CTI operations and refine processes.
# Traffic Light Protocol (TLP) in CTI

### Understanding TLP

- The Traffic Light Protocol (TLP) is a system used to classify the sensitivity of information shared within the threat intelligence community.
- TLP uses four colors (Red, Amber, Green, White) to indicate the level of sharing and the audience for the information.
- Each color has specific guidelines on how and with whom the information can be shared, ensuring appropriate handling of sensitive data.
- TLP helps organizations ==manage the risk associated with sharing threat intelligence while promoting collaboration.==
- Historical context: TLP was developed to address the challenges of information sharing in the cybersecurity community, particularly after high-profile breaches.
- Examples of TLP usage include sharing threat intelligence reports during security conferences or within industry-specific groups.

### TLP Color Codes and Their Implications

| TLP Color | Description                                                               | Sharing Guidelines                                                       |
| --------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Red       | Information not intended for disclosure; restricted to participants only. | Must not be shared outside the specific exchange or meeting.             |
| Amber     | Limited disclosure; restricted to participants' organizations.            | Can be shared within the organization and with clients who need to know. |
| Green     | Limited disclosure; restricted to the community.                          | Can be shared with peers within the sector but not publicly.             |
| White     | Unlimited disclosure; information can be shared freely.                   | Can be shared with anyone without restrictions.                          |

# Understanding White TLP and Threat Prioritization

### White TLP Overview

- The White TLP (Traffic Light Protocol) is assigned to data that has unlimited disclosure, meaning it can be shared freely without restrictions.
- An example of White TLP information includes data that poses minimal or no foreseeable risk of misuse, such as public safety announcements or general security awareness tips.
- Organizations must follow applicable rules and procedures for public release to ensure compliance and protect sensitive information.

### Threat Prioritization Process

- The CTI team prioritizes Indicators of Compromise (IOCs) based on recent intelligence, focusing on the most relevant threats.
- Recent intelligence blogs serve as a resource for identifying current threats, allowing the team to make informed decisions on which IOCs to implement.
- For instance, prioritizing IOCs from a recent malware campaign over older ones reflects a proactive approach to threat hunting.

# Analyzing, Reporting, and Feedback in CTI

### Analyzing and Assessment Phase

- The CTI team analyzes and evaluates data to answer questions posed during the planning phase, transforming data into actionable insights.
- This phase involves identifying patterns, trends, and anomalies in the data that could indicate potential threats.
- The findings are compiled into an intelligence report, which serves as a basis for decision-making and strategic planning.

### Reporting and Dissemination

- In the final phase, the CTI team formats their intelligence for dissemination to relevant stakeholders, including upper management and other teams.
- Reports may vary in format, from one-page summaries to detailed slide decks, depending on the audience's needs.
- Effective communication of intelligence findings is crucial for ensuring that stakeholders understand the implications and recommended actions.

### Feedback and Evaluation

- The CTI team collects feedback from stakeholders on their reports to ensure relevance and value.
- Continuous dialogue between the CTI team and consumers helps identify gaps in intelligence and improve future operations.
- Regular evaluations of the CTI process contribute to refining methodologies and enhancing overall effectiveness.

# CTI Objects and Their Applications

![3](/Course-Notes/.assets/Pasted_image_20241202221136.png)
### Purpose of CTI

- Security teams utilize CTI to meet various objectives, including threat detection, prevention, and response.
- Threat intelligence is delivered in multiple formats, such as security intelligence lists for firewalls and other security appliances.
- Examples of CTI applications include IP blocking lists, URL blocking lists, and domain name blocking lists, which help prevent malicious activities.

### Real-World Implementation of CTI

- The Cisco Secure Firewall Threat Intelligence Director (TID) feature exemplifies the integration of threat intelligence into security systems.
- TID publishes threat intelligence data into managed Cisco Secure Firewall devices, enhancing their defensive capabilities.
- The system ingests and normalizes third-party CTI data, allowing for automated responses to threats based on updated feeds.

# Key Components of Actionable Threat Intelligence

![2](/Course-Notes/.assets/Pasted_image_20241202221301.png)
### Importance of Data and Analysis

- Historical threat data, machine learning, and cyber threat analysis are critical components for actionable threat intelligence.
- Efficient and reliable information is essential for threat intelligence teams to produce accurate outcomes and insights.
- The increasing volume of threat data necessitates the use of advanced technologies like machine learning to process information quickly.

### Evolving Threat Landscape

- Reactive security systems are insufficient; organizations must adopt proactive measures to anticipate and respond to future threats.
- Advanced threat management solutions, such as Cisco SecureX, enable organizations to manage multiple threats simultaneously and automate responses.
- Continuous adaptation to the evolving threat landscape is crucial for maintaining effective cybersecurity defenses.

# Threat Intelligence Platforms (TIPs)

### Functionality of TIPs

- Threat Intelligence Platforms (TIPs) operationalize and automate the aggregation of threat intelligence from various sources.
- MISP (Malware Information Sharing Platform) is a leading open-source TIP that assists SOC analysts in sharing threat intelligence on malware attacks.
- TIPs serve as a workbench for analysts, allowing them to collect, manage, and investigate threat indicators efficiently.

### Integration and Impact of TIPs

- TIPs integrate with other security products via APIs, reducing the investigative workload for analysts.
- By sharing threat intelligence data with SIEMs and SOAR solutions, TIPs enhance the overall security posture of organizations.
- Management and leadership benefit from TIPs by gaining insights into critical threats and their potential impacts on the organization.

![1](/Course-Notes/.assets/Pasted_image_20241202221323.png)