%% #review  %%
# [[Cyber Threat Intelligence]]


## Key Types of Threat Intelligence

| Type            | Description                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| **Strategic**   | ==High-level information for business decision-makers==, including adversary trends and financial impacts. |
| **Tactical**    | ==Technical information related to adversary TTPs.==                                                       |
| **Operational** | Focuses on ==specific threats or attack campaigns==, often used by government organizations.               |
| **Technical**   | Detailed ==technical information about tools and resources== used by adversaries in attacks.               |
## Key Threat Intelligence Formats

|Format|Description|
|---|---|
|**Open Indicator of Compromise**|XML-based format for describing indicators with predefined terms.|
|**Cyber Observable Expression**|Standard for defining measurable events and properties for automated sharing of security information.|
|**Structured Threat Information eXpression (STIX)**|Structured language for defining threats and their context, widely used in CTI.|
|**Trusted Automated eXchange of Indicator Information (TAXII)**|Protocol for sharing CTI over HTTPS, designed to support STIX data exchange.|
## IOC vs IOA

|Concept|Indicators of Compromise (IOCs)|Indicators of Attack (IOAs)|
|---|---|---|
|Definition|Artifacts indicating evidence of an intrusion or breach|Early warning signs of an intrusion or attack|
|Purpose|Confirm malicious activity|Detect potential attacks in progress|
|Nature|Static and known threats|Dynamic and contextual, based on normal activity|
|Examples|File hashes, IP addresses, email indicators|Network scans, unusual logins, abnormal commands|
- **Indicators of Compromise (IOCs)**: Digital forensic artifacts indicating evidence of an intrusion or data breach, used to detect malicious activity.
- **Indicators of Attack (IOAs)**: Early warning signs of an intrusion or attack, focusing on the actions an adversary must perform for an attack to succeed.
## The Pyramid of Pain

![11](/Course-Notes/.assets/Pasted_image_20241202220734.png)

| Indicator Type      | Description                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| Email Indicators    | Sender addresses, email subjects, attachments, and links used in phishing attempts. |
| Network Indicators  | URLs, domain names, and IP addresses that signal command and control activities.    |
| Endpoint Indicators | Artifacts found on user devices, such as filenames, file hashes, and registry keys. |
![10](/Course-Notes/.assets/Pasted_image_20241202220831.png)

| Format                                                      | Description                                                               | Strengths                                           |
| ----------------------------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------- |
| Open Indicator of Compromise (Open IOC)                     | Uses XML with predefined terms and Boolean logic for complex definitions. | Flexible and expressive.                            |
| Cyber Observable Expression (CybOX)                         | A standard for defining observable events and properties.                 | Automated sharing of security information.          |
| Structured Threat Information eXpression (STIX)             | A structured language using XML or JSON for defining threats.             | Comprehensive object definitions and wide adoption. |
| Trusted Automated eXchange of Indicator Information (TAXII) | A transport protocol for sharing CTI over HTTPS, designed for STIX.       | Secure and standardized transport for CTI.          |

| Advantages of Using IOCs                                                                                                            | Limitations of IOCs                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IOCs facilitate proactive threat sharing among organizations, enhancing collective defense against cyber threats.                   | IOCs are static and primarily identify known threats, making them less effective against new or modified attacks.                                                 |
| They are vital for threat hunting, enabling SOC analysts to identify stealthy threats that may evade traditional security measures. | The open nature of IOC sharing can lead to the proliferation of low-quality or irrelevant indicators, requiring skilled analysts to validate their applicability. |
| Forensics teams utilize IOCs to trace attacker activities and gather evidence during investigations.                                | There is a lack of consensus on how to document and report IOCs, leading to inconsistencies in threat intelligence sharing.                                       |
| IOCs can improve incident response times by providing clear indicators of compromise that teams can act upon quickly.               | IOCs may not provide context about the threat, limiting their effectiveness in understanding the broader attack landscape.                                        |
| The ability to share IOCs across platforms and organizations enhances situational awareness and threat intelligence.                | Over-reliance on IOCs can lead to complacency, as organizations may overlook other critical security measures.                                                    |
| IOCs can be integrated into security tools and SIEM solutions for automated detection and response.                                 | Continuous updates and maintenance of IOC databases are necessary to ensure their relevance and effectiveness.                                                    |
## IOA

