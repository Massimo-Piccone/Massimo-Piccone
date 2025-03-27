# SOC Roles
Holistic roles - common set of skills and responsibilities
Benefits: 
- Quicker time to resolution, 
- more effective transfer of knowledge, 
- increased satisfaction, and
- reduced team burnout.
 ![4](/Course-Notes/.assets/Screenshot_2024-11-08_at_21.47.28.png)
 
 NIST NICE workforce framework (Publication—NIST 800-181 Rev.1) identifies the knowledge, skills, and abilities 
 
 (KSAs) in the categories of Investigate, Collect and Operate, and Analyze. 
 
 However, overlaps might occur in KSAs between the Investigate, and the Collect and Operate categories across various organizations.
 ![3](/Course-Notes/.assets/Screenshot_2024-11-08_at_21.49.17.png)

SOC Tier 1 — entry-level
triage and analyst role 
reviews alerts and creates tickets.
sysadmin and scripting skills,

## SOC Tier 2 Analyst: Incident Handler

The SOC Tier 2 analyst is the incident handler. That analyst does the following: 

- Performs an in-depth assessment of incidents that were escalated by the triage specialist.
- Provides an attack context by including telemetry data that was not collected by the triage specialist. This action might result in discovered actionable threat intelligence that aids in a detection feedback loop through Indicators of Compromise and better rulesets.
- Determines the scope of the attack, the nature of the attack, and the systems that are affected.
- Decides on a strategy for containment, remediation, and recovery and executes that strategy.
- Escalates to the Tier 3 analyst if issues arise.

## SOC Tier 3 Analyst: Incident Responder and Threat Hunter

The SOC Tier 3 analyst is the threat hunter and sometimes also the subject matter expert. This analyst is the most experienced member of the SOC workforce. The threat hunter does the following:

- Proactively identifies threats, security gaps, and unknown vulnerabilities.
- Researches new attack techniques and models threats that are relevant to the organization. Recommends optimizations and configurations for use in security monitoring tools and assets.
- Aids the other SOC analysts on major incidents. The threat hunter brings key insights, experience, and expertise to incidence response operations.

## SOC Manager

The SOC manager is the immediate supervisor for all SOC analysts and is responsible for the following:

- Managing the security team, including hiring, training, and evaluating team members
    
- Assessing incident reports
    
- Developing and implementing crisis communication procedures by overseeing the financial aspects of the SOC and supporting security audits.
    

The SOC manager reports to either the Chief Information Security Officer (CISO) or the Chief Information Officer (CIO).

## SOC Tools

The SOC Team will use tools for various activities. Some of the tools that make up their toolkit are as follows:

- **IT Service Management (ITSM)** system is a set of workflow tools that collects and manages incident data from security tools and devices into a structured automated workflow that assists the SOC with prioritizing threats. An example of a popular ITSM is ServiceNow.
    
- **Security and Information Event Management System (SIEM).** Provides real-time monitoring, analysis, and logging of events. Provides User and Entity Behavior Analytics (UEBA) via artificial intelligence (AI) and machine learning technologies. Splunk is an example of a popular SIEM.
    
- **Intrusion Detection System (IDS) / Intrusion Prevention System (IPS).** Monitors networks for malicious activity or policy violations. An IDS will provide an alert to the SOC analyst on a potential incident. An IPS will provide an alert to the analyst and will take additional remediation actions to block the intrusion to minimize damage. An IDS is usually classified as either Network Intrusion Detection Systems (NIDS) or Host Intrusion Detection Systems (HIDS). A NIDS will monitor network traffic for harmful or abnormal behavior. An HIDS will monitor a single device or host for harmful or abnormal behavior. Cisco Firepower 4100 Series is an example of an appliance with NIDS/IPS functionality and Cisco Secure Endpoint is an example of an HIDS/IPS.
    
- A **vulnerability scanner** is an application designed to assess computers, networks, or applications for known weaknesses. They identify vulnerabilities resulting from device misconfigurations, software flaws, and missing software patches that may be present in devices such as firewalls, routers, and servers, and endpoint devices. Nessus is an example of a popular vulnerability scan application.
    
