## Overview of Data Analysis

- ==SOC’s Main Task==: Monitor IT environments and implement and maintain detection and response capabilities.
- ==Data Importance==: Data collected and analyzed by a SOC determines its ability to detect attacks.
- ==Data Sources==: Machine-generated data and contextual information that impact an organization’s security posture.

- ==Detection==: Monitoring alerts and applying data analytics to create new detection rules, if needed, to detect the new threats.
- ==Investigation==: Searching, correlating, and enriching available data to verify if the activity is malicious.
- ==Incident response==: Analyzing the data to identify attacks and determine their timelines and scope or extent.
- ==Threat hunting==: Proactively analyzing the data instead of reacting to alerts, to identify intrusion attempts, misconfigured devices, and to uncover other signs of malicious activity.
- ==Forensics==: Using forensic methods to analyze the data and gather evidence of malicious activity.
- ==Auditing==: Proving compliance with regulatory requirements.

![6](/Course-Notes/.assets/Pasted_image_20241126110249.png)

- ==Data Analysis and Investigation==: SOC uses data analysis methods for investigations and creating detection rules.
- ==Detection Rules==: Highly sensitive alerts are created to understand the logic behind them.

- ==SOC Analysts’ Role==: Triage and investigate alerts, using data analysis for alert verification.
- ==Incident Response==: Incident response teams use data analysis to determine the scope of incidents and carry out remediation and containment measures.
- ==Data Importance==: Many SOC functions depend on the availability and accuracy of data for effective security operations.

![5](/Course-Notes/.assets/Pasted_image_20241126122706.png)

- ==Goal==: To perform efficient security events analysis.
- ==Focus==: Security-relevant information from the most relevant sources.
- ==Quality==: Relevance, type, and immediacy of the information influence the efficacy of subsequent SOC processes.

	- ==Device logs== record activities and changes at the device level, including resource consumption statistics, equipment operation events, and user actions linked to applications.
	- ==Connection/transaction== data includes aggregated bidirectional communication, traffic between IP addresses, and connection statistics like packet counts, duration, and protocol.
	- ==Flow data== provides aggregated information about streams of packets with common attributes, such as source and destination IP addresses and ports. It includes statistics like flow count, duration, direction, and size.
	- ==Packet captures== offer the highest level of detail, capturing data at network interfaces or traffic aggregation points. On high-speed networks, capturing large amounts of data requires ample storage space.

Common ==data sources== include:
	- Routers and switches
	- Firewalls, intrusion detection systems (IDSs), and intrusion prevention systems (IPSs)
	- Servers
	- Network services such as Active Directory, Dynamic Host Configuration Protocol (DHCP), and Domain Name System (DNS)
	- End-user devices

==Log analysis== is extracting the relevant, meaningful information from log data, interpreting the log data to determine what has been happening in the monitored environment.
- Abnormal data patterns (signatures), 
- Behavioral patterns, 
- and Traffic patterns.

Be familiar with the logging processes, log components, and log content so you can develop techniques for quick and efficient searching.

## Logging Overview

- IT environments contain devices that vary in type, complexity, capabilities, and placement.
- Many activities happen every second, 
  Most devices record them.
- Logging is the process that creates and maintains these records.

Log entries contain information such as time, a short description, and the severity of the activity.

![4](/Course-Notes/.assets/Pasted_image_20241126124503.png)

An event can trigger multiple events 
Logs are kept on device but can be configured to be sent to a remote destination server. (SysLog)

![3](/Course-Notes/.assets/Pasted_image_20241126152951.png)

- The device registers an activity.
- The device creates a log entry.
- The device saves the log entry locally in a log file.
- The device sends the log entry to a remote syslog server (optional).

- ==Logging Capabilities==: Depend on device configurations and software logging features.
- ==Logging Configuration==: Determines logging behavior and can specify parameters like enabling, disabling, and configuring logging.
- ==Logging Parameters==: Can be configured by administrators or coded within the software.

