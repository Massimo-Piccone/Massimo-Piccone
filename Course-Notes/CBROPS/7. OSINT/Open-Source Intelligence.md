# [[Quick Reference]]

Key Techniques

|Technique|Description|
|---|---|
|**Domain Name Technique**|Uses domain names to gather information about IP addresses, registrant details, and related domains.|
|**IP Address Technique**|Involves using IP addresses to find associated domain names, organization details, and vulnerabilities.|
|**Email Technique**|Gathers information about email addresses, including validity, breaches, and associated personal data.|
|**Username Technique**|Searches for usernames across platforms to find social media accounts and related information.|
|**Real Name Technique**|Uses real names to find personal details, social profiles, and connections to other individuals.|

Key Tools

- **Shodan**: A search engine for discovering devices connected to the internet, providing information about their configurations and vulnerabilities.
- **Maltego**: A data mining tool that visualizes relationships between entities based on online data sources.
- **Recon-ng**: A web reconnaissance framework that allows users to gather information through various modules and store results in a local database.
- **VirusTotal**: An online service that analyzes files and URLs for malware and provides reputation scores based on community input.

Key Applications

- **Business Intelligence**: Companies use OSINT to inform market strategies, assess competition, and identify investment opportunities.
- **Law Enforcement**: Agencies utilize OSINT to validate intelligence, track criminal activities, and analyze social trends.
- **Cybersecurity**: Both blue teams (defensive) and red teams (offensive) use OSINT to identify vulnerabilities and enhance security measures.

Key Benefits and Drawbacks

- **Benefits**: OSINT provides a cost-effective way to gather vast amounts of data, which can enhance decision-making and threat assessment.
- **Drawbacks**: The reliability of OSINT data can be questionable, as it may include fabricated or biased information. Additionally, the public availability of OSINT means that both security professionals and threat actors can access the same information.

Facts to Memorize

- OSINT stands for Open-Source Intelligence.
- SOCMINT refers to Social Media Intelligence, a subcomponent of OSINT.
- The deep web includes content not indexed by standard search engines.
- The dark web is a part of the deep web that requires specific software to access and is often associated with illegal activities.
- Common OSINT techniques include domain name, IP address, email, CVE ID number, username, and real name searches.

Reference Information

- OSINT tools can be categorized into generic tools (like search engines) and dedicated tools (like Maltego and Shodan).
- The OSINT framework organizes tools based on technique, source, or purpose.
- Ethical compliance and data anonymization are crucial considerations in OSINT activities.

Problem-Solving Steps

1. Define your objective: Determine what information you need and why.
2. Identify seed data: Use known data points (like usernames or domain names) as starting points.
3. Choose appropriate tools: Select OSINT tools based on the type of data you are collecting.
4. Collect data: Use the tools to gather information, ensuring to document your sources.
5. Analyze and interpret: Process the collected data to extract actionable intelligence.
6. Validate findings: Cross-reference information to ensure accuracy and reliability.

Key Terms/Concepts

- **Open-Source Intelligence (OSINT)**: Intelligence derived from publicly available data, including information from the internet and other public sources.
- **SOCMINT**: Social media intelligence, a subcomponent of OSINT that focuses on information collected from social media platforms.
- **Deep Web**: The part of the internet that is not indexed by traditional search engines, requiring special access.
- **Dark Web**: A subset of the deep web that is intentionally hidden and inaccessible through standard web browsers, often associated with illegal activities.

# OSINT Overview

### Definition and Importance of OSINT

- OSINT refers to intelligence derived from publicly available data, which is crucial for threat investigations.
- The evolution of OSINT has shifted from secretive data collection to utilizing vast amounts of publicly accessible information.
- SOC analysts leverage OSINT to derive actionable intelligence without needing specialized training or permissions.

### Intelligence Generation Process

- The process begins with data collection from public sources, followed by processing, analysis, and interpretation.
- Intelligence must be ==actionable, relevant, and valuable== to be considered effective.
- The transformation of raw data into intelligence involves critical thinking and contextual understanding.

![13](/Course-Notes/.assets/Pasted_image_20241202222030.png)
### Characteristics of OSINT

- OSINT is characterized by its accessibility; it does not require special permissions or techniques to access.
- It encompasses various types of information, including published content, subscription-based data, and casual observations.
- The term 'open-source' extends beyond intelligence to include software and design documents that are publicly available.

### Examples of OSINT

- Information published for public consumption, such as news articles and reports.
- Data available upon request, like government statistics.
- Observational data from public events, such as seminars or concerts.