- A **Threat Intelligence** service collects, processes, analyzes, and disseminates threat information and responds to activities that pose a threat to applications and systems. Threat Intelligence collects vulnerability and exploit information in real time, compiles into a single database, and disseminates it to consumers of the service. Cisco Talos is one of the largest providers of security threat intelligence.

## Before, During, and After Incidents

During the day, the SOC analyst typically focuses on monitoring. When an incident occurs, the SOC analyst’s attention turns to incident response and to some of the available tools. The SOC must coordinate with the stakeholders during the incident. Working with the network operations center (NOC), system owners, and data owners can improve the outcome.

The SOC Tier 1 triage specialist focuses on the ITSM ticketing system to monitor alerts. The threat hunter focuses on the Cisco Talos threat intelligence feeds.

![2](/Course-Notes/.assets/Screenshot_2024-11-08_at_21.54.20.png)

After an incident is resolved, the SOC begins its recovery phase. The team works closely with the legal department to make sure that all procedures are documented and would hold up in court proceedings. Reports are created that detail the findings and the lessons learned. The SOC analysts follow several steps in the post-incident phase:

1. Use forensics applications, such as Encase, Velociraptor, or Redline, to collect, analyze, and create reports. Also, take steps to help ensure legal compliance for potential court procedures.
2. Consider using a SOC 2 audit report to show organizational and legal compliance.
3. Generate multiple reports that will serve as lessons learned for future SOC incident response activities.

# Interaction of Various Roles Within the SOC

![1](/Course-Notes/.assets/Screenshot_2024-11-08_at_22.06.10.png)

The SOC tiers can include the following responsibilities:

- Tier 1:
    1. Monitors the alert queue continuously
    2. Triages security alerts.
    3. Monitors the health of the security sensors and endpoints
    4. Collects data and context necessary to initiate Tier 2 work

- Tier 2:
    1. Performs deep-dive incident analysis by correlating data from various sources
    2. Determines if a critical system or data set has been impacted.
    3. Provides guidance on remediation.
    4. Provides support for new analytic methods for use in threat detection

- Tier 3:
    1. Applies in-depth technical knowledge about the network, endpoint, threat intelligence, forensics, malware reverse engineering, and the functioning of specific applications or underlying IT infrastructure
    2. Acts as an advanced security analyst and proactive threat hunter who doesn’t wait for escalated incidents
    3. Participates in developing, tuning, and implementing threat detection analytics
- SOC Manager
	1. Communicates pertinent information to multiple parties.
		- CIO and CISO
		- Legal department, HR department, The company workforce, 
		- Public affairs if the incident may generate publicity, 
		- and Law enforcement if appropriate.

The SOC also has interactions with external resources. The following are examples of external resources that the SOC might contact during an incident:
- Legal entities
- Media sources
- International courts of law
- US-CERT/CISA

# [[Quick Reference]]

Key Roles in SOC

|Role|Description|
|---|---|
|**Tier 1 Analyst**|Entry-level position responsible for initial triage of alerts and monitoring security systems.|
|**Tier 2 Analyst**|Incident handler who performs in-depth assessments of escalated incidents and determines containment strategies.|
|**Tier 3 Analyst**|Senior-level threat hunter and subject matter expert who proactively identifies threats and assists in incident response.|
|**SOC Manager**|Oversees the SOC team, manages incident reports, and develops crisis communication procedures.|

Key Tools

- **IT Service Management (ITSM)**: Workflow tools that manage incident data and assist in prioritizing threats (e.g., ServiceNow).
- **Security Information and Event Management (SIEM)**: Provides real-time monitoring and analysis of security events (e.g., Splunk).
- **Intrusion Detection System (IDS)**: Monitors networks for malicious activity and alerts analysts (e.g., Cisco Firepower).
- **Vulnerability Scanner**: Assesses systems for known weaknesses (e.g., Nessus).
- **Threat Intelligence Service**: Collects and analyzes threat information to inform security measures (e.g., Cisco Talos).

