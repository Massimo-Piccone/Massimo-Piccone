 %% #review %%
# [[SOC Deployment Models and Types]]

## SOC Types and Staffing Considerations

| **SOC Type**              | **Focus**                                                                                                  | **Key Activities**                                                                                                                                                                                                        | **Nickname**                   |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **Threat-Centric SOC**    | Proactively hunts for malicious threats on networks by identifying vulnerabilities and anomalies.          | - Pre-attack: Implement policies, analyze network traffic for defenses. <br> - During attack: Detect and block malware threats. <br> - Post-attack: Marginalize impact, contain threats, remediate infected hosts.        | The Hunters                    |
| **Compliance-Based SOC**  | Focuses on ensuring network systems comply with security standards, configuration templates, and policies. | - Monitors configurations for unauthorized changes and security breaches. <br> - Ensures compliance with standards like CIS and PCI DSS. <br> - Evaluates the organization's security posture.                            | The Guardians / The Enforcers  |
| **Operational-Based SOC** | Internally focused, tasked with monitoring and maintaining the internal network's security posture.        | - Develops and deploys customized detection techniques (e.g., REGEX). <br> - Maintains access control policies, intrusion detection system rules, and firewall configurations. <br> - Monitors internal network security. | The Responders / The Defenders |
## SOC Deployment Models


| **SOC Model**      | **Description**                                 | **Pros**                                                                                                                              | **Cons**                                                                                          | **Cost** |
| ------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| **Internal**       | On-site, fully administered by the organization | - Best visibility <br> - Exclusive data management <br> - Most customizable <br> - Dedicated in-house staff                           | - Most expensive <br> - Most difficult to recruit and retain talent <br> - Slowest implementation | $$$      |
| **Virtual (vSOC)** | Contracted service                              | - Least expensive <br> - Quickest implementation <br> - Most flexible and scalable                                                    | - Least visibility <br> - Third-party data management <br> - Least customizable                   | $        |
| **Hybrid**         | Combination of internal and virtual             | - Quickest detection and response <br> - Most secure (extra pair of eyes) <br> - Knowledge share between internal SOC and third party | - Costly in the long term <br> - Additional hardware required <br> - Third-party data management  | $$       |
# [[Staffing an Effective SOC Team]]

## SOC Roles
NIST 800-181 Rev.1


| SOC Role                                                 | Responsibilities                                                                                          | Key Skills                                                                                             | Focus                                                                                                         |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| SOC Tier 1 Analyst: Triage Specialist                    | Initial triage of alerts from SIEM and ITSM systems.                                                      | Sysadmin knowledge, scripting, cybersecurity certifications (e.g., Cisco CyberOPS Associate, CompTIA). | Determining if alerts require further investigation and escalation.                                           |
| SOC Tier 2 Analyst: Incident Handler                     | In-depth assessment of incidents escalated by Tier 1 analysts.                                            | Deeper analysis, incident management, threat intelligence.                                             | Determining the scope and nature of attacks, developing containment and recovery strategies.                  |
| SOC Tier 3 Analyst: Incident Responder and Threat Hunter | Proactive threat identification, research on new attack techniques, optimizing security monitoring tools. | Extensive network security and data analytics knowledge, familiarity with attack techniques.           | Proactively identifying threats, researching new attack techniques, and optimizing security monitoring tools. |
| SOC Manager                                              | Overseeing the entire SOC team, including hiring, training, and evaluation.                               | Management, incident reporting, crisis communication, financial oversight, security audits.            | Managing the SOC team, incident reports, crisis communication, financial aspects, and supporting audits.      |

## SOC Tools

| Tool Category                                        | Tool Example                           | Key Features                                | Benefits                                                   | Best Practices                                                                      |
| ---------------------------------------------------- | -------------------------------------- | ------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| IT Service Management (ITSM)                         | ServiceNow                             | Automated workflows for incident management | Streamlined incident response, improved efficiency         | Integrate incident data from various security tools                                 |
| Security Information and Event Management (SIEM)     | Splunk                                 | Real-time monitoring, AI/ML-driven UEBA     | Timely incident detection, comprehensive threat visibility | Aggregate logs from multiple sources for holistic security insights                 |
| Intrusion Detection and Prevention Systems (IDS/IPS) | Cisco Firepower 4100 Series (NIDS/IPS) | Network traffic monitoring, threat blocking | Reduced detection time, proactive threat mitigation        | Understand the differences between NIDS and HIDS for effective deployment           |
| Vulnerability Scanners                               | Nessus                                 | Assessment of systems for known weaknesses  | Identification and remediation of security gaps            | Regular assessments, prioritization of vulnerabilities based on risk                |
| Threat Intelligence Services                         | Cisco Talos                            | Real-time threat data, actionable insights  | Improved incident response, enhanced security strategies   | Integrate threat intelligence into SIEMs for enriched context during investigations |
## Before, During, and After Incidents
NICE workforce framework categories: Investigate, Collect and Operate, Analyze

| Incident Phases | Activities                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Before Incident | Monitor alerts via ITSM ticketing system (SOC Tier 1 Triage Specialist) Focus on threat intelligence feeds, e.g., Cisco Talos (Threat Hunter)                                                                                                                                                                                                                                                                                                                                          |
| During Incident | Shift focus to incident response Utilize available tools and coordinate with stakeholders (e.g., NOC, system owners, data owners)                                                                                                                                                                                                                                                                                                                                                      |
| After Incident  | Begin recovery phase Collaborate with the legal department to document procedures for court proceedings Create detailed reports on findings and lessons learned Use forensic applications (e.g., Encase, Velociraptor, Redline) to collect, analyze, and report data Ensure legal compliance in preparation for potential court procedures Consider SOC 2 audit report for organizational and legal compliance Generate multiple reports for future SOC incident response improvements |

### Incident Management Process

| Incident Management Process                                                                                             | Incident Response Phases                                                                                          | Roles and Responsibilities in the SOC                                                                                          | Stakeholder Interaction During Incidents                                                                               |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| The SOC analyst’s role shifts from monitoring to incident response when an incident occurs, requiring immediate action. | Coordination with stakeholders, including NOC and legal teams, is critical for effective incident management.     | SOC teams are structured into tiers, each with specific responsibilities to ensure efficient incident management.              | The SOC must maintain open lines of communication with internal stakeholders, including IT, HR, and legal departments. |
| The recovery phase involves documenting procedures and findings to ensure compliance and improve future responses.      | Forensic tools like Encase and Velociraptor are used to analyze incidents and gather evidence for legal purposes. | Tier 1 analysts monitor alerts and perform initial triage, determining if further investigation is needed.                     | External communication may involve legal entities, media, and government organizations like US-CERT/CISA.              |
| Post-incident reports are essential for capturing lessons learned and refining incident response strategies.            | Clear communication among team members and with stakeholders is vital for successful incident resolution.         | Tier 2 analysts conduct deeper analysis, correlating data from multiple sources to assess impact and guide remediation.        | Building strong relationships with stakeholders enhances collaboration and improves incident outcomes.                 |
| Regular training and simulations can prepare the SOC for real-world incident scenarios.                                 |                                                                                                                   | Tier 3 analysts possess advanced technical skills and proactively hunt for threats, enhancing the SOC’s overall effectiveness. | Regular training and simulations can prepare the SOC for real-world incident scenarios.                                |

