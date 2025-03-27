- Correlation as a noun can be defined as a mutual relationship or connection between two or more things.
- In network security monitoring, event correlation is recognizing that two or more security events are related and then using the relationship to further the process of analysis.
- A simple, but very powerful example is to use the IP 5-tuple to correlate events.
- Imagine that an IPS alert provides an initial IP 5-tuple of interest.
- Assuming that the data is already normalized, the analyst can query the database with the IP 5-tuple to produce a report of correlated data.
- The figure is the result of this ELSA query: srcip=172.16.1.10 srcport=36205 dstip=10.10.4.20 dstport=25

![1](/Course-Notes/.assets/Pasted_image_20241130133556.png)

From top to bottom, the four matching events in the ELSA database are as follows:
- An SMTP transaction record that is produced by Bro.
- A TCP connection record that is produced by Bro.
- A TCP connection record that is produced by a Cisco Adaptive Security Appliance (Cisco ASA) firewall.
- An alert that is produced by Snort.

- Being associated with the same IP 5-tuple indicates a strong relationship between events.
- These events may not necessarily be the same.
- For example, a single SMTP connection may be used to send multiple email messages.
- A single email message may contain multiple suspicious attachments.
- There isn’t necessarily a one-to-one relationship between connections and transactions and alerts.
- Correlated events provide more detail and context to the analyst than can be obtained from any single event.

- The strong correlation between events is of obvious value to the analyst.
- The analyst must also use weaker correlations.
- The analysis may start with an IPS alert.
- The analyst must determine whether the exploit kit delivered an exploit or not.
- Using IP 5-tuple correlation, the analyst may find the HTTP transaction log.
- The transaction log may reveal an HTTP redirect from the exploit kit landing page to a malware download on a completely different website.
- The data associated with the HTTP transactions between the client and the target of the redirection is now of interest to the analyst.
- There is a correlation between these sets of events.