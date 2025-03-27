- ==Malware Type==: Highly modular threat capable of delivering various payloads, initially designed as banking Trojans.
- ==Evolution and Payload==: Initially a banking Trojan, [[Emotet]] has evolved to deliver various payloads, including Ryuk ransomware, and is known for stealing and reusing email accounts for impersonation.
- ==Infection Vector==: Emotet primarily infects systems through malicious emails, often impersonating known contacts, and utilizes a network of stolen SMTP accounts for its campaigns. often disguised as macro-laden documents or URLs.
- ==Propagation Method==: Emotet steals email credentials to impersonate victims and spread itself, utilizing a network of stolen SMTP accounts.

![2](/Course-Notes/.assets/Pasted_image_20241120152015.png)

- ==Victim Identification Challenges==: Emotet sometimes removes personal data and TLDs, making it difficult to identify the original victim.
- ==Impersonation Techniques==: Emotet impersonates organizations by stripping personal data and TLDs, leading to domain shortening.

- ==Emotet’s Tactics==: Emotet often includes contact information and previous email content to make the message seem authentic.
- ==Targeted Attack==: Emotet specifically targets individuals, as seen in the example targeting a staff member of U.S. Senator Cory Booker.
- ==Email Appearance==: Emotet spoofs the email address to appear as if it originated from an infected colleague.

![1](/Course-Notes/.assets/Pasted_image_20241120152433.png)

- ==Malware Functionality==: Enumerates network resources, brute forces access to administrator and user accounts, spreads via SMB protocol, and exfiltrates data.
- ==Exfiltration Capabilities==: Exfiltrates emails, sender/recipient information from IPM root folder, and emails sent/received within the last 180 days.
- ==Secondary Payloads==: TrickBot, IcedID, QuakBot, AzoRult, Ursnif/Gootkit, and Zeus Panda Banker Trojans.

- ==Threat Delivery==: Emotet delivers modular, malicious payloads to monetize infections.
- ==Payload Types==: Banking Trojans, stealers, self-propagation, email harvesters, and ransomware.

- ==Emotet Characteristics==: Often arrive via hijacked email threads, making them difficult for antispam systems to identify.
- ==Mitigation Strategy==: Combine advanced antispam systems with user awareness training for effective defense against Emotet.