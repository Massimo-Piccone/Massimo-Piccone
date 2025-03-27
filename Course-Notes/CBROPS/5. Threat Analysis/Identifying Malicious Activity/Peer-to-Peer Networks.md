- ==Definition==: A P2P network is a group of computers on the Internet that communicate with each other to perform tasks.
- ==Functionality==: Each computer serves as both a client and a server, with no centralized server storing shared information.
- ==Examples==: Popular P2P networking applications in the late 1990s included music sharing applications like Napster and Kazaa.

## [BitTorrent Application](https://en.wikipedia.org/wiki/BitTorrent)

- ==BitTorrent Functionality==: A P2P file sharing application that enables users to send or receive files.
- ==BitTorrent Tracker==: Provides a list of available files and facilitates connections with peers for file transfer.
- ==BitTorrent Protocol==: Allows users to download files from multiple sources simultaneously, creating a “swarm” of hosts.
- ==File Distribution==: The file is divided into pieces, with each peer receiving and distributing a piece.
- ==Data Integrity==: Cryptographic hashes protect pieces from accidental or malicious modifications.
- ==File Transfer==: Pieces are downloaded non-sequentially and rearranged by the BitTorrent client.
- ==Traffic Throttling==: More ISPs and companies are limiting and throttling BitTorrent traffic.
- ==BitTorrent Anonymization==: BitTorrent clients anonymize and encrypt BitTorrent traffic to avoid detection and throttling.

## [Risks of P2P File Sharing](https://www.us-cert.gov/ncas/tips/ST05-007)

- ==Trusting strangers== in a P2P network without knowing if downloaded files contain malware, pirated software, copyrighted material, or pornography.

- ==Unauthorized access== and sharing of sensitive personal files, leading to liability for both the P2P user and the company.

- Denial of service (==DoS==) when downloading large files, causing significant network traffic.

- ==Attackers gaining== access to the P2P user’s computer through port opening requests, vulnerabilities in P2P applications, or firewall modification.

## Botnets
==Botnet Configuration:== Can be client-server or peer-to-peer.

![1](/Course-Notes/.assets/Pasted_image_20241124143557.png)

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

