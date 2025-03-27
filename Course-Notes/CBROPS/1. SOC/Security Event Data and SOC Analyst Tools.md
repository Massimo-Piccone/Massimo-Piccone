# SOC Relevant Data and Security Event Data Introduction

When responding to an incident, the SOC analyst must perform an analysis based on event data types. For instance, the event data type that is used to display only the source and destination elements of a session differs from the event data type that represents a full account of all the data exchanged between two devices on the network.

![8](/Course-Notes/.assets/Screenshot_2024-11-08_at_22.28.38.png)


## Network Security Monitoring Data Types

Because no single data type offers a complete solution, the SOC analyst must conduct the investigation by analyzing several types of event data:

- Session data
- Full packet capture
- Transaction data
- Extracted data
- Statistical data
- Alert data
- External data
## Session Data or "flow data"

>A summarized conversation between two endpoint devices on the network.

A detective might analyze a phone bill in an investigative process. The phone bill does not capture any information that was exchanged during a phone call. However, knowing who called whom at what time and for how long can be useful during an investigation.

Session data documents all the individual network sessions, based on the session's 5-tuple: 
- Transport protocol,
- Source and destination IP address, 
- Source and destination port.

## Full Packet Capture

>A full account of all the data exchanged between devices

The header contains metadata, such as the packet’s source and destination IP address. The payload contains all the data exchanged.

Large storage requirements. Tedious to analyze. 
Usually, an analysis that is performed with higher-level data types is required for effectively guiding the analyst to relevant portions of full packet capture data. 

## Transaction Data

>Highlights operations that occur as a result of network sessions and system activities. 

Each log file contains transaction data. Note that there is not a one-to-one relationship between session data and transaction data. An individual network session might not produce any transactions or might be associated with several transactions. Transactions can also document local activities on a system that do not involve network communications.

## Extracted Content

>Artifacts that are mined from network traffic are considered extracted content.

Artifacts that may be extracted include the following: 

- **Sessions:** Session data about all network connections, including the standard IP 5-tuple, time stamp of the session start, and frame number within the PCAP where the session starts.
    
- **DNS:** Transaction data documenting all DNS requests and replies.
    
- **Hosts:** All IP addresses that are seen in the PCAP along with other relevant information that can be gleaned from the PCAP. Potential information includes DNS hostnames, open TCP ports, operating system, sessions that are associated with the host, and total packet and byte counts that are associated with the host.

## Statistical Data

>Statistical data aggregates other security monitoring data types. Statistical data is used to baseline network traffic activity. 

NetFlow session data documents each individual connection to a web server. A graph can be produced using NetFlow session data that shows the average number of connections per minute to the web server over a period of a month, The graph is considered statistical data that can be used to formulate a monthly report identifying baseline network traffic activity to and from the web server. Baseline data queries document the aggregate normal network traffic patterns and their trends. Comparing actual traffic patterns to the baseline patterns can reveal anomalous behavior. Two common statistical data queries are baseline graphs and top reports.

Top reports can answer questions such as the following:
- Which hosts request the most HTTP data?
- Which hosts serve the most HTTP data?
- Which DNS domains are the most requested?

## Alert Data

>Alert data is generally produced by an IDS or IPS system. 

Alert data is generated when network traffic or some other type of data matches a set of rules that are configured in a tool.

Despite being the most formed data type, alert data is not necessarily the most accurate or most relevant data type. False positives and false negatives are potential issues with alert data. SOC analysts are the primary recipients of this type of data and must analyze it to judge its disposition. 

## External Data

>Threat intelligence feeds.

 Threat actors are constantly making improvements to their malware to avoid detection. Therefore, the SOC must make constant improvements to the threat detection systems, including creating and refining rules and signatures or adding new detection capabilities.
 Indicators of compromise (IoCs) and artifacts 

# SOC Tools and Their Features

A SOC relies on a supporting infrastructure of tools and systems that provide the following services:

