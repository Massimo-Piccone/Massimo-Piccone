The network security analyst must use several types of data because no single data type offers a complete solution.

Monitoring types:
- Log data
- IPS alarts
- Full packet capture
- Netflow records

- Session data
	- Like when a detective analyzes a phone bill in their investigation. it doesn’t capture the content of communications but records key details like who communicated, when, and for how long. It tracks network sessions using a 5-tuple (transport protocol, source IP/port, destination IP/port) and includes timestamps and data volume. NetFlow is a widely used example of session data.
- Full packet capture
	- Akin to a wiretap, records all bits transferred across a networking wire, potentially extracting conversation content. While it may seem superior to session data, it has significant drawbacks. Full packet capture requires substantial storage and can be tedious to analyze, necessitating higher-level data types for effective guidance. PCAP is the most commonly used file format for storing full packet capture data.
- Transaction data
	- Records network session and system activities. For instance, an HTTP daemon logs client requests and responses, while an SMTP daemon logs connections, message forwarding, and local mailbox storage. A Linux system logs operating system login and logout activities. Each log file contains transaction data. Not all network sessions produce transactions, and some may be associated with multiple transactions. Transactions can also document local system activities unrelated to network communications.
- Extracted data
	- Files transmitted as email attachments or downloaded from websites, can be mined from network traffic. Some security monitoring systems pull extracted content from live network streams, while others allow mining from full packet capture files.
- Statistical data
	- Processes other security monitoring data types to describe network activities at a higher level. For instance, NetFlow documents individual web server connections as session data. Processing this session data and creating a graph showing the average number of connections per minute over the last month produces statistical data. Statistical data helps establish baselines, which document normal patterns and trends. Comparing actual traffic patterns to baselines can reveal anomalies.
- Alert data
	- Produced by IDS or IPS, is the most crystallized data type. It monitors traffic streams for malicious behavior using complex mechanisms and data sources. When traffic matches system rules, an alert is generated. While it’s not the most accurate or relevant, it’s a judgment call from a tool. False positives and negatives are potential issues. Alert data’s advantage is its real-time processing speed, surpassing human analysts. However, generating an alert often initiates the analysis process.
- Syslog
	- Provides real-time access to device logs. Most Linux hosts and network devices support syslog natively, while Windows hosts need additional software. Syslog allows hosts to forward log entries to central syslog servers, which act as listeners to capture events from remote syslog installations. These events are usually written to log files with time stamps, hostnames, and received events. The “push” model, where log events are sent as necessary, eliminates the need for individual queries.
![18](/Course-Notes/.assets/Screenshot_2024-11-15_at_10.07.25.png)RFC 5424 defines eight syslog severity levels: 0 to 7, with 0 being the highest and 7 the lowest.

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

![17](/Course-Notes/.assets/Screenshot_2024-11-15_at_10.12.03.png)

- **Indicator of Compromise (IOC)**
	An IOC is a high-fidelity predictor of system compromise extracted from security data. For instance, if CnC traffic is detected between an external IP address and a compromised system, that IP can be used as an IOC. If other internal systems communicate with it, they’re likely compromised. Similarly, if malware modifies the Windows registry in a specific way, it’s an IOC. Internal systems can be scanned for registry matches, indicating compromise.
	
	OpenIOC is an extensible XML schema that allows security professionals to describe technical characteristics of known threats, attackers’ methodologies, or other evidence of compromise.

- Network Time Protocol (NTP)
	- NTP Functionality: Synchronizes clocks of computers and network devices over a network, ensuring accurate timestamps for incident investigation.
	- NTP Security Risk: Malicious attackers can falsify NTP time advertisements, leading to incorrect timestamps and potential security breaches.
	- NTP Authentication: NTPv4 optionally implements authentication to verify the authenticity of the time source (NTP server).
	
	- Correlation Importance: Essential for analysts to utilize all NSM data types by linking events across different data sets.
	- IP 5-tuple Significance: Crucial for event correlation, enabling analysts to identify related network activities.
	- Metadata Utilization: Enhances NSM data by providing additional context, such as geolocation and reputation scores, associated with IP addresses.



![16](/Course-Notes/.assets/Screenshot_2024-11-15_at_10.13.38.png)![15](/Course-Notes/.assets/Screenshot_2024-11-15_at_10.13.53.png)


# SEIM
The success of a project depends on factors such as:
- business requirements, and 
- engineering specifications 
- Event and alarm volume in terms of disk usage, 
- and retention requirements must be understood.

The SIEM's backend and storage must be appropriately sized and perform well. The speed of result retrieval from a report or query is inversely proportional to log data size, so indexing doesn’t help much. Two major factors affect search volume: log data size from networked systems and the search query time range. If a SIEM only receives IPS alarms from a dozen sensors, how much data would it have to search through for an incident from a year ago? For regular reporting, waiting for results isn’t acceptable.

It is critical to understand reporting requirements and objectives. You need to understand not only where and how to deploy the SIEM and its collectors, but also why. Security teams choose to deploy an SIEM for many reasons:

- Security monitoring and incident response
- Anomaly detection
- Real-time rules-based alerts
- Data correlation
- Compliance or regulatory mandated logging and reporting
- Automated reports

