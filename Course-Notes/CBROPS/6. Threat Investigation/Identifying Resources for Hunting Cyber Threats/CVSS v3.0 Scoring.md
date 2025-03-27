### Base scoring
- Base scoring is computed by the vendor or originator with the intention of being published.
- Once it is set, it is not expected to change.
- Scores are computed from the big three: confidentiality, integrity, and availability.
- Temporal and environmental metrics modify scoring.
- The base score has the largest bearing on the final score and represents vulnerability severity.

### Temporal scoring
- Temporal scoring is computed by vendors and coordinators for publication.
- It modifies the base score of a vulnerability.
- Temporal scoring introduces mitigating factors that reduce the score of a vulnerability.
- These factors are re-evaluated at specific intervals as a vulnerability ages.
- The temporal score represents the urgency of a vulnerability at specific points in time.

### Environmental scoring
- Environmental scoring is an optional computation by end-user organizations.
- It adjusts the combined base-temporal score.
- The adjusted score represents a snapshot in time.
- It is tailored to a specific environment.
- User organizations should use environmental scoring to prioritize responses within their own environments.

## Cyber hunt operators

- CVSS Score Interpretation: High CVSS scores indicate high vulnerability severity, requiring immediate remediation.
- Vulnerability Prioritization: CVSS helps prioritize remediation efforts based on vulnerability severity.
- Hunt Operator’s Role: Cyber hunt operators identify vulnerabilities and assess their CVSS scores to determine remediation priority.
