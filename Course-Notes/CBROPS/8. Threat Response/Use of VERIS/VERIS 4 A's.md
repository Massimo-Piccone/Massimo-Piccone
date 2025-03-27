VERIS framework describes incidents and threats using ==a==ctors, ==a==ctions, ==a==ssets, and ==a==ttributes.

![2](/Course-Notes/.assets/Pasted_image_20241204150916.png)

- Handling Unknown Attributes: Most required fields allow for unknown values if an attribute is not present in the incident.

# Example 
%% [Reference](http://veriscommunity.net/enums.html) %%
The following is an example SOC case ticket of a TeslaCrypt ransomware incident in which the VERIS 4 A's were used.

![1](/Course-Notes/.assets/Pasted_image_20241204151330.png)

## Actors (or Agents)

Threat actors are the entities that cause or contribute to an incident.

VERIS recognizes three primary categories of threat actors:

- **External actors** are the external threats that originate from sources outside of the organization and its network.
- **Internal actors** are the internal threats that originate within the organization.
- **Partner actors** include any third party sharing a business relationship with the organization.

## Actions

- Threat Action Definition: Describes what the threat actor did to cause or contribute to the incident.
- Threat Action Categories: Malware, hacking, social, misuse, physical, error, and environmental.
- Incident Characteristics: Every incident has at least one threat action, but most will comprise multiple actions.

Heres is an example of the malware action:

- **Malware** is defined by VERIS as **“any malicious software, script, or code that is run on a device that alters its state or function without the owner’s informed consent,"** which would include ==viruses, spyware, backdoors, worms, and keyloggers.==

| Subcategories   | Description                                                            |
| --------------- | ---------------------------------------------------------------------- |
| Variety         | Describes the malware varieties or functions involved in the incident. |
| Vector          | Describes the path of attack or infection.                             |
| Vulnerabilities | Captures the specific vulnerability exploited by the malware.          |
| Common Name     | The common name or strain of the malware.                              |

>Here are examples of three other common actions:

- **Hacking** is defined within VERIS as **“all attempts to intentionally access or harm information assets without (or exceeding) authorization by circumventing or thwarting logical security mechanisms,"** which would include ==brute force, denial of service attacks, SQL injections, and cryptanalysis==. This SOC uses two attributes to describe hacking: ==variety and vector.==
    
    A typical SOC list of **hacking ==variety==** may include:
    
    1. Brute force or password guessing attacks
    2. Buffer overflow
    3. XSS
    4. Man-in-the-middle attacks
    5. Remote file inclusion
    6. SQL injection
    7. DoS
    8. Path traversal
    
    The **hacking ==vector==** describes the path of the attack. 
    
    1. Third-party online desktop sharing (LogMeIn, GoToAssist, and so on)
    2. Backdoor or command and control channel
    3. Command shell
    4. VPN
    5. Web application

| Hacking Variety                          | Hacking Vector                                                      |
| ---------------------------------------- | ------------------------------------------------------------------- |
| Brute force or password guessing attacks | Third-party online desktop sharing (LogMeIn, GoToAssist, and so on) |
| Buffer overflow                          | Backdoor or command and control channel                             |
| XSS                                      | Command shell                                                       |
| Man-in-the-middle attacks                | VPN                                                                 |
| Remote file inclusion                    | Web application                                                     |
| SQL injection                            | Web application                                                     |
| DoS                                      | Web application                                                     |
| Path traversal                           | Web application                                                     |

- **Social** action includes use of ==deception, intimidation, and manipulation to exploit the human element==. This SOC uses two attributes to describe a social attack: ==variety== and ==vector==.
    
    ==Varieties== of **social tactics** that were involved may include:
    
    1. Phishing
    2. Scam
    
    The **social ==vector==** describes the communication channels that are used in the attack. Social vector may include:
    
    1. Email
    2. IM
    3. Social media
    4. Website

- **Misuse** is defined as **the use of entrusted organizational resources or privileges for any purpose contrary to what was intended,** which includes ==misuse or abuse of corporate assets, access privileges, and policy violations among others.== These actions can be malicious or nonmalicious in nature. Misuse is exclusive to parties that enjoy a degree of trust from the organization, such as insiders and partners. This SOC uses two attributes to describe misuse: ==misuse variety and misuse vector.==
    
    The **misuse ==variety==** describes the varieties of the misuse that were involved with the incident, which may include:
    
    1. **Privilege abuse:** Abuse of system access privileges
    2. **Data mishandling:** Handling of data in an unapproved manner
    3. **Email misuse:** Inappropriate use of email
    4. **Network misuse:** Inappropriate use of network or web access
    5. **Illicit content:** Storage or distribution of illicit content
    6. **Unapproved hardware:** Use of unapproved hardware or devices
    7. **Unapproved software:** Use of unapproved software or services

## Assets

Assets are the **information assets that were compromised during the incident. “Compromised”** refers to ==any loss of confidentiality/possession, integrity/authenticity, or availability/utility.== Naturally, an incident can involve multiple assets and affect multiple attributes of those assets.

A typical organization may include the following list of assets:

- **Network hardware:** Routers, switches, IPS, firewall, and so on
- **Server:** Mail server, web server, application server, and so on
- **User device:** Laptop, desktop, smart phone, tablet, and so on
- **Others:** End user, storage media, and so on

## Attributes

Attributes are the **security attributes of the identified assets that were compromised during the incident**. VERIS uses a paired version of the ==six primary security attributes of **confidentiality/possession**, **integrity/authenticity**, and **availability/utility**==, which is an extension of the ==“C-I-A triad.”==


# [[Quick Reference]]

Key Actions

|Action Type|Description|
|---|---|
|**Malware**|Malicious software that alters a device's state or function without consent, including viruses and ransomware.|
|**Hacking**|Unauthorized access or harm to information assets, including methods like SQL injection and DoS attacks.|
|**Social**|Exploiting the human element through deception, such as phishing or scams.|
|**Misuse**|Use of organizational resources contrary to intended purposes, including privilege abuse and data mishandling.|

Key Actors

- **External Actors**: Threats originating from outside the organization.
- **Internal Actors**: Threats originating from within the organization.
- **Partner Actors**: Third parties sharing a business relationship with the organization.

Key Assets

- **Network Hardware**: Devices like routers and firewalls that are critical for network security.
- **Servers**: Systems that host applications and data, such as mail and web servers.
- **User Devices**: Personal devices like laptops and smartphones that access organizational resources.

Key Attributes

- **Confidentiality/Possession**: Ensuring that information is not disclosed to unauthorized individuals.
- **Integrity/Authenticity**: Maintaining the accuracy and trustworthiness of data.
- **Availability/Utility**: Ensuring that information and resources are accessible when needed.

Facts to Memorize

- The VERIS 4 A's: Actors, Actions, Assets, Attributes.
- Categories of threat actors: External, Internal, Partner.
- Seven primary categories of threat actions: Malware, Hacking, Social, Misuse, Physical, Error, Environmental.
- The C-I-A triad: Confidentiality, Integrity, Availability.

Reference Information

- Malware varieties include: backdoor, brute force, CnC, client-side attack, DoS, downloader, exploit vulnerability, infostealer, ransomware, rootkit.
- Hacking varieties include: brute force, buffer overflow, XSS, man-in-the-middle, remote file inclusion, SQL injection, DoS, path traversal.
- Social tactics include: Phishing, Scam.

Concept Comparisons

|Concept|Description|Examples|
|---|---|---|
|Actors|Entities causing or contributing to an incident.|External, Internal, Partner|
|Actions|What the threat actor did to cause or contribute to the incident.|Malware, Hacking, Social, Misuse|
|Assets|Information assets compromised during the incident.|Network hardware, Server, User device|
|Attributes|Security attributes of the identified assets that were compromised.|Confidentiality, Integrity, Availability|

Cause and Effect

|Cause|Effect|
|---|---|
|Introduction of malware|Compromise of assets leading to loss of confidentiality, integrity, or availability.|
|Hacking attempts|Unauthorized access to sensitive information or systems.|
|Social engineering tactics|Exploitation of human elements leading to data breaches or unauthorized access.|
|Misuse of privileges|Internal threats resulting in data mishandling or policy violations.|
# Overview of VERIS Framework

### Introduction to the 4 A's

- The VERIS framework is designed to provide a structured approach to documenting incidents and threats, focusing on four key components: Actors, Actions, Assets, and Attributes.
- Each of the 4 A's serves as a foundational element in understanding and analyzing security incidents, ensuring that all relevant information is captured.
- The framework allows for flexibility, as many fields are optional and can accommodate unknowns, making it adaptable to various incident scenarios.
- The 4 A's are essential for incident response teams to effectively communicate and analyze incidents, leading to better security practices.

### Importance of the 4 A's

- The 4 A's provide a comprehensive view of an incident, allowing organizations to understand the who, what, and how of security breaches.
- By categorizing incidents using the 4 A's, organizations can identify patterns and trends in security threats, leading to improved defences.
- The framework supports incident reporting and analysis, which is crucial for compliance and regulatory requirements.
- Utilizing the 4 A's can enhance collaboration between different teams within an organization, such as IT, security, and management.