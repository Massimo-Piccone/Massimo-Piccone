# Address Resolution Protocol

ARP operates between OSI layers 2 and 3. ARP messages use Ethertype **0x0806**, a two-octet field in an Ethernet header, to indicate the encapsulated protocol. Ethertype 0x0800 indicates IPv4, while 0x86DD indicates IPv6.

MAC Address = Hardware Address = Burned In Address
54:EE:75:B1:6F:22 = 54-EE-75-B1-6F-22 = 54EE.75B1.6F22

Broadcast Mac Address == FFFF.FFFF.FFFF

![7](/Course-Notes/.assets/Screenshot_2024-11-12_at_16.06.37.png)

Windows
```
Microsoft Windows [Version 10.0.10586]
(c) 2015 Microsoft Corporation. All rights reserved.

C:\Users\admin>arp -a

Interface: 10.10.6.204 --- 0x7
  Internet Address      Physical Address      Type
  10.10.6.1             0a-07-0a-0a-04-02     dynamic
  10.10.6.203           0a-06-0a-0a-06-10     dynamic
  10.10.6.255           ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static
  255.255.255.255       ff-ff-ff-ff-ff-ff     static
```

linux 
```
root@Inside-Kali:~#**arp -a**
? (10.10.6.204) at 0a:06:0a:0a:06:11 [ether] on eth0
? (10.10.6.1) at 0a:07:0a:0a:04:02 [ether] on eth0
root@Inside-Kali:~#
```

Attacks :
	Arp poisoning

# Legacy TCP/IP Vulnerabilities

TCP/IP protocol suite (RFC 793)
sponsorship of the U.S. Department of Defense
designed to work in a trusted environment

- ﻿﻿TCP was designed to solve technical challenge of moving information quickly and reliably
- ﻿﻿Internet of our day was not anticipated
- ﻿﻿TCP contains weaknesses in its design  
    Not easy to correct now
- ﻿﻿Early TCP/IP protocols are insecure  
    Susceptible to password sniffing and DoS attacks
    Example: r-utilities, rlogin, rop, rsh

TCP - IP - UDP - ICMP

# IP Vulnerabilities

- **Man-in-the-middle attack:** An MITM attack intercepts a communication between two systems. Essentially, the attacker inserts a device into a network that grabs packets that are streaming past. Those packets are then modified and placed back on the network for forwarding to their original destination. An MITM attack can completely defeat sophisticated authentication mechanisms because the attacker waits until after a communication session is established, which means that authentication has been completed, before starting to intercept packets. An MITM attack does not directly threaten your network's stability, but it is an exploit that can target a specific destination IP address. A form of MITM is called "eavesdropping." Eavesdropping differs only in that the perpetrator just copies IP packets off the network without modifying them in any way.
    
- **Session hijacking:** Session hijacking is a twist on the MITM attack. The attacker gains physical access to the network, initiates an MITM attack and then hijacks that session. In this manner, an attacker can illicitly gain full access to a destination computer by assuming the identity of a legitimate user. The legitimate user sees the login as successful but then is cut off. Subsequent attempts to log back in might be met with an error message that indicates that the user ID is already in use.
    
- **IP address spoofing:** Attackers spoof the source IP address in an IP packet. IP spoofing can be used for several purposes. In some scenarios, an attacker might want to inspect the response from the target victim (nonblind spoofing); in other cases the attacker might not care (blind spoofing). Blind IP address spoofing is most frequently used in DoS attacks. Some reasons for nonblind spoofing include sequence-number prediction, hijacking an authorized session, and determining the state of a firewall.
    
- **DoS attack:** In a DoS attack, an attacker attempts to prevent legitimate users from accessing information or services. By targeting your computer and its network connection, or the computers and network of the sites that you are trying to use, an attacker may be able to prevent you from accessing email, websites, online accounts, or other services that rely on the affected computers. Common types of DoS attacks include packet floods and service buffer overflow attacks. Other types of DoS attacks rely on specific flaws in various applications and operating systems, such as the "teardrop" attack which can crash older operating systems. For example, in a teardrop attack, the attacker sends IP fragmented packets to a target machine. Since the machine receiving such packets cannot reassemble them due to a bug in TCP/IP fragmentation reassembly, the packets overlap one another, crashing the target network device.
    
- **DDoS attack:** A distributed denial of service (DDoS) attack is a DoS attack that features a simultaneous, coordinated attack from multiple source machines. The best-known example of a DDoS attack is the "smurf" attack. Attackers have been known to use four programs to launch DDoS attacks: Trinoo, TFN, TFN2K, and Stacheldraht.
    