- ==Devices log== basic system information, security-related details, and application events.
- ==Log formats== include JSON, Common Event Format, Windows Event Log, and W3C standard.
- ==Log entries== can be simple or detailed.
- ==Devices== store logs locally for short periods with predefined storage sizes, then transfer long-term data to external devices.
- ==Log delivery== protocols include syslog, secure syslog, SNMP, NetFlow, API calls, emails, and chat messages.

- ==Log Variation by Device Type==: Different devices (e.g., host firewall, network firewall) generate logs with distinct information.
- ==Log Variation by Vendor==: Even for devices of the same type, log content can differ significantly between vendors.
- ==Log Variation by Log Type==: Different types of logs on the same device (e.g., login attempts, PowerShell activities) exhibit varying content.

## Logging Components

- ==Logging Design==: Depends on the size and complexity of the environment.
- ==Simple Logging==: A single device generates and stores logs locally.
- ==Complex Logging==: Multiple components collect, store, and provide access to log information for analysis.

![2](/Course-Notes/.assets/Pasted_image_20241126153459.png)

An organization can have multiple components in its log management implementation, including:

- ==Log source, log generator, or sensor==: These systems and devices generate and store event logs locally or remotely. Each device can have multiple features enabled, each logging information about its associated events.
- ==Logging agent==: Specialized software that runs on a device, collecting, filtering, and forwarding logs to remote log collectors. Examples include Cisco Secure Endpoints Connector with Cisco Orbital and Wazuh agent. Native logging agents exist on different operating systems.
- ==Time server==: Ensures clock synchronization across devices in the monitored environment.
- ==Log collector==: Processes and stores logs from multiple log generators. In SOCs, this is typically implemented in SIEM solutions.
- ==Telemetry broker==: Collects telemetry data from multiple sources and distributes it to consumers. It adjusts telemetry format to suit the destination’s needs. For instance, it converts Azure network security group (NSG) flow logs into IP Flow Information Export (IPFIX) format and forwards them to a secure cloud analytics system. Cisco Telemetry Broker is an advanced version of Cisco Secure Network Analytics (formerly Cisco Stealthwatch Enterprise) UDP Director.
- ==Log processor==: Receives and processes logs from log collectors. This involves parsing, normalization, indexing, and correlation. Log processors are often collocated with log collectors.
- ==Storage system==: Stores raw and processed logs. The size and type depend on log information, read access frequency, and retention period.
- ==Log management console==: Provides log information to administrators or analysts for monitoring and analysis. It includes ticketing and reporting features. SIEM platforms have their own management consoles.
- A ==SIEM solution== typically includes log collection, processing, management, and internal storage.

- ==Log sensors== -> log network devices 
- ==Log agents== -> log endpoints.

- ==Telemetry Definition==: Automated collection of data and measurements from a source.
- ==Telemetry Data Examples==: Routing protocol neighborship state, interface status, and traffic statistics.
- ==Telemetry Process==: Data collection at periodic intervals and forwarding to an analysis system.

## Log Storage Overview

- ==Location==: Event logs can be stored on the device that generated them or consolidated in a central log management solution.
- ==Consideration==: Consideration should be given to how and how often event logs will be accessed.
- ==Strategy==: Recent event logs might be stored on high-performance storage for quick access, while old event logs might be archived on slower, more cost-effective storage.

Examples of the requirements that impact log storage include:
- The amount and type of log data that must be stored
- The log retention period
- The frequency at which the log data is accessed

![1](/Course-Notes/.assets/Pasted_image_20241126182611.png)

HIPAA requires that logs be retained for six years, but there is no limit for investigations.

Log Storage considerations: 
- The log retention ==time==, 
- The log ==processing== actions,
- The average size of the logs 
>Significantly impacts storage space requirements.

Organizations often employ multiple log storage methods.
- ==Centralized Log Management==: Relevant logs are sent to a centralized solution for alerting and analysis.
- ==Supporting Logs==: Other supporting logs are kept locally at the log source for potential future use.
- ==File compression== is often used to reduce the size of log files.
- Logs may need to be accessed remotely, in which case a cloud storage is recommended for short- or long-term log storage.

