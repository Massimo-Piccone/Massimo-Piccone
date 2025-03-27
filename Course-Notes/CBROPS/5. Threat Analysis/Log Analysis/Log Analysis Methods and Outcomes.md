Key Methods of Log Analysis

![9](/Course-Notes/.assets/Pasted_image_20241127153705.png)

| Method Type             | Description                                                                                                  | Downsides                                                                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Statistical Methods     | Create normal behavior profiles to detect anomalies by comparing current data against established baselines. | - Requires accurate baseline profiles,<br>- Frequent recalculation due to user habit changes and software updates, and accurate deviation threshold determination.                                 |
| Knowledge-based Methods | Analyze logged events against known attack information to identify potential security incidents.             | - Requires Prior knowledge of attacks, including attack signatures and indicators.<br>- Cannot detect unknown attacks and effectiveness relies on accurate known attack signatures and indicators. |
| Advanced Methods        | Utilize machine learning algorithms to derive detection logic and adapt to new conditions automatically.     | - Requires continuous retraining for new attacks and are resource-intensive.                                                                                                                       |

Key Tools/Platforms

- **SIEM Platforms**: Tools for collecting and analyzing security data, capable of alerting on suspicious behaviors.
- **SOAR Platforms**: Security Orchestration, Automation and Response tools that automate security operations.
- **XDR Systems**: Extended Detection and Response systems that provide integrated security across multiple layers.
- **EDR Systems**: Endpoint Detection and Response systems focused on monitoring and responding to threats on endpoints.

#### Timestamps

Essential for understanding when events occurred and correlating multiple events.
- **Timeline Reconstruction:** Allows SOC analysts to recreate the sequence of events.
- **Anomaly Detection:** Enables comparison of events to identify unusual behavior.

==Time synchronization==: 
- Network Time Protocol (NTP) is used across devices

![8](/Course-Notes/.assets/Pasted_image_20241127155131.png)

==Time Stamping:==
- ISO 8601 format: YYYY-MM-DDTHH:MM:SS 
- Epoch time starts from January 1, 1970, UTC 00:00:00.

![7](/Course-Notes/.assets/Pasted_image_20241127155346.png)

Best practice:
The best practice is to use a format that is universally understandable and free from ambiguities. Two unambiguous formats are ISO 8601 and Epoch.

- Year 2038 Problem: 32-bit Epoch integers overflow after January 19, 2038, requiring 64-bit integers for future use.
- Time Zone Importance: Including the time zone in timestamps is crucial to avoid misinterpretation and ensure visibility of events within specific time periods.

- UTC Usage: UTC is recommended for device time configuration, either across all time zones or with a time offset.
- Time Offset: Time offset allows for easy conversion of timestamps to UTC, as seen in the example of converting a timestamp with a “-03:00” offset to UTC.

![6](/Course-Notes/.assets/Pasted_image_20241127155609.png)

#### Key Processes in Log Analysis

![5](/Course-Notes/.assets/Pasted_image_20241127155730.png)

| Process                    | Description                                                                                        |
| -------------------------- | -------------------------------------------------------------------------------------------------- |
| Log Parsing                | Breaking down log messages into individual data components for easier analysis. (Sentence -> Word) |
| Log Filtering              | Selecting relevant logs for analysis and discarding irrelevant entries to reduce noise.            |
| Log Normalization          | Mapping varying log formats to a common structure for consistency in analysis.                     |
| Log Indexing               | Organizing log entries based on attributes to facilitate quick searches and retrieval.             |
| Log Correlation (Analysis) | Discovering relationships between log entries to identify common events or incidents.              |
## Log Preprocessing
- Log parsing
- Log filtering
- Log normalization
- Log categorization
#### Log **parsing**
- Log Format and Parsing: Structured log formats like syslog and CEF are easier to parse due to their clearly defined data blocks.
- Log Parsing Tools: Tools like Elasticsearch, which is part of the ELK Stack, include log parser functions.
- Elasticsearch Functionality: Elasticsearch is an open-source search and analytics tool for various data types, including structured and unstructured data.
#### Log filtering 
- Log Filtering Purpose: To remove irrelevant logs and reduce “noise” for security analysts.
- Log Filtering Benefits: Improves the quality of log data for security analysis.
- Log Filtering Challenges: Some log sources cannot filter irrelevant log entries at the source.
#### Log Normalization 
- Log Normalization Goal: Represent all logs consistently by using a common schema and data formats.
- Log Normalization Process: Maps varying labels to a predefined, common structure and unifies data value formats.
- Log Normalization Benefit: Allows for consistent representation of logs regardless of their original format.

