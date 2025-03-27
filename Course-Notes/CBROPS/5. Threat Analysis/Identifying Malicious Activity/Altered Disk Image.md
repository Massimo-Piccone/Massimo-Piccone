- Malicious Software Introduction: Malicious software can be introduced by altering the software image stored on the victim’s device file system.

- Attack Scenario: An attacker can modify a valid device’s software image by adding malicious code and loading it onto the victim’s device.

- Protection Measures: Safe coding practices, digital signing, and secure boot can protect against memory and code manipulation.

## Software Image Verification

- Image Verification Method: Offline process to compare the calculated hash of the software image file with the trusted hash from the manufacturer.
- Cisco ASA Feature: Hash File Validation feature allows administrators to verify the hash of Cisco ASA software images.
	- Verifies the integrity of image files stored on the Cisco ASA file system.
	- `Verify` command followed by the hashing algorithm (e.g., `/md5`, `/sha-512`).

Syntax:
```
verify [/md5|/sha-512] _filesystem:filename_ [md5-hash|sha-512-hash]
```

Verify File:

```
ciscoasa# verify /sha-512 asa915-smp-k8.bin

<output omitted>

Done!

verify /SHA-512 (disk0:/asa915-smp-k8.bin) = 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e72142872
```

Verify Hash:

```
ciscoasa# verify /sha-512 asa915-smp-k8.bin 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19

<output omitted>

Done!

Verified (disk0:/asa915-smp-k8.bin) = 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e72142872
```

Failed Verify Message:

```
ciscoasa# verify /sha-512 asa915-smp-k8.bin 4deb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19

.....<output omitted>.....

Done!

==%Error verifying disk0:/asa915-smp-k8.bin==
Computed signature = 4eb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19

Submitted signature = 4deb359496738af1d14c3586b39de4f10b6ea77ea6281b88506190fea83717622115e51e01d57c5489 d4fe442ad3ab8c93e871b6e7214287208e947380498ae19
```

## Secure Boot

Secure boot ensures devices boot using trusted software.

- Cisco Secure Boot Functionality: Ensures the authenticity and integrity of code running on Cisco hardware platforms.
- Security Mechanism: Implements a secure startup process anchored in hardware, making it difficult to tamper with.
- Boot Process: Verifies the authenticity of software components through a “chain of trust” established by digital signatures.