- Network mapping
- Network monitoring
- Vulnerability detection
- Penetration testing
- Data collection
- Threat and anomaly detection
- Data aggregation and correlation

## Security Onion

Linux distro intended to support SOC analysts with a suite of tools for network security monitoring, including intrusion detection, network security monitoring, and log management to to provide four core network security-monitoring functions:
- Full packet capture
- Network-based and host-based intrusion detection sensors
- Security analysis tools
- Log management

### **Enterprise Log Search and Archive** (ELSA) 
version of Security Onion is composed of the following tools:

- **ELSA searchEngine:** ELSA is a centralized syslog framework that is built on Syslog-NG, MySQL, and Sphinx full-text search. It provides a fully asynchronous web-based query interface that normalizes logs and makes searching billions of them for arbitrary strings as easy as searching the web. It also includes tools for assigning permissions for viewing the logs, email-based alerts, scheduled queries, and graphing.

- **Snort NIDS:** An open source, rules-driven network intrusion detection system (NIDS) and network intrusion prevention system (NIPS) developed by Cisco (Sourcefire). It performs real-time threat detection and generates alerts when threats are detected. The NIPS inline mode is not supported within Security Onion.

![7](/Course-Notes/.assets/Screenshot_2024-11-08_at_23.15.02.png)

- **Suricata NIPS:** A script-driven NIDS and NIPS threat detection engine for analyzing traffic and generating alerts. NIPS _inline_ mode is not supported within Security Onion.

- **Zeek traffic analyzer (Bro):** A packet recorder and protocol parsing engine that is commonly used to analyze network traffic to detect behavioral anomalies.

   1. **Traffic logging:** Traffic captured by means of SPAN, a TAP port, or a packet broker. Traffic logging generates comprehensive, protocol-specific traffic logs for more than 35 network protocols and application layer analyzers, including HTTP, DNS FTP, and SMTP.   
   2. **Automated analysis:** Traffic analysis that uses Bro scripts.
   3. **File extraction:** Extracts and reassembles various file types directly off the wire.

- **Wazuh HIDS (OSSEC):** Host-based intrusion detection system (HIDS) that replaced OSSEC and is used to monitor and defend Security Onion. Wazuh offers a lightweight monitoring agent that can be installed on network host devices and is supported on Windows, Linux, Mac OS X, HP-UX, AIX, and Solaris platforms.

- **Netsniff-ng:** Captures network traffic via SPAN, a TAP port, or packet broker in the form of PCAP files.

- **Sysmon monitor:** Windows system service to monitor event log and system activity.
   
- **Syslog-ng BSD log daemon:** An enhanced BSD log daemon that can receive logs and collect inputs from a wide range of sources.

**Network analyst tools:** Provide packet capture and network traffic IP flow analytics capabilities that can be used to find anomalous network activity. The following popular network analyst tools are included within Security Onion:

- **Wireshark:** Network protocol analyzer

- **Sguil:** Sguil is built by network security analysts for network security analysts. Sguil's main component is an intuitive GUI that provides access to real-time events, session data, and raw packet captures. Sguil facilitates the practice of Network Security Monitoring and event driven analysis.

- **Squert:** Squert is a web application that is used to query and view event data that is stored in a Sguil database (typically IDS alert data). Squert is a visual tool that attempts to provide additional context to events by using metadata, time series representations and weighted and logically grouped result sets.

- **NetworkMiner:** Performs network traffic analysis for parsing PCAP files and extracting artifacts

- **CyberChef:** Web-based application for data manipulation

- **CapME:** Helps with analyzing PCAP transcripts and downloading captured PCAP files

### **Elastic Stack** (ELK) 
A newer Security Onion version. It includes the following tools:

- **Elasticsearch:** Ingest and index logs, large scalable search engine based on Apache Lucene

- **Logstash:** Data ingestion engine, parsing, and format logs
   
- **Kibana:** Web dashboard that offers visualizations of ingested log data and data exploration. (Kibana and Squert can pivot to CapMe to retrieve full packet captures.)

