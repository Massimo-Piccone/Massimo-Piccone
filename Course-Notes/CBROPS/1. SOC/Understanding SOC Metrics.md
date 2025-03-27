# Security Data Aggregation

SEIM — Real time reporting - Analysis of security events.
Collects, sorts, processes, prioritizes, stores, and reports to the security analyst.

#### Real-time Reports 
Reduce the time that is needed to detect, and to contain the threats. 
1. For example, if an employee laptop becomes infected by malware. 
2. Each system under attack may be running some host-based security controls, which can report the malicious activity to the SIEM. 
3. The SIEM can correlate those individual events into a single alert that identifies the original infected system and its attempted targets. 
4. The infected systems then can be isolated from the network until the malware is removed.

#### Historical reports
Reports that summarize the security status over time (ordered by months, not days). Enables the security analysts to establish a baseline of their SOC operations. 

The SIEM and its back-end storage must be properly sized and perform at a reasonable level. 
1. Total size of log data coming from the different systems,
2. and the time range of the search query.

#### Deployment
Deployment planning steps. 
Scope, business requirements, and engineering specifications, etc.

![5](/Course-Notes/.assets/Screenshot_2024-11-09_at_13.13.26.png)

#### Functions
- Log ==collection== of event records from sources throughout the organization
- Log ==normalization== to map log messages from different systems to a common data model
- Events and logs correlation to ==speed== the detection of and reaction to security threats
- ==Consolidating== duplicate event records to reduce the volume of event data to be analyzed
- ==Reporting== tools to address regulation compliance reporting requirements

>The SIEM is intended to be the glue for various security tools. 

The following figure shows the Splunk SIEM. The Splunk security posture dashboard gives a complete summary of what is happening in the enterprise. The SIEM creates a "single pane of glass" for the security analysts to monitor the enterprise.

![4](/Course-Notes/.assets/Screenshot_2024-11-09_at_13.13.41.png)

# Time to Detection (TTD)

Current industry estimate for time to detection (TTD) is 100 to 200 days, 
Defenders must adopt strategies and implement solutions that provide end-to-end network activities visibility and reduce the TTD. For example, the Cisco CSIRT, using a combination of people, processes (such as the incident response process), and technologies (such as ==Cisco== Advanced Malware Protection [AMP]), ==reduced the TTD from days to hours.==

![3](/Course-Notes/.assets/Screenshot_2024-11-09_at_13.22.38.png)

An ==average of 98 days for financial== services companies and ==197 days for retail.== 

# SOC Metrics

An effective threat-centric SOC consists of deep expertise with cutting-edge technology, leading security intelligence data, and advanced analytics to detect and investigate threats with great speed, accuracy, and focus.

- **Speed:** Faster detection and targeted mitigation reduce the mean time to respond.
- **Focus:** Higher fidelity reduces false positives and ensures proper containment and actionable recommendations for remediation.
- **Accuracy:** Continuous monitoring and investigation plus full packet capture illuminate security blind spots.

Reasons to use metrics to define and measure SOC effectiveness include the following:
- To understand and identify the cybersecurity risk to the business
- To measure the SOC effectiveness
- To optimize resource and investment allocation

![2](/Course-Notes/.assets/Screenshot_2024-11-09_at_13.29.22.png)

The mean time to detect should begin to trend downward, as shown in the figure. A continued decrease in the TTD is a direct correlation of a successful and mature SOC. 

Typical SOC metrics that demonstrate the SOC's value to the business may include:

- The mean Time to detect (TTD) of the incident after its occurrence 
- The mean time to contain (MTTC) the incident after its detection
- The mean time to mitigate (MTTM) the incident after its containment
- The number of incidents being detected, contained, and mitigated
- % of the discovered incidents found using the plays in the SOC playbook
- The number of new plays added to the SOC playbook
- The number of zero-day attack detections
- The false positive or true positive detection rate
- The operational cost of running the SOC

In conclusion, metrics are imperative to the success of any SOC organization. Metrics allow leadership to make decisions that are based on data and facts, and allow for the removal of emotion and anecdotes from critical decision-making processes.

