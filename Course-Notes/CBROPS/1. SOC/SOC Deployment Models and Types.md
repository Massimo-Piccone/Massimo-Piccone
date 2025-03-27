## SOC Types and Staffing Considerations
### Threat-Centric SOC — The Hunters

**Objective:** Proactively hunt for malicious threats in the network.

**Activities:** Includes threat hunting, threat modeling, and tracking of threat actors.

**Process:** Assumes attackers are already inside the network, seeking out indicators of compromise (IOCs) to mitigate potential attacks.

**Example:** Cisco Talos to avoid ransomware attacks by proactive threat hunting.

### Process 

**Before and attack**
- Comprehensive contextual awareness

- In-depth analysis of the network traffic

- Implement policies and controls that properly defend the environment.

**During an attack**
- Continuously detect the presence of malware and block identified threats.

**After an attack**
Marginalize the impact of an attack by: 

- Identifying the point of entry
- Determine the scope of the attack.
- Contain the threat
- Remediate the infected host.
- Minimize the risk of reinfection.

### Compliance-Based SOC — The Enforcers

**Objective**: Ensure adherence to regulatory compliance standards.

**Focus**: Procedures and reporting for compliance requirements (e.g., PCI DSS for payment security).

**Example**: A SOC managing security for an online bookstore focuses on encryption, password policies, and firewall configuration to meet PCI DSS standards.

- Comparing the compliance posture of network systems to reference configuration templates and standard system builds.
- Detects unauthorized changes and existing configuration problems.
- The link between risk management and incident response
- Organization and Automated system compliance process

### Operational-Based SOC (CSIRT) — The Defenders 

**Objective**: Maintain the operational integrity of an organization's internal network security.

**Focus**: Monitoring internal network security, developing customized detection techniques, and ensuring proper configuration of security devices.

**Example**: A SOC for a financial institution constantly adjusts and updates access control policies, intrusion detection systems, and firewall configurations to protect sensitive internal data.

- Develops and deploys customized detection techniques (e.g., REGEX-based search strings).
- Maintains operational integrity of identity management and access policies.
- Focuses on the administration of firewall access control lists and intrusion detection system rules.
- Addresses operational issues through operational solutions, avoiding misconfigurations.
- The CSIRT (Computer Security Incident Response Team) handles incident responses.

## Compare

| **SOC Type**              | **Focus**                                                                                               | **Key Activities**                                                                                                                                                                               | **Nickname**        |
|---------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| **Threat-Centric SOC**     | Proactively hunts for malicious threats on networks by identifying vulnerabilities and anomalies.       | - Pre-attack: Implement policies, analyze network traffic for defenses. <br> - During attack: Detect and block malware threats. <br> - Post-attack: Marginalize impact, contain threats, remediate infected hosts. | The Hunters         |
| **Compliance-Based SOC**   | Focuses on ensuring network systems comply with security standards, configuration templates, and policies. | - Monitors configurations for unauthorized changes and security breaches. <br> - Ensures compliance with standards like CIS and PCI DSS. <br> - Evaluates the organization's security posture.            | The Guardians / The Enforcers |
| **Operational-Based SOC**  | Internally focused, tasked with monitoring and maintaining the internal network's security posture.      | - Develops and deploys customized detection techniques (e.g., REGEX). <br> - Maintains access control policies, intrusion detection system rules, and firewall configurations. <br> - Monitors internal network security. | The Responders / The Defenders |

## SOC Deployment Models

#### **Internal SOC (On-premises)**

• **Description**: Resides within the organization with dedicated security infrastructure and a team that knows the organization’s assets and business challenges.

• **Key Features**:

- 24/7 monitoring of the internal network.
- High visibility and control over internal security posture.
- Complete control over data and security policies.
- Requires significant resources (staff, budget, and infrastructure).
- **Best For**: Organizations with large IT teams, high-security needs, and a budget to support year-round operations (e.g., regulated industries).

#### **Virtual SOC (vSOC)**

• **Description**: An outsourced, third-party-managed solution for cybersecurity monitoring and response.

• **Key Features**:

- Provides 24/7 monitoring via external security experts.
- Less agility than an internal SOC.
- Potential security risks with data exposure to third parties.
- Scalable, cost-effective, and quick to implement.
- **Best For**: Organizations with limited internal expertise or smaller budgets that need immediate security support but can’t afford a full internal SOC.

#### **Hybrid SOC**

• **Description**: Combines internal staff with third-party expertise to provide comprehensive monitoring and response.

• **Key Features**:

- Uses internal knowledge for policy and threat landscape, supplemented with third-party monitoring and expertise.
- Offers a balance between control and expertise.
- More cost-effective than a full internal SOC, but still maintains some control over sensitive data.
- **Best For**: Organizations needing both in-house control and external expertise but lack the resources to fully operate an internal SOC.
## Choosing the Right SOC Model

The **best SOC model** depends on several factors:

• **Size of the Organization**: Larger organizations may require a full internal SOC, while smaller ones may find a vSOC or hybrid model more suitable.

