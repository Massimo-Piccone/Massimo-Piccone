
![1](/Course-Notes/.assets/Pasted_image_20241202101905.png)

## Report Identification
Example: 100003-HF-IDS-MALWARE:BOT-C2

**Report Unique ID = 100003:**
- ==Identification==: Reports are identified by a unique ID and a set of indicators.
- ==Structure==: The leading digit of the unique ID indicates the data source.
- ==Data Source Codes==: 
	- 100,000-199,999 = IPS or IDS
	- 200,000-299,999 = NetFlow
	- 300,000-399,999 = Web Proxy

**Report Type = HF:**
- ==Report Types==: 
	- HF reports indicating certain malicious activity 
	- INV reports requiring further investigation.
- ==High Fidelity (HF)==: Automatically processable, triggered by malicious activity, and require remediation.
- ==Investigative (INV)==: May indicate host infection, policy violation, or normal activity, require further investigation, and may lead to high fidelity reports.

**Event Source = IDS:**
The event source identifies which source, or sources, that the report queries.

**Report Category = MALWARE:**
- ==Incident Categories==: VERIS and US-CERT provide standard categories for classifying incidents.
- ==Malware Incident==: MALWARE category represents malicious activity or indicators on a system or network.

**Description: BOT-C2:**
The free-text description component may provide a brief summary of what the report attempts to detect.


## Objective

- Describes the “what” and “why” of a play.
- Background info and a reason for why the play exists.
- Describe what a play is looking for on the network.
- It also explains why the play is worthwhile to run.
	- For example, the objective statement may describe the goal of discovering and reporting botnet-infected hosts for remediation.
- It may also aim to enhance future detection.

## Data Query
"Working” in the example

- Is not designed to be standalone information.
- Implements the objective and produces the report results.
- All necessary details of the data query should be documented in the analysis section.
- Data queries can sometimes be rather complex—due, in part, to being specific to whichever system in which the data resides.

- Data query is a machine-readable query.
- The query returns the result that is based on the play objective from the query system.
- A query system may consist of an 
	- Open Source logging solution, 
	- a relational database, 
	- a SIEM, 
	- a large-scale data warehouse, 
	- or a commercial application.

Splunk SIEM query:

```
index=”ids” earliest=-10m tag=HF-IDS NOT (tag=IN_DNS OR tag=DC_MBOX | stats count by host | sort -count limit=50 | rename attacker AS C2 | `csirtTable` | `makeAcaseHF` | `botSquash(C2)`
```

> Splunk partitions its event database into indexes.
1. The query is for the “ids” index.
2. Event data with certain tags that occurred within a certain time range.
3. The other query strings are used for report statistics and sorting.
4. “Rename” formats the output to make it more human readable.

## Action
- Documents the actions to take during the incident response phase.
- For example, a case that is generated into auto-remediation queue: CSIRT-Analysts-HF.
- The output of the query is a case that will go into a queue where someone will accept it.
- The person who accepts the case will then begin the reimage process.

## Analysis

- The analysis section provides documentation and training material on how the data query works.
	- ==Why== it is written the way it is and 
	- ==How== to interpret and act on the results.
	- Discusses the ==fidelity== of the query, 
	- expected ==true positive== results, and
	- likely sources of ==false positives==
	- and how to ==prioritize== the analysis.

- ==Can vary== significantly from play to play because it is specific to the data source.
- ==The main goal== is to help act on the data.

- Must be as prescriptive and insightful as possible.
	- It should describe what to do, 
	- for all the related parties involved in escalation,
	- and any other special-handling procedure.
- ==High-fidelity== play results are ==guaranteed== hits.
- Allows focus on action rather than the analysis.
- Most reports are ==investigative== 
- Therefore ==require significant analysis== to be accurate.

- The generated report is high fidelity.
- If an IRC JOIN is detected, verify if the “NICK” (nickname) is computer-generated.
-  HF require the reimage malware remediation process.
	1. If the bot matches the Infostealer list, email the clients with the password update instructions.
	2. If the client address matches the VIP list, those hosts must be escalated to the on-duty investigator

## Reference

- Managed using a tracking system such as Bugzilla.
- Bug and ticket tracking systems allow the SOC to track changes and document the motivation for those changes.
	- Additional useful details end up in this analysis and reference notes section.
- Comments allow for discussion among security analysts about various query options and the best way to approach the play objective.
	- CPlace for clarification, issues regarding the query, or potential trouble spots.
	- Discuss tweaks and describe what is and is not working about a report.
	- Multiple ways to solve the idea in the form of a data query.
	- Read play evolution, making the playbook more relevant in the long term.
	- Retiring reports and reopening reports.
- For example, ==wiki/10012, bugzilla:576, and GIR:n/a== provides more information about the play from the wiki and Bugzilla tracking systems.