### Roles and Responsabilities

| SOC Tier    | Responsibilities                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tier 1      | - Monitors the alert queue continuously<br><br>- Triages security alerts.<br><br>- Monitors the health of the security sensors and endpoints<br><br>- Collects data and context necessary to initiate Tier 2 work                                                                                                                                                                                                         |
| Tier 2      | - Performs deep-dive incident analysis by correlating data from various sources<br><br>- Determines if a critical system or data set has been impacted.<br><br>- Provides guidance on remediation.<br><br>- Provides support for new analytic methods for use in threat detection                                                                                                                                         |
| Tier 3      | - Applies in-depth technical knowledge about the network, endpoint, threat intelligence, forensics, malware reverse engineering, and the functioning of specific applications or underlying IT infrastructure<br><br>- Acts as an advanced security analyst and proactive threat hunter who doesn’t wait for escalated incidents<br><br>- Participates in developing, tuning, and implementing threat detection analytics |
| SOC Manager | Communicates pertinent information to multiple parties.<br><br>- CIO and CISO<br><br>- Legal department, HR department, The company workforce,<br><br>- Public affairs if the incident may generate publicity,<br><br>- Law enforcement if appropriate.                                                                                                                                                                   |

## Interaction of Various Roles Within the SOC
Concept Comparisons

|SOC Role|Responsibilities|Skills Required|
|---|---|---|
|Tier 1 Analyst|Initial triage of alerts, monitoring health of security sensors and endpoints|Basic networking, traffic capture, device monitoring|
|Tier 2 Analyst|In-depth incident analysis, determining attack scope, remediation strategies|Broader skill set, data analysis, incident handling|
|Tier 3 Analyst|Proactive threat hunting, advanced incident response, threat intelligence research|Advanced network security, forensics, malware analysis|
|SOC Manager|Managing team, incident report assessment, crisis communication|Leadership, communication, incident management|

# [[Security Event Data and SOC Analyst Tools]]

## Network Security Monitoring Data Types

| Data Type               | Description                                                                      | Notes                                                            |
| ----------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Session Data**        | ==Summarized conversation== between two endpoint devices.                        | Similar to analyzing a phone bill for investigative purposes.    |
| **Full Packet Capture** | Complete ==account of all data== exchanged between devices.                      | Large storage requirements and tedious to analyze.               |
| **Transaction Data**    | Highlights operations ==resulting from network sessions== and system activities. | Found in log files, not directly tied to session data.           |
| **Extracted Content**   | ==Artifacts== mined from network traffic.                                        | Includes session data, DNS requests, host information, and more. |
| **Statistical Data**    | Aggregates other security monitoring data types.                                 | Used to ==baseline network== traffic activity.                   |
| **Alert Data**          | Generally produced by ==IDS or IPS== systems.                                    | Often contains false positives and false negatives.              |
| **External Data**       | ==Threat intelligence feeds== and indicators of compromise (IoCs).               | Used to keep threat detection systems up-to-date.                |
## SOC Tools and Their Features
A SOC relies on a supporting infrastructure of tools and systems that provide the following services:

- Network mapping
- Network monitoring
- Vulnerability detection
- Penetration testing
- Data collection
- Threat and anomaly detection
- Data aggregation and correlation
### Security Onion

Linux distro intended to support SOC analysts with a suite of tools for network security monitoring, including intrusion detection, network security monitoring, and log management to to provide four core network security-monitoring functions:
- Full packet capture
- Network-based and host-based intrusion detection sensors
- Security analysis tools
- Log management
#### **Enterprise Log Search and Archive** (ELSA) 
Version of Security Onion is composed of the following tools:

| **SO Tools**                    | Description                                                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ELSA searchEngine**           | Centralized syslog framework built on Syslog-NG, MySQL, and Sphinx full-text search. Provides a web-based query interface for ==log normalization and searching.==                                                                               |
| **Snort NIDS**                  | Open source, ==rules-driven== network intrusion detection system (==NIDS==) and network intrusion prevention system (==NIPS==) developed by Cisco (Sourcefire). Performs real-time threat detection and generates alerts.                        |
| **Suricata NIPS**               | ==Script-driven NIDS and NIPS== threat detection engine for analyzing traffic and generating alerts. NIPS inline mode is not supported within Security Onion.                                                                                    |
| **Zeek traffic analyzer (Bro)** | ==Packet recorder and protocol parsing engine== for analyzing network traffic to detect behavioral anomalies.                                                                                                                                    |
| **Traffic logging**             | Traffic captured by means of SPAN, a TAP port, or a packet broker. Generates ==comprehensive, protocol-specific traffic logs== for over 35 network protocols and application layer analyzers, including HTTP, DNS FTP, and SMTP.                 |
| **Automated analysis**          | Traffic analysis using Bro scripts.                                                                                                                                                                                                              |
| **File extraction**             | Extracts and reassembles various ==file types directly off the wire==.                                                                                                                                                                           |
| **Wazuh HIDS (OSSEC)**          | Host-based intrusion detection system (==HIDS==) that replaced OSSEC and is ==used to monitor and defend Security Onion==. Wazuh offers a lightweight monitoring agent supported on Windows, Linux, Mac OS X, HP-UX, AIX, and Solaris platforms. |
| **Netsniff-ng**                 | Captures network ==traffic via SPAN==, a TAP port, or packet broker in the form of PCAP files.                                                                                                                                                   |
| **Sysmon monitor**              | ==Windows system== service to monitor ==event log and system activity.==                                                                                                                                                                         |
| **Syslog-ng BSD log daemon**    | Enhanced (Software) BSD log daemon that can receive logs and collect inputs from a wide range of sources.                                                                                                                                        |
| **Network analyst tools**       | Provide packet capture and network traffic IP flow analytics capabilities to find anomalous network activity. The following popular network analyst tools are included within Security Onion:                                                    |
#### **Elastic Stack** (ELK) 
A newer Security Onion version. It includes the following tools:

| Component     | Description                                                                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Elasticsearch | Ingest and index logs, large scalable search engine based on Apache Lucene                                                                            |
| Logstash      | Data ingestion engine, parsing, and format logs                                                                                                       |
| Kibana        | Web dashboard that offers visualizations of ingested log data and data exploration.                                                                   |
| TheHIVE       | Security incident response platform and case management system integrated with Malware Information Sharing Platform (MISP)                            |
| Elastic Beats | Lightweight data shipper server agent that sends specific types of operational data to Logstash and Elasticsearch                                     |
| Curator       | Manage indices through scheduled maintenance                                                                                                          |
| ElastAlert    | Query Elasticsearch and alert on user-defined anomalous behavior or other interesting bits of information                                             |
| FreqServer    | Detect DGAs and find random filenames, script names, process names, service names, workstation names, TLS certificate and issuer subjects, and so on. |
| DomainStats   | Conducts whois lookups and provides info about a domain by providing additional context, such as creation time, age, reputation.                      |
## Security Information and Event Management
>Collect and correlate logs to events that indicate malicious or suspicious actions.

| Feature          | Description                                           | Pros                                                                              | Cons                                                    | Notes                                                   |
| ---------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| Data Collection  | Collects logs from various sources.                   | Good at ingesting large volumes of data.                                          | May not interpret data contextually.                    | Automates data collection.                              |
| Data Correlation | Identifies patterns and relationships between events. | Correlates data to detect anomalies.                                              | May require human interpretation.                       | Alerts analysts about suspicious activities.            |
| Data Analysis    | Provides insights and recommendations.                | Offers search, indexing, alerts, pivot, reports, and data modeling.               | Requires human analysis for context.                    | Splunk Enterprise is a popular commercial SIEM product. |
| Customization    | Allows tailoring to specific organizational needs.    | Customizable through apps (configurations, knowledge objects, views, dashboards). | Requires understanding of Splunk and app compatibility. | Certain Cisco products support specific Splunk apps.    |
## Advanced Security Analytics Tools

| Advanced Security Analytics Tools                                                                                   |
| ------------------------------------------------------------------------------------------------------------------- |
| Cisco Secure Network Analytics (formerly Stealthwatch) for IP flow analysis and threat detection.                   |
| Cisco Secure Malware Analytics for cloud-based malware analysis.                                                    |
| Cisco SecureX for unified visibility and automated workflows across security infrastructure.                        |
| Cisco Secure Malware Analytics correlating data from millions of samples to provide insights into malware behavior. |

| Penetration Testing and Vulnerability Assessment                                                          |
| --------------------------------------------------------------------------------------------------------- |
| Penetration Testing simulates attacks to exploit vulnerabilities.                                         |
| Vulnerability Assessment identifies known vulnerabilities in systems.                                     |
| Kali Linux with Metasploit Framework and Armitage for ethical hacking.                                    |
| Using Armitage to exploit a vulnerability in Apache Struts to establish a reverse connection to a server. |

# [[Developing Key Relationships with Internal and External Stakeholders]]

#### Internal

| Internal Stakeholder             | Corporate Assets            | Role                                                       | Relationship with SOC                              |
| -------------------------------- | --------------------------- | ---------------------------------------------------------- | -------------------------------------------------- |
| Executive Management Team        | All assets                  | Incident response administration                           | Coordinate incident response among stakeholders.   |
| Incident Response Team Manager   | Not Applicable              | Ensure proper execution of incident response activities.   | Act as liaison between SOC and other teams.        |
| Incident Response Technical Lead | Not Applicable              | Verify technical accuracy of incident response activities. | Work together to ensure technical accuracy.        |
| Human Resources                  | PII, PHI, PSI               | Manage employee-related security compliance.               | Work together to maintain security compliance.     |
| IT (Network Security Engineer)   | Network Infrastructure      | Manage SOC infrastructure.                                 | Work with SOC to improve overall security posture. |
| GRC Group                        | Intellectual Property       | Align technology objectives with risk management.          | Maintain security posture of corporate assets.     |
| Legal Council                    | Organization's integrity    | Review incident response plans for compliance.             | Identify and obtain electronic evidence.           |
| Public Relations Affairs         | Organization’s public image | Manage communication during incidents.                     | Work together to divulge breach information.       |
| Helpdesk                         | Not applicable              | Serve as initial contact for incidents.                    | Provide updates during incident response.          |
#### External

| External Stakeholder        | Responsibility               | Relationship with SOC                                       |
| --------------------------- | ---------------------------- | ----------------------------------------------------------- |
| Cloud Providers             | Provide cloud services.      | Work together to define responsibility areas.               |
| Other Response<br><br>Teams | Share breach best practices. | Interchange best practices on managing a breach.            |
| Media                       | Manage public relations.     | Provide breach details as dictated by internal departments. |
| Law Enforcement             | Handle disciplinary actions. | Provide breach details as required by law.                  |
| Incident Reporter           | Analyze cyber threats.       | Provide breach details as mandated by government.           |
| Software Vendors            | Produce software.            | Disseminate software vulnerabilities affecting the breach.  |

# [[Understanding SOC Metrics]]

## Security Data Aggregation
SEIM — Real time reporting - Analysis of security events.
Collects, sorts, processes, prioritizes, stores, and reports to the security analyst.

#### Real-time Reports 

| Feature           | Description                                            | Example                                                               |
| ----------------- | ------------------------------------------------------ | --------------------------------------------------------------------- |
| Real-time Reports | Reduce the time needed to detect and contain threats.  | Malware infection on an employee laptop.                              |
| Event Correlation | Identify patterns across multiple events.              | SIEM correlates individual events into a single alert.                |
| Alert Generation  | Generate alerts for suspicious or malicious activity.  | SIEM identifies the infected system and its attempted targets.        |
| Incident Response | Isolate infected systems and take remediation actions. | Isolating the infected system from the network until malware removal. |

| Historical Reports | Summarize security status over time (ordered by months, not days). | SIEM and storage properly sized. | Total log data size and search query time range. |
| ------------------ | ------------------------------------------------------------------ | -------------------------------- | ------------------------------------------------ |
#### Deployment

- Requires careful ==Planning==, 
	- including understanding ==Scope==, 
	- ==Business requirements==, and 
	- ==Engineering specifications==.
- SIEM Sizing + performance and its back-end storage are critical for effective operation.
- Successful SIEM project involves strategic hardware installation. and execution.

![21](/Course-Notes/.assets/Screenshot_2024-11-09_at_13.13.26.png)

#### Functions
>The SIEM is intended to be the glue for various security tools. 
- Log ==collection== of event records from sources throughout the organization
- Log ==normalization== to map log messages from different systems to a common data model
- Events and logs correlation to ==speed== the detection of and reaction to security threats
- ==Consolidating== duplicate event records to reduce the volume of event data to be analyzed
- ==Reporting== tools to address regulation compliance reporting requirements
## Time to Detection (TTD)

