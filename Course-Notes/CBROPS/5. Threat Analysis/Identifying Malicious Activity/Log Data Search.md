Below is a sample syslog entry from the Security Onion server:

```
Jan  6 07:37:01 so CRON[22073]: (root) CMD (find /var/www/so/capme/pcap/*.pcap -mmin +5 -delete >/dev/null 
2>&1)
```

Below is a sample of a CISCO IOS syslog message format:

```
seq no:timestamp: %facility-severity-MNEMONIC:description
```

Date + Time of message or event.

- ==Facility Definition==: Represents the source or cause of a system message, which can be hardware, protocol, or system software.
- ==Facility Codes==: Defined in RFC 3164 (https://www.ietf.org/rfc/rfc3164.txt).
- ==Examples of Facilities==: SNMP, SYS, and so forth.

- ==Message Severity==: Single-digit code from 0 to 7, with 0 being the most severe and 7 being the least severe.
- ==Message Identification==: MNEMONIC text string that uniquely describes the message.
- ==Log Content==: Text string containing detailed information about the event being reported.

- ==Search Engine Functionality==: Similar to Google, allowing powerful queries across large data volumes.
- ==Search Operators==: Boolean, range, and directives for data isolation.

| Operator   | Meaning                                |
| ---------- | -------------------------------------- |
| Keyword    | Query **must** include the keywords    |
| -Keyword   | Query **must not** include the keyword |
| OR Keyword | Query **may** include the keyword      |
`http://www.cisco.com OR http://www.cisc0.com

![6](/Course-Notes/.assets/Pasted_image_20241121151816.png)

- ==ELSA Range Operators Function==: Filter search results based on specified ranges.
- ==ELSA Range Operators Requirement==: Include a keyword alongside the range operator.
- ==Example Usage==: Searching for hosts within a specific IP address range.

```
class=BRO_HTTP “-“ site:www.cisco.com –host>10.10.6.10 –host<10.10.6.20
```

![5](/Course-Notes/.assets/Pasted_image_20241121151914.png)

The above example constructs a search between hosts (only hosts whose IP addresses fall between 10.10.6.10 and 10.10.6.20) that went to http://www.cisco.com.

- ==Directive Function==: Limits or returns a specific number of results from a query. Returns unique values for the specified element.
- ==Example Usage==: Searching for a specific signature in IDS rules.

`72.163.4.161 sig_msg:"NETAPI Exploit" groupby:dstip`

- ==Directive Example==: groupby:dstip groups by destination IP address.
- ==Directive Similarity==: Similar to the SQL groupby command.

Additional ELSA search query syntax attributes and examples are provided in the ELSA documentation.

- ==IDS Alert Review==: Analysts can review IDS alerts, such as those from Sguil, to identify suspicious activity.
- ==Suspicious Activity Indicator==: Clearing Windows Event Logs suspiciously can trigger alerts.

![4](/Course-Notes/.assets/Pasted_image_20241121153338.png)

- ==Abnormal Activity Detection==: Analysts can identify unusual activities through IDS rules, such as those logged in Sguil.
- ==Alert Investigation==: Analysts should investigate alerts, like the one indicating unauthorized clearing of Windows event logs, to determine the cause.
- ==Privilege Level==: The alert was triggered because someone with system privileges, not administrator privileges, performed the unauthorized clearing.

The analyst may also look for additional events that are related to that specific target. For example, sorting on the IP addresses and connections may also reveal useful evidence.

![3](/Course-Notes/.assets/Pasted_image_20241121153413.png)

- ==Suspicious Connection Pattern==: Multiple connections from ports 8080 and 8443, potentially indicating an attack.
- ==Shellcode Involvement==: Some connection events indicate the presence of shellcode, further strengthening the suspicion of an attack.

![2](/Course-Notes/.assets/Pasted_image_20241121153436.png)

The analyst should make an effort to track down further evidence before escalating the event. Using ELSA, the analyst can search for other connections on these ports.

![1](/Course-Notes/.assets/Pasted_image_20241121153444.png)

- ==Investigation Focus==: Determine the attack that gained initial access and subsequent actions for persistence.
- ==Event Severity==: This event should be escalated.
- ==Compromised Ports==: Several connections have been made to the target using specific ports.

- ==Data Management==: Analysts need to know how to search and parse vast amounts of data to manage workload and defend the network.
- ==Query Options==: Understanding robust query options in SIEM helps analysts find specific information efficiently.
- ==Event Analysis==: Analysts analyze aggregated data in SIEM to understand the sequence of events and reconstruct security incidents.

## Modelling Network Attacks

- ==Malicious Attack Assessment Goal==: To develop a hypothetical attack model based on learned knowledge about each attack event.
- ==Malicious Activity Behavior==: Helps analysts construct a hypothesis on how the attack will likely proceed over time.
- ==Malicious Activity Type==: Indicates the intended attack strategy by the threat actor.

- ==Attack Model Classification==: Deterministic or probabilistic, influencing the analytical method used.
- ==Analyst’s Role==: Constructs models based on observed attack progression to predict subsequent actions and outcomes.
- ==Data Sources==: Host-based event logs and network attack events detected by IPS.

- **==Deterministic assessment==** relies on known data values to yield a single outcome for each proposed scenario. Minimum speculation is required to formulate an outcome.

- **==Probabilistic assessment==** considers a wide range of probable scenarios, providing a distribution of possible outcomes. It helps determine the likelihood of an exploit impacting the network. The probabilistic model is less accurate than the deterministic model due to its higher degree of speculation.