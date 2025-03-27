- ==HTTP Redirection==: A website can change the path to a resource using an HTTP redirect, directing the user’s browser to the new location.
- ==HTTP 302==: Response status code is commonly used for URL redirection.
- ==Security Implications==: Attackers exploit legitimate HTTP functions like HTTP redirects for attacks, making it crucial for security analysts to understand and mitigate these techniques.

- ==Location Header==: The URL of the new location.
- ==Browser Interpretation==: Browser should make an identical request to the new URL.

- ==Malware Obfuscation==: Attackers use web redirections to obfuscate the malware download source. Redirections are also less likely to raise suspicions as compared to hidden iFrames or external scripts
- ==Web Redirection Mechanism==: Attackers utilize “302 Found” responses to create a series of redirections, leading to the exploit delivery page.
- ==Purpose of Redirection Gates==: Frequently changing URLs of intermediate websites (gates) hinder attack analysis and make source determination difficult.

![2](/Course-Notes/.assets/Pasted_image_20241120125510.png)

1. The attacker has compromised a legitimate website (example.com).
2. The attacker causes the website to respond to the victim’s HTTP request with a 302 Found HTTP response status code.
3. This creates a series of HTTP 302 redirects through the attacker’s proxies.
4. The victim’s browser is finally redirected to the attacker’s web page that spreads the malicious exploit to the victim.

- ==Goal==: Ensure the victim’s web browser ends up on the attacker’s web page.
- ==Method==: Using iFrame or HTTP 302 cushioning.
- ==Malicious Exploit==: Served out to the victim from the attacker’s web page.

![1](/Course-Notes/.assets/Pasted_image_20241120125618.png)

Countermeasures:
- ==Cloud-based DNS security== service such as Cisco Umbrella to block the users from accessing malicious websites.
- ==Web proxy security== solution, such as the Cisco Web Security Appliance (WSA) to block users from accessing malicious websites.
- ==Educate== end users on how the browser is redirected to a malicious web page that delivers the exploit to the victim's machine through a series of HTTP 302 redirections
