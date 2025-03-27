- Overwhelming amount of data.
- Logs or baseline flags indicate timeframe for deeper inspection.
- Incident investigation begins when an alert such as an IPS alert is triggered.

Gathering 5 tuple during investigation:
- Src and Dst ==IP== can be used to identify source and spread.
- Bro or netflow logs can identify anomalous ==ports== or apps, 
  that can then be correlated with IP within the pcap.
- ==Protocol== Identification is often tied directly to the ports.
  Follow the tracks as there may be multiple protocols.

Payload: 
- Use the 5 tuple to obtain the final piece - The Payload.
- Plaintext vs Encrypted, The difficulty will vary.
- The exploit type that was used may be in different forms.
  EG: Shell code in memory or files written to disk.
- Identification is essential for detecting security incidents.

- Packet Filtering Techniques: 
- Goal: Obtain the most relevant dataset possible.
- Filtering by 5tuple + Payloads to filter packet capture results.

![1](/Course-Notes/.assets/Pasted_image_20241125153423.png)

- More detailed searches are often necessary. 
- A sequence of characters that define a search pattern. 
- Often utilizing string fields, or byte sequences.

- Using multiple “== equal” operators, chaining multiple statements with “or” is inefficient. 
  Use REGEX and "matches" to be more concise.
- PCRE Example: To match IP addresses from 192.168.1.101 to 192.168.1.109, use a REGEX pattern instead of typing each IP address individually.

`ip.src_host matches “192\.168\.1\.10[1-9]”`

- Special Character Handling: Uses a backslash (“\”) to escape the period, which is a special character.
- Character Class: Brackets are used to denote a character class, representing any digit from 1 to 9.

Character classes are also useful for creating lists. If the servers in this network are 192.168.1.120, 192.168.1.140, and 192.168.1.160, they could all be found with:

`ip.src_host matches “192\.168\.1\.1[246]0”`

- Snort uses REGEX for signatures.
- Familiarity with regular expressions allows for understanding and using signatures in Wireshark.

Many references and examples exist through the following resources:
- PCRE Regular Expression Cheatsheet—Debuggex
- PCRE Regular Expression Pattern Syntax Reference (PHP preg*)
- PCRE man pages