# OSINT Data Sources

![12](/Course-Notes/.assets/Pasted_image_20241202225001.png)
### Primary Sources of OSINT

- The internet serves as the primary source of OSINT, providing a wealth of information beyond traditional media.
- Key platforms include social networks (e.g., Facebook, Twitter), media-sharing sites (e.g., YouTube), and professional networks (e.g., LinkedIn).
- Academic and government websites also contribute valuable data for OSINT analysis.

### Deep Web and Dark Web

- The deep web consists of non-indexed content that requires special access, such as databases and subscription services.
- The dark web, a subset of the deep web, allows for anonymous exchanges and can contain sensitive information.
- Examples of dark web data include breached datasets and discussions on vulnerabilities.

### Legal and Ethical Considerations

- Accessing OSINT must comply with legal regulations and ethical standards, especially when dealing with sensitive data.
- The use of SOCMINT (social media intelligence) raises additional ethical concerns due to the nature of social media data.
- Analysts must navigate the balance between effective intelligence gathering and respecting privacy rights.

# OSINT Application

![11](/Course-Notes/.assets/Pasted_image_20241202225025.png)
### Use Cases in Various Sectors

- Businesses utilize OSINT for market analysis, competitive intelligence, and risk assessment.
- Law enforcement agencies apply OSINT to validate intelligence and track criminal activities.
- Government entities use OSINT for political analysis and disaster management strategies.

### Role of SOC Analysts

- SOC Tier 1 analysts employ OSINT to triage alerts and enrich data for better decision-making.
- OSINT is integral to incident investigation and threat hunting, providing context to digital evidence.
- Analysts must be adept at using OSINT tools and techniques to enhance their operational effectiveness.

### Offensive and Defensive Uses of OSINT

- Red teams use OSINT to identify vulnerabilities and simulate attacks, enhancing their offensive strategies.
- Blue teams leverage OSINT for defensive measures, including incident response and forensic analysis.
- The dual-use nature of OSINT highlights its importance in both cybersecurity and threat mitigation.

# Introduction to OSINT in Cybersecurity

### Definition and Importance of OSINT

- OSINT (Open Source Intelligence) refers to the collection and analysis of publicly available data to support decision-making in cybersecurity.
- It plays a crucial role in incident investigation, threat hunting, and forensic analysis by enriching digital evidence left by adversaries.
- Cyberattacks leave behind digital fingerprints, which OSINT helps to analyze for understanding attack motivations and profiling threat actors.

### Applications of OSINT

- OSINT is utilized in fraud detection by sourcing threat intelligence from public data, although its reliability can vary.
- Security professionals can leverage AI to track the propagation of threat intelligence across the internet, assessing its authenticity.
- Threat actors also exploit OSINT to identify targets and exploit weaknesses, tracing digital footprints for technical and non-technical information.

### Ethical Considerations in OSINT

- Ethical compliance is crucial when conducting OSINT activities to ensure responsible data collection and usage.
- Data anonymization is important to protect the identity of investigators and prevent threat actors from tracking their activities.
- Analysts must be aware of the potential misuse of OSINT techniques by malicious actors.

# Benefits and Drawbacks of OSINT

![10](/Course-Notes/.assets/Pasted_image_20241202225037.png)
### Advantages of OSINT

- The OSINT market is projected to grow significantly, providing organizations with a greater return on investment compared to other intelligence-gathering tools.
- A wide variety of data types are available, from simple data points like IP addresses to complex multimedia items, enhancing investigative capabilities.
- Advanced data processing techniques, including machine learning and AI, improve the quality of results derived from OSINT.

### Challenges and Limitations of OSINT

- The reliability of OSINT data can be questionable, as many sources may contain subjective or fabricated information.
- The prevalence of synthetic media, such as fake news and deepfakes, undermines the credibility of open-source data.
- Public availability of OSINT means that both investigators and threat actors have equal access to the same information, raising security concerns.

# OSINT Data Collection Techniques

![9](/Course-Notes/.assets/Pasted_image_20241202225044.png)
### Defining Goals for OSINT Collection

- Effective OSINT data collection begins with clearly defining the objectives, such as verifying a domain name's relation to malware.
- Initial input data, like usernames or IP addresses, serves as a seed for expanding the dataset relevant to the investigation.
- Choosing appropriate tools and techniques based on the type of data being collected is essential for effective analysis.

### The Recursive Nature of OSINT Collection