Key Responsibilities

|Role|Responsibilities|
|---|---|
|**Tier 1 Analyst**|Monitors alerts, performs initial triage, and collects necessary data for further investigation.|
|**Tier 2 Analyst**|Conducts deep-dive analysis, determines attack scope, and executes containment strategies.|
|**Tier 3 Analyst**|Researches new attack techniques, provides insights during incidents, and develops detection analytics.|
|**SOC Manager**|Manages team operations, oversees incident reports, and ensures compliance with security audits.|

Key Processes

- **Incident Management**: The structured approach to handling security incidents, including preparation, detection, analysis, containment, eradication, and recovery.
- **Post-Incident Review**: A process to analyze incidents after resolution to improve future response and security posture.

Facts to Memorize

- SOC roles: Tier 1 (Triage Specialist), Tier 2 (Incident Handler), Tier 3 (Incident Responder and Threat Hunter), SOC Manager
- Common SOC tools: ITSM (e.g., ServiceNow), SIEM (e.g., Splunk), IDS/IPS (e.g., Cisco Firepower), Vulnerability Scanner (e.g., Nessus), Threat Intelligence (e.g., Cisco Talos)
- NIST NICE workforce framework categories: Investigate, Collect and Operate, Analyze
- Key responsibilities of SOC Manager: Hiring, training, incident report assessment, crisis communication procedures

Reference Information

- NIST 800-181 Rev.1: Framework for identifying KSAs in cybersecurity roles
- Types of IDS: Network Intrusion Detection Systems (NIDS) and Host Intrusion Detection Systems (HIDS)
- Forensic applications: Encase, Velociraptor, Redline
- SOC 2 audit report: Used for demonstrating organizational and legal compliance

Concept Comparisons

|SOC Role|Responsibilities|Skills Required|
|---|---|---|
|Tier 1 Analyst|Initial triage of alerts, monitoring health of security sensors and endpoints|Basic networking, traffic capture, device monitoring|
|Tier 2 Analyst|In-depth incident analysis, determining attack scope, remediation strategies|Broader skill set, data analysis, incident handling|
|Tier 3 Analyst|Proactive threat hunting, advanced incident response, threat intelligence research|Advanced network security, forensics, malware analysis|
|SOC Manager|Managing team, incident report assessment, crisis communication|Leadership, communication, incident management|

Cause and Effect

| Event/Action                         | Effect/Outcome                                                                     |
| ------------------------------------ | ---------------------------------------------------------------------------------- |
| SOC team identifies a cyberattack    | Organization can respond quickly to mitigate damage and prevent future attacks     |
| Triage specialist escalates an alert | More experienced analysts can provide deeper analysis and context for incidents    |
| Incident response coordination       | Improved outcomes through collaboration with NOC, legal, and HR departments        |
| Post-incident reporting              | Lessons learned can enhance future SOC operations and incident response strategies |

# Overview of Security Operations Center (SOC)

### Definition and Purpose of SOC

- A Security Operations Center (SOC) is a centralized unit that deals with security issues on an organizational and technical level.
- SOCs are essential for organizations to effectively respond to sophisticated cyber threats and maintain a robust security posture.
- The size and structure of a SOC can vary based on the organization's scale and network complexity, ranging from small outsourced teams to large dedicated teams.
- SOCs play a critical role in incident detection, response, and recovery, ensuring that organizations can mitigate risks associated with cyberattacks.

### Importance of Staffing in SOC

- Adequate staffing is crucial for the effectiveness of a SOC, as it directly impacts the team's ability to respond to incidents in a timely manner.
- Larger organizations typically require a dedicated team of SOC analysts to handle the volume and complexity of potential threats.
- The roles within a SOC are not rigidly defined and can vary significantly between organizations, leading to overlaps in responsibilities.
- The NIST NICE workforce framework provides a guideline for the knowledge, skills, and abilities (KSAs) required for SOC roles, but implementation can differ widely.

