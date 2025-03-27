Sandboxing technology has the ability to emulate an environment, detonate a file without risk of infection, and analyze the file behavior.

Sandboxes detonate unknown files in a safe environment and then record its actions. You can use the reports to identify whether a corresponding file appears to be malicious

Packers change only the outer appearance of a threat, its underlying behavior generally stays the same.

Sandboxes help address many of the weaknesses of signature-based detection, so you can see exactly what a file does before it is labeled malicious or benign.

Sandboxing has three deficiencies:

- **Inherent efficacy:** Running a file in a sandbox is no guarantee that the disposition will show the threat that it poses to your environment.
    
- **Evasion tactics:** Malware authors deploy several techniques to bypass sandbox analysis.
    
- **Means to an end, not an end itself:** Sandboxing is a great tool for addressing malware in an environment, but sandboxing needs to be coupled with other capabilities to provide comprehensive malware protection.

### Cisco ThreatGrid solution
Delivered either as a cloud-based or on-premises appliance-based solution.

Below is a sample of Cisco ThreatGrid sandboxing analysis results, showing malware behaviors and generated outbound HTTP traffic. In this example, the HTTP outbound traffic is the malware’s command and control traffic, including the exact URI path.

![1](/Course-Notes/.assets/Screenshot_2024-11-11_at_19.04.57.png)

# File Integrity Checking

To ensure that a network device, such as the Cisco ASA, image has not been tampered with, the image needs to be verified by the network administrator. The Cisco ASA image is digitally signed to provide authenticity of the software image running on the Cisco ASA. The Cisco public key that is used to decrypt the image digital signature is bundled with the Cisco ASA image. The figure below shows using the `verify` <`image-name`> Cisco ASA command to validate the Cisco ASA image. In this case, the Cisco ASA image is valid since the computed image digital signature hash matched the embedded image digital signature hash.

```
ciscoasa(config)# verify lfbff.SSA

Verifying file integrity of disk0:/lfbff.SSA

Computed Hash SHA2: 7d4e8531f4552458b90f8619ca76a76b
2c8751668b060981f95ded6fcca92d21
e7fc950834209ab162e2b4daaa8b38e4
28eaa48e1895919b817b79e4ead0dfd6
 
Embedded Hash SHA2: 7d4e8531f4552458b90f8619ca76a76b
2c8751668b060981f95ded6fcca92d21
e7fc950834209ab162e2b4daaa8b38e4
28eaa48e1895919b817b79e4ead0dfd6
 
 
Digital signature successfully validate
```

When an attacker modifies a system image that has been digitally signed, what does the attacker need to also change the digital signature of the image?
	The private key that was used to sign the original image