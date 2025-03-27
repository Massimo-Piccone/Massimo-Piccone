WMS == SOAR

Software that tags and identifies an existing security event, tracks the event, and tracks the actions that are taken in dealing with those events, from detection to response to mitigation to ticketing closure.

# SOC WMS Concepts

Utilizes automation to improve efficiency. A syslog server centralizes networking and security logs. However, they are not normalized. SEIMs fix this.

The role of the security analyst is to follow the established workflow to ensure that incidents are processed efficiently and in the same way. Many repeatable job tasks can be automated to improve the SOC efficiency.

![10](/Course-Notes/.assets/Screenshot_2024-11-09_at_14.17.57.png)

WMS is a platform for orchestrating and automating incident response processes. 
WMS does not identify, collect, or help with approvals, which are features of SIEM or ticketing system. As seen in the following figure, the process begins in SIEM and then moves to the security WMS followed by the individual security devices

![9](/Course-Notes/.assets/Screenshot_2024-11-09_at_14.19.12.png)

WMS gets involved after the Tier 1 analyst has validated and registered the incident.
## Workflow Types

Workflows aim to coordinate tasks and synchronize data with the ultimate goal of efficiency.

There are three types of workflows:

- **Sequential:** Flow based. Progressing from stage1 onward, and does't move backward.
	-  **Rules-driven:** Based on a sequential workflow. The rules dictate the progress.

- **State machine:** Progresses from state to state. It is more complex and can return to a previous point if required.

Workflow: "The ordered execution of tasks through a well-defined and structured process". 
Systems can measure WMS and analyze the execution of the process to continue optimization. 
- The WMS defines and controls the various tasks and activities that are associated with a process.
- The SOC management team develops the workflow model that implements the standardized operating procedures for the incident handling process. 
- The workflow model guides the SOC analysts through the triage and response procedures. 

## Repeatable Tasks

| Task                                      | Description                                                                                                                                                                                                                  |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Audit log collection and enrichment       | The process of retrieving and enriching audit log data from all devices within the organization as part of SIEM.                                                                                                             |
| Look up user information                  | Querying the Active Directory or other user repositories to extract further details about a user, such as their department, job title, and so on.                                                                            |
| Look up device information (IP, hostname) | Querying DNS records to obtain information about a device (IP address or hostname) and querying the asset database for further details on the asset.                                                                         |
| Notifications and alerts                  | Generating alerts based on specific conditions configured within SOC security products, monitored by security analysts.                                                                                                      |
| Threat intelligence                       | Using external threat feeds within a SOC to review and research relevant threats based on specific parameters, such as the organization's industry, financial budget, and data characteristics.                              |
| Ticket management                         | Managing tickets within a SOC from creation through validation to resolution and closure.                                                                                                                                    |
| Callouts and escalations                  | When an alert is triggered, a triage process dictates management. After confirmation as an incident, it initiates the incident management and response process, including contacting personnel and possibly law enforcement. |
# Incident Response Workflow

Consistency is crucial in an incident response process. It defines how incidents are handled based on their severity. A sound process ensures that all incident severity levels have a defined response. As an incident progresses, its severity may change, especially during monitoring after remediation. The process should have procedures to handle incidents when their severity changes.

During incident response, consistent and timely reporting is crucial. Each incident severity type has defined notification, reporting, and monitoring periods. Investigators may be responsible for reporting, which is usually handed off to the next shift as staff work shifts end. Manual involvement can lead to missed reporting targets.

A SOC WMS automates these activities, reducing manual intervention and ensuring consistent and timely reporting. It can also generate alerts when reporting periods end, informing investigators or confirming action on reports.

Within a SOC, specialized individuals are highly trained in their functions. The SOC workflow is conceptual and customizable based on the organization’s situation.

Depending on the SOC’s organization, various security analysts and teams may be involved in the workflow. For instance, security analysts may monitor the alert queue and triage alerts, while CSIRT team members may respond to incidents. Each organization may have a unique SOC structure.


![8](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.08.23.png)

