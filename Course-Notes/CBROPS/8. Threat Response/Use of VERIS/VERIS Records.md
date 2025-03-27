# [[Quick Reference]]

Key Variables in VERIS Records

|Variable|Description|
|---|---|
|timeline.incident.year|The year when the incident was discovered.|
|timeline.incident.month|The month when the incident was discovered.|
|timeline.incident.day|The day when the incident was discovered.|
|incident_id|A unique identifier for the incident.|
|security_incident|Status of the incident (e.g., confirmed).|
|discovery_method|How the incident was discovered (e.g., law enforcement).|
|summary|A brief description of the incident.|

Key Challenges

- **Complexity of VERIS Records**: The framework can be intimidating due to its extensive nomenclature, but it can be simplified based on needs.
- **Data Population**: Security analysts may struggle to gather the necessary data to fill out the VERIS records accurately.

Key Examples

- **Internal Threat Actor Incident**: An example of a VERIS record documenting an incident caused by an internal actor misusing privileges for identity theft, including details like the year, month, and summary of the incident.

Key Applications

- **Security Operations Centers (SOCs)**: Typically implement a reduced set of VERIS terms focused on cybersecurity, omitting fields related to physical security threats.

Facts to Memorize

- VERIS stands for Vocabulary for Event Recording and Incident Sharing.
- The five sections of a VERIS record are: incident tracking, victim demographics, incident description, discovery and response, and impact assessment.
- Key variables in a VERIS record include: timeline.incident.year, timeline.incident.month, timeline.incident.day, and incident_id.

Reference Information

- SOC: Security Operations Center, typically implements a reduced set of VERIS terms focused on cybersecurity.
- The schema_version for the example provided is 1.3.

Concept Comparisons

|Concept|Description|Key Differences|
|---|---|---|
|Internal Threat Actor|An individual within the organization who poses a security risk.|Internal actors have access to systems and data, unlike external threats.|
|Privilege Misuse|Unauthorized use of access rights by an internal actor.|Involves misuse of granted permissions, often for personal gain.|
|Incident Discovery|The method by which an incident is identified or reported.|Can vary from law enforcement involvement to internal monitoring systems.|

Cause and Effect

| Cause                                       | Effect                                                                              |
| ------------------------------------------- | ----------------------------------------------------------------------------------- |
| Employee misuse for identity theft purposes | Financial loss of $14,121 and legal/regulatory costs of $8,000 due to the incident. |

# Overview of the VERIS Database

### Introduction to VERIS

- The VERIS (Vocabulary for Event Recording and Incident Sharing) database is a structured framework for documenting cybersecurity incidents.
- It standardizes the recording of incidents across five key sections: incident tracking, victim demographics, incident description, discovery and response, and impact assessment.
- The framework is designed to be flexible, allowing users to adapt it to their specific needs, whether simple or complex.

### Structure of VERIS Records

- VERIS records consist of various fields (variables) that capture essential details about incidents.
- Only a few fields are mandatory, and many are conditional based on the attributes present in the incident.
- Example of required timeline variables includes year, month, day, and time, which document when the incident was discovered.

# Key Variables in VERIS Records

### Mandatory Variables

- The mandatory fields in a VERIS record include timeline variables such as year, month, day, and time, which are crucial for incident tracking.
- Example: For an incident discovered on November 1, 2019, the variables would be:
	- `timeline.incident.year`: 2019
    - `timeline.incident.month`: 11
    - `timeline.incident.day`: 01

### Optional Variables and Their Usage

- Many fields in VERIS records are optional and can be included based on the incident's context.
- Security Operations Centers (SOCs) often implement a reduced set of VERIS terms, focusing on cybersecurity-related terms and omitting others.
- This selective approach helps streamline the documentation process and focuses on relevant threats.

# Example of a VERIS Record
|Variable|Value|
|---|---|
|timeline.incident.year|2019|
|timeline.incident.month|08|
|schema_version|1.3|
|incident_id|2019-Doberman|
|security_incident|Confirmed|
|discovery_method|Ext - law enforcement|
|discovery_notes|Found out from local police|
|timeline.discovery.unit|Months|
|summary|Employee misuse for identity theft purposes|
|actor.internal|True|
|actor.internal.motive|Financial|
|actor.internal.variety|Finance|
|action.misuse|True|
|action.misuse.variety|Privilege abuse|
|action.misuse.vector|LAN access|
|attribute.confidentiality|True|
|asset.server|True|
|plus.lead_investigator|Gordon|
|plus.case_status|Complete|
|impact.loss.1.variety|Response and recovery|
|impact.loss.1.amount|14121|
|impact.loss.2.variety|Legal and regulatory|
|impact.loss.2.amount|8000|
### Incident Documentation Example

- An example incident involving an internal threat actor due to privilege misuse is documented as follows:
	- `timeline.incident.year`: 2019
    - `timeline.incident.month`: 08
    - `schema_version`: 1.3
    - `incident_id`: 2019-Doberman
    - `security_incident`: Confirmed
    - `discovery_method`: Ext - law enforcement
    - `discovery_notes`: Found out from local police
    - `summary`: Employee misuse for identity theft purposes

### Detailed Variable Breakdown

- The following table summarizes key variables used in the incident example:

| Variable               | Value                 | Description                                 |
| ---------------------- | --------------------- | ------------------------------------------- |
| timeline.incident.year | 2019                  | Year of the incident discovery              |
| actor.internal         | True                  | Indicates if the actor is internal          |
| action.misuse          | True                  | Indicates if there was misuse of privileges |
| impact.loss.1.variety  | Response and recovery | Type of impact loss incurred                |
| impact.loss.1.amount   | 14121                 | Amount lost due to response and recovery    |

# Challenges in Using VERIS

### Data Population Concerns

- A significant challenge for SOCs is ensuring that security analysts can accurately populate the various fields in VERIS records.
- Analysts must have access to relevant data and context to fill out the records effectively, which can be a barrier to comprehensive documentation.
- Training and resources may be necessary to help analysts understand how to gather and input the required information.

### Simplification of VERIS Terms

- SOCs often simplify the VERIS framework by limiting the terms used to those that are directly related to cybersecurity.
- This simplification helps in focusing on the most relevant aspects of incidents while avoiding unnecessary complexity.
- However, it may also lead to a loss of valuable context regarding other types of threats.

