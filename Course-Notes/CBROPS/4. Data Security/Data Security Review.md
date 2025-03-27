%% #review %%

# [[Data Type Categories]]

Monitoring types:
- Log data
- IPS alarts
- Full packet capture
- Netflow records

| Data Type           | Description                                                                                                                                | Example                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Session data        | Tracks network sessions using a 5-tuple (transport protocol, source IP/port, destination IP/port) and includes timestamps and data volume. | NetFlow                                                            |
| Full packet capture | Records all bits transferred across a networking wire, potentially extracting conversation content.                                        | PCAP                                                               |
| Transaction data    | Records network session and system activities.                                                                                             | HTTP daemon logs, SMTP daemon logs, Linux system login/logout logs |
| Extracted data      | Files transmitted as email attachments or downloaded from websites.                                                                        | Files extracted from network traffic                               |
| Statistical data    | Processes other security monitoring data types to describe network activities at a higher level.                                           | Average number of connections per minute to a web server           |
| Alert data          | Produced by IDS or IPS, is the most crystallized data type.                                                                                | IDS/IPS alerts                                                     |
| Syslog              | Provides real-time access to device logs.                                                                                                  | Syslog server and log files                                        |
RFC 5424 defines eight syslog severity levels: 0 being the highest and 7 the lowest.

| Code | Severity      | Description                      |
| ---- | ------------- | -------------------------------- |
| 0    | Emergency     | System is unusable               |
| 1    | Alert         | Action must be taken immediately |
| 2    | Critical      | Critical conditions              |
| 3    | Error         | Error conditions                 |
| 4    | Warning       | Warning conditions               |
| 5    | Notice        | Normal but significant condition |
| 6    | Informational | Informational messages           |
| 7    | Debug         | Debug messages                   |

Standard format for easy navigation with 3rd party tools.

![24](/Course-Notes/.assets/Screenshot_2024-11-15_at_10.12.03.png)

| Indicator of Compromise (IOC)                                                                                                                                                                               | Network Time Protocol (NTP)                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| An IOC is a high-fidelity predictor of system compromise extracted from security data.                                                                                                                      | NTP Functionality: Synchronizes clocks of computers and network devices over a network, ensuring accurate timestamps for incident investigation.  |
| For instance, if CnC traffic is detected between an external IP address and a compromised system, that IP can be used as an IOC. If other internal systems communicate with it, they’re likely compromised. | NTP Security Risk: Malicious attackers can falsify NTP time advertisements, leading to incorrect timestamps and potential security breaches.      |
| Similarly, if malware modifies the Windows registry in a specific way, it’s an IOC. Internal systems can be scanned for registry matches, indicating compromise.                                            | NTP Authentication: NTPv4 optionally implements authentication to verify the authenticity of the time source (NTP server).                        |
| OpenIOC is an extensible XML schema that allows security professionals to describe technical characteristics of known threats, attackers’ methodologies, or other evidence of compromise.                   | Correlation Importance: Essential for analysts to utilize all NSM data types by linking events across different data sets.                        |
| IP 5-tuple Significance: Crucial for event correlation, enabling analysts to identify related network activities.                                                                                           | Metadata Utilization: Enhances NSM data by providing additional context, such as geolocation and reputation scores, associated with IP addresses. |
# SEIM
The success of a project depends on factors such as:
- business requirements, and 
- engineering specifications 
- Event and alarm volume in terms of disk usage, 
- and retention requirements must be understood.

| Reason for SIEM Deployment                              | Description                                                                                   |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Security monitoring and incident response               | Monitoring security events and responding to incidents.                                       |
| Anomaly detection                                       | Identifying unusual or suspicious patterns in log data.                                       |
| Real-time rules-based alerts                            | Generating alerts based on predefined rules when specific events occur.                       |
| Data correlation                                        | Combining data from multiple sources to provide a more comprehensive view of security events. |
| Compliance or regulatory mandated logging and reporting | Logging and reporting activities to meet legal or regulatory requirements.                    |
| Automated reports                                       | Generating regular reports on security events and trends.                                     |
SEIM Configuration

| Aspect                 | Description                                                                                                  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Correlation Engine     | SIEMs use algorithms to analyze logs and identify relationships between events.                              |
| Correlation Benefits   | Confirms security incident details, eliminates circumstantial evidence.                                      |
| Correlation Example    | Identifies multiple suspicious activities from a single host, creating a more comprehensive incident report. |
| Correlation Challenges | Requires understanding of attack patterns and logical reasoning, best handled by humans.                     |
| SIEM Value Proposition | Helps find incidents that might be missed by existing tools.                                                 |
# Security Orchestration, Automation, and Response
SOAR

| Feature             | SOAR                                                                        |
| ------------------- | --------------------------------------------------------------------------- |
| Data Aggregation    | Collects and analyzes cyber threat intelligence.                            |
| Threat Intelligence | Supports integration with third-party threat security technologies.         |
| Incident Response   | Automates incident investigation and response workflows based on playbooks. |
| Automation          | Automates information security event management and incident response.      |
| MTTD/MTTR           | Reduces mean-time-to-detect (MTTD)/mean-time-to-respond (MTTR) metrics.     |

| Area                                   | Description                                                                                                  |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Security Incident Lifecycle Automation | Full automation of incident response processes, workflows, policy execution, and incident reporting.         |
| Threat and Vulnerability Management    | Proactive management of risks associated with vulnerabilities and threat investigation support.              |
| Security Incident Response             | Advanced analytics for threat confirmation and automation for incident response.                             |
| SOAR Adoption                          | Gartner predicts 30% of organizations with security teams larger than five will leverage SOAR tools by 2022. |
| Automated Threat Response              | Automated reactions to malicious elements from known attack vectors.                                         |
## Cisco SecureX Platform

| Feature                   | Description                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Unified Visibility        | Unifies visibility across all parts of an organization’s security portfolio, including Cisco and third-party solutions. |
| Cloud-Native Architecture | Fully cloud-native and multi-tenant solution.                                                                           |
| Enterprise-Wide Analytics | Analyzes events and data across the enterprise and over 150 million endpoints, network traffic, and encrypted traffic.  |
| Threat Identification     | Identifies threats targeting assets within minutes.                                                                     |
| Data Enrichment           | Uses data enrichment and telemetry from security products and threat intelligence feeds for quick remediation.          |
| Threat Hunting            | Leverages the expertise of Cisco Talos threat analysts for threat hunting.                                              |

# Security Onion Overview

1. Presentation of data to the analyst
2. Optimization and maintenance of data
3. Collection processing of raw NSM data

![23](/Course-Notes/.assets/Pasted_image_20241115140017.png)
## Deployment Options