By implementing a SOC that is built around the metrics, the leadership will be able to show the maturation of the organization and processes, pinpoint areas of focus for process improvement, identify gaps in prevention, and detection and operational capabilities. 

![1](/Course-Notes/.assets/Screenshot_2024-11-09_at_13.30.00.png)

# [[Quick Reference]]

Key Functions of SIEM

|Function|Description|
|---|---|
|Log Collection|Gathers event records from various sources within the organization.|
|Log Normalization|Maps log messages from different systems to a common data model for easier analysis.|
|Event Correlation|Combines multiple log entries to identify potential security threats more quickly.|
|Reporting Tools|Provides compliance reporting and summaries of security status over time.|

Key Metrics

- **Mean Time to Detect (MTTD)**: Average time taken to identify a security incident after it occurs.
- **Mean Time to Contain (MTTC)**: Average time taken to contain a security incident after detection.
- **Mean Time to Mitigate (MTTM)**: Average time taken to fully resolve a security incident after containment.

Seminal Studies

- **Cisco Annual Security Report**: Highlights the industry estimate for TTD and emphasizes the need for improved detection strategies.
- **Ponemon Institute Report**: Provides statistics on the average TTD for different sectors, revealing significant delays in detection.

Key Challenges

- **High TTD**: The lengthy time to detect breaches allows attackers to exploit vulnerabilities and steal sensitive data.
- **Resource Drain from False Positives**: Excessive false positives can overwhelm security teams and divert resources from genuine threats.

Facts to Memorize

- Time to Detection (TTD) is estimated at 100 to 200 days.
- Average detection time for financial services is 98 days; for retail, it is 197 days.
- Effective security controls should minimize false negatives and false positives.

Reference Information

- SIEM: Security Information and Event Management.
- SOC: Security Operations Center.
- APT: Advanced Persistent Threat.

Problem-Solving Steps

To effectively reduce Time to Detection (TTD):

1. **Implement Comprehensive Monitoring**: Ensure all endpoints and network activities are monitored.
2. **Utilize Advanced Analytics**: Leverage machine learning and AI to identify patterns indicative of threats.
3. **Establish Incident Response Protocols**: Develop clear processes for detection, containment, and mitigation.
4. **Regularly Review and Update Security Controls**: Ensure that security measures are current and effective against evolving threats.
5. **Train Security Personnel**: Continuous education for SOC analysts on the latest threats and detection techniques.

Key Terms/Concepts

- **SIEM (Security Information and Event Management)**: A system that collects, analyzes, and reports on security data from across an organization to help detect and respond to security threats.
- **Time to Detection (TTD)**: The duration it takes to identify a security breach after it has occurred, which is critical for minimizing damage.
- **False Positive/Negative**: Terms used to describe the accuracy of security controls; false positives indicate benign activity flagged as malicious, while false negatives indicate actual threats that went undetected.

# Overview of Security Information and Event Management (SIEM)

### Definition and Purpose of SIEM

- A Security Information and Event Management (SIEM) system is crucial for enterprises to provide real-time reporting and analysis of security events.
- SIEM collects, sorts, processes, prioritizes, stores, and reports alarms to security analysts, aiming to reduce detection and containment time for threats.
- Example: If a laptop is infected with malware, the SIEM can correlate events from various systems to identify the source and isolate it from the network.

### Key Functions of SIEM

- ****Log Collection****: Gathers event records from various organizational sources, ensuring comprehensive data coverage.
- ****Log Normalization****: Maps log messages from different systems to a common data model for consistency in analysis.
- ****Event Correlation****: Speeds up detection and response to security threats by linking related events together.
- ****Consolidation of Duplicate Events****: Reduces the volume of data to be analyzed, enhancing efficiency in threat detection.
- ****Reporting Tools****: Facilitates compliance with regulatory requirements through detailed reporting capabilities.

### Deployment Considerations

- Deploying a SIEM requires careful planning, including understanding scope, business requirements, and engineering specifications.
- Proper sizing and performance of the SIEM and its back-end storage are critical for effective operation.
- A successful SIEM project involves more than just hardware installation; it requires strategic planning and execution.