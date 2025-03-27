# [[Quick Reference]]

Key Phases of the Forensic Process

|Phase|Description|
|---|---|
|Collection|Identify, label, record, and acquire data from relevant sources while preserving data integrity.|
|Examination|Process collected data using automated and manual methods to extract relevant information.|
|Analysis|Analyze the results of the examination using legally justifiable methods to derive useful information.|
|Reporting|Document the analysis results, actions taken, and recommendations for future improvements.|

Key People

- **NIST (National Institute of Standards and Technology)**: Provides guidelines for digital forensics, including the SP800-86 guideline.

Key Applications of Digital Forensics

- **Legal Proceedings**: Collecting evidence for court cases.
- **Internal Disciplinary Actions**: Investigating misconduct within organizations.
- **Malware Incident Handling**: Analyzing and responding to malware attacks.
- **Operational Problem Investigation**: Understanding unusual operational issues.

Key Considerations in Evidence Collection

- Evidence must be valid and treated properly to be admissible in court.
- The integrity of the evidence must be preserved throughout the collection and analysis process.
- The context of evidence can change its classification from direct to circumstantial.

Facts to Memorize

- Types of evidence: Direct evidence, Circumstantial evidence, Corroborating evidence, Best evidence.
- Four phases of the forensic process: Collection, Examination, Analysis, Reporting.

Reference Information

- Direct evidence does not require inference, while circumstantial evidence does.
- The best evidence rule prefers original documents over copies, but copies can still be used if originals are unavailable.

Problem-Solving Steps

1. **Collection**: Identify and acquire data from relevant sources while preserving integrity.
    
    - Tip: Act quickly to avoid losing dynamic data.
    - Common Pitfall: Failing to label and record data properly.
2. **Examination**: Process collected data using forensic tools to extract relevant information.
    
    - Tip: Use both automated and manual methods for thoroughness.
    - Common Pitfall: Overlooking important data due to improper filtering.
3. **Analysis**: Analyze the examined data using legally justifiable methods.
    
    - Tip: Keep a clear record of methods used for analysis.
    - Common Pitfall: Drawing conclusions without sufficient evidence.
4. **Reporting**: Document the findings and recommendations based on the analysis.
    
    - Tip: Tailor the report's formality to the audience and purpose.
    - Common Pitfall: Failing to include necessary details in the report.

Key Terms/Concepts

- **Direct Evidence**: Evidence that directly supports a conclusion without needing any inference.
- **Circumstantial Evidence**: Evidence that requires an inference to connect it to a conclusion.
- **Corroborating Evidence**: Evidence that supports an assertion already backed by other evidence, increasing confidence in the conclusion.
- **Best Evidence**: A legal principle that prefers original documents or firsthand testimony over copies or secondhand accounts.

# Understanding Evidence in Network Security and Law Enforcement

### The Role of Evidence in Investigations

- Both network security analysts and police detectives rely on evidence to reconstruct events and determine the nature of incidents.
- Evidence collection and analysis is iterative; initial findings often lead to further inquiries and additional evidence gathering.
- The validity of evidence is crucial; improper handling can render it inadmissible in legal contexts, impacting criminal prosecutions.
- The process of reaching conclusions is based on a confidence level, which is influenced by the quality and quantity of evidence collected.

### Types of Evidence

- ****Direct Evidence****: This type of evidence does not require inference; it directly supports a conclusion. Example: A witness seeing snow fall is direct evidence of snowfall.
- ****Circumstantial Evidence****: This requires inference to connect it to a conclusion. Example: A witness noting a clear road that later is covered in snow requires the inference that snow must have fallen while they were inside.
- The context of the assertion matters; evidence can shift from circumstantial to direct based on what is being asserted.

### Corroborating Evidence

- Corroborating evidence supports an assertion already backed by other evidence, enhancing confidence in the conclusion drawn.
- In network security, an IPS alert serves as direct evidence of a condition being met, but additional evidence is often needed to assert malicious intent.
- Examples of corroborating evidence include PCAP files and sandbox analysis results, which can validate or refute initial findings.

### The Best Evidence Rule

- The best evidence rule prioritizes the most reliable form of evidence available, traditionally favoring eyewitness accounts over hearsay.
- In the digital age, original digital files are often less accessible; thus, printouts or other representations may serve as the best evidence.
- The evolution of evidence presentation in courts reflects the need for clarity and understanding in the digital context.

# Digital Forensics: Definition and Phases

### Definition of Digital Forensics

- Digital forensics applies scientific methods to the identification, collection, examination, and analysis of digital data.
- It aims to preserve the integrity of data while maintaining a strict chain of custody, crucial for legal proceedings.
- The scope of digital forensics includes various devices and data sources, from computers to mobile devices and network equipment.

### The Four Phases of Digital Forensics

> The forensic process is structured into four key phases: Collection, Examination, Analysis, and Reporting.

- ****Collection****: Involves identifying and acquiring data while ensuring its integrity. Timeliness is critical to prevent data loss, especially from volatile sources.
- ****Examination****: This phase processes the collected data using both automated and manual methods to extract relevant information while maintaining data integrity.
- ****Analysis****: Involves interpreting the examined data using legally justifiable methods to answer the investigative questions.
- ****Reporting****: The final phase documents the findings, detailing actions taken, tools used, and recommendations for future improvements.

![1](/Course-Notes/.assets/Pasted_image_20241130132807.png)
### Applications of Digital Forensics

- Digital forensics is essential in various scenarios, including legal investigations, internal audits, and incident response for malware attacks.
- The forensic process can help organizations understand security breaches and improve their defenses against future incidents.
- The methodology ensures that findings are credible and can withstand scrutiny in legal contexts.