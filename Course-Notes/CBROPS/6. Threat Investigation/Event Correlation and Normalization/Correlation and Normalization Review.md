%% #review %%
# [[Event Sources]]
 
 Types of Event Sources

| **DHCP server**                    | **Transaction data**: Dynamic IP address assignments. Attribution to a host by MAC address.                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                    | **Example**: If the same IOCs (such as CnC traffic to a particular CnC controller address) are seen at different points in the day from different IP addresses, the DHCP server logs may confirm that it is the same device (same MAC address) that is roaming between different wireless networks.                                                                                                                                      |
| **DNS server**                     | **Transaction data**: DNS queries/responses transactions.                                                                                                                                                                                                                                                                                                                                                                                |
|                                    | **Example**: Looking for DGA domain names, which are often used in malware campaigns. Suspicious data in the DNS transactions may imply DNS tunneling.                                                                                                                                                                                                                                                                                   |
| **AAA server**                     | **Alert data**: Successful and failed authentication and authorization events.                                                                                                                                                                                                                                                                                                                                                           |
|                                    | **Example**: Many failed authentication events may indicate attempts at a password attack. More important is the successful authentication event at the end of the series of failures, which may indicate successful unauthorized access.                                                                                                                                                                                                |
| **NetFlow-capable network device** | **Session data**: NetFlow v5 records (IP 5-tuples, byte and packet count, and time stamps). NetFlow v9 and IPFIX are extendable and can have much more data included. Cisco Stealthwatch provides integration with other security devices such as the Cisco Web Security Appliance (WSA) and the Cisco Identity Services Engine (ISE) to provide additional data such as username, user device type, and URL requests with the IP flows. |
|                                    | **Statistical data**: NetFlow data can be processed to perform reports such as top conversations and top hosts. It can also be analyzed against time to produce baselines.                                                                                                                                                                                                                                                               |
|                                    | **Example**: Use NetFlow to determine the normal traffic baseline. Traffic exceeding the baseline may indicate malicious activities. An organization may know that there is no more than 1 GB of data that is typically sent to China during nonbusiness hours, but today FTP traffic to China exceeding 10 GB during nonbusiness hours indicates a possible data exfiltration.                                                          |
| **IPS**                            | **Alert data**: IPS alerts triggered by the IPS rules and signatures.                                                                                                                                                                                                                                                                                                                                                                    |
|                                    | Some IPS solutions can capture the trigger packet or can capture conversations or time-based complete packet captures.                                                                                                                                                                                                                                                                                                                   |
|                                    | **Example**: If it is a true positive, data that is contained within the alert, such as the IP 5-tuple, can be used to correlate with other network security monitoring data.                                                                                                                                                                                                                                                            |
| **Firewall**                       | **Session data**: Connection events, NAT translations.                                                                                                                                                                                                                                                                                                                                                                                   |
|                                    | **Packet captures**: PCAPs are collected manually by the firewall administrator.                                                                                                                                                                                                                                                                                                                                                         |
|                                    | **Statistical data**: Top sources and destinations, top access rules.                                                                                                                                                                                                                                                                                                                                                                    |
|                                    | **Example**: Correlating the firewall events to the other events or correlation of the pre- and post-NAT IP address.                                                                                                                                                                                                                                                                                                                     |
| **Proxy (web and email)**          | **Transaction data**: Documents client requests and server responses.                                                                                                                                                                                                                                                                                                                                                                    |
|                                    | **Extracted data**: Malicious email attachment.                                                                                                                                                                                                                                                                                                                                                                                          |
|                                    | **Example**: Correlating the web-based attack back to the victim username by examining the web proxy log and extracting a potentially malicious email attachment to execute it in a sandbox.                                                                                                                                                                                                                                             |

