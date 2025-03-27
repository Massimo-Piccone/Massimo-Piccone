%% #review%%
# [[Understanding the Network Design]]

| **Category**                    | **Key Point**                           | **Description**                                                                                         |
|----------------------------------|-----------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Network Topology & Asset Management** | **Network Topology Understanding**     | SOC analysts must understand network layout, including critical assets and ingress/egress points.        |
|                                  | **Obtaining Network Topology Map**      | Obtain a network topology map identifying all network-connected devices.                                 |
|                                  | **Vulnerability Assessment**           | Inquire about obtaining a vulnerability assessment or conducting a scan if one is not available.         |
|                                  | **Network Inventory Request**          | Request a list of all network-based appliances (routers, firewalls, switches, storage devices).           |
|                                  | **Critical System Inventory Request**  | Request a report on the location and identity of critical Windows/Linux host systems.                    |
|                                  | **Asset Categorization**               | Categorize network assets by priority (critical, important, sensitive) to prioritize threat responses.    |
| **Threat Response & Prioritization** | **Threat Prioritization**              | Prioritize threat responses based on asset location and importance, with a focus on internal and financial assets. |
|                                  | **Example Scenario**                   | A compromised web server in the DMZ poses a lower risk than a compromised internal system in a sensitive department like Accounting/Payroll. |
| **Device & Data Logging**        | **Device Location Identification**      | Identify physical locations of security-related devices (IPS/IDS, firewalls, Active Directory servers).    |
|                                  | **Data Logging Output Understanding**   | Understand the data logging output from identified devices to properly assess and respond to threats.     |

# [[Log Data Search]]

Formats 
Security Onion server:
```
Jan  6 07:37:01 so CRON[22073]: (root) CMD (find /var/www/so/capme/pcap/*.pcap -mmin +5 -delete >/dev/null 
2>&1)
```

CISCO IOS syslog message format:
```
seq no:timestamp: %facility-severity-MNEMONIC:description
```

