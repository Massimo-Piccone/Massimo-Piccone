%% #review [[Malicious Activity Review]] [[Tools Review]] [[Tactics Review]]%%
# [[NetFlow Log]]

>- A network protocol for collecting and monitoring network traffic flow data.
>- Captures session data, including system identities, communication time, and data transferred.

| Feature           | Description                                                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Support           | ==Widely adopted and supported== by various platforms beyond Cisco.                                                                       |
| Capabilities      | Provides information about ==network conversations==, similar to how a phone bill details voice conversations.                            |
| Limitations       | Cannot determine the specific content of network traffic, similar to how a phone bill ==doesn’t reveal the actual conversation details==. |
| Provides          | a 24x7 view of all network communications, acting as a complete ==audit trail==.                                                          |
| Application       | Used for network ==diagnostics==, ==maintenance==, and security ==analysis==.                                                             |
| Benefits          | ==Identifies anomalous activity== and reconstructs events during security incidents.                                                      |
| Role              | Augments security controls in a ==defense-in-depth== approach.                                                                            |
| Malware Detection | Provides valuable ==data for detecting malware==, including zero-day threats.                                                             |
| Importance        | Critical for ==detecting APTs== and conducting ==post-incident forensic== analysis.                                                       |
| Security Analysis | Uses behavioral analysis and ==pattern recognition== to detect undocumented attack vectors.                                               |
| Attack Detection  | Enables ==early detection== of attacks in the attack lifecycle.                                                                           |

| Feature            | Description                                                                      |
| ------------------ | -------------------------------------------------------------------------------- |
| Perimeter Controls | Ineffective against insider threats.                                             |
| Detection          | Identifies signs of insider attacks in progress, such as unusual data transfers. |
| Standards          | NetFlow (evolved into IPFIX) developed by Cisco.                                 |
| Versions           | Nine versions of NetFlow released.                                               |
| Current Version    | IPFIX.                                                                           |

| **Version** | **Status**                                                                                   | **Key Features**                                                                                               |
|-------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **v5**      | Most commonly deployed version today, only supports IPv4                                      | - Supports IPv4 traffic<br>- Fixed flow format<br>- Basic traffic monitoring and reporting                     |
| **v9**      | Next-generation flow formatting that supports IPv6, MPLS, and multicast                      | - Supports IPv6, MPLS, and multicast<br>- Flexible flow template structure<br>- More advanced traffic analysis |
| **v10**     | IPFIX, the industry standardized version of v9                                               | - Standardized by IETF<br>- Supports IPv6, MPLS, and multicast<br>- Extensible and customizable flow export     |
![15](/Course-Notes/.assets/Screenshot_2024-11-23_at_10.53.42.png)
### Netflow v9
- ==Output==: Flow records in various formats, with NetFlow version 9 being the most recent and template-based.
- ==Template-Based Format Advantage==:Enables future enhancements without changing the basic flow-record format.

- ==Deep Packet Inspection== (v9 v10): identify applications within network traffic, enabling deeper inspection of network sessions.
- ==Malicious Traffic Detection==: These technologies can detect malicious code using port 80 for tunneling command-and-control traffic.
- ==Flow Data Enhancement==: Advanced NetFlow analysis systems can include application information in flow data for enhanced analysis.

Some of the most commonly used data elements that are generated by NetFlow include the following:
- Source IP address
- Destination IP address
- Source port
- Destination port
- Protocol
- Time stamps for the flow start and conclusion
- Amount of data passed

| Aspect                       | Description                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------- |
| NetFlow Data Requirement     | Needs a collector and an analysis engine to store and correlate the data.                                |
| NetFlow Analysis Tools       | Cisco Stealthwatch is an example, and many other tools, including freeware options, are available.       |
| Security Tool Utilization    | NetFlow data can help determine the state and scope of a compromise.                                     |
| Flow Definition              | A unidirectional series of packets between a source and a destination.                                   |
| Flow Identification          | Determined by the five-tuple: source IP, destination IP, source and destination ports, and IP protocols. |
| Flow Example                 | HTTPS one-way communication flow.                                                                        |
| NetFlow Security Benefit     | Anomaly detection and historical investigation capabilities.                                             |
| NetFlow Data Usage           | Correlate traffic activity from/to a device and compare timestamps against other logs.                   |
| NetFlow User                 | Security analysts.                                                                                       |
### IPS vs NetFlow

