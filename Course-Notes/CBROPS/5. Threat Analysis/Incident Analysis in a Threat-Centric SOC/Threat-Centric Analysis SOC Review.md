%% #review %%
# [[Classic Kill Chain Model Overview]]


![8](/Course-Notes/.assets/Pasted_image_20241130105545.png)

| **Topic**                        | **Details**                                                                                                                                     |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Overview of the Kill Chain Model** | A framework to understand and analyze the stages of a cyber attack, helping defenders identify and mitigate threats at various points.           |
| **Definition and Importance**     | Developed by Lockheed Martin to improve cybersecurity strategies and responses.                                                                 |
|                                   | Emphasizes the sequential nature of attacks; disrupting any phase can prevent the attack from succeeding.                                        |
| **Phases of the Kill Chain**      | Consists of seven phases: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command-and-Control, and Actions on Objectives.     |
|                                   | Each phase is a critical step in the attack lifecycle, providing opportunities for detection and response.                                       |
|                                   | Understanding these phases helps organizations implement targeted defenses and improve incident response strategies.                            |
## Detailed Analysis of Each Phase
### Phase 1: Reconnaissance
| **Topic**                           | **Details**                                                                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Understanding Reconnaissance**    | Initial phase of the cyber kill chain, focuses on intelligence gathering about potential targets.                                                |
|                                     | Analyzes publicly available info like company websites, social media, and news articles to identify vulnerabilities and infiltration points.      |
|                                     | Goal: Assess if a target network is worth attacking based on perceived security of assets.                                                      |
| **Information Gathering Techniques** | Threat actors search for employee names, contact info, and roles through social media and public records.                                        |
|                                     | Publicly available info exploited for social engineering attacks, targeting specific individuals.                                               |
|                                     | Identifying forward-facing servers and critical systems helps narrow down attack vectors.                                                       |
| **Domain Registration and Email Harvesting** | Domain registration reveals valid email addresses for phishing campaigns (e.g., cisco.com).                                                       |
|                                     | Tools like CentralOps.net provide detailed WHOIS records, including technical contacts and emails for targeted attacks.                         |
|                                     | Naming conventions for email addresses help build comprehensive lists of potential targets.                                                    |
| **Case Study: Cisco Domain Lookup** | Example of cisco.com shows how threat actors can extract valuable info from domain lookups.                                                      |
|                                     | WHOIS records provide insights into the organization’s structure and potential vulnerabilities.                                                |
|                                     | Ability to deduce employee roles and contact information enhances the attacker's targeting capabilities.                                         |
### Phase 2: Weaponization
| **Topic**                           | **Details**                                                                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Goals of Weaponization**          | Involves creating a cyber weapon tailored to vulnerabilities identified during reconnaissance.                                                     |
|                                     | Objective: Exploit specific weaknesses in the target system to gain access or disrupt operations.                                                |
|                                     | Successful attacks require only one effective access vector to breach the organization.                                                         |
| **Types of Cyber Weapons**          | Common cyber weapons: viruses, code injections, phishing campaigns, and exploits for system vulnerabilities.                                     |
|                                     | Tools like Metasploit provide pre-developed exploits for attackers and defenders to identify security issues.                                   |
|                                     | Challenge for attackers: select weapons that are not easily detectable by security systems.                                                    |
| **Zero-Day Exploits**               | Exploit vulnerabilities unknown to the software vendor with no available patches.                                                                |
|                                     | Dangerous as they can bypass traditional detection methods.                                                                                      |
|                                     | Attackers may develop custom weapons to create zero-day exploits, enhancing their chances of success.                                            |
| **Case Study: Metasploit Tool**     | Metasploit is used for penetration testing and vulnerability assessment, showcasing available exploits.                                           |
|                                     | The tool delivers payloads for attackers and helps defenders strengthen security.                                                                |
|                                     | Understanding Metasploit's capabilities is crucial for both attackers and defenders in cybersecurity.                                             |
### Phase 3: Delivery

| **Topic**                           | **Details**                                                                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Delivery Mechanisms**             | Refers to transmitting the malicious payload to the target through various channels.                                                            |
|                                     | Common methods: email attachments, phishing emails, malicious URLs, USB devices.                                                                |
|                                     | Each method is tailored to the specific target to increase success likelihood.                                                                  |
| **Techniques for Undetected Delivery** | Minimizing detection risks using code obfuscation and encryption.                                                                                |
|                                     | Attackers disguise payloads as legitimate software to evade security measures.                                                                  |
|                                     | Understanding detection systems helps attackers refine their delivery methods.                                                                  |
| **Example of Phishing Campaigns**   | Phishing emails often contain malicious links that lead to harmful websites to install malware.                                                  |
|                                     | Phishing relies on social engineering to manipulate users into clicking on malicious links.                                                     |
|                                     | Awareness of phishing tactics is crucial for individuals and organizations to protect against attacks.                                           |
| **Case Study: Phishing Email Analysis** | Analyzing suspect emails reveals tactics used by threat actors to deceive users.                                                                |
|                                     | Red flags in emails (e.g., suspicious URLs, poor grammar) help users avoid phishing attempts.                                                  |
|                                     | Continuous education on phishing recognition is vital for enhancing organizational security.                                                   |
### Phase 4: Exploitation

