- Different sources of security event data record different details about the event.
- Session logs often document the IP 5-tuple along with packet and byte counts.
- Transaction logs may document user identification, client request, server response, and file hash data.
- Different security event data sources may use different labels.
- For example, Src_IP and SIP may be used for the same purpose.
- Different security event data sources may format data differently.
- For example, 2016-12-15, Dec-15-2016, and 1481778000 all represent the same data value in three different formats.
- The SOC must use many different sources of security event data because no single data source provides the full picture.
- The varying details, labels, and formats are a challenge and data normalization is the solution.

- Normalization is the process of ==manipulating security event data and fitting it into a common schema.==
- Security event monitoring systems must provide parsers that are designed to work with each of the different data sources.
- The parsers algorithmically take the event data and extract the relevant characteristics and fill in the appropriate fields in the common schema.
- Enterprise log search and archive (ELSA) is an example of an event manager.
- ELSA parses a connection log entry that is received from a firewall.
- The top of the entry shows the original syslog message in bold.
- The bottom of the entry shows the data that was extracted from the message and the common schema fields with which the data has been associated.
- Relevant data has been normalized from the original connection log message.
- For example, the IP 5-tuple information has been placed in the proto, srcip, srcport, dstip, and dstport fields.

![3](/Course-Notes/.assets/Pasted_image_20241130133147.png)

- ELSA has parsed an HTTP transaction event produced by Bro.
- The log entry format is different from the firewall connection log message.
- The relevant data is successfully parsed out of the log entry.
- The IP 5-tuple information is parsed into the same fields as the firewall syslog message.

![2](/Course-Notes/.assets/Pasted_image_20241130133204.png)

Fields that are associated with HTTP transactions:
- Method
- Site
- URL
- Referrer    
- User_agent

- The Snort alert is in a different format than the earlier examples.
- The data has been extracted and placed into the common schema.
- The IP 5-tuple uses the proto, srcip, srcport, dstip, and dstport fields.

![1](/Course-Notes/.assets/Pasted_image_20241130133232.png)

Fields that are uniquely associated with IPS alert messages:
- sig_sid
- sig_msg
- sig_classification

