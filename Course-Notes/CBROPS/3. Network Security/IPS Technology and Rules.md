# Intrusion Detection and Prevention

unlike a traditional firewall, IPS/IDS systems analyze the payload of the packet to determine if the payload is potentially malicious. Note that IPS allows or blocks traffic after determining whether it is considered malicious.

![19](/Course-Notes/.assets/Pasted_image_20241114113745.png)

## Detection versus Prevention

![18](/Course-Notes/.assets/Pasted_image_20241114113941.png)
After an IDS generates an alarm, you must respond. For instance, you can configure firewall rules to block malicious IP addresses. However, this approach is not scalable and has drawbacks. For example, if you’re slow to block malicious traffic, adversaries can steal data. If they attack from multiple changing IP addresses, would you be able to configure new blocking rules quickly? In these situations, implementing an IPS is advisable.
![17](/Course-Notes/.assets/Pasted_image_20241114113955.png)
An IPS can identify and block attacks that normally pass through a traditional firewall device or an IDS. If the traffic that comes in through an interface on an IPS matches an IPS signature or rule, an IPS can act and drop that traffic.

## Detection Methods
![16](/Course-Notes/.assets/Pasted_image_20241114114306.png)

Anomaly-based detection learns normal network activity patterns and compares live traffic to the baseline. Any deviations indicate suspicious activity. However, users’ changing workflows can generate false alarms.

Signature-based (rule-based) detection analyzes live traffic using a database of IPS rules (signatures) to identify suspicious activity. The rules recognize attacks based on known patterns. The IPS appliance has pre-installed signatures, and administrators can create custom ones from external security intelligence sources like Cisco Talos. Talos also provides contextual threat information, including IOCs, malicious IP addresses, domains, and malware file hash values.

Today, sophisticated IPSs can gain deeper insight into traffic flows by reassembling traffic, rebuilding TCP sessions, and maintaining states. This behavior, known as deep packet inspection (DPI), allows IPSs to obtain a broader context than just focusing on one packet. Present-day IPSs also import security intelligence data feeds and external information to enhance their capabilities and efficiency. The newly branded name for IPS solutions is Cisco Secure IPS.

## IPS Roles and Features

![15](/Course-Notes/.assets/Pasted_image_20241114114529.png)

An IPS can analyze traffic from Layer 2 to Layer 7, as follows:

- Analyze the traffic that controls the Layer 2 to Layer 3 mappings, such as Address Resolution Protocol (ARP) and DHCP traffic.
- Verify that packets follow the correct protocol format and block malformed packets for networking protocols such as IP, TCP, UDP, and Internet Control Message Protocol (ICMP).
- Analyze the packet’s payload to identify the presence of suspicious activities and malware.

can be used a standalone hardware or virtual appliance or run alongside NGFW and other appliances.

You can configure IPS to send alerts in response to events that it detects. Sending notifications about security events to an external system helps monitor the environment. An external system can be a syslog or SNMP server or a SIEM.

## Types of IPSs

![14](/Course-Notes/.assets/Pasted_image_20241114115129.png)
- **Network intrusion prevention system (NIPS)**: A NIPS, which can be active or passive, monitors all the traffic traversing the network and analyzes the activity in the network.
    
    - An active NIPS can inspect the traffic inline as it passes through and alert or drop the traffic if it is considered malicious.
        
    -  A passive NIPS behaves like an IDS that is not inline with the traffic, meaning you must configure another network device to forward the traffic to the passive NIPS for inspection. Unlike an active NIPS, a passive NIPS can alert you of malicious traffic but it cannot drop the traffic.

- **Wireless intrusion prevention system (WIPS)**: In a secure wireless network environment, only permitted devices (access points) should provide access to the wireless network. If an attacker can set up a rogue access point and make clients connect to their wireless network, the attacker can then perform a man-in-the-middle (MITM) attack or a denial of service (DoS) attack. To protect against and mitigate wireless network attacks, you can deploy a WIPS in the network. WIPS scans for rogue access points ) and prevents them from broadcasting unauthorized wireless networks (wireless IPS capability). Some of the Cisco access points in correlation with Cisco wireless LAN controller (WLC) can enable WIPS functions out of the box. When an authorized Cisco access point detects a rogue access point with clients associated to it, it starts broadcasting deauthorization frames, which tell the wireless clients that were connected to the rogue access point to disconnect.
![13](/Course-Notes/.assets/Pasted_image_20241114115406.png)