| Feature                          | NetFlow Analysis                     | IPS                    |
| -------------------------------- | ------------------------------------ | ---------------------- |
| Focus                            | Metadata analysis                    | Deep packet inspection |
| Application Awareness            | No                                   | Yes                    |
| Network Awareness                | No                                   | Yes                    |
| Behavior Baseline Identification | No                                   | Yes                    |
| Analysis                         | No                                   | Yes                    |
| Data Capture                     | Metadata about network conversations | Actual packet data     |

| **Feature**               | **NetFlow**                                              | **IPS (Intrusion Prevention System)**                            |
|---------------------------|----------------------------------------------------------|------------------------------------------------------------------|
| **Detection of Threats**   | Flow analysis                                            | Inline protection to drop offending traffic                      |
| **Network Traffic Analysis** | Analyzes network flow data (e.g., source/destination, ports) | Deep file and application inspections                           |
| **Deployment**             | Collectors receive flow information from exporters (network devices) | Inline placement within the network to actively block threats    |
| **Privacy**                | Looks at header-level information                        | Inspects files and applications deeply, potentially exposing sensitive data |
| **Storage**                | Fewer storage requirements, can be stored for years for forensic investigations | Requires large storage, especially for packet capture related to IPS alerts |
| **Host-based Analysis**    | Based on network flows, no client agents required        | Requires host-based IPS application running on the host         |

| Component                             | Description                                                                             |
| ------------------------------------- | --------------------------------------------------------------------------------------- |
| Stealthwatch Management Console (SMC) | GUI-based console for aggregating, organizing, and presenting network traffic analysis. |
| Flow Collector                        | Receives and stores NetFlow data.                                                       |
| Flow Sensor                           | Collects NetFlow data from network devices.                                             |

| Feature                                    | Description                                                                                                                                    |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| IPS Integration                            | Can block attacks when inline with traffic and provides context for IPS signatures when combined with NetFlow.                                 |
| Security Analyst Advantage                 | Offers context for triggered IPS signatures.                                                                                                   |
| NetFlow Data Sources                       | Traditional networking and security devices, and special-purpose NetFlow collection appliances.                                                |
| NetFlow Data Access Challenges             | Security analysts might face difficulties accessing NetFlow data due to device limitations, access restrictions, or performance concerns.      |
| Alternative Data Collection                | Dedicated NetFlow exporters can be utilized to collect and export flow information, potentially enhanced with application performance metrics. |
| NetFlow Exporter Integration               | These devices can be integrated into the network using methods like SPAN or Ethernet TAP.                                                      |
| NetFlow Configuration                      | Enable NetFlow collection on network devices and direct data to a NetFlow collector.                                                           |
| Cisco Stealthwatch Management Center (SMC) | A GUI-based console for aggregating, organizing, and presenting network traffic analysis.                                                      |
| SMC Features                               | Provides graphical representations, user identity information, customized reports, and integrated security and network intelligence.           |
![14](/Course-Notes/.assets/Pasted_image_20241123025001.png)
### Flow Stitching 
![13](/Course-Notes/.assets/Pasted_image_20241123025144.png)

| Component | Description                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------------- |
| Purpose   | Reconstructs the full network session by combining two unidirectional flow records generated by NetFlow. |
| Process   | Flow collector combines two flow records representing the same network session.                          |
| Benefit   | Provides analysts with a complete view of each network connection.                                       |
### Flow Deduplication 
![12](/Course-Notes/.assets/Pasted_image_20241123025303.png)

| Feature    | Description                                                                      |
| ---------- | -------------------------------------------------------------------------------- |
| Purpose    | Remove duplicate network connection records captured by multiple flow exporters. |
| Location   | Performed by flow collectors before security analysis.                           |
| Importance | Ensures accurate and reliable security analysis of network flows.                |
### NAT Stitching
![11](/Course-Notes/.assets/Pasted_image_20241123025348.png)

| Feature  | Description                                                           |
| -------- | --------------------------------------------------------------------- |
| Function | Unify NAT information from inside and outside the firewall.           |
| Purpose  | Pinpoint which IPs and users are responsible for a particular action. |
## References

For additional information, refer to these resources:

- Santos, Omar, _Network Security with NetFlow and IPFIX,_ Cisco Press 2016

- Chapple, Mike, Ph.D., _NetFlow Security Monitoring for Dummies_, John Wiley & Sons, Inc., 2012

