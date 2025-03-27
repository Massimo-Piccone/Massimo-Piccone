- ==Goal==: Compromise endpoints or networks protected by network IPS technology.
- ==Method==: Use network IPS evasion techniques to bypass intrusion detection and traffic filtering functions.
## Traffic Fragmentation

An early network IPS evasion technique used traffic fragmentation to bypass the network IPS sensor. Fragmentation-based evasion attempts to avoid detection or filtering by fragmenting malicious traffic.

- Bypassing the network IPS sensor if the IPS sensor does not perform any fragment reassembly

- Reordering the fragments, hoping the network IPS sensor does not correctly reorder the fragments

Classic examples of fragmentation-based evasion include the following:
___
##### IP Fragmentation (L3)
1. **Fragmentation to Evade Detection**:
    - Split malicious data across fragments to bypass IPS *if it doesn’t reassemble packets*.
2. **Ambiguous Fragmentation**:
    - Send overlapping or conflicting fragments to make the IPS and target interpret the packet differently, allowing malicious payloads to reach the target undetected.
###### Example
- Packet fragmented into: [Part 1] + [Part 2], with the malicious code spread across the fragments.
###### Mitigation
- Ensure IPS reassembles fragments exactly as the target system would.
- Monitor for excessive or suspicious fragmentation (e.g., overlaps or small, unnecessary fragments).
- Configure systems to reject ambiguous or improperly fragmented packets.
___
1. **Segment Manipulation:** 
	- An attacker alters the segmentation of TCP streams to evade IPS detection.
2. **Attack Technique:** 
	- Overwrites part of a previous segment with new data in a subsequent segment to hide or obfuscate malicious payloads.
###### Example
- Segment 1: [Data A].
- Segment 2 (overlapping): [Altered Data A], overwriting the earlier segment.
###### Mitigation
- Ensure the IPS reassembles TCP streams exactly as the target host does.
- Monitor for overlapping or conflicting TCP segments.
- Check for anomalies in segment order or retransmissions.
____
##### Overlapping Fragment Attack (L3)
- A class of attack where IP header offset values don’t match, causing one fragment to overlap another.
- Impact: Different operating systems handle overlapping fragments differently, potentially leading to confusion for IPS sensors.
- IPS Sensor Limitation: IPS sensors may not accurately predict how target systems will reassemble packets with overlapping fragments.
###### Example
- Fragment 1: [Data A | Data B].
- Fragment 2 (overlapping): [Data C | Data D], causing ambiguity when reassembling.
###### Mitigation 
- Enforce RFC 1858-compliant fragment handling to discard overlapping fragments.
- Use IPS/IDS that reassembles fragments like the target system and detects anomalies.
- Enable Path MTU Discovery (PMTUD) and block unnecessary fragmented traffic.
- Drop fragments smaller than a minimum size threshold (e.g., <8 bytes).
- Patch systems to handle fragment reassembly securely.
- Detect and flag unusual or excessive fragmentation patterns.
___ 

In the example below, the second IP fragment specifies an offset value that is 3 bytes less than the actual end of the first IP fragment. The receiving operating system can process this in three different ways:

- It can prefer the original data that it received, so **cmd.jpg** is in the accepted data stream.

- It can overwrite the original data using what is in the overlapping fragment, so **cmd.exe** is in the accepted data stream.

- It can recognize that there is ambiguity in the fragments and reject the data.

![3](/Course-Notes/.assets/Pasted_image_20241123135359.png)

- IPS Sensor Vulnerability: IPS sensor can miss attacks if it processes overlapping fragments differently than the intended victim.
- Example Attack Scenario: An attack targeting cmd.exe might be missed if the IPS sensor identifies the fragment as non-threatening cmd.jpg.

```
# Note
- IPS Sensor Mode: Promiscuous mode IPS sensors face challenges in interpreting overlapping IP fragments with data overwrites.
- Inline Mode IPS Sensor Behavior: Modern IPS sensors in inline mode process data to remove ambiguity, allowing overlapping fragments with consistent data and dropping fragments with overwrites.
```

## Traffic Substitution and Insertion

#### Substitution

>An attacker substitutes payload data with other data in a different format but with the same meaning to evade detection.

- IPS Sensor Vulnerability: IPS sensors may miss malicious payloads if they don’t recognize the true meaning of data and only focus on specific data formats.

Examples:
	- Using Unicode representation instead of characters inside HTTP requests
	- Exploiting case sensitivity and changing case of characters in a malicious payload, if the network IPS sensor is configured with case-sensitive signatures only
	- Substitution of spaces with tabs, and vice versa—for example, inside HTTP requests

Attack Example:
- Attacker substitutes character with its Unicode representation.
- Impact: Web server views the string as the same and acts on them accordingly.
- IPS Sensor Requirement: Must be aware of all possible encodings accepted by end hosts to match network traffic to known malicious signatures.

![2](/Course-Notes/.assets/Pasted_image_20241123140250.png)

#### Insertion

- Insertion Attack Mechanism: The attacker sends a malicious sequence byte-by-byte, inserting extra bytes within the sequence.
- IPS Sensor Behavior: The IPS sensor accepts all bytes, including the extra bytes, and recognizes the complete sequence as non-malicious.
- Success Condition: The insertion evasion is successful if the victim host only accepts bytes belonging to the malicious sequence.

## Encryption and Tunneling

- Encryption as Evasion Method: Attackers use encryption to hide their traffic from IPS sensors.
- IPS Sensor Limitation: IPS sensors rely on plaintext data for analysis and cannot decrypt encrypted packets.
- Impact of Encrypted Connections: IPS sensors cannot analyze encrypted traffic, such as site-to-site VPN tunnels.

- Protocol Tunneling: Attackers can evade detection by tunneling traffic over permitted protocols like DNS or HTTP.
- Combinations: Attackers can combine encryption and tunneling, for instance, using HTTPS to tunnel attack traffic.

## Protocol-Level Misinterpretation

Method 1
- Attacker’s Goal: Evade detection by causing the IPS sensor to misinterpret network protocols.
- Attacker’s Method: Misinterpret the end-to-end meaning of network protocols to make the IPS sensor see traffic differently from the target.
- IPS Sensor’s Response: Ignore or misinterpret traffic that should be detected.

Example:
- Attack Type: Corrupting TCP checksum to confuse IPS sensor.
- IPS Sensor Behavior: Accepts and processes packets with bad TCP checksum, seeing more data than end host.
- Impact on End Host: Most hosts will not accept packets with bad TCP checksum.

Method 2
- Endian Format Manipulation: A technique to mislead IPS sensors by altering the data’s endian format.
- Little Endian: Stores the low-order byte at the lowest address and the high-order byte at the highest address.
- Big Endian: Stores the low-order byte at the highest address and the high-order byte at the lowest address.

![1](/Course-Notes/.assets/Pasted_image_20241123141841.png)

- Endian Format in Networking: Protocol headers in distributed computing specify the endian format for data payloads.
- Attack Vector: Attackers exploit the endian format specification to mislead IPS sensors.
- Impact of Endian Format: Attackers use big endian to format data payloads, causing IPS sensors to misinterpret the data as safe.
## Resource Exhaustion

- Evasion Method: Extreme resource consumption by sending fake traffic to create noise.
- Impact on IPS: Overwhelms the IPS sensor, preventing it from analyzing and detecting true attack traffic.
- Example Attack: Using attack tools to generate numerous false IPS alerts, consuming sensor resources.
## Timing Attacks

- Attack Evasion Technique: Performing actions slower than normal to avoid exceeding detection thresholds.
- Detection Mechanism: Signatures correlate different packets based on time windows.