- **Host Intrusion prevention system (HIPS)**: Host-based IPS is software that is installed directly on an endpoint that connects to the network, such as a laptop. Today, HIPS has evolved to more modern endpoint protection solutions, such as Cisco Secure Endpoint (formerly known as Cisco Advanced Malware Protection [AMP]). Cisco Secure Endpoint is designed to prevent software viruses, worms, trojans, and malware such as ransomware, spyware, adware, and fileless malware in an efficient way. The enterprise employee endpoint device is a common attack vector which often serves as the entry point into the targeted network. From the endpoint device, the adversaries can spread the malware to other hosts on the network, but if you protect the endpoints, you can drastically decrease the risk factor of malware gaining access.

## NIPS Placement Within the Network
If you deploy NIPS correctly within the network, it can lead to greater traffic visibility. If done incorrectly, some traffic could bypass the IPS and move through the network undetected, making the network vulnerable.

![12](/Course-Notes/.assets/Pasted_image_20241114115509.png)

An IPS placement must be in the path of, or inline with the traffic, in order for it to block malicious traffic flows. 

The figure shows an example of IPS placement at the internet edge. The IPS can inspect traffic going to and coming from the internet. However, traffic between the local network is not inspected by the IPS because that traffic never reaches it. The Layer 3 core switch routes the traffic directly between the HR Net, IT Net, and Finance Net local networks.

The security team must decide what to protect to determine IDS/IPS placement. Traditionally, most IT threats originate from the external network. To secure the network, inspect all inbound internet traffic for potential malicious activity and outbound traffic for command-and-control traffic and exfiltrated data.

Depending on what an IPS is supposed to protect, you can place it at the network perimeter or deeper within the network, for instance at the data center perimeter. If you deploy an IPS at the network perimeter, then it can only inspect traffic entering and leaving the network perimeter, while the rest of the network remains unprotected. In many cases, the security team deploys multiple IPSs to protect specific segments of the network. An example is placing an IPS at the perimeter of the data center which is specifically tuned to protect the data center from potential threats that are more specific to the data center servers. Another common practice is to deploy IPS solutions from multiple vendors or different types of IPSs (rules-based, anomaly-based, NIPS, WIPS, HIPS), to protect the whole environment using a defense-in-depth approach.

![11](/Course-Notes/.assets/Pasted_image_20241114120332.png)

The figure shows another example of IPS placement in the network with multiple IPSs. One is placed at the network perimeter protecting the entire network from outside threats, while the other is placed in the data center, protecting resources within from internal and external threats. The internal IPS can protect the data center from malware proliferation or lateral movement of attackers in case a single system is infected.

# Common Threat Detection and Prevention Systems

## Snort
Launched in 1998.
Free and open-source IDS and IPS system.
Cisco acquired Sourcefire in 2013.
Snort is now incorporated into multiple product lines, such as 
	- Cisco Secure Firewall Threat Defense (previously Cisco NGFW), 
	- Cisco Umbrella cloud-delivered firewall (CDFW), 
	- Cisco ISR routers running Cisco IOS XE Software,
	- Cisco Software-Defined WAN (SD-WAN) router lineup.
![10](/Course-Notes/.assets/Pasted_image_20241114120704.png)

Linux, Windows, or dedicated network appliances. 

It has the following three main modes of operation:
1. **Sniffer:** Snort reads the network data stream (captures packets) and displays the packet information on the console, behaving similarly to the TCPdump program.
    
2. **Logger:** Snort writes each captured packet to a separate file similarly to TCPdump used with the -w option. On a high-bandwidth network, it is better to write output to a binary file because it stores the data in a TCPdump format. You can view a TCPdump-formatted file with packet analyzer tools, such as Wireshark.
    
3. **Network Intrusion Detection System (NIDS) mode:** This is where Snort performs detection and analysis of network traffic and if configured, acts as an IPS. This is the most feature-rich mode but at the same time the most complex of all three, requiring a configuration file. The configuration file references the set of Snort rules, which are used to detect suspicious and malicious activities.

In Cisco products that feature Snort, Snort operates in the NIDS mode and can act as an IPS.