| Feature             | Description                                                                                                                                                                                        |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Definition          | Indicators of Attack (IOAs) are indicators that help detect the behavior and intentions of adversaries during an attack, focusing on the actions taken rather than just the artifacts left behind. |
| Purpose             | Unlike IOCs, IOAs provide early warning signs of potential intrusions, allowing for proactive defense measures.                                                                                    |
| Detection Mechanism | IOAs require a baseline of normal activity to distinguish between legitimate and suspicious behavior, making context crucial for their effectiveness.                                              |
| Examples            | Examples of IOA activities include unusual network scans, simultaneous logins from different locations, and non-privileged users executing administrative commands.                                |
| Challenges          | IOAs can generate more false positives than IOCs, necessitating thorough investigation and analysis.                                                                                               |
| Value               | The dynamic nature of IOAs makes them valuable for real-time threat detection and response.                                                                                                        |
## CTI Lifecycle

| Step                           | Description                                                                                                                             |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Planning and Preparation       | Establishes objectives and methodologies for the CTI operation, including identifying adversaries and their motivations.                |
| Collecting and Gathering       | Involves gathering information from various sources, such as threat feeds and blogs, to build a comprehensive understanding of threats. |
| Sorting and Processing         | Organizes collected data into manageable formats, facilitating analysis and inspection of IOCs and IOAs.                                |
| Vetting and Validation         | Ensures the accuracy of collected indicators by cross-checking against multiple sources to reduce false positives.                      |
| Sensitivity and Prioritization | Assigns sensitivity levels to IOCs using the Traffic Light Protocol (TLP) to control information sharing and protect sensitive data.    |
| Analysis and Production        | Involves analyzing the validated indicators to produce actionable intelligence for stakeholders.                                        |
| Dissemination                  | Shares the produced intelligence with relevant parties while adhering to the established sensitivity levels.                            |
| Feedback and Review            | Collects feedback on the intelligence provided to improve future CTI operations and refine processes.                                   |
![9](/Course-Notes/.assets/Pasted_image_20241202221122.png)

## Traffic Light Protocol (TLP) in CTI


| TLP Color | Description                                                               | Sharing Guidelines                                                       |
| --------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Red       | Information not intended for disclosure; restricted to participants only. | Must not be shared outside the specific exchange or meeting.             |
| Amber     | Limited disclosure; restricted to participants' organizations.            | Can be shared within the organization and with clients who need to know. |
| Green     | Limited disclosure; restricted to the community.                          | Can be shared with peers within the sector but not publicly.             |
| White     | Unlimited disclosure; information can be shared freely.                   | Can be shared with anyone without restrictions.                          |
## CTI Objects and Their Applications

| Purpose of CTI                                                                                                                                       | Real-World Implementation of CTI                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Security teams utilize CTI to meet various objectives, including threat detection, prevention, and response.                                         | The Cisco Secure Firewall Threat Intelligence Director (TID) feature exemplifies the integration of threat intelligence into security systems. |
| Threat intelligence is delivered in multiple formats, such as security intelligence lists for firewalls and other security appliances.               | TID publishes threat intelligence data into managed Cisco Secure Firewall devices, enhancing their defensive capabilities.                     |
| Examples of CTI applications include IP blocking lists, URL blocking lists, and domain name blocking lists, which help prevent malicious activities. | The system ingests and normalizes third-party CTI data, allowing for automated responses to threats based on updated feeds.                    |
![8](/Course-Notes/.assets/Pasted_image_20241202221136.png)

## Threat Intelligence Platforms (TIPs)

| Functionality of TIPs                                                                                                                                 | Integration and Impact of TIPs                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Threat Intelligence Platforms (TIPs) operationalize and automate the aggregation of threat intelligence from various sources.                         | TIPs integrate with other security products via APIs, reducing the investigative workload for analysts.                                |
| MISP (Malware Information Sharing Platform) is a leading open-source TIP that assists SOC analysts in sharing threat intelligence on malware attacks. | By sharing threat intelligence data with SIEMs and SOAR solutions, TIPs enhance the overall security posture of organizations.         |
| TIPs serve as a workbench for analysts, allowing them to collect, manage, and investigate threat indicators efficiently.                              | Management and leadership benefit from TIPs by gaining insights into critical threats and their potential impacts on the organization. |
![7](/Course-Notes/.assets/Pasted_image_20241202221323.png)