| Key Investigations                                                                                                                              | Key Techniques                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Traffic Analysis: Using NetFlow data to establish a baseline of normal network behavior and identify anomalies.                                 | Deep Packet Inspection: A method used by firewalls to analyze the data part (payload) of network packets for security purposes.         |
| Authentication Monitoring: Analyzing AAA server logs for patterns of failed and successful authentication attempts to detect potential attacks. | Baseline Establishment: The process of determining normal network behavior to identify deviations that may indicate malicious activity. |
| Proxy Logs Review: Examining web proxy logs for suspicious requests or blocked content to identify potential threats.                           | Content Filtering: The practice of blocking or allowing content based on predefined policies, often implemented in proxy servers.       |
Cause and Effect

|Cause|Effect|
|---|---|
|High volume of failed authentications|May indicate a password attack or unauthorized access attempts.|
|Unusual NetFlow traffic patterns|Could signify data exfiltration or a security breach if traffic exceeds normal baselines.|
|Triggering of IPS alerts|Indicates potential security threats that need to be investigated further.|
|Proxy server blocking requests|Protects the network from accessing malicious sites or content.|
## Event Data Sources

| Component   | Data Type        | Description                                                                       | Example                                                                                                                                                 | Rationale                                                                                                                  |
| ----------- | ---------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| DHCP Server | Transaction Data | Dynamic IP address assignments and attribution to hosts by MAC address.           | If multiple IOCs are detected from different IPs at various times, DHCP logs can confirm if they belong to the same device by checking the MAC address. | This helps in tracking devices that roam across networks, providing insights into potential malicious activities.          |
| DNS Server  | Transaction Data | Logs of DNS queries and responses are critical for identifying malicious domains. | Detection of DGA (Domain Generation Algorithm) domain names often used in malware campaigns.                                                            | Analyzing DNS logs can reveal suspicious activities, such as DNS tunneling, which may indicate data exfiltration attempts. |
| AAA Server  | Alert Data       | Records of successful and failed authentication attempts.                         | A series of failed logins followed by a successful one may indicate a password attack.                                                                  | Monitoring authentication events is essential for identifying unauthorized access and potential breaches.                  |
## Network Traffic Analysis

| Data Source                       | Data Type        | Description                                                                                                          | Example                                                                                                                   | Rationale                                                                                               |
| --------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| NetFlow Data                      | Session Data     | NetFlow records include IP 5-tuples, byte counts, and timestamps, providing a comprehensive view of network traffic. | Unusual traffic patterns, such as excessive data transfers to specific countries, indicating potential data exfiltration. | NetFlow data is crucial for understanding network traffic and identifying potential security incidents. |
| —                                 | Statistical Data | NetFlow can generate reports on top conversations and hosts, helping to establish traffic baselines.                 | N/A                                                                                                                       | Statistical data from NetFlow aids in baseline creation and anomaly detection.                          |
| Intrusion Prevention System (IPS) | Alert Data       | IPS generates alerts based on predefined rules and can capture packets related to triggered alerts.                  | Alerts for spoofed DNS queries or potential malware downloads.                                                            | IPS data is vital for real-time threat detection and response.                                          |
| Firewall Data                     | Session Data     | Firewalls log connection events and NAT translations, providing insights into network traffic.                       | N/A                                                                                                                       | Firewall logs are essential for understanding network connectivity and security events.                 |
| —                                 | Statistical Data | Firewalls can report on top sources and destinations, helping to identify unusual patterns.                          | Unusual traffic patterns, such as excessive data transfers to specific countries.                                         | Statistical data from firewalls aids in anomaly detection and policy enforcement.                       |
| Firewall Data                     | Transaction Data | Proxies log client requests and server responses, which can be analyzed for malicious content.                       | Correlating web proxy logs with user activity to identify compromised accounts or malware delivery methods.               | Proxy logs are crucial for monitoring and controlling web traffic.                                      |
## NetFlow Protocols

Evolution of NetFlow

| Version           | IPv6 Support  | Additional Features                                |
| ----------------- | ------------- | -------------------------------------------------- |
| NetFlow v5        | Lacks support | N/A                                                |
| NetFlow v9, IPFIX | Supported     | Support for usernames, HTTP URLs, and other fields |

### Key Features of NetFlow v5

