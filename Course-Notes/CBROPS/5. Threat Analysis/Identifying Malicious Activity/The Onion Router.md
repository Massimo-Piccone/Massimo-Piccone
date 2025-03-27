[The Onion Router (Tor)](https://2019.www.torproject.org/index.html.en) is 
- Open Source software
- Open network that enables 
- Anonymous communications
Usage: 
- Used globally, especially in censored regions and by those seeking privacy.
Built for:
- Dissidents, individuals in repressive regimes, and anyone wanting to keep their browsing private.

- ==Access Method==: Users access the Tor network through the Tor browser.
- ==Browser Functionality==: The Tor browser routes web traffic through the Tor network instead of directly to websites.
- ==Network Composition==: Thousands of servers (Tor relays) owned and maintained by individuals, universities, companies, and so on.

![4](/Course-Notes/.assets/Pasted_image_20241124130338.png)

Attackers:
- ==Usage==: Increasingly used for malicious purposes.
- ==Functionality==: Allows attackers to bypass network traffic analysis.
- ==Potential Exploit==: May allow attackers to pass malicious traffic undetected.

## Tor Relays

- ==Malware Communication==: Many malware variants use Tor to communicate with CnC servers.
- ==Attacker’s IP Address Hiding==: Tor client hides the attacker’s IP address, making it appear as if the connection originates from a Tor exit relay.

Tor Network:
- ==Structure==: Composed of thousands of relays operated globally, forming a random pathway for data packets.
- ==Data Transmission==: Data packets traverse three relays, obscuring the origin and destination of the data.
- ==Tor Client Functionality==: Tor clients, like the Tor browser, utilize the Tor network to anonymize internet traffic.

![3](/Course-Notes/.assets/Pasted_image_20241124130631.png)

Types of Tor relays:

- ==**Guard relay:**== A guard (OR1) is the first Tor relay in a chain of three Tor relays of a Tor circuit.
- ==**Middle relay:**== A middle relay (OR2) is neither a guard relay nor an exit relay, but acts as the second hop between the guard relay and the exit relay. It receives traffic from the guard relay and passes it along to the exit relay.
- ==**Exit relay:**== An exit relay (OR3) is the final relay before it reaches its destination server. Same message as sent to OR1.
- ==**Bridge:**== A bridge is a relay that is not publicly listed as part of the Tor network.

Path Creation:
3 stages, 3 Random relays, 
Independently TLS encrypted.


- **First layer:** The Tor browser assembles data, encrypts it with the symmetric key (SK3) that matches the exit relay during TLS negotiation, and sends it to the destination server.
- **Second layer:** It then re-encrypts the output with the symmetric key (SK2) that matches the middle relay.
- **Third layer:** Finally, it encrypts the output for a third time with the symmetric key (SK1) that matches the first Tor relay node, called the “guard” node.

The Tor browser is now ready to send its triple-encrypted payload through the circuit.

1. The Tor browser sends a triple-encrypted payload to the guard relay. The guard relay decrypts the first layer using its symmetric key (SK1) and forwards the double-encrypted payload with the next destination.

2. The middle relay decrypts the second layer using its symmetric key (SK2) and forwards the single-encrypted payload with the next destination.

3. The exit relay decrypts the final layer using its symmetric key (SK3) and sends the fully decrypted payload to the destination server. If the Tor browser and destination server use a further layer of encryption, the exit relay can’t read the messages.

- Relay Visibility: Adversaries can only see encrypted traffic going to the Tor relay, not its destination.
- Exit Visibility: Adversaries can only see traffic coming from the Tor exit relay, not its origin.
- Traffic Traceability: Adversaries cannot trace the origin or destination of traffic through the Tor network.

## Detecting Tor Traffic

Directory Nodes:
- Integrity of the Tor network 
- Each controlled by a different organization
- Track and publicize the state of the Tor network.
- Active relay status is known to Directory nodes
Many security intelligence feeds will have a list of the current Tor relays & IP address.

[The relay search tool:](https://metrics.torproject.org/rs.html#simple)
- Tor Metrics site can search for the relays IP address. 
- Displays data about the relays and bridges.
- Configuration information, and graphs about usage.

![2](/Course-Notes/.assets/Pasted_image_20241124134642.png)


Cisco Security Intelligence feed.
- Includes Tor Exit Relay IP Addresses.
- used to Block Tor Connections in NGFW by setting `Tor_exit_node category` in the Blacklist column.

![1](/Course-Notes/.assets/Pasted_image_20241124135210.png)

Cisco Stealthwatch, using NetFlow and security intelligence data, can also detect communications with Tor guard relays and exit relays.

