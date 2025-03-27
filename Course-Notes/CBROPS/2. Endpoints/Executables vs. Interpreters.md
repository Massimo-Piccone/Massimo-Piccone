Executables == 
- Binary files 
- Run CPU code 
- Perform tasks independently

Interpreters ==
- An Application
- Reads instructions from source files
- Performs tasks on behalf of the source file
- Each source file is a script

Scripting methods:

- **bash:** Bourne Again Shell (bash) is the command-line shell that is used in most Linux installations. It provides a very feature-rich set of commands you can execute from the command line or as a script. A Bash shell script file is a plaintext file that begins with the following in the first line of the file:
    
    #!/bin/sh
    
    This entry is often referred to as a “shebang” and its purpose is to point the system to the interpreter that will run the file. In this case, /bin/sh is the command to run the bash shell. The remainder of the file will contain the shell commands to execute as part of the script. Lines that begin with the # character are not executed. They are used to enter comments so script authors can document information about the operation of the script for other users.
    
    Bash filenames typically end with the extension **.sh**, for example, `MyBashScript.sh`.
- **Perl:** Perl is a powerful, interpreted programming language. It is used extensively throughout the Internet for virtually every application imaginable. Once installed locally, you can write Perl scripts, and have Perl interpret and execute them. 
    
    A Perl script file begins with a line (shebang) to identify the application that should run it. It appears as follows:
    
    #!/usr/bin/perl
    
    The path may differ depending on where Perl is installed on the local host, but the purpose remains the same: to point to the Perl application when the script is executed. The remainder of the file consists of comments and the Perl code to execute.
    
    Perl files typically end with the file extension **.pl**, for example, `MyPerlScript.pl`.
    
- **Python:** Python is another very popular interpreted programming environment. It is not as widely used as Perl but it is gaining popularity because it is considered an easier programming environment to use than Perl. 
    
    Python script files begin with a shebang to point to the location of the interpreter. The following is an example of a Python shebang:
    
    #!/usr/bin/python3
    
    The path may differ depending on where Python is installed on the local system, but the purpose remains the same: to point to the Python application when the script is executed. The remainder of the file consists of code and comments.
    
    Python files typically end in a **.py** file extension, for example, `MyPythonScript.py`.