| Industry           | Average TTD (Days) |
| ------------------ | ------------------ |
| Retail             | 197                |
| Financial Services | 98                 |
| ==Cisco== AMP      | Hours              |
## SOC Metrics

| Metric                                                 | Description                                                  | Importance                                                            |
| ------------------------------------------------------ | ------------------------------------------------------------ | --------------------------------------------------------------------- |
| Mean Time to Detect (TTD)                              | Time taken to ==identify== an incident ==after it occurs.==  | Directly correlates to SOC maturity and effectiveness.                |
| Mean Time to Contain (MTTC)                            | Time taken to ==contain== an incident ==after detection.==   | Measures the SOC’s ability to limit incident impact.                  |
| Mean Time to Mitigate (MTTM)                           | Time taken to ==resolve== an incident ==after containment.== | Reflects the SOC’s efficiency in incident resolution.                 |
| Number of Incidents Detected, Contained, and Mitigated | Total incidents handled by the SOC.                          | Demonstrates the SOC’s workload and effectiveness.                    |
| Incidents Found Using SOC Playbook                     | % of incidents resolved using predefined playbook            | Highlights the effectiveness of incident response processes.          |
| New SOC Playbook Additions                             | Number of new IRP added                                      | Indicates the SOC’s adaptability and continuous improvement.          |
| Zero-Day Attack Detections                             | Number of previously unknown threats identified.             | Showcases the SOC’s advanced threat detection capabilities.           |
| False Positive/True Positive Detection Rate            | Ratio of false alarms to actual threats.                     | Reflects the accuracy and reliability of the SOC’s detection systems. |
| Operational Cost of Running the SOC                    | Total cost associated with the SOC’s operations.             | Helps in optimizing resource allocation and cost-effectiveness.       |
![20](/Course-Notes/.assets/Screenshot_2024-11-09_at_13.30.00.png)

# [[Understanding SOC Workflow and Automation]]

WMS gets involved after the Tier 1 analyst has validated and registered the incident.

- WMS is a platform for orchestrating and automating incident response processes. 
- Doesn't identify, collect, or help with approvals, which are features of SIEM or ticketing system.

Software that tags and identifies an existing security event, tracks the event, and tracks the actions that are taken in dealing with those events, from detection to ticketing closure. 
## SOC WMS Concepts
SEIMs normalizes centralized networking like syslog servers. 
Security analysts only follow the established workflows.
Automation improves efficiency. 

![19](/Course-Notes/.assets/Screenshot_2024-11-09_at_14.19.12.png)
### Workflow Types

| Workflow Type  | Description                                                                                      | Example                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| Sequential     | Flow-based, progresses from one stage to the next without going backward.                        | Ordering items from a supplier, receiving, and storing them in the warehouse.    |
| - Rules-driven | Based on a sequential workflow, with rules determining the flow.                                 | An item’s location in the warehouse triggers a notification to the picking team. |
| State machine  | Progresses from state to state, allowing for complex processes and returning to previous points. | An item’s status changes from ‘in stock’ to ‘picked’ and then to ‘shipped’.      |

| Component                        | Description                                                                   | Role in WMS                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Workflow                         | The ordered execution of tasks through a well-defined and structured process. | Defines and controls the sequence of tasks within a process.                            |
| WMS (Workflow Management System) | A system that measures and analyzes the execution of a workflow.              | Measures and analyzes the execution of the workflow to identify areas for optimization. |
| SOC Management Team              | Develops the workflow model implementing standardized operating procedures.   | Defines the workflow model and associated procedures.                                   |
| SOC Analysts                     | Follow the workflow model to guide incident handling.                         | Follow the workflow model to perform triage and response activities.                    |
### Repeatable Tasks

| Task                                      | Description                                                                                                                                                                                                                  |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Audit log collection and enrichment       | The process of retrieving and enriching audit log data from all devices within the organization as part of SIEM.                                                                                                             |
| Look up user information                  | Querying the Active Directory or other user repositories to extract further details about a user, such as their department, job title, and so on.                                                                            |
| Look up device information (IP, hostname) | Querying DNS records to obtain information about a device (IP address or hostname) and querying the asset database for further details on the asset.                                                                         |
| Notifications and alerts                  | Generating alerts based on specific conditions configured within SOC security products, monitored by security analysts.                                                                                                      |
| Threat intelligence                       | Using external threat feeds within a SOC to review and research relevant threats based on specific parameters, such as the organization's industry, financial budget, and data characteristics.                              |
| Ticket management                         | Managing tickets within a SOC from creation through validation to resolution and closure.                                                                                                                                    |
| Callouts and escalations                  | When an alert is triggered, a triage process dictates management. After confirmation as an incident, it initiates the incident management and response process, including contacting personnel and possibly law enforcement. |
## Incident Response Workflow

| Aspect                           | Importance                                                    | Challenges                                            | Solution                                                         | Benefits                                                              |
| -------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------- |
| Consistency in Incident Response | Crucial for effective handling of incidents based on severity | Ensuring consistent response for all severity levels  | Defined procedures for handling incidents with changing severity | Timely and appropriate response to incidents                          |
| Reporting                        | Critical for timely communication and monitoring              | Manual reporting can lead to missed targets           | Automated reporting with alerts                                  | Consistent and timely reporting, reducing manual effort               |
| SOC Workflow                     | Conceptual and customizable                                   | Requires specialized individuals with training        | Customizable workflow based on organizational needs              | Efficient and tailored incident response process                      |
| Team Involvement                 | Varies based on organizational structure                      | May involve security analysts, CSIRT team, and others | Flexible team structure to suit organizational requirements      | Appropriate resources for each stage of the incident response process |
![18](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.08.23.png)

| Role                                   | Description                                                                                                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tier 1 analyst                         | Continuously monitors the alert queue, triages security alerts, monitors the health of security sensors and endpoints, and collects data and context necessary to initiate Tier 2 work.                                               |
| Tier 2 analyst                         | Performs deep-dive incident analysis by correlating data from various sources, determines if a critical system or data set has been affected, advises on remediation, and provides support for new analytic threat detection methods. |
| Incident response handler              | Manages the incident, executes containment strategies, ensures the incident response process is followed, and may communicate with the business to provide periodic updates.                                                          |
| Forensics specialist                   | Focused on gathering, retaining, and analyzing computer-related data for investigative purposes in a manner that maintains data integrity.                                                                                            |
| Malware reverse engineering specialist | Analyzes malware behaviors in depth to determine tactics, techniques, procedures, and indicators of compromise. May also write signatures to detect, hunt, and prevent malware.                                                       |
| SOC management                         | Manages resources, including personnel, budget, shift scheduling, and technology strategy to meet SLAs; communicates with management and serves as the organizational point person for business-critical incidents.                   |
| Executive                              | Provides overall direction for the SOC and ensures that the SOC meets and maintains defined objectives.                                                                                                                               |
## SOC WMS Integration