| Scenario      | Description                                                                                                     | Features                                                                | Benefits                                                            |
| ------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Standalone    | A single machine running both the server and sensor components.                                                 | Multiple network interfaces for monitoring different segments.          | Easiest and most convenient centralized network monitoring.         |
| Server-sensor | A single machine running the server component, with one or more separate machines running the sensor component. | Sensors handle sniffing, storage, and database management.              | Reduces network traffic by keeping data on sensors until requested. |
| Hybrid        | A combination of standalone and server-sensor installations.                                                    | Combines the benefits of both standalone and server-sensor deployments. | Offers flexibility and scalability.                                 |
##  Network Security Monitoring (NSM) Tools

| Component                                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Bro]([https://github.com/Security-Onion-Solutions/security-onion/wiki/Bro](https://github.com/Security-Onion-Solutions/security-onion/wiki/Bro))                                                                                                        | Bro is a powerful network analysis framework that is much different from the typical IDS.                                                                                                                                                                                                                                                                                                                   |
| [ELSA ]([https://github.com/mcholste/elsa/](https://github.com/mcholste/elsa/))                                                                                                                                                                          | ELSA is a centralized syslog framework that is built on Syslog-NG, MySQL, and Sphinx full-text search. It provides a fully asynchronous web-based query interface that normalizes logs and makes searching billions of them for arbitrary strings as easy as searching the web. It also includes tools for assigning permissions for viewing the logs, email-based alerts, scheduled queries, and graphing. |
| [Netsniff-ng](file:///Applications/Raycast.app/Contents/Resources/RaycastWeb_RaycastWeb.bundle/Contents/Resources/%5Bhttp://netsniff-ng.org/%5D(http://netsniff-ng.org/))                                                                                | Netsniff-ng is a free, performant Linux networking toolkit.                                                                                                                                                                                                                                                                                                                                                 |
| [OSSEC](file:///Applications/Raycast.app/Contents/Resources/RaycastWeb_RaycastWeb.bundle/Contents/Resources/%5Bhttps://ossec.github.io/%5D(https://ossec.github.io/))                                                                                    | OSSEC is an Open Source host-based IDS, or HIDS. It performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting, and active response.                                                                                                                                                                                                                          |
| [Sguil](file:///Applications/Raycast.app/Contents/Resources/RaycastWeb_RaycastWeb.bundle/Contents/Resources/%5Bhttp://sguil.sourceforge.net/%5D(http://sguil.sourceforge.net/))                                                                          | Sguil (pronounced “sgweel”) is built by network security analysts for network security analysts. Sguil’s main component is an intuitive GUI that provides access to real-time events, session data, and raw packet captures. Sguil facilitates the practice of Network Security Monitoring and event driven analysis.                                                                                       |
| [Snort](file:///Applications/Raycast.app/Contents/Resources/RaycastWeb_RaycastWeb.bundle/Contents/Resources/%5Bhttps://www.snort.org%5D(http://www.snort.org/))                                                                                          | Snort is an Open Source network intrusion prevention and detection system (IDS/IPS) developed by Sourcefire. Combining the benefits of signature, protocol, and anomaly-based inspection, Snort is the most widely deployed IDS/IPS technology worldwide. With millions of downloads and over 500,000 registered users, Snort has become the de facto standard for IPS.                                     |
| [Squert](file:///Applications/Raycast.app/Contents/Resources/RaycastWeb_RaycastWeb.bundle/Contents/Resources/%5Bhttp://www.squertproject.org/%5D(http://www.squertproject.org/))                                                                         | Squert is a web application that is used to query and view event data that is stored in a Sguil database (typically IDS alert data). Squert is a visual tool that attempts to provide additional context to events by using metadata, time series representations and weighted and logically grouped result sets.                                                                                           |
| [Suricata](file:///Applications/Raycast.app/Contents/Resources/RaycastWeb_RaycastWeb.bundle/Contents/Resources/%5Bhttp://www.openinfosecfoundation.org/index.php/download-suricata%5D(http://www.openinfosecfoundation.org/index.php/download-suricata)) | The Suricata engine is an Open Source next-generation intrusion detection and prevention engine.                                                                                                                                                                                                                                                                                                            |
# Full Packet Capture

| Factor                       | Description                           | Considerations                                                                                        |
| ---------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Location                     | Placement of sensing interfaces       | Chokepoints like firewall ingress, data center ingress, and VPN client ingress                        |
| Method of network connection | Connection type for sensing interface | SPAN port (least reliable), network tap, or inline                                                    |
| NIC configuration            | Network card settings                 | Disable offloading features (checksum, segmentation) to ensure captured packets match network traffic |

| Feature               | Full Packet Capture                                 | Netflow                                                |
| --------------------- | --------------------------------------------------- | ------------------------------------------------------ |
| Storage Requirements  | High, consumes disk space quickly                   | Lower, more storage efficient                          |
| Data Retention        | Target lifespan varies (hours to months)            | Typically retains flow summaries for longer periods    |
| Storage Sharing       | May need to share storage with other NSM data types | Typically does not share storage with other data types |
| Security Onion Policy | Data purged when drive utilization exceeds 90%      | N/A                                                    |
## TCPdump
![22](/Course-Notes/.assets/Pasted_image_20241115143623.png)![21](/Course-Notes/.assets/Screenshot_2024-11-15_at_14.37.54.png)
# BPF Syntax Examples

| **Parameter**                                              | **Description**                                                                                 |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `host mailserver`                                          | Captures packets from or to host mail server                                                   |
| `host mailserver and webserver`                            | Captures packets between mail server and web server                                            |
| `tcp port 80`                                              | Captures TCP packets to or from port 80                                                       |
| `tcp port http`                                            | Captures TCP packets to or from port 80 or the HTTP port number as defined in the `/etc/services` file |
| `icmp[icmptype] != icmp-echo and icmp[icmptype] != icmp-echoreply` | Captures all ICMP packets that are not echo requests or replies (i.e., not ping packets)       |
| `host 192.168.0.1 and $begin:math:text$192.168.0.2 or 192.168.0.3$end:math:text$`      | Captures traffic between 192.168.0.1 and either 192.168.0.2 or 192.168.0.3                     |
# Session Data

| Tool  | Description                                                       | NSM Functions                                                                                                          | Data Produced                                                                                  |
| ----- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Bro   | Network analysis framework written in the Bro scripting language. | Audit records of every network session and application-layer sessions (e.g., HTTP URIs, MIME types, server responses). | Session data, transaction data, extracted content, statistical data, metadata, and alert data. |
| Argus | Not mentioned.                                                    | Not mentioned.                                                                                                         | Session data.                                                                                  |
| PRADS | Not mentioned.                                                    | Not mentioned.                                                                                                         | Session data.                                                                                  |
# Transaction Data

```
Dec  4 19:02:48 inside-srv postfix/smtpd[7358]: connect from dmz-srv.abc.public[172.16.1.10]
Dec  4 19:02:48 inside-srv postfix/smtpd[7358]: 48C3A186A0A: client=dmz-srv.abc.public[172.16.1.10]
Dec  4 19:02:48 inside-srv postfix/cleanup[7362]: 48C3A186A0A: message-id=<58446858.8050301@services.public>
Dec  4 19:02:48 inside-srv postfix/qmgr[4268]: 48C3A186A0A: from=<william@services.public>, size=160062, nrcpt=1 (queue active)
Dec  4 19:02:48 inside-srv postfix/smtpd[7358]: disconnect from dmz-srv.abc.public[172.16.1.10]
Dec  4 19:02:48 inside-srv postfix/local[7363]: 48C3A186A0A: to=<wendy@abc.private>, orig_to=<wendy@abc.public>, relay=local, delay=0.07, delays=0.06/0/0/0, dsn=2.0.0, status=sent (delivered to maildir)
```

| Feature            | Description                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| Audit Trails       | Provides audit trails of client requests and server responses                                                                       |
| Data Sources       | Sourced from servers: DHCP, DNS, Mail, Web, Proxies, etc.                                                                           |
| Syslog Collection  | Security Onion includes Syslog-ng to collect Syslog messages                                                                        |
| Transaction Logs   | Servers configured to forward transaction logs                                                                                      |
| Bro Integration    | Security Onion includes Bro                                                                                                         |
| Bro Logs           | Capable of producing transaction logs for common application protocols                                                              |
| Data Visualization | As with any of the NSM data types, using an application to present the data can make visualization better and analytic steps easier |
# Alert Data

```
SRC: GET /3rdparty/phpMyAdmin/server_sync.php?c=phpinfo() HTTP/1.1
SRC: Host: www.abc.public
SRC: User-Agent: Mozilla/5.00 (Nikto/2.1.6) (Evasions:None) (Test:006608)
SRC: Connection: Keep-Alive
SRC: 
DST: HTTP/1.1 404 Not Found
DST: Date: Thu, 05 Dec 2019 20:56:43 GMT
DST: Server: Apache/2.2.22 (Debian)
DST: Vary: Accept-Encoding
DST: Content-Length: 313
DST: Keep-Alive: timeout=5, max=49
DST: Connection: Keep-Alive
DST: Content-Type: text/html; charset=iso-8859-1
DST: 
DST: <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
DST: <html><head>
DST: <title>404 Not Found</title>
DST: </head><body>
DST: <h1>Not Found</h1>
DST: <p>The requested URL /3rdparty/phpMyAdmin/server_sync.php was not found on this server.</p>
DST: <hr>
DST: <address>Apache/2.2.22 (Debian) Server at www.abc.public Port 80</address>
DST: </body></html>
```

| Component         | Description                                                                          |
| ----------------- | ------------------------------------------------------------------------------------ |
| IDS/IPS           | IDS = port mirroring or network tap; IPS = inline; IPS with drop disabled = IDS mode |
| Alert Efficacy    | Analyst must determine if the alert was relevant (success or failure)                |
| Alert Correlation | Analyst must correlate alerts to determine if they are related                       |
| Security Onion    | Rules-based IDS operations                                                           |
| Snort             | Snort is a popular IDS/IPS                                                           |
| Suricata          | Suricata is a modern IDS/IPS                                                         |
| Consoles          | Sguil and Squert are consoles for Snort and Suricata                                 |
| ELSA              | ELSA is a log management system                                                      |
| capME!            | capME! is a PCAP decoder                                                             |
## Extracted Content

| Feature              | Description                                                                      |
| -------------------- | -------------------------------------------------------------------------------- |
| Artifacts            | Artifacts that are carved out of real time traffic streams, or out of PCAP files |
| Extractable Content  | Can be files, string, full web pages                                             |
| Bro                  | Bro is capable of extracting files and streams                                   |
| Default Extraction   | Default: all recognized Windows executable files                                 |
| Other Types          | Other types can be configured                                                    |
| Security Onion       | Security Onion includes Network Miner                                            |
| Extracted Data Types | Extracts many data types                                                         |
| Data Types           | Certificates, images, session data, DNS, Host IPs                                |
| Artifacts            | Artifacts that may be extracted include the following:                           |
## Statistical Data

| Feature                                   | Description                                                                                                                               |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Aggregates events and provides summaries  | Useful in developing an overall picture                                                                                                   |
| Queried and reported in different formats | Can answer questions: Which hosts request the most HTTP data? Which hosts serve the most HTTP data? Which DNS domains are most requested? |
| Produce baselines over time.              |                                                                                                                                           |
![20](/Course-Notes/.assets/Pasted_image_20241115181903.png)
## Meta data — data about data
- Geolocation
- Ownership
- Reputation
	- Email
	- C&C
	- Malware distribution
# Personally Identifiable Information
![19](/Course-Notes/.assets/Pasted_image_20241116094050.png)

| Data Type | Examples                                                                                                                                                                                                                |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PII       | Name, telephone numbers, date and place of birth, passport number, social security number, driver license number, personal characteristics (photographic image, x-rays, fingerprints, biometric image or template data) |
| Non-PII   | Office location, business email address, other information releasable to the public                                                                                                                                     |
# Regulatory Compliance
![18](/Course-Notes/.assets/Pasted_image_20241116094441.png)Current trends in regulatory compliance include the following:

- Strengthened enforcement
- Global spread of data breach notification laws
- More prescriptive regulations
- Growing requirements regarding third parties (business partners)
- Risk-based compliance on the rise
- Compliance process streamlined and automated
## Examples of compliance regulations

|                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Regulation                                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                 | Scope                                                                                                                                                                                                                                   |
| PCI DSS                                                                                                                                                                                                                                                                                                        | Proprietary information security standard for organizations handling branded credit cards.                                                                                                                                                                                  | Visa, MasterCard, American Express, Discover, and JCB                                                                                                                                                                                   |
| HIPAA                                                                                                                                                                                                                                                                                                          | Legislation requiring national standards for healthcare transactions to protect patient information.                                                                                                                                                                        | Electronic transfer of confidential patient information                                                                                                                                                                                 |
| SOX Act                                                                                                                                                                                                                                                                                                        | Legislation to protect shareholders and the public from accounting errors and fraudulent practices.                                                                                                                                                                         | Enterprises to improve the accuracy of corporate disclosures                                                                                                                                                                            |
| General Data Protection Regulation (GDPR)                                                                                                                                                                                                                                                                      | Applies to organizations handling personal data of EU citizens, regardless of location.                                                                                                                                                                                     | Fines for non-compliance can reach up to 4% of annual global revenue or EUR 20 million per violation. Strengthens consent requirements, introduces the right to erasure and data portability, and mandates 72-hour breach notification. |
| Public Sector Information (PSI) Directive (Open Data Directive)<br>[REF1](https://ec.europa.eu/digital-single-market/en/implementation-public-sector-information-directive-member-states)<br>[REF2](https://ec.europa.eu/digital-single-market/en/public-sector-information-psi-directive-open-data-directive) | Governs the reuse of public sector information across the EU.                                                                                                                                                                                                               | Encourages free reuse of public sector data, limits charges to marginal costs, and strengthens transparency requirements for public-private agreements.                                                                                 |
| Federal Information Security Management Act (FISMA)                                                                                                                                                                                                                                                            | Bolstered computer and network security within the U.S. government by requiring yearly audits.                                                                                                                                                                              |                                                                                                                                                                                                                                         |
| Gramm-Leach-Bliley Act (GLBA)                                                                                                                                                                                                                                                                                  | Erased antitrust laws prohibiting bank mergers and information sharing, aiming to encourage competition.                                                                                                                                                                    |                                                                                                                                                                                                                                         |
| Personal Information Protection and Electronic Documents Act (PIPEDA)                                                                                                                                                                                                                                          | A Canadian law governing how private sector organizations collect, use, and disclose personal information.                                                                                                                                                                  |                                                                                                                                                                                                                                         |
| Data Protection Directive (95/46/EC)                                                                                                                                                                                                                                                                           | Regulates the processing of personal data within the European Union.                                                                                                                                                                                                        |                                                                                                                                                                                                                                         |
| Basel II                                                                                                                                                                                                                                                                                                       | The second Basel Accord, Basel II is a set of recommendations on banking laws and regulations. It aims to establish an international standard for banking regulators to control the amount of capital banks must hold to safeguard against financial and operational risks. |                                                                                                                                                                                                                                         |
| Digital Millennium Copyright Act (DMCA)                                                                                                                                                                                                                                                                        | A U.S. copyright law implementing two 1996 WIPO treaties. It criminalizes the production and dissemination of technology intended to circumvent digital rights management (DRM) measures, as well as the act of circumventing such measures.                                |                                                                                                                                                                                                                                         |
| Safe Harbor Act                                                                                                                                                                                                                                                                                                | A regulatory framework enabling data transfer between the EU and the U.S. It establishes privacy processes and safeguards to bridge privacy differences and facilitate international trade.                                                                                 |                                                                                                                                                                                                                                         |
# Intellectual Property

| Impact                   | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| Financial Loss           | Billions of dollars in losses annually.                   |
| Job Displacement         | Loss of numerous jobs due to intellectual property theft. |
| Reputational Damage      | Negative impact on company reputation.                    |
| Legal Consequences       | Potential litigation and regulatory sanctions.            |
| Operational Disruption   | Disruption of business operations.                        |
| Competitive Disadvantage | Undermining of competitiveness in the market.             |
## Information Assets

| Traditional Intellectual Property                           | Expanded Definition of Information Assets                                                                                                |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Patented inventions                                         | Patented inventions, human capital (employees’ inventive skills, technical knowledge, and institutional memory)                          |
| Customer lists and client files                             | Customer lists and client files, sales tools, marketing materials, and advertising plans                                                 |
| Sales figures and budget projections                        | Sales figures and budget projections, sensitive financials (credit rating, mergers/acquisitions, stock price, private capital infusions) |
| Design documents and plans for future products and services | Design documents and plans for future products and services, R&D results, test data, and market studies                                  |
| Banking information                                         | Banking information, business processes, proprietary practices, and supply chain innovations                                             |
## Threat Spectrum

| Threat Actor             | Description                                                                        | Motivation                                       |
| ------------------------ | ---------------------------------------------------------------------------------- | ------------------------------------------------ |
| Organized Crime          | Professional hackers and counterfeiters operating in illegal schemes.              | Generate revenue from stolen information assets. |
| Unscrupulous Competitors | Employ illegal techniques like industrial espionage and reverse engineering.       | Gain unfair advantages in the marketplace.       |
| State Entities           | Use eminent domain or intelligence agencies to seize intellectual property.        | Benefit domestic industries.                     |
| Individuals              | Current and former employees, or competitor agents, steal proprietary information. | Sell information to other entities.              |
## A Pervasive Security Culture

| Aspect               | Description                                                                            |
| -------------------- | -------------------------------------------------------------------------------------- |
| Inventory            | Carefully inventory information assets to understand their value.                      |
| Relationships        | Identify how assets relate to employees, suppliers, partners, etc.                     |
| Defense              | Secure network borders and understand user interactions.                               |
| Strategy             | Align security measures with business plans, IT strategy, risk tolerance, and culture. |
| Employee Involvement | Foster a security culture valuing information assets.                                  |
| Employee Engagement  | Ensure employees feel ownership of security principles.                                |
| Data Lifecycle       | Understand data flow, access, and storage.                                             |
| Security Framework   | Shift focus from perimeter security to protecting sensitive data.                      |
| Visibility           | Increase network visibility to detect information asset loss.                          |
| Zero Trust Model     | Implement a comprehensive access control approach.                                     |
# [[Basic Cryptography Concepts]]

| Attack Vector          | Description                                              | Consequences                                |
| ---------------------- | -------------------------------------------------------- | ------------------------------------------- |
| Breaking the Algorithm | Attempting to reverse the encryption process.            | Potential access to sensitive information.  |
| Using the Algorithm    | Leveraging cryptography to conceal malicious activities. | Bypassing security measures like firewalls. |

| Category                               | Example                                            | Description                                                                                                                                                                              |
| -------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Circumventing cryptographic algorithms | OpenSSL Heartbleed vulnerability (CVE-2014-0160)   | Exploits a flaw in the TLS heartbeat extension (RFC 6520) validation, allowing attackers to retrieve private data from server memory.                                                    |
| Cryptography as an attack technology   | TLS/SSL encryption for command and control traffic | Attackers use TLS/SSL to conceal malicious communications, making detection challenging. Detection methods include decryption and signature analysis, or traffic analysis using NetFlow. |
## Digital Certificates
Valid:
![17](/Course-Notes/.assets/Pasted_image_20241116142752_1.png)
Not valid:
![16](/Course-Notes/.assets/Pasted_image_20241116142803_1.png)
# Cryptography Overview

| Term                  | Description                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------ |
| Cryptology            | Umbrella term covering cryptography and cryptanalysis.                                     |
| Cryptanalysis         | Practice and study of weaknesses in cryptographic techniques.                              |
| Cryptography          | Practice and study of securing communications in the presence of third parties.            |
| Confidentiality       | Ensuring only authorized parties can read a message.                                       |
| Data integrity        | Ensuring any changes to data in transit will be detected and rejected.                     |
| Origin authentication | Ensuring messages received were actually sent from the perceived origin.                   |
| Non-repudiation       | Ensuring the original source of a secured message cannot deny having produced the message. |
![15](/Course-Notes/.assets/Screenshot_2024-11-16_at_14.33.57_1.png)![14](/Course-Notes/.assets/Screenshot_2024-11-16_at_14.37.24_1.png)
## Ciphers for Everyone

| Cipher Type                  | Description                                        | Example                                                         | Key                                                                            |
| ---------------------------- | -------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Substitution Cipher          | Substitutes one letter for another.                | Caesar cipher: Shift alphabet by a certain key (e.g., 5).       | A becomes F, B becomes G, and so on.                                           |
| Poly alphabetic Cipher       | Uses multiple substitution alphabets.              | Vigenère cipher: A series of Caesar ciphers based on a keyword. | Key: “SECRETKEY”, Message: “ATTACK AT DAWN”, Encrypted message: “SXVRGDKXBSAP” |
| Transposition Cipher         | Rearranges or permutates letters.                  | THE PACKAGE IS DELIVERED -> DEREVILEDSIEGAKCAPEHT               | Reversal                                                                       |
| Rail Fence Cipher            | Words are spelled out as if they are a rail fence. | THE PACKAGE IS DELIVERED -> DEREVILEDSIEGAKCAPEHT               | 3                                                                              |
| One-time Pad (Vernam Cipher) | XOR operation is applied to plaintext with a key.  | THE PACKAGE IS DELIVERED -> DEREVILEDSIEGAKCAPEHT               | Random data (challenging to create and distribute)                             |
# Hash Algorithms

| Feature                           | Description                                                               |
| --------------------------------- | ------------------------------------------------------------------------- |
| Secret Key                        | Shared between sender and receiver.                                       |
| Hash Function                     | Used to generate the message authentication code.                         |
| Message Authentication Code (MAC) | Output of the hash function, combining message data and the secret key.   |
| Security                          | MAC ensures only sender and receiver can compute the correct hash digest. |
| Authentication                    | Receipt of a valid MAC confirms the message’s origin.                     |
![13](/Course-Notes/.assets/Pasted_image_20241116154057_1.png)
## Cryptographic Authentication in Action
![12](/Course-Notes/.assets/Pasted_image_20241116154147_1.png)

| Step | Description                                                                                                            |
| ---- | ---------------------------------------------------------------------------------------------------------------------- |
| 1    | Sender inputs data and secret key into a hashing algorithm.                                                            |
| 2    | The algorithm calculates a fixed-length message authentication code (MAC).                                             |
| 3    | The MAC, or fingerprint, is attached to the message and sent to the receiver.                                          |
| 4    | The receiver removes the fingerprint from the message.                                                                 |
| 5    | The receiver uses the received message and its copy of the secret key as input to the same hashing function.           |
| 6    | If the calculated fingerprint matches the received fingerprint, data integrity and origin authentication are verified. |

| Product                    | Use Case                                       | Description                                                                                       |
| -------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| IPsec gateways and clients | Packet integrity and authenticity verification | Uses a hashing algorithm (RFC 2104) for more complex verification than a simple keyed hash.       |
| Cisco IOS routers          | Routing protocol updates authentication        | Adds authentication information to routing protocol updates using keyed hashing with secret keys. |
| Cisco software images      | Downloaded image integrity check               | Provides an MD5-based checksum for customers to verify the integrity of downloaded images.        |
| Various                    | Data encryption                                | Hashing can be used in a feedback-like mode to encrypt data.                                      |

| Feature               | Description                                                              | Security Level | Privacy |
| --------------------- | ------------------------------------------------------------------------ | -------------- | ------- |
| Keyed Hash Validation | Validates route integrity using a hash function and a shared secret key. | High           | Low     |
| Secret Key Importance | The strength of the technique relies on the secrecy of the key.          | N/A            | N/A     |
| Attack Mitigation     | Prevents route manipulation by attackers.                                | High           | Low     |
| Data Confidentiality  | Does not provide privacy; routing updates can be read by attackers.      | N/A            | Low     |
![11](/Course-Notes/.assets/Pasted_image_20241116165230_1.png)

## Comparing Hashing Algorithms

| Algorithm          | Description                                                                                              | Notes                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| MD5                | A one-way function                                                                                       | Vulnerable to collisions, not recommended for new applications                           |
| SHA-1              | A secure hash algorithm                                                                                  | Larger message digest than MD5, more secure against attacks                              |
| SHA-2              | Six algorithms (SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256)                        | Generate message digests of varying lengths (224-512 bits) based on input message length |
| SHA-512            | More efficient than SHA-256 on 64-bit systems                                                            | SHA-512/224 and SHA-512/256 provide a smaller digest size                                |
| SHA-2 Adoption     | Approved by NIST in 2006 for federal agencies                                                            | Mandated for collision-resistant applications after 2010 due to SHA-1 vulnerabilities    |
| SHA-3              | A family of cryptographic hash functions and extendable-output functions                                 | Includes SHA3-224, SHA3-256, SHA3-384, SHA3-512, SHAKE128, and SHAKE256                  |
| SHA-3 Applications | Used in digital signatures, key derivation, pseudorandom bit generation, and other security applications |                                                                                          |
| SHA-3 Advantages   | Offers a backup to SHA-2                                                                                 | Can be implemented with minimal circuitry, suitable for small devices                    |
# Encryption Overview

| Layer             | Description                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| Application Layer | Encrypt application layer data, such as encrypting email messages with PGP.                    |
| Session Layer     | Encrypt session layer data using a protocol such as SSL or TLS.                                |
| Network Layer     | Encrypt network layer data using protocols such as those provided in the IPsec protocol suite. |
| Data Link Layer   | Encrypt data link layer using MACsec (IEEE 802.1AE) or proprietary link-encrypting devices.    |
![10](/Course-Notes/.assets/Pasted_image_20241116170740_1.png)
## Encryption Algorithm Features

| Feature                    | Description                                                                                               |
| -------------------------- | --------------------------------------------------------------------------------------------------------- |
| Resilience to Attacks      | Resists common attacks by requiring a long key length, making brute force attacks unfeasible.             |
| Key Length and Scalability | Longer keys provide stronger encryption, while scalability allows for flexible key selection.             |
| Avalanche Effect           | Small changes in plaintext result in significant changes in ciphertext, ensuring message confidentiality. |
# Cryptanalysis
The practice of breaking encrypted codes. 

| Attack Type             | Description                                           | Practicality                                                       | Countermeasures                                             |
| ----------------------- | ----------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| Brute-force attack      | Tries every possible key.                             | High, if key space is small.                                       | Use large key spaces (e.g., AES).                           |
| Ciphertext-only attack  | Attempts to recover plaintext from ciphertext.        | Low, due to pseudorandom output of modern algorithms.              | Use pseudorandom encryption algorithms.                     |
| Known-plaintext attack  | Attempts to decrypt ciphertext using known plaintext. | Moderate, if plaintext characteristics are known.                  | Use large key spaces and obscure plaintext characteristics. |
| Chosen-plaintext attack | Attempts to decrypt ciphertext by choosing plaintext. | Low, due to difficulty in capturing both ciphertext and plaintext. | Maintain secure communication channels.                     |

| Attack Type              | Description                                                                         | Example                                                                                                | Notes                                                                           |
| ------------------------ | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Chosen-ciphertext attack | Attacker chooses ciphertext and has access to decrypted plaintext.                  | Attacker sends data through a tamper-proof encryption device to deduce the embedded key.               | Requires access to both ciphertext and plaintext, making it less practical.     |
| Birthday attack          | A brute-force attack against hash functions, exploiting statistical probability.    | Repeatedly applying a hash function to random inputs until a collision (duplicate output) occurs.      | Theory can be demonstrated with a group of 23 people sharing the same birthday. |
| Meet-in-the-middle       | A known-plaintext attack where the attacker has access to plaintext and ciphertext. | Encrypt plaintext with all possible keys and store results. Decrypt ciphertext with all possible keys. | Effective against block ciphers with long keys.                                 |
# Symmetric Encryption Algorithms
AKA "private key encryption"
Hardest part is keeping the secret keys safe.

- Often found in IPsec technology. Fast and used for bulk encryption, VPN protection, and data privacy.
- Challenges: Secure key exchange between parties.
- Key Length: ≥80 bits are more secure against brute-force attacks, while shorter lengths are obsolete.

DES, 3DES, AES, IDEA, RC2/4/5/6, Blowfish, SEAL, IDEA, Blowfish, Twofish, and Serpent.

| Algorithm | Description                                                | Advantages                                      | Challenges                                   |
| --------- | ---------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------- |
| DES       | A block cipher encrypting 64-bit blocks with a 56-bit key. | Simple, widely used.                            | Vulnerable to brute-force attacks.           |
| 3DES      | Applies DES three times with different keys.               | More secure than DES.                           | Slower than AES.                             |
| AES       | An iterated block cipher using 128, 192, or 256-bit keys.  | Stronger key length than DES, faster than 3DES. | None significant.                            |
| RC4       | A stream cipher used in SSL/TLS.                           | Fast, widely used.                              | Potential weaknesses, but considered secure. |
# Asymmetric Encryption Algorithms

| Feature             | Description                                                                                                |
| ------------------- | ---------------------------------------------------------------------------------------------------------- |
| Key Length Range    | 1024 to 4096 bits.                                                                                         |
| Variable key length | Allows for trade-off between speed and security.                                                           |
| Security Basis      | Difficulty of factoring large numbers.                                                                     |
| Key Management      | Simpler key management because one key can be public.                                                      |
| Security Services   | Provides confidentiality and origin authentication.                                                        |
| Usage               | Used for low-volume cryptographic mechanisms like digital signatures and key exchange due to slower speed. |
![9](/Course-Notes/.assets/Pasted_image_20241117094405_1.png)

| Method                    | Description                                                          | Example                 |
| ------------------------- | -------------------------------------------------------------------- | ----------------------- |
| Public Key Encryption     | Encrypt with recipient’s public key, decrypt with their private key. | Confidentiality         |
| Private Key Encryption    | Encrypt with sender’s private key, decrypt with their public key.    | Origin Authentication   |
| PGP (Pretty Good Privacy) | A widely used encryption software.                                   | Email                   |
| Public/Private Key Pair   | Two keys, one for encryption and one for decryption.                 | Share Public Keys       |
| Encrypt Twice             | Encrypt with both public and private keys.                           | Private Key, Public Key |
| Receiving Devices         | Decrypt with private key, then with public key.                      | Decryption Process      |
| Symmetric Encryption      | Used for bulk data encryption in protocols like SSH, SSL, and IPsec. | Real-Time Protocols     |
# [Diffie-Hellman Key Agreement]([https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange))

| Feature                  | Description                                   |
| ------------------------ | --------------------------------------------- |
| Purpose                  | Share information over an untrusted network.  |
| Shared Secret            | Mutually computed shared secret.              |
| Security                 | Cannot be computed by eavesdroppers.          |
| Computational Complexity | Expensive to compute, intractable to reverse. |
| Applications             | SSL/TLS, SSH, IKE.                            |
![8](/Course-Notes/.assets/Pasted_image_20241117100948_1.png)

| Concept                                | Description                                                                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DH Key Agreement Process               | Two parties (Alice and Bob) agree on a common color (large prime number p and generator g) and each selects a secret color (private key). They publicly exchange their mixed colors (public keys) and finally mix the received color with their private color to get the shared secret key. |
| Public Key Calculation                 | Alice’s public key (A) is calculated using g, p, and her private key (a), while Bob’s public key (B) is calculated using g, p, and his private key (b).                                                                                                                                     |
| Shared Secret Key Calculation          | Alice and Bob each mix the received public key with their private key to get the shared secret key.                                                                                                                                                                                         |
| Shared Secret Key Calculation          | Both parties calculate the same shared secret key (s) using their private keys, the other party’s public key, and a prime number (p).                                                                                                                                                       |
| DH Group Strength and Computation Time | Different DH groups determine key strength and computation time, with higher group numbers offering greater security but requiring more time.                                                                                                                                               |
| Ephemeral Diffie-Hellman (EDH)         | EDH uses temporary private keys for each key exchange, ensuring perfect forward secrecy (PFS) even if a private key is exposed.                                                                                                                                                             |
The mathematical model in the DH key exchange process:

| Variable | Description                   | Visibility                             |
| -------- | ----------------------------- | -------------------------------------- |
| p        | Large prime number            | Known to Alice, Bob, and Eve           |
| g        | Generator                     | Known to Alice, Bob, and Eve           |
| a        | Alice’s chosen private key    | Known only to Alice                    |
| b        | Bob’s chosen private key      | Known only to Bob                      |
| A        | Alice’s calculated public key | Known to Alice, Bob, and Eve           |
| B        | Bob’s calculated public key   | Known to Alice, Bob, and Eve           |
| s        | Shared secret key             | Known to Alice and Bob, but not to Eve |
After each party calculates the shared secret key **s** independently, each party will end up with the exact same value **s**. All three formulas for **s** will produce the same result. **s** = **g**^**ab** mod **p** = **B**^**a** mod **p** = **A**^**b** mod **p**.

# SSH Legacy Encryption

| Feature                | SSHv1                                                                            | SSHv2                                                                      |
| ---------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Privacy                | Provided                                                                         | Provided                                                                   |
| Data Integrity         | Provided                                                                         | Provided                                                                   |
| Origin Authentication  | Provided                                                                         | Provided                                                                   |
| Key Exchange Mechanism | Asymmetric encryption for key exchange, Symmetric encryption for data encryption | Diffie-Hellman (DH) key exchange, Symmetric encryption for data encryption |

| Feature                             | Description                                                                                                                                                                                                                                                                            |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection Establishment            | Client connects to server, Server presents public key, Client and server negotiate symmetric encryption algorithm (in clear text), Client encrypts session key with server’s public key, Server decrypts session key, and both parties share the session key for symmetric encryption. |
| Data Protection                     | After key exchange, all user credentials and data are protected using symmetric encryption.                                                                                                                                                                                            |
| Asymmetric Encryption Functionality | Facilitates symmetric key exchange and peer authentication.                                                                                                                                                                                                                            |
| Peer Authentication Mechanism       | Clients recognize non-authentic systems by comparing provided public keys with known server keys.                                                                                                                                                                                      |
| User Authentication Challenge       | Users often lack the knowledge to verify the authenticity of server public keys, despite client software displaying them.                                                                                                                                                              |
# Digital Signatures
## RSA Digital signature
![7](/Course-Notes/.assets/Pasted_image_20241117110846_1.png)

| Process              | Description                                                                    |
| -------------------- | ------------------------------------------------------------------------------ |
| Signature Process    | The signer creates a hash, or fingerprint, of the document.                    |
| Signature Process    | The signer encrypts the hash with their private key.                           |
| Signature Process    | The encrypted hash, known as the signature, is added to the document.          |
| Verification Process | The verifier obtains the signer’s public key.                                  |
| Verification Process | The verifier decrypts the signature using the signer’s public key.             |
| Verification Process | The verifier compares the decrypted hash to the hash of the received document. |

| Digital Signatures                                                        |
| ------------------------------------------------------------------------- |
| Proves the source of the data and that the signer has seen and signed it. |
| Ensures the data has not been changed since it was signed.                |
| Prevents the signer from denying they signed the data.                    |
| The signature is authentic and cannot be forged.                          |
| The signature is unique to the document and cannot be reused.             |
| The signature cannot be altered after the document is signed.             |
| The signer cannot deny signing the document.                              |
# PKI Overview

| Challenge                                                                                                         | Solution                                                                                                                                                              | Role                                                                                                                                        |
| ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Public Key Distribution Challenge: Ensuring the authenticity of public keys to prevent man-in-the-middle attacks. | Public Key Infrastructure (PKI) Solution: PKI provides a framework for secure public key distribution through digital certificates and certificate authorities (CAs). | Certificate Authority (CA) Role: CAs act as trusted third parties, signing digital certificates to validate the authenticity of public keys |
![6](/Course-Notes/.assets/Pasted_image_20241117131431_1.png)
## PKI Terminology and Components

| Term          | Description                                                                          |
| ------------- | ------------------------------------------------------------------------------------ |
| PKI           | Service framework supporting large-scale public key-based technologies.              |
| CA            | Trusted third party signing public keys in a PKI-based system.                       |
| Certificate   | Document binding an entity’s name to its public key, signed by the CA.               |
| Vendors       | Offer CA servers as managed services or products (e.g., VeriSign, Entrust, GoDaddy). |
| Organizations | May implement private PKIs using Microsoft Server or Open SSL.                       |
## Public-Key Cryptography Standards

| PKCS Standard | Description                                     |
| ------------- | ----------------------------------------------- |
| PKCS #1       | RSA Cryptography Standard                       |
| PKCS #3       | D-H Key Agreement Standard                      |
| PKCS #5       | Password-Based Cryptography Standard            |
| PKCS #6       | Extended-Certificate Syntax Standard            |
| PKCS #7       | Cryptographic Message Syntax Standard           |
| PKCS #8       | Private-Key Information Syntax Standard         |
| PKCS #10      | Certification Request Syntax Standard           |
| PKCS #12      | Personal Information Exchange Syntax Standard   |
| PKCS #13      | Elliptic Curve Cryptography Standard            |
| PKCS #15      | Cryptographic Token Information Format Standard |
### X.509v3 structure

| Field                                | Description                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------- |
| Version                              | The version of the X.509 certificate format.                                 |
| Serial number                        | A unique identifier for the certificate.                                     |
| Algorithm ID                         | The identifier for the cryptographic algorithm used to sign the certificate. |
| Issuer                               | The entity that issued the certificate.                                      |
| Validity                             | The period during which the certificate is valid.                            |
| Not before                           | The date and time before which the certificate is not valid.                 |
| Not after                            | The date and time after which the certificate is no longer valid.            |
| Subject                              | The entity to which the certificate is issued.                               |
| Subject public key info              | Information about the subject’s public key.                                  |
| Public key algorithm                 | The algorithm used for the subject’s public key.                             |
| Subject public key                   | The subject’s public key.                                                    |
| Issuer unique identifier (optional)  | A unique identifier for the issuer (optional).                               |
| Subject unique identifier (optional) | A unique identifier for the subject (optional).                              |
| Extensions (optional)                | Additional information about the certificate (optional).                     |
| Certificate signature algorithm      | The algorithm used to sign the certificate.                                  |
| Certificate signature                | The signature created by the issuer using its private key.                   |
# PKI Operations
## Certificate Enrolment
![5](/Course-Notes/.assets/Pasted_image_20241117132940_1.png)To obtain an identity certificate, a system administrator will enroll with the PKI. 
1. Obtain the CA’s identity certificate. 
2. Certificate signing request (CSR) (PKCS #10). 
	- Identity information that is associated with the enrolling system
		- system name, 
		- the organization to which the system belongs, 
		- and location information.
3. System’s public key is included with the CSR
## Authentication Using Certificates
![4](/Course-Notes/.assets/Pasted_image_20241117133854_1.png)

| Component                       | Description                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Certificate Authority (CA) Role | Not involved in certificate validation; systems use the root CA certificate to validate signatures on received certificates. |
| Certificate Function            | Identifies the valid public key of a peer, not the peer’s identity directly.                                                 |
| Peer Identity Verification      | Systems challenge peers to prove possession of the private key associated with the validated public key to confirm identity. |
## Certificate Revocation

![3](/Course-Notes/.assets/Pasted_image_20241117134042_1.png)

| Certificate Revocation Reason                                                 | Certificate Revocation Process                                                                               | Certificate Revocation Method                                                                        |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Keys are compromised or business use of the certificate calls for revocation. | Generating new keys forces the creation of a new digital certificate, rendering the old certificate invalid. | A centralized function providing “push” and “pull” methods to obtain a list of revoked certificates. |

| Method                                                                     | Description                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| CRL                                                                        | A list of revoked certificate serial numbers is distributed as a time-stamped, CA-signed file.    |
| OCSP                                                                       | Entities can query the OCSP server at any time to check for validity of the received certificate. |
There is a window of opportunity for attackers while the new CRL is not yet propagated.
# SSL/TLS

- Purpose of SSL/TLS: Provide secure transactions between web browsers and web servers.
- Standardization: SSL is obsolete, replaced by TLS, which is standardized by the IETF.
- TLS Version 1.3: Introduces changes to improve security, privacy, and performance compared to TLS 1.2.

| TLS           | Description                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Functionality | Provides secure communication between peers using PKI authentication and public key encryption for session key exchange. |
| Applications  | Widely used for secure web communication (HTTPS) and also applied to applications like SMTP, LDAP, and POP3.             |
| Goal          | Establish a secure channel between communicating peers, relying on a reliable data stream from the underlying transport. |
![2](/Course-Notes/.assets/Pasted_image_20241117150156_1.png)

| Cipher Suite            | Description                                                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Cipher Suite Definition | Defined in protocol documents (RFC 5246 for TLS 1.2) and specify the structure and use of cipher suites.                         |
| Mandatory Cipher Suite  | TLS_RSA_WITH_AES_128_CBC_SHA, including RSA for authentication and key exchange, AES for confidentiality, and SHA for integrity. |
| Cipher Suite Registry   | Maintained by IANA and defined in RFC 2434 to support future protocols.                                                          |
## Web Browser Security Warnings

| Issue                      | Description                                                       | Potential Impact                                                                                 |
| -------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Hostname/identity mismatch | URL hostname does not match the name in the server’s certificate. | May indicate a phishing attempt or a compromised server.                                         |
| Validity date range        | Certificate has expired or is not yet valid.                      | Expired certificates may be due to oversight, but they could also indicate a compromised server. |
| Signature validation error | Browser cannot verify the certificate’s signature.                | Could indicate a man-in-the-middle attack or a compromised server.                               |
# Cipher Suite

| Feature                  | Description                                                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| TLS Cipher Suites        | Define a set of cryptographic algorithms for authentication, key exchange, encryption, message authentication code, and PRF algorithms. |
| TLS Handshake            | Involves a client hello and a server hello, where the client presents a list of supported cipher suites and the server selects one.     |
| TLS Protocol Flexibility | Allows for the modification of encryption, key exchange, and message authentication algorithms without replacing the entire protocol.   |

| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | Description                                 |
| --------------------------------------- | ------------------------------------------- |
| 1. ECDHE_ECDSA                          | Authentication and key exchange algorithms. |
| 2. AES_256_GCM                          | Bulk encryption algorithm.                  |
| 3. SHA-384                              | Pseudorandom function.                      |

| TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 | Description                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 1. ECDHE_ECDSA                          | Authentication and key exchange algorithms.                                                             |
| 2. AES_128_CBC                          | Bulk encryption algorithm. Unlike AES GCM, AES CBC mode does not provide data authenticity (integrity). |
| 3. SHA-256                              | - Hashed Message Authentication Code algorithm.<br>- Used for the pseudo-random function.               |

| TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA256_P384 | Description                                                                                                                                                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. ECDHE_ECDSA                               | the authentication and key exchange algorithms.                                                                                                                                                               |
| 2. AES_256_CBC                               | the bulk encryption algorithm. Unlike AES GCM, AES CBC mode does not provide data authenticity (integrity). Therefore, a message authentication code algorithm is required for data authenticity (integrity). |
| 3. SHA-256                                   | the Hashed Message Authentication Code algorithm.                                                                                                                                                             |
| 4. SHA-384                                   | specified to be used for the pseudo-random function.                                                                                                                                                          |

| Feature                        | Description                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| NULL Cipher                    | Only for testing or debugging purposes, not for actual encryption.                                                                               |
| Insecure Cipher Suites         | Legacy cipher suites using DES, RC4, or MD5 are not recommended due to security vulnerabilities.                                                 |
| TLS v1.3 Security Enhancements | Removes support for outdated features like RSA, MD5, and weak elliptic curves, reducing the attack surface and ensuring perfect forward secrecy. |
# Key Management

Key management deals with the secure generation, verification, exchange, storage, and destruction of keys. It is extremely important to have secure methods of key management.

- Key Management Importance: Crucial for cryptosystem design, often the most challenging aspect.
- Impact of Key Management: Mistakes can lead to cryptosystem failures, and modern algorithms rely on key management.
- Attack Focus: Most attacks target key management rather than the cryptographic algorithm itself.

| Category                  | Description                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Key Management Components | ==Key Generation:== Automated process requiring effective randomization to ensure equal key likelihood and prevent predictability for attackers.                          |
|                           | ==Key Storage:== Secure storage is crucial, considering potential vulnerabilities like memory swapping on multiuser systems.                                              |
|                           | ==Key Management Procedures:== Include key verification, secure key exchange, key revocation, and key destruction for robust security.                                    |
| Key Spaces                | Key Space: The set of all possible key values for an algorithm, with a key of n bits producing 2^n possible values.                                                       |
|                           | Key Space Size: Determined by the number of bits in the key, with 2n possible key values for an n-bit key.                                                                |
|                           | Weak Keys: Exist in almost every algorithm and should be prevented in implementation.                                                                                     |
| Key Length Issues         | Brute-Force Attack: A method of breaking a cryptographic system by trying all possible keys, which becomes infeasible with sufficiently large key spaces.                 |
|                           | Key Length Selection: Determines the balance between protection strength and performance, with longer keys providing stronger protection but potentially impacting speed. |
# NSA Suite B
![1](/Course-Notes/.assets/Screenshot_2024-11-17_at_18.00.33.png)
- Cryptographic Algorithms: Suite B cryptography uses AES, ECDSA, ECDH, and SHA-2 for encryption, digital signatures, key agreement, and message digesting, respectively.
- Information Assurance: The NSA considers these algorithms sufficient for protecting classified information.

 NSA Suite B cryptography for IPsec is standardized in RFC 6379 and has industry acceptance.