| Role                                   | Description                                                                                                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tier 1 analyst                         | Continuously monitors the alert queue, triages security alerts, monitors the health of security sensors and endpoints, and collects data and context necessary to initiate Tier 2 work.                                               |
| Tier 2 analyst                         | Performs deep-dive incident analysis by correlating data from various sources, determines if a critical system or data set has been affected, advises on remediation, and provides support for new analytic threat detection methods. |
| Incident response handler              | Manages the incident, executes containment strategies, ensures the incident response process is followed, and may communicate with the business to provide periodic updates.                                                          |
| Forensics specialist                   | Focused on gathering, retaining, and analyzing computer-related data for investigative purposes in a manner that maintains data integrity.                                                                                            |
| Malware reverse engineering specialist | Analyzes malware behaviors in depth to determine tactics, techniques, procedures, and indicators of compromise. May also write signatures to detect, hunt, and prevent malware.                                                       |
| SOC management                         | Manages resources, including personnel, budget, shift scheduling, and technology strategy to meet SLAs; communicates with management and serves as the organizational point person for business-critical incidents.                   |
| Executive                              | Provides overall direction for the SOC and ensures that the SOC meets and maintains defined objectives.                                                                                                                               |
# SOC WMS Integration

Security teams struggle to keep up with the ever-increasing volume of work due to traditional, manual remediation processes. The WMS, the latest technology in the SOC environment, aims to automate incident remediation by receiving security events and alerts from SIEM and pushing information or commands to security devices. These devices execute procedures or configurations to remediate or contain malicious actions.

SOC responsibilities include cybersecurity incident management, vulnerability management, threat intelligence and hunting, network security monitoring and detection, governance and compliance management, and physical security and threat management.

To improve efficiency, the WMS is typically integrated with SIEM, IT operations ticketing management, and other security controls. Integration provides structure to processes involving independent systems. For instance, an optimum WMS may correlate SIEM events, create tickets for SOC analysts, and execute workflows defined for specific events. Some tasks may be automated to enhance efficiency and consistency.

### WMS Integration with SIEM

![7](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.20.38.png)

SIEM, a core integration point for a WMS, captures network audit log data and analyzes log traffic to detect potential and suspicious behavior. Correlation logic, configured as use cases, triggers alerts, notifications, reports, and callouts to configured destinations.

WMS integration with SIEM automates workflows based on alerts, notifications, reports, and callouts, ensuring consistency in reporting and incident response.

### Integration Methods

APIs and frameworks like TAXII are common methods for integrating WMS within a SOC. 

RESTful API uses HTTP requests to retrieve, update, and delete data. REST, the language of the Internet, enables WMSs to communicate with upstream and downstream tools. For instance, a WMS can update a corporate enterprise ticket management system or its own workflow using RESTful APIs.

Command-line APIs, similar to RESTful APIs, are run directly from the command line. WMS can execute one-time commands and retrieve specific information using command-line APIs. For instance, a WMS may query a SIEM tool with SOC to check the status of a use case and confirm if it’s still active or has been rebuilt or tested.

TAXII, a free and open transport mechanism, standardizes the automated exchange of cyber threat information. WMS can apply the industry-recognized TAXII framework to retrieve and exchange information related to specific threats or groups of threats based on its specific threat intelligence or conditions.

# SOC Workflow Automation Example

SOC Automation Importance:
- Mission-critical for organizations as they grow or mature their security capabilities.
SOC Automation Benefits: 
- Optimizes effectiveness and operating speed of the SOC, allows businesses to meet regulatory obligations, and frees up security analysts’ time.
Automation and Orchestration: 
- Automation involves tools and machines executing repeatable actions without human intervention, while orchestration utilizes automation to complete workflows.

![6](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.46.36.png)

By integrating advanced security automation technology, businesses gain significant advantages, such as:

- Enhanced incident management with faster response times, consistent capabilities, and reduced human error risk.
- Playbook evolution for recurring and unique events.
- Shift of analyst focus to critical thinking-demanding issues.
- Time savings and reduced labor costs from eliminating manual efforts.
- Faster detection, containment, and remediation.

However, complex analysis may not suit automation, especially when disparate data sources or incompatible tools are involved. In most cases, analysts still review data outputs, similar to other security monitoring approaches. SIEM, log management, or other security solutions may require human analysis and critical thinking.

### Example SOC Workflow:

A SOC Tier 1 analyst receives an alert and initiates the following workflow:

![5](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.47.01.png)

Each SOC workflow level has several subtasks. 

- Opens a case in the ticketing system.
- Looks up user details in the user directory.
- Looks up the user hostname and IP address.
- Looks up the IP address in the threat intel platform for context.
- Collects user proxy traffic and packet captures.
- Reviews user traffic history with threat intel for context and potential threat impact.
- Assigns severity and priority.
- Escalates the event to Tier 2 for investigation.

Some tasks can be automated, but others, like reviewing user traffic history, may be manual.

![4](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.48.45.png)

Tier 2 SOC analysts perform the following tasks after escalation from Tier 1 analysts:

- Review threat intelligence, packet captures, endpoint indicators of compromise, endpoint log collection, and memory dumps.
- Determine and execute host containment.
- Add evidence collection artifacts to the case and update case details.
- Notify SOC Tier 3 and management.

![3](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.49.20.png)

The SOC Tier 3 forensics and incident handler performs these tasks:

- Remediate machines by reimaging and extracting malicious content.
- Send new indicators to the threat intel platform.
- Provide context and threat summaries for platform updates.
- Update case details and close cases.

![2](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.49.44.png)

Management collects summary and statistics on the case, including time to detect, contain, resolve, and close.

![1](/Course-Notes/.assets/Screenshot_2024-11-09_at_15.50.21.png)
### WMS Products

Many SOC WMS (or SOAR) vendors focus on automating workflows for the SOC. These vendors include:

- Cisco SecureX
- Cisco CloudCenter Action Orchestrator (simplifies workflow creation with a drag-and-drop designer)
- CyberSponse
- IBM Resilient Systems
- Proofpoint Threat Response
- Swimlane

Orchestration and automation can help SOC analysts operate more efficiently. 

# Detecting and Isolating Malicious Devices 

- Before SecureX: Customers receive alarms from Secure Network Analytics based on behavioral detections. Then customer uses these findings to associated it with Secure Endpoint devices and file hashes. With this information they can manually trigger host isolation and hash isolation if needed.

- With SecureX: The workflow will automatically isolate hosts associated with devices that triggered alarms on suspicious excessive communication with a new external server and get notified about isolated hosts and blocked hashes automatically within WebEx teams. The SOC team achieve faster time to response for critical threats.
- Identifies and extracts the source IPs and hashes, isolates infected devices, and blocks malicious files or applications, and notifies the team.

- Network Monitoring and Enrichment: Highlights the use of Secure Network Analytics and AnyConnect to monitor network traffic and gather user and file context for threat detection and response.

- ﻿﻿Customer security team use Secure Network Analytics to detect devices infected with new malware based on behavioral analytics

- ﻿﻿Security team uses detections found to isolate the infected systems and stop malicious files execution.

# [[Quick Reference]]

Key People

- **Karen Scarfone**: Co-author of the NIST Special Publication on Computer Security Incident Handling, providing guidelines for incident response.
- **Tim Grance**: Co-author of the NIST Special Publication, contributing to the development of incident handling best practices.

Fundamental Theories

|Theory/Model|Description|
|---|---|
|**Workflow Types**|Three types: Sequential (linear), State Machine (can return to previous states), Rules-driven (based on rules).|
|**Incident Response Process**|A defined process for handling incidents based on severity, ensuring consistent and timely reporting.|

Key Roles in SOC

|Role|Description|
|---|---|
|**Tier 1 Analyst**|Monitors alerts, triages security alerts, and collects necessary data for further analysis.|
|**Tier 2 Analyst**|Conducts deep-dive analysis, correlates data, and advises on remediation strategies.|
|**Incident Response Handler**|Manages incidents, executes containment strategies, and communicates updates to stakeholders.|
|**Forensics Specialist**|Gathers and analyzes data for investigative purposes while maintaining data integrity.|
|**SOC Management**|Oversees personnel, budget, and technology strategy to meet service level agreements (SLAs).|

Key Products

- **Cisco SecureX**: A platform that integrates security tools and automates workflows for incident response.
- **IBM Resilient Systems**: A WMS that focuses on incident response and management.
- **CyberSponse**: A security orchestration platform that automates workflows and incident response processes.

Facts to Memorize

- SIEM: Security Information and Event Management
- WMS: Workflow Management System
- SOC: Security Operations Center
- SOAR: Security Orchestration, Automation, and Response
- API: Application Programming Interface
- RESTful API: Representational State Transfer API
- TAXII: Trusted Automated eXchange of Indicator Information

Reference Information

- Incident Response Process: Detection, Analysis, Containment, Eradication, Recovery, and Post-Incident Review
- Types of Workflows: Sequential, State Machine, Rules-Driven
- Roles in SOC: Tier 1 Analyst, Tier 2 Analyst, Incident Response Handler, Forensics Specialist, Malware Reverse Engineering Specialist, SOC Management, Executive

Concept Comparisons

|Concept|Description|
|---|---|
|SIEM|Aggregates and analyzes security logs from various sources to detect potential incidents.|
|WMS|Automates incident response processes and manages workflows for handling security events.|
|SOC|A centralized unit that deals with security incidents and threats in an organization.|
|SOAR|Combines security orchestration, automation, and response to improve incident management.|

