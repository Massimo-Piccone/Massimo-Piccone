## Log Poisoning

>An adversary injects malicious code into a log file by triggering error conditions.
- ==Attack Vector==: Adversary injects malicious code in form inputs or HTTP request headers. (LFI)
- ==Impact==: Malicious code is logged and can potentially be executed.
- ==Target Log==: apache.log, auth.log, vsftpd.log, and ssh.log.
- ==Requirement==: The system must be susceptible to LFI attacks for log poisoning to be effective.
#### Log4j

- ==Vulnerability== (2021)**: A significant security flaw in the Log4j logging utility that allowed adversaries to execute malicious code on vulnerable servers, leading to severe security breaches.
- ==Method==: Adversaries submitted specially crafted requests to vulnerable servers, causing them to connect to adversary-controlled servers over LDAP.
- ==Impact==: Adversaries could gain full control of vulnerable servers, leading to information theft, ransomware attacks, and other malicious activities.
## Log Tampering

>Manipulating log files and entries to conceal evidence of hacking activities.
- ==Purpose==: To erase traces of an attacker’s presence or actions from log records.
- ==Impact==: Obstructs investigations and hinders the identification of attackers and their methods.

Sanitization practices:
• Disabling logging on all accessed systems
• Deleting recorded data
• Modifying logs with fake data
• Erasing logs of historical commands used by attackers

- ==Log Tampering Mitigation==: Hardening log sources and management platforms, and detecting disabled logging events.
- ==Log Entry Protection==: Using log management solutions with digital signing capabilities to prevent tampering and modifications.
- ==Splunk’s Log Management==: Splunk stores logs and prevents deletion or modification through its user interface.
## Challenges in Log Management

| Challenge Type             | Description                                                                                                  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Log Generation and Storage | Issues with managing log sources, ==inconsistent content==, timestamps, and formats across devices.          |
| Log Protection             | Protecting ==sensitive information== in logs from unauthorized access through encryption and access control. |
| Log Analysis               | Challenges faced by SOC analysts due to ==overwhelming== tasks, lack of training, and inadequate tools.      |

Key Techniques for Mitigation

- **Hardening Log Sources**: Strengthening the security of devices that generate logs to prevent tampering.
- **Digital Signing of Logs**: Using cryptographic methods to ensure the integrity of log entries, making them tamper-proof.
- **Access Control**: Implementing strict access policies to limit who can view or modify log files.

Key Tools

- **Splunk**: A log management solution that stores logs securely and prevents deletion or modification of log entries through its user interface.

Facts to Memorize

- Log4j vulnerability disclosed in December 2021
- Common log files targeted in log poisoning: apache.log, auth.log, vsftpd.log, ssh.log
- Local File Inclusion (LFI) is a common web application vulnerability
- Log management solutions can digitally sign log entries to protect against tampering

Reference Information

- Log poisoning: Involves injecting malicious code into log files
- Log tampering: Manipulating log files to erase or alter evidence of activities
- Log management challenges: Include log generation, protection, and analysis

Cause and Effect

|Cause|Effect|
|---|---|
|Log poisoning through malicious code injection|Can lead to unauthorized access, data theft, or system control by adversaries|
|Log tampering by attackers|Results in loss of evidence, making it difficult for SOC analysts to investigate incidents|
|Lack of proper log management solutions|Increases vulnerability to attacks and complicates incident response and forensic investigations|
|Inconsistent log formats and timestamps|Hinders effective log analysis and can lead to misinterpretation of log data|

Key Terms/Concepts

- **Log Poisoning**: An attack where an adversary injects malicious code into log files, often through error conditions, to exploit vulnerabilities like Local File Inclusion (LFI).
- **Log Tampering**: The manipulation of log files to erase or alter evidence of an attack, often involving sanitization practices to mislead security analysts.
- **Log Management**: The process of collecting, storing, and analyzing log data to ensure security and compliance, while facing challenges related to generation, protection, and analysis.