Snort is a rule-based (signature-based) intrusion system. Predefined Snort rules (or signatures) belong to two general groups:

- **Subscriber Ruleset:** Cisco Talos, the Cisco threat intelligence team, develops, tests, and approves the Subscriber Ruleset. Cisco customers receive the updates to the Subscriber Ruleset automatically and in real time. Non-Cisco customers can also receive updates to the Subscriber Ruleset by subscribing to the Snort service.
    
- **Community Ruleset:** Freely available, Snort community develops the rules, while Cisco Talos provides intelligence about the rules.


## Zeek

Passive network traffic analysis and a packet recorder. Zeek enables the security operations center (SOC) analysts to collect large quantities of data and aggregates raw data into formatted log files. 

Zeek comes with built-in functionality for a range of analysis and detection tasks, including extracting files from HTTP sessions, detecting malware by interfacing to external security intelligence sources, and reporting vulnerable versions of software seen on the network.

Not considered to be an IDS or IPS. A real-time network security monitoring (NSM) tool used to investigate the network activities. 

Supports IDS functionality (detection and alerting), and also provides its own scripting language to extend and customize its functionality. 
Scripting allows the SOC analysts to specify their custom detection methods. In this way, Zeek supports a wider range of different approaches to finding malicious activity, such as semantic misuse detection, anomaly detection, and behavioral analysis.

![9](/Course-Notes/.assets/Pasted_image_20241114122538.png)The main components of Zeek are:
	- Event Engine
	- Policy Script Interpreter
	- Event Handlers

When Zeek processes the packets, they first pass through the Event Engine, which aggregates the packets into events based on the protocol-specific information. The Event Engine contains the main data points about a communication flow.

Zeek events serve as an input to the Policy Script Interpreter, which makes decisions on whether the events are significant or potentially dangerous. 

The interpreter executes the Event Handlers (scripts), which are written in Zeek’s custom scripting language. The scripts reflect the security policy that defines which action to take on a certain event. You can configure the script to raise alarms to external systems and execute a piece of (external) software as an attack mitigation or response.

Zeek creates multiple log files in which it stores key information about the protocol exchange that was observed on the network. The most important is the connection log or conn.log file, which stores high-level information about the traffic crossing the network including:

- Source and destination IP addresses
- Which protocol and application created the connection
- When the conversation happened and how long it lasted 
- Packet and data statistics

Zeek also assigns a unique identifier (UID) field to each conversation so it can track related activity in other, more specific log files. SOC analysts often use the connection log as a starting point for an investigation. But when they need more data about a transaction, the SOC analysts must inspect the other more detailed log files created by Zeek. Each application protocol that Zeek observes and inspects has its own corresponding log file. For example, there is the dns.log file for the Domain Name System (DNS) transactions, the http.log file for the HTTP transactions, and so on. Each protocol log file contains relevant protocol-specific information. The common value across all log files is the UID, which links the specific protocol conversation back to the connection log.

Several other log files are not protocol-related, such as the files.log, which stores metadata about files transferred over networks. Zeek can also store the extracted files on a disk for further analysis.

#### Summery

Passive network traffic analysis and a packet recorder. 
aggregates data into formatted log files. 
provides its own scripting language
3 main components:
	- Event Engine (Collects raw Data)
	- Policy Script Interpreter (interperpates events)
	- Event Handlers (Executes appropriate scripts)
Uses UID to track conversations
Creates details logs containing:
	- Source and destination IP addresses
	- Which protocol and application created the connection
	- When the conversation happened and how long it lasted 
	- Packet and data statistics

## Suricata

Suricata is a free, open-source IDS/IPS

It offers native support for several protocols, such as HTTP, DNS, Transport Layer Security (TLS), and Server Message Block (SMB), even when operating over nonstandard ports. For example, Suricata will recognize HTTP even when someone is running an HTTP server on TCP port 8080.

Similar to the Snort engine because it performs packet-level inspection, or deep packet analysis, and is based on signatures or rules, which contain:
- Rule definition
- Header
- Action

![8](/Course-Notes/.assets/Pasted_image_20241114132314.png)
Suricata alerts include the timestamp, source and destination IPs, and the Suricata signature.

The rule definition contains the match conditions. The header may contain the protocol, source and destination IPs and ports, and the direction. The rule action controls what the rule does, such as dropping traffic or generating alerts.

