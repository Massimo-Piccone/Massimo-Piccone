- Personal Firewall Functionality: Protect individual hosts by controlling traffic arriving at and leaving them, unlike traditional firewalls that control network traffic.
- Distributed Firewall Implementation: Pervasive use of personal firewalls, controlled by a centralized system, can provide similar protection to traditional firewalls.

Crucial for protecting mobile systems and in split tunnelling for remote-access VPNs to prevent unauthorized access.

- NGFW Features: Provide protocol and port-based policies, application-level traffic control, and network-specific policy definitions.
- Application Control: Allow and deny traffic based on application lists, with options for user-defined rules and malware protection.
- Monitoring and Reporting: Monitor incoming and outgoing connections, track traffic handling, and potentially alert users to suspicious activity

#### Firewall logs 
Depending on the firewall and how you configure it, the logs that are generated may contain information such as the following:

- Which connections or packets were blocked
- Data that is related to blocked connections or dropped packets, such as the IP addresses, port numbers, and protocols
- Data that is related to permitted connections, such as the IP addresses, port numbers, and protocols

Log files and uses:
- Outbound connections that initiate from internal servers, which could indicate that your computer is being used to attack other computers
- Repeated unsuccessful access attempts from a single IP address within a short time

Suspicious IP address activity, can be investigated with WHOIS but attackers often use spoofed IP addresses. 

host-based firewalls generate large amounts of data, so for optimal use you may need specialized search and event correlation tools.

### Windows firewall host-based firewall

You can create the following types of rules:
- **Program rules:** Rules that control connections for an application or program
- **Port rules:** Rules that control connections for specific ports and protocols
- **Predefined rules:** Rules that apply to specific Windows services and features
- **Custom rules:** Rules that combine several different parameters, including programs, protocols, ports, and services

To create a rule in Windows Firewall with Advanced Security, follow these steps:

1. In the navigation pane on the left, select the category for which you want to create a new rule: **Inbound Rules**, **Outbound Rules**, or **Connection Security Rules**.
2. In the Action pane, click **New Rule**. The New Rule Wizard opens.
3. In the Rule Type screen, select the rule type.
4. Follow the wizard through the process of creating the rule. Depending on the type of rule you create, you may be prompted to select the action to be taken when a connection matches your specified conditions. You may also be prompted to specify when you want the rule to apply (when your computer is connected to its corporate domain, a private network, and/or a public network) 

Windows Firewall **logging** can help you identify malicious activity. Logging is disabled by default. To create a log file, complete the following steps:

1. In the panel on the right, click **Properties**.
2. In the dialog box that opens, click the **Private Profile** tab. In the **Logging** area, click the **Customize** button. A new window opens.
3. Choose the maximum log size, the location for the log file, and what you want to log (dropped packets, successful connections, or both).

To view your log file, complete the following steps:

1. In the main Windows Firewall with Advanced Security window, click **Monitoring**.
2. In the Monitoring pane, click the file path link under **Logging Settings** and to the right of **File Name**. The log opens in Notepad.

The log file contains the following information (and much more) about each event:

- Date
- Time
- Action taken
- Protocol used
- Source IP address
- Destination IP address
- Source port
- Destination port

### Linux host-based firewalls

- **IPtables:** This type of firewall is implemented in the Linux kernel and typically works at the network layer. By using the `iptables` command, you can modify the kernel-level firewall in any Linux operating system to control access to ports, protocols, and services. You can also specify source and destination addresses in the `iptables` command to control access to ports, protocols, and services based on host or network address.

- **Uncomplicated firewall** **(UFW):** UFW is a simplified front end for IPtables.

- **TCPwrappers:** This type of firewall is implemented in the Linux user space, works at the application layer, and is used to permit or deny access to a specific service. It can only be used with network services that are Xinetd-based. The tcpwrappers firewall enables you to specify which hosts can access which services.