- OSINT collection is not linear; it involves a recursive process where outputs from one technique inform inputs for another.
- This iterative approach allows for a comprehensive gathering of information, enhancing the depth of analysis.
- Organizing collected data effectively is crucial for usability and analysis, ensuring that investigators can draw meaningful conclusions.

# OSINT Framework and Tools

![8](/Course-Notes/.assets/Pasted_image_20241202225058.png)
### Overview of the OSINT Framework

- The OSINT framework is a repository of tools categorized by technique, source, or purpose, facilitating open-source data collection.
- Common tools include search engines and specialized applications for specific data types, such as email addresses or usernames.
- The framework provides an interactive interface for browsing tools, with indicators for installation and registration requirements.

### Examples of OSINT Tools

- Tools for username searches include Namechk, KnowEm, and WhatsMyName, each with specific usage requirements.
- Domain name investigation tools include Mnemonic and DNS History, which help in tracking domain-related information.
- The organization of tools within the OSINT framework aids in systematic investigations, promoting creativity in data collection tasks.

# OSINT Framework Overview

### Introduction to OSINT

- OSINT (Open Source Intelligence) refers to the process of collecting and analyzing publicly available information for intelligence purposes.
- The OSINT framework provides a structured approach to facilitate systematic investigations.
- Browsing the OSINT framework website can inspire creativity in data collection tasks.
- OSINT is crucial for various fields, including cybersecurity, law enforcement, and competitive intelligence.

### Importance of Systematic Investigation

- Systematic investigation ensures thoroughness and accuracy in data collection.
- It helps in identifying relevant sources and tools for effective OSINT.
- A structured approach minimizes the risk of overlooking critical information.
- The OSINT framework categorizes tools based on their functionality, aiding in efficient data gathering.

# OSINT Data Collection Approaches

![7](/Course-Notes/.assets/Pasted_image_20241202225107.png)
### Passive vs. Active Collection

- ****Passive Collection****: Involves gathering data without direct interaction with the target, often using third-party sources.
- ****Active Collection****: Requires direct engagement with the target, which can expose the investigator's identity.
- The choice between passive and active collection affects the volume and quality of data obtained.
- Passive methods aim to remain undetected, while active methods may leave a digital footprint.

### Limitations of Each Approach

- Passive collection may yield limited data quality and quantity due to its non-intrusive nature.
- Active collection can lead to detection and potential countermeasures from the target.
- Security professionals often prefer active methods for sensitive data, despite the risks involved.
- Understanding the implications of each approach is crucial for effective OSINT operations.

# OSINT Techniques Overview

![6](/Course-Notes/.assets/Pasted_image_20241202225114.png)
### Common OSINT Techniques

- Techniques include domain name, IP address, email, CVE ID number, username, and real name searches.
- Each technique utilizes specific input types to gather relevant data.
- The effectiveness of a technique depends on the tools used and the nature of the input data.
- Legal considerations, such as GDPR, govern the use of collected data, emphasizing the importance of ethical practices.

### Data Input Types and Tools

- Input types can range from usernames to multimedia files, influencing the search results.
- Tools can be used in conjunction to refine and extend data collection.
- Publicly available OSINT tools are legal to use, but intent determines the legality of data usage.
- Examples of tools include VirusTotal for domain names and Have I Been Pwned for email searches.

# Detailed OSINT Techniques

### Domain Name Technique

- Utilizes domain names to gather information such as IP addresses, DNS records, and registrant details.
- Tools like Whois and VirusTotal provide insights into domain reputation and associated threats.
- Example outputs include DNS name servers, registration dates, and subdomain mappings.
- Understanding domain relationships can aid in identifying malicious activities.

### IP Address Technique

- Involves using IP addresses to obtain information about organizations, hosted domains, and potential vulnerabilities.
- Reverse lookup services can reveal associated domain names and ISP details.
- Tools like MaxMind and IP2Location help in gathering comprehensive data about IP addresses.
- Example outputs include organization location, web server technology, and SSL certificate details.

### Email Technique

- Email addresses serve as unique identifiers, making them effective for OSINT searches.
- Tools can verify email validity, check for breaches, and identify the owner’s details.
- Example outputs include the owner’s name, address, and social media profiles.
- Services like Verify Email and Have I Been Pwned are commonly used for email investigations.

### CVE ID Number Technique

- CVE (Common Vulnerabilities and Exposures) IDs provide insights into specific vulnerabilities and exploits.
- Databases like the National Vulnerability Database offer detailed information about threats.
- Example outputs include affected products, CVSS scores, and available solutions.
- Understanding CVEs is essential for cybersecurity professionals to mitigate risks.

### Username Technique