Cause and Effect

| Cause                                 | Effect                                                                                                |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Introduction of SIEM                  | Improved log aggregation and incident detection capabilities for security analysts.                   |
| Automation of repeatable tasks in SOC | Increased efficiency and allowed analysts to focus on more complex tasks requiring critical thinking. |
| Integration of WMS with SIEM          | Streamlined workflows and improved consistency in incident response and reporting.                    |

# Overview of Security Operations Center (SOC)

### Role of Security Analysts

- Security analysts are responsible for monitoring and analyzing logs from various security and networking tools to identify potential security incidents.
- Traditionally, analysts had to log into multiple devices to review logs, which is time-consuming and inefficient.
- The volume of events can be overwhelming, with rates of hundreds of events per hour, necessitating automation for effective analysis.
- Analysts must possess a deep understanding of network paths and device interactions to effectively correlate logs and identify incidents.

### Challenges in Log Analysis

- Logs from different devices often have inconsistent formats, making correlation difficult.
- Variability in date and time formats can lead to confusion and errors in analysis.
- Incomplete logs may lack critical information such as system names, domain names, or IP addresses, complicating incident identification.
- The introduction of SIEM (Security Information and Event Management) systems has streamlined log aggregation and normalization, improving incident detection.

# Introduction to Workflow Management Systems (WMS)

### Definition and Purpose of WMS

- A WMS is software designed to tag, identify, and track security events from detection to resolution.
- It automates incident response processes, including containment and eradication of malicious actions.
- Unlike SIEM, a WMS does not collect evidence or assist with approvals; it focuses on automating remediation tasks.
- The workflow begins in SIEM, transitions to WMS, and then to individual security devices for action.

### Contextual Use of WMS in SOC

- In a SOC, WMS is often referred to as SOAR (Security Orchestration, Automation, and Response), though terminology may vary by vendor.
- The WMS enhances the efficiency of incident response by automating repeatable tasks, allowing analysts to focus on more complex issues.
- After an incident is confirmed, the WMS coordinates the response efforts among various security tools and personnel.

# Workflow Types in SOC

### Types of Workflows

- ****Sequential Workflows****: These follow a linear progression from one task to the next without reverting to previous stages, often represented in flow charts.
- ****State Machine Workflows****: More complex, allowing for transitions between various states, including returning to previous states as needed.
- ****Rules-Driven Workflows****: Based on sequential workflows, these are guided by specific rules that dictate the flow of tasks.

### Importance of Workflow Management

- Workflows ensure that tasks are executed in a structured manner, improving efficiency and responsiveness in incident handling.
- The SOC management team develops workflow models that standardize operating procedures for incident response.
- Effective workflows can be measured and analyzed for continuous improvement, enhancing overall SOC performance.

# Automation of Repeatable Tasks

### Common Tasks Suitable for Automation

- ****Audit Log Collection and Enrichment****: Automating the retrieval and enhancement of audit logs from various devices as part of SIEM processes.
- ****User Information Lookup****: Automating queries to Active Directory to gather user details such as department and job title.
- ****Device Information Lookup****: Automating DNS queries to obtain device-related information like IP addresses and hostnames.
- ****Notifications and Alerts****: Automating the generation of alerts based on predefined conditions monitored by security analysts.

### Benefits of Automating SOC Tasks

- Automation allows junior staff to focus on more complex tasks that require critical thinking and problem-solving skills.
- Reduces the time taken to respond to incidents by streamlining routine processes.
- Enhances the accuracy and consistency of task execution, minimizing human error.
- Improves overall SOC efficiency and effectiveness in incident management.

# Incident Management and Response Process

### Overview of Incident Management

- The incident management process is initiated once an alert is confirmed as an incident, leading to necessary callouts and personnel contact.
- It may involve law enforcement agencies depending on the severity and nature of the incident.
- A structured incident response process is crucial for effective management, ensuring that incidents are handled according to their severity levels.

### Severity Levels and Response Procedures

- Each incident severity level must have a defined response process to ensure appropriate handling.
- The severity of an incident can change over time, necessitating a flexible response strategy.
- Procedures should be in place to manage incidents as their severity levels change, particularly during monitoring and remediation phases.

### Reporting and Documentation

- Consistent and timely reporting is essential during incident response, with defined notification times for each severity type.
- Incident investigators are responsible for maintaining reporting standards, which can be challenging during shift changes.
- Automation through a Security Operations Center Workflow Management System (SOC WMS) can enhance reporting consistency and reduce manual errors.

# Roles and Responsibilities in a Security Operations Center (SOC)