SIEMs require ongoing configuration and tuning to effectively alert on incidents. Without tuning, the SIEM will be overwhelmed with unnecessary alarms, making it difficult to identify valuable information.

SIEMs have correlation engines with special algorithms that analyze logs and identify relationships between events. Correlation is a powerful method for confirming security incident details and eliminating circumstantial evidence. Noticing an alarm from a single host can be compelling, but it’s often insufficient. For instance, web proxy logs may indicate a host was a possible victim of a drive-by download attack. The SIEM can notify the analyst’s team, but the extent of the threat is unknown. It’s possible the host downloaded a complete file, but it’s unclear if it was unpacked, executed, or still relevant. If the antivirus deleted or quarantined the file, there may be a concern.

Correlation can solve this problem. If malware is downloaded, port scanning occurs, large outbound NetFlow to unusual servers, repeated connections to PHP scripts hosted in sketchy places, or other suspicious activity from the same host, create an incident report with additional details. The order is crucial as most attacks follow a pattern (bait, redirect, exploit, additional malware delivery, check-in). Tie these steps with security alarms and time stamps to ensure the events occur in the correct order.

The statistical and mathematical correlation determinations are best handled by the SIEM. However, the logical correlation can really only be done well by a human brain.

When deciding on SIEM deployment, the most important question to answer is “How does this technology help find incidents that would otherwise be overlooked with the existing tools?”

# Security Orchestration, Automation, and Response

SOAR involves security and IT teams collaborating to monitor and analyze security procedures. As organizations grow, automated SOC capabilities increase due to the need for faster incident detection, investigation, and remediation. Automation makes tools execute repeatable actions without human intervention, while orchestration completes workflows. Reducing redundant tasks allows security analysts to focus on critical functions like collaboration and informed decision-making.

A SIEM system collects log- and event-related data from security devices and resources, presenting security alarms to analysts in real time. A SOAR platform builds on this by automating information security event management and incident response when threats are detected. SOAR collects and analyzes cyber threat intelligence, supports integration with third-party threat security technologies, and integrates security threat intelligence and automates incident investigation and response workflows based on playbooks.

SOAR platforms share data aggregation capabilities with SIEMs, such as correlating and analyzing security alerts, but go further by integrating security threat intelligence and automating incident response. This reduces mean-time-to-detect (MTTD)/mean-time-to-respond (MTTR) metrics and improves playbook workflow efficiency.

![14](/Course-Notes/.assets/Pasted_image_20241115135624.png)

The Gartner Group defined SOAR in 2017, stating that a SOAR should have full security incident lifecycle automation, including orchestration, automation, and measurement of incident response processes, workflows, policy execution, and incident reporting.
  
- Threat and vulnerability management proactively manages risks associated with newly discovered vulnerabilities and supports investigations of potential threats.

- Security incident response uses advanced analytics to manage security incidents after a threat is confirmed and automation for incident response.

- Gartner’s SOAR market guide predicts that 30% of organizations with a security team larger than five people will leverage SOAR tools by year-end 2022.

SOAR platforms can automate reactions to malicious elements from well-known attack vectors. For instance, SOAR can analyze malicious spear-phishing campaign components and implement threat containment strategies against malicious IP addresses, embedded URLs, and files.

## Cisco SecureX Platform

Cisco SecureX is a new platform that integrates multiple security technologies from a single view for easy control and unified policies across on-premises and cloud assets. It’s an open, cloud-native platform that connects Cisco-integrated security with non-Cisco security products.

Cisco SecureX offers workflow automation, analytics, remediation, threat hunting, and the ability to interconnect disparate security systems. It’s included with every licensed Cisco security product and provides a comprehensive user experience across Cisco’s security portfolio. Cisco SecureX uses the CloudCenter Action Orchestrator as the underlying orchestration engine and offers more IT service functionality than a traditional SOAR. It includes pre-built playbooks and runbooks, and organizations can create custom playbooks for their network environment.

The foundational capabilities of Cisco SecureX include the following:

- Unifying visibility across all parts of an organization’s security portfolio, and Cisco or third-party solutions.
    
- A solution that is fully cloud-native and multi-tenant.
    
- Analyzing events and data across the enterprise and more than 150 million endpoints, and network traffic from switches and routers, including encrypted traffic, Google, AWS, Azure, and private data center environments.
    
- Within minutes, identifying threat targeted assets, enabling quick remediation by using data enrichment telemtery from security products and threat intelligence feeds.
    
- Bringing the power of Cisco Talos threat analysts into the organization to hunt for the latest threats.

![13](/Course-Notes/.assets/Pasted_image_20241115135744.png)

# Security Onion Overview

The Security Onion distribution is based on the Ubuntu Linux operating system and contains several useful security tools that are designed to provide four core network security-monitoring functions, as follows:

- Full packet capture
- Network-based and host-based intrusion detection sensors
- Security analysis tools
- Log management

Security Onion offers intrusion detection tools including Snort, Suricata, Bro, and OSSEC, along with analysis tools ELSA, Sguil, and Squert.

![12](/Course-Notes/.assets/Pasted_image_20241115140017.png)
1. Presentation of data to the analyst
2. Optimization and maintenance of data
3. Collection processing of raw NSM data
## Deployment Options

