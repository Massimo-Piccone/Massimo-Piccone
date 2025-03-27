# [[Quick Reference]]

Fundamental Theories

|**Model**|**Description**|
|---|---|
|**Pyramid of Pain**|Illustrates the relationship between various IOCs and a threat actor's behaviors, emphasizing TTPs as the most valuable for detection.|
|**ATT&CK Matrices**|Visual tools (Pre-ATT&CK, Enterprise ATT&CK, Mobile ATT&CK, ICS-SCADA/IoT ATT&CK) that help analysts understand the relationship between tactics and techniques used by threat actors.|

Key People

- **David Biacco**: Developed the Pyramid of Pain model to help analysts understand the value of different IOCs in threat detection.

Key Institutions/Organizations

- **MITRE Corporation**: A not-for-profit organization that manages federally funded research and development centers, responsible for the development of the ATT&CK framework and the Common Vulnerabilities and Exposures (CVE) database.

Seminal Studies

- **CIS RAM**: The Center for Internet Security Risk Assessment Method, which provides a model for assessing security posture against cybersecurity best practices.
- **NIST Cybersecurity Framework**: A framework developed by the National Institute of Standards and Technology to improve cybersecurity for critical infrastructure.

Facts to Memorize

- MITRE ATT&CK Framework: A comprehensive knowledge base of adversary tactics and techniques.
- Pyramid of Pain: A model illustrating the relationship between different types of indicators of compromise (IOCs) and threat actor behaviors.
- Tactics, Techniques, and Procedures (TTPs): Key components for identifying advanced persistent threats.
- ATT&CK Navigator: A tool for visualizing defensive coverage and assessing threat gaps.

Reference Information

- MITRE ATT&CK matrices: Pre-ATT&CK, Enterprise ATT&CK, Mobile ATT&CK, ICS-SCADA/IoT ATT&CK.
- Sources of cyber threat intelligence: Threat intelligence reports, conference presentations, webinars, social media, blogs, open source code repositories, malware samples.
- Common Vulnerabilities and Exposures (CVE) database: Created by MITRE in 1999.

Cause and Effect

|Cause|Effect|
|---|---|
|Development of the MITRE ATT&CK framework|Provides a structured approach for understanding and analyzing threat actor behaviors.|
|Use of the Pyramid of Pain|Guides analysts to focus on high-value indicators and understand threat actor behaviors.|
|Integration of cyber threat intelligence|Enhances threat hunting and incident response capabilities for organizations.|
|Creation of ATT&CK Navigator|Allows organizations to visualize their defensive coverage and identify threat gaps.|

Key Terms/Concepts

- **MITRE ATT&CK Framework**: A comprehensive knowledge base of known adversary tactics, techniques, and procedures (TTPs) based on real-world observations, used for threat intelligence and incident response.
- **Tactics, Techniques, and Procedures (TTPs)**: The behaviors and methods used by threat actors to achieve their objectives during an attack.
- **Pyramid of Pain**: A model illustrating the relationship between different types of indicators of compromise (IOCs) and the difficulty of changing them, emphasizing the importance of focusing on TTPs rather than low-value IOCs.

# Overview of the MITRE ATT&CK Framework

### Introduction to MITRE ATT&CK

- The MITRE ATT&CK framework is a comprehensive repository of known attack techniques used by threat actors globally, providing insights into their tactics, techniques, and procedures (TTPs).
- It is developed by the MITRE organization, which is based in the U.S. and funded through federal resources for open-source research.
- The framework includes detailed documentation for each technique, including explanations, examples, detection recommendations, and associated threat actors.
- MITRE has established partnerships with organizations like CERN and NIST, contributing to significant cybersecurity initiatives, including the Common Vulnerabilities and Exposures (CVE) database since 1999.

### Integration with Cyber Threat Intelligence

- The ATT&CK framework integrates cyber threat intelligence into threat hunting and incident response, enhancing the capabilities of Security Operations Center (SOC) analysts.
- It provides a structured analysis of the classic kill chain model, allowing analysts to understand common TTPs employed by threat actors at each stage of an attack.
- Analysts can incorporate other threat models, such as the diamond model for intrusion analysis, into their ATT&CK framework assessments.

# [The Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html)
![10](/Course-Notes/.assets/Pasted_image_20241130110449.png)
### Concept and Importance

- The Pyramid of Pain illustrates the varying value of different types of indicators of compromise (IOCs), guiding analysts to focus on more meaningful indicators rather than trivial atomic IOCs.
- Atomic IOCs include easily modified attributes like MD5/SHA hashes, IP addresses, and filenames, which can be quickly changed by threat actors to evade detection.
- The pyramid emphasizes that TTPs are at the top, representing the most valuable information for identifying advanced persistent threats (APTs).

### Tactics, Techniques, and Procedures (TTPs)

- Tactics represent the overarching goals of threat actors, while techniques demonstrate how these goals are achieved, and procedures outline the specific methods used.
- Understanding TTPs is crucial for analysts to piece together attack narratives from complex data sources like network traffic and logs.
- Recognizing and responding to TTPs can force threat actors to alter their methods, creating operational challenges for them.

# Getting Started with the MITRE ATT&CK Framework

### Access and Community Involvement

- The MITRE ATT&CK framework is a free, open-access resource that is community-driven, allowing anyone to contribute and utilize the knowledge base.
- It collects cyber threat intelligence from diverse sources, including threat intelligence reports, conference presentations, webinars, social media, blogs, open-source code repositories, and malware samples.

### Framework Structure and Components

