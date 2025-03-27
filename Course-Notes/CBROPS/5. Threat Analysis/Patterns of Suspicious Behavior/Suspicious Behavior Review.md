 %% #review%%
# [[Network Baselining]]
### About Baselines:

| **Aspect**               | **Description**                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Often Underestimated** | Network baselining is frequently overlooked in network security strategies.                                         |
| **Administrator Focus**  | Network administrators often focus more on security software, logging, and backups, sometimes neglecting baselines. |
| **Baseline Importance**  | Establishing a strong baseline of network traffic behavior is essential for effective network security.             |
### Using Baselines:

| **Aspect**          | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| **Definition**      | A baseline is an activity profile that represents normal system or network behavior, which can be used for future comparisons. |
| **Purpose**         | Baselines help flag anomalies and detect unusual or malicious activities.       |
| **Establishment**   | Creating a baseline requires monitoring and analyzing typical activities like application usage, user access patterns, and network traffic. |

A baseline determines the following:
- Is the network on the green line?
- How fast is network load increasing?
- When will the two will intersect?    
![6](/Course-Notes/.assets/Pasted_image_20241125133031.png)

### Network Load and Baseline Analysis

| **Aspect**               | **Description**                                                                 |
|--------------------------|---------------------------------------------------------------------------------|
| **Network Load**          | The increasing demand on the network as new applications and factors are added, often stressing existing resources. |
| **Baseline Importance**   | - Regularly assessing the current network state helps identify failures and supports informed budget decisions for upgrades. <br> - More effective than analyzing network diagrams and hardware/software lists alone. |
| **Known-Good Profile**    | A known-good profile serves as a reference point for identifying anomalies and understanding normal network behavior. |
| **Baseline Benefits**     | - Enables faster anomaly detection and investigation. <br> - Allows for comparison against expected network operations. <br> - Essential for effective baseline analysis, including monitoring events, transactions, and sessions. |

### Uses of Baselines

| **Aspect**                        | **Description**                                                                 |
|-----------------------------------|---------------------------------------------------------------------------------|
| **Network Baseline**              | Includes NetFlow and passive DNS statistics to identify normal network traffic patterns. |
| **Log Baseline**                  | Represents normal system behavior, such as user logins, system restarts, and alerts. |
| **Application Transaction Baseline** | Provides insights into network protocols and host device communication patterns. |
| **Abnormal Behavior Detection**   | Easier to identify and flag deviations from the standard baseline profile.       |
| **Malicious DNS Traffic Detection** | Unusual URL patterns or potential DNS poisoning threats can be identified and flagged as red flag events. |
| **Anomaly Detection**             | Baseline data helps flag patterns deviating from the norm, enabling quick investigation of potential security incidents. |
![5](/Course-Notes/.assets/Pasted_image_20241125133907.png)
## Core Baseline Process

| **Key Concept**               | **Description**                                                                                       |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| **NMS Tools Limitations**     | NMS tools can assist with network management but often lack flexibility and ease of use.              |
| **Understanding the Process** | Studying the network management process and its workings is helpful, even with the use of tools.      |
| Management Information Base.  | —                                                                                                     |
| **MIB Definition**            | A database containing network management information used by protocols like SNMP or CMIP.             |
| **MIB Object Access**         | MIB object values can be retrieved or changed via SNMP/CMIP commands, typically through a GUI system. |
| **MIB Structure**             | MIB is structured in a tree, containing both public (standard) and private (proprietary) branches.    |
![4](/Course-Notes/.assets/Pasted_image_20241125134122.png)

# [[Identifying Anomalies and Suspicious Behaviors]]

Baselines are crucial for comparison with the current network activity to identify anomalies.

Example

|**Key Point**|**Description**|
|---|---|
|**High profile threat**|Can be detected by analyzing the network traffic they generate.|
|**Embedded threat**|Typically aim to exfiltrate data from the network.|
|**Analysts**|Monitoring network bandwidth and identifying unusual outbound traffic spikes can indicate potential intrusions.|
|**Network Traffic Analysis**|Requires a detailed analysis of traffic types beyond just bandwidth usage.|
|**Baseline Traffic Types**|Includes information about allowed ports, communicating hosts, and used protocols.|
|**Anomaly Detection**|Unusual traffic patterns, like direct internet access over port 80 or external SSH connections, are red flags.|
![3](/Course-Notes/.assets/Pasted_image_20241125134751.png)

