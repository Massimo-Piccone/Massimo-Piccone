
- ==Attack Type==: Directory traversal attacks exploit improper input validation to gain access to a file system.
- ==Exploitation==: Attackers exploit poor programming practices that fail to validate user input, allowing them to navigate outside the intended directory structure.
- ==Impact==: Attackers can access files and directories they shouldn’t have access to.

**Directory Traversal**
-  ==Attack Target==: Web servers and their root directories.
- ==Attack Goa==l: Accessing files and directories outside the web server’s root directory.
- ==Attack Method==: Crafting URLs to navigate to restricted directories and potentially execute programs on the host server.

![5](/Course-Notes/.assets/Pasted_image_20241119200236.png)

- ==URL Structure==: The URL is divided into two parts: the beginning (https://drive.google.com) represents the website being visited, while the rest functions like a directory structure on a computer.
- ==Directory Traversal==: This technique allows exploration of the file system by navigating through subfolders to access content.
- ==Analyst Familiarity==: Characters used in command-line navigation can be incorporated to aid in understanding the directory traversal process.

![4](/Course-Notes/.assets/Pasted_image_20241119200303.png)

- ==URL Structure==: The URL, including the port number, provides access to the website.
- ===Directory Navigation===: Using ..\ sequences in the URL navigates the file system, similar to command line navigation.
- ==File Access: Entering== ..\ sequences in the URL allows access to files on the web server, such as boot.ini.

![3](/Course-Notes/.assets/Pasted_image_20241119200321.png)

>Note: The escape-encoded URI: %255c decodes to a backslash, which is a form of obfuscation.

- ==Attacker’s Action==: The attacker has browsed to the location of an executable and passed it some arguments.
- ==Executable Example==: The attacker ran the Windows command prompt (cmd.exe) and executed a “dir” command.
- ==Potential Attack==: The attacker could have run other executables on the target system.

![2](/Course-Notes/.assets/Pasted_image_20241119200405.png)

This code will be injected into the website script and then parsed. The cookie will be processed and point the browser to the /etc/passwd file.

![1](/Course-Notes/.assets/Pasted_image_20241119200417.png)

The output is the contents of /etc/passwd. Some very valuable information can be gleaned here.

- ==Vulnerability==: Allows access to sensitive information like accounts, passwords, and code on web servers.
- ==Impact==: Can lead to target fingerprinting, account discovery, password retrieval, and even code execution.
- ==Mitigation==: Modern web servers include input checking and vulnerability checks to prevent directory traversal.