- **Smurf attack:** A smurf attack exploits the IP broadcast addressing to create a DoS. This attack uses the ICMP. One of the utilities that are embedded in ICMP is `ping` which is commonly used to test the availability of certain destinations. The attacker installs smurf on a hacked computer. The hacked machine starts continuously pinging one or more networks—with all their attached hosts—using IP broadcast addresses. Every host that receives the broadcast ping message is obliged to respond with its availability. The result is that the hacked machine gets overwhelmed with inbound ping responses.
    
- **Resource exhaustion attacks:** Resource exhaustion attacks are forms of DoS attacks. These attacks cause the server’s or network's resources to be consumed to the point where the service is no longer responding, or the response is significantly reduced. By targeting IP routers, an attacker may adversely affect the integrity and availability of the network infrastructure, including end-to-end IP connectivity. Router resources that are commonly affected by packet flood attacks include the following: CPU, packet memory, route memory, network bandwidth, and virtual type terminal (vty) lines.

# ICMP Vulnerabilities

The following are the security issues of ICMP messages that a security analyst needs to understand:

- **Reconnaissance and scanning**: ICMP can be used to launch information gathering attacks. Attackers can use different methods within the ICMP to find out live host, network topology, and OS fingerprinting, and determine the state of a firewall.
    
    1. **ICMP unreachables:** Commonly used by attackers to perform network reconnaissance. In cyber security, network reconnaissance refers to the act of scanning the target network to gather information about the target. For example, during a protocol or port scan, an ICMP Protocol Unreachable tells an attacker that a protocol is not in use on the target device. An ICMP Port Unreachable tells the attacker that a port is not in use on the target device.
        
    2. **ICMP mask reply:** A feature that malicious insiders or outsiders can use to map your IP network. This feature allows the router to tell a requesting endpoint what the correct subnet mask is for a given network.
        
    3. **ICMP redirects:** A router sends an IP redirect to notify the sender of a better route to the destination. The intended purpose of this feature was for a router to send redirects to the hosts on its directly connected networks. However, an attacker can use this feature to send an ICMP redirect message to the victim's host, luring the victim's host into sending all traffic through a router that is owned by the attacker. ICMP redirect attack is an example of an MITM attack, where an attacker will act as the middle man for all communication from the source to the destination.
        
    4. **ICMP router discovery:** ICMP Router Discovery Protocol (IRDP) allows hosts to locate routers that can be used as a gateway to reach IP-based devices on other networks. Because IRDP does not have any form of authentication, it is impossible for end hosts to tell whether the information they receive is valid or not. Therefore, an attacker can perform an MITM attack using IRDP. Attackers can also spoof the IRDP messages to add bad route entries into a victim’s routing table, so that the victim’s host will forward the packets to the wrong address, and be unable to reach other networks, resulting in a form of a DoS attack.
        
    5. **Firewalk:** Firewalking is an active reconnaissance technique that employs `traceroute`-like techniques to analyze IP packet responses to determine the gateway ACL filters and map out the networks. The firewalking technique works by sending out TCP or UDP packets with a TTL that is one greater than the targeted gateway. If the gateway allows the traffic, it will forward the packets to the next hop where they will expire and elicit an ICMP Time Exceeded Message. If the gateway host does not allow the traffic, it will likely drop the packets and the attacker will see no response.
        
- **ICMP tunneling:** An ICMP tunnel, also known as ICMPTX, establishes a covert connection between two remote computers, using ICMP echo requests and reply packets. ICMP tunneling can be used to bypass firewalls rules through obfuscation of the actual traffic inside the ICMP packets. Without proper deep packet inspection or log review, network administrators will not be able to detect this type of tunneling traffic through their network. A common ICMP tunneling program is LOKI that uses ICMP as a tunneling protocol for a covert channel. By using LOKI, an attacker can transmit data secretly by hiding their malicious traffic inside ICMP so that the networking devices cannot detect the transmission.
    
- **ICMP-based OS fingerprinting:** OS fingerprinting is the process of learning which operating system is running on a device. ICMP can be used to perform an active OS fingerprint scan. For example, if the ICMP reply contains a TTL value of 128, it is probably a Windows machine, and if the ICMP reply contains a TTL value of 64, it is probably a Linux-based machine.
    