- **TheHIVE:** Security incident response platform and case management system integrated with Malware Information Sharing Platform (MISP)
   
- **Elastic Beats:** Lightweight data shipper server agent that sends specific types of operational data to Logstash and Elasticsearch

- **Curator:** Manage indices through scheduled maintenance

- **ElastAlert:** Query Elasticsearch and alert on user-defined anomalous behavior or other interesting bits of information
   
- **FreqServer:** Detect DGAs and find random filenames, script names, process names, service names, workstation names, TLS certificate and issuer subjects, and so on.

- **DomainStats:** Conducts `whois` lookups and provides info about a domain by providing additional context, such as creation time, age, reputation.

The following figure shows the relationship between the Security Onion 2 Elastic Stack components.
![6](/Course-Notes/.assets/Screenshot_2024-11-08_at_23.23.35.png)

**Cisco Secure Network Analytics (formerly Stealthwatch):** 
Displays the IP flows across network devices that are configured to send NetFlow data to Cisco Secure Network Analytics. Cisco Secure Network Analytics uses NetFlow, IPFIX, and other types of network telemetry data to detect a wide range of threats such as advanced persistent threats (APT)s, distributed denial of service (DDoS) attacks, zero-day malware, and insider threats. Cisco Secure Network Analytics applies various behavior and policy-based algorithms to alarm SOC analysts about suspicious behavior on the network.

![5](/Course-Notes/.assets/Screenshot_2024-11-09_at_11.05.18.png)

**Cisco Secure Malware Analytics (formerly Threat Grid):** 
A cloud-based malware analysis and threat intelligence sandbox solution. A SOC analyst can submit malware samples for analysis during an investigation. 
- Static and dynamic analysis engines to dissect file behaviors.
- Search and correlate data elements of a single malware against the database. 
Samples collected and sourced from around the world providing a global view of malware attacks and its association. Cisco Secure Malware Analytics is included as an integrated component of many Cisco Secure products.

![4](/Course-Notes/.assets/Screenshot_2024-11-09_at_11.07.28.png)

**Cisco SecureX platform:** 
- Integrated security portfolio with the organization's entire security infrastructure. 
- Consistent experience that unifies visibility and identifies unknown threats. 
- Enables automated workflows to strengthen security across the network, endpoint, cloud, and applications. 
Cisco SecureX is an open, cloud-native platform that is included with many Cisco Secure products. It provides a comprehensive user experience, aligns with products from more than 175 security technology providers, and offers more than 300 product-to-product integrations.

![3](/Course-Notes/.assets/Screenshot_2024-11-09_at_11.10.20.png)

**Penetration testing tools:** 
- Simulates the actions of an attacker who aims to breach the information security.
- Vulnerability assessment is the process that looks for known vulnerabilities.
Most organizations usually start with a vulnerability assessment, and act on its results to either eliminate those weaknesses or reduce them to an acceptable level of risk, and then perform a penetration test if they are confident in their improved security posture. 

![2](/Course-Notes/.assets/Screenshot_2024-11-09_at_11.15.53.png)

## Security Information and Event Management

>Collect and correlate logs to events that indicate malicious or suspicious actions.

SIEM systems help SOC analysts by collecting all relevant security data into one place, correlating the data, alerting SOC analysts about anomalies, and enriching the data. Without SIEM systems, a security operations team would not be able to monitor hundreds, thousands, or millions of assets. A SIEM automates the collection, indexing, and alerting of data that is critical to SOC operations. 

- Excellent for ingesting, processing, and storing large volumes of data, 
- Not so good at interpreted in the context of the network environment. 

While some response actions can and should be automated, humans still need to interpret, analyze, and decide how a specific set of events impacts the environment.

Splunk Enterprise is a popular commercial SIEM product that offers several features including search, indexing, alters, pivot, reports, and data modeling.

Splunk Enterprise, with artificial intelligence and machine-learning capabilities, helps SOC analysts uncover the actionable insights from all the data, regardless of the format.

