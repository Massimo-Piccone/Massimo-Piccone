- Log Collection Activities: Describes activities and components involved in log collection.
- Log Collection Components: Covers log sources, formats, delivery mechanisms, and log management platform centralization.
- SOC Analyst Awareness: Briefly covers log collection concerns.
## SOC Data Collection Function

1. SOC can only defend what they see,
2. What they see is limited to what they log.
3. Good logging can be be cost-prohibitive and complex.
4. Balance resources, efficiency, and ability to detect attacks.

SOC must determine the following:
- Which information should be collected?
- Which level of detail should be included in the log?
- Which sources have information to be collected?
- Where should the logs be stored?
- Which log sources are most important?

These answers help define auditing policy and determine:
- Sources provide the most relevant data, 
- Which types of information to collect from each source, 
- and The level of detail to be included in the log.

![10](/Course-Notes/.assets/Pasted_image_20241127113705.png)

To answer these questions, a SOC relies on:

- **==SOC knowledge==** of attack and detection techniques, threat investigations, threat hunting, incident response, and threat intelligence define required data for attack detection. The SOC may monitor specific environments for specific use cases, selecting only useful sources and data.
    
- **==Tactical threat intelligence==** provides information on required data to detect attacks. It includes signatures and analytics (indicators of compromise [IOCs] and indicators of attack [IOAs]) pertaining to threats. The SOC should collect data containing IOCs and IOAs for analysis.
	- ==IOCs are reactive==, driven by the assumption that an attack has occurred. They are traces or artifacts left behind by a threat actor or malicious code on a system tied to a specific threat, indicating a breach or compromise.
	- ==IOAs are more proactive==, focusing on detecting what a threat actor is trying to accomplish. They are behavioral, driven by the assumption that “it looks like an attack is occurring.”

- ==**Compliance requirements**== mandate which data should be logged and for how long.
    
- **==Security community sources==** like the MITRE Corporation’s Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK) framework provide knowledge about common adversary tactics and techniques based on real-world observations. MITRE also summarizes relevant data sources for detection, aiding in data collection decisions.

![9](/Course-Notes/.assets/Pasted_image_20241127114610.png)

