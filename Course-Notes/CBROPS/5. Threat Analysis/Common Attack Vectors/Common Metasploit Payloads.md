Payloads within the Metasploit framework refer to the modules utilized during exploitation events to gain access to, control of, and functionality within the target host environment.

The following are the three basic types of payloads within the Metasploit framework:

- **==Singles==:** Self-contained payloads that function on their own.
- **==Stagers==:** Establish the required communications path between the attack platform and the target host. 
- **==Stages==:** The payload that is delivered to the target host. Stages are used with the stagers, and contain everything outside of the network communications component to perform execution and ultimately exploit the target host.

## Singles

- ==Definition==: Self-contained payloads that can function independently of the Metasploit framework.
- ==Execution==: Can be executed with handlers outside of the Metasploit framework and are well-documented.
- ==Detection and Prevention==: Easy to detect, block, and log, making them less effective for stealthy attacks.

## Stagers

- ==Functionality==: Establishes a network connection between the attacker and victim, facilitating the upload and download of information.
- ==Design==: Simplistic, compact, and reliable.
- ==Purpose==: To set up a communications path for the attack platform to communicate with the target host.

## Stages

- ==Definition==: Payload delivered to the target host, providing increased functionality compared to stagers.
- ==Types==: Precompiled and configured or customized before deployment.
- ==Functionality==: Self-contained components for executing and exploiting the target host, excluding network communications.

## Other Payloads

- ==Functionality==: Each payload in Metasploit has a unique role within the framework, with some designed to handle various tasks during exploitation.
- ==Detection==: The size and target footprint of payloads are easy to detect, and the traffic they generate can attract attention.
- ==Metasploit Modularity==: Metasploit is a modular framework that allows for efficient management of the exploitation process, making it difficult to detect malicious activities.

Other payload types that are available within the framework are the following:

1. ==Meterpreter== is a payload designed to run in memory on the target host, avoiding detection by host-based intrusion detection systems. It doesn’t need to start its own process.  

2. ==PassiveX== is an antiquated payload used to circumvent outbound firewalls. It creates a hidden instance of Internet Explorer using ActiveX control, which still has vulnerabilities. Developers continuously update ActiveX techniques to prevent such attacks.

3. ==NoNX== is a CPU feature that prevents code execution in certain memory areas. Metasploit NoNX payloads are designed to bypass DEP.

4. ==Ord== is a Windows stager-based payload with advantages and disadvantages.
	**Advantages**:
	- Compatible with Windows 9x and later without a return address
	- Small
	**Disadvantages**:
	- Relies on ws2_32.dll being loaded in the target process before exploitation
	- Less stable than other stagers

5. ==IPv6== allows Metasploit and its payloads to function like IPv4 network-configured payloads. Metasploit payloads have adapted to function in an IPv6 environment.

6. ==Reflective DLL injection== is a technique where a stage payload is injected into a compromised host process running in memory, avoiding writing to the target hard drive. Both VNC and Meterpreter payloads use this technique.