| Example                      | **Description**                                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Login**               | Bob Smith typically logs in from 9 am to 5 pm every day.                                                                                                  |
| **Unusual Login Activity**   | On 01/18/2015 and 01/19/2015, Bob Smith logged in at 4 am on a Sunday and Monday, deviating from the usual routine.                                       |
| **Potential Insider Threat** | The unusual login activity, especially from a different location, warrants further investigation to determine if it indicates a potential insider threat. |

| **Category**                       | **Key Point**                                 | **Description**                                                                                       |
|-------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Network Monitoring**              | **Network Baseline**                         | Identifies anomalous behavior like out-of-hours access, even if evidence is removed from log files.     |
|                                     | **Limitations of Auditing**                  | Occasional audits may miss suspicious activity if evidence is cleaned up by threat actors.             |
|                                     | **Value of Monitoring**                      | Essential for detecting security threats and suspicious activities via log event data.                 |
| **Logging & Investigation**         | **Logging Importance**                       | System restarts and application crashes are key for spotting suspicious behavior.                      |
|                                     | **Baseline Comparison**                      | Compare baseline uptime with current behavior to identify potential changes.                           |
|                                     | **Further Investigation**                    | Analyze logs and network traffic for malicious activity if no changes are found.                       |
| **Anomaly Detection**              | **Host Level Detection**                     | Monitor settings like Volume Shadow Copy and scheduled jobs for unusual modifications.                 |
|                                     | **User Level Detection**                     | Observe user commands, especially those modifying services, for unusual activity.                      |
| **Malware Detection**              | **Malware Persistence**                      | Malware (e.g., Metasploit) persists by loading as an unregistered service, undetected without a baseline. |
| **Powershell Monitoring**          | **Powershell’s Power**                       | Powerful CLI with access to .NET APIs and system executables.                                         |
|                                     | **Powershell’s Capabilities**                | Powershell can modify system settings, start processes, and open remote sessions.                      |
|                                     | **Suspicious Activity Detection**           | Monitor Powershell usage for unusual patterns, particularly by users who don’t typically use it.       |
| **User-Detected Malware**          | **Malware Detection by Users**               | Users can detect suspicious activity via strange or inaccessible files and changed settings.           |
|                                     | **Unusual Behavior Timing**                  | Correlate timing of unusual behavior with other suspicious files, processes, or services.              |
| **Suspicious Activity Analysis**   | **Suspicious Activity Analysis**             | Perform deeper analysis once suspicious activity is identified.                                         |
|                                     | **Required Information**                     | Gather date, time, and affected systems for analysis of suspicious activity.                           |
|                                     | **Data Collection**                          | Collect relevant logs, network traffic captures, or suspicious files from affected systems within the identified timeframe. |

# [[PCAP Analysis]]

| **Category**                       | **Key Point**                                 | **Description**                                                                                       |
|-------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **Incident Detection & Investigation** | **Overwhelming Data**                         | Large volumes of data require focusing on logs or baseline flags that indicate specific timeframes for deeper inspection. |
|                                     | **Incident Trigger**                         | Investigation begins when an alert, like an IPS alert, is triggered.                                   |
| **5-Tuple Gathering**              | **Src & Dst IP**                             | Source and destination IPs help identify the source and spread of the issue.                          |
|                                     | **Bro/Netflow Logs**                         | These logs help identify anomalous ports or applications, which can then be correlated with IPs in the pcap. |
|                                     | **Protocol Identification**                  | Protocols are often tied to specific ports; following the tracks may reveal multiple protocols.       |
| **Payload Analysis**               | **5-Tuple for Payload**                      | Use the 5-tuple to obtain the final piece: the payload.                                               |
|                                     | **Plaintext vs Encrypted Payloads**          | Identifying whether the payload is plaintext or encrypted impacts difficulty in analysis.             |
|                                     | **Exploit Type**                             | Exploits may appear as shell code in memory or files written to disk, and must be identified.         |
|                                     | **Incident Detection**                       | Identifying the payload and exploit type is essential for detecting security incidents.               |

### **Packet Filtering Techniques**

| **Goal**                           | The goal is to obtain the most relevant dataset possible for analysis.           |
| ---------------------------------- | -------------------------------------------------------------------------------- |
| **Filtering by 5-Tuple + Payload** | Filter packet capture results by 5-tuple and payloads to focus on relevant data. |
![2](/Course-Notes/.assets/Pasted_image_20241125153423.png)
### **Regular Expression Syntax**