The Splunk Enterprise environment can be customized to fit the specific needs of the organization by the use of apps. An app is a collection of configurations, knowledge objects, views, and dashboards that run on the Splunk platform. Certain Cisco products support certain Splunk apps.

![1](/Course-Notes/.assets/Screenshot_2024-11-09_at_11.16.14.png)

# [[Quick Reference]]

Key Tools and Features

| Tool Name             | Description                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Security Onion**    | A suite of tools for network security monitoring, including intrusion detection and log management.          |
| **Snort**             | An open-source network intrusion detection and prevention system that generates alerts for detected threats. |
| **Suricata**          | A script-driven threat detection engine for analyzing network traffic and generating alerts.                 |
| **Wireshark**         | A network protocol analyzer used for capturing and analyzing network traffic.                                |
| **Splunk Enterprise** | A commercial SIEM product that provides search, indexing, and alerting capabilities for security data.       |

Key Data Types

- **Session Data**: Summarized communication between two devices, akin to a phone bill, documenting network sessions.
- **Transaction Data**: Logs operations resulting from network sessions, such as HTTP requests and responses.
- **Alert Data**: Generated by IDS/IPS systems when network traffic matches predefined rules, indicating potential threats.
- **External Data**: Information from outside the organization that helps identify emerging threats.

Key Concepts in Network Security Monitoring

- **Attack Kill Chain**: A model that outlines the stages of a cyber attack, helping analysts understand which data to examine during an incident.
- **Baseline Data**: Normal network traffic patterns used to identify anomalies by comparing actual traffic against established baselines.

Key Features of Security Tools

|Feature|Description|
|---|---|
|**Data Aggregation**|Collecting and summarizing data from various sources for analysis.|
|**Threat Detection**|Identifying potential security threats through monitoring and analysis.|
|**Log Management**|Organizing and maintaining logs for easy access and analysis.|
|**Automated Analysis**|Using scripts and algorithms to analyze traffic and detect anomalies.|
|**Incident Response**|Procedures and tools used to respond to security incidents effectively.|

Facts to Memorize

- Common data types in SOC: Session data, Full packet capture, Transaction data, Extracted data, Statistical data, Alert data, External data.
- Key features of Security Onion: Full packet capture, Intrusion detection, Log management.
- Popular SIEM product: Splunk Enterprise.

Reference Information

- NetFlow-v5, NetFlow-v9, and IPFIX are standards for session data.
- PCAP is the common file format for full packet capture data.
- Security Onion includes tools like Snort, Suricata, Zeek, and Wazuh.

Cause and Effect

|Cause|Effect|
|---|---|
|Use of session data in investigations|Provides a summary of network interactions, aiding in identifying suspicious behavior.|
|Implementation of full packet capture|Allows for detailed analysis of network traffic, but increases storage needs and complexity.|
|Integration of SIEM systems|Centralizes security data, enabling better monitoring and response to threats.|
|Adoption of threat intelligence feeds|Enhances the organization's ability to anticipate and respond to emerging threats.|

Key Terms/Concepts

- **SOC (Security Operations Center)**: A centralized unit that deals with security issues on an organizational and technical level.
- **Event Data Types**: Different types of data used in security analysis, including session data, full packet capture, transaction data, and alert data.
- **Full Packet Capture**: A method of capturing all data packets transmitted over a network, allowing for detailed analysis of network traffic.
- **SIEM (Security Information and Event Management)**: A system that collects and analyzes security data from across the organization to identify potential threats.

# Introduction to SOC and Event Data Types

### Understanding SOC Analysts' Role

- SOC analysts are responsible for monitoring and responding to security incidents by analyzing various types of event data.
- They must understand the attack kill chain process to identify which data types are relevant during an incident response.
- The effectiveness of an SOC analyst relies on their ability to interpret different data types to piece together the narrative of an incident.

### Importance of Event Data Types

- Different event data types provide unique insights; no single type can offer a complete picture of network activity.
- Analysts must utilize multiple data types to conduct thorough investigations and understand the context of security incidents.

