# File System
![1](/Course-Notes/.assets/Screenshot_2024-11-10_at_12.42.16.png)
- **/tmp:** Stores temporary files. It is often used as a workspace by applications. Users should not use this directory to store anything of any importance because many Linux distributions wipe this directory on boot, and in a default installation, any user is able to read and write to this directory. Attackers may use this folder to store malware, often as the first stage of an attack, because it is a consistent and permissive directory across Linux installations.
    
- **/home:** Location where the personal directories for users are stored. These directories should be secured because they often contain private and sensitive information (like configuration files with password, SSH private identity keys, and user files). 
    
- **/usr:** Used to store user-space programs and data. The reason for the /usr directory is mostly historical, but in modern Linux installations it contains several subdirectories:
    
    1. **/usr/local:** A location set aside for administrators to install software.
        
    2. **/usr/share:** Originally, this directory was used to share files between hosts that could be used on different Linux/Unix platforms. It was designed as a workaround when disk space was at a premium. Today's systems have no such constraints, so it is no longer used in that capacity. 
        
    3. **/usr/lib:** Stores library files that executable programs need to access at run time
        
    4. **/usr/bin** and **/usr/sbin:** These directories are used to store binary (compiled) executable files. These files make up the bulk of the Linux operating system. The **/usr/sbin** was traditionally reserved for files that can only be used by root, but that distinction no longer applies.
        
    5. **/usr/man:** This directory is used to store the manual pages, AKA “man pages,” that contain the documentation for important files in the operating system and installed applications.
        
- **/dev:** Contains device files. Hardware and virtual devices, such as terminals, appear as files to the operating system. When Linux needs to access a device, it often does so by interacting through device files. Unlike other directories here, this folder is "special" in that the files and folders inside are representations of hardware and objects in the kernel. For example, although it appears to be a file, /dev/sda may point to your first hard disk drive, and /dev/urandom is a secure random number generator.
    
- **/etc:** Stores system configuration files for the operating system and services. For example, SSL keys for web servers, private keys for SSH servers, and user accounts and passwords are kept here. This directory must be kept secure to keep the system secure.
    
- **/var:** This directory is used by the operating system and applications to store run-time data and log files. There are several subdirectories that are located here, two of which are common to all Linux distributions:
    
    1. **/var/log:** Used by the operating system and applications to store log files. At a minimum, non-privileged users must be prevented from writing to this folder. Otherwise, the integrity of the log files would be compromised after an attack.
        
    2. **/var/tmp:** Used as a workspace to store temporary run-time data for the operating system and running applications.
        
- **/bin and /sbin:** Used to store system binary files. Traditionally, files stored here were required to boot the operating system. All other system files were stored in the **/usr/bin** and **/usr/sbin** directories. But now, many files found in **/usr/bin** and **/usr/sbin** are required at boot time.
    
- **/lib:** Stores library files that must be available to executable files at run time.
