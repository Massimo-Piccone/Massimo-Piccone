%% #review [[Tools Review]] [[Malicious Activity Review]] %%

## Fast Flux and Botnets

Threat actors may also use DNS traffic to establish CnC back-end communication channels between compromised hosts and remote systems that are controlled by the attacker.

| Technique                        | Description                                                                                                                                                       |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Botnet Definition                | A network of infected devices controlled by malicious software.                                                                                                   |
| Botnet Communication             | Utilizes mechanisms like DNS, HTTP, HTTPS, and IRC to communicate with CnC servers.                                                                               |
| Fast-Flux Technique              | Uses a shifting number of compromised hosts behind a single domain name to hide attack servers.                                                                   |
| DNS Load Balancing               | Multiple IP addresses can be registered to a single host domain name, allowing threat actors to obfuscate their attacking system.                                 |
| Fast Flux Service Network (FFSN) | Botnets can use a combination of round-robin IP addresses and low TTL values to rapidly change IP addresses associated with malicious domains, evading detection. |
| DNS Record Management            | Removing malicious DNS records is more complex than isolating compromised IP addresses due to the potential for multiple DNS records per IP address.              |
| Fast Flux Definition             | A technique that rapidly changes the IP address of a malicious server, making it difficult to detect and block.                                                   |
| Impact of Fast Flux              | Renders traditional IP-based blocking techniques ineffective, hindering defenders’ ability to locate and target the malicious server.                             |
| Purpose of Fast Flux             | Obscures the malicious server’s location, making it challenging to identify and neutralize.                                                                       |
![6](/Course-Notes/.assets/Pasted_image_20241123123949.png)

## Double IP Flux