- The framework normalizes information from various sources into specific adversary tactics and techniques, correlating them with known threat actors and groups.
- Each technique includes contextual information, detection strategies, and mitigation recommendations, providing actionable insights for analysts.
- The Enterprise ATT&CK Matrix visually represents the relationships between different components, highlighting the evolving nature of the framework.

# Enterprise ATT&CK Matrix Components
![9](/Course-Notes/.assets/Pasted_image_20241130110536.png)
### Understanding the Matrix

- The Enterprise ATT&CK Matrix is a visual representation of the techniques employed by threat actors, categorized by tactics and techniques.
- Each component of the matrix is interconnected, illustrating how different techniques can be used in conjunction to achieve an adversary's objectives.
- The matrix is continuously updated to reflect new techniques and trends in cyber threats, ensuring its relevance and utility for analysts.

![8](/Course-Notes/.assets/Pasted_image_20241130110603.png)
# Overview of MITRE ATT&CK Matrices

### Introduction to MITRE ATT&CK

- The MITRE organization has developed four ATT&CK matrices: Pre-ATT&CK, Enterprise ATT&CK, Mobile ATT&CK, and ICS-SCADA/IoT ATT&CK, each serving to visualize threat actor tactics and techniques.
- These matrices assist organizations in identifying vulnerabilities in their network defenses and prioritizing them based on assessed risks.
- Each matrix is tailored to specific operating systems and platforms, including Windows, Linux, macOS, AWS, GCP, Azure, Azure Active Directory, Office 365, and SaaS.

![7](/Course-Notes/.assets/Pasted_image_20241130110629.png)
### Structure of the Enterprise ATT&CK Matrix

- The Enterprise ATT&CK matrix is organized into tactics (columns) and techniques (rows), where tactics represent the objectives of threat actors during an attack.
- Each tactic is assigned a unique ID (e.g., TA001, TA002) to facilitate tracking and reference.
- Tactics are sequenced from left to right, representing a potential flow of actions, but threat actors may not follow this order, often jumping between tactics.

![6](/Course-Notes/.assets/Pasted_image_20241130110726.png)
### Importance of Tactics and Techniques

- Tactics provide a high-level view of the attacker's goals, while techniques offer detailed methods to achieve those goals.
- Understanding the relationship between tactics and techniques helps organizations anticipate and mitigate potential threats.
- Techniques are categorized based on their tactical objectives, actions performed, and the adversary groups that utilize them.

# Techniques, Detection, and Mitigation Strategies

![5](/Course-Notes/.assets/Pasted_image_20241130110734.png)
![4](/Course-Notes/.assets/Pasted_image_20241130110745.png)
### Techniques Overview

- Techniques form the backbone of the ATT&CK framework, providing contextual details about potential threat indicators.
- Each technique is associated with specific adversary groups, threat actors, and software known to employ that technique.
- The organization of techniques is influenced by factors such as tactical objectives, required components, and detection requirements.

### Detection Strategies

- Detection strategies focus on identifying adversary behavior through log analysis and packet capture.
- ATT&CK provides vendor-agnostic solutions that can enhance internal threat assessments and response plans.
- Effective detection strategies are crucial for security investigators to respond promptly to threats.

### Mitigation Strategies

- Mitigation strategies aim to prevent techniques from functioning or achieving the adversary's desired outcomes.
- ATT&CK mitigation guidance offers generic recommendations that can be tailored to specific organizational needs.
- Implementing these strategies can significantly improve an organization’s security posture against potential attacks.

# MITRE ATT&CK [Navigator Web Application](https://github.com/mitre-attack/attack-navigator/blob/master/README.md)

![3](/Course-Notes/.assets/Pasted_image_20241130110755.png)
### Overview of the Navigator Tool

- The ATT&CK Navigator is an interactive web application designed to visualize an organization’s defensive coverage and assess threat gaps.
- Analysts can create customized views from the Pre-ATT&CK, Enterprise ATT&CK, and Mobile ATT&CK matrices, with support for ICS-SCADA/IoT expected soon.
- The tool allows for the organization of threats by type, concern, phase, or date, facilitating a comprehensive analysis of potential vulnerabilities.

![2](/Course-Notes/.assets/Pasted_image_20241130110814.png)
### Features of the Navigator

- Users can display information for specific techniques and tactics, as well as access details on adversaries and their preferred techniques.
- The Navigator supports the creation of multiple layers, which can be saved as JSON, CSV, or SVG files for further analysis.
- It is recommended to deploy a personal instance of the Navigator for sensitive data to ensure confidentiality.

# Creating a Threat Model Using the ATT&CK Framework

![1](/Course-Notes/.assets/Pasted_image_20241130110912.png)
### Assessing Risks and Vulnerabilities

- Analysts must first evaluate the risks and vulnerabilities of key business assets to create an effective threat model.
- Prioritizing assets based on importance allows for a structured approach to risk assessment.
- The Center for Internet Security Risk Assessment Method (CIS RAM) provides a model for assessing security posture against best practices.

### Conducting Threat Gap Analysis

- The ATT&CK Navigator aids in visualizing defensive coverage and identifying potential attack vectors.
- A threat gap analysis helps pinpoint vulnerabilities that could be exploited by threat actors.
- Organizations should conduct industry-specific searches on the ATT&CK website to identify relevant advanced persistent threat groups and their tactics, techniques, and procedures (TTPs).

### Ranking and Prioritizing Risks

- Identified risks should be ranked based on the probability and potential impact of attacks on critical assets.
- This prioritization helps organizations focus their resources on the most significant threats.
- Continuous assessment and updating of the threat model are essential for maintaining an effective security posture.