Data Types:
- ==Adversary Detection==: Collecting data about command execution can detect the most adversary techniques.
- ==Adversary Techniques==: The figure shows the common data types and the number of adversary techniques associated with each data type. [Source](https://github.com/mitre-attack/attack-datasources)

## Log Sources

Log sources create records of events (log entries) stored in log files. They can be user laptops, Linux workstations, or network devices like firewalls or routers.

![8](/Course-Notes/.assets/Pasted_image_20241127114815.png)

**Network-based logs**
- ==Significance==: Provide visibility into network activities, crucial for detecting and understanding attacks.
- ==Advantage==: Simplify monitoring and analysis compared to collecting logs from individual endpoints.
- ==Content==: Contain events related to multiple endpoints, offering insights into network behavior.

- ==Information==: Provide basic traffic information, including IP addresses, ports, flows, connections, and communication protocols.
- ==Capabilities==: Detect and alert on potentially malicious network activities, providing logs about triggered alerts.
- ==Value==: Great use to the SOC analyst.

- ==Sources==: Intermediary devices like routers, switches, and firewalls, and devices hosting network services.
- ==Network Service Devices==: Provide network service and have information about the entire network.
- ==Network Service Examples==: Identity and access management (IAM), DNS, and DHCP servers.

**Endpoint logs**
- ==Functionality==: Provide detailed information about endpoint events, including file details, autorun services, logged-in users, and executed commands.
- ==Endpoint Security==: Endpoints can have anti-malware or EDR capabilities to analyze events, detect malicious activity, and generate alerts.
- ==Value==: Endpoint logs and alerts are valuable to SOC analysts for threat detection and incident response.

1. Logs are created locally.
2. Logging agent used to delivers logs 
3. Remote log platform processes and analyzes.

**Agentless logging**
- ==Functionality==: Delivery of local logs to a remote destination using native operating system logging capabilities.
- ==Advantage==: Reduces complexity by not requiring additional software agents.
- ==Disadvantage==: May impose security issues if the operating system lacks secure log transport.

**Agent-based logging**
- ==Benefits==: Provides log processing, filtering, and secure transport of logs.
- ==Example==: Splunk Universal Forwarder, a lightweight agent that monitors and forwards logs to a collector.
- ==Forwarder Functionality==: Monitors endpoint features, forwards logs over a secure channel to Splunk for indexing and consolidation.

**Log Collection**
- ==Importance==: Collecting logs from endpoints is becoming more important due to the increasing use of secure protocols that encrypt traffic.
- ==Challenges==: Adversaries may disable logging and detection capabilities on endpoints, making network logs the only source of visibility.
- ==Modern SOC Approach==: A modern SOC typically collects both network and endpoint logs to provide the most visibility with minimal overhead.

![7](/Course-Notes/.assets/Pasted_image_20241127115945.png)

**Breakdown:**
- ==Malicious Access Attempt==: A malicious adversary attempted to remotely log into a host using RDP from a known malicious IP address.
- ==Malicious File Transfer==: The adversary sent a malicious file to another host using HTTPS, which was blocked by the endpoint’s advanced malware protection.
- ==Security Controls==: RDP connection could have been blocked by properly configuring security controls, and TLS decryption by the firewall would have improved inspection capability.

**Logging configuration:**
1. Logging Activity is the result of the logging configuration.
2. Logging configuration specifies which records are relevant and which can be filtered out.

The logging configuration determines:
- Which logging features are enabled.
- Where / how to store / send logs.
- The level of log detail.

Configured in the management console of source.

- ==Windows systems== -> Group Policy Editor to configure logged events in Windows Event Log.
- ==Cisco Secure Firewall Threat Defense== -> Specify which AC policy rules to log.(FireManCent to make AC policy rules.)

 ==Centralized Logging Management== Enables quick adjustment of logging configurations in case of incidents.

![6](/Course-Notes/.assets/Pasted_image_20241127121425.png)

Group Policy Management editor.
- ==Auditing Policy Configuration==: Allows fine-grained control over which events are logged and in which scenarios.
- ==Logging Events==: Enables logging for both successful and failed process creation.

## Log Formats
- Determines the structure and separation of log information.
- Provides meaningful text descriptors instead of numeric values for effective reconstruction of events.
- Makes logs easier to read and process by humans and machines.

- Format and delivery protocols are separate.
- ==Format== Specifies the structure and content of logs.
- ==Delivery== Carries logs with a specific log format across the network.

Log formatting influences the log processing performance. 
Fixed log structure allows for fast, automated log processing.

Log formats that are common in security events logging:

|Format Type|Owned By|Encoding Type|
|---|---|---|
|SYSLOG|IETF|Key-Value Pairs|
|CEF|HP/ArcSight|Key-Value Pairs|
|LEEF|IBM/QRadar|Key-Value Pairs|
|CEE|MITRE|JSON/XML|
|IDMEF|IETF|XML|

Common in logging implementations:

#### Syslog log
The oldest, uses UDP port 514 as the transport protocol. The syslog format defines the following components:

**==Header==:** 
- Priority
- Version of the syslog protocol specification
- Timestamp
- Logging hostname
- Application
- Process name or process ID
- and Message ID

The priority is calculated from the facility, a value that represents the feature or the component on the device that creates the log, and the severity value, which represents the criticality of an event.

- ==**Structured data==:** Expresses information about the event. The format includes individual data blocks within square brackets.

- ==**Message==:** Contains descriptive text about the event in a free text format.

``` syslog
<165>1 2003-10-11T22:14:15.003Z mymachine.example.com
evntslog - ID47 [exampleSDID@32473 iut="3" eventSource=
"Application" eventID="1011"] BOMAn application
event log entry...
```

The header contains the following information:
- Priority: 165
- Version: 1
- Timestamp: 11 October 2003 at 22:14:15 UTC, 3 milliseconds into the next second
- Z letter at the end of the timestamp indicates UTC
- Log source: host with the domain name “mymachine.example.com”
- Application: “evntslog”
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

The base CEF format is:

```CEF-Format
_CEF:Version|Device Vendor|Device Product|Device Version|Signature ID|Name|Severity|Extension_
```

- The example log is in the base CEF format.
- It includes the CEF version (version 0), the device vendor (Trend Micro), the product name and version (Control Manager version 7.0), the signature ID (100), the event name and severity (malware successfully stopped, severity 10), and additional information in the extension element.

```CEF-Example
CEF:0|Trend Micro|Control Manager|7.0|100|malware successfully
stopped|10|src=192.168.1.1 rt=Mar 28 2022 09:31:00 GMT+00:00 dhost=Client-03
duser=Admin fname=update.exe cs1Label=Malware Name cs1=LockBit2 act=blocked
```

- ==CEF Format Extension==: The extension element in CEF format includes the key “src” to specify the source IPv4 address.
- ==Source IP Address==: The value of the “src” key is “192.168.1.1”.

 ==Other CEF Keys==: 
- **==rt==:** log receipt timestamp
- **==dhost==:** the domain name of the destination endpoint
- ==**duser==:** the name of the destination user
- **==fname==:** the file name
- **==cs1Label==:** a text descriptor that specifies the type of the information in the cs1 key
- **==cs1==:** custom information about the event (in this example, the name of the malware)
- **==act==:** short text about the event action

#### **JSON**

- ==Format==: Hierarchical, human-readable, and widely supported.
- ==Object Structure==: A collection of keys and their values, allowing for custom key names.
- ==Log Processing==: Requires more processing for efficient search due to potential inconsistency in key names.

Cisco Secure Endpoint login event log in JSON format.
![5](/Course-Notes/.assets/Pasted_image_20241127131239.png)

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

![4](/Course-Notes/.assets/Pasted_image_20241127132120.png)

- Log Entry Structure: The log entry consists of a timestamp followed by seven Key-Value Pairs (KVPs).
- KVP Information Breakdown: Each row in the table represents one KVP from the log entry, providing details about the device and its state.
- Importance of Key Interpretation: Understanding the meaning of keys in different log formats is crucial for SOC analysts to interpret log information accurately.

## Log Examples

- Log Content Variability: Logs from different devices and systems vary in content and format.
- Log Interpretation: SOC analysts need to understand the content and format of logs to interpret them effectively.
- Log Examples: Firewall logs include IP address, port, and protocol information, while endpoint logs may include failed login details.

```
Apr 14 2019 12:52:31 firepower %FTD-6-430002: AccessControlRuleAction: ==Block with reset, SrcIP: 192.168.170.155, DstIP: 209.165.200.22==, SrcPort: 49905, ==DstPort: 443==, Protocol: tcp, IngressInterface: Inside_1, EgressInterface: Outside_1, ==IngressZone: Inside, EgressZone: Outside==, ACPolicy: FWPolicy_1, ==AccessControlRuleName: Blocked Countries Outbound==, Prefilter Policy: Prefilter, User: Unknown, Client: SSL client, ApplicationProtocol: HTTPS, WebApplication: Office 365, InitiatorPackets: 3, ResponderPackets: 1, InitiatorBytes: 459, ResponderBytes: 78, NAPPolicy: Unknown, URL: [https://nexus.randomapps.live.com](https://nexus.randomapps.live.com/)
```

- Log Source: Cisco Secure Firewall Threat Defense device.
- Log Content: IP address, firewall zones and interfaces, protocol and application information, connection reset information.
- Log Trigger: Access control rule named “Blocked Countries Outbound” based on geolocation information.

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

- Windows Log Entry 4672: Created by Active Directory when sensitive “administrator equivalent” privileges are assigned to a logged-on user.
- Impact of Privileges: Users with these privileges may be able to bypass other security controls on the machine.
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

- Goal: To make all logs available at a single location for easier analysis.
- Centralization Point: Typically a centralized log management platform or SIEM platform in SOCs.
- SIEM Platform Functionality: Provides full visibility into the monitored environment for log analysis, threat hunting, and forensic analysis.

![3](/Course-Notes/.assets/Pasted_image_20241127141317.png)

- Centralized Collection Challenges: Requires significant financial, processing, and storage resources.
- Licensing Costs: Many SIEM solutions use a subscription model based on events per second, which can be expensive for high-traffic networks.

Note

- Pricing Models: SIEM vendors use event-based, volume-based, and device-based pricing models.
- Volume-based Pricing: Licensing cost is based on the storage size of events ingested per month, week, or day.
- Device-based Pricing: Licensing cost is based on the number of devices sending events to the SIEM.

![2](/Course-Notes/.assets/Pasted_image_20241127141351.png)

- Log Centralization Strategy: SOCs utilize both centralized and local log collections, with only the most informative security events logged centrally.
- Centralized Log Analysis: SOC analysts start threat investigations by analyzing centralized logs, which can guide them to relevant local logs for further details.
- SIEM Platform Implementation: SIEM platforms can be deployed on-premises or in the cloud and are not the sole log centralization points in a network.

## Log Delivery Methods

- Log Transfer Definition: Transferring logs from one location to another, typically between log sources and management platforms, and between management platforms and long-term storage.
- Log Transfer Methods: Two basic methods exist for transferring logs.
- Long-Term Storage Options: Can be appliance-based or cloud-based.

	- **Push:** A log collector always listens for data that a log source sends, for example, using syslog or NetFlow.
	- **Pull:** A log collector periodically requests data from a log source, for example using an API request. Pulling data is the most common option for obtaining logs from databases and cloud infrastructure.

- Hybrid Subscription Method: A variant of the pull method with push characteristics.
- Log Collection Process: The log collector pulls logs from the source and subscribes to receive new logs.
- Log Transmission: The log source pushes new logs to the log collector.

- Log Delivery Process Terms: Log shipping, log fetching, and log retrieval.

- Push Method Drawbacks: Log transmission failure, erroneous data, or source failure.
- Pull Method Drawbacks: Unreachable log source connection.
- Log Collector Functionality: Should detect unreachable issues and trigger appropriate responses.

![1](/Course-Notes/.assets/Pasted_image_20241127141558.png)

- Delivery Methods: Protocols that handle reliability, compression, and confidentiality in log communication.
- Protocol Examples: Common protocols for log retrieval include HTTP, HTTPS, and TCP.
- Protocol Function: Protocols ensure reliable and secure communication between log sources and collectors.

- ==Syslog (RFCs 3164, 5424, 5426)==: The industry protocol standard, syslog is widely available, fast, and easy to parse, making it ideal for log retrieval. Push-based delivery ensures timely log access, though message size limitations (2048 bytes) exist. UDP (port 514) is the common transport protocol, lacking delivery guarantees and potentially dropping logs or failing remote systems. Despite these drawbacks, UDP offers faster delivery and lower bandwidth.
- ==Secure Syslog (RFC 5425)==: Secure syslog messages are encrypted over TCP port 514 for a secure connection.
- ==SNMP (RFCs 1213, 1216, 1218)==: SNMP provides push and pull delivery methods. SNMPv3 is the most secure, offering access control, authentication, and encryption. It enables secure data gathering from devices, including reboot events potentially indicative of malicious activity. SNMP requires device administrator enablement on many systems.
- ==Remote File Monitoring==: This method retrieves log files from a shared directory at the log source using an external system. It’s suitable for log source systems that lack local log management or logging agent support.
- ==API-based log retrieval== enables machine-to-machine communication but requires compatibility between the log collector and log source. It allows selective log authentication and gathering, avoiding redundant log fetching. However, it consumes more resources and has a limited query volume, making it unsuitable for high-volume log sources. RESTful API, a common API, supports XML and JSON encoding and uses HTTP/HTTPS requests for data retrieval, modification, posting, and deletion.

## Log Collection Concerns

- Log Collection Importance: Essential for log analysis and ensuring desired information is gathered.
- SOC Responsibility: Address concerns and implement log collection effectively.

- ==Log security== involves securing log transport and access to information. Use transport mechanisms like TLS with authentication, encryption, and integrity checks for reliable delivery. Logs often contain sensitive user, business, or system information, so special attention is required for handling and protection. Information in log files can provide attackers with valuable insights or expose sensitive data. [Reference Common Weakness Enumeration CWS-532:](https://cwe.mitre.org/data/definitions/532.html)
- ==Log retention== may be required by compliance frameworks or SOC operations.
- ==Continuous adjustments and improvements== depend on gathered threat intelligence and threat investigation outputs. These inputs may require SOC changes, such as including or excluding log sources or modifying log source configurations.
- Centralized log configuration management enables quick ==responsiveness== to security events.

