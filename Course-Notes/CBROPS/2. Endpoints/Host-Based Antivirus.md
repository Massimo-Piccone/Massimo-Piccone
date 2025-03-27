HIPS combines the capabilities of antivirus, antispyware, and personal firewall software.

Host-Based Intrusion Prevention Systems can be Any combination of these:

- Signature-Based IPS
	-  Compare traffic to signatures
	- Signatures detect attacks & vulnerabilities
	- Must update signatures
	- Need signatures for new threats

- Anomaly-Based IPS
	- Relies on a base-line
	- Evaluates traffic
	- Uncharacteristic traffic patterns trigger alerts

- Policy-Based IPS
	- Policies are strictly followed
	- Policy defined what traffic is acceptable
	- Policies can be modified
	- Policy violations will send alerts

# Host-Based Malware Protection
commercial products for malware detection can realistically achieve about 40 percent success in detection.

AMP = Advanced Malware Protection

Cisco AMP for Endpoints

- It provides cloud-based detection of malware through the Cisco Talos Threat Intelligence Cloud, which is a powerful alternative to traditional malware detection and that offers these features:
    
    1. Rapid detection of known malware by examining the file's SHA
        
    2. Use of cloud resources to test files with unknown dispositions
        
    3. Use of machine learning techniques to constantly keep itself up-to-date
        
- Cisco AMP provides a historical perspective so that you can see, over time, the actions that files performed on a system. You can trace back an infection and identify the root cause. The history gives you visibility into the following:
    
    1. **File trajectory:** Shows you the hosts where files were seen
        
    2. **Device trajectory:** Shows you the actions that files performed on a given host
        
- You can block malicious network connections based on the following:
    
    1. Security intelligence feeds (IP reputation)
        
    2. Custom IP blocked lists
        
- Because malware that employs stealth techniques to hide its true intent may not initially be identified as malicious, the machine learning and behavior monitoring engines in the cloud may change the disposition of a file from "unknown" to "malicious." Such a change is known as retrospective alerting, or cloud recall. In other words, Cisco AMP for Endpoints can go back to the systems where the file was previously seen and alert the client to the changed disposition and quarantine the file.
    
- You can deploy simple custom detections or advanced custom detections in which you can create your own signatures for malware detection.
    
- Management is facilitated by giving you the ability to create groups of hosts which can run different policies to suit the detection needs of specific environments.
    
- Cisco AMP for Endpoints also provides robust reporting tools.
    

As shown in the figure below, Cisco AMP for Endpoints consists of the following elements:

- **Cisco Talos Threat Intelligence Cloud:** Cisco AMP cloud is constantly updated with information from Cisco Talos and Threat Grid to provide real-time threat intelligence. It is also where Cisco malware detection and analytic engines reside.
    
- **Client Connectors:** Components that run on the endpoints. Client Connectors communicate with the cloud to send information about files and to receive file disposition information.
    
- **Cisco AMP for Networks:** Gives Firepower devices the ability to query the cloud to obtain file disposition information on files that are detected by the Firepower device.

![2](/Course-Notes/.assets/Screenshot_2024-11-11_at_18.39.10.png)


## [Cisco Talos Threat Intelligence Cloud](https://www.talosintelligence.com/docs/Talos_WhitePaper.pdf)
The most critical component of the overall Cisco AMP for Endpoints architecture is the Cisco Talos Threat Intelligence Cloud.

Cisco Talos, the primary threat information contributor to the Cisco Security ecosystem, combines intelligence infrastructure, telemetry, public and private feeds, and Open Source threat intel. The Cisco Talos Security Intelligence and Research Group comprises leading threat researchers with sophisticated systems to create threat intelligence for Cisco products. As the world’s largest private threat intelligence and research team, Cisco Talos maintains the official rulesets of Snort.org, ClamAV, SenderBase.org, and SpamCop.

- **Detection publishing:** Detection signatures are in the cloud, which reduces the size of the client connector and reduces the amount of processing that has to take place on the connector, since the bulk of the work is being performed in the cloud.
    
    1. Administrators can create custom signatures in the cloud and push them down to the endpoint connectors.
        
    2. Cross-referencing of files and signatures is done in the cloud, so the cloud is self-updating without having to communicate those updates to endpoints every time.