| **Topic**                   | **Details**                                                                                                                                   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Phase 4: Exploitation**    | Occurs after the delivery of malicious code, where attackers exploit vulnerabilities in applications, operating systems, or user behavior.   |
|                             | Common vulnerabilities: outdated software, misconfigured systems, and social engineering tactics targeting users.                            |
|                             | The choice of exploit is crucial; selecting the wrong one can lead to detection or unintended consequences, such as system crashes.          |
### Phase 5: Installation
| **Topic**                     | **Details**                                                                                                                                     |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Phase 5: Installation**      | Involves establishing a backdoor for persistent access to the compromised system, allowing attackers to return without detection.               |
|                               | Persistence techniques survive system reboots and evade anti-malware measures, making detection challenging.                                     |
|                               | Attackers may use automated tools, such as botnets communicating with command-and-control servers, to maintain access.                         |
### Phase 6: Command-and-Control (CnC)
| **Topic**                      | **Details**                                                                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Phase 6: Command-and-Control (CnC)** | CnC is the phase where compromised systems communicate with an external server to receive commands and exfiltrate data.                        |
|                                 | Communication can be detected through unusual network traffic patterns, such as connections to suspicious domains or IRC channels.             |
|                                 | Effective detection of CnC can reveal the scope of an attack and help in mitigating further damage.                                             |
### Phase 7: Actions on Objectives
| **Topic**                          | **Details**                                                                                                                                   |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Phase 7: Actions on Objectives**  | In this phase, attackers execute their primary goals, such as data theft, system disruption, or using the compromised system for further attacks. |
|                                     | Actions depend on the attacker's objectives, such as stealing intellectual property or deploying ransomware.                                  |
|                                     | Once access is achieved, attackers often seek to expand their foothold within the network, complicating detection and response efforts.        |
## Ransomware

### Understanding Kill Chain in Ransomware

| **Topic**                             | **Details**                                                                                                                                   |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Recon**                             | Attackers gather information about potential targets, often using social media and company websites, to craft convincing phishing emails.     |
| **Weaponization**                     | The attacker prepares ransomware and identifies the delivery method, typically via email with malicious links or attachments.                 |
| **Delivery**                          | The crafted email is sent to potential victims, relying on social engineering to entice users to click on links or open attachments.          |
| **Exploitation**                      | When a user clicks a malicious link, the exploit is triggered, leading to the installation of a downloader or stager on the victim's machine. |
| **Installation**                      | The downloader contacts a CnC server to download the ransomware payload, tailored to the target's system architecture.                        |
| **Command-and-Control (CnC)**         | The installed ransomware communicates with the CnC server to receive encryption keys and further instructions.                                |
| **Action on Objectives**              | The ransomware encrypts files on the victim's system, often accompanied by a ransom note that urges payment.                                  |
### Mitigation Strategies Against Ransomware

| **Topic**                        | **Details**                                                                                                                             |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Threat Intelligence**          | Provides knowledge of existing ransomware threats and communication vectors, helping organizations ==stay informed== about new threats. |
| **Email Security**               | ==Blocks malicious attachments and links==, preventing the delivery of ransomware to users.                                             |
| **DNS Security**                 | ==Prevents connections== to known malicious domains, disrupting CnC communications.                                                     |
| **Client Security**              | ==Inspects files== for malware, quarantining or removing threats before they can execute.                                               |
| **Web Security**                 | ==Blocks access== to infected sites and files, reducing the risk of exploitation during web browsing.                                   |
| **Intrusion Prevention**         | ==Detects and blocks attacks== during the exploitation phase, preventing the installation of ransomware.                                |
| **Importance of User Education** | ==Educating== users about phishing risks and not clicking on suspicious links reduces the likelihood of successful attacks.             |
|                                  | Regular ==training== and simulated phishing attacks reinforce safe practices among employees.                                           |
# [[Dimond Model]]

![7](/Course-Notes/.assets/dimon_model.png)