- Data Block Descriptor Normalization: Normalization process involves mapping vendor-specific data block descriptors to standardized normalized descriptors.
- Normalized Data Block Descriptors: “FileName” and “FilePath” are examples of normalized data block descriptors.
- Vendor-Specific Data Block Descriptors: “file” data block descriptor can refer to either file name or file path depending on the vendor.

![4](/Course-Notes/.assets/Pasted_image_20241127160228.png)

- Figure Content: Connection log entries from two firewalls.
- Upper Part of the Figure: Original syslog messages.
- Lower Part of the Figure: Normalized syslog messages with a common structure.

#### Log **Categorization**
- Log Categorization: Assigning logs to categories based on common characteristics, such as source device type or security feature, to facilitate searching and filtering.
- Log Preprocessing: Logging agents preprocess logs before sending them to the log collector.
- Compatibility Requirement: Logging agents and log management platforms must be compatible.

## Log Indexing

- Log indexing
- Log correlation
- Log enrichment

Logically arranging log entries based on their attributes, often chronologically, but also by parameters like event IDs, event names, event severity levels, and usernames.
To make log entries easy to view and process during threat investigations.
Similar to book indexing, where books are ordered by author, subject, or genre.

![3](/Course-Notes/.assets/Pasted_image_20241127173105.png)

- Enables faster and more effective searching and quicker retrieval of specific log entries.
- Consider a scenario where a specific log entry needs to be found within a large volume of unindexed logs.

| Severity Level   | Log Message                                                              | Timestamp                |
|------------------|---------------------------------------------------------------------------|--------------------------|
| Warning          | Memory space is low.                                                     | 2022-01-22T05:32:30+0000 |
| Error            | Software installation failed as some components are missing.             | 2022-01-22T05:40:00+0000 |
| Informational    | Update files downloaded successfully.                                     | 2022-01-22T06:28:40+0000 |
| Error            | Memory is full, downloading update files cannot be completed.            | 2022-01-22T06:12:08+0000 |
| Informational    | Missing components downloaded successfully.                              | 2022-01-22T05:55:20+0000 |
| Warning          | Software needs to restart after installing the new updates.              | 2022-01-22T06:40:49+0000 |
- Task Objective: Find all logs with the severity level of Error.
- Search Method: Searching through the unindexed table requires reading each row and determining the severity level.
- Search Time: Depends on the number of log entries.

| Severity Level   | Log Message                                                              | Timestamp                |
|------------------|---------------------------------------------------------------------------|--------------------------|
| Error            | Software installation failed as some components are missing.             | 2022-01-22T05:40:00+0000 |
| Error            | Memory is full, downloading update files cannot be completed.            | 2022-01-22T06:12:08+0000 |
| Informational    | Missing components downloaded successfully.                              | 2022-01-22T05:55:20+0000 |
| Informational    | Update files downloaded successfully.                                     | 2022-01-22T06:28:40+0000 |
| Warning          | Memory space is low.                                                     | 2022-01-22T05:32:30+0000 |
| Warning          | Software needs to restart after installing the new updates.              | 2022-01-22T06:40:49+0000 |

- Reduces query time and saves processing resources by grouping similar log entries.
- Sorting logs based on the Severity Level field Allows for efficient retrieval of specific log types, such as Error entries.

## Log Correlation

- Discovering relationships between log entries to reveal the same security event or incident.
- Common Data for Correlation: IP address, port, hostname, asset tag, and so on.

- A shared artifact in log entries that represents the same event.
- Correlation Key Example: IP addresses and ports of a Remote Desktop Protocol (RDP) connection.
- Log Correlation Benefits: Provides a broader view of an event by combining information from multiple log sources.

![2](/Course-Notes/.assets/Pasted_image_20241127182029.png)

- Correlation Methods: Manual correlation involves visual examination of logs, while automated correlation utilizes search query strings and log management platforms like SIEMs.
- Query Language: A programming language used to retrieve, manipulate, or modify data from a data set, with specific syntax and commands for each platform.
- Effective Query Formulation: An effective query should narrow down the results to a manageable size and provide the desired output immediately.

SQL syntax requires:
- characteristics of the data (attributes that data must exhibit)
- where to look for the data (which log sources to include)
- what to do with the data (retrieve, sort, delete, insert, update)

- Query Processing: SOC analysts can specify how to process query results, including visualization, statistical computation, and correlation with other query results.
- Detection Rule Implementation: SOC analysts can implement successful queries as detection rules for automation and adjustment.
- Query Example: An example using Splunk to search logs from multiple sources, correlating results with a search string.
```
Index=network | fields host ip message
```