- IP 5tuple data: src IP, dst IP, src port, dst port, and transport protocol.
- Number of bytes and packets transferred, providing insights into network traffic.
- Despite its limitations, NetFlow v5 remains a foundational tool for network traffic analysis.

### NetFlow Reporting and Analysis

| Topology         | Description                                                    | Example                                                               |
| ---------------- | -------------------------------------------------------------- | --------------------------------------------------------------------- |
| Top reports      | Provide statistical insights into host communication patterns. | Top Conversations                                                     |
| Security threats | Identify suspicious traffic patterns.                          | SYN flood attack from host 10.3.2.202 to server 10.3.1.120 on port 80 |
| Baseline values  | Establish normal network behavior.                             | Aggregated NetFlow data at the collector                              |

| Aspect            | Description                                                                            |
| ----------------- | -------------------------------------------------------------------------------------- |
| Baseline Values   | Provide insights into expected application protocol traffic and data transfer volumes. |
| Variance Analysis | Helps identify anomalies that may indicate security incidents or performance issues.   |
## Proxy Servers

| Proxy Servers                                                                                                                     | Functionality of Proxy Servers                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Proxy servers provide content security by acting as intermediaries between clients and external servers.                          | They require two connections: one from the client to the proxy and another from the proxy to the external server, allowing for request interception. |
| Proxies can deny requests or responses based on configured policies, enhancing security and compliance.                           | Email proxies are often published as the Mail Transfer Agent (MX) record in DNS, directing incoming emails for inspection.                           |
| Email proxies validate the reputation of SMTP sender IP addresses and can quarantine or drop connections from known spam sources. | Proxy servers can log detailed transaction data, including the IP 5-tuple and the number of bytes and packets exchanged.                             |
| Transaction data provides insights into specific client requests, such as URLs accessed and server responses.                     | Example: Using the Open Source Squid web proxy to block access to gambling websites demonstrates practical application of proxy policies.            |
## Identity and Access Management (IAM)

| Feature                      | Description                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------ |
| Audit Trails                 | Comprehensive logging of network access events.                                      |
| User Repositories            | Integration with user directories like AD or LDAP.                                   |
| AAA Services                 | Authentication, Authorization, and Accounting for various access methods.            |
| Differentiated Authorization | Varying privileges based on user context (e.g., device type, connection method).     |
| Device Profiling             | Automatic identification of device types connecting to the network.                  |
| Posture Assessment           | Checks client systems for compliance with security standards before granting access. |
| Non-Compliance Handling      | Quarantining non-compliant devices and limiting access to remediation resources.     |
| Logging                      | Detailed records of user identity, authentication, and authorization events.         |

# Antivirus Solutions

| Feature                | Description                                                         |
| ---------------------- | ------------------------------------------------------------------- |
| Virus Detection        | Detects viruses on file systems, emails, and during downloads.      |
| Malware Protection     | Protects against malware.                                           |
| Proxy Functionality    | Provides visibility into sessions and enables full packet capture.  |
| Alerts                 | Generates alerts when viruses are detected.                         |
| Centralized Management | Allows for centralized log collection and configuration management. |
| Centralized Logging    | Facilitates easier monitoring and analysis of security incidents.   |
| SOC Integration        | Alerts can be sent to a SOC for immediate action.                   |
## Application Logging

| Importance of Application Logs                                                                                             | Use of Syslog for Remote Logging                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Application logs provide transactional and statistical data essential for monitoring application performance and security. | Syslog is a tool that enables remote logging capabilities, allowing logs to be sent to a centralized location for analysis. |
| The Apache web server, for example, uses a common log format to log client addresses and requested resources.              | Centralized application logs are crucial for mission-critical applications, such as e-commerce payment processing systems.  |
| Centralized logging of application data aids SOC analysts in correlating events and obtaining statistics.                  | Collecting logs from various applications helps in identifying trends and potential security threats.                       |

# [[Evidence]]

>Guidelines for digital forensics, including the SP800-86 guideline.

## Process

![9](/Course-Notes/.assets/Pasted_image_20241130132807.png)