| **Topic**                           | **Details**                                                                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Introduction to the Diamond Model** | A systematic method for analyzing cybersecurity events, helping to track and counter threats.                                                   |
| **Purpose and Functionality**        | Provides a framework for SOC teams to verify APTs and develop strategies to counter malicious activities.                                         |
|                                     | Emphasizes repeatability in analysis, allowing comparison and structured understanding of similar incidents.                                      |
|                                     | Helps analysts build a comprehensive understanding of adversary behavior and attack patterns.                                                    |
|                                     | Facilitates identification of relationships between incidents, enhancing the organization's security posture.                                     |

| **Topic**                               | **Details**                                                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Key Components of the Diamond Model** |                                                                                                    |
| **Adversary**                           | Represents the threat actor responsible for the attack, including their motives and techniques.    |
| **Capability**                          | Refers to the tools, techniques, and procedures (TTPs) the adversary uses to carry out the attack. |
| **Victim**                              | The target of the attack, typically an organization or system.                                     |
### Detailed Analysis of Diamond Model Nodes

| **Topic**          | **Details**                                                                                                                                    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Adversary**      | The entity responsible for conducting an intrusion, which can be an individual or group.                                                       |
|                    | Can be categorized into adversary operator (individual executing the attack) and adversary customer (entity benefiting from the attack).       |
|                    | Understanding the adversary’s motivations and capabilities is crucial for developing effective countermeasures.                                |
|                    | Case studies of notable adversaries, such as state-sponsored hackers or cybercriminal organizations, illustrate the diversity of methods used. |
| **Capability**     | Refers to the tools and techniques employed by adversaries during an attack, ranging from simple scripts to sophisticated malware.             |
|                    | The adversary's arsenal includes capabilities categorized by complexity and sophistication.                                                    |
|                    | Examples include exploits, social engineering, and custom-built malware.                                                                       |
|                    | Effectiveness depends on the vulnerabilities targeted, highlighting the importance of vulnerability management.                                |
| **Victim**         | The target of the adversary’s attack, which can be an individual, organization, or specific asset.                                             |
|                    | Can be analyzed as victim persona (group being attacked) and victim asset (specific target of the attack).                                     |
|                    | Understanding the victim's vulnerabilities and exposures is essential for anticipating attacks.                                                |
|                    | The victim asset may be used in multiple attacks, necessitating ongoing vigilance and monitoring.                                              |
| **Infrastructure** | Encompasses the physical and logical communication nodes used by adversaries to maintain command and control over their capabilities.          |
|                    | - Type 1 (owned by the adversary) <br>- Type 2 (co-opted from third parties).                                                                  |
|                    | Intermediary infrastructure can obscure the adversary’s identity, complicating detection and response.                                         |
|                    | Service providers (e.g., ISPs) play a critical role, often being unwitting participants in adversarial activities.                             |
### Application of the Diamond Model

| **Linking Incidents**                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------- |
| The diamond model allows analysts to link common nodes across different incidents, identifying patterns and correlations.              |
| By answering key questions (infrastructure used, target, methods), analysts can build a comprehensive picture of adversarial behavior. |
| Correlating incidents based on shared capabilities and infrastructure can help identify the same adversary across multiple attacks.    |
| This process aids in developing an adversary portfolio, enhancing future threat detection and response efforts.                        |

| **Meta-Features of the Diamond Model** | **Details**                                                                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **Timestamp**                          | Captures when an event occurred, allowing for chronological analysis of attacks.                                             |
| **Phase**                              | Categorizes events into groups similar to the phases of the kill chain, providing insight into the attack lifecycle.         |
| **Result**                             | Indicates the outcome of the adversary's operation, informing future defensive strategies.                                   |
| **Direction**                          | Denotes the flow of actions between the adversary and victim, highlighting the role of infrastructure in the attack process. |
| **Methodology**                        | Classifies the type of attack used (e.g., DoS or spear-phishing), aiding in identifying trends and tactics.                  |
# [[MITRE ATTACK™ Framework]]

Fundamental Theories

| **Model**                              | **Description**                                                                                                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pyramid of Pain** - **David Biacco** | Illustrates the relationship between various IOCs and a threat actor's behaviors, emphasizing TTPs as the most valuable for detection.                                                 |
| **ATT&CK Matrices**                    | Visual tools (Pre-ATT&CK, Enterprise ATT&CK, Mobile ATT&CK, ICS-SCADA/IoT ATT&CK) that help analysts understand the relationship between tactics and techniques used by threat actors. |
# [The Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)

![6](/Course-Notes/.assets/Pasted_image_20241130110449.png)