Using Lua scripts, Suricata also supports advanced functionality to detect malicious activities, which is not possible within the Suricata ruleset syntax.

Suricata can run in several modes:

- Network security monitoring (NSM)
- Intrusion detection (IDS)
- Intrusion prevention (IPS), which must be in line with the traffic flow

Most deployments combine NSM and IDS modes, which require that the system receives a copy of the traffic in real time. Suricata logs store traffic flow information in the JSON format, which simplifies integration with the log aggregation functionality (SIEM).

# Building Blocks of Snort Rules
Snort rule is a set of keywords and arguments that the Snort engine uses to detect malicious activity on the network.

It is basically a piece of code that describes a state and an action to perform if that state is true. The goal is to determine if a certain packet differs from others in such a way that it is considered malicious.

Snort rules are single-line rules, but for better readability, you can use the backslash (“\”) character to split the rule into multiple lines. Snort rules reside in a rules file. A rules file can contain one or more rules.

Each Snort rule has two logical sections:
- **The rule header** contains information that defines the “who and where” of a packet. It also tells Snort what action to take when a packet has all the attributes that are indicated in the rule.
- **The rule body** contains the rule options that form the heart of the Snort intrusion detection engine, combining ease of use with power and flexibility.

![7](/Course-Notes/.assets/Pasted_image_20241114141638.png)
#### Rule Header:
The Rule Header consists of the following basic traffic definition:
- Action
- Protocol
- Source IP and Port 
- Operator
- Destination IP and Port

The rule header contains the action for the rule and the options to match the traffic that should be evaluated against the rule. The first field in the rule header is the action field. It tells the Snort engine what to do with traffic that matches the rule criteria.

- **Alert:** Generates an intrusion event.
- **Pass:** Allows the packet to pass without further evaluation of subsequent rules against the packet. It does not generate an intrusion event. Pass rules are evaluated first.
- **Drop:** Drops the packet, but subsequent packets in the connection are not dropped. Generates an intrusion event.
- **Block:** Drops the current matching packet and all the subsequent packets in the connection. Generates an intrusion event.
- **Reject:** Drops the packet and all subsequent packets in the connection. Sends TCP RST for TCP traffic or ICMP unreachable for UDP traffic to the source and destination hosts. Generates an intrusion event.
- **Rewrite:** Replaces the packet content based on the replace option in the rule. Generates an intrusion event

![6](/Course-Notes/.assets/Pasted_image_20241114142649.png)

The second field in the rule header is the protocol field. Snort currently supports analysis of TCP, UDP, ICMP, and IP.

Fields that follow the action and the protocol fields include the source parameters (IP addresses and ports), the direction operator, and the destination parameters (IP addresses and ports).

IP addresses and ports can be defined as literals or variables. Variable names start with the dollar symbol ("$"). Using variables is the preferred way of defining rules because it is more flexible and scalable.

The direction operator can be "->" and "<>". The "->" operator instructs Snort to inspect the traffic from source to destination and the "<>" operator instructs Snort to inspect the traffic in both directions.

#### Rule Body:
The rule body contains a list of rule options and is the core of the Snort intrusion detection engine. Understanding the format of the rule body is significant because it must adhere to a very specific syntax. The entire rule body with the different rule options is enclosed in parentheses, and each rule option ends in a semicolon (“;”). Each rule option is structured as a keyword followed by a colon (“:”) and arguments. If multiple arguments apply, the arguments are separated by commas (“,”).

There are four major categories of rule options:

- **General:** These options provide general information about the rule but do not affect detection, such as, for example, the message to display associated to the Snort rule (msg), the Snort ID (sid), and revision of the Snort rule (rev).

- **Payload:** These options look for data within the packet payload, for example, the content rule option will search for specific content in the packet payload.

- **Non-payload:** These options look for non-payload data. For example, the flow rule option allows a rule to only be applied to certain directions of the traffic flow.

- **Post-detection:** These options are rule-specific triggers that happen after the rule was matched. For example, the replace rule option is an inline feature which causes Snort to replace the prior matching content with some given string.

![5](/Course-Notes/.assets/Pasted_image_20241114142820.png)

At startup, the Snort engine first checks the syntax of all the rules. If it detects an error, it logs a warning into the syslog log file and does not start up. Any reported errors must be resolved before again attempting to start the engine.