| SOC Responsibility                        | WMS Role                                                  | Benefits of WMS Integration                        |
| ----------------------------------------- | --------------------------------------------------------- | -------------------------------------------------- |
| Cybersecurity incident management         | Automates incident remediation                            | Increased efficiency and consistency               |
| Vulnerability management                  | Receives security events and alerts from SIEM             | Structured processes involving independent systems |
| Threat intelligence and hunting           | Pushes information or commands to security devices        | Improved incident response times                   |
| Network security monitoring and detection | Executes procedures or configurations on security devices | Enhanced threat containment                        |
| Governance and compliance management      | Correlates SIEM events                                    | Streamlined compliance processes                   |
| Physical security and threat management   | Creates tickets for SOC analysts                          | Centralized incident management                    |
![17](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.20.38.png)

| Component                     | Function                                                                                     | Benefit                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| SIEM                          | Captures network audit log data and analyzes log traffic                                     | Detects potential and suspicious behavior              |
| Correlation Logic (Use Cases) | Triggers alerts, notifications, reports, and callouts based on configured rules              | Automates incident response and reporting              |
| WMS Integration with SIEM     | Automatically routes alerts, notifications, reports, and callouts to configured destinations | Ensures consistency in reporting and incident response |
### Integration Methods

| Method      | Description                                                                                               | Example                                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| RESTful API | Uses HTTP requests to retrieve, update, and delete data.                                                  | Updating a corporate enterprise ticket management system.                               |
| CLI-API     | Runs directly from the command line.                                                                      | Querying a SIEM tool to check the status of a use case.                                 |
| TAXII       | A free and open transport mechanism for standardizing the automated exchange of cyber threat information. | Retrieving and exchanging information related to specific threats or groups of threats. |
## SOC Workflow Automation Example

![16](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.46.36.png)
### Example SOC Workflow:
![15](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.47.01.png)

Each SOC workflow level has several subtasks. 

- Opens a case in the ticketing system.
- Looks up user details in the user directory.
- Looks up the user hostname and IP address.
- Looks up the IP address in the threat intel platform for context.
- Collects user proxy traffic and packet captures.
- Reviews user traffic history with threat intel for context and potential threat impact.
- Assigns severity and priority.
- Escalates the event to Tier 2 for investigation.
 ![14](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.48.45.png)

Tier 2 SOC analysts perform the following tasks after escalation from Tier 1 analysts:

- Review threat intelligence, packet captures, endpoint indicators of compromise, endpoint log collection, and memory dumps.
- Determine and execute host containment.
- Add evidence collection artifacts to the case and update case details.
- Notify SOC Tier 3 and management.
![13](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.49.20.png)

The SOC Tier 3 forensics and incident handler performs these tasks:

- Remediate machines by reimaging and extracting malicious content.
- Send new indicators to the threat intel platform.
- Provide context and threat summaries for platform updates.
- Update case details and close cases.

![12](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.49.44.png)

Management collects summary and statistics on the case, including time to detect, contain, resolve, and close.

![11](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.50.21.png)

### WMS Products
vendors focus on automating workflows for the SOC

- Cisco SecureX
- Cisco CloudCenter Action Orchestrator (simplifies workflow creation with a drag-and-drop designer)
- CyberSponse
- IBM Resilient Systems
- Proofpoint Threat Response
- Swimlane

## Detecting and Isolating Malicious Devices 

| Before SecureX                                                                                                                                                                                  | With SecureX                                                                                                                                                  | Benefits                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Customers receive alarms from Secure Network Analytics based on behavioral detections.                                                                                                          | The workflow will automatically isolate hosts associated with devices that triggered alarms on suspicious excessive communication with a new external server. | Faster time to response for critical threats. |
| Customers use these findings to associated it with Secure Endpoint devices and file hashes.                                                                                                     | Get notified about isolated hosts and blocked hashes automatically within WebEx teams.                                                                        | Automatic isolation and notification.         |
| With this information they can manually trigger host isolation and hash isolation if needed.                                                                                                    | Identifies and extracts the source IPs and hashes, isolates infected devices, and blocks malicious files or applications.                                     | Automated threat isolation and blocking.      |
| Network Monitoring and Enrichment: Highlights the use of Secure Network Analytics and AnyConnect to monitor network traffic and gather user and file context for threat detection and response. | Security team uses detections found to isolate the infected systems and stop malicious files execution.                                                       | Enhanced threat detection and response.       |
# [[Cybersecurity Operations, Posture, and Testing]]

Cyberattacks are not the only concern of cybersecurity
- System configuration
- Data encryption
- Security of communication protocols
- Security of software
- Physical security
- System recovery and redundancy

==Protect== Devices, networks, services, applications, and data are protected.
==From== damage or unauthorized access.
==By== Visibility, Prevention, Protection, Detection, Mitigation.

## Security categories

| Security Type        | Description                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------- |
| Network security     | Secures a computer network from threats, blocking attacks and allowing only authorized access.          |
| Application security | Analyzes applications for weaknesses and adds security features, such as encryption.                    |
| Information security | Protects privacy and data integrity, ensuring data availability through measures like encryption.       |
| Operational security | Secures business operations, including risk management, employee education, and backup plans.           |
| Disaster recovery    | Procedures for recovering after cyberattacks or natural disasters.                                      |
| End-user education   | Educates users on social engineering, suspicious activities, security policies, and incident reporting. |
## Important concepts in security posture

| Term                  | Definition                                                                                                                                                              | Example                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Threat                | Any circumstance or event with the potential to cause harm to an asset.                                                                                                 | Malicious software targeting workstations.                                                        |
| Vulnerability         | A weakness that compromises either the security or the functionality of a system.                                                                                       | Weak or easily guessed password.                                                                  |
| Exploit               | A mechanism that uses a vulnerability to compromise the security or functionality of a system.                                                                          | Malicious code used to gain access to a system.                                                   |
| Risk                  | The likelihood that a particular threat that uses a specific attack will exploit a particular vulnerability of an asset that will result in an undesirable consequence. | The likelihood that a malicious code exploit will gain access to a system due to a weak password. |
| Mitigation techniques | Methods and actions that are used to protect against threats and exploits.                                                                                              | Implementing updates and patches, increasing the frequency of data backups.                       |
Several possible causes result from:
1. Lack of quality control processes
2. Unsupported legacy software applications
3. Inherent product flaws or weaknesses
4. Unpatched software defects

## Attack Surface

Total sum of vulnerabilities and entry points within a software, system, or network that can be exploited by unauthorized users, hackers, or malicious actors. It encompasses all the points where an attacker can attempt to gain access to a system and includes hardware, software, and network interfaces. Reducing the attack surface is a key goal in enhancing cybersecurity by minimizing potential risks and vulnerabilities.