# [[Open-Source Intelligence]]

Key Techniques

|Technique|Description|
|---|---|
|**Domain Name Technique**|Uses domain names to gather information about IP addresses, registrant details, and related domains.|
|**IP Address Technique**|Involves using IP addresses to find associated domain names, organization details, and vulnerabilities.|
|**Email Technique**|Gathers information about email addresses, including validity, breaches, and associated personal data.|
|**Username Technique**|Searches for usernames across platforms to find social media accounts and related information.|
|**Real Name Technique**|Uses real names to find personal details, social profiles, and connections to other individuals.|
Problem-Solving Steps

1. Define your objective: Determine what information you need and why.
2. Identify seed data: Use known data points (like usernames or domain names) as starting points.
3. Choose appropriate tools: Select OSINT tools based on the type of data you are collecting.
4. Collect data: Use the tools to gather information, ensuring to document your sources.
5. Analyze and interpret: Process the collected data to extract actionable intelligence.
6. Validate findings: Cross-reference information to ensure accuracy and reliability.

### OSINT Data Sources
![6](/Course-Notes/.assets/Pasted_image_20241202225001.png)

| Category                         | Description                                                                                                             | Examples                                                                                                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary Sources                  | The internet serves as the primary source of OSINT, providing a wealth of information beyond traditional media.         | Social networks (e.g., Facebook, Twitter), media-sharing sites (e.g., YouTube), professional networks (e.g., LinkedIn), academic and government websites |
| Deep Web and Dark Web            | The deep web consists of non-indexed content that requires special access, such as databases and subscription services. | The dark web, a subset of the deep web, allows for anonymous exchanges and can contain sensitive information.                                            |
| Legal and Ethical Considerations | Accessing OSINT must comply with legal regulations and ethical standards, especially when dealing with sensitive data.  | The use of SOCMINT (social media intelligence) raises additional ethical concerns due to the nature of social media data.                                |

# OSINT Application
![5](/Course-Notes/.assets/Pasted_image_20241202225025.png)
>OSINT refers to the collection and analysis of publicly available data to support decision-making in cybersecurity.

- Does not require special permissions or techniques to access.
- Anything publicly available.

| Advantages of OSINT                                                                                                                                              | Challenges and Limitations of OSINT                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| The OSINT market is projected to grow significantly, providing organizations with a greater return on investment compared to other intelligence-gathering tools. | The reliability of OSINT data can be questionable, as many sources may contain subjective or fabricated information.                               |
| A wide variety of data types are available, from simple data points like IP addresses to complex multimedia items, enhancing investigative capabilities.         | The prevalence of synthetic media, such as fake news and deepfakes, undermines the credibility of open-source data.                                |
| Advanced data processing techniques, including machine learning and AI, improve the quality of results derived from OSINT.                                       | Public availability of OSINT means that both investigators and threat actors have equal access to the same information, raising security concerns. |
### [OSINT Framework](https://osintframework.com/)

![4](/Course-Notes/.assets/Pasted_image_20241202225044.png)![3](/Course-Notes/.assets/Pasted_image_20241202225058.png)


- The OSINT framework is a repository of tools categorized by technique, source, or purpose, facilitating open-source data collection.
- Common tools include search engines and specialized applications for specific data types, such as email addresses or usernames.
- The framework provides an interactive interface for browsing tools, with indicators for installation and registration requirements.

## OSINT Tools

- Tools for username searches include Namechk, KnowEm, and WhatsMyName, each with specific usage requirements.
- Domain name investigation tools include Mnemonic and DNS History, which help in tracking domain-related information.
- The organization of tools within the OSINT framework aids in systematic investigations, promoting creativity in data collection tasks.

![2](/Course-Notes/.assets/Pasted_image_20241202225107.png)

Active Vs Passive