# Overview of Alert Data

### Definition and Importance of Alert Data

- Alert data is generated by tools that analyze network traffic and other data types against predefined rules.
- It serves as a crucial first step in identifying potential security threats, allowing for faster response times than manual analysis.
- The generation of alert data is based on complex mechanisms that process large volumes of data in real-time.

### Limitations of Alert Data

- Despite its speed, alert data can suffer from inaccuracies, leading to false positives (incorrect alerts) and false negatives (missed threats).
- The effectiveness of alert data relies heavily on the quality of the rules and configurations set within the monitoring tools.
- SOC analysts must interpret alert data to determine its validity, which can be time-consuming.

### Role of SOC Analysts

- SOC analysts are responsible for reviewing alert data and making judgments on its relevance and accuracy.
- They utilize alert data as a starting point for deeper investigations into potential security incidents.
- The analysts' expertise is crucial in refining the alerting process and improving the overall security posture of the organization.

# External Data in SOC Operations

### Definition and Sources of External Data

- External data refers to information sourced from outside the organization, including threat intelligence feeds and reports.
- It provides insights into emerging threats and vulnerabilities that may affect the organization.
- Organizations must subscribe to threat intelligence feeds to stay updated on the latest security threats.

### Importance of Threat Intelligence Feeds

- Threat intelligence feeds help organizations proactively defend against potential attacks by providing actionable insights.
- They allow SOC teams to refine detection rules and improve the fidelity of alerts based on current threat landscapes.
- Incorporating external data into SOC operations enhances the context and relevance of alerts generated by internal systems.

### Integration of External Data into SOC Processes

- SOC analysts use external data to create indicators of compromise (IoCs) that help in identifying malicious activity.
- The integration of external data improves the overall effectiveness of the SOC by providing a broader view of the threat environment.
- Continuous updates from external sources are necessary to adapt to evolving threat tactics employed by adversaries.

# SOC Tools and Their Features

### Overview of SOC Tools

- SOC tools are essential for collecting, managing, and analyzing data to support security operations.
- A comprehensive suite of tools is necessary for effective network security monitoring (NSM).
- Each tool serves specific functions, such as network mapping, monitoring, and vulnerability detection.

### Key Tools in Security Onion

> Security Onion is a Linux-based distribution designed to support SOC analysts with various security monitoring tools.

- It includes functionalities for full packet capture, intrusion detection, and log management.
- The suite of tools within Security Onion enhances the capabilities of SOC analysts in detecting and responding to threats.

### Detailed Features of Security Onion Tools

> The following tools are integral to Security Onion's functionality:

| Tool Name     | Description                                                    | Key Features                                         |
| ------------- | -------------------------------------------------------------- | ---------------------------------------------------- |
| ELSA          | Centralized syslog framework for log management and searching. | Web-based query interface, log normalization.        |
| Snort         | Open-source NIDS/NIPS for real-time threat detection.          | Rules-driven alerts, real-time monitoring.           |
| Suricata      | Script-driven NIDS/NIPS for traffic analysis.                  | Multi-threaded, protocol parsing.                    |
| Zeek (Bro)    | Packet recorder and protocol parser for behavioral analysis.   | Anomaly detection, extensive logging.                |
| Wazuh (OSSEC) | Host-based intrusion detection system for monitoring hosts.    | Lightweight agent, cross-platform support.           |
| Wireshark     | Network protocol analyzer for deep packet inspection.          | GUI for packet analysis, extensive protocol support. |

# Conclusion and Future Considerations

### Evolving Threat Landscape

- The threat landscape is constantly changing, requiring SOC teams to adapt their tools and strategies.
- Continuous improvement of detection capabilities is essential to keep pace with threat actors' advancements.
- SOC analysts must remain vigilant and proactive in their approach to security monitoring.

### Importance of Training and Development

- Ongoing training for SOC analysts is crucial to ensure they are equipped with the latest knowledge and skills.
- Familiarity with the tools and technologies used in SOC operations enhances the effectiveness of threat detection and response.
- Organizations should invest in professional development opportunities for their SOC teams.