- **Large-scale data processing (big data):** Data comes to the cloud from many sources.
    
    1. File samples are provided to the cloud for processing. If the disposition of a given sample is deemed malicious, it is stored in the cloud and reported to endpoints that see the same file.
        
    2. An important design goal of the cloud is to provide results as quickly as possible, so low latency is a key characteristic.
        
    3. The cloud includes advanced analytic engines that constantly correlate the incoming data. It uses the analytic results to update its signatures.
        
    4. It also includes machine-learning engines to further refine its signatures and reevaluate the detections that it has already performed.

- **Decision making** **that is** **performed real time:** The cloud is not just a repository for signatures—it evolves, based on the data that it receives.

- **Reporting:** The cloud applies its analytic capabilities to provide robust reporting capabilities.

## Next-Generation Endpoint Security

Next-generation endpoint security combines preventative protection with continuous detection and response capabilities. It includes continuous monitoring, rapid time to detection, and architectural integrations.

An endpoint protection platform (EPP) provides integrated endpoint security with personal firewall, port and device control, and anti-malware capabilities. EPP is often described as a traditional antivirus solution that scans files for malicious threats in a threat intelligence database.

While antivirus solutions scan, detect, and remove identified viruses, they cannot protect against signatureless and fileless malware threats. Deploying an antivirus solution improves front-line security but doesn’t protect endpoint host systems from sophisticated network-based threats.

An effective endpoint protection platform needs to apply advanced anti-malware capabilities such as:
- **Machine learning:** Machine learning capabilities allow the endpoint protection platform to use large-scale data to determine the true malicious nature of files.
- **Threat intelligence:** Expansive threat intelligence allows the EPP to use both historical and real-time data from billions of threats to automatically block known malefactors. 
- **Sandboxing:** Sandboxing allows the endpoint protection platform to isolate suspect files into a safe environment. Within this environment, the endpoint protection platform can safely detonate and monitor the nature of the files without risking detriment to the rest of the system.

Endpoint security solutions should have both endpoint protection platform and endpoint detection and response (EDR) solution capabilities. EDR solutions detect threats across a network environment, investigating the entire threat lifecycle to provide insights into its origin, behavior, and prevention strategies.

![1](/Course-Notes/.assets/Screenshot_2024-11-11_at_18.44.08.png)

By containing threats at the endpoint, EDR solutions eliminate and prevent them from spreading. While EPP (or traditional antivirus) solutions block most threats, EDR solutions detect, investigate, and remediate advanced and persistent threats that evade traditional perimeter defenses. EDR solutions can also detect threats beyond signature-based attacks, such as fileless malware, ransomware, and polymorphic attacks.

Key capabilities of endpoint detection and response:

- **Detection:** Threat detection is a foundational capability of an EDR solution. With continuous file analysis, an EDR solution will be able to flag offending files at the first sign of malicious behavior. 
    
- **Containment:** After detecting a malicious file, an EDR solution must be able to contain the threat. Malicious files aim to infect as many processes, applications, and users as possible. 
    
- **Investigation:** Once the malicious file has been detected and contained, an EDR solution should investigate. In the investigative process, sandboxing is a critical capability. Sandboxing can be used at the perimeter, to help permit or deny access, but it can also be used effectively after the point of entry. Sandboxing is when the file is isolated into a simulated (virtual) environment where it is tested and monitored for elicit behaviors.
    
- **Elimination:** The most obvious component of an EDR solution needs to be its ability to eliminate the threat. An EDR solution should provide actionable data on the lifespan of the file. If the EDR solution has retrospective capabilities, this actionable data should be used to automatically remediate systems to their state prior to infection.

An EDR solution targets advanced threats that evade front-line defenses and enter the network. An endpoint protection platform focuses solely on prevention and should be paired with an EDR solution. A comprehensive endpoint security solution includes both EPP and EDR capabilities. Cisco AMP for Endpoints provides next-generation capabilities to prevent attacks and quickly detect and respond to advanced malware. Cisco AMP for Endpoints continuously monitors network endpoints for malicious behavior, indicators of compromise, and decreases time to detection. Cisco AMP for Endpoints also provides response capabilities to contain and eliminate threats.
