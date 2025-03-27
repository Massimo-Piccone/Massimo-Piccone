%% #review %%
## [[Security Incident Investigation Procedures]]

Problem-Solving Steps

1. **Identify the alert**: Review the IDS/IPS alert to gather initial information.
2. **Determine 'Who'**: Analyze the source IP/domain associated with the alert.
3. **Determine 'What'**: Identify the type of malware involved, if possible.
4. **Determine 'When'**: Check the timestamp of the alert to understand the timing of the event.
5. **Determine 'Where'**: Use geolocation tools to find the physical location of the source IP.
6. **Determine 'Why'**: Investigate the purpose of the malware and its intended impact.
7. **Determine 'How'**: Analyze the infection vector to understand how the malware entered the system.

### Tools for Geolocation

> Various tools can assist in determining the geolocation of an IP address, including:

- **VirusTotal**
- **WhatsMyIP.com**
- **IPCIM.com**
- **checkIP.org**
- **IP Location Finder**
- **IP2Location**
%% Caution: The accuracy of these tools can vary, and the data is only as reliable as the sources used. %%
##### Windows Path Analysis

 The Windows `tracert` command can help visualize the path of packets across the network.

```
C:\Users\test> tracert www.cisco.com
Tracing route to e144.dscb.akamaiedge.net [184.24.164.198] over a maximum of 30 hops:
  1     9 ms   10 ms     2 ms  192.168.1.1
  2    18 ms   16 ms    27 ms  209.165.200.233
  3    18 ms   23 ms    19 ms  te-0-3-0-11-sur04.sanmateo.ca.sfba.comcast.net [68.87.196.45]
  4    16 ms   18 ms    20 ms  hu-0-16-0-0-ar01.hayward.ca.sfba.comcast.net [68.87.194.25]
  5    20 ms   19 ms    20 ms  be-33651-cr01.9greatoaks.ca.ibone.comcast.net [68.86.94.153]
  6    18 ms   22 ms    19 ms  hu-0-10-0-0-pe03.11greatoaks.ca.ibone.comcast.net [68.86.85.214]
  7    20 ms   18 ms    23 ms  ae-13.r02.snjsca04.us.bb.gin.ntt.net [129.250.66.33]
  8    25 ms   18 ms    19 ms  ae-46.r01.snjsca04.us.bb.gin.ntt.net [129.250.6.158]
  9    23 ms   19 ms    18 ms  a184-24-164-198.deploy.static.akamaitechnologies.com [184.24.164.198]
Trace complete.
```
### Geolocation Data Insights

> Geolocation services provide various data points, including:

- **Country**
- **Region**
- **City**
- **ZIP code**
- **Longitude and latitude**
 
 >Accuracy rates for city-level identification can range from 50% to 80%, while nation-state identification is often 95-99% accurate.

### Malware Identification and Analysis

- **VirusTotal**: A website that analyzes files and URLs for viruses, worms, trojans, and other kinds of malicious content.
- **Malwr.com**: A sandbox environment for analyzing malware behavior and capabilities.
### Common Infection Vectors

- Malware often enters systems through malicious email attachments or links that users inadvertently execute.
- Cleverly crafted websites can trick users into downloading malicious files, often disguised as security software.
- Web browsers like Google Chrome provide warnings against suspicious sites, but users may ignore these alerts.

### Analyzing Infection Methods

- Analysts can verify the presence of alerts on host systems to trace the delivery method of malware.
- Full packet captures and tools like ELSA can help identify previous communications with suspicious IP addresses.
- Understanding the delivery mechanism is crucial for preventing future infections and enhancing security measures.