1. **Collection**: Identify and acquire data from relevant sources while preserving integrity.
    - Tip: Act quickly to avoid losing dynamic data.
    - Common Pitfall: Failing to label and record data properly.
    
2. **Examination**: Process collected data using forensic tools to extract relevant information.
    - Tip: Use both automated and manual methods for thoroughness.
    - Common Pitfall: Overlooking important data due to improper filtering.
    
3. **Analysis**: Analyze the examined data using legally justifiable methods.
    - Tip: Keep a clear record of methods used for analysis.
    - Common Pitfall: Drawing conclusions without sufficient evidence.
    
4. **Reporting**: Document the findings and recommendations based on the analysis.
    - Tip: Tailor the report's formality to the audience and purpose.
    - Common Pitfall: Failing to include necessary details in the report.

## Evidence Collection

- Evidence must be valid and treated properly to be admissible in court.
- The integrity of the evidence must be preserved throughout the collection and analysis process.
- The context of evidence can change its classification from direct to circumstantial.

| Aspect              | Network Security Analysts                                                | Police Detectives                                                        |
| ------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Role of Evidence    | Reconstruct cyber incidents and breaches.                                | Reconstruct crimes and determine incident nature.                        |
| Evidence Collection | Iterative process, often leading to further inquiries.                   | Iterative process, often leading to further inquiries.                   |
| Evidence Validity   | Proper handling is crucial for admissibility in legal proceedings.       | Proper handling is crucial for admissibility in legal proceedings.       |
| Conclusion Reaching | Based on a confidence level influenced by evidence quality and quantity. | Based on a confidence level influenced by evidence quality and quantity. |
#### Types

| Evidence Type           | Description                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| Direct Evidence         | Evidence that directly supports a conclusion without needing any inference.                                    |
| Circumstantial Evidence | Evidence that requires an inference to connect it to a conclusion.                                             |
| Corroborating Evidence  | Evidence that supports an assertion already backed by other evidence, increasing confidence in the conclusion. |
| Best Evidence           | A legal principle that prefers original documents or firsthand testimony over copies or secondhand accounts.   |

# [[Chain of Custody]]

>  Ensures that no one other than the single named custodian had a chance to access or alter the information.

| Step                       | Description                                                                                                  | Importance                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Understanding              | Thorough understanding of common operating systems, applications, and devices.                               | Essential for identifying relevant files and understanding their significance. |
| Evidence Focus             | Focuses on files left behind, as they can be recorded and analyzed.                                          | Crucial for uncovering evidence and building a case.                           |
| Formal Investigations      | May require maintaining a chain of custody for all evidence.                                                 | Necessary for ensuring the admissibility of evidence in legal proceedings.     |
| Chain of Custody           | Documentation showing the seizure, custody, control, transfer, analysis, and disposition of evidence.        | Essential for maintaining the integrity and validity of evidence.              |
| Legal Significance         | Maintaining a chain of custody is crucial to ensure the evidence’s validity in court.                        | Prevents evidence from being deemed worthless in legal proceedings.            |
| Documentation              | A chain of custody is a document describing the exact time each person took possession of specific evidence. | Provides a clear record of evidence handling, enhancing credibility.           |
| Custodian Role             | Responsible for storing evidence in a secure, access-controlled location.                                    | Ensures that only the custodian could have accessed or altered the evidence.   |
| Evidence Admissibility     | Evidence often is inadmissible in court if the defense can introduce doubt about access control.             | Maintaining a strict chain of custody prevents such doubts.                    |
| Investigator Documentation | Investigators should maintain separate documentation for themselves.                                         | Helps in maintaining a clear and separate record of the investigation process. |
#### Process

| Question                                                                          | Answer                                                                                           |
| --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| What is the evidence?                                                             | A complete bit-by-bit image copy of a hard drive.                                                |
| What method was used to collect the evidence?                                     | Creating a bit-by-bit image copy of the hard drive.                                              |
| When was the evidence collected?                                                  | The first image of a hard drive that investigators take is known as the best evidence.           |
| Who has handled the evidence and why did that person need to handle the evidence? | Investigators need to handle the evidence to create the best evidence and working copy.          |
| Where is the evidence permanently stored?                                         | The chain of custody form should be attached to the best evidence and stored under lock and key. |
# [[Security Data Normalization]]

