## [[Quick Reference]]

Fundamental Theories

|Theory/Model|Description|
|---|---|
|**Machine Learning**|A subset of artificial intelligence that enables systems to learn from data and improve over time without being explicitly programmed.|
|**Behavior-Based Detection**|A detection method that focuses on identifying abnormal behavior in network traffic rather than relying solely on known signatures.|

Key Tools/Systems

- **Cisco Cognitive Intelligence**: A threat analytic system that excels in detecting zero-day threats by analyzing network behavior over time.
- **IPS Signatures**: Intrusion Prevention System signatures that help block known malware attacks based on established patterns.

Key Events

- **DNS Changer Trojan**: A malware that alters DNS settings on infected hosts, allowing attackers to control and intercept network traffic. It exemplifies the need for advanced detection methods like those provided by Cisco Cognitive Intelligence.

Key Features of Threat Analytic Systems

| Feature                         | Description                                                                                                 |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **False Positive Rate**         | Threat analytic systems can achieve a false positive rate as low as 0.000001%, enhancing their reliability. |
| **Real-Time Threat Monitoring** | Provides security analysts with immediate updates on threat levels and behaviors within the network.        |
| **Interactive Dashboard**       | Allows analysts to navigate incidents and access detailed information for investigation and remediation.    |

Facts to Memorize

- False positive rate of threat analytic systems can be as low as 0.000001%.
- The DNS Changer Trojan changes DNS settings on infected hosts.
- Cisco Cognitive Intelligence identifies threats by analyzing network traffic behavior.

Reference Information

- Cisco Cognitive Intelligence (formerly Cognitive Threat Analytics) uses machine learning and anomaly detection.
- Threat analytic systems correlate large amounts of data to identify security breaches.
- Ransomware detection is a key feature of threat analytic systems.

Concept Comparisons

|Feature|Traditional Signature-Based Detection|Threat Analytic Systems|
|---|---|---|
|Detection Method|Relies on known signatures|Uses behavioral analysis and anomaly detection|
|False Positive Rate|Generally higher|Can be as low as 0.000001%|
|Speed of Detection|Slower, often reactive|Faster, proactive detection|
|Adaptability to New Threats|Limited, requires updates|High, can identify novel threats|
|Focus of Analysis|Specific known threats|General behavior and anomalies|

Cause and Effect

|Cause|Effect|
|---|---|
|Emergence of new malware types|Increased need for advanced threat detection systems|
|Use of behavioral analysis in threat detection|Faster identification of security breaches|
|Escalation of threat severity|Immediate alerts for security analysts to respond|
|Implementation of machine learning|Enhanced ability to detect zero-day threats|

# Overview of Threat Analytic Systems

### Importance of Threat Detection

- Preventing malware attacks is more manageable when dealing with established threats that have documented signatures.
- Effective use of IPS signatures, updated IP/domain block lists, and antivirus signatures can mitigate known attacks.
- Unknown malware poses a significant challenge for detection and prevention, necessitating advanced tools and strategies.
- Security analysts must be well-trained and equipped to respond quickly to breaches to minimize damage.
- The role of threat analytic systems is crucial in identifying generic security breaches without known signatures.

### Functionality of Threat Analytic Systems

- Threat analytic systems correlate large data sets using statistical and mathematical models to identify emerging threats.
- They detect Command and Control (CnC) activity associated with malware, enhancing the speed of threat discovery.
- These systems utilize behavioral analysis and anomaly detection to identify symptoms of malware infections or data breaches.
- Achieving a false positive rate as low as 0.000001% allows for sensitive detection of a wide range of threats.
- Automatic behavior-based machine learning capabilities further streamline the detection process.

# Case Study: Cisco Cognitive Intelligence

### Overview of Cisco Cognitive Intelligence

- Formerly known as Cognitive Threat Analytics (CTA), it employs network traffic behavior analysis and machine learning.
- It excels in zero-day threat detection by analyzing historical data to identify abnormal events.
- The system's big data capabilities allow it to detect smaller incidents that could lead to significant damage.
- Cisco Cognitive Intelligence provides a dashboard that summarizes threats by risk level, aiding quick assessments by security analysts.

![2](/Course-Notes/.assets/Pasted_image_20241129230705.png)
### Dashboard Features and Functionality

- The health status section of the dashboard displays an overview of threats, categorized by risk level from critical to low.
- The 'Relative Threat Exposure' section benchmarks the organization's threat level against global trends and similar networks.
- Specific behaviors of detected threats are highlighted, allowing analysts to focus on confirmed and high-confidence incidents.
- The dashboard tracks escalations in threat severity, providing real-time updates on risk levels and associated behaviors.

![1](/Course-Notes/.assets/Pasted_image_20241129230712.png)
# Threat Detection and Response Strategies

### Behavioral Analysis and Anomaly Detection

- Behavioral analysis involves monitoring network traffic to identify deviations from normal patterns, indicating potential threats.
- Anomaly detection systems can flag unusual activities that may signify malware infections or data breaches.
- Cisco Cognitive Intelligence uses these techniques to provide insights into real-time threats and their impact on users.
- Specific behaviors, such as ransomware activity or data exfiltration, are tracked to enhance response strategies.

### Incident Management and Remediation

- The CTA dashboard allows security analysts to interactively investigate incidents by clicking on them for detailed information.
- Each incident includes critical data such as usernames, specific behaviors, and timestamps for effective tracking.
- Escalation of threats is monitored, with changes in risk levels and new behaviors documented for timely remediation.
- The system helps analysts focus on confirmed breaches, streamlining the remediation process and reducing response times.