Analyzing network traffic without a baseline can be time-consuming, especially with large volumes of log entries and DNS requests.

About Baselines:
- ==Often Underestimated==: Network baselining is often overlooked in network security.
- ==Administrator Focus==: Network administrators prioritize security software, logging, and backups.
- ==Baseline Importance==: A good baseline of network traffic behavior is crucial for network security.

Using Baselines:
- ==Definition==: An activity profile for normal system or network behavior, used for comparison with future behavior.
- ==Purpose==: To flag anomalies and detect unusual activities.
- ==Establishment==: Requires system training and monitoring of typical activities like application usage, user access, and network traffic.

Network Break Point: 
>The point at which the network will fail due to hardware and software limitations.

The following figure is another way of looking at the baseline.

A baseline determines the following:
- Is the network on the green line?
- How fast is network load increasing?
- When will the two will intersect?    

![3](/Course-Notes/.assets/Pasted_image_20241125133031.png)

- ==Network Load==: The increasing demand on the network as new applications and factors are added.
- ==Baseline Importance==: 
- Regularly assessing the current network state to identify failures and inform budget decisions for upgrades.
- More effective than analyzing network diagrams and hardware/software lists.

- ==known-good profile==: Provides a reference point for identifying anomalies and understanding normal network behavior.
- ==Baseline Benefits==: Enables faster anomaly investigation and comparison against expected network operation.
- Essential for baseline analysis, including events, transactions, and session monitoring.

Uses:
- ==Network Baseline==: Includes NetFlow and passive DNS statistics to identify normal network traffic patterns.
- ==Log Baseline==: Represents normal system behavior, such as user logins, system restarts, and alerts.
- ==Application Transaction Baseline==: Provides insights into network protocols and host device communication patterns.

- ==Abnormal Behavior Detection==: Easier to identify and flag deviations from the standard baseline profile.
- ==Malicious DNS Traffic Detection==: Unusual URL patterns or potential DNS poisoning threats can be identified and flagged as red flag events.
- ==Anomaly Detection==: Baseline data helps flag patterns deviating from the norm, enabling quick investigation of potential security incidents.

![2](/Course-Notes/.assets/Pasted_image_20241125133907.png)

## Core Baseline Process

- ==NMS Tools Limitations==: While NMS tools can assist with some steps, they often lack flexibility or ease of use.
- ==Understanding the Process==: Studying the process and understanding the network’s workings is beneficial, even with tool usage.

Note: Management Information Base.
- ==MIB Definition==: A database of network management information used and maintained by network management protocols like SNMP or CMIP.
- ==MIB Object Access==: Values of MIB objects can be changed or retrieved using SNMP or CMIP commands, typically through a GUI network management system.
- ==MIB Structure==: Organized in a tree structure with public (standard) and private (proprietary) branches.

![1](/Course-Notes/.assets/Pasted_image_20241125134122.png)