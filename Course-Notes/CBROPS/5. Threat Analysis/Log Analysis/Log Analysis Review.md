%% #review %%
# [[Security Data Analysis]]

- ==SOC’s Main Task==: Monitor and implement detection and response capabilities.
- Data collected and analyzed by a SOC determines its ability to detect attacks.
- Many functions depend on the accuracy of data for security operations.

| Task           | Description                                                     |
| -------------- | --------------------------------------------------------------- |
| Monitoring     | Continuously observe IT environments for suspicious activities. |
| Detection      | Identify potential security incidents using monitoring data.    |
| Response       | Implement measures to mitigate detected security incidents.     |
| Investigation  | Analyze security incidents to determine the cause and impact.   |
| Threat Hunting | Proactively search for potential threats and vulnerabilities.   |
| Forensics      | Gather and analyze evidence related to security incidents.      |
| Auditing       | Assess compliance with security policies and regulations.       |
![17](/Course-Notes/.assets/Pasted_image_20241126110249.png)
![16](/Course-Notes/.assets/Pasted_image_20241126122706.png)

| Log Data Type               | Description                                                                | Importance                                                                          |
| --------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Device logs                 | Record activities and changes at the device level.                         | Provides insights into resource consumption, equipment operation, and user actions. |
| Connection/transaction data | Includes aggregated bidirectional communication and connection statistics. | Captures traffic patterns and connection details.                                   |
| Flow data                   | Provides aggregated information about streams of packets.                  | Offers insights into traffic volume, direction, and duration.                       |
| Packet captures             | Captures data at network interfaces or traffic aggregation points.         | Provides the highest level of detail for in-depth analysis.                         |

| Category                            | Description                                                                                                                               |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Abnormal data patterns (signatures) | Identifying unusual patterns or sequences in log data that may indicate potential security incidents.                                     |
| Behavioral patterns                 | Analyzing log data to understand the typical behavior of users, systems, or applications, and identifying deviations from these patterns. |
| Traffic patterns                    | Examining log data related to network traffic to detect unusual activities, such as large data transfers or suspicious connections.       |
## Overview
Device logs vary in type, complexity, capabilities, and placement.

![15](/Course-Notes/.assets/Pasted_image_20241126124503.png)![14](/Course-Notes/.assets/Pasted_image_20241126152951.png)

| Logging Capabilities                                           | Logging Configuration                                                                                     | Logging Parameters                                                | Devices log                                                                 | Log formats                                                     | Log entries                | Devices                                                                                                               | Log delivery                                                                                  | Log Variation by Device Type                                                                       | Log Variation by Vendor                                                                  | Log Variation by Log Type                                                                                         |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Depend on device configurations and software logging features. | Determines logging behavior and can specify parameters like enabling, disabling, and configuring logging. | Can be configured by administrators or coded within the software. | basic system information, security-related details, and application events. | JSON, Common Event Format, Windows Event Log, and W3C standard. | can be simple or detailed. | store logs locally for short periods with predefined storage sizes, then transfer long-term data to external devices. | protocols include syslog, secure syslog, SNMP, NetFlow, API calls, emails, and chat messages. | Different devices (e.g., host firewall, network firewall) generate logs with distinct information. | Even for devices of the same type, log content can differ significantly between vendors. | Different types of logs on the same device (e.g., login attempts, PowerShell activities) exhibit varying content. |
### Logging Components
![13](/Course-Notes/.assets/Pasted_image_20241126153459.png)

| Component                            | Description                                                                         |
| ------------------------------------ | ----------------------------------------------------------------------------------- |
| Log source, log generator, or sensor | Devices that generate and store event logs locally or remotely.                     |
| Logging agent                        | Software that collects, filters, and forwards logs to remote log collectors.        |
| Time server                          | Ensures clock synchronization across devices.                                       |
| Log collector                        | Processes and stores logs from multiple log generators.                             |
| Telemetry broker                     | Collects telemetry data from multiple sources and distributes it to consumers.      |
| Log processor                        | Receives and processes logs from log collectors.                                    |
| Storage system                       | Stores raw and processed logs.                                                      |
| Log management console               | Provides log information to administrators or analysts for monitoring and analysis. |
| SIEM solution                        | Typically includes log collection, processing, management, and internal storage.    |
## Log Storage Overview