- Usernames can be derived from other data, allowing for cross-platform searches.
- Tools can verify username presence across social networks and suggest alternatives.
- Example outputs include lists of social media accounts and online community memberships.
- Services like Namechk and Usersearch facilitate username investigations.

### Real Name or People Search Technique

- Real names can yield valuable information when correlated with other data.
- Tools can provide personal details, social network profiles, and family connections.
- Example outputs include addresses, employment history, and educational background.
- Services like ThatsThem and Peek You are useful for real name searches.

# OSINT Tools

![5](/Course-Notes/.assets/Pasted_image_20241202225128.png)
### Overview of OSINT Tools

- OSINT tools range from generic search engines to specialized platforms for specific data types.
- Understanding the functionality of each tool is crucial for effective data collection.
- Tools can be categorized based on their input types and the nature of the data they provide.
- Familiarity with various tools enhances the investigator's ability to gather comprehensive intelligence.

### Examples of OSINT Tools

- ****Search Engines****: Google, Bing for general information gathering.
- ****Domain Tools****: Whois, VirusTotal for domain-related investigations.
- ****IP Tools****: MaxMind, IP2Location for IP address analysis.
- ****Email Tools****: Have I Been Pwned, Email Permutator for email validation.

# Introduction to OSINT Tools

### Overview of OSINT

- OSINT stands for Open Source Intelligence, which involves collecting and analyzing publicly available information.
- It is widely used in security analysis, law enforcement, and corporate investigations.
- OSINT tools can be categorized into generic tools, authoritative services, and OSINT-dedicated tools.
- The effectiveness of OSINT relies on the ability to filter and analyze vast amounts of data from various sources.

### Types of OSINT Tools

- OSINT tools can be open-source or commercial, with some offering free functionalities and others requiring payment.
- Examples of OSINT tools include search engines (Google, Bing), specialized tools (Maltego, Shodan), and social media analysis tools.
- Tools can be manual (requiring user input) or automated (collecting and processing data without user intervention).

# Consumer Search Engines in OSINT

![4](/Course-Notes/.assets/Pasted_image_20241202225205.png)
### Functionality of Search Engines

- Search engines are essential for accessing both the surface web and the deep web.
- Native search engines like Google and Bing use web crawlers to index content, while metasearch engines aggregate results from multiple sources.
- Examples of metasearch engines include DuckDuckGo and Swisscows, which prioritize user privacy.

### Advanced Search Techniques

- Advanced search techniques, known as 'dorking', help refine search results to find specific information.
- Common operators include ****site:**** (restricts to a domain), ****filetype:**** (limits to file types), and ****intitle:**** (restricts to document titles).
- Example of a search string: ****site:example.com phone**** returns pages from example.com containing the word 'phone'.

# OSINT Tools for Social Media

![3](/Course-Notes/.assets/Pasted_image_20241202225213.png)
### Data Extraction from Social Media

- Social media platforms generate unstructured data, which requires specialized tools for extraction.
- Tools like Google Social Search and Social Searcher can search across multiple platforms and filter results.
- APIs provided by social media platforms may not offer complete data access, limiting the information available.

### Specific Tools for Social Media Analysis

- Tools such as MIT’s TweeQL can map tweets geographically and analyze historical data.
- Social media data can reveal personal information, which can be exploited for security breaches, such as password cracking.
- Understanding the social footprint of an organization can be crucial for security assessments.

# Authoritative and Official Online Services

![2](/Course-Notes/.assets/Pasted_image_20241202225222.png)
### Cisco Talos Intelligence Group

- Cisco Talos is a leading commercial threat intelligence team providing various cybersecurity services.
- Their web portal offers access to lists of vulnerabilities, advisories, and reputation centers for domains and IPs.
- Users can check the reputation of domains, IP addresses, and files using input data such as IPv4/IPv6 addresses and CIDR ranges.

### Input Data for Reputation Checks

- Input examples include specific IP addresses (e.g., ****198.133.219.25****) and domain names (e.g., ****cisco.com****).
- Reputation centers help assess the security posture of a domain or IP, which is vital for threat analysis.
- Understanding the reputation of online entities can aid in identifying potential threats and vulnerabilities.

# Input Data for Reputation Centers

### Types of Input Data