![4](/Course-Notes/.assets/Pasted_image_20241114142840.png)

The figure shows another example of a Snort rule, components.

The rule header defines the rule to alert on specific TCP traffic going from the networks and ports, as indicated by the EXTERNAL_NET and HTTP_PORTS variables, and going to the networks indicated by the HOME_NET variable over any ports.

The rule body provides information on which specific traffic matches the rule. For example, the flow rule options specify that only established connections to the clients are inspected. The detection rule option specifies that the engine is looking for files that have parameters specified in the file data field. When such files are recognized, the Snort engine creates an alert with the message specified in the message rule option. This Snort rule has the sid 65535 and is rev 1.

# Cisco IPS Solutions
## Cisco Secure Firewall

Cisco Secure Firewall Threat Defense combines ASA, and Cisco Secure Firewall solutions under a single unified code base.

Adaptive Security Appliance (ASA), contributes classic firewall features, such as IP routing, Layer 3/Layer 4 ACL, site-to-site VPN, remote-access VPN, and Network Address Translation (NAT) functionality.

As a result of this convergence, Cisco Secure Firewall Threat Defense has next-generation Cisco Secure Firewall and IPS capabilities, providing clearer visibility, traffic control, and protection from threats to the network.

![3](/Course-Notes/.assets/Pasted_image_20241114160648.png)
**Cisco Secure Firewall Threat Defense - Key Features**

1. **Security Intelligence (SI) Feature**
	- Acts as the first line of defense using Cisco Talos intelligence.
	- Identifies and blocks known malicious IPs, URLs, and domain names automatically.
	- Reduces Snort engine workload by dropping flagged traffic immediately.

2. **URL Filtering**
	- Allows for blocking specific URLs or categories of websites.
	- Useful for preventing access to inappropriate or harmful sites.

3. **File and Malware Analysis**
	- Uses Cisco Secure Malware Analytics (formerly ThreatGRID) for sandboxed malware analysis.
	- Supports both on-box and cloud-based analysis for enhanced security.

4. **TLS/SSL Traffic Inspection**
	- Can inspect encrypted web traffic to block old or insecure protocols (e.g., SSL) and weak cipher suites.
	- Detects threats hidden within encrypted connections, like malware and data exfiltration.
	- Supports TLS/SSL decryption for inbound and outbound traffic, acting as a proxy to inspect connections thoroughly.

5. **Deployment Flexibility**
	- Available as a physical appliance or virtual machine.
	- Compatible with virtualization platforms (VMware vSphere, KVM) and public cloud services (Microsoft Azure, AWS).

This summary highlights the main capabilities of Cisco Secure Firewall Threat Defense, emphasizing its security intelligence, URL filtering, malware analysis, encrypted traffic inspection, and versatile deployment options.

Cisco Secure Firewall devices can be managed using:

- Cisco Secure Firewall Device Management (FDM), which is a single device manager

- Cisco Secure Firewall Management Center, which can manage multiple devices and can be implemented as a physical or virtual appliance    

- Cisco Defense Orchestrator, which is a cloud-based manager that can manage different types of devices such as Cisco Secure Firewall ASA, Cisco Secure Firewall Threat Defense, Cisco Meraki, Cisco Umbrella, and more.

- Cloud Delivered FMC

### Log4j Exploit Mitigation with Cisco Secure Firewall Threat Defense

In December of 2021, the security community disclosed the Log4j vulnerability of the Java-based logging library for the widely used Apache web server. Adversary exploits the Log4Shell vulnerability by submitting a specially crafted request to a vulnerable server that causes the server to execute malicious code. The malicious code causes the vulnerable server to connect back to the adversary controlled server over LDAP. The adversary then serves the malicious payloads to take full control of the vulnerable server to steal information, launch ransomware, or conduct other malicious activity.

The vulnerability was fairly simple to exploit and because the Apache web server is widely used, it received a Common Vulnerability Scoring System (CVSS) 3.0 base score of 10 (the highest possible), and CVSS 2.0 base score of 9.3. After disclosing the vulnerability, exploiting started immediately and the security community instructed web server administrators to patch vulnerable servers.