Organizations often employ multiple log storage methods

==Strategy==: Recent event logs might be stored on high-performance storage for quick access, while old event logs might be archived on slower, more cost-effective storage.

Log Storage considerations: 
- The log retention ==time==, 
- The log ==processing== actions,
- The average size of the logs

>Significantly impacts storage space requirements.

# [[Log Collection]]

1. SOC can only defend what they see,
2. What they see is limited to what they log.
3. Good logging can be be cost-prohibitive and complex.
4. Balance resources, efficiency, and ability to detect attacks.

	- Log sources 
	- Formats
	- Delivery mechanisms
	- Log management platform centralization

These answers help define auditing policy and determine:
- ==Which sources== provide the most relevant data, 
- Which ==types of information== to collect from each source, 
- and The ==level of detail== to be included in the log.

![12](/Course-Notes/.assets/Pasted_image_20241127113705.png)

To answer these questions, a SOC relies on:

|**Category**|**Description**|**Key Points**|
|---|---|---|
|**SOC Knowledge**|Information related to attack detection, threat investigations, hunting, incident response, and threat intelligence.|Defines data required for attack detection and focuses on useful sources and data for specific environments and use cases.|
|**Tactical Threat Intelligence**|Provides information on necessary data to detect attacks, including IOCs and IOAs.|Includes signatures, analytics, and indicators of compromise (IOCs) and indicators of attack (IOAs). Data should be collected containing IOCs and IOAs for analysis.|
|**IOCs (Indicators of Compromise)**|Reactive, trace-based indicators that suggest an attack has occurred, often artifacts left behind by threat actors or malicious code.|- Reactive in nature - Suggest an attack has already occurred - Traces/artifacts left behind on systems, indicating a breach or compromise.|
|**IOAs (Indicators of Attack)**|Proactive, behavioral indicators focused on detecting an ongoing attack.|- Proactive in nature - Focus on detecting an attack as it occurs - Behavioral, indicating an attack is happening or about to occur.|
|**Compliance Requirements**|Regulations that mandate data to be logged and how long it should be retained.|- Dictates logging requirements - Specifies data retention policies for compliance.|
|**Security Community Sources**|External frameworks (e.g., MITRE ATT&CK) and sources that provide knowledge about adversary tactics and techniques.|- MITRE ATT&CK framework summarizes adversary tactics and techniques. - Helps identify relevant data sources for attack detection. - Provides guidance for data collection.|
![11](/Course-Notes/.assets/Pasted_image_20241127114610.png)