- Cisco White Paper: _Network as a Security Sensor_ [http://www.cisco.com/c/en/us/solutions/collateral/enterprise-networks/enterprise-network-security/white-paper-c11-736595.pdf](http://www.cisco.com/c/en/us/solutions/collateral/enterprise-networks/enterprise-network-security/white-paper-c11-736595.pdf)

# NetFlow as a Security Tool

| Feature         | Description                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Uses            | Examines IP flows across the entire enterprise network, capturing IP 5-tuple information, communication time, and data transferred. |
| Benefits        | Understand who, what, where, how, and when regarding each IP flow.                                                                  |
| Target Audience | Analysts responsible for maintaining visibility and security within the enterprise network.                                         |
![10](/Course-Notes/.assets/Pasted_image_20241123025912.png)
- **Where:** Gi0/0/0 (network device input interface), Gi0/1.20 (network device output interface).
- **How:** 1482 (traffic bytes count), 23 (traffic packet counts).
- **When:** 12:33:53.358 to 12:33:53.370.
## Network as a Sensor
Typically, the following security controls are implemented in most enterprise networks:

- Firewall
- Intrusion prevention system
- Web and email proxy
- Anti-virus/anti-malware
- Identity and access management

| Security Challenge                                                                   | Security Solution Requirements                                       | Cisco Stealthwatch Functionality                                                                                  | Threat Detection Capabilities                                                                |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| DDoS attack with legitimate traffic                                                  | Anomaly detection, behavior analysis, and baselining for the network | Provides complete visibility into network activity by analyzing NetFlow, IPFIX, and other network telemetry data. | Detects a wide range of threats including APTs, DDoS, zero-day malware, and insider threats. |
| User downloads 100 Gb of data in one day, significantly more than their usual 10 Mb  | ""                                                                   | ""                                                                                                                | ""                                                                                           |
| User connects to the corporate LAN with a zero-day malware                           | ""                                                                   | ""                                                                                                                | ""                                                                                           |
| Insider steals proprietary information by tunnelling it out through another protocol | ""                                                                   | ""                                                                                                                | ""                                                                                           |
![9](/Course-Notes/.assets/Pasted_image_20241123031630.png)

| Feature                 | Description                                                                                          |
| ----------------------- | ---------------------------------------------------------------------------------------------------- |
| Network Visibility      | Broad and deep visibility into network IP traffic flow patterns.                                     |
| Threat Intelligence     | Provides rich threat intelligence information.                                                       |
| Data Capture            | Uses NetFlow to capture comprehensive session data and metadata related to IP flows.                 |
| Threat Identification   | Utilizes captured data to identify security threats more rapidly.                                    |
| NetFlow Version 5       | Fixed-format data structure with 18 data elements, unable to expand.                                 |
| NetFlow Version 9       | Fixed-field format with 108 data elements, utilizing template-based FlowSet for flexibility.         |
| Flow Record Structure   | NetFlow versions 5 and 9 employ fixed-field formats for data records.                                |
| NetFlow Importance      | Critical for network security by identifying anomalous traffic.                                      |
| NetFlow Functionality   | Provides visibility into network traffic and enables baseline creation for anomaly detection.        |
| Security Benefit        | Alerts on traffic deviating from the established baseline, indicating potential security issues.     |
| NetFlow Data Source     | NetFlow data is exported from various network devices across the enterprise network.                 |
| Analytics Scope         | Provides visibility across the entire enterprise network, including branch offices and data centers. |
| Data Export Destination | NetFlow data is exported to a centralized NetFlow analytics system.                                  |
## NetFlow as Security Tool Examples
Cisco Stealthwatch, which shows a summary of the conversation between two hosts:
![8](/Course-Notes/.assets/Pasted_image_20241123031736.png)
- Unusual Traffic Behavior: A client host in Atlanta is tunneling a large amount of peer-to-peer traffic over UDP port 53 to a destination server in Puerto Rico.
- Traffic Type: Peer-to-peer traffic.
- Traffic Duration: 6 minutes and 1 second.

| Note                           | Description                                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Host Grouping                  | Hosts can be grouped by business unit, client function, location, responsibility, or a combination of these factors.            |
| Geolocation                    | Cisco Stealthwatch performs geolocation lookup of IP addresses to determine country information.                                |
| Future Investigation           | Analyze recent network traffic activities from the same client host for other anomalies.                                        |
| Packet Capture Analysis        | Examine the packet capture of DNS traffic to determine the content of tunneled peer-to-peer traffic.                            |
| NetFlow Detection              | NetFlow can detect network traffic activities that are 1 hour apart from two locations several hundred miles apart.             |
| Suspicious User                | The analyst may suspect something suspicious about the ethel user.                                                              |
| Further Investigation          | The analyst should perform future investigations into all the recent network traffic activities from the ethel user.            |
| Cisco Stealthwatch Integration | Integrates with Cisco Identity Services Engine (ISE) to correlate data and build a more complete picture of network activities. |
| Data Correlation               | Correlates username to IP address-mapping information from Cisco ISE with NetFlow data.                                         |
| Benefit                        | Provides a context-aware view of network activities by associating usernames with IP addresses in NetFlow records.              |
![7](/Course-Notes/.assets/Pasted_image_20241123031906.png)
![6](/Course-Notes/.assets/Screenshot_2024-11-23_at_10.53.09.png)
# Network Behavior Anomaly Detection

| Use Case                              | Description                                                                                               |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Signature-based Detection Limitations | Advanced attackers can craft innovative attacks that bypass signature-based defenses.                     |
| Cisco Netflow Solution                | Use baselines to identify threats that bypass conventional signature-based defenses.                      |
| NetFlow Analysis                      | Detects both known and unknown threats by identifying anomalous behaviors in network traffic.             |
| Baselines & Anomalies                 | digests historical network traffic to establish norms and alerts when there are any deviations to trends. |
| PCI Compliance Mapping                | Map relationships between PCI components like point-of-sale machines and payment processing systems.      |
| Traffic Behavior Baseline             | Baseline traffic behaviors between PCI components using NetFlow.                                          |
| PCI Concerns Addressing               | Address PCI concerns by analyzing traffic patterns and identifying potential vulnerabilities.             |
Server activities can be baselined using different behaviors under normal conditions.
![5](/Course-Notes/.assets/Pasted_image_20241123111154.png)

| Challenge                                                                              | Solution                                                                                                                                                        |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Detecting abnormal network traffic accurately while minimizing computational overhead. | Using a sliding time window for baseline calculation to limit anomaly detection to a specific time scope, reducing data analysis and improving detection speed. |
| Baseline Selection                                                                     | The baseline should be chosen carefully to reflect the current network behavior, avoiding outdated data that could distort the perception of normalcy.          |
# Data Loss Detection Using NetFlow Example

- ==Data Accessibility Risk==: Data stored on corporate networks is at risk due to increased accessibility.
- ==Data Sharing and Storage==: Organizations provide easy access to databases for information sharing and storage.
- ==Data Mobility==: Advanced storage and compression technology enables easy movement of data across devices, increasing the risk of data loss or theft.

| Data leakage sources                    | Consequences                 |
| --------------------------------------- | ---------------------------- |
| A disgruntled employee                  | ==Data Breach:==             |
| An employee about to leave the company  | Undermine brand              |
| A person who has privileged credentials | Jeopardize competitive edge  |
| Cybercriminals                          | ==Regulatory Breach:==       |
|                                         | Reduce customer confidence   |
|                                         | Lead to fines                |
|                                         | ==Data at Risk:==            |
|                                         | Intellectual property        |
|                                         | Financial data               |
|                                         | Merger and acquisition plans |
|                                         | Sensitive customer data      |
### Cisco Stealthwatch Management Center 
>Java-based GUI to detect and investigate data loss incidents.

Data loss dashboard:
- Displays data transfer activity between inside and outside networks. 
- Provides information on data loss alarms, trends, and associated host information.

Viewing user network activities quickly involves checking triggered alarms. For instance, the Trend of Data Loss Alarms graph is visible on the top-right corner of the dashboard.

![4](/Course-Notes/.assets/Pasted_image_20241123114501.png)
From this graph, the analyst can see the various data loss alarms occurring on the different dates. In this example, the analyst will examine some suspicious data loss activity on 11/18/15.
![3](/Course-Notes/.assets/Pasted_image_20241123114510.png)

| Feature              | Description                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Traffic Monitoring   | Cisco Stealthwatch monitors outbound traffic from inside hosts to establish a baseline.                            |
| Data Loss Alarm      | The system triggers an alarm when data loss exceeds a predefined threshold.                                        |
| Alarm Details        | Analysts can view specific details of data loss alarms, including the source host and the amount of data involved. |
| Geolocation Analysis | Can convert IP addresses to corresponding countries and identify suspicious data transfer destinations.            |
# [[DNS Risk and Mitigation Tool]]

- ==DNS Functionality==: Correlates IP addresses to domain names and organizes the Internet into a hierarchy.
- ==DNS Vulnerability==: Can be used by threat actors for malicious activities due to its ubiquitous nature.
- ==DNS Record Updates==: DNS records are continuously updated due to the constantly changing nature of the Internet.

- ==DNS Poisoning==: Threat actors intercept DNS requests and redirect traffic to malicious websites.
- ==Data Exfiltration==: Threat actors tunnel sensitive data within DNS traffic or use DNS TXT records to exfiltrate information.
- ==Data Reconstruction==: Threat actors reassemble DNS TXT records to retrieve exfiltrated data, such as documents or credentials.

The figure below shows part of a PCAP. As an analyst, if you see this PCAP, should you be suspicious about these DNS queries.

![2](/Course-Notes/.assets/Pasted_image_20241123122852.png)

| Category                    | Description                                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ==DNS Query==               | DNS queries contains encoded information.                                                                                 |
| ==Content==                 | Credit card numbers are encoded in hexadecimal format within DNS queries.                                                 |
| ==DNS Traffic Monitoring==  | Monitoring deviations from the baseline DNS traffic is crucial to detect potential data exfiltration using DNS tunneling. |
| ==DNS Tunneling Detection== | An increase in DNS traffic or numerous requests to a single suspicious domain may indicate DNS tunneling.                 |
| ==Baseline Importance==     | A behavioral traffic baseline helps analysts identify unusual DNS activities that might otherwise go unnoticed.           |

| Technique                       | Description                                                                                                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DGA                             | Malware generates a large number of domain names daily.                                                                                                                                       |
| - Domain Registration Strategy  | Cybercriminals register only a few of the possible generated domains.                                                                                                                         |
| DNS Traffic Manipulation        | Malware directs botnet DNS traffic to cybercriminal-owned recursive DNS servers.                                                                                                              |
| DNS Traffic Analysis            | Analyzing large volumes of DNS traffic helps create a baseline profile for expected behavior.                                                                                                 |
| DNS Allowed/Blocked Lists       | Creating lists of legitimate and suspicious DNS requests aids in identifying anomalies.                                                                                                       |
| Abnormal DNS Packets            | Tracking abnormally sized packets, such as those with unusually long labels or hostnames, can indicate suspicious activities.                                                                 |
| DNS Tunnelling Expectation      | Tunnelling requests may have long labels of up to 63 characters, and contain long names up to 255 characters.                                                                                 |
| **Defensive Measures**          | Utilize Cisco FirePower DNS Inspection Policy for monitoring and blocking connections based on site/domain reputation.                                                                        |
| - DNS Sinkhole                  | Implement a DNS sinkhole or DNS response policy zone, to prevent attacks or reroute suspicious DNS queries for analysis.                                                                      |
| - Domain Registrar Verification | Confirm the legitimacy of a DNS request by verifying the domain registrars using resources like [domaintools.com](http://domaintools.com/) or [avgthreatlabs.com](http://avgthreatlabs.com/). |
| - Suspicious registrars         | Malware authors will use registrars with [weak or non-existent enforcement policies](https://www.spamhaus.org/statistics/registrars/)).                                                       |
# [[The Onion Router]]

[The Onion Router (Tor)](https://2019.www.torproject.org/index.html.en) is 
- Open Source software
- Open network that enables 
- Anonymous communications
Usage: 
- Used globally, especially in censored regions and by those seeking privacy.
Built for:
- Dissidents, individuals in repressive regimes, and anyone wanting to keep their browsing private.

- ==Access Method==: Users access the Tor network through the Tor browser.
- ==Browser Functionality==: The Tor browser routes web traffic through the Tor network instead of directly to websites.
- ==Network Composition==: Thousands of servers (Tor relays) owned and maintained by individuals, universities, companies, and so on.

## Tor Relays

- ==Malware Communication==: Many malware variants use Tor to communicate with CnC servers.
- ==Attacker’s IP Address Hiding==: Tor client hides the attacker’s IP address, making it appear as if the connection originates from a Tor exit relay.

Tor Network:
- ==Structure==: Composed of thousands of relays operated globally, forming a random pathway for data packets.
- ==Data Transmission==: Data packets traverse three relays, obscuring the origin and destination of the data.
- ==Tor Client Functionality==: Tor clients, like the Tor browser, utilize the Tor network to anonymize internet traffic.
![1](/Course-Notes/.assets/Pasted_image_20241124130631.png)

| Tor Relay Type         | Description                                                           |
| ---------------------- | --------------------------------------------------------------------- |
| **Guard relay (OR1)**  | The first relay in a Tor circuit.                                     |
| **Middle relay (OR2)** | The second relay in a Tor circuit, between the guard and exit relays. |
| **Exit relay (OR3)**   | The final relay before reaching the destination server.               |
| **Bridge**             | A relay not publicly listed on the Tor network.                       |

Path Creation:
3 stages, 3 Random relays, 
Independently TLS encrypted.

| Layer        | Description                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------- |
| First layer  | Data is encrypted with the symmetric key (SK3) matching the exit relay.                         |
| Second layer | Data is re-encrypted with the symmetric key (SK2) matching the middle relay.                    |
| Third layer  | Data is encrypted with the symmetric key (SK1) matching the first relay node, the “guard” node. |

| Step         | Description                                                                                                                                                                                                                                  | Visibility                                                                              |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Tor Browser  | Sends a triple-encrypted payload through the circuit.                                                                                                                                                                                        | Adversaries can only see encrypted traffic going to the Tor relay, not its destination. |
| Guard Relay  | Decrypts the first layer using its symmetric key (SK1) and forwards the double-encrypted payload with the next destination.                                                                                                                  | Adversaries can only see traffic coming from the Tor exit relay, not its origin.        |
| Middle Relay | Decrypts the second layer using its symmetric key (SK2) and forwards the single-encrypted payload with the next destination.                                                                                                                 | Adversaries cannot trace the origin or destination of traffic through the Tor network.  |
| Exit Relay   | Decrypts the final layer using its symmetric key (SK3) and sends the fully decrypted payload to the destination server. If the Tor browser and destination server use a further layer of encryption, the exit relay can’t read the messages. | Adversaries cannot trace the origin or destination of traffic through the Tor network.  |
## Detecting Tor Traffic

| Component                                                          | Description                                                                                                                                                 |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Directory Nodes                                                    | Each controlled by a different organization.<br>Active relay status is known to Directory nodes.<br>Track and publicize the state of the Tor network.       |
| Security Intelligence Feeds                                        | Often have a list of the current Tor relays & IP address.                                                                                                   |
| [Relay Search Tool](https://metrics.torproject.org/rs.html#simple) | Tor Metrics site can search for the relays IP address.<br>Displays data about the relays and bridges.<br>Configuration information, and graphs about usage. |
Cisco Security Intelligence feed.
- Includes Tor Exit Relay IP Addresses.
- used to Block Tor Connections in NGFW by setting `Tor_exit_node category` in the Blacklist column.
- Cisco Stealthwatch, using NetFlow and security intelligence data, can also detect communications with Tor guard relays and exit relays.

# [[Peer-to-Peer Networks]]

## [BitTorrent Application](https://en.wikipedia.org/wiki/BitTorrent)

- ==BitTorrent Functionality==: A P2P file sharing application that enables users to send or receive files.
- ==BitTorrent Tracker==: Provides a list of available files and facilitates connections with peers for file transfer.
- ==BitTorrent Protocol==: Allows users to download files from multiple sources simultaneously, creating a “swarm” of hosts.
- ==File Distribution==: The file is divided into pieces, with each peer receiving and distributing a piece.
- ==Data Integrity==: Cryptographic hashes protect pieces from accidental or malicious modifications.
- ==File Transfer==: Pieces are downloaded non-sequentially and rearranged by the BitTorrent client.
- ==Traffic Throttling==: More ISPs and companies are limiting and throttling BitTorrent traffic.
- ==BitTorrent Anonymization==: BitTorrent clients anonymize and encrypt BitTorrent traffic to avoid detection and throttling.

## [Risks of P2P File Sharing](https://www.us-cert.gov/ncas/tips/ST05-007)

- ==Trusting strangers== in a P2P network without knowing if downloaded files contain malware, pirated software, copyrighted material, or pornography.

- ==Unauthorized access== and sharing of sensitive personal files, leading to liability for both the P2P user and the company.

- Denial of service (==DoS==) when downloading large files, causing significant network traffic.

- ==Attackers gaining== access to the P2P user’s computer through port opening requests, vulnerabilities in P2P applications, or firewall modification.