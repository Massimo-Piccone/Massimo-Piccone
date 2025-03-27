# [[Quick Reference]]

Key Steps in Threat Investigation

| Step | Description                                                                                                           |
| ---- | --------------------------------------------------------------------------------------------------------------------- |
| 1    | Research the suspicious URL to determine if it is associated with known malware.                                      |
| 2    | Use services like VirusTotal to check the reputation of the URL and gather additional context.                        |
| 3    | Confirm findings with other databases, such as URLhaus, to validate the URL's malicious nature.                       |
| 4    | Conduct a Google exact-match search for the URL to find articles and resources related to it.                         |
| 5    | Investigate the malware associated with the URL for actionable intelligence, such as IOCs (Indicators of Compromise). |


Key Tools/Services

- **VirusTotal**: A service that analyzes files and URLs for viruses, worms, trojans, and other kinds of malicious content.
- **URLhaus**: A project that tracks malware distribution sites and provides information on malicious URLs.
- **Google Search**: A tool for finding additional information and context about suspicious URLs.

Key Findings

- **Malicious URL Confirmation**: Multiple OSINT sources confirmed that the URL is associated with malware.
- **Community Insights**: User comments and reports on VirusTotal provided additional context and references to security reports, such as those from Rapid7.

Key Actions for SOC Analysts

- **Escalate Alerts**: After confirming a true positive, escalate the alert to the Incident Response (IR) team with all gathered OSINT findings.
- **Document Findings**: Keep detailed records of the investigation process and findings for future reference and analysis.

Facts to Memorize

- URL reputation services are essential for identifying malicious domains.
- VirusTotal is a key resource for checking URL and file reputations.
- URLhaus provides information on malware downloads and associated hashes.
- Community reports can provide valuable insights into malware behavior and IOCs.

Reference Information

- Common OSINT tools: VirusTotal, URLhaus, Google search, urlscan.io.
- Types of IOCs: IP addresses, URLs, file hashes, CVE identifiers.
- Importance of community feedback in threat intelligence.

Problem-Solving Steps

1. **Identify the alert**: Start with the suspicious URL provided in the alert.
2. **Check URL reputation**: Use VirusTotal to assess the URL's reputation score.
3. **Cross-reference findings**: Consult URLhaus for additional context on the URL's use in malware.
4. **Conduct a Google search**: Perform an exact-match search for the URL to find articles or reports.
5. **Investigate malware**: Use the information gathered to identify the malware associated with the URL.
6. **Collect IOCs**: Gather IOCs and signatures related to the malware for detection purposes.
7. **Escalate findings**: Compile all findings and escalate the alert to the Incident Response team.

Cause and Effect

| Cause                                      | Effect                                                                           |
| ------------------------------------------ | -------------------------------------------------------------------------------- |
| Alert indicates suspicious traffic to C2   | Initiates OSINT investigation to determine the nature of the traffic.            |
| Confirmation of malicious URL from sources | Validates the need for further investigation and potential incident response.    |
| Gathering IOCs and signatures              | Enables proactive measures to detect and mitigate the identified malware.        |
| Escalation to IR team                      | Ensures that the incident is addressed by specialized personnel for remediation. |

# Understanding the Use Case

![8](/Course-Notes/.assets/Pasted_image_20241202225448.png)
### Overview of OSINT in Cybersecurity

- OSINT (Open Source Intelligence) refers to the collection and analysis of publicly available information to support security operations.
- SOC (Security Operations Center) Tier 1 analysts utilize OSINT to investigate alerts and potential threats.
- The primary goal is to determine the legitimacy of alerts and identify malicious activities.
- OSINT can include data from various sources such as social media, forums, and specialized databases.
- Effective use of OSINT can significantly reduce response times and improve threat detection.

### The Role of SOC Tier 1 Analysts

- SOC Tier 1 analysts are the first line of defense in cybersecurity, responsible for monitoring alerts and conducting initial investigations.
- They assess the severity of alerts and prioritize them based on potential impact.
- Analysts use various tools and techniques to gather information about suspicious activities.
- Communication with higher-tier analysts (Tier 2 and Tier 3) is crucial for escalating significant threats.
- Continuous learning and adaptation to new threats are essential for SOC analysts.

# Steps in Threat Investigation Using OSINT
![7](/Course-Notes/.assets/Pasted_image_20241202225502.png)
### Initial Alert Triage

- Upon receiving an alert about suspicious traffic to a C2 (Command and Control) domain, the analyst begins the investigation.
- The first step is to gather the URL associated with the alert, e.g., `http://72.X.Y.Z/[malicious_script].bat`.
- Analysts should utilize URL reputation services to assess the URL's safety and gather additional context.
- Tools like VirusTotal can provide a reputation score and community feedback on the URL.
- Keeping browser tabs open for multiple sources allows for cross-referencing information.

![6](/Course-Notes/.assets/Pasted_image_20241202225526.png)
### Utilizing OSINT Tools

- ****VirusTotal****: Submit the suspicious URL to check for malicious indicators and community reports.
- ****URLhaus****: This database provides information on URLs used for malware distribution, including associated malware hashes.
- ****Google Search****: Conduct an exact-match search for the URL to find articles and resources that discuss the threat.
- Analysts should document findings from each tool to build a comprehensive view of the threat.
- Cross-referencing multiple sources helps confirm the malicious nature of the URL.

![5](/Course-Notes/.assets/Pasted_image_20241202225530.png)
# Deepening the Investigation

![4](/Course-Notes/.assets/Pasted_image_20241202225540.png)
### Identifying Associated Malware

- After confirming the URL is malicious, the next step is to identify the specific malware involved.
- Analysts can revisit the VirusTotal Community tab for user comments and reports related to the URL.
- Community feedback may include references to well-known security reports, such as those from Rapid7.
- Gathering information about the malware can lead to actionable intelligence, including IOCs (Indicators of Compromise) and signatures.
- Understanding the malware's behavior is crucial for developing detection and response strategies.

![3](/Course-Notes/.assets/Pasted_image_20241202225555.png)
### Gathering Additional Evidence

![2](/Course-Notes/.assets/Pasted_image_20241202225602.png)

- Analysts should look up the CVE (Common Vulnerabilities and Exposures) number associated with the malware for detailed information.
- The MITRE ATT&CK framework and NVD (National Vulnerability Database) are valuable resources for understanding vulnerabilities.
- File hashes from URLhaus can be submitted to reputation services to check for known malicious files.
- Using sandbox environments to analyze the malware can provide insights into its behavior and impact.
- Collecting comprehensive evidence is essential for escalating the alert to the Incident Response (IR) team.

![1](/Course-Notes/.assets/Pasted_image_20241202225624.png)
# Conclusion and Next Steps

### Confirming the Alert

- After thorough investigation and evidence collection, analysts can confirm whether the alert is a true positive.
- All findings should be documented and presented to the IR team for further action.
- Analysts should ensure that all relevant data, including IOCs and malware signatures, are included in the escalation report.
- Continuous monitoring and follow-up on the incident are necessary to mitigate any potential impact.
- Learning from each investigation helps improve future alert triage processes.
