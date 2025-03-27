[FIRST](http://www.first.org/) provides several examples.

## Vulnerability

- The flaw in the handler function for remote procedure call (RPC) commands allows manipulation of data pointers within the Virtual Machine Executable (VMX) process.
- This vulnerability may result in a denial of service (DoS) on the host or potentially execute code on the host.
- The vulnerability can be exploited by a user in a Guest Virtual Machine (GVM) to crash the VMX process.

## Attack

- Exploit Requirement: Access to a GVM with at least 4GB of memory and the ability to construct a specially crafted remote RPC call.
- Target Process: The VMX process, which runs in the VMkernel and handles I/O to non-critical devices, user interfaces, snapshot managers, and remote consoles.
- Potential Impact: Crashing the VMX process, leading to a DoS of the host or potentially executing code on the host operating system.

## CVSS v3.0 Base Score: 9.9

| Metric                     | Value   | Comments                                                                                                                                                                                        |
| -------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Attack Vector**          | Network | VMX process is bound to the network stack and the attacker can send RPC commands remotely.                                                                                                      |
| **Attack Complexity**      | Low     | The only required condition for this attack is for virtual machines to have 4GB of memory. VMs with less than 4GB are not affected.                                                             |
| **Privileges Required**    | Low     | The attacker must have access to the guest VM, which is easy in a tenant environment.                                                                                                           |
| **User Interaction**       | None    | The attacker requires no user interaction to successfully exploit the vulnerability. RPC commands can be sent anytime.                                                                          |
| **Scope**                  | Changed | The vulnerable component is the VMX process, which can only be accessed from the guest VM. The impacted component is the host OS, which has separate authorization authority from the guest VM. |
| **Confidentiality Impact** | High    | Full compromise of host operating system via remote code execution.                                                                                                                             |
| **Integrity Impact**       | High    | Full compromise of host operating system via remote code execution.                                                                                                                             |
| **Availability Impact**    | High    | Full compromise of host operating system via remote code execution.                                                                                                                             |