- Query Action: Search for log entries in another data set and correlate the results with the first search.
- Join Command: Joins search results from two searches using “ip” as the correlating field, with the “left” option specifying the type of join.
- Data Sets: The first search uses the “hosts” index, while the second search uses the “endpoints” index.
- Detection Rule Implementation: SOC analysts can implement successful queries as detection rules for automation and adjustment.
- Query Example: An example using Splunk to search logs from multiple sources, correlating results with a search string.
```
Index=network | fields host ip message
```

- Query Action: Search for log entries in another data set and correlate the results with the first search.
- Join Command: Joins search results from two searches using “ip” as the correlating field, with the “left” option specifying the type of join.
- Data Sets: The first search uses the “hosts” index, while the second search uses the “endpoints” index.

```
Index=network | fields host ip message
| join type=left ip [search index=endpoints | fields host ip message]
```

- Aggregation Functionality: Users can add actions to aggregate results, group results, or perform statistical operations.
- Example Query: Lists unique values of “message” and “host” fields grouped by “ip” field.
- Query Output: Provides a list of unique hosts that have logged events containing the specified IP address, along with all unique messages.

```
Index=network | fields host ip message
| join type=left ip [search index=endpoints | fields host ip message]
| stats values(message) values(host) by ip
```

## Log Enrichment

- Log Enrichment Definition: The process of supplementing raw log data with contextual data to provide a broader view of security events.
- Importance of Contextual Information: Essential for SOC analysts to make informed investigation decisions and understand the significance of security events.
- Sources of Contextual Data: Asset inventory systems, geolocation databases, network services servers, and threat intelligence platforms.

![1](/Course-Notes/.assets/Pasted_image_20241128112618.png)

- Data Enrichment Source: DHCP server, asset inventory system, and Cisco Identity Services Engine (ISE).
- Cisco ISE Integration: Provides contextual information like device profile and posture data.
- Contextual Information: Operating system, patch level, and antivirus solution status.

Note
- Device Profiling: Cisco ISE identifies the type of device connected to the network and assigns it to the appropriate VLAN based on its profile.
- Posturing: ISE checks for OS update levels, antivirus, and firewall software status, potentially quarantining devices that are not compliant.
- Purpose of ISE: To ensure network security and compliance by managing device access and configuration.

- External Data Source Lookup Automation: SIEM, XDR, or SOAR platforms can automate external data source lookups for log enrichment.
- Integration Methods: These platforms can integrate with external data sources using APIs.
- External Data Source Types: On-premises systems (e.g., asset inventory) or cloud-based services (e.g., VirusTotal).

Key Considerations

- **Time Synchronization**: Ensuring all devices have synchronized clocks to accurately correlate log events. (NTP)
- **Timestamp Formats**: Using universally understandable formats like ISO 8601 or Epoch to avoid ambiguity in log entries.
- **Contextual Information**: Enriching logs with additional data from external sources to enhance investigation capabilities.

Reference Information

- SIEM platforms are the primary tools for log collection and analysis.
- Common log preprocessing methods: parsing, filtering, normalization, categorization.
- Log correlation keys can include IP address, port, hostname, and timestamps.

Cause and Effect

|Cause|Effect|
|---|---|
|Implementation of log analysis methods|Improved threat detection and incident response capabilities in SOCs.|
|Use of NTP for time synchronization|Accurate timestamps in logs, enabling effective correlation and analysis of events.|
|Integration of threat intelligence|Enhanced responsiveness of SOC platforms to evolving attack techniques.|
|Log enrichment with external data sources|Broader context for security events, leading to more informed investigation decisions.|

Key Terms/Concepts

- **Log Analysis**: The process of reviewing and interpreting log data to detect and investigate security incidents.
- **SIEM (Security Information and Event Management)**: A platform that collects and analyzes security data from across an organization’s IT infrastructure.
- **NTP (Network Time Protocol)**: A protocol used to synchronize the clocks of computers over a network.
- **Log Preprocessing**: The initial phase of log analysis that involves preparing logs for analysis without interpreting the data.
- **Log Enrichment**: The process of supplementing raw log data with contextual information to provide a broader view of security events.

### 1659355200 Epoch time in GMT?

1. **Divide the timestamp by 31.5 million to estimate the number of years** that have passed since 1970.
2. **Subtract the seconds for those years** to find how many seconds remain.
3. **Divide the remainder by the number of seconds in a month** (or day) to find the exact month or day.
4. **Add the months or days to the starting year (1970)**.

1:
$$1659355200÷31,557,600≈52.5$$
2:
$$52×31,557,600=1,641,003,200seconds$$
$$1659355200−1,641,003,200=18,952,000seconds$$
3:
$$$18,952,000÷86400=219.35185185$$
4:
	219.35185185 Days 52 Years from 1970-01-01

