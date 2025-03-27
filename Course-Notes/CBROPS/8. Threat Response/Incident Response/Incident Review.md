%% #review %%
## [[Incident Response Planning]]

- Enables an efficient recovery from security incidents. 
	- Used to prevent or minimize disruption of critical computing services, 
	- Minimize the loss of proprietary and confidential information, 
	- and facilitate information exchange among the different groups 
- That are responsible for:
	- Detecting, 
	- Identifying, 
	- Reporting, 
	- Containing, 
	- Eradicating, and
	- Repairing security incidents.

An effective IRP requires answers to these questions:
- What are the ==assets== that are being protected?
- What are the ==threats== to the assets?
- How are threats ==detected==?
- How will the organization ==respond== to threats?
This is the foundation for security monitoring and incident response processes.
## [[Incident Response Life Cycle]]

**RACI Model**: A communication framework that defines roles in incident response 
==Responsible, Accountable, Consulted, and Informed==.

Incident response life cycle phases: 

| Stage                    | Description                                                                                                               | Key Activities                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Preparation              | Prepare the company team and resources for a security incident.                                                           | Educate users and IT staff on incident response.<br><br>Develop and maintain proper documentation.<br><br>Plan data retention, incident response roles, and responsibilities (RACI).                                                   |
| Identification           | Continuously monitor for cyber threats and activate the incident response team when a true positive incident is detected. | SOC analyst or incident response team investigates the incident.<br><br>May contact CERT/CC or other security intelligence sources for threat information.                                                                             |
| Analysis                 | Quickly analyze and validate each incident, following a predefined process and documenting steps.                         | Initial analysis to determine the scope of the incident.<br><br>Identify affected networks, systems, or applications.<br><br>Determine the origin of the incident.<br><br>Identify attack methods and vulnerabilities being exploited. |
| Containment              | Critical decision to limit the impact of the incident.                                                                    | Determine the incident’s scope and affected devices.<br><br>Assess network reachability and containment setup time.<br><br>Consider the business impact of containment.                                                                |
| Eradication and Recovery | Remove the root cause of the incident, restore data and systems, and monitor for recurrence.                              | Investigate the origin of the incident and remove malicious code.<br><br>Restore data and software from backups.<br><br>Implement tactical and strategic fixes.                                                                        |
| Lessons Learned          | Analyze the incident, perform an FMEA, and document the response.                                                         | Analyze the incident response process.<br><br>Perform an FMEA against the incident.<br><br>Document the incident response and lessons learned.                                                                                         |
| Reporting                | Report the incident at predefined intervals based on severity.                                                            | Notify relevant stakeholders, including the CIO, head of information security, system owner, HR, public affairs, legal department, and law enforcement.                                                                                |
### Importance of a Structured Approach

- A structured incident response process helps organizations minimize damage and recover more quickly from security incidents.
- It ensures that all team members understand their roles and responsibilities, which is crucial during high-pressure situations.
- The RACI model (Responsible, Accountable, Consulted, Informed) is often used to clarify roles within the incident response team.
- By following a life-cycle approach, organizations can continuously improve their incident response capabilities based on past experiences.

## [[Incident Response Policy Elements]]

Primary incident response policy elements include:

| Element                         | Description                                                                                               |
| ------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Mission, Strategies, and Goals  | Determine incident response capability.                                                                   |
| Organizational Capability       | Need a functional CSIRT with trained incident responders.<br>Staffing education and Org Security Culture. |
| Incident Response Team          | Everyone in the organization has a role to play.                                                          |
| Threats and Attacks             | Attackers use social engineering techniques.                                                              |
| Stakeholder Engagement          | Stakeholders should know their roles during a security event.                                             |
| Incident Response Plan Approval | Senior management must approve the incident response plan.                                                |
| Incident Response Process       | The incident response team continuously communicates during the reporting phase.                          |
| Metrics and Measurement         | Metrics measure incident response capability and effectiveness.                                           |
| Incident Response Plan Review   | Annual reviews ensure maturation and fulfillment of goals.                                                |
| Organization missions           | Explains how the incident response policy supports the organization’s overall missions.                   |
## [[Incident Attack Categories]]

| Attack Type                         | Description                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------------------- |
| External or removable media attacks | Malicious code spreading onto systems from infected USB flash drives or other peripheral devices. |
| Attrition attacks                   | Compromising, degrading, or destroying systems, networks, or services using brute-force methods.  |
| Web attacks                         | Occurring from or against websites or web-based applications.                                     |
| Email attacks                       | Involving executing malicious code via email messages or attachments.                             |
| Impersonation attacks               | Replacing benign elements with malicious ones.                                                    |
| Improper usage attacks              | Resulting from violating acceptable usage policies by authorized users.                           |
| Equipment loss or theft attacks     | Involving the loss or theft of computing devices or media.                                        |
| Other attacks                       | An attack that does not fit into another category                                                 |
## [[Reference US-CERT Incident Categories]]