Data Types:
- ==Adversary Detection==: Collecting data about command execution can detect the most adversary techniques.
- ==Adversary Techniques==: The figure shows the common data types and the number of adversary techniques associated with each data type. [Source](https://github.com/mitre-attack/attack-datasources)
## Log Sources
![10](/Course-Notes/.assets/Pasted_image_20241127114815.png)
### **Network-based logs**

|**Category**|**Description**|**Key Points**|
|---|---|---|
|**Significance**|Provides visibility into network activities, vital for detecting and understanding attacks.|- Key for attack detection and network behavior analysis.|
|**Advantage**|Easier to monitor compared to endpoint logs.|- Simplifies monitoring across multiple endpoints.|
|**Content**|Includes events from multiple endpoints, offering insights into network behavior.|- Provides a network-wide view of traffic and interactions.|
|**Information**|Basic data on IPs, ports, flows, connections, and protocols.|- Includes traffic info like IP addresses, ports, and protocols.|
|**Capabilities**|Detects and alerts on suspicious network activity.|- Logs alerts triggered by potentially malicious network activity.|
|**Value**|Crucial for SOC analysts in real-time monitoring and incident investigation.|- Essential for identifying and investigating network-based threats.|
|**Sources**|Collected from routers, switches, firewalls, and network service devices.|- Includes network infrastructure devices (routers, firewalls, etc.).|
|**Network Service Devices**|Devices that provide network services and capture traffic data.|- Include IAM, DNS, and DHCP servers.|
### **Endpoint Logs**

|**Category**|**Description**|**Key Points**|
|---|---|---|
|**Functionality**|Provides detailed data on endpoint events such as file actions, autorun services, logged-in users, and commands.|- Includes file details, user logins, executed commands, and autorun services.|
|**Endpoint Security**|Endpoint logs can be analyzed by anti-malware or EDR tools to detect and alert on malicious activities.|- Anti-malware/EDR tools help detect malicious behavior and generate alerts.|
|**Value**|Essential for SOC analysts in threat detection and incident response.|- Valuable for real-time detection and investigation of endpoint-related threats.|
|**Log Creation Process**|Logs are created locally on the endpoint and delivered via a logging agent for remote analysis.|1. Logs created locally. 2. Delivered by logging agent. 3. Processed and analyzed remotely.|
### **Agentless logging**

|**Category**|**Description**|**Key Points**|
|---|---|---|
|**Functionality**|Delivers local logs to a remote destination using the operating system’s native logging capabilities.|- Uses OS logging features for remote log delivery.|
|**Advantage**|Simplifies setup by eliminating the need for additional software agents.|- Reduces complexity and agent overhead.|
|**Disadvantage**|Potential security risks if the OS lacks secure log transport mechanisms.|- Security concerns if log transport is not encrypted or secure.|
### **Agent-based logging**

|**Category**|**Description**|**Key Points**|
|---|---|---|
|**Benefits**|Offers log processing, filtering, and secure log transport.|- Provides secure and efficient log forwarding and processing.|
|**Example**|Splunk Universal Forwarder, a lightweight agent for log collection and forwarding.|- Splunk Universal Forwarder monitors logs and sends them to a central collector.|
|**Forwarder Functionality**|Monitors endpoint features and securely forwards logs to a collector for indexing and analysis.|- Collects and sends logs over a secure channel for indexing and consolidation in a central platform (e.g., Splunk).|
## Log Formats

| Format Type | Owned By    | Encoding Type   |
| ----------- | ----------- | --------------- |
| SYSLOG      | IETF        | Key-Value Pairs |
| CEF         | HP/ArcSight | Key-Value Pairs |
| LEEF        | IBM/QRadar  | Key-Value Pairs |
| CEE         | MITRE       | JSON/XML        |
| IDMEF       | IETF        | XML             |
#### Syslog log
**==Header==:** 
- Priority
- Version of the syslog protocol specification
- Timestamp
- Logging hostname
- Application
- Process name or process ID
- and Message ID

 ==**Message==:** Contains descriptive text about the event in a free text format.

``` syslog
<165>1 2003-10-11T22:14:15.003Z mymachine.example.com
evntslog - ID47 [exampleSDID@32473 iut="3" eventSource=
"Application" eventID="1011"] BOMAn application
event log entry...
```

The header contains the following information:
- ==Priority==: 165
- ==Version==: 1
- ==Timestamp==: 11 October 2003 at 22:14:15 UTC, 3 milliseconds into the next second
- ==Z== letter at the end of the timestamp indicates UTC
- ==Log source==: host with the domain name “mymachine.example.com”
- ==Application==: “evntslog”
 Process name and process ID are unknown
- Message ID: “ID47”
- Structured-data:
- Value: “[exampleSDID@32473 iut=“3” eventSource=“Application” eventID=“1011”]”
- Message: “An application event log entry…”
- BOM at the beginning of the message indicates UTF-8 encoding.
#### CEF
- CEF is a proprietary log format developed by ArcSight.
- It is used in ArcSight’s SIEM platform.
- CEF defines many attributes (or keys) that describe an event.
- The set includes standard (predefined) and customizable keys.
Examples of standard keys are:
- Source and destination IP addresses
- Filename
- File path
- Username
- URL
- Source and destination ports.
==Other CEF Keys==: 
- **==rt==:** log receipt timestamp
- **==dhost==:** the domain name of the destination endpoint
- ==**duser==:** the name of the destination user
- **==fname==:** the file name
- **==cs1Label==:** a text descriptor that specifies the type of the information in the cs1 key
- **==cs1==:** custom information about the event (in this example, the name of the malware)
- **==act==:** short text about the event action

The base CEF format is:
```CEF-Format
_CEF:Version|Device Vendor|Device Product|Device Version|Signature ID|Name|Severity|Extension_
```

Example 
```CEF-Example
CEF:0|Trend Micro|Control Manager|7.0|100|malware successfully
stopped|10|src=192.168.1.1 rt=Mar 28 2022 09:31:00 GMT+00:00 dhost=Client-03
duser=Admin fname=update.exe cs1Label=Malware Name cs1=LockBit2 act=blocked
```
#### **JSON**
- ==Format==: Hierarchical, human-readable, and widely supported.
- ==Object Structure==: A collection of keys and their values, allowing for custom key names.
- ==Log Processing==: Requires more processing for efficient search due to potential inconsistency in key names.
![9](/Course-Notes/.assets/Pasted_image_20241127131239.png)
#### **Log Event Enhanced Format (LEEF)**
- ==Proprietary== format to exchange logs in IBM QRadar SIEM.
- Focused on ==network== security events.
- LEEF has a smaller number of keys (==attributes==) compared to CEF.
#### **Common Event Expression (CEE)**
- ==Purpose==: Standardize log format for all computing systems.
- ==Development==: Developed by MITRE Corporation in collaboration with U.S. governmental entities and some SIEM vendors.
- ==Encoding==: Encoded based on Common Log Syntax (CLS) encodings, using XML and JSON.
#### **Intrusion Detection Message Exchange Format (IDMEF)**
- ==Purpose==: Defines data formats and exchange procedures for sharing information between intrusion detection and response systems and management systems.
- ==Standardization==: Created by the IETF but not published as a standard, limiting its adoption.
- ==Message Exchange==: Uses XML-based messages exchanged via the Intrusion Detection Exchange Protocol (IDXP).
#### **Key-Value Pairs (KVPs)**

- ==Key-Value Pairs== (KVPs): Data blocks in log formats with key and value components separated by a predefined character.
- ==Key==: Identifies a block of data and is often positioned on the left side of the colon (:).
	- Must be a string
- ==Value==: Represents the actual data being represented.
	-  Value: Can be a string, number, Boolean, array, or object.
![8](/Course-Notes/.assets/Pasted_image_20241127132120.png)

- Log Entry Structure: The log entry consists of a timestamp followed by seven Key-Value Pairs (KVPs).
- KVP Information Breakdown: Each row in the table represents one KVP from the log entry, providing details about the device and its state.
- Importance of Key Interpretation: Understanding the meaning of keys in different log formats is crucial for SOC analysts to interpret log information accurately.

## Log Examples

==Cisco Secure Firewall Threat Defense device.==
```
Apr 14 2019 12:52:31 firepower %FTD-6-430002: AccessControlRuleAction: ==Block with reset, SrcIP: 192.168.170.155, DstIP: 209.165.200.22==, SrcPort: 49905, ==DstPort: 443==, Protocol: tcp, IngressInterface: Inside_1, EgressInterface: Outside_1, ==IngressZone: Inside, EgressZone: Outside==, ACPolicy: FWPolicy_1, ==AccessControlRuleName: Blocked Countries Outbound==, Prefilter Policy: Prefilter, User: Unknown, Client: SSL client, ApplicationProtocol: HTTPS, WebApplication: Office 365, InitiatorPackets: 3, ResponderPackets: 1, InitiatorBytes: 459, ResponderBytes: 78, NAPPolicy: Unknown, URL: [https://nexus.randomapps.live.com](https://nexus.randomapps.live.com/)
```
- Content: IP address, firewall zones and interfaces, protocol and application information, connection reset information.
- Trigger: Access control rule named “Blocked Countries Outbound” based on geolocation information.

==Windows Log Entry 4672: Created by Active Directory==
```
Special privileges assigned to new logon.
Subject:
        Security ID:  WIN-DC1\IamWho
        Account Name:  IamWho
        Account Domain:  WIN-DC1
        Logon ID:  0x2b241
Privileges:
        SeSecurityPrivilege
        SeTakeOwnershipPrivilege
        SeLoadDriverPrivilege
        SeBackupPrivilege
        SeRestorePrivilege
        SeDebugPrivilege
        SeSystemEnvironmentPrivilege
        SeImpersonatePrivilege
```

- Trgger: sensitive “administrator equivalent” privileges are assigned to a logged-on user.
- Users with these privileges may be able to bypass other security controls on the machine.
- Linux Logging: Similar to other operating systems, Linux systems generate and store information in log files for security and troubleshooting purposes.

```
Aug 12 10:04:01 linuxhost ==sudo:    john== : TTY=pts/0 ; PWD=/var/log ; USER=root ; ==COMMAND=/usr/bin/su==

Aug 12 10:04:01 linuxhost sudo: pam_unix(sudo:session): ==session opened for user root(uid=0) by (uid=1000)==

Aug 12 10:04:01 linuxhost ==su: (to root) root== on pts/1

Aug 12 10:04:01 linuxhost su: pam_unix(su:session): ==session opened for user root(uid=0) by johm(uid=0)==
```

- Event Description: User “john” used the “su” command to gain super user privileges.
- Event Source: The event is logged in the auth.log file located in the /var/log directory.
- User Information: The user who escalated privileges is “john”.
## Log Centralization
![7](/Course-Notes/.assets/Pasted_image_20241127141317.png)

| Topic                | Description                                                                             |
| -------------------- | --------------------------------------------------------------------------------------- |
| Volume-based Pricing | Licensing cost is based on the storage size of events ingested per month, week, or day. |
| Device-based Pricing | Licensing cost is based on the number of devices sending events to the SIEM.            |

![6](/Course-Notes/.assets/Pasted_image_20241127141351.png)

| **Strategy**                   | **Description**                                                                                                  |
|---------------------------------|------------------------------------------------------------------------------------------------------------------|
| **Log Centralization Strategy** | SOCs utilize both centralized and local log collections, with only the most informative security events logged centrally. |
| **Centralized Log Analysis**    | SOC analysts start threat investigations by analyzing centralized logs, which can guide them to relevant local logs for further details. |
| **SIEM Platform Implementation**| SIEM platforms can be deployed on-premises or in the cloud and are not the sole log centralization points in a network. |
## Log Delivery Methods
**Log Transfer Definition**: Transferring logs from one location to another, typically between log sources and management platforms, and between management platforms and long-term storage.

| **Category**                   | **Details**                                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Log Transfer Methods**       | Two basic methods exist for transferring logs:                                                                                                                    |
| - **Push**                     | A log collector always listens for data that a log source sends, e.g., using syslog or NetFlow.                                                                   |
| - **Pull**                     | A log collector periodically requests data from a log source, e.g., using an API request. Most common for obtaining logs from databases and cloud infrastructure. |
| **Hybrid Subscription Method** | A variant of the pull method with push characteristics.                                                                                                           |

| **Category**                   | **Details**                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------- |
| **Log Collection Process**     | The log collector pulls logs from the source and subscribes to receive new logs. |
| **Log Transmission**           | The log source pushes new logs to the log collector.                             |
| **Log Delivery Process Terms** | Log shipping, log fetching, and log retrieval.                                   |

| **Category**                    | **Details**                                                         |
| ------------------------------- | ------------------------------------------------------------------- |
| **Push Method Drawbacks**       | Log transmission failure, erroneous data, or source failure.        |
| **Pull Method Drawbacks**       | Unreachable log source connection.                                  |
| **Log Collector Functionality** | Should detect unreachable issues and trigger appropriate responses. |
![5](/Course-Notes/.assets/Pasted_image_20241127141558.png)

| **Log Transfer Method**           | **Description**                                                                                                                                                       |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Syslog (RFCs 3164, 5424, 5426)** | The industry protocol standard, syslog is widely available, fast, and easy to parse, making it ideal for log retrieval. Push-based delivery ensures timely log access, though message size limitations (2048 bytes) exist. UDP (port 514) is the common transport protocol, lacking delivery guarantees and potentially dropping logs or failing remote systems. Despite these drawbacks, UDP offers faster delivery and lower bandwidth. |
| **Secure Syslog (RFC 5425)**      | Secure syslog messages are encrypted over TCP port 514 for a secure connection.                                                                                       |
| **SNMP (RFCs 1213, 1216, 1218)**   | SNMP provides push and pull delivery methods. SNMPv3 is the most secure, offering access control, authentication, and encryption. It enables secure data gathering from devices, including reboot events potentially indicative of malicious activity. SNMP requires device administrator enablement on many systems. |
| **Remote File Monitoring**        | This method retrieves log files from a shared directory at the log source using an external system. It’s suitable for log source systems that lack local log management or logging agent support. |
| **API-based log retrieval**       | Enables machine-to-machine communication but requires compatibility between the log collector and log source. It allows selective log authentication and gathering, avoiding redundant log fetching. However, it consumes more resources and has a limited query volume, making it unsuitable for high-volume log sources. RESTful API, a common API, supports XML and JSON encoding and uses HTTP/HTTPS requests for data retrieval, modification, posting, and deletion. |
## Log Collection Concerns

| **Topic**                         | **Description**                                                                                                                                                                |
|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Log Collection Importance**     | Essential for log analysis and ensuring desired information is gathered.                                                                                                      |
| **SOC Responsibility**            | Address concerns and implement log collection effectively.                                                                                                                   |
| **Log Security**                  | Involves securing log transport and access to information. Use transport mechanisms like TLS with authentication, encryption, and integrity checks for reliable delivery. Logs often contain sensitive user, business, or system information, so special attention is required for handling and protection. Information in log files can provide attackers with valuable insights or expose sensitive data. [Reference Common Weakness Enumeration CWS-532](https://cwe.mitre.org/data/definitions/532.html) |
| **Log Retention**                 | May be required by compliance frameworks or SOC operations.                                                                                                                  |
| **Continuous Adjustments & Improvements** | Depend on gathered threat intelligence and threat investigation outputs. These inputs may require SOC changes, such as including or excluding log sources or modifying log source configurations. |
| **Centralized Log Configuration Management** | Enables quick **responsiveness** to security events.                                                                                                                           |
# [[Log Analysis Methods and Outcomes]]

| Method Type             | Description                                                                                                  | Downsides                                                                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Statistical Methods     | Create normal behavior profiles to detect anomalies by comparing current data against established baselines. | - Requires accurate baseline profiles,<br>- Frequent recalculation due to user habit changes and software updates, and accurate deviation threshold determination.                                 |
| Knowledge-based Methods | Analyze logged events against known attack information to identify potential security incidents.             | - Requires Prior knowledge of attacks, including attack signatures and indicators.<br>- Cannot detect unknown attacks and effectiveness relies on accurate known attack signatures and indicators. |
| Advanced Methods        | Utilize machine learning algorithms to derive detection logic and adapt to new conditions automatically.     | - Requires continuous retraining for new attacks and are resource-intensive.                                                                                                                       |

| **Platform/System**  | **Description**                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------|
| **SIEM Platforms**    | Tools for collecting and analyzing security data, capable of alerting on suspicious behaviors.       |
| **SOAR Platforms**    | Security Orchestration, Automation and Response tools that automate security operations.             |
| **XDR Systems**       | Extended Detection and Response systems that provide integrated security across multiple layers.     |
| **EDR Systems**       | Endpoint Detection and Response systems focused on monitoring and responding to threats on endpoints. |
#### Times
Time Syncs
- ==NTP== is used to sync time across devices.
Time Stamps
- ==ISO== 8601 format: YYYY-MM-DDTHH:MM:SS 
- ==Epoch== time starts from January 1, 1970, UTC 00:00:00.

![4](/Course-Notes/.assets/Pasted_image_20241127155346.png)

Problems 
- ==32-bit Epoch== integers overflow after January 19, 2038, requiring 64-bit integers.
- Time Zones: Including the time zone in timestamps is crucial to avoid misinterpretation.

UTC
- Recommended for device time configuration, across all time zones or with a time offset.
- Time Offset: Allows for easy conversion of timestamps to UTC “-03:00” offset to UTC.

#### Key Processes in Log Analysis

| Process                    | Description                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| Log Parsing                | Breaking down log messages into individual data components for easier analysis. (Sentence -> Word) |
| Log Filtering              | Selecting relevant logs for analysis and discarding irrelevant entries to reduce noise.            |
| Log Normalization          | Mapping varying log formats to a common structure for consistency in analysis.                     |
| Log Indexing               | Organizing log entries based on attributes to facilitate quick searches and retrieval.             |
| Log Correlation (Analysis) | Discovering relationships between log entries to identify common events or incidents.              |
## Log Preprocessing
#### Log **parsing**
- Structured log formats like syslog and CEF are easier to parse because it is clearly defined.
- Tools like ==Elasticsearch==, which is part of the ==ELK Stack==, include log parser functions.
- Elasticsearch is a search/analytics tool for various data, both structured and unstructured.
#### Log filtering 
- Removes irrelevant logs and reduce “noise
- Improves the quality of log data for analysis.
- Some log sources cannot filter log entries at the source.
#### Log Normalization 
- Represents all logs consistently by using a common schema and data formats.
- Maps varying labels to a predefined, common structure and unifies data value formats.
- Allows for consistent representation of logs regardless of their original format.

Data Block Normalization
![3](/Course-Notes/.assets/Pasted_image_20241127160228.png)
- Mapping vendor-specific data block descriptors to standardized normalized descriptors.
- “FileName” and “FilePath” are examples of normalized data block descriptors.
- “file” data block descriptor can refer to either file name or file path depending on the vendor.

#### Log **Categorization**
| **Topic**               | **Description**                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **Log Categorization**   | Assigning logs to categories based on common characteristics, such as source device type or security feature, to facilitate searching and filtering. |
| **Log Preprocessing**    | Logging agents preprocess logs before sending them to the log collector.                                                            |
| **Compatibility Requirement** | Logging agents and log management platforms must be compatible.                                                                  |
## Log Indexing

>Logically arranging log entries based on their attributes

![2](/Course-Notes/.assets/Pasted_image_20241127173105.png)
## Log Correlation

> Relationships between log entries to reveal the same security event
> Provides a broader view of an event by combining information from multiple log sources.

EG: IP address, port, hostname, asset tag, and so on.
A shared artifact in log entries that represents the same event.

Manual correlation involves visual examination of logs, 
Automated correlation utilizes search query strings and log management platforms like SIEMs.

SQL syntax requires:
- characteristics of the data (attributes that data must exhibit)
- where to look for the data (which log sources to include)
- what to do with the data (retrieve, sort, delete, insert, update)

## Log enrichment

> Supplementing raw log data with context to provide a broader view of security events.
> Sources: Geolocation databases, network services servers, and threat intelligence platforms.

![1](/Course-Notes/.assets/Pasted_image_20241128112618.png)
##### Cisco ISE Integration: 
Provides contextual information, such as:
Operating system, patch level, and antivirus solution status.

| **Cisco ISE**        | **Description**                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Device Profiling** | Cisco ISE identifies the type of device connected to the network and assigns it to the appropriate VLAN based on its profile.                                            |
| **Posturing**        | ISE checks the device's OS update levels, antivirus, and firewall software status. Devices that are not compliant may be quarantined until they meet security standards. |
| **Purpose of ISE**   | To ensure network security and compliance by managing device access and configuration.                                                                                   |

| **More Data Sources**                      | **Description**                                                                                                                                    |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **External Data Source Lookup Automation** | SIEM, XDR, or SOAR platforms can automate the process of looking up external data sources to enrich logs with additional context or information.   |
| **Integration Methods**                    | These platforms integrate with external data sources via **APIs**, allowing them to pull data from other systems automatically.                    |
| **External Data Source Types**             | External data sources can include **on-premises systems** (e.g., asset inventory) or **cloud-based services** (e.g., VirusTotal for malware data). |
# [[Log Attacks and Log Management Challenges]]

## Log Poisoning

>An adversary injects malicious code into a log file by triggering error conditions.
- ==Attack Vector==: Adversary injects malicious code in form inputs or HTTP request headers. (LFI)
- ==Impact==: Malicious code is logged and can potentially be executed.
- ==Target Log==: apache.log, auth.log, vsftpd.log, and ssh.log.
- ==Requirement==: The system must be susceptible to LFI attacks for log poisoning to be effective.
	#### EG: Log4j
	- ==Vulnerability== (2021) logging utility vulnerability that allowed malicious code exec.
	- ==Method==: Allowing remote shell over LDAP.
## Log Tampering

>Manipulating log files and entries to conceal evidence of hacking activities.

Sanitization practices:
• Disabling logging on all accessed systems
• Deleting recorded data
• Modifying logs with fake data
• Erasing logs of historical commands used by attackers
## Challenges in Log Management

| Challenge Type             | Description                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Log Generation and Storage | Issues with managing log sources, ==inconsistent content==, timestamps, and formats across devices.          |
| Log Protection             | Protecting ==sensitive information== in logs from unauthorized access through encryption and access control. |
| Log Analysis               | Challenges faced by SOC analysts due to ==overwhelming== tasks, lack of training, and inadequate tools.      |