| **Inefficient Search Operators**   | Using multiple "==" operators or chaining with "or" is inefficient. Use REGEX with "matches" for conciseness.                       |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **REGEX Example for IP Matching**  | Example: `ip.src_host matches "192\.168\.1\.10[1-9]"` to match IP addresses from 192.168.1.101 to 192.168.1.109.                    |
| **Special Character Handling**     | Use a backslash ("\") to escape special characters, like the period (".").                                                          |
| **Character Class**                | Brackets are used to define a character class, e.g., `[1-9]` matches any digit from 1 to 9.                                         |
| **Compatibility**                  | ==Snort & Wireshark== use REGEX for signatures to identify patterns in network traffic.                                             |
| **REGEX Cheatsheets & References** | Resources include PCRE Regular Expression Cheatsheet, PCRE Syntax Reference, and PCRE man pages.                                    |
### Example Syntax 
#### **Character Class for Lists**

To match IP addresses ==range== from 192.168.1.101 to 192.168.1.109, use a REGEX pattern instead of typing each IP address individually.

`ip.src_host matches “192\.168\.1\.10[1-9]”

Brackets are used to denote a character class, representing any digit from 1 to 9.

Character classes are also useful for creating ==lists==. If the servers in this network are 192.168.1.120, 192.168.1.140, and 192.168.1.160, they could all be found with:

`ip.src_host matches “192\.168\.1\.1[246]0”`
### Learning resources 

Many references and examples exist through the following resources:
- PCRE Regular Expression Cheatsheet—Debuggex
- PCRE Regular Expression Pattern Syntax Reference (PHP preg*)
- PCRE man pages

# [[Delivery]]

| **Category**                         | **Key Point**                   | **Description**                                                                                                      |
| ------------------------------------ | ------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| **File Behavior Analysis**           | **The Last Step**               | File behavior analysis is often the final step in the investigation.                                                 |
|                                      | **File Origins**                | Suspicious files may originate directly from the anomaly or be created/modified during the event timeframe.          |
|                                      | **Triaging Files**              | Extracted and related files should be quickly triaged to determine if they are malicious.                            |
|                                      | **Suspicious Files**            | File analysis begins by identifying suspicious files, often executables or libraries loaded into existing processes. |
|                                      | **Malware Behavior**            | Behavior varies based on malware type; related files can affect malware execution.                                   |
| **Malware Execution & Exfiltration** | **Malware Execution Mechanism** | Some malware executes child processes, while others are "droppers" that download and run additional files.           |
|                                      | **Malware Data Exfiltration**   | Malware may transfer stolen data (e.g., credentials or banking info) to a suspicious server or site.                 |
|                                      | **Malware File Behavior**       | Malware files can be temporary or persistent, often residing in temporary directories.                               |
| **File Behavioral Analysis**         | **File Behavioral Analysis**    | Files are analyzed in a controlled environment to determine their behavior and potential threat.                     |
|                                      | **Sandbox Functionality**       | Sandboxes isolate files in a safe environment to monitor and analyze their behavior.                                 |
|                                      | **Malwr.com Sandbox**           | Malwr.com provides a platform for uploading files for automated analysis and potential signing based on behavior.    |
![1](/Course-Notes/.assets/Pasted_image_20241125180453.png)
#### **Malware Detection**

| Uses hashes to compare submitted samples with known malware.              |
| ------------------------------------------------------------------------- |
| Samples are run through a sandbox for analysis if no hash match is found. |
| Provides a comprehensive report with detailed results of the analysis.    |

| **Category**            | **Key Point**               | **Description**                                                                                   |
| ----------------------- | --------------------------- | ------------------------------------------------------------------------------------------------- |
| **Malware Information** | **Malware Information**     | Includes filename, size, hash, and antivirus signatures for identification.                       |
|                         | **Antivirus Analysis**      | Analysts reference antivirus signatures for vendor-specific analysis.                             |
|                         | **Future Identification**   | Enables unique identification of malware samples for future detection.                            |
| **Malware Behavior**    | **Malware Behavior Report** | Documents popups generated by malware and IP addresses/domains it attempts to contact.            |
|                         | **Anomaly Detection**       | Cross-reference behavior reports with previous PCAP analysis for anomaly detection.               |
|                         | **Investigation Clues**     | Provides clues such as associated files, registry keys, and mutexes linked to the malware sample. |

Look for Answers:
- Where did the malware come from?
- What was the method and point of entry?
- Where has it been and what systems were affected?
- What did the threat do and what is it doing now?
- How is the threat stopped and root cause eliminated?