| Description                                                                                                                                                                                                                                                                                       | Reporting Timeframe                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| CAT 0                                                                                                                                                                                                                                                                                             | Exercise/Network Defense Testing                                                                                                                 |
| Used during state, federal, national, and international exercises and approved activity testing of internal and external network defenses or responses.                                                                                                                                           | Not applicable; this category is for internal use of each agency during exercises.                                                               |
| CAT 1                                                                                                                                                                                                                                                                                             | Unauthorized Access                                                                                                                              |
| An individual will gain logical or physical access without permission to a federal agency network, system, application, data, or other resource                                                                                                                                                   | Within 1 hour of discovery and detection.                                                                                                        |
| CAT 2                                                                                                                                                                                                                                                                                             | Denial of Service (DoS)                                                                                                                          |
| An attack that successfully prevents or impairs the normal authorized functionality of networks, systems, or applications by exhausting resources. This activity includes being the victim or participating in the DoS.                                                                           | Within 2 hours of discovery and detection, if the successful attack is still ongoing and the agency is unable to successfully mitigate activity. |
| CAT 3                                                                                                                                                                                                                                                                                             | Malicious Code                                                                                                                                   |
| A successful installation of malicious software (for example, virus, worm, Trojan horse, or other code-based malicious entity) that infects an operating system or application. Agencies are not required to report malicious logic that has been successfully quarantined by antivirus software. | Daily Note: Within 1 hour of discovery and detection if widespread across agency.                                                                |
| CAT 4                                                                                                                                                                                                                                                                                             | Improper Usage                                                                                                                                   |
| A person violates acceptable computing use policies.                                                                                                                                                                                                                                              | Weekly                                                                                                                                           |
| CAT 5                                                                                                                                                                                                                                                                                             | Scans/Probes/Attempted Access                                                                                                                    |
| Any activity that seeks to access or identify a federal agency computer, open ports, protocols, service, or any combination for later exploit. This activity does not directly result in a compromise or denial of service.                                                                       | Monthly Note: If system is classified, report within 1 hour of discovery.                                                                        |
| CAT 6                                                                                                                                                                                                                                                                                             | Investigation                                                                                                                                    |
| Unconfirmed incidents that are potentially malicious or anomalous activity that is deemed by the reporting entity to warrant further review.                                                                                                                                                      | Not applicable; this category is for the use of each agency to categorize a potential incident that is currently being investigated.             |
## [[Regulatory Compliance Incident Response Requirements]]

|Compliance Regulation|Description|
|---|---|
|PCI DSS|Protects credit card holder data and requires an incident response plan for breaches.|
|Sarbanes-Oxley Act|Aims to prevent misleading financial information and protect shareholders.|
|HIPAA|Safeguards medical information and ensures patient confidentiality.|
## [[CSIRT Categories]]

CSIRT is responsible for ==receiving==, ==reviewing==, and ==responding== to security incidents.

![2](/Course-Notes/.assets/Pasted_image_20241204110336.png)

Ensure **company**, **system**, and **data preservation**
by investigating security incidents and preventing them through 
- Threat assessment, 
- Detection, 
- Mitigation planning, 
- Incident trend analysis, and 
- Security architecture review.

| Type                 | Description                                                                                 | Examples                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Internal CSIRTs      | Provide incident handling services to their parent organization.                            | Bank CSIRT, Manufacturing Company CSIRT, University CSIRT, Federal Agency CSIRT |
| National CSIRTs      | Provide incident handling services to a country.                                            | JPCERT/CC, Singapore Computer Emergency Response Team (SingCERT)                |
| Coordination Centers | Coordinate and facilitate incident handling across various CSIRTs.                          | CERT Coordination Center, US-CERT                                               |
| Analysis Centers     | Synthesize data from various sources to determine trends and patterns in incident activity. | N/A                                                                             |
| Vendor Teams         | Handle reports of vulnerabilities in their software or hardware products.                   | Cisco Product Security Incident Response Team (PSIRT)                           |
## [[CSIRT Framework]]

A CSIRT can be described in terms of:
- ==What it sets out to do== 
- ==For whom==
- ==What its roots look like== 
- ==And who its peers are== 

| Description                 | Purpose                                                                                                                |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Mission Statement           | Defines the high-level goals, objectives, and priorities of the CSIRT.                                                 |
| Constituency                | Defines the specific community the CSIRT serves and its relationship to that community.                                |
| Organizational Structure    | Defines the position of the CSIRT within the organization it serves.                                                   |
| Relationship to Other Teams | Describes how the CSIRT interacts with other security teams within the organization or across different organizations. |
## [[CSIRT Incident Handling Services]]

![1](/Course-Notes/.assets/Pasted_image_20241204115411.png)

| Function                       | Description                                                                                                                         |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Triage**                     | Provides a single point of contact for incoming information, sorts and prioritizes events, and assigns tracking numbers.            |
| **Handling**                   | Offers support and guidance for suspected or confirmed incidents, analyzes reports, and determines appropriate responses.           |
| **Feedback**                   | Provides feedback on issues not directly related to specific incidents, including responses to media inquiries and regular updates. |
| **Announcement<br>(Optional)** | Generates tailored information for constituents about ongoing threats and protective measures.                                      |
- CSIRTs provide both ==reactive== and ==proactive== services
- A well-structured incident handling can greatly improve resilience against cyber threats.
- Collaboration and communication with stakeholders are essential for achieving these goals.