| Technique      | Purpose                                                                       | Example                                                                                                                      |
| -------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Double IP Flux | Rapidly change hostname-to-IP address mappings and authoritative name servers | Changing the IP address of the authoritative name server ([ns.example.com](http://ns.example.com/)) in the attacker’s domain |
## Domain Generation Algorithm

| Functionality         | Description                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DGA Functionality     | DGAs are used in malware to periodically randomize domain names, making it difficult to block or identify the malware’s command and control (CnC) servers. |
| DGA Domain Generation | DGAs generate different domain names using random numbers, current time, or a combination of both, often combined with alphanumeric characters.            |
| DGA Example           | In the provided example, randomly generated sub-domain names resolve to the same IP address, illustrating how DGAs can be used to evade detection.         |

# TOR 

- ==Functionality==: Allows attackers to bypass network traffic analysis.
- ==Potential Exploit==: May allow attackers to pass malicious traffic undetected.

# [[IPS Evasion Techniques]]
### IP Fragmentation (L3)

| Technique                        | Description                                                                                                                                                        | Example                                                                                           | Mitigation                                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fragmentation to Evade Detection | Split malicious data across fragments to bypass IPS if it doesn’t reassemble packets.                                                                              | Packet fragmented into: [Part 1] + [Part 2], with the malicious code spread across the fragments. | Ensure IPS reassembles fragments exactly as the target system would.                                                                                                        |
| Ambiguous Fragmentation          | Send overlapping or conflicting fragments to make the IPS and target interpret the packet differently, allowing malicious payloads to reach the target undetected. | N/A                                                                                               | Monitor for excessive or suspicious fragmentation (e.g., overlaps or small, unnecessary fragments). Configure systems to reject ambiguous or improperly fragmented packets. |
## **Segment Manipulation:** 

| Segment Manipulation                                                       | Attack Technique                                                                                                     | Example                                                                                          | Mitigation                                                                                                                                                                                          |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| An attacker alters the segmentation of TCP streams to evade IPS detection. | Overwrites part of a previous segment with new data in a subsequent segment to hide or obfuscate malicious payloads. | Segment 1: [Data A]. Segment 2 (overlapping): [Altered Data A], overwriting the earlier segment. | Ensure the IPS reassembles TCP streams exactly as the target host does.<br><br>Monitor for overlapping or conflicting TCP segments.<br><br>Check for anomalies in segment order or retransmissions. |
### Overlapping Fragment Attack (L3)

| Attack Type                      | Description                                                                                           | Impact                                                                                                                  | IPS Sensor Limitation                                                                                         | Example                                                                                                            |
| -------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Overlapping Fragment Attack (L3) | A class of attack where IP header offset values don’t match, causing one fragment to overlap another. | Different operating systems handle overlapping fragments differently, potentially leading to confusion for IPS sensors. | IPS sensors may not accurately predict how target systems will reassemble packets with overlapping fragments. | Fragment 1: [Data A \| Data B]. Fragment 2 (overlapping): [Data C \| Data D], causing ambiguity when reassembling. |
###### Mitigation 
- Enforce RFC 1858-compliant fragment handling to discard overlapping fragments.
- Use IPS/IDS that reassembles fragments like the target system and detects anomalies.
- Enable Path MTU Discovery (PMTUD) and block unnecessary fragmented traffic.
- Drop fragments smaller than a minimum size threshold (e.g., <8 bytes).
- Patch systems to handle fragment reassembly securely.
- Detect and flag unusual or excessive fragmentation patterns.

### IPS Sensor Vulnerability

| IPS Sensor Mode  | Challenges                                                             | Example Attack Scenario                                                                                            |
| ---------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Promiscuous Mode | Difficulty interpreting overlapping IP fragments with data overwrites. | An attack targeting cmd.exe might be missed if the IPS sensor identifies the fragment as non-threatening cmd.jpg.  |
| Inline Mode      | Modern IPS sensors process data to remove ambiguity.                   | Overlapping fragments with consistent data are interpreted correctly, while fragments with overwrites are dropped. |

## Traffic Substitution and Insertion
##### Description
An attacker substitutes payload data with other data in a different format but with the same meaning to evade detection.
##### IPS Sensor Vulnerability
IPS sensors may miss malicious payloads if they don’t recognize the true meaning of data and only focus on specific data formats.
##### Example
1. Using Unicode representation instead of characters inside HTTP requests
2. Exploiting case sensitivity and changing case of characters in a malicious payload, if the network IPS sensor is configured with case-sensitive signatures only
3. Substitution of spaces with tabs, and vice versafor example, inside HTTP requests

Attack Example:
- Attacker substitutes character with its Unicode representation.
- Impact: Web server views the string as the same and acts on them accordingly.
- IPS Sensor Requirement: Must be aware of all possible encodings accepted by end hosts to match network traffic to known malicious signatures.

![5](/Course-Notes/.assets/Pasted_image_20241123140250.png)

| Component           | Description                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Attack Mechanism    | The attacker sends a malicious sequence byte-by-byte, inserting extra bytes within the sequence.                    |
| IPS Sensor Behavior | The IPS sensor accepts all bytes, including the extra bytes, and recognizes the complete sequence as non-malicious. |
| Success Condition   | The insertion evasion is successful if the victim host only accepts bytes belonging to the malicious sequence.      |
## Encryption and Tunneling

| Evasion Method                  | Description                                                                                         | Impact on IPS Sensors                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Encryption                      | Attackers use encryption to hide their traffic from IPS sensors.                                    | IPS sensors cannot analyze encrypted packets.               |
| IPS Sensor Limitation           | IPS sensors rely on plaintext data for analysis.                                                    | N/A                                                         |
| Impact of Encrypted Connections | IPS sensors cannot analyze encrypted traffic, such as site-to-site VPN tunnels.                     | Encrypted connections are invisible to IPS sensors.         |
| Protocol Tunneling              | Attackers can evade detection by tunneling traffic over permitted protocols like DNS or HTTP.       | IPS sensors cannot analyze traffic within protocol tunnels. |
| Combinations                    | Attackers can combine encryption and tunneling, for instance, using HTTPS to tunnel attack traffic. | IPS sensors cannot analyze encrypted, tunneled traffic.     |
## Protocol-Level Misinterpretation
| **Method**   | **Method 1**                                                                                     | **Method 2**                                                      |
|--------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| **Attacker’s Goal** | Evade detection by causing the IPS sensor to misinterpret network protocols.                     | Mislead IPS sensors by altering the data’s endian format.         |
| **Attacker’s Method** | Misinterpret the end-to-end meaning of network protocols to make the IPS sensor see traffic differently from the target. | Endian Format Manipulation: A technique to mislead IPS sensors by altering the data’s endian format. |
| **IPS Sensor’s Response** | Ignore or misinterpret traffic that should be detected.                                          | N/A                                                               |
| **Example**  | Corrupting TCP checksum to confuse IPS sensor.                                                    | N/A                                                               |
| **Attack Type** | Attack Type: Corrupting TCP checksum to confuse IPS sensor.                                        | N/A                                                               |
| **IPS Sensor Behavior** | IPS Sensor Behavior: Accepts and processes packets with bad TCP checksum, seeing more data than end host. | N/A                                                               |
| **Impact on End Host** | Most hosts will not accept packets with bad TCP checksum.                                          | N/A                                                               |
![4](/Course-Notes/.assets/Pasted_image_20241123141841.png)

## Resource Exhaustion

| Evasion Method                                                        | Impact on IPS                                                                              | Example Attack                                                                        |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| Extreme resource consumption by sending fake traffic to create noise. | Overwhelms the IPS sensor, preventing it from analyzing and detecting true attack traffic. | Using attack tools to generate numerous false IPS alerts, consuming sensor resources. |
## Timing Attacks

| Timing Attacks           | Description                                                                    |
| ------------------------ | ------------------------------------------------------------------------------ |
| Attack Evasion Technique | Performing actions slower than normal to avoid exceeding detection thresholds. |
| Detection Mechanism      | Signatures correlate different packets based on time windows.                  |
# [[Gaining Access and Control]]

Common Methods: 
- Phishing campaigns, 
- Malware collection, and 
- Directing users to fake login portals.
- Data leaks
- Exfiltration 
- Exploiting weak services
- Credential staffing
- Online misconfigurations.
Targets: 
- Employee credentials for remote network access.
Alternaitves:
- Password Brute-Forcing (Offliine)
- Password Spraying (Avoids Lockout)
Metigation:
- Changing default credentials
- Limiting attack surface public-facing systems
- Enforcing strong password policies
- Regularly auditing password policies
___
If attackers can gain access to an endpoint, they can also gain control of the endpoint and use it to launch more wide-spread attacks
- Pivoting
- Installation
- Exfiltration
- Botnet Control

DDoS:
- An attacker controls zombies to launch a DDoS attack against the victim’s infrastructure.
- Zombies use a covert channel to communicate with the CnC server controlled by the attacker.
- ==Communication== often occurs over IRC, encrypted channels, bot-specific peer-to-peer networks, and even Twitter.

## Botnets
Bots can log keystrokes, gather passwords, capture packets, financial information, launch DoS attacks, relay spam, and open back doors. 

1. A botnet operator sends self-propagating malware designed connect victim to C&C servers. 
2. They exploit back doors opened by worms and viruses. Bots are more versatile than worms in  infection vectors and can be modified quickly. 
3. The newly infected host logs into the CnC server and awaits commands. 
4. Instructions from the CnC server to each bot in the botnet execute actions. 
5. When the zombies receive the instructions, they generate malicious traffic aimed at the victim.

==Botnet Configuration:== Can be client-server or peer-to-peer.

![3](/Course-Notes/.assets/Pasted_image_20241124143557.png)

## Detecting Malicious Encrypted P2P Traffic

Tactics:
- Traffic Fingerprinting: Monitors encrypted packets to find patterns matching known malicious activity.
- Malicious Activity Detection: Identifies connections to known CnC servers by their distinct patterns.

Challenges:
- Traffic Fingerprinting Limitation: Cannot catch all malicious encrypted traffic.
- Malicious Traffic Evasion: Bad actors can insert random packets to mask the expected fingerprint.

Recommendation:
Implement a layered approach using various techniques, including machine learning algorithms.

[Cisco's Approach:](https://www.cisco.com/c/en/us/solutions/collateral/enterprise-networks/enterprise-network-security/nb-09-encrytd-traf-anlytcs-wp-cte-en.pdf)
- **Cisco Stealthwatch** includes encrypted traffic analytics, which collect network traffic and use machine learning and behavioral modeling to detect a wide range of malicious encrypted traffic, without any decryption.
- **Cisco Umbrella** includes DNS protection technologies that can prevent connections to malicious domains, stopping threats before they are able to establish an encrypted connection.
- **Cisco AMP for Endpoints** is another effective endpoint protection solution to stop a threat before it starts.

# [[Encapsulation]]

- Definition: The process of encapsulating the payload with an additional header for tunneling through intermediate networks.
- Keeping outsiders from getting in was the focus but now insider threats are increasing more and more.
- Insider Threat Detection: Identifying anomalies in data exfiltration to detect insider threats.

Lifecycle of an insider exfiltration:

1. Identify places where sensitive data is stored.
2. Retrieve the data from the location.
3. Move the data within the organization to prepare for exfiltration.
4. Transfer the data outside the organization.

| Technique            | Description                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Protocol Tunneling   | Encapsulates data packets inside a different protocol to bypass firewalls during Exfiltration.                                    |
| Detection            | Performing anomalous behaviors on outbound traffic can detect data leaking using tunneling.                                       |
| DNS Tunneling        | Uses the DNS protocol to communicate non-DNS traffic over port 53 by encapsulating non-DNS data inside DNS queries and responses. |
| DNS Exfiltration     | Attackers manipulate DNS requests to exfiltrate data from a compromised system.                                                   |
| CnC DNS Manipulation | DNS responses are manipulated for Command and Control (CnC) callbacks from the attacker’s infrastructure to a compromised system. |
| Vulnerability        | Enterprise network firewalls allow DNS traffic over port 53.                                                                      |
| Example              | Many free tunneling software packages. EG: [Iodine](https://code.kryo.se/iodine/)                                                 |
## DNS Tunnels
Manual DNS Review is Challenging and time consuming.
Instead we use Baselines and Abnormality for visibility.

![2](/Course-Notes/.assets/Pasted_image_20241124145600.png)

| Threat                    | Description                                                                                                                             | Detection                                 | Prevention                                       |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------ |
| Unusual DNS Request       | Malware could encode stolen data as the subdomain part of a DNS lookup for a domain where the name server is controlled by an attacker. | Monitor DNS log for suspicious activities | Block DNS tunneling traffic to malicious domains |
| Data Exfiltration via DNS | Malware can tunnel out data by encoding it as a subdomain and sending a DNS lookup request to a domain controlled by the attacker.      | Monitor DNS log for suspicious activities | ""                                               |
| Data Encoding Methods     | Two common encoding methods used to avoid detection are Base32 and Base64 encoding.                                                     | Monitor DNS log for suspicious activities | ""                                               |
| DNS Traffic Trends        | Big and complex packets will become more common with future DNS protocol extensions.                                                    | Monitor DNS log for suspicious activities | ""                                               |
| DNS Security Challenges   | Traditional detection techniques may not be sufficient to prevent data leaks over DNS.                                                  | Monitor DNS log for suspicious activities | ""                                               |
| DNS Security Solution     | Adding a security solution that inspects and filters DNS traffic can help contain botnets.                                              | Monitor DNS log for suspicious activities | ""                                               |
![1](/Course-Notes/.assets/Pasted_image_20241124145634.png)
## Other Tunnels

 FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel.

Adversaries may leverage various operating system utilities to exfiltrate data over an alternative protocol.

# [[Altered Disk Image]]

| Malicious Software Introduction                                                                                | Attack Scenario                                                                                                          | Protection Measures                                                                                       |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------- |
| Malicious software can be introduced by altering the software image stored on the victim’s device file system. | An attacker can modify a valid device’s software image by adding malicious code and loading it onto the victim’s device. | Safe coding practices, digital signing, and secure boot can protect against memory and code manipulation. |

| **Feature**             | **Software Image Verification**                                       | **Secure Boot**                                   |
| ----------------------- | --------------------------------------------------------------------- | ------------------------------------------------- |
| **Description**         | Offline process to compare the software image hash with trusted hash. | Ensures devices boot using trusted software.      |
| **Cisco ASA Feature**   | Hash File Validation feature for verifying image file integrity.      | Ensures authenticity and integrity of boot code.  |
| **Verification Method** | Compares calculated hash with trusted hash from manufacturer.         | Verifies authenticity through a chain of trust.   |
| **Commands**            | `verify [/md5                                                         | /sha-512] filename [hash]`                        |
| **Example Command**     | `verify /sha-512 disk0:/asa915-smp-k8.bin`                            | N/A                                               |
| **Success Output**      | Displays matching hash when verification is successful.               | N/A                                               |
| **Failure Output**      | Displays error if computed and submitted hashes do not match.         | N/A                                               |
| **Security Mechanism**  | Ensures software image integrity through hashing.                     | Anchored in hardware, difficult to tamper with.   |
| **Boot Process**        | N/A                                                                   | Verifies authenticity through digital signatures. |