### SOC Workflow Overview

- The SOC workflow is customized based on organizational needs, involving various tiers of security analysts and teams.
- Different roles within the SOC focus on specific stages of incident management, such as detection, triage, and response.
- The integration of specialized roles enhances the overall effectiveness of incident response efforts.

### Key Roles in SOC

> The following roles are commonly found within a SOC:

- ****Tier 1 Analyst****: Monitors alerts, triages security incidents, and collects necessary data for further analysis.
- ****Tier 2 Analyst****: Conducts in-depth analysis, correlates data, and advises on remediation strategies.
- ****Incident Response Handler****: Manages incidents, executes containment strategies, and communicates updates to stakeholders.
- ****Forensics Specialists****: Focus on data integrity while gathering and analyzing computer-related evidence.
- ****Malware Reverse Engineering Specialists****: Analyze malware to understand its behavior and develop detection signatures.
- ****SOC Management****: Oversees personnel, budget, and technology strategy to meet service level agreements (SLAs).

# SOC Workflow Management System (WMS) Integration

### Importance of WMS in SOC

- The WMS automates remediation processes, addressing the challenges posed by manual incident management.
- It receives security events from Security Information and Event Management (SIEM) systems and executes remediation commands on security devices.
- Integration with SIEM and other systems enhances the efficiency and consistency of SOC operations.

### Processes Managed by WMS

> The WMS is responsible for various processes, including:

1. Cybersecurity incident management
2. Vulnerability management
3. Threat intelligence and hunting
4. Network security monitoring and detection
5. Governance and compliance management
6. Physical security and threat management

### WMS and SIEM Integration

- The WMS serves as a core integration point with SIEM solutions, which capture and analyze audit log data.
- SIEM systems issue alerts based on correlation logic, which can trigger automated workflows in the WMS.
- This integration allows for streamlined incident response processes, improving overall SOC efficiency.

# Overview of SIEM and WMS Integration

### Understanding SIEM Solutions

- SIEM (Security Information and Event Management) solutions monitor and analyze security events in real-time, providing alerts and notifications when specific conditions are met.
- Alerts can be directed to various destinations, including ticketing systems, emails, and SMS, facilitating immediate incident response.
- The integration of SIEM with other systems enhances the overall security posture by automating workflows and ensuring consistency in incident management.

### Benefits of WMS Integration with SIEM

- Integrating WMS (Workflow Management Systems) with SIEM allows for automated workflows based on alerts, improving incident response times.
- Automation ensures consistency in reporting and incident handling, reducing the risk of human error.
- WMS can streamline operations by automating repetitive tasks, allowing analysts to focus on critical decision-making.

# Integration Approaches for WMS in SOC

### API Integration Methods

- APIs (Application Programming Interfaces) are essential for integrating WMS with SIEM, allowing for seamless data exchange between systems.
- RESTful APIs utilize HTTP requests to manage data, enabling WMS to interact with other tools like ticket management systems effectively.
- Command-line APIs allow for executing specific commands directly from the command line, useful for ad hoc queries and operations.

### TAXII Framework for Threat Intelligence

- TAXII (Trusted Automated eXchange of Indicator Information) is a standardized protocol for sharing cyber threat intelligence.
- WMS can leverage TAXII to automate the retrieval and exchange of threat information, enhancing decision-making capabilities.
- This integration is particularly beneficial for WMS that need to respond to specific threat conditions.

# SOC Workflow Automation

### Importance of Automation in SOC

- Automation in SOC operations is critical for managing security incidents efficiently, especially as organizations scale their security capabilities.
- Orchestration of automated tasks reduces the time spent on manual processes, allowing analysts to focus on high-priority issues.
- Automation helps meet regulatory requirements by ensuring timely responses to security incidents.

### Example of SOC Workflow

- A typical SOC workflow begins with a Tier 1 analyst receiving a SIEM alert and performing several tasks to assess the situation.
- Tasks include opening a case, gathering user details, and analyzing threat intelligence to determine the severity of the incident.
- The workflow progresses through Tier 2 and Tier 3 analysts, each with specific responsibilities, ensuring thorough investigation and resolution.

# WMS Products and Vendors

### Leading WMS Solutions for SOC

- Various vendors provide WMS (or SOAR - Security Orchestration, Automation, and Response) solutions tailored for SOC needs.
- Notable products include Cisco SecureX, IBM Resilient Systems, and Swimlane, each offering unique functionalities for workflow automation.
- These tools enhance the efficiency of SOC analysts by automating routine tasks and facilitating better incident management.