Distributed client/server model. A Security Onion server communicates with one or more Security Onion sensors (clients). The server and sensor components can run on a single physical or virtual machine, or multiple sensors can be distributed throughout an infrastructure and configured to report back to the Security Onion server. There are three deployment scenarios for Security Onion:

**Standalone:** 
- A single machine running both the server and sensor components. 
- Can have multiple network interfaces monitoring different network segments. 
- Easiest and most convenient centralized network monitoring.
	
**Server-sensor:** 
- A single machine running the server component, and one or more separate machines running the sensor component, reporting back to the server. 
- The sensors run all sniffing processes and store the associated packet captures, IDS alerts, and databases for Sguil and ELSA. 
- The server connects to the client machine and all queries that are sent to the server are sent to the appropriate sensors, with the requested information being directed back to the client. 
- Reduces network traffic by keeping the bulk of the collected data on the sensors until requested by the analyst’s client. All traffic through SSH-encrypted tunnels.
    
- **Hybrid:** A hybrid installation consists of a standalone installation that also has one or more separate sensors reporting back to the server component of the standalone machine.
    

##  Network Security Monitoring (NSM) Tools

- **Bro** ([https://github.com/Security-Onion-Solutions/security-onion/wiki/Bro](https://github.com/Security-Onion-Solutions/security-onion/wiki/Bro)): Bro is a powerful network analysis framework that is much different from the typical IDS.
    
- **ELSA** ([https://github.com/mcholste/elsa/](https://github.com/mcholste/elsa/)): ELSA is a centralized syslog framework that is built on Syslog-NG, MySQL, and Sphinx full-text search. It provides a fully asynchronous web-based query interface that normalizes logs and makes searching billions of them for arbitrary strings as easy as searching the web. It also includes tools for assigning permissions for viewing the logs, email-based alerts, scheduled queries, and graphing.
    
- [**Netsniff-ng**]([http://netsniff-ng.org/](http://netsniff-ng.org/)): Netsniff-ng is a free, performant Linux networking toolkit.
    
- [**OSSEC**]([https://ossec.github.io/](https://ossec.github.io/)): OSSEC is an Open Source host-based IDS, or HIDS. It performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting, and active response.
    
- [**Sguil**]([http://sguil.sourceforge.net/](http://sguil.sourceforge.net/)): Sguil (pronounced "sgweel") is built by network security analysts for network security analysts. Sguil's main component is an intuitive GUI that provides access to real-time events, session data, and raw packet captures. Sguil facilitates the practice of Network Security Monitoring and event driven analysis.
    
- [**Snort**]([https://www.snort.org](http://www.snort.org/)): Snort is an Open Source network intrusion prevention and detection system (IDS/IPS) developed by Sourcefire. Combining the benefits of signature, protocol, and anomaly-based inspection, Snort is the most widely deployed IDS/IPS technology worldwide. With millions of downloads and over 500,000 registered users, Snort has become the de facto standard for IPS.
    
- [**Squert**]([http://www.squertproject.org/](http://www.squertproject.org/)): Squert is a web application that is used to query and view event data that is stored in a Sguil database (typically IDS alert data). Squert is a visual tool that attempts to provide additional context to events by using metadata, time series representations and weighted and logically grouped result sets.
    
- [**Suricata**]([http://www.openinfosecfoundation.org/index.php/download-suricata](http://www.openinfosecfoundation.org/index.php/download-suricata)): The Suricata engine is an Open Source next-generation intrusion detection and prevention engine.


# Full Packet Capture

When setting up full packet capture, there are several things to consider:

- **Location:** The placement of sensing interfaces will affect which conversations are seen. Generally, sensing interfaces are placed at chokepoints in the network, such as ingress points behind an Internet-facing firewall, ingress points to the data center, and ingress points for remote-access VPN clients.
    
- **Method of network connection:** A single sensing interface may be connected to a switch port that mirrors traffic, often called a Switched Port Analyzer (SPAN) port. This method is the least reliable because packets can be missed. Even if only a single switch port is mirrored, the mirrored port allows full duplex connectivity and that may overflow the simplex capacity outbound from the mirroring interface. Another option is a network tap that splits a duplex connection into two separate simplex connections. The sensor can then dedicate two interfaces to receive traffic from the tap. While this guarantees network bandwidth, it does not necessarily guarantee compute capacity to handle packet capture. The most reliable method of connection is inline, where the sensor uses two interfaces and traffic is forced through the sensor between these two interfaces. This makes the sensor a bottleneck. If the sensor cannot forward the frames at wire speed, network performance may suffer. But, because the sensor will only forward the packets that it can process, it does not deliver any packets that are not recorded by the sensor.
    
- **NIC configuration:** With modern systems, certain aspects of packet processing that were originally done by the operating system can be offloaded to the NIC. Examples include the checksum offload and TCP segmentation offload. This offloading can improve system and network performance. From an NSM perspective, the packets that are captured must be exactly what is transferred on the network. Care must be taken to ensure that the offloading features are disabled on full packet capture interfaces. Security Onion automatically disables these offloads on its sensing interfaces. On Linux systems, the `ethtool` `-k` command can be used to verify the features that are configured on a NIC.

	    so@so:~$ **ethtool -k eth1**
	    Features for eth1:
	    rx-checksumming: off
	    tx-checksumming: off
	    	tx-checksum-ipv4: off [fixed]
	    	tx-checksum-ip-generic: off
	    	tx-checksum-ipv6: off [fixed]
	    	tx-checksum-fcoe-crc: off [fixed]
	    	tx-checksum-sctp: off [fixed]
	    scatter-gather: off
	    	tx-scatter-gather: off
	    	tx-scatter-gather-fraglist: off [fixed]
	    tcp-segmentation-offload: off
	    	tx-tcp-segmentation: off
	    	tx-tcp-ecn-segmentation: off [fixed]
	    	tx-tcp6-segmentation: off [fixed]
	    udp-fragmentation-offload: off [fixed]
	    generic-segmentation-offload: off
	    generic-receive-offload: off
	    large-receive-offload: off [fixed]
	    <…output truncated…>


Storage requirements and policies must also be considered with full packet capture. Full packet capture quickly consumes disk space. The oldest data must be purged to make room for new data as it arrives. The target lifespan of full packet data will vary from one SOC to the next, based on requirements and constraints. Some SOCs may only expect a couple of hours of full packet history, while others may target as much as a full month of full packet history, and anything in between is possible. Analysts must understand how long they can expect full packet capture to be available in an environment. Full packet capture may also have to share available storage with other NSM data types, depending on the NSM architecture. The default policy on Security Onion is to purge data based on a drive utilization threshold. A cron job is run once per minute to delete the oldest PCAP files when drive utilization exceeds 90 percent.


Netflow is best alternative when full packet capture is unavailable

## TCPdump

![11](/Course-Notes/.assets/Pasted_image_20241115143623.png)
![10](/Course-Notes/.assets/Screenshot_2024-11-15_at_14.37.54.png)

BPF syntax allows you to combine criteria to form a capture filter to be used within the `tcpdump` command:

- `**host**`: Defines a specific host
- `**net**`: Defines a network, classful or classless, and can be combined with `mask`
    1. **`net 192.168.`**`1`**`.0`**
    2. **`net 192.168.`**`1`**`.0 mask 255.255.255.0`**
    3. **`net 192.168.`**`1`**`.0/24`**
- `**port**`: Specifies a specific port
- `**src**`: Source, can be combined with any type
- `dst`: Destination, can be combined with any type
- `and`: Combines two filters; both must be true
- `or`: Combines two filters; either must be true
- `not`: Negates a filter (useful for ignoring designated traffic)
- `ip`: Filters, based on IPv4 packets
- `ip6`: Filters, based on IPv6 packets
- `**arp**`: Filters, based on ARP traffic
- `**icmp**`: Filters, based on ICMP messages
- `tcp`: Filters, based on TCP segments
- `udp`: Filters, based on UDP datagrams

# BPF Syntax Examples

| **Parameter**                                              | **Description**                                                                                 |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| `host mailserver`                                          | Captures packets from or to host mail server                                                   |
| `host mailserver and webserver`                            | Captures packets between mail server and web server                                            |
| `tcp port 80`                                              | Captures TCP packets to or from port 80                                                       |
| `tcp port http`                                            | Captures TCP packets to or from port 80 or the HTTP port number as defined in the `/etc/services` file |
| `icmp[icmptype] != icmp-echo and icmp[icmptype] != icmp-echoreply` | Captures all ICMP packets that are not echo requests or replies (i.e., not ping packets)       |
| `host 192.168.0.1 and $begin:math:text$192.168.0.2 or 192.168.0.3$end:math:text$`      | Captures traffic between 192.168.0.1 and either 192.168.0.2 or 192.168.0.3                     |

To capture traffic that is not destined for the local machine, the network card must be placed into a special mode, referred to as "promiscuous mode," which causes the network card to interpret all traffic that it sees. Administrative or superuser permissions within the operating system are required to enter promiscuous mode. For this reason, tcpdump (and windump) must be run as the root user (or administrator user).

# Session Data

Security Onion offers a few tools that can capture session data, including Bro, Argus, and Passive Real-Time Asset Detection System (PRADS). In NSM, it is generally a best practice to limit redundancy. While there are exceptions, it is inefficient to have multiple tools collect and store what is largely the same data. Bro can produce much more than session data. The analyst can configure it to produce session data, transaction data, extracted content, statistical data, metadata, and alert data. For this reason, the Security Onion administrator will commonly choose to implement Bro but not Argus or PRADS.

Bro is a network analysis framework that is written in a specialized scripting language that is also named Bro. The default Bro installation provides several NSM functions. It provides audit records of every network session that is seen on the wire. It also provides audit records at the application layer. For example, all HTTP sessions are tracked with the requested Uniform Resource Identifiers (URIs), MIME types, and server responses. The Bro scripting language provides analyzers for many commonly used protocols that can be used for semantic analysis at the application layer. As such, Bro can be extended in any fashion by a skilled engineer.

While session data is very simple, it can be used to answer many important questions that arise regularly in the SOC. Threat intelligence reports may provide a list of suspicious external IP addresses. Session data can be consulted to see if any internal systems have communicated with any of the suspicious external IP addresses. Similarly, if a particular TCP port is associated with an active malware campaign command and control, session data can be consulted to see if any internal systems are communicating by using that TCP port. If an internal host has been identified as being compromised, session data can identify other internal systems that it has communicated with (potential lateral movement) and any external systems that it has communicated with (potential data exfiltration).

# Transaction Data

```
Dec  4 19:02:48 inside-srv postfix/smtpd[7358]: connect from dmz-srv.abc.public[172.16.1.10]
Dec  4 19:02:48 inside-srv postfix/smtpd[7358]: 48C3A186A0A: client=dmz-srv.abc.public[172.16.1.10]
Dec  4 19:02:48 inside-srv postfix/cleanup[7362]: 48C3A186A0A: message-id=<58446858.8050301@services.public>
Dec  4 19:02:48 inside-srv postfix/qmgr[4268]: 48C3A186A0A: from=<william@services.public>, size=160062, nrcpt=1 (queue active)
Dec  4 19:02:48 inside-srv postfix/smtpd[7358]: disconnect from dmz-srv.abc.public[172.16.1.10]
Dec  4 19:02:48 inside-srv postfix/local[7363]: 48C3A186A0A: to=<wendy@abc.private>, orig_to=<wendy@abc.public>, relay=local, delay=0.07, delays=0.06/0/0/0, dsn=2.0.0, status=sent (delivered to maildir)
```

- Provides audit trails of client requests and server responses
- ﻿﻿Sourced from servers:
	- ﻿﻿DHCP
	- ﻿﻿DNS
	- ﻿﻿Mail
	- ﻿﻿Web
	- ﻿﻿Proxies, etc.

- ﻿﻿Security Onion includes Syslog-ng to collect Syslog messages
	- ﻿﻿Servers configured to forward transaction logs
- ﻿﻿Security Onion includes Bro
	- ﻿﻿Capable of producing transaction logs for common application protocols

As with any of the NSM data types, using an application to present the data can make visualization better and analytic steps easier. The following image shows the above Bro log in ELSA. Note that any of the underlined fields are hyperlinks in ELSA. Clicking the hyperlink will pivot to a new report focusing on the selected detail.

# Alert Data

- ﻿﻿Produced by IDS and IPS systems
	- ﻿﻿IPS = inline
	- ﻿﻿IDS = port mirroring or network tap
		- ﻿﻿IPS with drop disabled considered IDS mode
- ﻿﻿Analyst must determine efficacy of the alert
	- ﻿﻿Relevancy: success or unsuccessful?
	- ﻿﻿Alert correlation
- ﻿﻿Security Onion
	- ﻿﻿Rules-based IDS operations
		- ﻿﻿Snort
		- ﻿﻿Suricata
- ﻿﻿Consoles
	- ﻿﻿Sguil
	- ﻿﻿Squert

![9](/Course-Notes/.assets/Pasted_image_20241115154320.png)
![8](/Course-Notes/.assets/Pasted_image_20241115154109.png)

At this point, the analyst might check internal systems documentation, or contact someone in IT, to find out if this server is running this potentially vulnerable version of phpMyAdmin. Other NSM data is available to the analyst. In this case, the analyst can answer the question. Looking at the packet data, the analyst can see that there was an HTTP GET request for /3rdparty/phpMyAdmin/server_synch.php. The question is, how did the server respond to this request? Logs of client requests and server responses are transaction data. Bro records HTTP transaction data, and ELSA provides an interface to query the Bro logs. The security analyst may pivot from Sguil to ELSA, querying on the alert 5-tuple, and potentially including BRO_HTTP.uri = phpmyadmin in the query specification. This figure shows an entry produced by ELSA.

![7](/Course-Notes/.assets/Pasted_image_20241115154528.png)

ELSA can pivot directly to capME!, which will decode the PCAP data associated with this particular TCP connection. HTTP GET requests are made within this TCP connection. Here, multiple GET requests that are associated with the URI /3rdparty/phpMyAdmin/server_sync.php. In that decode, the analyst can see that the server responded with a 404 Not Found. The example transcript below shows that the exploit missed its target. The target URI was not available on the server.

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
# Other Data Types

#### Extracted Content
- ﻿﻿Artifacts that are carved out of real time traffic streams, or out of PCAP files
- ﻿﻿Can be files, string, full web pages
- ﻿﻿Bro is capable of extracting files and streams
	- ﻿﻿Default: all recognized Windows executable files
	- ﻿﻿Other types can be configured
- ﻿﻿Security Onion includes Network Miner
	- ﻿﻿Extracts many data types
		- ﻿﻿Certificates, images, session data, DNS, Host IPs

Artifacts that may be extracted include the following:

- **Sessions:** Session data about all network connections, including the standard IP 5-tuple, time stamp of the session start, and frame number within the PCAP where the session starts.
- **DNS:** Transaction data documenting all DNS requests and replies.
- **Hosts:** All IP addresses that are seen in the PCAP along with other relevant information that can be gleaned from the PCAP. Potential information includes DNS hostnames, open TCP ports, operating system, sessions that are associated with the host, and total packet and byte counts that are associated with the host

#### Statistical Data
- ﻿﻿Aggregates events and provides summaries
- ﻿﻿Useful in developing an overall picture
- ﻿﻿Queried and reported in different formats
- ﻿﻿Can answer questions:
	- ﻿﻿Which hosts request the most HTTP data?
	- ﻿﻿Which hosts serve the most HTTP data?
	- ﻿﻿Which DNS domains are most requested?
- Produce baselines over time.

![6](/Course-Notes/.assets/Pasted_image_20241115181903.png)
![5](/Course-Notes/.assets/Pasted_image_20241115181909.png)
#### Meta data — data about data
- Geolocation
- Ownership
- Reputation
	- Email
	- C&C
	- Malware distribution

# Correlating NSM Data

Each NSM data type can reveal certain pieces of information. Multiple data types and multiple data sources must be used together to reveal all the information. To put the information together, the analyst must be able to correlate data of different types from different sources. The IP 5-tuple and time stamps are valuable for correlating events across multiple data sets. Here is an example where multiple data sources can be used and correlated to develop a larger picture.

In the following figure, three IPS alerts are summarized. Each alert contains the full IP 5-tuple. The destination port (TCP port 25) identifies the SMTP protocol. The time stamps are identical. Email services are configured where inbound email is first received by a system on the demilitarized zone (DMZ) and then forwarded to the internal email server. IPS sensors are deployed on both the DMZ subnet and the internal server subnet. With knowledge of the DMZ and internal server addresses and IPS sensor placement, the analyst can deduce that all three alerts are associated with the delivery of the same email, as it was received on the DMZ, then forwarded from the DMZ and finally received on the internal server subnet.

![4](/Course-Notes/.assets/Pasted_image_20241115182653.png)

the analyst sees that the alert is associated with a suspicious executable email attachment, which can correlate with extracted content. 
The analyst examines the files that Bro has extracted and finds that three files are extracted from SMTP with the same time stamps as the three alerts. 
A quick hash sum computation on the three files verifies that they are all identical. Again, the same email with the attachment was seen three times as it was forwarded through the network. The analyst submits this file it to a sandbox detonation service to see if any malicious activity is triggered. As seen in the figure, when the file is executed, it attempts to connect to a system on the Internet.

The email was directed to Wendy.

```
Oct 12 19:53:29 inside-srv postfix/smtpd[4620]: connect from dmz-srv.abc.public[
172.16.1.10]
Oct 12 19:53:29 inside-srv postfix/smtpd[4620]: 9F659187BDC: client=dmz-srv.abc.
public[172.16.1.10]
Oct 12 19:53:29 inside-srv postfix/cleanup[4625]: 9F659187BDC: message-id=<894ec
b45-9d17-474e-e263-cb8184c24f02@services.public>
Oct 12 19:53:29 inside-srv postfix/qmgr[4607]: 9F659187BDC: from=<karla@services
.public>, size=102582, nrcpt=1 (queue active)
Oct 12 19:53:29 inside-srv postfix/smtpd[4620]: disconnect from dmz-srv.abc.publ
ic[172.16.1.10]
Oct 12 19:53:29 inside-srv postfix/local[4626]: 9F659187BDC: to=<wendy@abc.priva
te>, ==orig_to=<wendy@abc.public>==, relay=local, delay=0.07, delays=0.05/0.01/0/0.0
1, dsn=2.0.0, status=sent (delivered to maildir)
Oct 12 19:53:29 inside-srv postfix/qmgr[4607]: 9F659187BDC: removed
```

So far, the logs show that the email reached the internal SMTP server and was directed to Wendy. Looking further in the log file shows that Wendy logged in with an Internet Message Access Protocol (IMAP) client. IMAP clients automatically synchronize mailboxes upon connection. The analyst can assume that Wendy did receive the email.

The log also indicates Wendy's IP address, which is an important artifact.

```
Oct 12 20:57:29 inside-srv imapd: LOGIN, ==user=wendy==, ==ip=[::ffff:10.10.6.10]==, port=[1677], protocol=IMAP
```

![3](/Course-Notes/.assets/Pasted_image_20241115182913.png)

Given the precise information that the focused session data provides, the analyst can easily find relevant conversations within the full packet capture data. Using the protocol decode features of the protocol analyzer, the analyst can examine the details of an FTP data session and view any data that has been exfiltrated.

The intent of this simplified scenario is to demonstrate that event correlation across multiple data types and data sources is critical to the network security analysis process.

# Personally Identifiable Information

![2](/Course-Notes/.assets/Pasted_image_20241116094050.png)
Examples of PII data include the following:

- Name, such as full name, maiden name, mother's maiden name
- Telephone numbers, including home, and mobile numbers
- Date and place of birth
- Passport number, social security number, driver license number
- Personal characteristics, including photographic image (especially of the face or other distinguishing characteristic), x-rays, fingerprints, or other biometric image or template data (for instance, retina scan, voice signature, and facial geometry)

Examples of non-PII data include the following:

- Office location
- Business email address    
- Other information that is releasable to the public

# Regulatory Compliance

![1](/Course-Notes/.assets/Pasted_image_20241116094441.png)

Current trends in regulatory compliance include the following:

- Strengthened enforcement
- Global spread of data breach notification laws
- More prescriptive regulations
- Growing requirements regarding third parties (business partners)
- Risk-based compliance on the rise
- Compliance process streamlined and automated

## Examples of compliance regulations

- **Payment Card Industry Data Security Standard** (PCI DSS)**:** The PCI DSS is a proprietary information security standard for organizations that handle branded credit cards from the major card brands including Visa, MasterCard, American Express, Discover, and JCB. Private label cards, which are without a logo from a major card brand, are not included in the scope of the PCI DSS.
    
- **Health Insurance Portability and Accountability Act** **(HIPAA):** On the healthcare side, the HIPAA legislation, which was enacted in 1996, required the U.S. Department of Health and Human Services to develop a set of national standards for healthcare transactions. These standards provide assurance that the electronic transfer of confidential patient information will be as safe as, or more safe than paper-based patient records.
    
- **Sarbanes-Oxley (SOX) Act:** The SOX Act of 2002 is legislation that was passed by the U.S. Congress to protect shareholders and the general public from accounting errors and fraudulent practices in the enterprise, as well as improve the accuracy of corporate disclosures. The law was created in response to several major corporate and accounting scandals, including those affecting Enron, Tyco International, Peregrine Systems, and WorldCom. These scandals resulted in a decline of public trust in accounting and reporting practices.
    
- **General Data Protection Regulation (GDPR):** The GDPR law applies to any organization that holds and uses personal data on European Union (EU) citizens. GDPR applies whether the organization is based in Europe or not. If the organization possesses EU data then it must comply with GDPR. Fines for non-compliance can be substantial: up to 4% of your annual global revenue (turnover) or EUR 20 million (~$21 million) per violation. The law is intended to strengthen individuals’ personal privacy rights. For instance, under GDPR, conditions for consent are much stronger, and the consent language must be simple and easy to understand. It provides the right to erasure, which enables EU citizens to have organizations permanently delete all their personal data. GDPR also introduces data portability: EU citizens can demand copies of all data that organizations hold on them or have their data forwarded to another organization if they choose. In addition, GDPR requires organizations to gather all related information and notify the appropriate regulators within 72 hours of a data breach discovery.
    
- **Public Sector Information (PSI) Directive**, also referred to as the '**Open Data Directive**', governs the reuse of public sector information throughout the European Union. It builds on existing legislation pertaining to privacy and data protection by removing barriers that may hinder the reuse of public sector information. Public sector information includes any content, whatever its medium (written on paper or stored in electronic form or as a sound, visual or audiovisual recording). In the European Union, the public sector is one of the most data-intensive sectors. Under the newly revised rules: this Directive encourages the Member States to make material held by public sector entities (national utilities, transport) freely available for re-use. With this Directive, public sector bodies are not be able to charge more than the marginal cost for the reuse of their data, except in very limited cases. This allows more small and medium sized enterprises (SME) and startups to enter new markets that provide data-based products and services. It also strengthens the transparency requirements for public–private agreements involving public sector information, avoiding exclusive arrangements.
    
    1. PSI Reference: [https://ec.europa.eu/digital-single-market/en/implementation-public-sector-information-directive-member-states](https://ec.europa.eu/digital-single-market/en/implementation-public-sector-information-directive-member-states)
        
    2. PSI Reference: [https://ec.europa.eu/digital-single-market/en/public-sector-information-psi-directive-open-data-directive](https://ec.europa.eu/digital-single-market/en/public-sector-information-psi-directive-open-data-directive)
        
- **Federal Information Security Management Act (FISMA)**: The FISMA of 2002 was intended to bolster computer and network security within the U.S. government and affiliated parties by requiring yearly audits. FISMA also brought attention within the U.S. government to cybersecurity, which the U.S. government had previously largely neglected.
    
- **Gramm-Leach-Bliley Act (GLBA):** The GLBA of 1999 erased longstanding antitrust laws that prohibited banks, insurance companies, and securities firms from merging and sharing information with one another. The idea was that smaller firms would then be able to pursue acquisitions or alliances, or both, that would help encourage competition against many of the larger financial institutions. Included in the GLBA were several consumer privacy protections. Namely, companies must tell their customers what kinds of data they plan to share and with whom, and they must give their customers a chance to opt out of that data sharing.
    
- **Personal Information Protection and Electronic Documents Act** **(PIPEDA):** The PIPEDA, or the PIPED Act, is a Canadian law relating to data privacy. It governs how private sector organizations collect, use, and disclose personal information while conducting commercial business.
    
- **Data Protection Directive (95/46/EC):** The Directive 95/46/EC (on the protection of individuals regarding the processing of personal data and on the free movement of such data) is a European Union directive that was adopted in 1995 which regulates the processing of personal data within the European Union.
    
- **Basel II:** Basel II is the second of the Basel Accords, which are recommendations on banking laws and regulations that are issued by the Basel Committee on Banking Supervision. Basel II, initially published in June 2004, was intended to create an international standard for banking regulators to control how much capital banks need to put aside to guard against the types of financial and operational risks banks face.
    
- **Digital Millennium Copyright Act** **(DMCA):** The DMCA is a United States copyright law that implements two 1996 treaties of the World Intellectual Property Organization (WIPO). It criminalizes production and dissemination of technology, devices, or services that are intended to circumvent measures (commonly known as digital rights management or DRM) that control access to copyrighted works. It also criminalizes the act of circumventing an access control, regardless of actual infringement of copyright itself. In addition, the DMCA heightens the penalties for copyright infringement on the Internet.
    
- **Safe Harbor Act:** Related to the Organization for Economic Co-operation and Development (OECD) principles and their impact on international trade is the regulatory framework of a Safe Harbor Agreement. From the EU perspective, data transfer can happen only if there is a determination of adequate privacy processes and safeguards in place. The EU does not automatically grant that assurance of adequacy for non-EU member nations, like the United States or Canada does. To facilitate data transfer, to enable international trade, and to bridge any privacy differences, the EU, and United States, through the Department of Commerce, have developed a Safe Harbor framework that satisfies the adequacy requirement.

# Intellectual Property

the loss of intellectual property costs businesses billions of dollars and results in the loss of many jobs every year. Loss of an organization’s intellectual property can damage employees, partners, customers, and other institutional stakeholders. Theft or nullification of these assets may reduce or even erase profits, disrupt operations, undermine competitiveness, compromise hard-won reputations, and invite litigation or regulatory sanctions.

the challenge of safeguarding a company’s intellectual property portfolio, “It’s identifying what you need to protect, determining who would benefit from taking it, understanding the vectors that can be used to compromise it, and then developing a defense commensurate with the value of the property.”

## Information Assets

Intellectual property has traditionally been defined as trademarks, copyrights, patents, and trade secrets for which a person or organization can claim exclusive ownership. But in today’s business world, that definition has expanded to include virtually any nonmaterial asset—whether owned in a strictly legal sense or not—that distinguishes a business and enables it to thrive and prosper. Cisco refers to these as information assets.

Information assets encompass traditional intellectual property, in addition to other nonmaterial assets, and incorporate many areas within a business, including:

- Patented inventions that distinguish a company’s products. But also the company’s human capital: employees who have the inventive skills, technical knowledge, and institutional memory that contribute to an organization's stature in the marketplace.
    
- Customer lists and client files, but also the sales tools, marketing materials, and advertising plans that enable the business to find and retain customers and clients.
    
- Sales figures and budget projections that, if revealed, could compromise competitiveness. But also other sensitive financials that could affect the business’s credit rating, mergers/acquisitions, stock price, or private capital infusions.
    
- Design documents and plans for future products and services. But also all the R&D results, test data, and market studies that go into producing a successful product.
    
- Banking information that could make the business vulnerable to thievery. But also the business processes, proprietary practices, and supply chain innovations that help a company achieve and maintain profitability.

The list includes just a few of the forms that information assets can take. Every organization will have its own inventory of valued assets.

Companies must protect their information assets, including those entrusted by customers, clients, partners, and the public. These external assets range from sensitive business data to customer credit card numbers and citizens’ identity, tax, and health records. Companies now steward their customers’ sensitive information, and inadequate protection could harm customers and negatively impact the company.

## Threat Spectrum

The threat spectrum is the ways in which an organization’s information assets can be compromised.

Types of attackers that threaten information assets fall into four categories:

- **Organized crime:** Organized crime includes professional counterfeiters, hackers, and others who operate as part of illegal schemes, conspiracies, or criminal networks. Stolen information assets can continue to generate revenue over time.
    
- **Unscrupulous competitors:** Competitors employ illegal techniques ranging from industrial espionage to patent-infringing reverse engineering to gain unfair advantages in the marketplace. Even joint ventures and sanctioned partnerships have resulted in covert intellectual property theft.
    
- **State entities:** Countries use their powers of eminent domain to seize or nationalize intellectual property. They may also use their own intelligence-gathering organizations to uncover valuable assets that can benefit domestic industries.
    
- **Individuals:** Current and former employees steal and sell corporate intellectual property, sometimes gathering information for another entity. Competitors have also placed agents in businesses expressly to gather proprietary information.

## A Pervasive Security Culture

The most effective way to protect information assets is to carefully inventory what must be protected and identify how those assets relate to the people and processes that make up the business’ intricate skein of trust relationships. For instance, securing a data network involves not only defending its borders, but also understanding how employees, suppliers, partners, vendors, application service providers, and others interact with the network and access the various information resources. To effectively defend its information assets, a company needs to weigh its business plans, its IT strategy, its risk tolerance, and its corporate culture.

As with security in general, the protection of information assets is the business of every employee. One of the main duties of a company’s chief security officer is to construct and maintain a security culture within the organization that places a high value on information assets and their preservation. Employees must feel a sense of ownership when enforcing a set of security principles.

Creating a security culture capable of protecting information assets also requires an intimate understanding of the data lifecycle—what it is, where it goes, who touches it, and where it ultimately resides. The process is multidimensional, going beyond IT infrastructure to include people, policies, and processes. So the security organization must query and partner with all the relevant stakeholders to make sure that the entire spectrum of needs is addressed and met.

The emergence of the zero trust security model has also shifted the center focus of some security frameworks from securing the perimeter to protecting sensitive data such as the company’s information assets. Visibility is the key in defending any valuable information assets. The more visibility you have into the network across the business ecosystem, the better chance to quickly detect the loss of information assets. The zero trust security model provides visibility and analytics across the business ecosystem. The zero trust security model is a comprehensive approach to securing all access across the networks, applications, and environment. Zero trust is assumed when someone or something requests access to work assets. Trustworthiness must first be verified before granting access.