>The process of manipulating security event data and fitting it into a common schema.

| Data Source      | Details Recorded                                                     | Example Labels                                  |
| ---------------- | -------------------------------------------------------------------- | ----------------------------------------------- |
| Session logs     | IP 5-tuple, packet and byte counts                                   | ==Src_IP==, ==Dst_IP==, SIP, DIP, SP, DP        |
| Transaction logs | User identification, client request, server response, file hash data | UserID, ==Client_IP==, ==Server_IP==, File_Hash |
- Security event monitoring systems must provide parsers that are designed to work with each of the different data sources.
- The parsers algorithmically take the event data and extract the relevant characteristics and fill in the appropriate fields in the common schema.
- Enterprise log search and archive (ELSA) is an example of an event manager.

#### Firewall Log

| Original Syslog Message<br><br> | **Oct 23 10:12:12 myfirewall kernel:FIREWALL:inbound:tcp:192.168.1.100:443:10.0.0.1:80** |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| Normalized Data (Common Schema) | proto:tcp<br>srcip:192.168.1.100<br>srcport:443<br>dstip:10.0.0.1<br>dstport:80          |
![8](/Course-Notes/.assets/Pasted_image_20241130133147.png)

#### Bro Log
- ELSA has parsed an HTTP transaction event produced by Bro.
- The log entry format is different from the firewall connection log message.
- The relevant data is successfully parsed out of the log entry.
- The IP 5-tuple information is parsed into the same fields as the firewall syslog message.

![7](/Course-Notes/.assets/Pasted_image_20241130133204.png)
Fields that are associated with HTTP transactions:
- Method
- Site
- URL
- Referrer    
- User_agent
#### Snort Log

- The Snort alert is in a different format than the earlier examples.
- The data has been extracted and placed into the common schema.
- The IP 5-tuple uses the proto, srcip, srcport, dstip, and dstport fields.

![6](/Course-Notes/.assets/Pasted_image_20241130133232.png)
Fields that are uniquely associated with IPS alert messages:
- sig_sid
- sig_msg
- sig_classification

# [[Event Correlation]]

| Event             | Description                                                 | Action                                               |
| ----------------- | ----------------------------------------------------------- | ---------------------------------------------------- |
| IPS Alert         | An IPS alert is generated with an IP 5-tuple of interest.   | Analyze the alert and identify the IP 5-tuple.       |
| Database Query    | Query the database using the IP 5-tuple from the IPS alert. | Use a normalized database to perform the query.      |
| Report Generation | Generate a report containing correlated data.               | Analyze the report to understand the related events. |
![5](/Course-Notes/.assets/Pasted_image_20241130133556.png)

| Relationship            | Description                                                                         | Example                                                             |
| ----------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| IP 5-tuple Association  | Strong relationship between events sharing the same IP 5-tuple.                     | Multiple email messages sent over a single SMTP connection.         |
| Event Type              | Events may not necessarily be the same.                                             | A single email message can contain multiple suspicious attachments. |
| One-to-One Relationship | Not necessarily a direct correlation between connections, transactions, and alerts. | A single event may trigger multiple alerts.                         |
| Correlated Events       | Provide more detail and context than individual events.                             | Correlated events offer a comprehensive view of an incident.        |
# [[Other Security Data Manipulation]]

|Concept|Description|Key Differences|
|---|---|---|
|Aggregation|Gathering data to gain insights about specific variables.|Focuses on collecting data without summarizing it.|
|Summarization|Producing compact descriptions of key data set qualities.|Provides a summarized view, often in graphical or tabular format.|
|Deduplication|Presenting relevant details from overlapping data in a concise format.|Involves normalizing data and removing redundancy to create a clear report.|
Key Tools/Systems

