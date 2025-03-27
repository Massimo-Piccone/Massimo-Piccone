- ==Schema Structure: Five== main sections to capture different aspects of an incident narrative.
- ==Sections== provide a ==comprehensive understanding== of incident cause and severity.
- ==Data Captured: Variables== within each section document different aspects of the incident.


| **Incident Tracking**      | incident_id            | ExampleBreach_00001          |
| -------------------------- | ---------------------- | ---------------------------- |
| **Victim Demographics**    | victim.victim_id       | Example Inc.                 |
| **Incident Description**   | actor.external.country | ISO 3166-2:RU                |
| **Discovery and Response** | corrective_action      | Create a new IPS rule to ... |
| **Impact Assessment**      | impact.overall_rating  | Damaging                     |

| Section                | Description                                                                                                                                                                        | Example Variable                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Incident Tracking      | Captures general information about the incident for unique identification of the incident for storage and tracking over time.                                                      | incident_id                                                         |
| Victim Demographics    | Describes (but does not identify) the organization affected by the incident for comparisons.                                                                                       | victim.victim_id                                                    |
| Incident Description   | "Who did what to what, or whom, with what result" Translates the incident narrative into a form suitable for trending and analysis using the A4 threat model.                      | actor.external.country                                              |
| Discovery and Response | Focuses on the timeline of events, discovery, and response for insight into detection capabilities.                                                                                | corrective_action                                                   |
| Impact Assessment      | The three perspectives are: <br>1) categorize the varieties of losses, <br>2) estimate the magnitude of losses, and <br>3) capture a qualitative assessment of the overall effect. | - impact.loss<br>- impact.overall_amount<br>- impact.overall_rating |
Refer to [VERIS](https://verisframework.org/index.html) for a full list of all the different variables. Specific variables are used to document incidents depending on specific incident details. The latest VERIS schema information is available on GitHub: [https://github.com/vz-risk/veris](https://github.com/vz-risk/veris).