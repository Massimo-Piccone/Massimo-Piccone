DNS service enables access to the network resources by their names instead of having to remember their IP addresses.

- ==DNS Mapping Types: ==DNS uses resource records (==RRs==) for various mappings, including hostname to IP address (==A record==), domain name to mail servers (==MX record==), and name server for a domain (==NS record==).

![9](/Course-Notes/.assets/Pasted_image_20241118122243.png)

- ==Resource Record Examples==: Examples of resource records include A records for mapping hostnames to IPv4 addresses, MX records for mapping domain names to mail servers, and NS records for specifying the name server for a domain.

- ==DNS Server Example==: An example from a Microsoft DNS server shows how A records map hostnames (e.g., hq-srv, inside-srv) to IP addresses (e.g., 192.168.1.2) within the secure-x.local domain, with the hq-srv host acting as the name server.

![8](/Course-Notes/.assets/Pasted_image_20241118122305.png)

- ==DNS Resolver==: The client side of DNS responsible for resource-mapping.
- ==DNS Query==: A request sent by a DNS resolver to a DNS server for information defined in an RR.
- ==Resource Record (RR)==: Information defined in a DNS query.

- ==DNS Importance==: Critical protocol for network operations.
- ==DNS Vulnerabilities==: Weak implementation allows for malicious activities.
- ==Security Analysts’ Role:== Understand DNS to detect DNS-based attacks.

## DNS Ports

- ==DNS Query Protocol==: Primarily uses UDP port 53 for DNS queries and responses.
- ==DNS Response Protocol==: Uses TCP port 53 when the DNS response data size exceeds 512 bytes or for zone transfers.
- ==Zone Transfer==: Used by DNS administrators to replicate DNS databases across a set of DNS servers.

## DNS Distributed Database

- ==DNS Database Structure==: A globally distributed, scalable, hierarchical, and dynamic database with no single server containing the entire database.

- ==Domain Name Space==: A tree-like data structure of linked domain names, starting from the root (represented by a dot) and branching into subdomains.

- ==Fully Qualified Domain Name (FQDN)==: A hierarchical representation of a domain name, with each label separated by a dot and the top-level domain (TLD) at the far right.

![7](/Course-Notes/.assets/Pasted_image_20241118122938.png)

## DNS Terminology

- ==Resource Record (RR)==: Defines DNS DBdata types, including SOA, A/AAAA, MX, NS, PTR, and CNAME. Composed of NAME, TYPE, CLASS, TTL, RDLENGTH, and RDATA fields.
- ==stub DNS resolvers== are simple DNS resolvers on client devices that send DNS queries to recursive DNS resolvers to resolve domain names.
- ==DNS Recursive Resolver==: Processes client DNS queries by querying authoritative DNS servers and returning the answer. (Resolves DNS queries on behalf of clients.)
- ==Open DNS Recursive Resolver==: Allows queries from all IP addresses, potentially vulnerable to DDoS attacks.
- ==Authoritative DNS Server Role==: is responsible for managing the resource records (RRs) for a domain and providing authoritative responses to DNS queries.
- ==DNS Query Flow==: 
	1. Stub DNS resolver issues DNS queries to the DNS recursive resolver.
	2. The **DNS recursive resolver** queries the necessary **authoritative DNS servers** for the resource record information.
	3. The **authoritative DNS servers** provide the authoritative responses back to the **DNS recursive resolver**.
	4. The **DNS recursive resolver** then provides the answer back to the **DNS client**.
- ==DNS Zones==: 
	1. Contiguous portions of the DNS namespace
	2. Managed by a single administrative authority
	3. The authoritative source for the domains within the zone
	4. Defined in a zone file containing the resource records

## DNS RR Types

DNS Resource Record Types:

- ==**A record==:** Used to map host names to the IPv4 address of the host. In an A record, multiple IP addresses can correspond to a single hostname. There can also be multiple host names each of which maps to the same IP address. There must be a valid A record in the DNS for the host.domain.name in order for a command, such as `telnet host.domain.name`, to work.
- ==**AAAA** **record==:** AAAA is used to map hostnames to the IPv6 address of the host.
- ==**MX** **record==:** MX maps a domain name to a list of mail servers for that domain.
- ==**PTR** **record==:** A PTR points to a canonical name. The most common use is for implementing reverse DNS lookups, mapping an IP address to the hostname.
- ==**NS record==:** An NS record identifies the DNS servers that are responsible (authoritative) for a zone.
- ==**CNAME record**==: A CNAME record is used to specify that a domain name is an alias for another domain name, which is the "canonical" domain name.
- ==**TXT record==:** A TXT record is used to associate any arbitrary text with a hostname. This record type is only used in specific cases such as Domain Keys Identified Mail, used as a method to detect email spoofing.
- ==**SOA record==:** Each zone contains an SOA record. The SOA record identifies the name server that is the best source of information for the data within the zone. The SOA record also contains various other parameters that define the behavior of the DNS server.

## The `nslookup` Utility

A network utility for querying DNS databases, resolving domain names, and examining DNS records.


- **==A record==:** Using the `nslookup` utility, it shows that the **dmz.secure-x.public** host that is resolved to the IP address of 192.0.2.50 from the 209.165.200.233 DNS server, and the 209.165.200.233 DNS server is not the authoritative DNS server for the secure-x.public domain.
	![6](/Course-Notes/.assets/Pasted_image_20241118134959.png)

- ==**PTR record**==: In this example, using the `nslookup` utility, the `set q=ptr` option can be used to examine the PTR record. In this example, the PTR record from DNS shows 192.0.2.50 resolves to the various hostnames in the secure-x.public domain, such as dmz.secure-x.public.
	![5](/Course-Notes/.assets/Pasted_image_20241118135006.png)

- ==**MX record==:** In this example, using the `nslookup` utility, the `set q=mx` option can be used to examine the MX record. In this example, the MX record from DNS shows that 192.0.2.55 is the mail server for the secure-x.public domain.
	![4](/Course-Notes/.assets/Pasted_image_20241118135016.png)

# Dynamic DNS

The Dynamic Domain Name System (DDNS) automatically discovers and registers the client system’s public IP addresses. The DDNS client on the private network connects to the DDNS provider with a unique login name. The provider links the discovered public IP address with a hostname in the domain name system.

- Dynamic DNS (DDNS) Service: A service that maps a static domain name to a dynamic IP address, enabling connections to networks with dynamic IP addresses.

![3](/Course-Notes/.assets/Pasted_image_20241118140228.png)


- ==DDNS Use:== Enabling connections to networks with dynamic IP addresses, such as hosting websites or connecting to home VPNs.
- ==DDNS Malicious Use:== Threat actors use DDNS for malicious purposes like launching attacks with persistent connections to CnC servers or data exfiltration.
- ==DDNS Usage by Attackers:== Attackers frequently use DDNS services for generating subdomains.

- ==Block Rate Comparison:== DDNS-based domain web traffic block rate is nearly 20%, significantly higher than the average block rate for all other web traffic (less than 1%).
- ==High Block Rate DDNS Domains: ==Many DDNS-based domains are blocked with almost 100% frequency.![2](/Course-Notes/.assets/Screenshot_2024-11-18_at_14.05.02.png)

# Recursive DNS Query

Understanding how the recursive DNS query process works is important to an analyst when dealing with DNS-based attacks and interpreting packet captures with DNS flows.

- ==DNS RR’s Role==: Retrieves DNS information from authoritative servers and provides it to the original DNS resolver.
- ==Recursive DNS Request Processing==: More processing is required compared to non-recursive DNS requests.
- ==Cached Information Handling==: The recursive DNS resolver may have cached information and respond with it directly.

1. The DNS resolver queries the recursor for www.cisco.com’s address.
2. The recursor queries the root name servers for the .com domain.
3. The root name servers refer the recursor to the generic Top-Level Domain (gTLD) name servers.
4. The recursor queries the gTLD name servers for the .com domain.
5. The gTLD name servers refer the recursor to the .cisco.com name servers, ns1.cisco.com or ns2.cisco.com.
6. The recursor queries ns1.cisco.com or ns2.cisco.com for www.cisco.com’s address.
7. ns1.cisco.com or ns2.cisco.com sends an authoritative DNS query response with the A (address) RR information for www.cisco.com.
8. The recursor sends the A (address) RR information for www.cisco.com to the resolver.

![1](/Course-Notes/.assets/Pasted_image_20241118141325.png)