| Pyramid of pain                                | **Details**                                                                                                                                                       |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Concept and Importance**                     | The Pyramid of Pain illustrates the varying value of different types of indicators of compromise (IOCs), guiding analysts to focus on more meaningful indicators. |
|                                                | Atomic IOCs include easily modified attributes like MD5/SHA hashes, IP addresses, and filenames, which can be quickly changed to evade detection.                 |
|                                                | The pyramid emphasizes that TTPs are the most valuable indicators for identifying advanced persistent threats (APTs).                                             |
| **Tactics, Techniques, and Procedures (TTPs)** |                                                                                                                                                                   |
| **Tactics**                                    | Represent the overarching goals of threat actors.                                                                                                                 |
| **Techniques**                                 | Demonstrate how the threat actors achieve their goals.                                                                                                            |
| **Procedures**                                 | Outline the specific methods used by threat actors.                                                                                                               |
|                                                | Understanding TTPs is crucial for analysts to piece together attack narratives from complex data sources like network traffic and logs.                           |
|                                                | Recognizing and responding to TTPs can force threat actors to alter their methods, creating operational challenges for them.                                      |
# MITRE ATT&CK Framework

### Enterprise ATT&CK Matrix Components
![5](/Course-Notes/.assets/Pasted_image_20241130110536.png)

| Understanding <br>The Matrix | A Visual representation of the TTPs                                                                                                        |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
|                              | It is interconnected, illustrating how different techniques can be used in conjunction to achieve an adversary's objectives.               |
|                              | The matrix is continuously updated to reflect new techniques and trends in cyber threats, ensuring its relevance and utility for analysts. |
![4](/Course-Notes/.assets/Pasted_image_20241130110603.png)

| **Topic**                 | **Details**                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Techniques Overview**   | Techniques form the backbone of the ATT&CK framework, providing contextual details about potential threat indicators.    |
|                           | Each technique is associated with specific adversary groups, threat actors, and software known to employ that technique. |
|                           | The organization of techniques is influenced by tactical objectives, required components, and detection requirements.    |
| **Detection Strategies**  | Focus on identifying adversary behavior through log analysis and packet capture.                                         |
|                           | ATT&CK provides vendor-agnostic solutions that enhance internal threat assessments and response plans.                   |
|                           | Effective detection strategies are crucial for security investigators to respond promptly to threats.                    |
| **Mitigation Strategies** | Aim to prevent techniques from functioning or achieving the adversary's desired outcomes.                                |
|                           | ATT&CK mitigation guidance offers generic recommendations that can be tailored to specific organizational needs.         |
|                           | Implementing these strategies can significantly improve an organization’s security posture against potential attacks.    |
![3](/Course-Notes/.assets/Pasted_image_20241130110629.png)![2](/Course-Notes/.assets/Pasted_image_20241130110726.png)
### MITRE ATT&CK [Navigator Web Application](https://github.com/mitre-attack/attack-navigator/blob/master/README.md)
![1](/Course-Notes/.assets/Pasted_image_20241130110755.png)

| **Overview of the Navigator Tool**                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The ATT&CK Navigator is an interactive web application designed to visualize an organization’s defensive coverage and assess threat gaps.              |
| Analysts can create customized views from the Pre-ATT&CK, Enterprise ATT&CK, and Mobile ATT&CK matrices, with support for ICS-SCADA/IoT expected soon. |
| The tool allows for the organization of threats by type, concern, phase, or date, facilitating a comprehensive analysis of potential vulnerabilities.  |
| **Features of the Navigator**                                                                                                                          |
| Users can display information for specific techniques and tactics, as well as access details on adversaries and their preferred techniques.            |
| The Navigator supports the creation of multiple layers, which can be saved as JSON, CSV, or SVG files for further analysis.                            |
| It is recommended to deploy a personal instance of the Navigator for sensitive data to ensure confidentiality.                                         |

| Title                                   | Threat Model Using the ATT&CK                                                                                                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Assessing Risks and Vulnerabilities** | Analysts must evaluate the risks and vulnerabilities of key business assets to create an effective threat model.                                                                           |
|                                         | Prioritizing assets based on importance allows for a structured approach to risk assessment.                                                                                               |
|                                         | The Center for Internet Security Risk Assessment Method (CIS RAM) provides a model for assessing security posture against best practices.                                                  |
| **Conducting Threat Gap Analysis**      | The ATT&CK Navigator aids in visualizing defensive coverage and identifying potential attack vectors.                                                                                      |
|                                         | A threat gap analysis helps pinpoint vulnerabilities that could be exploited by threat actors.                                                                                             |
|                                         | Organizations should conduct industry-specific searches on the ATT&CK website to identify relevant advanced persistent threat groups and their tactics, techniques, and procedures (TTPs). |
| **Ranking and Prioritizing Risks**      | Identified risks should be ranked based on the probability and potential impact of attacks on critical assets.                                                                             |
|                                         | This prioritization helps organizations focus their resources on the most significant threats.                                                                                             |
|                                         | Continuous assessment and updating of the threat model are essential for maintaining an effective security posture.                                                                        |
