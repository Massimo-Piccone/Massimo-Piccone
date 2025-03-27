# [[Quick Reference]]

Key Statistics

- **Average Time to Detect Incidents**: According to the 2015 Cisco annual security report, the average time to detect an incident is 200 days.
- **Improved Detection Time**: With proper processes and technologies, Cisco has reduced the average detection time to 46 hours.

Key Strategies for Incident Handling

- **Playbook**: A documented set of procedures and guidelines to assist organizations in detecting and responding to incidents.
- **Preparation**: Organizations should prepare for common attack vectors and develop specific incident-handling procedures.

Key Challenges

- **Detection Difficulty**: Accurately detecting incidents can be challenging due to the variety of attack methods and the need for detailed analysis.
- **Response Variability**: Different types of incidents require different response strategies based on their severity.

Facts to Memorize

- Average time to detect an incident: 200 days (Cisco 2015 report)
- Reduced average time to detect an incident: 46 hours (Cisco with proper measures)
- Common attack vectors include: External/removable media, Attrition, Web attacks, Email attacks, Impersonation, Improper usage, Loss or theft of devices.

Reference Information

- Incident response process involves detection, assessment, and response.
- Incident classifications are based on severity.

Key Terms/Concepts

- **Incident Response**: The process of detecting, responding to, and recovering from security incidents.
- **Attack Vector**: A method or pathway used by an attacker to gain access to a target system or network.
- **DDoS (Distributed Denial of Service)**: An attack that aims to make a service unavailable by overwhelming it with traffic from multiple sources.

%% [Source](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf) %%
# Table

| Attack Type                         | Description                                                                                       |
| ----------------------------------- | ------------------------------------------------------------------------------------------------- |
| External or removable media attacks | Malicious code spreading onto systems from infected USB flash drives or other peripheral devices. |
| Attrition attacks                   | Compromising, degrading, or destroying systems, networks, or services using brute-force methods.  |
| Web attacks                         | Occurring from or against websites or web-based applications.                                     |
| Email attacks                       | Involving executing malicious code via email messages or attachments.                             |
| Impersonation attacks               | Replacing benign elements with malicious ones.                                                    |
| Improper usage attacks              | Resulting from violating acceptable usage policies by authorized users.                           |
| Equipment loss or theft attacks     | Involving the loss or theft of computing devices or media.                                        |
| Other attacks                       | An attack that does not fit into another category                                                 |
# Incident Detection and Response

### Importance of Incident Detection

- Accurate detection of incidents is crucial for effective incident response, as it allows organizations to respond promptly and mitigate damage.
- The 2015 Cisco annual security report highlighted a concerning average detection time of 200 days, emphasizing the need for improved detection methods.
- Cisco's implementation of proper people, processes, and technologies reduced detection time to 46 hours, showcasing the impact of a structured approach.
- Organizations must develop a playbook to guide incident detection, ensuring consistency and efficiency in response efforts.
- The complexity of incidents necessitates a flexible approach, as not all incidents can be addressed with a one-size-fits-all solution.

### Incident Response Strategies

- Organizations should prepare for a variety of incidents, focusing on common attack vectors to streamline response efforts.
- Different types of incidents require tailored response strategies based on their severity and potential impact.
- Incident classifications help prioritize response efforts, ensuring that critical incidents receive immediate attention.
- A proactive approach to incident response includes regular training and updates to the incident response playbook.
- Continuous improvement of incident response processes is essential to adapt to evolving threats.

# Common Attack Vectors

### External/Removable Media Attacks

- Attacks can originate from removable media, such as USB drives, which may carry malicious code.
- Example: An infected USB flash drive spreads malware when connected to a system, compromising security.
- Organizations should implement policies to restrict the use of unverified external media to mitigate risks.
- Regular training on the dangers of external media can help raise awareness among employees.
- Monitoring and scanning of external devices upon connection can help detect potential threats.

### Attrition Attacks

- Attrition attacks utilize brute-force methods to compromise systems, networks, or services.
- Example: Distributed Denial of Service (DDoS) attacks aim to impair access to services by overwhelming them with traffic.
- Organizations should employ rate limiting and traffic analysis to detect and mitigate DDoS attacks.
- Implementing strong authentication mechanisms can help defend against brute-force attacks.
- Regularly updating and patching systems can reduce vulnerabilities that attrition attacks exploit.

### Web Attacks

- Web attacks target websites or web-based applications, exploiting vulnerabilities in their code.
- Example: Cross-Site Scripting (XSS) attacks can steal user credentials or redirect users to malicious sites.
- Organizations should conduct regular security assessments and code reviews to identify vulnerabilities.
- Implementing Content Security Policies (CSP) can help mitigate the risk of XSS attacks.
- User education on recognizing phishing attempts can reduce the effectiveness of web-based attacks.

### Email Attacks

- Email attacks are executed through malicious messages or attachments, often designed to trick users.
- Example: Exploit code disguised as an attachment can compromise a system when opened.
- Organizations should implement email filtering solutions to detect and block malicious content.
- Regular training on recognizing phishing emails can empower users to avoid falling victim to these attacks.
- Multi-factor authentication (MFA) can provide an additional layer of security against compromised accounts.

### Impersonation and Improper Usage

- Impersonation attacks involve replacing benign elements with malicious ones, such as spoofing or man-in-the-middle attacks.
- Example: SQL injection attacks can manipulate databases by impersonating legitimate queries.
- Organizations should enforce strict access controls and monitoring to detect unauthorized actions.
- Improper usage incidents arise from violations of acceptable use policies by authorized users.
- Example: A user installing file-sharing software may inadvertently expose sensitive data, highlighting the need for clear policies.

# Additional Incident Categories

### Loss or Theft of Devices

- The loss or theft of computing devices poses significant risks to organizational security.
- Example: A stolen laptop containing sensitive data can lead to data breaches and compliance issues.
- Organizations should implement encryption and remote wipe capabilities to protect data on devices.
- Regular audits of device inventory can help track and secure organizational assets.
- Employee training on device security can reduce the likelihood of loss or theft.

### Other Attack Categories

- The 'other' category encompasses attacks that do not fit neatly into established classifications.
- Organizations should maintain flexibility in their incident response plans to address unforeseen incidents.
- Continuous monitoring and threat intelligence can help identify emerging attack vectors.
- Developing a culture of security awareness can empower employees to report suspicious activities.
- Regularly updating incident response playbooks ensures preparedness for new types of incidents.