- **ELSA**: A system used for querying and analyzing security data, allowing for aggregation and summarization of data.
- **Cisco Stealthwatch**: A sophisticated NetFlow analysis system that provides deduplication and correlation of flow records.

| Data Format       | Description                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------ |
| NetFlow Version 5 | Focuses on the IP 5-tuple and basic packet/byte counts, but does not support IPv6.         |
| NetFlow Version 9 | A more robust version that is extensible and supports new data types, replacing version 5. |
| IPFIX             | An open protocol that is also extensible and used for flow data tracking.                  |

## Problem-Solving Steps

To effectively analyze security data using aggregation, summarization, and deduplication, follow these steps:

1. **Identify the Data Source**: Determine where the security data is coming from (e.g., ELSA).
2. **Perform Aggregation**: Use queries to gather data based on common variables (e.g., IP address).
3. **Summarize the Data**: Use summarization techniques (e.g., groupby directive) to create a clear overview of the data.
4. **Deduplicate the Data**: Normalize the data and remove redundant entries to create a concise report.
5. **Analyze the Results**: Review the summarized and deduplicated data to identify patterns or anomalies.

## Aggregation
>`10.10.4.20`

| Aspect                 | Description                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------ |
| Aggregation Definition | A data mining technique that gathers data to gain insights about specific variables. |
| Aggregation Method     | Involves collecting records with a shared variable, such as an IP address.           |
| ELSA Query Example     | Querying ELSA with an IP address returns records sharing that IP.<br>"10.10.4.20"    |
![4](/Course-Notes/.assets/Pasted_image_20241130134123.png)
## Summarization
>`dstip=10.10.4.20 groupby:srcip`

| Technique                 | Description                                                                                                                      | Application                                                                              | ELSA Query Implementation                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Data Summarization        | A data mining technique that generates concise descriptions of key data set qualities, often presented graphically or tabularly. | Useful for analyzing aggregated data, particularly when grouping by specific attributes. | Utilizes the groupby directive to summarize data based on designated attributes. |
![3](/Course-Notes/.assets/Pasted_image_20241130134132.png)
## Deduplication
```
time= Fri Dec 16, 20:12:24, duration=0.042049
proto=TCP, srcip=172.16.1.10, srcport=36205, dstip=10.10.4.20, dstport=25
pkts_in=44, bytes_in=200, pkts_out=85, bytes_out=102452
service=smtp, from=karla <karla@services.public> to=wendy@abc.public, subject=Check it out!
path=10.10.4.20,172.16.1.10,209.165.200.233,209.165.200.235
```

| Step               | Description                                                                                               |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Deduplication Goal | Present relevant details from overlapping data in a concise format.                                       |
| Data Preparation   | Data elements must be normalized before deduplication.                                                    |
| Data Extraction    | Relevant data fields are added to a consolidated report while redundant and irrelevant data are excluded. |
![2](/Course-Notes/.assets/Pasted_image_20241130134139.png)
![1](/Course-Notes/.assets/Pasted_image_20241130134152.png)

| **Field**           | **Value**                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Start Time**      | 09:04:48.323                                                                                                                         |
| **Client Identity** | 10.10.10.10 1000:5a6c:abcd susan                                                                                                     |
| **Client Port**     | 21322                                                                                                                                |
| **Server IP**       | 192.0.2.77                                                                                                                           |
| **Server Port**     | 80                                                                                                                                   |
| **Protocol**        | TCP                                                                                                                                  |
| **Client Bytes**    | 1025                                                                                                                                 |
| **Client Pkts**     | 5                                                                                                                                    |
| **Server Bytes**    | 28712                                                                                                                                |
| **Server Pkts**     | 17                                                                                                                                   |
| **App**             | HTTP                                                                                                                                 |
| **Exporter**        | l2-sw, g1/2, in; l2-sw, g1/24, out; l3-sw, g1/6, in; l3-sw, g4/12, out; rtr, g1/1, in; rtr, g1/4, out; asa, g1/1, in; asa, g1/0, out |