# SOC Roles and Responsibilities

### SOC Tier 1 Analyst: Triage Specialist

- The Tier 1 analyst is the entry-level position responsible for initial triage of alerts generated by security tools.
- They assess alerts from Security Information and Event Management (SIEM) systems and IT Service Management (ITSM) ticketing systems.
- Key skills include sysadmin knowledge, scripting, and relevant cybersecurity certifications (e.g., Cisco CyberOPS Associate, CompTIA).
- The primary function is to determine if an alert requires further investigation and escalate it to the investigation team if necessary.

### SOC Tier 2 Analyst: Incident Handler

- The Tier 2 analyst performs in-depth assessments of incidents escalated by Tier 1 analysts.
- They provide context for attacks by analyzing additional telemetry data, which can lead to actionable threat intelligence.
- Responsibilities include determining the scope and nature of attacks, and developing strategies for containment and recovery.
- This role requires a broader skill set than Tier 1, focusing on deeper analysis and incident management.

### SOC Tier 3 Analyst: Incident Responder and Threat Hunter

- The Tier 3 analyst is the most experienced member of the SOC, often acting as a subject matter expert.
- Responsibilities include proactively identifying threats, researching new attack techniques, and optimizing security monitoring tools.
- They assist Tier 2 analysts during major incidents, providing insights and expertise to enhance incident response efforts.
- This role requires extensive knowledge of network security and data analytics, as well as familiarity with the latest attack techniques.

### SOC Manager

- The SOC manager oversees the entire SOC team, including hiring, training, and evaluating analysts.
- They are responsible for managing incident reports and developing crisis communication procedures.
- The manager also oversees the financial aspects of the SOC and supports security audits.
- This role typically reports to the Chief Information Security Officer (CISO) or Chief Information Officer (CIO).

# SOC Tools and Technologies

### IT Service Management (ITSM) Tools

- ITSM tools are essential for managing incident data and streamlining workflows within the SOC.
- These tools help prioritize threats and organize incident response efforts effectively.
- An example of a widely used ITSM tool is ServiceNow, which automates incident management processes.
- ITSM systems integrate data from various security tools, providing a structured approach to incident handling.

### Security Information and Event Management (SIEM) Systems

- SIEM systems are critical for collecting and analyzing security data from across the organization.
- They provide real-time analysis of security alerts generated by applications and network hardware.
- SIEM tools help SOC analysts identify patterns and correlations in security events, facilitating quicker incident response.
- Effective use of SIEM can significantly enhance an organization's ability to detect and respond to cyber threats.

# Overview of SOC Tools

### IT Service Management (ITSM)

- ITSM systems streamline incident management by automating workflows, allowing SOC teams to prioritize threats effectively.
- ServiceNow is a widely used ITSM tool that integrates incident data from various security tools.
- ITSM helps in tracking incidents from detection to resolution, ensuring accountability and efficiency.
- The structured workflow assists in maintaining a historical record of incidents for future reference.
- ITSM systems can also facilitate communication between different teams during an incident response.

### Security Information and Event Management (SIEM)

- SIEM systems provide real-time monitoring and analysis of security events, crucial for timely incident response.
- Splunk is a leading SIEM tool that utilizes AI and machine learning for User and Entity Behavior Analytics (UEBA).
- SIEMs aggregate logs from various sources, enabling comprehensive visibility into security incidents.
- They help in identifying patterns and anomalies that may indicate potential threats.
- SIEMs are essential for compliance reporting and forensic investigations post-incident.

### Intrusion Detection and Prevention Systems (IDS/IPS)

- IDS monitors network traffic for suspicious activity and alerts SOC analysts, while IPS takes proactive measures to block threats.
- Cisco Firepower 4100 Series exemplifies a device with both NIDS and IPS capabilities.
- NIDS analyzes traffic across the entire network, while HIDS focuses on individual devices.
- Effective use of IDS/IPS can significantly reduce the time to detect and respond to intrusions.
- Understanding the differences between NIDS and HIDS is crucial for effective deployment in a security architecture.