- People
- Network
- Software
- Physical

## Attack Vectors
> Path of attack

- Phishing emails and social engineering 
- Weak or compromised user credential
- Malicious insider threats
- Device misconfiguration
- Ransomware or malware
- Unpatched software
- Unencrypted data
- Zero-day vulnerabilities

![10](/Course-Notes/.assets/Screenshot_2024-11-09_at_19.12.11.png)
### Social engineering attacks 
Exploit human psychology 

| **Attack Type**                            | Description                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------- |
| **Phishing emails**                        | Legitimate-looking emails with malicious links or attachments.                   |
| **Fake calls from IT support**             | Attacker poses as IT support to obtain passwords.                                |
| **Malicious media drops**                  | Employees find USB drives or other media and insert them into company computers. |
| **Interactions initiated by the attacker** | Attacker uses fake profiles, spreads misinformation, or asks for access.         |
### Network access control 

| **Attack Type**                    | Description                                                                              |
| ------------------------------ | ---------------------------------------------------------------------------------------- |
| **Unauthorized Access**            | Gaining access to the network without proper authentication                              |
| **Address Spoofing**               | Impersonating a trusted network address to perform man-in-the-middle attacks             |
| **Protocol and Port Exploitation** | Taking advantage of open and poorly configured network communication protocols and ports |
### Software attack surface 

| **Category**          | Description                                    |
| ----------------- | ---------------------------------------------- |
| **Applications**      | Not using encryption to transmit or store data |
| **Operating Systems** | Outdated or unpatched                          |
| **APIs**              | Unsecured or poorly implemented                |
### Physical attack surface 

| **Physical Security Vulnerabilities** | Description                                                                |
| --------------------------------- | -------------------------------------------------------------------------- |
| **Unattended Workstations**           | Unlocked and unattended workstations provide an entry point for attackers. |
| **Inadequate Access Control**         | Faulty or unlocked doors allow unauthorized access to network equipment.   |
| **Improper Data Disposal**            | Decommissioned equipment with sensitive data not erased before disposal.   |
### Reducing attack surface

| Challenge                     | Description                                                                                        |
| ----------------------------- | -------------------------------------------------------------------------------------------------- |
| Lack of Direct Control        | Assets are not under the organization’s direct control.                                            |
| Limited Influence on Security | Organization has no influence on the security features of assets.                                  |
| Complexity of Technology      | Technology itself is complex (e.g., hundreds of features in clouds).                               |
| Technical Expertise Gap       | Organizations lack the technical expertise to configure, implement, and monitor their environment. |
| Excessive Sensitive Data      | Organizations store and try to control excessive amounts of sensitive data.                        |
## Security Posture

