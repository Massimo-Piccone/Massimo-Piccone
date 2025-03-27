# [[Quick Reference]]

Key Techniques

|Technique|Description|
|---|---|
|Aggregation|Pulling records that share a common variable to gather more information, e.g., querying by IP address.|
|Summarization|Producing compact descriptions of data qualities, often using groupby directives in queries.|
|Deduplication|Normalizing data elements and consolidating overlapping records to present unique data in a report.|

Key Tools/Systems

- **ELSA**: A system used for querying and analyzing security data, allowing for aggregation and summarization of data.
- **Cisco Stealthwatch**: A sophisticated NetFlow analysis system that provides deduplication and correlation of flow records.

Key Data Formats

- **NetFlow Version 5**: Focuses on the IP 5-tuple and basic packet/byte counts, but does not support IPv6.
- **NetFlow Version 9**: A more robust version that is extensible and supports new data types, replacing version 5.
- **IPFIX**: An open protocol that is also extensible and used for flow data tracking.

Key Applications

- **Security Operations Center (SOC)**: Utilizes data mining techniques to focus investigations on relevant data, improving efficiency in threat detection and response.

Facts to Memorize

- NetFlow version 5 does not support IPv6.
- NetFlow version 9 and IPFIX are more robust and extensible than version 5.
- The IP 5-tuple consists of source IP, source port, destination IP, destination port, and protocol.

Reference Information

- ELSA (Enterprise Log Search and Archive) is a tool used for querying and analyzing security data.
- Deduplication is essential for producing concise reports from overlapping data.
- Cisco Stealthwatch is an example of a sophisticated NetFlow analysis system.

Concept Comparisons

|Concept|Description|Key Differences|
|---|---|---|
|Aggregation|Gathering data to gain insights about specific variables.|Focuses on collecting data without summarizing it.|
|Summarization|Producing compact descriptions of key data set qualities.|Provides a summarized view, often in graphical or tabular format.|
|Deduplication|Presenting relevant details from overlapping data in a concise format.|Involves normalizing data and removing redundancy to create a clear report.|

Problem-Solving Steps

To effectively analyze security data using aggregation, summarization, and deduplication, follow these steps:

1. **Identify the Data Source**: Determine where the security data is coming from (e.g., ELSA).
2. **Perform Aggregation**: Use queries to gather data based on common variables (e.g., IP address).
3. **Summarize the Data**: Use summarization techniques (e.g., groupby directive) to create a clear overview of the data.
4. **Deduplicate the Data**: Normalize the data and remove redundant entries to create a concise report.
5. **Analyze the Results**: Review the summarized and deduplicated data to identify patterns or anomalies.

# Overview of Security Data Manipulation

### Introduction to Security Data Mining

- Security data mining involves techniques that help analysts focus on relevant data for investigations.
- Key techniques include aggregation, summarization, and deduplication, which streamline the analysis process.
- These methods are essential for Security Operations Center (SOC) analysts to manage large volumes of security data effectively.

### Importance of Data Manipulation Techniques

- Effective data manipulation enhances the ability to detect and respond to security incidents.
- By filtering out noise, analysts can concentrate on actionable intelligence.
- Historical context: As cyber threats have evolved, so have the techniques for analyzing security data.

## Aggregation

- Aggregation Definition: A data mining technique that gathers data to gain insights about specific variables.
- Aggregation Method: Involves collecting records with a shared variable, such as an IP address.
- ELSA Query Example: Querying ELSA with an IP address returns records sharing that IP.

```
10.10.4.20
```

![5](/Course-Notes/.assets/Pasted_image_20241130134123.png)

## Summarization

- Data Summarization: A data mining technique that generates concise descriptions of key data set qualities, often presented graphically or tabularly.
- Summarization Application: Useful for analyzing aggregated data, particularly when grouping by specific attributes.
- ELSA Query Implementation: Utilizes the groupby directive to summarize data based on designated attributes, as demonstrated in the example with source and destination IP addresses.

```
dstip=10.10.4.20 groupby:srcip
```

![4](/Course-Notes/.assets/Pasted_image_20241130134132.png)

## Deduplication

- Deduplication Goal: Present relevant details from overlapping data in a concise format.
- Data Preparation: Data elements must be normalized before deduplication.
- Data Extraction: Relevant data fields are added to a consolidated report while redundant and irrelevant data are excluded.

![3](/Course-Notes/.assets/Pasted_image_20241130134139.png)

A deduplicated report of these four records might look similar to the following:

```
time= Fri Dec 16, 20:12:24, duration=0.042049
proto=TCP, srcip=172.16.1.10, srcport=36205, dstip=10.10.4.20, dstport=25
pkts_in=44, bytes_in=200, pkts_out=85, bytes_out=102452
service=smtp, from=karla <karla@services.public> to=wendy@abc.public, subject=Check it out!
path=10.10.4.20,172.16.1.10,209.165.200.233,209.165.200.235
```
![2](/Course-Notes/.assets/Pasted_image_20241130134152.png)
![1](/Course-Notes/.assets/Pasted_image_20241130134158.png)

| **Field**           | **Value**                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Start Time**      | 09:04:48.323                                                                                                                         |
| **Client Identity** | 10.10.10.10 1000:5a6c:abcd susan                                                                                                     |
| **Client Port**     | 21322                                                                                                                                |
| **Server IP**       | 192.0.2.77                                                                                                                           |
| **Server Port**     | 80                                                                                                                                   |
| **Protocol**        | TCP                                                                                                                                  |
| **Client Bytes**    | 1025                                                                                                                                 |
| **Client Pkts**     | 5                                                                                                                                    |
| **Server Bytes**    | 28712                                                                                                                                |
| **Server Pkts**     | 17                                                                                                                                   |
| **App**             | HTTP                                                                                                                                 |
| **Exporter**        | l2-sw, g1/2, in; l2-sw, g1/24, out; l3-sw, g1/6, in; l3-sw, g4/12, out; rtr, g1/1, in; rtr, g1/4, out; asa, g1/1, in; asa, g1/0, out |