• **IT Security Budget**: Organizations with a larger budget can afford an internal SOC, while those with limited budgets may opt for a vSOC.

• **In-house Expertise**: Organizations with strong internal security teams can operate an internal SOC or hybrid SOC, while those with less expertise may need a vSOC for third-party support.

• **Data Sensitivity**: Highly sensitive data may require an internal SOC to ensure it stays in-house, while less sensitive data may be handled adequately by a vSOC.

## Drawbacks of Each Model

**Internal SOC**:
• **Drawbacks**: High cost of building and maintaining, resource-intensive, and requires a large budget and staff.

**vSOC**:
• **Drawbacks**: Longer escalation times, third-party visibility of private data, and potential security gaps in monitoring.

**Hybrid SOC**:
• **Drawbacks**: May not result in long-term cost savings, additional hardware for on-premises systems, and complexity in balancing internal and external resources.

## Example Use Cases

• **Internal SOC**: A large, regulated company (e.g., financial institution) with extensive security needs and resources.

• **vSOC**: A small to medium-sized organization that needs quick, scalable, and cost-effective security but doesn’t have the budget for an in-house SOC.

• **Hybrid SOC**: A medium to large organization with in-house security staff, but needs external expertise to fill knowledge gaps or scale operations.

| **SOC Model**      | **Description**                                 | **Pros**                                                                                                                              | **Cons**                                                                                          | **Cost** |
| ------------------ | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | -------- |
| **Internal**       | On-site, fully administered by the organization | - Best visibility <br> - Exclusive data management <br> - Most customizable <br> - Dedicated in-house staff                           | - Most expensive <br> - Most difficult to recruit and retain talent <br> - Slowest implementation | $$$      |
| **Virtual (vSOC)** | Contracted service                              | - Least expensive <br> - Quickest implementation <br> - Most flexible and scalable                                                    | - Least visibility <br> - Third-party data management <br> - Least customizable                   | $        |
| **Hybrid**         | Combination of internal and virtual             | - Quickest detection and response <br> - Most secure (extra pair of eyes) <br> - Knowledge share between internal SOC and third party | - Costly in the long term <br> - Additional hardware required <br> - Third-party data management  | $$       |
# [[Quick Reference]]

Key Actions After an Attack

- **Marginalize the impact**: Identify the point of entry to limit damage.
- **Determine the scope**: Assess the extent of the attack.
- **Contain the threat**: Isolate the infected host to prevent further spread.
- **Remediate**: Take steps to fix the vulnerabilities that were exploited.
- **Minimize reinfection risk**: Implement measures to prevent future attacks.

Key Challenges in SOC Operations

- **Detection of Attacks**: Difficulty in identifying attacks even with trained personnel.
- **Operational Issues**: Misconfiguration of security features can lead to vulnerabilities.
- **Resource Constraints**: Organizations may face limitations in staffing and budget for SOC operations.

Key Compliance Standards

- **Center of Internet Security (CIS)**: Provides benchmarks for security practices.
- **PCI DSS**: Standards for organizations that handle credit card information, ensuring secure transactions.

Facts to Memorize

- Types of SOC: Threat-centric, Compliance-based, Operational-based
- Key SOC Models: Internal, Virtual (vSOC), Hybrid
- Key roles in SOC: Tier 1, Tier 2, Tier 3 analysts
- Compliance standards: PCI DSS, CIS benchmarks

Reference Information

- Threat intelligence gathering services
- Vulnerability scanners and their limitations
- Computer Security Incident Response Team (CSIRT) functions
- Importance of operational integrity in SOC

Concept Comparisons

|SOC Type|Focus Area|Key Characteristics|Pros/Cons|
|---|---|---|---|
|Threat-centric|Proactive threat hunting|Continuous monitoring for malicious threats, contextual awareness before, during, and after attacks|Effective threat detection, but requires skilled personnel|
|Compliance-based|Compliance posture monitoring|Focus on unauthorized changes, adherence to standards like PCI DSS and CIS benchmarks|Ensures compliance, but may miss active threats|
|Operational-based|Internal network security|Tailored detection techniques, operational integrity, CSIRT involvement|Best for internal security, but can be resource-intensive|

Cause and Effect

|Event/Action|Impact/Outcome|
|---|---|
|Implementation of a threat-centric SOC|Improved detection of emerging threats and vulnerabilities, leading to a more secure network environment|
|Establishing a compliance-based SOC|Enhanced compliance with industry standards, reducing the risk of breaches due to misconfigurations|
|Development of operational-based SOC practices|Increased operational integrity and tailored security measures, but potential for misconfiguration if not managed properly|

Key Terms/Concepts

- **SOC (Security Operations Center)**: A centralized unit that deals with security issues on an organizational and technical level.
- **Threat-Centric SOC**: Focuses on proactively hunting for malicious threats and vulnerabilities across networks.
- **Compliance-Based SOC**: Monitors compliance posture against reference configurations and standards to detect unauthorized changes.
- **Operational-Based SOC**: Internally focused SOC that monitors the security posture of an organization’s internal network.
