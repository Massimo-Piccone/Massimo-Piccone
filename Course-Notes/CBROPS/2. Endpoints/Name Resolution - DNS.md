## Name Resolution Configuration Files

#### **resolv.conf** 
Primary configuration file for DNS name resolution. You will often find this file in the **/etc** directory. The **resolv.conf** is a simple text file that contains a series of directives for configuring name resolution. There are two types of directives:

- **Search domain:** This directive lists domains to append when resolving a hostname with no domain.
- **Name server:** This directive identifies the IP addresses of the DNS servers to use for resolving hostnames.

##### Security considerations  
- **Name servers or domains** that are not valid for your organization. Be advised however that certain devices such as laptops that tend to roam may have other domains or DNS servers that are listed here if you view the file before connecting the device to local network resources.
- **Public DNS server entries**. In particular, the Google public DNS servers with IP addresses such as 8.8.8.8, 8.8.4.4, or 4.2.2.1. There are other public DNS servers too, so it may be wise to have a list of common servers that you can reference. Often times, public servers are used to get around enterprise DNS servers that may be enforcing usage policies through DNS sink holes or IP blocked lists.

#### **nsswitch.conf**
The operating system looks at nsswitch.conf to determine how the host name is will be translated to an IP address.

- **files:** Represents local files on the host
- **compat:** Similar to **files**, but extends its capabilities by allowing entries in the files to grant users or user groups access to the system
- **dns:** Reference DNS servers
- **db:** Do lookups in database files on the local system

##### Security considerations  

1. A user on the system executes malware.
2. The malware creates an entry in the /etc/hosts file with the IP address of malicious web server.
    1. The malicious web server is configured to look like a banking website that is frequented by the operator of the system.
    2. The IP address of the entry in the /etc/hosts file maps to the hostname of the user’s banking website.
3. The malware also configures the **nsswitch.conf** file to do a file lookup first followed by a DNS lookup.
4. The next time that the user goes to visit the banking site, the host looks at the **/etc/hosts** file first and finds the name of the banking site in the file.
    1. The IP address that is mapped to the banking site is that of the malicious server that is disguised as the real banking site.
    2. Since the name was resolved with the **/etc/hosts** file, there is no need to reach out to DNS to resolve the name. 
5. The user is presented with a web page that looks exactly like his or her regular banking site’s page.
6. The user enters his or her banking credentials which the malicious server records.
7. Instead of granting the user access to his or her bank account, the malicious server pops up a message indicating that the banking site is down for maintenance and to try again later.

## Testing Name Resolution

### `nslookup` 

```
ed@ubuntu:/usr/lib/systemd$ nslookup 72.163.4.161

Server:127.0.1.1
Address:127.0.1.1#53

Non-authoritative answer:
161.4.163.72.in-addr.arpaname = www1.cisco.com
```

### `whois`

```
ed@ubuntu:/usr/lib/systemd$ whois 72.163.4.161

#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/whois_tou.html
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/public/whoisinaccuracy/index.xhtml
#
#
# The following results may also be obtained via:
# https://whois.arin.net/rest/nets;q=72.163.4.161?showDetails=true&showARIN=false&showNonArinTopLevelNet=false&ext=netref2
#
NetRange:       72.163.0.0 - 72.163.255.255
CIDR:           72.163.0.0/16
NetName:        CISCO-GEN-7
NetHandle:      NET-72-163-0-0-1
Parent:         NET72 (NET-72-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       
Organization:   Cisco Systems, Inc. (CISCOS-2)
RegDate:        2006-10-24
Updated:        2015-08-13
Ref:            https://whois.arin.net/rest/net/NET-72-163-0-0-1
```
