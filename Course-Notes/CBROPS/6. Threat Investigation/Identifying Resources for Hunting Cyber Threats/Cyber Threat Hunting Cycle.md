Four stage Hunting loop
![1](/Course-Notes/.assets/Pasted_image_20241129154737.png)
Hypothesis:
- Use the ==hacker mindset== to form a hypothesis.
- ==Consider== the following:
	- Why would someone want to attack this network?
	- How would someone infiltrate the network?
	- What would the attacker target?
	- What is the attacker’s end goal?
	- What parts of the system contain valuable information, such as names, social security numbers, addresses, or trade secrets?

==Example== of a hypothesis:
- An attacker sends an email with a malicious link to members of the IT department to compromise accounts, and then uses their information to gain access to key pieces of infrastructure.

Investigate:
- The goal is to ==validate the hypothesis==.
- Use tools and techniques to ==investigate== the hypothesis.
- First sweep: Analyzes logs, queries data sets, and uses other tools to ==determine== if the hypothesis has ==merit==.
- Second Sweep: ==Advanced techniques==, such as data visualization and machine learning ==to help==.
- Looks for evidence that suggests the hypothesis is probable and likely to have been carried out.
- ==Find clues== that support the hypothesis and next stage.

Uncover:
- The hunter actively attempts to ==discover a pattern== or the attacker’s tactics, techniques, and procedures (==TTP==).
- TTP Example: An attacker achieves persistence, through specific registry key modifications.
- Investigate specific ==IOCs== to determine what activities support them.
- ==Linking IOCs== will show the storyline of the attack.
- ==Tracking==: Discover a list of individuals that the malicious email was sent to and determine which individuals clicked the link.
- Note what happened directly after the attack.
- This is where the ==success== of the cycle is achieved.
- The attacker has essentially been ==caught==.
- The ==TTPs== that are discovered will be ==shared== so that other hunters can search for those same data points.

Inform:
- ==Apply knowledge== to reduce risk and simplify future hunts.
- ==Documenting== the hunting cycle saves other analysts work when similar instances are encountered.
- ==Automation== reduces manpower for repeatable tasks.
- ==Create signatures and rules== for future detection systems.
- ==The key== to this stage is documentation and automation.
- Informs others of discoveries, 
	- Prevents duplication of effort, and 
	- Automates where appropriate to concentrate focus.