### Future Trends in SOC Operations

- The integration of artificial intelligence and machine learning in SOC tools is expected to enhance threat detection capabilities.
- Automation of routine tasks can free up SOC analysts to focus on more complex security challenges.
- Collaboration between SOC teams and external threat intelligence providers will become increasingly important.

# Overview of Security Tools

### Network Traffic Analysis Tools

- ****NetworkMiner****: A tool for analyzing network traffic, specifically designed to parse PCAP files and extract artifacts, which can be crucial for forensic investigations.
- ****CyberChef****: A web-based application that facilitates data manipulation, allowing analysts to perform various operations on data sets easily.
- ****CapME****: Assists in analyzing PCAP transcripts and downloading captured PCAP files, enhancing the ability to review network traffic.
- ****Security Onion****: A Linux distribution that includes various tools for network security monitoring, including the aforementioned tools, to help SOC analysts detect intrusions.
- ****Example Use Case****: A SOC analyst might use NetworkMiner to extract files from a suspicious PCAP file to investigate potential malware.

### Security Onion and Elastic Stack Components

- ****Elastic Stack (ELK)****: A newer version of Security Onion that integrates several powerful tools for log management and analysis.
- ****Elasticsearch****: A scalable search engine that ingests and indexes logs, allowing for quick searches and data retrieval.
- ****Logstash****: A data ingestion engine that parses and formats logs, making them ready for analysis.
- ****Kibana****: A web dashboard that provides visualizations of ingested log data, facilitating data exploration and analysis.
- ****TheHIVE****: A security incident response platform that integrates with MISP for effective case management.

# Advanced Security Analytics Tools

### Cisco Security Solutions

- ****Cisco Secure Network Analytics****: Formerly known as Stealthwatch, this tool provides insights into IP flows and detects various threats using telemetry data.
- ****Cisco Secure Malware Analytics****: A cloud-based solution for malware analysis that allows SOC analysts to submit samples for dynamic and static analysis.
- ****Cisco SecureX****: A platform that connects various Cisco security products, providing unified visibility and automated workflows across the security infrastructure.
- ****Integration Example****: Cisco Secure Malware Analytics can correlate data from millions of samples to provide insights into malware behavior.

### Penetration Testing and Vulnerability Assessment

- ****Penetration Testing****: Simulates an attack to exploit vulnerabilities, providing insights into the security posture of an organization.
- ****Vulnerability Assessment****: Identifies known vulnerabilities in systems, often performed before penetration testing to prioritize security improvements.
- ****Kali Linux****: A distribution that includes numerous penetration testing tools such as Metasploit Framework and Armitage, which are essential for ethical hacking.
- ****Example Scenario****: Using Armitage to exploit a vulnerability in Apache Struts to establish a reverse connection to a server.

# Security Information and Event Management (SIEM)

### Purpose and Functionality of SIEM

- ****SIEM Overview****: Collects and correlates logs to identify malicious actions within a network, crucial for SOC operations.
- ****Data Collection****: Automates the gathering of security data from various sources, allowing for centralized monitoring.
- ****Alerting Mechanism****: Notifies SOC analysts of anomalies, enabling timely responses to potential threats.
- ****Limitations****: While SIEMs are effective for data processing, human interpretation is still necessary to understand the context of alerts.
- ****Splunk Enterprise****: A leading commercial SIEM that offers features like search, indexing, and reporting, enhanced by AI and machine learning capabilities.

### Splunk Enterprise Features

- ****Customizability****: Splunk can be tailored to meet specific organizational needs through apps that provide additional functionalities.
- ****Data Modeling****: Allows analysts to create models that represent data relationships, enhancing analysis capabilities.
- ****Integration with Cisco Products****: Certain Cisco products are compatible with Splunk apps, facilitating a more cohesive security environment.
- ****Example Use Case****: A SOC analyst using Splunk to correlate logs from multiple sources to identify a potential breach.