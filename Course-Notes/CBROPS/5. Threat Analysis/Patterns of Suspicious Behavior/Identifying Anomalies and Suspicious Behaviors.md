- ==Baseline Importance==: A network baseline is crucial for comparison with the current network activity to identify anomalies.
- ==Anomaly Detection==: Automated alerts flag unusual patterns in network activity, which analysts investigate to determine if they are suspicious or false positives.
- ==Analyst’s Role==: Analysts play a key role in understanding network behavior and identifying potential threats, even from seemingly insignificant anomalies.

Example:
1. ==High profile threat==: Can be detected by analyzing the network traffic they generate.
2. ==Embedded threat==: Typically aim to exfiltrate data from the network.
3. ==Analysts==: Monitoring network bandwidth and identifying unusual outbound traffic spikes can indicate potential intrusions.

- ==Network Traffic Analysis==: Requires a detailed analysis of traffic types beyond just bandwidth usage.
- ==Baseline Traffic Types==: Includes information about allowed ports, communicating hosts, and used protocols.
- ==Anomaly Detection==: Unusual traffic patterns, like direct internet access over port 80 or external SSH connections, are red flags.

![1](/Course-Notes/.assets/Pasted_image_20241125134751.png)

- ==User Login==: Bob Smith typically logs in from 9 am to 5 pm every day.
- ==Unusual Login Activity==: On 01/18/2015 and 01/19/2015, Bob Smith logged in at 4 am on a Sunday and Monday, deviating from the usual routine.
- ==Potential Insider Threat==: The unusual login activity, especially from a different location, warrants further investigation to determine if it indicates a potential insider threat.

- ==Network Baseline==: A network baseline can identify anomalous behavior, such as out-of-hours network access, even if evidence is removed from log files.
- ==Limitations of Auditing==: Occasional auditing of remote log locations might not reveal suspicious activity, especially if threat actors actively clean up evidence.
- ==Value of Monitoring==: Monitoring log event data is crucial for detecting potential security threats and suspicious activities.

- ==Logging Importance==: System restarts and application crashes are crucial for identifying suspicious behavior.
- ==Baseline Comparison==: Compare the baseline uptime to the current device behavior to identify potential changes causing issues.
- ==Further Investigation==: Analyze logs and network traffic for malicious activity if no changes are found.

- ==Anomaly Detection at Host Level==: Monitoring system settings like Volume Shadow Copy and scheduled jobs for unusual modifications.
- ==Anomaly Detection at User Level==: Observing user commands for unusual behavior, especially those related to modifying services.
- ==Malware Persistence Technique==: Malware, like Metasploit, can gain persistence by loading itself as an unregistered service, making it difficult to detect without a baseline of known-good services.

- ==Powershell’s Powe==r: Extremely powerful CLI with access to .NET APIs and system executables.
- ==Powershell’s Capabilities==: Modify system settings, start new processes, and open remote sessions.
- ==Suspicious Activity Detection==: Monitor Powershell usage for unusual patterns, especially remote sessions initiated by users who typically don’t use that method.

- ==Malware Detection by Users==: Users can detect suspicious activity by noticing unusual behavior, such as strange files, inaccessible files, or changed settings.
- ==Unusual Behavior Timing==: The timing of unusual behavior can be correlated with other suspicious files, processes, or services to aid in malware investigation.

- ==Suspicious Activity Analysis==: Perform deeper analysis once suspicious activity is identified.
- ==Required Information==: Date, time, and affected systems of the suspicious activity.
- ==Data Collection==: Collect relevant logs, network traffic captures, or suspicious files from the affected systems within the identified timeframe.

