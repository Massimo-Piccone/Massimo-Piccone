## [[Quick reference]]

Key Processes

| Process Step           | Description                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Posting a Hot Threat   | Security analysts can initiate a hot threat by logging into a portal and providing necessary details about the threat. |
| Reviewing a Hot Threat | A senior investigator reviews the posted threat to validate its criteria and add context.                              |
| Monitoring Hot Threats | The SOC team conducts automated hunts through data streams to detect matches with hot threat IOCs.                     |
| Retiring Hot Threats   | Threats are retired from the dashboard after 30 days or when their importance diminishes significantly.                |

Key Challenges

- **Integration into Workflow**: SOCs often struggle to effectively incorporate the hot threat dashboard into their existing processes.
- **Maintaining Relevance**: Ensuring that the dashboard remains updated with current threats while retiring outdated ones can be challenging.

Key Intelligence Sources

- **Talos**: A threat intelligence organization that provides insights and data on emerging threats.
- **ISACs (Information Sharing and Analysis Centers)**: Organizations that facilitate the sharing of information about cybersecurity threats among members.
- **Open Source Intel-sharing Forums**: Platforms where security professionals share information about vulnerabilities and threats.

Key Communication Techniques

- **Traffic Light Protocol (TLP)**: A system used to classify and share sensitive information based on four color-coded designations (Red, Amber, Green, White) to control the flow of information.

Facts to Memorize

- CVSS base score thresholds: High (7.0 or greater), Medium (4.0 - 6.9)
- TLP color codes: Red, Amber, Green, White
- Hot threats should be monitored for a maximum of 30 days before retirement.

Reference Information

- CVSS (Common Vulnerability Scoring System): A standard for assessing the severity of security vulnerabilities.
- IOCs (Indicators of Compromise): Artifacts observed on a network or in operating system files that indicate a potential intrusion.
- SOC (Security Operations Center): A centralized unit that deals with security issues on an organizational and technical level.

Concept Comparisons

|Concept|Description|Key Differences|
|---|---|---|
|Hot Threat Dashboard|A tool for monitoring current high-priority threats in a network.|Focuses on a limited number of threats for efficiency.|
|Traditional Monitoring|Continuous monitoring of all threats without prioritization.|May lead to information overload and less effective response to critical threats.|

Cause and Effect

| Cause                                             | Effect                                                                                      |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Newly disclosed vulnerabilities with high CVSS    | Triggers a fire-drill to assess risk and verify detection capabilities against the network. |
| Active exploitation of medium CVSS threats        | May elevate the urgency of monitoring and response efforts.                                 |
| Reliable intelligence indicating targeted attacks | Initiates focused monitoring and investigation of specific threats.                         |
| Diminishing IOCs over time                        | Leads to the retirement of threats from the hot threat dashboard after 30 days.             |

# Overview of Hot Threats

### High Impact Vulnerabilities

- Notable vulnerabilities include Logjam, Freak, Shellshock, BEAST, POODLE, and Heartbleed, which have significantly impacted network security.
- Each new vulnerability necessitates a risk assessment and verification of detection capabilities by analysts.
- Threat intelligence partners and law enforcement agencies provide bulletins and warnings, requiring heightened vigilance.
- New threats often emerge without available patches, evading even well-designed security controls, emphasizing the need for a hot threat monitoring process.

### Importance of a Hot Threat Dashboard

- A hot threat dashboard visually represents currently **monitored** threats, providing quick insights into top concerns for network security.
- Threats are dynamically added or retired based on specific criteria to ensure the dashboard remains current and actionable.
- Daily monitoring of intelligence sources and vulnerability reports is essential for identifying emerging threats.
- The dashboard aids in prioritizing threats, focusing on fewer than 15 at a time to maximize efficiency and impact.

# Hot Threat Process

![1](/Course-Notes/.assets/Pasted_image_20241129223425.png)
### Criteria for Recording Hot Threats

- Newly disclosed vulnerabilities with a CVSS base score of 7.0 or higher are recorded as hot threats.
- Medium CVSS scores may be considered if there is active exploitation and the environment is vulnerable.
- Reliable intelligence indicating targeted attacks from sources like Talos and ISACs can trigger hot threat status.
- Native intelligence, such as observed anomalies or surges in security alerts, can also lead to a threat being classified as hot.

### Flow of the Hot Threat Process

- Analysts review intelligence sources to determine if identified threats require tracking and attention.
- The life cycle of a hot threat includes steps for monitoring, analysis, and eventual retirement of threats.
- A flow diagram can be utilized to visualize the process and ensure relevant threats are accurately represented on the dashboard.

# Managing Hot Threats

### Posting and Reviewing Hot Threats

- Any security analyst can initiate a hot threat by logging into the portal and providing necessary details.
- The Traffic Light Protocol (TLP) governs the sharing of sensitive information, with four color-coded designations: Red, Amber, Green, and White.
- A senior investigator reviews posted threats to validate criteria and add context, activating prioritized monitoring across shifts.

### Monitoring and Retiring Hot Threats

- The SOC team conducts automated hunts through customer data streams to match hot threat indicators of compromise (IOCs).
- Successful attacks are analyzed, and customers are notified with guidance to mitigate further harm.
- Hot threats are retired after 30 days or when their importance diminishes, but older threats remain searchable for IOCs.

# Challenges and Considerations

### Challenges in Implementing a Hot Threat Dashboard

- SOCs face difficulties in integrating the hot threat dashboard into existing workflows and processes.
- The dashboard provides direction for new hunts but requires further development to maximize its utility.
- Continuous evaluation of the dashboard's effectiveness is necessary to ensure it meets the needs of the SOC.