To mitigate new threats such as Log4j by using the intrusion policy, you could wait for Cisco Talos to release a new Snort rule for the new threat. Although Cisco Talos updates Snort rules quickly, a vulnerability of this scale must be acted upon very quickly. In a particularly critical environment, you could manually create a new Snort rule by using the security intelligence information gathered about the new threat.

For most organizations, LDAP is only used internally and it is not common for LDAP requests to be sent to servers on the internet. Another quick mitigation option for the Log4J threat is to define an access control policy rule to prevent outbound LDAP traffic to any server on the internet. You can apply the policy at least for the time that the web server administrators patch all the servers. If choosing this option, you must select LDAP as the application in the access control policy rule so the LDAP traffic can be detected over any ports. The attacker could be smart and obscure the LDAP server’s destination port, changing it to some random valid TCP port number. The attacker can also change the port regularly, preventing a classic Layer 3 or Layer 4 firewall to block the traffic based on the destination port.

The figure shows part of the Cisco Secure Firewall Threat Defense access control policy rule to block outbound LDAP connections to mitigate the Log4j vulnerability. Note that the selected application is LDAP and logging is enabled.

![2](/Course-Notes/.assets/Pasted_image_20241114171807.png)


## Cisco Umbrella Cloud Delivered Firewall

Cisco Umbrella comprises many different security services, including:
- Secure Web Gateway (SWG)
- cloud access security broker
- DNS layer security
- cloud-delivered firewall (CDFW)
- data loss prevention
- threat Intelligence

Cisco data centers in the cloud host all the Cisco Umbrella services. The customer's Cisco Umbrella administrators configure their Cisco Umbrella policies and perform all their monitoring via the centralized, web-based management console in the cloud.

![1](/Course-Notes/.assets/Pasted_image_20241114172009.png)

**Cisco Umbrella Solution Components**

1. **Secure Web Gateway (SWG)**:
	- Acts as an HTTP/HTTPS proxy.
	- Inspects and filters web traffic based on domain or category (URL filtering).

2. **DNS Layer Security**:
	- Functions as an upstream DNS server.
	- Blocks access to domains associated with malware, phishing, botnets, and other high-risk threats.

3. **Cisco Distributed Firewall (CDFW)**:
	- Provides visibility and control over client-to-internet traffic.
	- Supports rule-based blocking at Layers 3, 4 (IP, port, protocol), Layer 7 (application visibility and control), and IPS rules.
	- Logs all activity and blocks traffic based on defined firewall policies.
	- Traffic is forwarded to the CDFW through an IPsec tunnel between the network device and the Cisco Umbrella cloud.

**Traffic Flow in Cisco Umbrella**

1. **Traffic Initialization**:
	- LAN traffic reaches Cisco Umbrella via an IPsec tunnel from an on-premises device (router or firewall) to the Cisco cloud.
	- Traffic is encrypted over the internet to secure the connection.

2. **Decryption and DNS Resolution**:
	- Upon reaching Cisco Umbrella, the traffic is decrypted.
	- DNS resolver checks the domain for malicious or restricted content per DNS policy.
	- Approved traffic moves to the CDFW for further inspection.

3. **CDFW Filtering**:
	- CDFW blocks or allows traffic based on firewall policies.
	- Permitted web traffic then proceeds to SWG for web-specific inspection.

4. **SWG Inspection (Web Traffic Only)**:
	- SWG examines approved web traffic per the Web Policy.
	- It decides to accept or drop traffic based on the content filter.

5. **Network Address Translation (NAT)**:
	- Approved traffic is sent to NAT, which replaces the original source address with the Cisco Umbrella address.
	- Ensures return traffic re-enters Cisco Umbrella for reverse inspection before reaching the source.

6. **Non-Web Traffic Handling**:
	- Non-web traffic allowed by CDFW bypasses SWG and proceeds directly to NAT processing.

This outline captures how Cisco Umbrella utilizes DNS filtering, firewall policies, and secure web filtering in tandem to control and secure internet-bound traffic.

# Summary
- Describe and differentiate between intrusion detection and intrusion prevention.
- Explain detection rules.
- Differentiate between rule-based and anomaly-based intrusion detection.
- Describe Snort, Zeek, and Suricata detection solutions.
- Describe the structuring of a Snort rule and rule elements.
- Describe how to mitigate a high-risk threat using Cisco Secure Firewall Threat Defense.
- List Cisco IPS solutions and describe their features.