| **Date + Time**                 | Timestamp of the message or event.                                              |
| ------------------------------- | ------------------------------------------------------------------------------- |
| **Facility Definition**         | Represents the source/cause of a system message (hardware, protocol, software). |
| **Facility Codes**              | Defined in RFC 3164 [RFC 3164](https://www.ietf.org/rfc/rfc3164.txt).           |
| **Examples of Facilities**      | SNMP, SYS, etc.                                                                 |
| **Message Severity**            | Single-digit code (0-7); 0 = most severe, 7 = least severe.                     |
| **Message Identification**      | MNEMONIC text string uniquely identifying the message.                          |
| **Log Content**                 | Text string with detailed information about the reported event.                 |
| **Search Engine Functionality** | Allows powerful queries across large data volumes (like Google).                |
### ELSA Syntax

| **Search Operators** | Boolean, range, and directives for isolating data. |
| -------------------- | -------------------------------------------------- |
| Keyword              | Query **must** include the keywords                |
| -Keyword             | Query **must not** include the keyword             |
| OR Keyword           | Query **may** include the keyword                  |

```
class=BRO_HTTP “-“ site:www.cisco.com –host>10.10.6.10 –host<10.10.6.20
```
The above example constructs a search between hosts (only hosts whose IP addresses fall between 10.10.6.10 and 10.10.6.20) that went to http://www.cisco.com.

```
72.163.4.161 sig_msg:"NETAPI Exploit" groupby:dstip
```
- ==Directive Example==: groupby:dstip groups by destination IP address.
- Analysts can review IDS alerts, such as those from Sguil, to identify suspicious activity.

## Modelling Network Attacks

| **Key Concept**                      | **Details**                                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------- |
| **Malicious Attack Assessment Goal** | Develop a hypothetical attack model based on learned knowledge of each attack event.               |
| **Malicious Activity Behavior**      | Helps analysts hypothesize how the attack will likely proceed over time.                           |
| **Malicious Activity Type**          | Indicates the intended strategy of the threat actor.                                               |
| **Attack Model Classification**      | Can be deterministic or probabilistic, affecting the analytical method used.                       |
| **Analyst’s Role**                   | Constructs models to predict future actions and outcomes based on attack progression.              |
| **Data Sources**                     | Host-based event logs and IPS-detected network attack events.                                      |
| **Deterministic Assessment**         | Relies on known data to produce a single outcome with minimal speculation.                         |
| **Probabilistic Assessment**         | Considers a range of scenarios, providing possible outcomes with less accuracy due to speculation. |
# [[Zero Trust Model]]

![7](/Course-Notes/.assets/Pasted_image_20241121141546.png)
## Zero Trust Workforce Protections

>Only authorized users can access required work applications from any location.

![6](/Course-Notes/.assets/Pasted_image_20241121141620.png)

- Users access work applications using secured personal or corporate-managed devices.
- Multifactor authentication is crucial for securing the workforce.
## Zero Trust Workload Protections

>Ensures secure access for APIs, microservices, and containers accessing applications in cloud, data centers, and virtualized environments. Secure interacting workloads.
>==Goal==: Secure access when workloads interact with each other.

![5](/Course-Notes/.assets/Pasted_image_20241121141702.png)

| **Key Concept**                | **Details**                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Definition                     | Ensures secure access for APIs, microservices, and containers in cloud, data centers, and virtualized environments. |
| Goal                           | Secure access when workloads interact with each other.                                                              |
| **Data Center Infrastructure** | Hybrid multicloud infrastructure using bare-metal, virtualized, and container-based workloads.                      |
| **Workload Definition**        | Compute stack, associated application, and requests made to the application, running in various environments.       |
| **Cloud Workload Prediction**  | Cisco estimates 94% of workloads will run in cloud environments by 2021, with 6% in traditional data centers.       |
### Challenges

| **Challenges in Dynamic Environment** |                                                                                                                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - Insufficiency                       | Static perimeter-based security model in data centers is insufficient for current technology.                                                                     |
| - Lack of Ability                     | Difficulty in generating and managing policies for segmentation based on application behavior.                                                                    |
| - No Consistent Approach              | No uniform method for implementing segmentation with allowed lists across multicloud infrastructures.                                                             |
| - Lack of Comprehensive Approach      | Inadequate approach to reduce attack surface, minimize lateral movement, and detect behavior deviations.                                                          |

| **Key Concept**            | **Details**                                                                                                                                                       |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Platform Functionality** | Cisco Tetration uses traffic telemetry data to provide comprehensive workload protection for multicloud data centers.                                             |
| **Platform Features**      | Secures hybrid multicloud workloads, contains lateral movement with application segmentation, and provides visibility into database and application dependencies. |
| **Platform Purpose**       | Designed to address challenges in multicloud data centers.                                                                                                        |
## Zero Trust Workplace Protections

>Ensures secure access for any devices connecting to enterprise networks.
>==Goal==: Secure all user and device connections across the network, including IoT.

![4](/Course-Notes/.assets/Pasted_image_20241121141901.png)

- ==Zero Trust Model Mechanism==: Grant access only to authorized users, devices, and workloads after establishing trust and preventing threats.
- ==Cisco SD-Access Functionality==: Provide insight into users and devices, identify threats, and maintain control over all network connections, including IoT devices.

## Zero Trust Model Security Vision

>Integrating various security solutions to secure the workplace, workload, and workforce.

- ==Zero Trust Model Benefits==: Provides better visibility, reduces attack surface, and offers a consistent and productive security experience for users.
- ==Zero Trust Model Mechanism==: Requires verification of security states for every access request, segments resources, and limits permissions and traffic.

# Linux [[System Logs]] 

Linux systems offer comprehensive logging for system events and application events.
Logging Process is handled by `syslogd` or its variant `rsyslogd`, with additional functionality.

| **Key Concept**             | **Details**                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| **Log File Location**       | Primary log file is typically `/var/log/messages` or `/var/log/syslog`, but the configuration file determines the exact files used. |
| **Logging Options**         | Logs can be sent to the console, forwarded to a remote syslog server, or aggregated to a central location for analysis. |
| **rsyslogd Configuration**  | The `rsyslogd` configuration file lists all the files used for logging and can be customized based on specific event types. |
## Configuring Syslog

|Log Facility/Severity|Log File Path|
|---|---|
|`auth,authpriv.*`|`/var/log/auth.log`|
|`*.*;auth,authpriv.none`|`-/var/log/syslog`|
|`cron.*`|`/var/log/cron.log`|
|`daemon.*`|`-/var/log/daemon.log`|
|`kern.*`|`-/var/log/kern.log`|
|`lpr.*`|`-/var/log/lpr.log`|
|`mail.*`|`-/var/log/mail.log`|
|`user.*`|`-/var/log/user.log`|
## Selector Syntax

(facility)==.==(severity)
- Facility == the component reporting the event.
- Severity == a priority for the event.

| Level    | Description                                   |
| -------- | --------------------------------------------- |
| 1:Debug  | Debug information from running processes.     |
| 2:Info   | Simple informational messages.                |
| 3:Notice | A condition that may require some attention.  |
| 4:Warn   | A warning.                                    |
| 5:Err    | An error condition                            |
| 6:Crit   | A critical condition                          |
| 7:Alert  | A condition that requires immediate attention |
| 8:Emerg  | An emergency condition                        |
  
| Examples                 | Description                                                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| mail.info                | Translates to the mail facility with a severity of info. This format will include severity of info or greater (notice, warn, err ).                 |
| - =mail.info             | Translates to the mail facility with a severity of info. This format means only include the info severity.                                          |
| auth,authpriv.*          | Translates to facility auth and authpriv with a priority of any.                                                                                    |
| ***.*;auth,authpriv.none | Translates to any facility with any severity, except auth and authpriv facilities with no severity. Basically, everything except auth and authpriv. |
## Action Syntax

| Action                     | Description                                                                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------- |
| mail.info /var/log/maillog | Send events with a facility of mail and a severity of info or greater to the /var/log/maillog file. |
| -/var/log/messages         | The dash has no effect.                                                                             |
| kern.* /dev/console        | This configuration sends alerts from the kernel facility with any priority to the console.          |
``` Log-Conig
#  /etc/rsyslog.conf    Configuration file for rsyslog.  
#  
#           For more information see  
#           /usr/share/doc/rsyslog-doc/html/rsyslog_conf.html  
...  
...  
auth,authpriv.*             /var/log/auth.log  
*.*;auth,authpriv.none      -/var/log/syslog  
#cron.*                     /var/log/cron.log  
daemon.*                    -/var/log/daemon.log  
kern.*                      -/var/log/kern.log  
lpr.*                       -/var/log/lpr.log  
mail.*                      -/var/log/mail.log  
user.*                      -/var/log/user.log  

#
# Logging for the mail system.  Split it up so that  
# it is easy to write scripts to parse these files.  
#  
mail.info                  -/var/log/mail.info  
mail.warn                  -/var/log/mail.warn  
mail.err                   /var/log/mail.err  
#  
# Logging for INN news system.  
#  
news.crit                  /var/log/news/news.crit  
news.err                   /var/log/news/news.err  
news.notice                -/var/log/news/news.notice
```

# [[Windows Event Viewer]]

| Purpose of Windows Event Viewer | Enables browsing and managing event logs for system monitoring and troubleshooting. |
| ------------------------------- | ----------------------------------------------------------------------------------- |
| Functionality                   | Microsoft management console snap-in.                                               |
| Usage                           | - Troubleshoot a problem with Event Viewer.                                         |
|                                 | - Locate events related to the problem.                                             |
|                                 | - Filter for specific events across multiple logs.                                  |
|                                 | - Display all potentially related events.                                           |
| Log Types                       | - Windows Application Logs                                                          |
|                                 | - Windows Services Logs                                                             |

| Starting Event Viewer        |                                             |
| ---------------------------- | ------------------------------------------- |
| Launch via command prompt:   | - Command prompt + the `"eventvwr"` command |
| **Using Windows interface:** | - Click the Start button                    |
|                              | - Click Control Panel                       |
|                              | - Click Administrative Tools                |
|                              | - Double-click Event Viewer                 |

# [[Firewall Log]]

| Category                  | Description                                                                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Importance                | Provide insight into and context for security events.                                                                                                                                           |
| Analysis                  | Understand communication relationships, timing, and attacker’s motives/tools.                                                                                                                   |
| ACL-Denied Logs           | May indicate potential unauthorized attempts to access the network.                                                                                                                             |
| Potential Security Threat | Footprinting or port scanning attempt from the 209.165.200.233 outside host to the hosts in the dmz.                                                                                            |
| Impact on IPS             | IPS placed behind the firewall will not be able to detect the port scanning traffic.                                                                                                            |
| Firewall Log Message      | Log messages from the Cisco ASA syslog show the 209.165.200.233 outside host attempting to connect to different dmz hosts over different ports and being denied by the “outside_access_in” ACL. |
### CISCO ASA Firewall Log
```
Aug 14 2019 12:38:51 %ASA-6-302013: Built inbound TCP connection 855 for outside:209.165.200.236/1107 (209.165.200.236/1107) to dmz:10.1.1.1/80 (10.1.1.1/80)
```
- Firewall Log Messages: Track NATs and connection events.
- Cisco ASA Appliance Syslog: Example of tracking connection events.
- Translation Type: Dynamic translation.
```
%ASA-6-305009: Built dynamic translation from inside:172.16.1.1 to outside:198.51.100.1
```
- Initial Log Message Focus: A small subset of log messages will provide the most benefit initially.
- Log Message Severity: The severity level of a log message is indicated by a number, such as %ASA-==3==-106014 log.

| **Syslog Mnemonic** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `%ASA-3-106014`     | Deny inbound ICMP from `src interface_name: IP_address` to `dst interface_name: IP_address` (type `dec`, code `dec`) - The ASA denied an inbound ICMP packet.                                                                                                                                                                                                                                                                                                                                                         |
| `%ASA-6-106015`     | `Deny TCP (no connection) from IP_address/port to IP_address/port flags tcp_flags on interface interface_name` The ASA discarded a TCP packet that has no associated connection in the ASA connection table. The ASA looks for a SYN flag in the packet, which indicates a request to establish a new connection. If the SYN flag is not set, and there is no existing connection, the ASA discards the packet                                                                                                        |
| `%ASA-1-106021`     | `Deny protocol reverse path check from source_address to dest_address on interface interface_name` Someone is attempting to spoof an IP address on an inbound connection. Unicast RPF, also known as reverse route lookup, detected a packet that does not have a source address that is represented by a route in the ASA routing table                                                                                                                                                                              |
| `%ASA-6-302014`     | `Teardown TCP connection id for interface : real-address / real-port [(``idfw_user``)] to interface : real-address` / `real-port` [`(``idfw_user``)] duration` `hh``:``mm``:``ss` `bytes bytes [` `reason` `] [(` `user` `)]` A TCP connection between two hosts was deleted.<br><br>Reasons for the deleted connection:<br>- **Conn-timeout:** The connection ended when a flow is closed because of the expiration of its inactivity timer.<br>- **Deny terminate:** Flow was terminated by application inspection. |
| `%ASA-6-302016`     | `Teardown UDP connection number for interface : real-address / real-port [(``idfw_user``)] to interface : real-address / real-port [(``idfw_user``)] duration` `hh``:``mm``:``ss` `bytes bytes [(``user``)]` A UDP connection between two hosts was deleted.                                                                                                                                                                                                                                                          |
| `%ASA-6-302021`     | `Teardown ICMP connection for faddr { faddr \| icmp_seq_num} [(``idfw_user``)] gaddr { gaddr \| cmp_type } laddr laddr [(``idfw_user``)]` An ICMP session is removed in the fast-path when stateful ICMP is enabled using the `inspect icmp` command.                                                                                                                                                                                                                                                                 |
# [[DNS Log]]

| Aspect                               | Description                                                                                                                                                                 |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Importance                           | Crucial for incident reconstruction and understanding attacker behavior.                                                                                                    |
| DNS Resolution Process               | Clients resolve domain names into IP addresses by sending requests to recursive name servers.                                                                               |
| Security Aspects of DNS              | Monitoring DNS queries and answers reveals who is accessing services and who is providing them.                                                                             |
| DNS Logging Challenges               | Difficult to analyze logs from various name servers with different logging capabilities and formats, and high volume of DNS queries.                                        |
| DNS Traffic Monitoring Solution      | Passively capture all DNS activity on the wire at major network choke-points and store them in a compressed format.                                                         |
| Malicious DNS Request Identification | Compare observed DNS activity with a baseline or model of normality to identify unusual patterns.                                                                           |
| Malicious DNS Requests               | Malware can use DNS requests to encode commands or exfiltrate data.                                                                                                         |
| Malware Example                      | Multigrain: Multigrain malware steals credit and debit card information, using domains like [dojfgj.com](http://dojfgj.com/) with hundreds of sub-domains for exfiltration. |
| DNS Lookup Investigation             | Investigating unusual DNS requests, such as those with long sub-domains or those directed to suspicious domains, can reveal malware activity.                               |
![3](/Course-Notes/.assets/Pasted_image_20241122135632.png)
![2](/Course-Notes/.assets/Pasted_image_20241122135637.png)

| Feature                  | Description                                                                                     |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| Data Exfiltration Method | Attacker used DNS queries to exfiltrate credit card data encoded in hexadecimal format.         |
| Data Encoding            | Credit card data was encoded in hexadecimal format and prepended to the sub-domain.             |
| Attacker’s Goal          | To decode the data remotely and send sensitive information out of the network.                  |

| DNS Logging            | Disabled by default on most DNS servers and should be enabled.                                  |
| ---------------------- | ----------------------------------------------------------------------------------------------- |
| DNS Logging in Windows | Enabled by checking checkboxes and selecting request/response logging.                          |
| Logging Format         | Can log requests and responses together in a single entry.                                      |
| Log Size               | Can grow rapidly, especially on large networks, due to detailed logging designed for debugging. |
# [[Web Proxy Log]]

malware often spreads through http/https for CnC communication.

```
! Squid Web Proxy Access Log Example

1265529266.756 261 192.168.1.45 TCP_TUNNEL/200 3511 CONNECT services.example.com:443 - HIER_DIRECT/209.165.200.235
1265529273.873 8 192.168.1.254 TCP_HIT/200 1563 GET http://www.example.com/en-us/default/layout/previous.gif - NONE/- image/gif
1265529273.881 12 192.168.1.254 TCP_HIT/200 2961 GET http://www.example.com/gif/lightning-100x60.jpg - NONE/- image/jpeg
1364222662.246 90 192.168.0.6 TCP_MISS/200 619 GET http://www.example.com/pagead/conversion/? - DIRECT/172.16.0.152 image/gif
1364222662.257 85 192.168.0.6 TCP_MISS/200 2347 GET http://www.example.com/pagead/conversion/? - DIRECT/172.16.0.152 image/gif
1364222675.456 15 192.168.2.1 TCP_MISS/200 141159 GET http://spotlight2.com/system/logs/k1.exe 
1364222689.532 77 192.168.2.1 TCP_MISS/200 36098 GET http://spotlight2.com/module/4c06c7a4c2bd4567139df133455
```

| Field                   | Description                                                                                                                                    |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Web Proxy Functionality | Decrypts SSL/TLS traffic for inspection, logs HTTP/HTTPS traffic, and provides precise browsing session logs.                                  |
| Web Proxy Log Analysis  | Helps investigate web-based attacks, such as identifying potential data exfiltration or malware droppers based on suspicious traffic patterns. |
| Log Entry Format        | Describes the HTTP request or response, including timestamp, client information, and request details.                                          |
| Timestamp Format        | Epoch time, representing the number of seconds since January 1, 1970, at midnight GMT.                                                         |
| Epoch Time Conversion   | Can be converted to a more familiar format using online converters.                                                                            |
| Log Entry Fields        | IP address, HTTP method, URL, HTTP status code, and caching status.                                                                            |
| Caching Status          | TCP_HIT (cached in web proxy cache), TCP_MEM_HIT (cached in RAM), or TCP_TUNNEL (traffic tunneled to the web server).                          |
| TCP_TUNNEL Explanation  | Squid proxy doesn’t understand or interpret tunneled traffic, such as encrypted HTTPS traffic.                                                 |
### **HTTP Status Codes**

|**Transaction/Error**|**Status**|**Description**|
|---|---|---|
|**Successful Transactions**|200|OK|
||201|Created|
||202|Accepted|
|**Redirected Transactions**|301|Moved permanently|
||302|Moved temporarily|
||304|Not modified|
|**Client-Side Errors**|400|Bad request|
||401|Unauthorized|
||403|Forbidden|
||404|Not found|
|**Server-Side Errors**|500|Internal server error|
||501|Not implemented|
||502|Bad gateway|
||503|Service unavailable|
### **Common HTTP Request Methods (from RFC 2616)**

| **Request Method**                           | **Definition**                   |
| -------------------------------------------- | -------------------------------- |
| **Common, Legitimate Requests**              |                                  |
| GET                                          | Retrieval and simple searches    |
| POST                                         | Submit data-query                |
| PUT                                          | Upload data-files                |
| **Uncommon, Potentially Malicious Requests** |                                  |
| HEAD                                         | Metadata retrieval               |
| DELETE                                       | Remove resource                  |
| TRACE                                        | Application layer trace of route |
| OPTIONS                                      | Request available methods        |
| CONNECT                                      | Tunnel SSL connection            |
| PROPFIND                                     | Retrieve properties of an object |
# [[Email Proxy Log]]

Example of the Cisco ESA log:
```
Thu Sep 18 16:17:38 2019 Info: Start MID 1653 ICID 16488
Thu Sep 18 16:17:38 2019 Info: MID 1653 ICID 16488 From: <auto-notify@ups.com>
Thu Sep 18 16:17:38 2019 Info: MID 1653 ICID 16488 RID 0 To: <any.one@mylocal_domain.com>
Thu Sep 18 16:17:38 2019 Info: MID 1653 Message-ID '<BLU437-SMTP10E1315A60354F2906677B9DB70@phx.gbl>'
Thu Sep 18 16:17:38 2019 Info: MID 1653 Subject 'Package delivery notification''
Thu Sep 18 16:17:38 2019 Info: MID 1653 ready 8313 bytes from <auto-notify@ups.com>
Thu Sep 18 16:17:38 2019 Info: MID 1653 matched all recipients for per-recipient policy DEFAULT in the inbound table
Thu Sep 18 16:17:38 2019 Info: ICID 16488 close
Thu Sep 18 16:17:39 2019 Info: MID 1653 interim verdict using engine: CASE spam negative
Thu Sep 18 16:17:39 2019 Info: MID 1653 using engine: CASE spam negative
Thu Sep 18 16:17:39 2019 Info: MID 1653 AMP file reputation verdict : MALWARE
Thu Sep 18 16:17:39 2019 Info: Message aborted MID 1653 Dropped by amp
Thu Sep 18 16:17:39 2019 Info: Message finished MID 1653 done
```
- Malware Detection: Cisco ESA with Cisco AMP detected and dropped a malware attachment in an email from auto-notify@ups.com.
	- Email Proxy Logs: Email proxies typically log incoming spam, emails with detected viruses, and outgoing emails with sensitive content.
	- DLP Policy Violation: An email from user1@exampleone.com violated the DLP policy and was quarantined by the email proxy.

# [[AAA Server Log]]

| Description               | Details                                                                                                    |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| AAA Server Functionality  | Provides authentication, authorization, and accounting services for both wired and wireless user requests. |
| AAA Server Log Importance | Offers valuable insights during incident investigations, such as potential brute force attacks.            |
| Authentication Status     | User it1 first failed authentication then was successfully authenticated.                                  |
| Log Source                | The live log page from the Cisco Identity Services Engine (ISE).                                           |
| Additional Information    | Network switch port, user endpoint device MAC address, etc.                                                |
![1](/Course-Notes/.assets/Pasted_image_20241122143747.png)

# NGFW ([[Next Generation Firewall Log]])

| Feature                                 | Description                                                                                                                                                                      |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Security Device                         | Cisco Firepower NGFW.                                                                                                                                                            |
| NGFW Services                           | Provides traditional firewall services, VPN, IPS, AMP, DNS inspection, application visibility and control, reputation-based filtering, URL filtering, SSL decryption, and so on. |
| NGFW Information                        | Provides robust information during incident investigations from a single device management console.                                                                              |
| Connection Blocking                     | Cisco Firepower NGFW blocks connections to Windows updates and gambling-related websites due to the configured access policy.                                                    |
| - Connection Event Information          | Connection events provide details such as connection time, source and destination hosts, protocols used, data transacted, and more.                                              |
| - Purpose of Tracking Connection Events | To monitor network behavior and detect suspicious activities.                                                                                                                    |
| Malware Detection Method                | Cisco Firepower NGFW blocks malware based on the file’s SHA-256 value.                                                                                                           |
| - Malware Event Visualization           | Malware events are visualized in a figure.                                                                                                                                       |
| Event Information                       | Cisco Firepower NGFW IPS events include time, sending and receiving IP addresses and countries, and compromise indication.                                                       |
| Detailed Information                    | Drilling down on an IPS event provides packet-level information and the IPS rule that triggered the event.                                                                       |
| Host Profile Status                     | Identify potentially attacked and compromised hosts.                                                                                                                             |
| Security Event Indicator                | Three IOCs are present on the host.                                                                                                                                              |
# [[Applications Log]]

>Events logged by network applications, determined by software developers.

| Area                                      | Description                                                                                       |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------- |
| SOC Operations and Application Logs       | Analysts monitor application logs to ensure appropriate resource usage and detect misuse.         |
| Storage Location                          | Linux: /var/log folder; Windows: Event Viewer.                                                    |
| SQL Log Purpose                           | Records user activities, including database access and select functions.                          |
| - Investigating SQL Injection             | Analyzing SQL logs to identify suspicious user queries and database selections.                   |
| Security Analysis                         | Examining SQL logs for potential security breaches, such as SQL injection attacks.                |
| Application Security Specialist Role      | Assists in incident investigations, identifies application flaws, and provides immediate fixes.   |
| - Incident Investigation Responsibilities | Determines the cause of breaches, analyzes log and audit trail activity.                          |
| - SOC Structure                           | Application security specialist may be a distinct role within a Security Operations Center (SOC). |