| Collection Type | Description                                                                                   | Implications                                                          | Preference                                                    |
| --------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------- |
| Passive         | Gathers data without direct interaction, often using third-party sources.                     | Limited data quality and quantity, potential for detection.           | May be preferred for certain scenarios.                       |
| Active          | Requires direct engagement with the target, potentially exposing the investigator’s identity. | Potential for detection and countermeasures, higher risk of exposure. | Often preferred for sensitive data by security professionals. |

# [[OSINT Use Case]]

Key Steps in Threat Investigation

|Step|Description|
|---|---|
|1|Research the suspicious URL to determine if it is associated with known malware.|
|2|Use services like VirusTotal to check the reputation of the URL and gather additional context.|
|3|Confirm findings with other databases, such as URLhaus, to validate the URL's malicious nature.|
|4|Conduct a Google exact-match search for the URL to find articles and resources related to it.|
|5|Investigate the malware associated with the URL for actionable intelligence, such as IOCs (Indicators of Compromise).|
Problem-Solving Steps

1. **Identify the alert**: Start with the suspicious URL provided in the alert.
2. **Check URL reputation**: Use VirusTotal to assess the URL's reputation score.
3. **Cross-reference findings**: Consult URLhaus for additional context on the URL's use in malware.
4. **Conduct a Google search**: Perform an exact-match search for the URL to find articles or reports.
5. **Investigate malware**: Use the information gathered to identify the malware associated with the URL.
6. **Collect IOCs**: Gather IOCs and signatures related to the malware for detection purposes.
7. **Escalate findings**: Compile all findings and escalate the alert to the Incident Response team.

Facts to Memorize

- URL reputation services are essential for identifying malicious domains.
- VirusTotal is a key resource for checking URL and file reputations.
- URLhaus provides information on malware downloads and associated hashes.
- Community reports can provide valuable insights into malware behavior and IOCs.

![1](/Course-Notes/.assets/Pasted_image_20241202225448.png)

### Initial Alert Triage

- Upon receiving an alert about suspicious traffic to a C2 (Command and Control) domain, the analyst begins the investigation.
- The first step is to gather the URL associated with the alert, e.g., `http://72.X.Y.Z/[malicious_script].bat`.
- Analysts should utilize URL reputation services to assess the URL's safety and gather additional context.
- Tools like VirusTotal can provide a reputation score and community feedback on the URL.
- Keeping browser tabs open for multiple sources allows for cross-referencing information.

### Utilizing OSINT Tools

- ****VirusTotal****: Submit the suspicious URL to check for malicious indicators and community reports.
- ****URLhaus****: This database provides information on URLs used for malware distribution, including associated malware hashes.
- ****Google Search****: Conduct an exact-match search for the URL to find articles and resources that discuss the threat.
- Analysts should document findings from each tool to build a comprehensive view of the threat.
- Cross-referencing multiple sources helps confirm the malicious nature of the URL.

### Identifying Associated Malware

- After confirming the URL is malicious, the next step is to identify the specific malware involved.
- Analysts can revisit the VirusTotal Community tab for user comments and reports related to the URL.
- Community feedback may include references to well-known security reports, such as those from Rapid7.
- Gathering information about the malware can lead to actionable intelligence, including IOCs (Indicators of Compromise) and signatures.
- Understanding the malware's behavior is crucial for developing detection and response strategies.

### Gathering Additional Evidence

- Analysts should look up the CVE (Common Vulnerabilities and Exposures) number associated with the malware for detailed information.
- The MITRE ATT&CK framework and NVD (National Vulnerability Database) are valuable resources for understanding vulnerabilities.
- File hashes from URLhaus can be submitted to reputation services to check for known malicious files.
- Using sandbox environments to analyze the malware can provide insights into its behavior and impact.
- Collecting comprehensive evidence is essential for escalating the alert to the Incident Response (IR) team.

### Confirming the Alert

- After thorough investigation and evidence collection, analysts can confirm whether the alert is a true positive.
- All findings should be documented and presented to the IR team for further action.
- Analysts should ensure that all relevant data, including IOCs and malware signatures, are included in the escalation report.
- Continuous monitoring and follow-up on the incident are necessary to mitigate any potential impact.
- Learning from each investigation helps improve future alert triage processes.