### Vulnerability Scanners

- Vulnerability scanners assess systems for known weaknesses, helping organizations identify and remediate security gaps.
- Nessus is a popular tool that scans for misconfigurations, software flaws, and missing patches.
- Regular vulnerability assessments are essential for maintaining a strong security posture.
- These tools can prioritize vulnerabilities based on risk, aiding in efficient resource allocation for remediation.
- Integrating vulnerability scanning into the SOC workflow enhances proactive threat management.

### Threat Intelligence Services

- Threat intelligence services collect and analyze data on emerging threats, providing actionable insights to SOC teams.
- Cisco Talos is a prominent provider of threat intelligence, offering real-time data on vulnerabilities and exploits.
- Utilizing threat intelligence can improve incident response times and enhance overall security strategies.
- Threat intelligence feeds can be integrated into SIEMs for enriched context during investigations.
- Understanding the threat landscape is vital for anticipating and mitigating potential attacks.

# Incident Management Process

### Incident Response Phases

- The SOC analyst's role shifts from monitoring to incident response when an incident occurs, requiring immediate action.
- Coordination with stakeholders, including NOC and legal teams, is critical for effective incident management.
- The recovery phase involves documenting procedures and findings to ensure compliance and improve future responses.
- Forensic tools like Encase and Velociraptor are used to analyze incidents and gather evidence for legal purposes.
- Post-incident reports are essential for capturing lessons learned and refining incident response strategies.

### Roles and Responsibilities in the SOC

- SOC teams are structured into tiers, each with specific responsibilities to ensure efficient incident management.
- Tier 1 analysts monitor alerts and perform initial triage, determining if further investigation is needed.
- Tier 2 analysts conduct deeper analysis, correlating data from multiple sources to assess impact and guide remediation.
- Tier 3 analysts possess advanced technical skills and proactively hunt for threats, enhancing the SOC's overall effectiveness.
- Clear communication among team members and with stakeholders is vital for successful incident resolution.

### Stakeholder Interaction During Incidents

- The SOC must maintain open lines of communication with internal stakeholders, including IT, HR, and legal departments.
- The SOC manager plays a key role in prioritizing tasks and ensuring resources are allocated effectively during incidents.
- External communication may involve legal entities, media, and government organizations like US-CERT/CISA.
- Building strong relationships with stakeholders enhances collaboration and improves incident outcomes.
- Regular training and simulations can prepare the SOC for real-world incident scenarios.

# Tools and Techniques for Incident Analysis

### Forensic Tools

- Forensic applications are critical for collecting and analyzing data post-incident, ensuring thorough investigations.
- Tools like Encase and Velociraptor provide capabilities for data recovery and analysis, essential for legal compliance.
- The use of forensics helps in understanding the attack vector and improving future defenses.
- Analysts must be trained in forensic methodologies to effectively utilize these tools during investigations.
- Documenting forensic findings is crucial for legal proceedings and organizational learning.

### Reporting and Documentation

- Post-incident reports should detail the incident timeline, response actions, and lessons learned for future reference.
- SOC teams should create multiple reports to cater to different stakeholders, including technical and non-technical audiences.
- Documentation must comply with legal standards to ensure it can be used in court if necessary.
- Reports should include recommendations for improving security posture based on incident analysis.
- Regular reviews of incident reports can help identify trends and areas for improvement in the SOC's processes.

### Continuous Improvement in SOC Operations

- The SOC should regularly review and update its standard operating procedures (SOPs) based on lessons learned from incidents.
- Training and development programs for SOC analysts are essential for keeping skills current and effective.
- Implementing feedback loops from incident responses can enhance the SOC's overall effectiveness.
- Collaboration with other departments can provide insights into improving security measures organization-wide.
- Continuous monitoring and assessment of tools and technologies ensure the SOC remains equipped to handle evolving threats.