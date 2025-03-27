%% #review %%
## [[VERIS Overview]] 

>Vocabulary for Event Recording and Incident Sharing (VERIS)
- ﻿﻿Developed by Verizon
- ﻿﻿Open format available for use by organizations, without licensing fees

==Allows comparison of incidents== with others, revealing new information sources.
## [[VERIS Community Database]]

>﻿﻿VERIS Community Database (VCDB)
- ﻿﻿Open and free repository of publicly reported security incidents

![2](/Course-Notes/.assets/Pasted_image_20241204125504.png)

## [[VERIS Incidents Structure]]

| Section                | Description                                                                                                                                                                        | Example Variable                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Incident Tracking      | Captures general information about the incident for unique identification of the incident for storage and tracking over time.                                                      | incident_id                                                         |
| Victim Demographics    | Describes (but does not identify) the organization affected by the incident for comparisons.                                                                                       | victim.victim_id                                                    |
| Incident Description   | "Who did what to what, or whom, with what result" Translates the incident narrative into a form suitable for trending and analysis using the A4 threat model.                      | actor.external.country                                              |
| Discovery and Response | Focuses on the timeline of events, discovery, and response for insight into detection capabilities.                                                                                | corrective_action                                                   |
| Impact Assessment      | The three perspectives are: <br>1) categorize the varieties of losses, <br>2) estimate the magnitude of losses, and <br>3) capture a qualitative assessment of the overall effect. | - impact.loss<br>- impact.overall_amount<br>- impact.overall_rating |

## [[VERIS 4 A's]] 

![1](/Course-Notes/.assets/Pasted_image_20241204150916.png)

|Concept|Description|Examples|
|---|---|---|
|Actors|Entities causing or contributing to an incident.|External, Internal, Partner|
|Actions|What the threat actor did to cause or contribute to the incident.|Malware, Hacking, Social, Misuse|
|Assets|Information assets compromised during the incident.|Network hardware, Server, User device|
|Attributes|Security attributes of the identified assets that were compromised.|Confidentiality, Integrity, Availability|
Each example can be broken down into 2 sections, ==variety== and ==vector==.

## [[VERIS Records]] 

Example of a VERIS Record:

| Variable                      | Value                                       |
| ----------------------------- | ------------------------------------------- |
| timeline.incident.==year==    | 2019                                        |
| timeline.incident.==month==   | 08                                          |
| schema_==version==            | 1.3                                         |
| incident_==id==               | 2019-Doberman                               |
| security_==incident==         | Confirmed                                   |
| ==discovery==_method          | Ext - law enforcement                       |
| discovery_notes               | Found out from local police                 |
| ==timeline==.discovery.unit   | Months                                      |
| ==summary==                   | Employee misuse for identity theft purposes |
| actor.==internal==            | True                                        |
| actor.internal.==motive==     | Financial                                   |
| actor.internal.==variety==    | Finance                                     |
| action.==misuse==             | True                                        |
| action.misuse.==variety==     | Privilege abuse                             |
| action.misuse.==vector==      | LAN access                                  |
| ==attribute==.confidentiality | True                                        |
| ==asset==.server              | True                                        |
| plus.lead_investigator        | Gordon                                      |
| plus.case_==status==          | Complete                                    |
| ==impact==.loss.1.variety     | Response and recovery                       |
| impact.loss.1.==amount==      | 14121                                       |
| impact.loss.2.==variety==     | Legal and regulatory                        |
| impact.loss.2.==amount==      | 8000                                        |
**Mandatory fields** 
- Year, month, day, and time.
- Crucial for incident tracking.

**Optional fields** 
- Most are optional
- Can be as loose or specific as necessary 

>It is simple and streamlined, but this can be a double edged sword.

### Concept Comparisons

|Concept|Description|Key Differences|
|---|---|---|
|Internal Threat Actor|An individual within the organization who poses a security risk.|Internal actors have access to systems and data, unlike external threats.|
|Privilege Misuse|Unauthorized use of access rights by an internal actor.|Involves misuse of granted permissions, often for personal gain.|
|Incident Discovery|The method by which an incident is identified or reported.|Can vary from law enforcement involvement to internal monitoring systems.|

## [[VERIS Community Database]] (VCDB)

Catalogs security incidents in the public domain using the VERIS framework
Shared under a Creative Commons license, allowing free access and use
VCDB offers a graphic interface for users to visualize incident data

Key Features of the VCDB

|Feature|Description|
|---|---|
|**Open Data**|The data is free for anyone to use and contribute to, encouraging community involvement.|
|**JSON Format**|Incident data is available in JSON format for easy access and integration.|
|**Incident Cataloging**|Contains raw data for thousands of security incidents, allowing for comprehensive analysis.|
|**Public Repository**|Acts as a public repository of breach data, facilitating evidence-based risk management.|
|**Creative Commons License**|Data shared under this license allows for reuse and redistribution.|

## [[Verizon Data Breach Investigations Report and Cisco Annual Security Report]]

Verizon publishes an annual Data Breach Investigations Report (DBIR)
using statistics from thousands of incidents that were classified using VERIS

Verizon researchers analyzed that information to highlight new patterns, steady trends, and interesting tidbits in the evolving cybersecurity threat landscape.

Cisco Does the same with its resources.