| **Term**                                     | Definition                                                                                                                                                                                                                        | Importance                                                                                   | Role in Security Posture                                                                                                                                    |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cybersecurity Posture**                    | The status of actions taken to protect information resources from cyberattacks.                                                                                                                                                   | Central to cybersecurity efforts.                                                            | Outcome of protection, detection, and response capabilities.                                                                                                |
| **Security Posture Definition**              | The outcome of all protection, detection, and response capabilities implemented by an organization.                                                                                                                               | Essential for understanding the effectiveness of security measures.                          | Consists of people, processes, and technology.                                                                                                              |
| **Factors Contributing to Security Posture** | Policies, technical elements, and implementation by the security operations team.                                                                                                                                                 | Directly impact the strength of the security posture.                                        | Includes management policies, security controls, and disaster recovery procedures.                                                                          |
| **Security Posture Maintenance**             | Not a static state but an evolving and dynamic assessment.                                                                                                                                                                        | Requires continuous evaluation and adjustment to remain effective.                           | Involves continuous evaluation and adjustment as systems, technology, threats, and user habits change.                                                      |
| **Resilience**                               | The ability of a resource to adjust and continue operating under both expected and unexpected conditions.                                                                                                                         | Improves security posture by enabling early detection and fast recovery from failures.       | Enables early detection and fast recovery from failures.                                                                                                    |
| **Resilience vs. Robustness**                | Resilience involves preparing for and recovering from failures, while robustness focuses on preventing failures.                                                                                                                  | Understanding the difference helps in creating a balanced security strategy.                 | Resilience focuses on recovery, while robustness focuses on prevention.                                                                                     |
| **Benefits of Resilience**                   | Improves security posture by enabling early detection and fast recovery from failures, reducing risk of system damage.                                                                                                            | Enhances overall security and reduces the impact of failures.                                | Enables early detection and fast recovery from failures.                                                                                                    |
| **Security Posture Assessment**              | Evaluates an organization’s security posture by analyzing its IT assets, security controls, and risk exposure.                                                                                                                    | Identifies areas for improvement and potential vulnerabilities.                              | Analyzes IT assets, security controls, and risk exposure.                                                                                                   |
| **Asset Inventory**                          | Maintains a comprehensive inventory of all IT assets, including their attributes, business impact value, and associated security costs.                                                                                           | Helps in understanding the organization’s security posture and risk exposure.                | Includes attributes, business impact value, and associated security costs.                                                                                  |
| **Security Controls**                        | Covers all implemented security and privacy controls, including preventive, protective, and detection measures, and their effectiveness through continuous monitoring.                                                            | Ensures that appropriate measures are in place to protect assets.                            | Includes preventive, protective, and detection measures.                                                                                                    |
| **Cybersecurity Risk Assessment**            | Evaluates the potential loss or harm to assets that cyber-attacks can cause.                                                                                                                                                      | Helps in prioritizing security investments and allocating resources effectively.             | Evaluates potential loss or harm to assets from cyber-attacks.                                                                                              |
| **Security Investment Decision**             | Organizations must balance security and business agility, relying on CISOs for expert advice on security matters.                                                                                                                 | CISOs provide valuable insights into the appropriate level of investment.                    | Balances security and business agility, with CISOs providing expert advice.                                                                                 |
| **CISO’s Role**                              | Ensures security strategy aligns with business needs, advises on security during planning and design, and keeps business leaders informed about security status.                                                                  | CISOs play a crucial role in aligning security with business objectives.                     | Ensures security strategy aligns with business needs.                                                                                                       |
| **Security Team’s Role**                     | Implements security measures that align with business objectives and reports directly to the CISO.                                                                                                                                | Responsible for implementing security measures and reporting to the CISO.                    | Implements security measures aligned with business objectives.                                                                                              |
| **Compliance Strategy**                      | Meeting the requirements of security regulations and frameworks like PCI-DSS and GDPR can help reduce cybersecurity risks and protect data.                                                                                       | Helps in reducing cybersecurity risks and protecting data.                                   | Meets requirements of security regulations and frameworks.                                                                                                  |
| **Compliance vs. Security Posture**          | Compliance alone doesn’t guarantee a strong security posture; data breaches can occur in compliant organizations.                                                                                                                 | Compliance is important but should not be the sole focus of security efforts.                | Compliance does not guarantee a strong security posture.                                                                                                    |
| **Security Investment Allocation**           | Businesses should quantify risk likelihood and impact to determine appropriate security investment, considering business requirements and potential threats.                                                                      | Helps in allocating resources effectively based on risk assessment.                          | Quantifies risk likelihood and impact to determine appropriate investment.                                                                                  |
| **Achieving a Strong Security Posture**      | Requires a combination of technical solutions and a strong security culture throughout the organization.                                                                                                                          | A strong security posture involves both technical measures and a security-conscious culture. | Requires a combination of technical solutions and a strong security culture.                                                                                |
| **Security Strategy Goal**                   | Keep resources safe from emerging threats and risks.                                                                                                                                                                              | Ensures that the organization’s resources are protected from potential threats.              | Keeps resources safe from emerging threats and risks.                                                                                                       |
| **Security Strategy Adaptation**             | Reflects the operational needs of the organization and continuously adapts to the organization’s goals.                                                                                                                           | Ensures that the security strategy remains relevant and effective.                           | Reflects operational needs and continuously adapts to organizational goals.                                                                                 |
| **Security Tactics**                         | Operational elements and methods chosen to achieve a strategic goal, including human resources plans, network segmentation, secure remote access, access controls, threat recognition training, software updates, and monitoring. | Implemented to achieve the security strategy.                                                | Includes human resources plans, network segmentation, secure remote access, access controls, threat recognition training, software updates, and monitoring. |
| **AUP Compliance**                           | Employees must sign the AUP, agreeing to comply with the outlined rules and policies, before accessing network resources.                                                                                                         | Ensures that employees understand and agree to comply with security policies.                | Employees must sign the AUP before accessing network resources.                                                                                             |
| **Policy Implementation**                    | IT operational teams are responsible for implementing the compliance requirements outlined in the AUP, using various methods like configuring security policies on devices.                                                       | Ensures that the policies outlined in the AUP are implemented effectively.                   | IT operational teams implement compliance requirements outlined in the AUP.                                                                                 |
| **AUP Role**                                 | The AUP serves as a document that outlines strategic requirements for data security and privacy, with tactics like onboarding procedures and device configuration used to meet those requirements.                                | Outlines strategic requirements for data security and privacy.                               | Serves as a document outlining strategic requirements for data security and privacy.                                                                        |
Frameworks
- PCI-DSS (Payment Card Industry Data Security Standard)
- GDPR (General Data Protection Regulation
- HIPPA (Health Insurance Portability and Accounting Act)
- SOX (Sarbanes-Oxley Act)
- FedRAMP (Federal Risk and Authorization Management Program

## Security Assessments

Goal: Determine the extent to which the security and privacy controls meet three qualifications:
- They are implemented correctly.
- They operate as intended.
- They produce the desired outcome regarding the security requirements for the system.

 Based on the assessment objectives defining what must be assessed and how.
- The subject under assessment, 
- The desired security status of the subject
- The method, depth, and coverage to verify the security status of the subjects

Assessments can evaluate multiple cybersecurity elements, from the technical to physical.
- Vulnerability assessment
- Risk assessment
- Documentation, configuration, and code review
- Physical security test
- Penetration test

### Security Assessment Objectives, Objects, and Methods

Assessment object: Ask yourself the two questions:
- Where can I get the information that I need?
- What controls, features, and documents can I assess?
EG:
- **Specifications:** Document-based artifacts, such as written policies, procedures, plans, and architectural designs of the system.
- **Mechanisms:** Hardware, software, or firmware security capabilities that are used.
- **Activities:** Actions that involve people, such as system backup operations and traffic monitoring.
- **Individuals:** People applying the specifications, mechanisms, and performing activities.

NIST defines three assessment methods to evaluate assessment objects:
- Examinations: Review documentation, observe processes, check configurations, verify physical security, and study technical manuals and user guides. For instance, reviewing the IPS ruleset to ensure it aligns with security policies.
- Interviews: Facilitate discussions with individuals to gather evidence about assessment objectives.
- Tests: Create specific conditions to compare actual behavior with expected behavior. Security tests may include access controls, penetration of critical system components, backup operations, incident response, and physical access devices. The organization provides test considerations, including resources, features to test, and acceptable test actions, to help plan the test and address assessment objectives.

## Assessment Approaches

Internal VS External
![9](/Course-Notes/.assets/Screenshot_2024-11-09_at_19.50.19.png)

(White) Crystal box 
- Topology diagrams
- aAsset lists
- Configuration files

Gray box = Simulate an insider threat
- Limited knowledge 
- Same privileges as a regular non-technical user.

(Black) Dark box = Simulate a real adversary
- Specialized scanning tools
	- Network-mapping tools
	- Vulnerability scanners
	- Nessus
	- Nmap
	- Burpsuite
	- OpenVAS
	- ImmuniWeb
	- Metasploit

![8](/Course-Notes/.assets/Screenshot_2024-11-09_at_19.50.37.png)

## Security Tests

Assesses protection, detection, and response in a controlled environment.
- Types of tests that determine achievable objectives
- Test prerequisites for starting the test
- Test phases and constraints
- Legal backgrounds that require explicit permissions

![7](/Course-Notes/.assets/Screenshot_2024-11-09_at_19.53.02.png)

- **Network discovery tests:** Tests that identify which systems exist, which services these systems provide, and the software that implements them.
- **Vulnerability scans:** Tests that identify software vulnerabilities.
- **Penetration tests:** Tests that attempt to exploit vulnerabilities
- **Compliance tests:** Tests that check whether the operational state corresponds to legal or framework requirements.

## Vulnerability Assessments and Penetration Tests

![6](/Course-Notes/.assets/Screenshot_2024-11-09_at_19.54.13.png)

| Step                     | Description                                                           | Tools/Techniques                                                                                           |
| ------------------------ | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Target Identification    | Gather preliminary information about the target.                      | OSINT techniques, domain name lookup, web URL search, network address range analysis, email address lookup |
| Asset Identification     | Identify specific assets within the target’s network.                 | Network scanning tools                                                                                     |
| Service Identification   | Determine the services running on the identified assets.              | Scanning tools for operating system and application identification                                         |
| Vulnerability Assessment | Analyze the identified assets and services for known vulnerabilities. | Vulnerability scanner                                                                                      |
### Penetration tests

![5](/Course-Notes/.assets/Screenshot_2024-11-09_at_20.00.57.png)

- Attack techniques that are successful against the system
- The level of expertise that an adversary requires to compromise the system (how easy it is to compromise the system)
- How fragile or resilient the system is in the case of a successful attack and what consequences such an attack could have
- Effectiveness of the defenses
- Which security measures can improve the security posture

![4](/Course-Notes/.assets/Screenshot_2024-11-09_at_20.02.17.png)![3](/Course-Notes/.assets/Screenshot_2024-11-09_at_20.05.44.png)![2](/Course-Notes/.assets/Screenshot_2024-11-09_at_20.06.01.png)

| Category                | Description                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Engagement rules        | - Specify how assessments are conducted, <br>- Including data handling, <br>- Briefing, <br>- Reporting, <br>- Start/finish dates, <br>- Announcement, <br>- Information availability, <br>- And applicable laws.     |
| Scope of the assessment | - Defines the security concerns to be addressed,<br>- The specific assets to be tested,<br>- The extent of the assessment, <br>- The testing environment, <br>- Access level, and <br>- Permitted testing techniques. |
## Execution and Closure Stages

- **Discovery phase:** Gather information about the target and identify the vulnerabilities.
- **Attack phase:** Try to validate the discovered vulnerability. In the attack phase, you perform the following activities:
    1. Choose an exploit that fits the vulnerability and attempt to gain access to the target.
    2. Escalate the privileges.
    3. Browse the system to discover new information.
    4. Establish presence by introducing new adversarial tools to the target system.

## Security Assessment Legal Framework

| **Region** | Framework                                                  | Description                                                                      |
| ------ | ---------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **EU**     | Network and Information Security Directive (NIS Directive) | Provides a basis for cybersecurity obligations, especially for critical systems. |
| **EU**     | TIBER-EU                                                   | A framework that supports the NIS Directive.                                     |
| **US**     | NIST Cybersecurity Framework                               | A voluntary framework for improving cybersecurity risk management.               |
| **US**     | DoD CMMC 2.0                                               | A framework specifically designed for the U.S. Department of Defense.            |
| **US**     | NICCS Framework                                            | A framework that categorizes cybersecurity activities and roles.                 |
## Cybercrime Laws

| **Area**          | Description                                                               | Requirements                                                     |
| ----------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Compliance**    | Respect cybercrime laws in all countries where assessments are conducted. | Understand and comply with relevant legislation in each country. |
| **Authorization** | Obtain authorization before starting assessments.                         | Get explicit permission to conduct assessments.                  |
| **Notification**  | Inform stakeholders about the assessment.                                 | Communicate the purpose and scope of the assessment.             |
| **Scope**         | Understand the allowed system activities.                                 | Clarify the boundaries of the assessment.                        |
| **Documentation** | Obtain necessary authorization documents.                                 | Get permissions, contracts, RoE, and assessment scope documents. |
| **Phishing**      | Avoid phishing attacks without explicit permission.                       | Obtain clear authorization for phishing tests.                   |
| **SOC Testing**   | Ensure SOC testing is conducted by a certified and qualified team.        | Verify the credentials and expertise of the testing team.        |
- Penetration testers must adhere to cybercrime laws in all jurisdictions where they operate.
- Obtaining explicit permission to conduct assessments is essential to avoid legal repercussions.
- A 'get-out-of-jail-free' document is crucial, outlining authorized activities and protecting testers from liability.

# [[Cybersecurity Teaming Concepts]]

### Key Teams

|Team Color|Role|Description|
|---|---|---|
|Red|Offenders|Identify risks and vulnerabilities through simulated attacks.|
|Blue|Defenders|Monitor security posture and respond to threats.|
|Yellow|Builders|Develop and maintain secure applications and systems.|
|Purple|Collaborators|Enhance security by combining red and blue team efforts.|
|Green|Developers|Implement security practices in system and application development.|
|Orange|Offensive|Focus on offensive security techniques to improve defenses.|
|White|Oversight|Management representatives who monitor and enforce rules during security exercises.|
Reference Information

- MITRE ATT&CK framework: A comprehensive knowledge base of adversarial tactics and techniques.
- Cyber Threat Intelligence (CTI): The process of gathering and analyzing information about threats and adversaries.
- Security Information and Event Management (SIEM): A solution for collecting and analyzing security data.

# [[Security Operations Center Processes and Services]]

Key Services Provided by SOC 

| Service                | Description                                                                  |
| ---------------------- | ---------------------------------------------------------------------------- |
| Threat Intelligence    | Gathering and analyzing threat data to inform incident response strategies.  |
| Incident Detection     | Monitoring security alerts and incidents to identify potential threats.      |
| Incident Analysis      | Investigating incidents to determine the root cause and impact.              |
| Incident Coordination  | Collaborating with other departments to manage incidents effectively.        |
| Post-Incident Analysis | Analyzing incidents to identify lessons learned and improve future response. |
 Six-step incident response plan

|Service|Description|
|---|---|
|Preparation|Establishing security policies, risk assessments, and forming a CSIRT.|
|Identification|Detecting potential security incidents and gathering evidence.|
|Containment|Preventing the spread of confirmed incidents and securing resources.|
|Eradication|Removing unauthorized information and malware from systems.|
|Recovery|Restoring affected systems to their normal state.|
|Lessons Learned|Analyzing incidents to prevent future occurrences and improve response.|
## SOC Interaction with Other Departments

| Importance                          | Description                                                             |
| ----------------------------------- | ----------------------------------------------------------------------- |
| Maintaining Organizational Security | Collaboration with IT, networking, and software departments.            |
| Incident Response                   | Effective communication for quick incident identification and response. |
| Resource Allocation                 | Strong relationships with business stakeholders for resource gathering. |
| Comprehensive Security              | Mutual benefits from collaboration with other departments.              |
| Security Awareness                  | Regular meetings and updates foster a culture of security.              |

| Category  | Description                                                                   |
| --------- | ----------------------------------------------------------------------------- |
| Tools     | Advanced tools for monitoring, detection, and response to security incidents. |
| Resources | Experienced SOC analysts with a strong technical background in cybersecurity. |
|           | Internal resources from IT and networking departments.                        |
|           | External relationships with vendors and cybersecurity experts.                |
|           | Continuous training and certification for SOC analysts.                       |
### Examples of Security Incidents
 - Security incidents can originate from various sources, including user reports, helpdesk alerts, and automated monitoring systems.
- Common examples of incidents include malware infections, unauthorized access attempts, and data breaches.
- The SOC must prioritize incidents based on severity and potential impact on the organization, ensuring that critical threats are addressed first.
- Case studies of past incidents can provide valuable insights into effective response strategies and areas for improvement.
- Continuous monitoring and analysis of security incidents help refine the SOC's approach to incident management.
![1](/Course-Notes/.assets/Pasted_image_20241204222711.png)