- **Denial of service attacks:** DoS attacks that use ICMP include the following:
    
    1. **ICMP flood attack:** The attacker overwhelms the targeted resource with ICMP echo request (ping) packets, large ICMP packets, and other ICMP types to significantly saturate and slow down the victim's network infrastructure. The following figure is an example of the ICMP Flood. 
    ![6](/Course-Notes/.assets/Pasted_image_20241112165721.png)
    2. **Smurf attack:** In a smurf attack, an attacker broadcasts many ICMP echo request packets using a spoofed source IP address (which is the victim's IP address) to a network using an IP broadcast address. If networking devices do not filter this traffic, then they will be broadcasted to all computers in the network. The victim’s network will get congested with all the ICMP echo replies traffic, which will bring down the productivity of the entire victim's network. This exchange is illustrated in the following figure.
    ![5](/Course-Notes/.assets/Pasted_image_20241112165744.png)

# TCP Vulnerabilities
## TCP SYN Flooding
DoS attack that exploits a TCP characteristic (SYN, SYN-ACK, ACK) to make server processes unable to respond. 
Any service that binds to and listens on a TCP socket is vulnerable.

Half-open connections, initiated but not finished. 
SYN->/<-SYN-ACK. If the handshake is not completed, the connection stays in the half-open state indefinitely, occupying the finite-sized data structure. If there are enough half-open connections to fill it, the host becomes disabled.

![4](/Course-Notes/.assets/Pasted_image_20241112172201.png)
Setting a time limit for half-open connections, then deleting them after the timeout, can help with the TCP SYN flooding problem, but the attacker may continuously send the TCP SYN flood attack traffic. The attacked host will not have space to accept new incoming legitimate TCP connections, but the TCP connection that was established before the attack will have no effect. In this type of attack, the attacker has no interest in examining the responses from the victim. When the spoofed address does belong to a connected host, that host sends a reset to indicate the end of the handshake.

![3](/Course-Notes/.assets/Pasted_image_20241112173537.png)

### Variations

**Direct attack:** When attackers rapidly send SYN segments without spoofing their IP source address, that is a direct attack. 
-  It can be performed by simply using many TCP `connect()` calls. To be effective, attackers must prevent SYN-RECEIVED. They prevent their OS from responding to the SYN-ACK in any way. Any ACKs, resets (RSTs), or ICMP messages will release the allocation. 
- This can be accomplished through firewall rules that either filter outgoing packets to the listener (allowing only SYNs out), or filter incoming packets so that any SYN-ACKs are discarded before they reach the local TCP processing code. 
	- To Prevent this attack a simple firewall rule to block packets with the attacker's source IP address is all that is needed. This defense behavior can be automated, and such functions are available in off-the-shelf reactive firewalls.
    
- **Spoofing-based attack:** The attacker also needs to be able to form and inject raw IP packets with valid IP and TCP headers. Popular libraries exist to aid with raw packet formation and injection, therefore attacks that are based on spoofing are actually fairly easy. 
- For spoofing attacks, the machines at the spoofed source addresses must not respond in any way to the SYN-ACKs that are sent to them. 
- Another option is to spoof many different source addresses, assuming that some percentage of the spoofed addresses will be unrespondent to the SYN-ACKs. This option is accomplished either by cycling through a list of source addresses that are known to be desirable for the purpose, or by generating addresses inside a subnet with similar properties.
	- The real limitation of single-attacker spoofing-based attacks is that if the packets can somehow be traced back to their true source, the attacker can be easily shut down. Although the tracing process typically involves some time and coordination between ISPs, it is not impossible.
    
- **Distributed attacks:** The attacker takes advantage of numerous drone machines throughout the Internet to act on their behalf through a C&C. But to increase the effectiveness even further, each drone could use a spoofing attack and multiple spoofed addresses. Currently, distributed attacks are feasible because there are several "botnets" or "drone armies" of thousands of compromised machines that are used by criminals for DoS attacks. Drone machines are constantly added or removed from the armies and can change their IP addresses or connectivity, so it is quite challenging to block these attacks.

## TCP Session Hijacking

TCP hijacking is the oldest type of session hijacking. 
The attempt to overtake an already active session between two hosts. With IP spoofing, you still need to authenticate to the target. With TCP session hijacking involves spoofing the address of an already-authenticated host as it communicates with the target. The attacker will probably spoof the IP address or MAC address of the host.

As discussed earlier, sequence numbers are exchanged during a TCP three-way handshake, as follows:

1. Host A sends a SYN bit set packet with a sequence number to Host B to establish a TCP session. The sequence number is used to assure the transmission of packets in a chronological order. It is increased by one with each octet of data. Both sides of the connection wait for a packet with a specified sequence number. The first seq-number for both directions is random.

2. Host B will reply with a packet that has the SYN and ACK bits set and contains an initial sequence number. The packet also contains an acknowledgment number, which is the seq-number of the client + 1.

3. Host A will reply with an ACK bit set packet to Host B with initial sequence number (ISN) + 1.


Systems with poor TCP ISN generation are vulnerable to blind TCP spoofing attacks. If attackers manage to predict the ISN, they can actually send the last ACK data packet to the server, spoofing as the original host, and then hijack the TCP connection. Attackers can make a full connection to those systems and send, but not receive, data while spoofing a different IP address. The target's logs will show the spoofed IP address, and the attacker can take advantage of any trust relationship between the server and the client. This attack was popular in the mid-90's when people commonly used `rlogin`, which is a remote shell protocol. (rsh) (similar to SSH) that allows users to log in on another host via the network, communicating using TCP port number 513. While the `rlogin` family is mostly a thing of the past, other types of session hijacking are still actively being used. 

Session hijacking can also be done at the application level. At the application level, a hijacker can hijack already existing sessions but can also create new sessions from the stolen data, for example, HTTP session hijacking. Hijacking an HTTP session involves obtaining the session ID of the HTTP session, which is the unique identifier of the HTTP session. One way for the attacker to obtain the session ID is by sniffing the HTTP packets. Tools that can be used to perform session hijacking attacks include Juggernaut, Hunt, TTY Watcher, and T-Sight.

Hijacking a TCP session requires an attacker to send a packet with a right seq-number, otherwise they are dropped. The attacker has two options to get the right seq-number:

1. **Non-blind spoofing:** The attacker can see the traffic that is being sent between the host and the target. Non-blind spoofing is the easiest type of session hijacking to perform, but it requires attacker to capture packets as they are passing between the two machines. Spoofing-based attacks were discussed earlier in TCP SYN flooding attack methods.

2. **Blind spoofing:** The attacker cannot see the traffic that is being sent between the host and the target. Blind spoofing is the most difficult type of session hijacking because it is nearly impossible to correctly guess TCP sequence numbers. TCP sequence prediction is a type of blind hijacking because an attacker needs to make an educated guess on the sequence numbers between the host and target. In TCP-based applications, sequence numbers inform the receiving machine which order to put the packets in if they are received out of order. Sequence numbers are a 32-bit field in the TCP header. Therefore, they range from 1 to 4,294,967,295. Every byte is sequenced, but only the sequence number of the first byte in the segment is put in the TCP header. To effectively hijack a TCP session, you must accurately predict the sequence numbers that are being used between the target and host.

## TCP Reset Attack

The TCP reset attack, also known as forged TCP reset or spoofed TCP reset packet, is a technique of maliciously killing TCP communications between two hosts. A TCP connection is terminated by using the FIN bit in the TCP flags or by using the RST bit. The regular way that a TCP connection is torn down is by using the FIN bit in the TCP flags. One side of the connection sends a packet with the FIN bit set. The other side of the connection responds with two packets, an ACK, and a FIN of its own. This last FIN is acknowledged by the original station, indicating that the connection has been closed on both sides, as shown in the figure below.

![2](/Course-Notes/.assets/Pasted_image_20241112182640.png)

Closing a connection can also be done by using the RST bit in the TCP flags field. In most packets, the RST bit is set to 0 and has no effect. If the RST bit is set to 1, it indicates to the receiving computer that the computer should immediately stop using the TCP connection. A reset indicates that this connection is considered closed, and there is no need to send additional packets. A reset is an abrupt way to tear down the TCP connection. Resets are commonly seen when TCP data packets are sent to a server where no connection has been established, or when SYNs are sent to a port that the server is not listening on. The server should reply with a reset, showing that the connection is closed or unavailable, as shown in the figure below.

![1](/Course-Notes/.assets/Pasted_image_20241112182648.png)

Resets can also be sent by applications when a user is suddenly kicked out of an application. When the RST bit is used as designed, it can be a useful tool. But it is possible for an attacker to monitor the TCP packets on the connection and then send a spoofed packet containing a TCP reset to one or both endpoints. The headers in the spoofed packet must indicate, falsely, that the RST packet came from the victim host and not from the attacker. Every field in the IP and TCP headers must be set to a convincing spoofed value for the fake RST packet to trick the victim host into closing the TCP connection. Properly formatted spoofed TCP resets can be a very effective way to disrupt any TCP connection that the attacker can monitor.

# UDP Vulnerabilities

UDP is vulnerable because of the optional checksum. There is no Verification management and is easy to recompute allowing alteration of application data. (NFS, SNMP, DNS, TFTP, and other realtime services such as online games, streaming media, and VoIP)

SNMPv1 and DNS messages use UDP as transport protocol, and are vulnerable to eavesdropping. It is easy for an attacker see and change, as long as the messages aren't encrypted and attacker knows the format of the messages.

Most attacks involving UDP relate to exhaustion of some shared resource (buffers, link capacity, and so on), or exploitation of bugs in protocol implementations, causing system crashes or other insecure behavior. 

### UDP flood 
Or UDP Unicorn attacks are triggered by sending many UDP packets to random ports on the victim's system. The victim's system will notice that no application is listening on that port and reply with an ICMP destination port unreachable packet. If many UDP packets are sent, the victim will be forced to send numerous ICMP destination port unreachable packets. Usually, these attacks are accomplished by spoofing the attacker's source IP address. Software, such as Low Orbit Ion Cannon and UDP Unicorn, can be used to perform UDP flooding attacks. 
