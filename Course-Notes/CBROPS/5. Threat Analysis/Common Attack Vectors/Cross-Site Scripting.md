
- ==Definition==: Maliciously causing a script, typically JavaScript, to execute in a user’s browser.
- The victim is not aware that a malicious XSS attack has taken place on their system.

Three different types of xxs:

**Stored (persistent XSS)**
- **Attack Method:** Embedding malicious code within a stored page on the web server, such as comment boxes and message boards.
-  **Vulnerability:** Failure of the server to sanitize input, allowing the attacker’s code to be posted and displayed to all users.

**Document Object Model (DOM)**

>A DOM is a class of JavaScript that defines objects within HTML elements for use by the web browser.

1. The threat actor sends a message to a client containing a JavaScript URL embedded with malicious script tags. 
2. The client clicks on the URL and the client's web browser establishes an HTML connection to a vulnerable or exploited website. 
3. When a web browser loads a web page, it will create a DOM.  

- ==DOM Manipulation==: Threat actors can modify the browser’s DOM to extract sensitive information or execute malicious code.
- ==Malicious Script Execution==: Malicious script tags can be injected and executed on the client’s web browser, leading to actions like session cookie hijacking, site redirection, and malicious code execution.
- ==Impact Vulnerabilities==: Malicious actors can exploit vulnerabilities in the DOM route handler to inject and execute malicious scripts, potentially compromising sensitive data and executing malicious code.

**Reflected (nonpersistent** **XSS)** 

- ==Execution==: The attacker injects HTML code into a link, knowing the target page will fail to sanitize it.The user needs to click the link containing the HTML code again for the code to be executed.
- ==Impact==: An attacker can append the user login session cookie onto the URL of an image being requested from an external site. Armed with the cookie of the user, the attacker could then potentially masquerade as that user, gaining the full permissions of that user on the site.


The figure below illustrates a web page that requests a user to input a username. Instead, the attacker inputs functioning HTML code.

![3](/Course-Notes/.assets/Pasted_image_20241119203001.png)

The HTML code is accepted by the web page, which in turn attempts to display the Supplied name in a welcome message:

![2](/Course-Notes/.assets/Pasted_image_20241119220336.png)

But instead of displaying a welcome message, the HTML code is interpreted like actual code and (in this case) creates a pop-up window:

![1](/Course-Notes/.assets/Pasted_image_20241119220351.png)

The OWASP provides many resources for the defender to understand best security practices when developing web applications. The OWASP also provides guides such as the “XSS Filter Evasion Cheat Sheet,” to assist with testing web applications for poor filtering.