- ****IPv4 and IPv6 Addresses****: Reputation centers accept both IPv4 (e.g., 198.133.219.25) and IPv6 addresses (e.g., 2001:420:1101:1::a) as input for evaluation.
- ****CIDR Ranges****: CIDR notation is also accepted, allowing for ranges of IP addresses (e.g., 198.133.219.25/24). This helps in assessing entire subnets.
- ****Domains and Hostnames****: Input can include standard domains (e.g., cisco.com) and internationalized domain names (e.g., 达彼思.香港).
- ****URIs****: Uniform Resource Identifiers can be submitted for analysis, although specific examples were not provided in the notes.
- ****Network Owner Information****: The reputation centers evaluate the input based on the network owner, such as Cisco Systems.
- ****Country Information****: Country data (e.g., United States) is also considered in the evaluation process.

### Threat Levels Evaluated

- ****Untrusted****: Indicates a high likelihood of malicious activity associated with the input.
- ****Questionable****: Suggests some risk but not enough evidence to classify as malicious.
- ****Neutral****: No significant evidence to suggest either trust or distrust.
- ****Favorable****: Indicates a generally positive reputation, with some evidence supporting this.
- ****Trusted****: Strong evidence of a good reputation, often associated with well-known entities.
- ****Unknown****: For inputs that have not been previously evaluated or lack sufficient data.

# Online Services for OSINT Information

### VirusTotal

- ****Functionality****: Analyzes files and URLs for malware detection and provides detailed reports on domains.
- ****Community Sharing****: Automatically shares findings with the security community, enhancing collective knowledge.
- ****Data Provided****: Includes serving IP addresses, server technology, social media accounts, and more.
- ****Hash Calculations****: Generates and shares hashes (e.g., SHA-256) for submitted files, contributing to a public database.
- ****Access Levels****: Offers free access with limitations, public access for members, and premium services for extensive use.
- ****Use Cases****: Ideal for quick checks on suspicious domains or files.

### AlienVault OTX

- ****Threat Data Platform****: Facilitates sharing of research results and threat investigation.
- ****Analysis Types****: Performs static and dynamic analysis on submitted files and URLs.
- ****Community Access****: Free for registered members, promoting collaborative threat intelligence.
- ****Data Types****: Provides malware analysis, threat data, trends, and an IP reputation list.
- ****Submission Methods****: Users can submit files and URLs via a web portal or API.
- ****Use Cases****: Useful for determining the maliciousness of files and URLs.

# Dedicated OSINT Tools

![1](/Course-Notes/.assets/Pasted_image_20241202225302.png)
### Shodan

- ****Search Engine for Devices****: Collects public information about internet-connected devices, including servers and IoT devices.
- ****Search Parameters****: Accepts various parameters like geographic locations, CVE IDs, and IP addresses to refine searches.
- ****Data Presentation****: Results are displayed in structured formats (.json, .csv, .xml) and reports.
- ****Vulnerability Assessment****: Helps evaluate internet exposure and detect vulnerabilities in publicly available services.
- ****Use Cases****: Ideal for tracking IoT devices and assessing security risks.
- ****Registration Requirement****: Free account needed for limited daily searches.

### Maltego

- ****Data Mining Tool****: Searches thousands of online data sources to identify relationships between entities.
- ****Transforms****: Applies processing transforms to generate output data, revealing connections between emails, phone numbers, and social accounts.
- ****Graphical Representation****: Results are presented in an interactive graph format, simplifying analysis.
- ****Automated Searches****: Allows for repetitive and sequential searches to gather comprehensive data.
- ****Community Version****: Available in Kali Linux, but requires registration for full access.
- ****Use Cases****: Effective for social network analysis and relationship mapping.

# Additional OSINT Tools

### Recon-ng

- ****Framework for Information Gathering****: Utilizes separate modules to perform various tasks and store results in a local database.
- ****Modular Design****: Users can add modules from the Recon-ng Marketplace to enhance functionality.
- ****Data Relationships****: Displays search results in a graph format, showing relationships between gathered items.
- ****Input Flexibility****: Output from one module can serve as input for another, facilitating complex queries.
- ****User Customization****: Users can sort and filter database data for tailored results.
- ****Use Cases****: Suitable for comprehensive reconnaissance and data aggregation.

### FOCA

- ****Metadata Extraction Tool****: Analyzes electronic documents to extract metadata, revealing sensitive information.
- ****File Collection****: Can collect files from web pages using search engines like Google, Bing, and DuckDuckGo.
- ****Supported Formats****: Extracts metadata from various file types, including Microsoft Office and PDF.
- ****Use Cases****: Useful for identifying potential information leaks and vulnerabilities in documents.
- ****User Interface****: Provides a straightforward interface for users to initiate searches and analyze results.
- ****Data Presentation****: Results are organized for easy interpretation and action.