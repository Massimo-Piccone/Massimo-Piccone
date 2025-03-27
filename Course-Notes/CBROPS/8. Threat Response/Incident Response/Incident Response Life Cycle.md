# [[Quick Reference]]

Key People

- **SOC Analyst**: Responsible for monitoring security systems and identifying potential incidents.
- **Incident Response Team**: A group of professionals tasked with managing and responding to security incidents.
- **CERT**: Computer Emergency Response Team, provides resources and information on current threats.

Key Regulations/Legislation

- **NIST Guidelines**: Standards and guidelines published by the National Institute of Standards and Technology for incident response processes.
- **SANS Institute**: Provides training and resources for cybersecurity professionals, including incident response best practices.

Key Communication Techniques

- **RACI Model**: A communication framework that defines roles in incident response as Responsible, Accountable, Consulted, and Informed.
- **Incident Reporting**: Establishing clear protocols for notifying stakeholders about incidents, including legal considerations.

Facts to Memorize

- NIST: National Institute of Standards and Technology
- SANS: SysAdmin, Audit, Network, and Security
- RACI: Responsible, Accountable, Consulted, Informed
- FMEA: Failure Mode and Effects Analysis

Reference Information

- Incident response life cycle phases: Preparation, Identification, Analysis, Containment, Eradication and Recovery, Lessons Learned, Reporting
- Key roles in incident response: SOC Analyst, Incident Response Team, CERT (Computer Emergency Response Team)
- Types of reporting: Internal and External

Problem-Solving Steps
1. **Preparation**: Train staff, document processes, and establish roles.
2. **Identification**: Monitor systems and detect incidents.
3. **Analysis**: Validate incidents and assess their scope.
4. **Containment**: Decide on containment strategies based on the incident's nature.
5. **Eradication & Recovery**: Remove threats and restore systems from backups.
6. **Lessons Learned**: Review the incident for future improvements.
7. **Reporting**: Notify stakeholders and document the incident.

Key Terms/Concepts

- **Incident Response Life Cycle**: A structured approach to managing and responding to security incidents, typically consisting of several phases.
- **Preparation Phase**: The initial phase focused on getting the team and resources ready to handle incidents, including training and documentation.
- **Identification Phase**: Involves continuous monitoring and threat hunting to detect incidents and activate the response team.
- **Containment Phase**: Critical decisions are made to limit the impact of the incident, considering various factors such as scope and urgency.
- **Lessons Learned Phase**: Analyzing the incident to understand its causes and improve future responses.
# Table

| Stage                    | Description                                                                                                               | Key Activities                                                                                                                                                                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Preparation              | Prepare the company team and resources for a security incident.                                                           | Educate users and IT staff on incident response.<br><br>Develop and maintain proper documentation.<br><br>Plan data retention, incident response roles, and responsibilities (RACI).                                                   |
| Identification           | Continuously monitor for cyber threats and activate the incident response team when a true positive incident is detected. | SOC analyst or incident response team investigates the incident.<br><br>May contact CERT/CC or other security intelligence sources for threat information.                                                                             |
| Analysis                 | Quickly analyze and validate each incident, following a predefined process and documenting steps.                         | Initial analysis to determine the scope of the incident.<br><br>Identify affected networks, systems, or applications.<br><br>Determine the origin of the incident.<br><br>Identify attack methods and vulnerabilities being exploited. |
| Containment              | Critical decision to limit the impact of the incident.                                                                    | Determine the incident’s scope and affected devices.<br><br>Assess network reachability and containment setup time.<br><br>Consider the business impact of containment.                                                                |
| Eradication and Recovery | Remove the root cause of the incident, restore data and systems, and monitor for recurrence.                              | Investigate the origin of the incident and remove malicious code.<br><br>Restore data and software from backups.<br><br>Implement tactical and strategic fixes.                                                                        |
| Lessons Learned          | Analyze the incident, perform an FMEA, and document the response.                                                         | Analyze the incident response process.<br><br>Perform an FMEA against the incident.<br><br>Document the incident response and lessons learned.                                                                                         |
| Reporting                | Report the incident at predefined intervals based on severity.                                                            | Notify relevant stakeholders, including the CIO, head of information security, system owner, HR, public affairs, legal department, and law enforcement.                                                                                |
# Overview of the Incident Response Life Cycle

![1](/Course-Notes/.assets/Pasted_image_20241203164645.png)
### Phases of Incident Response

- The incident response life cycle consists of several phases: Preparation, Identification, Analysis, Containment, Eradication and Recovery, Lessons Learned, and Reporting.
- Each phase is interconnected and builds upon the previous one, ensuring a comprehensive approach to managing security incidents.
- The life cycle is derived from standardized processes published by organizations like NIST and SANS, which provide frameworks for effective incident management.
- Organizations may adapt these phases to fit their specific needs, but common principles remain consistent across different entities.
- A diagram typically illustrates these phases, emphasizing the cyclical nature of incident response.

### Importance of a Structured Approach

- A structured incident response process helps organizations minimize damage and recover more quickly from security incidents.
- It ensures that all team members understand their roles and responsibilities, which is crucial during high-pressure situations.
- The RACI model (Responsible, Accountable, Consulted, Informed) is often used to clarify roles within the incident response team.
- By following a life-cycle approach, organizations can continuously improve their incident response capabilities based on past experiences.