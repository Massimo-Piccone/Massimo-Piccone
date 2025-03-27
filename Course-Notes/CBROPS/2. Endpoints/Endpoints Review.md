# Linux Overview
___ 
%% #review %%
# [[Linux File System]]

![3](/Course-Notes/.assets/Screenshot_2024-11-10_at_12.42.16.png)

| Directory                  | Description                                                                                                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /tmp                       | Stores ==temporary files==. It is often used as a workspace by applications.                                                                                                  |
| /home                      | Location where the personal ==directories for users== are stored.                                                                                                             |
| /usr                       | Used to store ==user-space programs== and data.                                                                                                                               |
| - /usr/local               | A location set aside ==for administrators== to install software.                                                                                                              |
| - /usr/share               | Originally, this directory was used to ==share files between hosts== that could be used on different Linux/Unix platforms.                                                    |
| - /usr/lib                 | Stores library files that ==executable programs need== to access at run time                                                                                                  |
| - /usr/bin and - /usr/sbin | These directories are used to store ==binary (compiled) executable== files.                                                                                                   |
| - /usr/man                 | This directory is used to store the manual pages, AKA “==man pages==”, that contain the documentation for important files in the operating system and installed applications. |
| /dev                       | Contains ==device files==. Hardware and virtual devices, such as terminals, appear as files to the operating system.                                                          |
| /etc                       | Stores system ==configuration files== for the operating system and services.                                                                                                  |
| /var                       | This directory is used by the operating system and applications to store run-time data and log files.                                                                         |
| - /var/log                 | Used by the operating system and applications to ==store log files.==                                                                                                         |
| - /var/tmp                 | Used as a workspace to store ==temporary run-time data== for the operating system and running applications.                                                                   |
| /bin and /sbin             | Used to store ==system binary files==. Traditionally, files stored here were required to boot the operating system.                                                           |
| /lib                       | Stores library files that must be available to ==executable files at run time==.                                                                                              |
# [[Devices]]

| Device Type | Description                                                               | Example                                |
| ----------- | ------------------------------------------------------------------------- | -------------------------------------- |
| Block       | Process data in fixed chunks.                                             | Disk drives, storage devices           |
| Character   | Work with data streams.                                                   | /dev/null, directly connected printers |
| Pipe        | Similar to character devices, but direct data streams to another process. | N/A                                    |
| Sockets     | Used for interprocess communication, such as network communication.       | N/A                                    |
You can tell a device’s type by listing the files in the **/dev** directory with file details. The following command lists files in a directory
### Permissions
#### Symbolic Permissions

| Final value | Permission         | Representation |
| ----------- | ------------------ | -------------- |
| 0 (0+0+0)   | No permission      | ---            |
| 1 (0+0+1)   | Execute            | --x            |
| 2 (0+2+0)   | Write              | -w-            |
| 3 (0+2+1)   | Write+Execute      | -wx            |
| 4 (4+0+0)   | Read               | r--            |
| 5(4+0+1)    | Read+Execute       | r-x            |
| 6 (4+2+0)   | Read+Write         | rw-            |
| 7 (4+2+1)   | Read+Write+Execute | rwx            |

| Access Class | Operator             | Access Type |
| ------------ | -------------------- | ----------- |
| u (user)     | + (add access)       | r (read)    |
| g (group)    | - (remove access)    | w (write)   |
| o (other)    | = (set exact access) | x (execute) |
| a (All)      | user, group, other   | rwx         |
## Disk and File Systems
Inside /dev (Devices)

- **/dev/sda:** The first physical disk
- **/dev/sda1:** The first partition of the first physical disk
- **/dev/sda2:** The second partition of the first physical disk

```
ed@labhost:~$ sudo parted -l

Model: VMware Virtual disk (scsi)
Disk /dev/sda: 322GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Disk Flags:

Number  Start   End    Size    Type      File system     Flags
 1      1049kB  314GB  314GB   primary   ext4            boot
 2      314GB   322GB  8588MB  extended
 5      314GB   322GB  8588MB  logical   linux-swap(v1)
```

### File System Types

| File System          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ext2, ext3, and ext4 | ==Native Linux== file systems, ext4 is the latest. Linux maintains backward compatibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| NTFS                 | Used by ==modern Windows==, it supports versatile permissions, large disks, and advanced features.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| FAT16, FAT32, exFAT  | Native to ==older Windows==, it’s mostly replaced by NTFS but remains common on USB storage devices. Linux is compatible but lacks permissions and large disk support.                                                                                                                                                                                                                                                                                                                                                                           |
| ISO 9660 and JOLIET  | Optical media file ==system standards==.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| HFS+                 | ==Apple’s file system for X==. Linux has drivers for read/write compatibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Swap                 | A special file system used in Linux swap partitions. It’s disk space reserved for the system to ==use when it needs to free memory==. RAM is faster than disk drives, so ideally, everything should run in RAM. However, if the system runs low on RAM, it can move data to the swap partition. Swap space isn’t a file system; it’s directly addressable disk space for temporarily dumping content from RAM. When main memory is oversubscribed, system performance degrades because data moves more frequently between RAM and the swap disk. |
### Mounting Devices
To manually mount a device, use the `mount` command. The basic syntax is as follows:
`mount -t <_type_> <_device name_> <_mount point_>`

 - Linux mounts disks on boot and references /etc/fstab for configuration. 
 - You can override configuration parameters with the –o option. 
 - Newer /etc/fstab lists devices by their UUID numbers for better identification. 
 
```
# / was on /dev/sda1 during installation
UUID=339228c9-cbc3-4503-950f-40415e03779f / ext4 errors=remount-ro 0 1
```

| Column             | Description                                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------------- |
| UUID of the device | Refers to the device file and is used by Linux for device tracking. Example: /dev/sda1.              |
| Mount point        | Indicates where the root of the file system is located. Example: root (/).                           |
| File system type   | Describes the type of file system used. Example: ext4.                                               |
| Options            | Specifies operating parameters, such as actions on encountering errors (e.g., remount as read-only). |
| Dump frequency     | Deprecated and not relevant in modern Linux environments.                                            |
| Pass number        | Configures the order devices should be mounted; root is 1, others are 2.                             |
# [[System Initialization]]

The Linux boot process:
1. Hardware checks
2. Device bus discovery
3. Device discovery
4. Kernel subsystem initializes
5. Root file system mounts
6. Start user processes

Boot parameters that are processed by the bootloader are called **/proc/cmdline**.

```
BOOT_IMAGE=/boot/vmlinuz-4.4.0-22-generic root=UUID=339228c9-cbc3-4503-950f-40415e03779f ro quiet splash
```

## How Linux Controls the Boot Process

| System        | Description                                              |
| ------------- | -------------------------------------------------------- |
| System V init | Uses a series of scripts located in a startup directory. |
| Systemd       | Initializes services and processes in parallel.          |
## Run Levels

| Run Level | Description                                                         |
| --------- | ------------------------------------------------------------------- |
| 0         | Halt the system                                                     |
| 1-2       | Emergency repair                                                    |
| 3         | Default run level to start the system without a graphical interface |
| 5         | Default run level to start the system with a graphical interface    |
| 6         | Reboot the system                                                   |
## Common Boot Management Processes
Traditional System V Bootup

| Component              | Description                                            | Role                                                 |
| ---------------------- | ------------------------------------------------------ | ---------------------------------------------------- |
| init                   | A process that controls the startup of user processes. | Controls the startup of user processes.              |
| /etc/inittab           | A configuration file.                                  | Specifies the run level and startup instructions.    |
| Run level              | A state of the system.                                 | Determines which services are started.               |
| start and stop scripts | Scripts located in the run level directory.            | Start and stop services for the specified run level. |
/proc/cmdline - can be referenced to show the boot parameters

# [[Emergency - Alternate Startup Options]]

Issues may require a safe configuration or external boot for a clean environment.

**Single User**
- ﻿﻿It initializes the system into run level 1
	- ﻿﻿only essential services and processes
	- ﻿﻿No GUI
	- ﻿﻿No networking
	- ﻿﻿CLI only
- ﻿﻿To preserve the system do not use single user mode
	- ﻿﻿Uses files on disk to boot system
	- ﻿﻿Modifies critical files and timestamps
	- ﻿﻿Hinders forensics

The steps for entering single user mode are as follows:

| Step | Action                                            | Notes                                   |
| ---- | ------------------------------------------------- | --------------------------------------- |
| 1    | Boot the system                                   | BIOS splash screen will appear.         |
| 2    | Press left shift key                              | Displays GRUB menu.                     |
| 3    | Select ‘Advanced Options’                         | Use up/down arrow keys.                 |
| 4    | Select kernel with ‘(recovery mode)’              | Newest kernel is typically at the top.  |
| 5    | Press Enter                                       | Enters recovery mode menu.              |
| 6    | Select ‘root’                                     | Enters single user mode command prompt. |
| 7    | Press Enter                                       | Enters command prompt.                  |
| 8    | Execute commands                                  | File system is mounted read-only.       |
| 9    | Remount file system in read/write mode (optional) | Type ‘mount -o remount,rw /‘            |
| 10   | Complete tasks                                    | Type ‘reboot’ when finished.            |
| 11   | System restart                                    | System should restart normally.         |
## Live Boot

- ﻿﻿Boot from external media
	- ﻿﻿Purpose built for troubleshooting and recovery
- ﻿﻿Prefer this method over Single User mode
	- ﻿﻿Some distributions do not mount file systems, use files on disk, or access the network

## Shutting Down the System

| Option   | Description                                          |
| -------- | ---------------------------------------------------- |
| --help   | Show this help                                       |
| - H      | Halt the machine                                     |
| - P      | Power-off the machine                                |
| - r      | Reboot the machine                                   |
| - h      | Equivalent to —poweroff, overridden by —halt         |
| - k      | Don’t halt/power-off/reboot, just send warnings      |
| -no-wall | Don’t send wall message before halt/power-off/reboot |
| - C      | Cancel a pending shutdown                            |

| Time Parameter | Description                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------ |
| hh:mm          | The hour in 24-hour format followed by the number of minutes.                                                |
| +m             | The number of minutes from the time the command was issued.                                                  |
| now            | The time parameter will also accept the keyword “now” to indicate that the command will execute immediately. |
# [[System Processes]]

- Processes are identified by PIDs.
	- Ensure resource allocation.
- Created using the fork-and-exec mechanism.
	- Parent duplicates itself and can be replaced.
## Displaying Processes and Process Threads

### The Top Command
> The **top** application is divided into two sections

The upper portion lists general information regarding system resource utilization as follows: 

| Metric              | Description                                                              |
| ------------------- | ------------------------------------------------------------------------ |
| System Uptime       | The total time the system has been running since its last reboot.        |
| System Load Average | The average CPU load over the last 1, 5, and 15 minutes.                 |
| Processes           | A summary of the number of processes running on the host.                |
| CPU Utilization     | A breakdown of CPU usage by user space, system processes, and idle time. |
| Memory Utilization  | A breakdown of system memory usage.                                      |
| Swap Utilization    | A breakdown of swap space usage.                                         |
The columns of information that is displayed by **top** are as follows:

| PID  | User | PR  | NI  | VIRT       | RES    | SHR   | S   | %CPU | %MEM | TIME+/ | COMMAND |
| ---- | ---- | --- | --- | ---------- | ------ | ----- | --- | ---- | ---- | ------ | ------- |
| 2000 | root | 20  | 0   | 1234567890 | 123456 | 12345 | S   | 0.3  | 2.0  | 1:00   | bash    |
| 2002 | root | 20  | 0   | 32541230   | 2351   | 3251  | S   | 0.1  | 1.0  | 2:00   | bash    |


- **PID:** Process ID number. 
- **User:** The user name of the process’s owner
- **PR:** The scheduling priority of the process
- **NI:** The process’s **priority** value. ==negative values indicating higher priority.== 
- **VIRT:** Virtual memory
- **RES:** Resident, non-swapped physical memory
- **SHR:** Shared memory
- **%CPU:** The estimated percentage of CPU resources being consumed by the process
- **%MEM:** The percentage of physical memory being consumed by the process
- **TIME+/–:** The total CPU time the process has consumed since it started
- **COMMAND:** The name of the process

| S   | Process status                                                                        |
| --- | ------------------------------------------------------------------------------------- |
| D   | Uninterruptible sleep (stuck waiting for input or output)                             |
| R   | Running (executing normally)                                                          |
| S   | Sleeping (waiting internally)                                                         |
| T   | Stopped by job control (stopped with a signal from the kernel)                        |
| t   | Stopped by debugger (another process has full control)                                |
| Z   | Zombie (completed processes that are not yet removed from the kernel’s process table) |
## The ps Command

Extract specific information about processes.
- **UNIX:** Options can be grouped and must be preceded by a dash.
- **BSD:** Options can be grouped and must not be preceded by a dash.
- **GNU:** Long form where options are preceded by double dashes.

| Option | Description                                                |
| ------ | ---------------------------------------------------------- |
| -e     | all users                                                  |
| -f     | full (UID, PPID, C:, STIME)                                |
| aux    | displays an overview of all the processes that are running |
| -C     | Specify processes related to Damon                         |
| -o     | specify information that you want about a process          |
## Displaying Open Files

### The lsof Command
```
ed@carl:~$ sudo lsof /var/log/syslog
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
rsyslogd 651 syslog    5w   REG    8,1   161355 4063351 /var/log/syslog
```

| Command | PID  | User | FD  | Type | Device | Size/Off | Node    | Name      |
| ------- | ---- | ---- | --- | ---- | ------ | -------- | ------- | --------- |
| lsof    | 2000 | root | 0u  | REG  | 0x8000 | 1024     | 2097152 | /dev/null |
| lsof    | 2133 | root | 1u  | REG  | 0x8000 | 1024     | 2343251 | /dev/null |
- **Command:** The name of the process using the file.
- **PID:** The process ID of the command using the file.
- **User:** The user running the process.
- **FD:** File descriptor: a reference number that is used by the kernel to identify an open file. File descriptors may be followed by a code letter to further describe the state of the file. In the example, the letter “w” indicates that the process has a write block on a portion of the file.
- **Type:** Identifies the type of file. For example, DIR represents a directory, inet is a network connection or BLK to represent a block device such as a disk drive. The example lists the type as REG which represents a regular file.
- **Device:** Device number that represents the device being called to perform the I/O.
- **Size/Off:** The file size or memory offset. The `lsof` command will display whichever one is appropriate for the file being listed.
- **Node:** The file’s INODE number, which is used to uniquely identify the file on the file system.
- **Name:** The path and filename

To list the processes that are accessing log files in a directory, use the +D option

## Monitoring CPU and Memory Utilization

top -p [PID]
vmstat — top with refresh time parameter 


| Category | Metric | Description                                           |
| -------- | ------ | ----------------------------------------------------- |
| procs    | -r     | Number of processes in a runnable state               |
|          | -b     | Number of processes in uninterruptible sleep          |
| memory   | -swpd  | Virtual memory used                                   |
|          | -free  | Available memory                                      |
|          | -buff  | Memory used for buffering by the kernel               |
|          | -cache | Memory reserved as cache                              |
| swap     | -si    | Swapped in                                            |
|          | -so    | Swapped out                                           |
| io       | -bi    | Blocks received from block device                     |
|          | -bo    | Blocks sent to block device                           |
| system   | -in    | Number of interrupts                                  |
|          | -cs    | Number of context switches                            |
| cpu      | -us    | CPU time spent processing non-kernel (user) processes |
|          | -sy    | CPU time spent processing kernel processes            |
|          | -id    | CPU idle time                                         |
|          | -wa    | Time spent waiting for I/O                            |
|          | -st    | Time stolen from virtual machine                      |
## Monitoring I/O with `iostat`

```
ed@carl:~$ iostat 2

Linux 4.4.0-22-generic (carl) 06/11/2016 _x86_64_(4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
			1.88    0.00    0.22    0.00    0.00   97.90

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.18         1.14         4.89     691475    2978716
```
# Other Useful Command-Line Tools

## Using History
```
u@test:~$ history | less (grep maybe?)
	732  [command]
# You can recall this command using its number
u@test:~$ !732
	[command outupt]
u@test:~$ !! 
	[previous command]
```
## The `awk` Command

- ==Text processing tool== in Linux OS, 
- **awk** can take its input from files, STDIN, or even devices.

The basic workflow is as follows:
	1. Read a line of input. Lines are typically terminated with newline characters. When **awk**encounters a newline character, that signals the end of the line.
	2. Execute commands on the line.
	3. Move on to the next line if it has not reached the end of the file.
## The `sed` Command

- ==Stream editing tool==
- configure on lines of text that are read in from files or STDIN
- Lines are determined when `sed` encounters a newline character.
- perform string substitutions. 

The general syntax of the `sed` command is as follows:
	`sed –e ‘s/<input pattern>/<output pattern/<options>’`

Implement `sed` for simple text substitution:

```
ed@carl:~$ echo "left" | sed -e 's/left/right/'
right
```
## The vi Command

Full-screen visual interface for ==editing text files==
 - Command mode for issuing commands 
 - Insert mode for text entry and editing.
	- Accessed from command mode by pressing “i”, indicated by “Insert” in the status area, and exited by pressing “Esc”.
	- Saving Edits: In command mode, press “:” to display a colon, then “w” followed by Enter to save the edits.
	- Quitting the Application: Press colon (:), then q (quit), then exclamation point (!), to override the warning message and exit without saving.
	- Saving Edits: Enter :, then w (write), then q (quit) to save and exit.
	- Deleting Characters: Press x in command mode to delete the character under the cursor. Use dd to delete the entire line, dw to delete from the cursor to the end of the word, and yw to yank a word.

- Text Manipulation: Yanked or deleted text can be recovered, and text can be inserted or appended at specific locations.
- Navigation: Commands like “h”, “j”, “k”, “l”, “w”, “b”, “$”, “^”, “gg”, and “G” allow for moving the cursor within a file.
- Search and Replace: The “:” command, followed by `“/<search pattern>/<replacement text>/g”`, enables searching and replacing text in a file.

# [[Networking]]

### Secure Shell Protocol (`SSH`)

- SSH is the preferred tool for remotely accessing Linux hosts.
	- ==Encrypted channel== to mitigate security risks.
	- Authenticate with ==credentials== or ==public/private== key pairs.
- SSH can also be used to ==tunnel non-encrypted protocols== over SSH.

Sharing Files over SSH
```
scp <source> <user@host>: <remote dst>
```

### **`netstat`** Command

- View network connections and stats
- Check active connections
- Routing tables
- Interface statistics
- Protocol usage

- Active Connections: List all active network connections and listening ports (netstat -tuln).
- Routing Tables: View current routing tables (netstat -r).
- Interface Statistics: Check statistics for each network interface, including errors and dropped packets (netstat -i).
- Network Protocols: Monitor the usage and statistics of network protocols like TCP, UDP, and ICMP (netstat -s).
- `–rn` options as shown displays the routing table with numeric IP addresses. If you prefer to see hostnames, you can remove the `n` option.

```
ed@ned:~$ **netstat -rn**
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.7.1     0.0.0.0         UG        0 0          0 ens160
192.168.7.0     0.0.0.0         255.255.255.0   U         0 0          0 ens160
```

The IP address 0.0.0.0 with a netmask of 0.0.0.0 represents any IP address.

### `ifconfig` Command (Or IP)

| Purpose                                                                                                      | Description                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configures and displays the status of network interfaces.                                                    | View or change IP, netmask, broadcast address; activate/deactivate interfaces                                                                                  |
| View information such as IP address, MAC address, netmask, and broadcast address for each network interface. | View information such as IP address, MAC address, netmask, and broadcast address for each network interface.                                                   |
| Bring network interfaces up or down (ifconfig eth0 up/down).                                                 | Bring network interfaces up or down (ifconfig eth0 up/down).                                                                                                   |
| Change IP address, netmask, and other configuration settings for network interfaces.                         | Change IP address, netmask, and other configuration settings for network interfaces.                                                                           |
| Note: ifconfig is largely deprecated and replaced by ip in newer Linux distributions.                        | Note: ifconfig is largely deprecated and replaced by ip in newer Linux distributions.                                                                          |
| Typical Example:                                                                                             | The ifconfig (or ip) command accepts many options, but with the syntax shown in the following example, a lot of information is retrieved about the interfaces. |
##### Configuring Basic Properties (IP, Subnet Mask, Gateway)

```
ed@carl:~$ sudo ifconfig ens160 192.168.7.73 netmask 255.255.255.0 broadcast 192.168.7.255
```

### **`route`** Command

The route command is used to modify or view the IP routing table.

- It can be used to view the current routing table, set a default gateway, and add or remove specific routes.
- To add a default gateway, use the following command:
	sudo route add default gw 192.168.7.1
- To statically set a route to a network, use the following command:
	route add -net 192.168.7.0 netmask 255.255.255.0 gw 192.168.7.1

```
ed@ned:~$ sudo route add -net 192.168.133.0 netmask 255.255.255.0 gw 192.168.7.200

ed@ned:~$ netstat -rn

Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.7.1     0.0.0.0         UG        0 0          0 ens160
192.168.7.0     0.0.0.0         255.255.255.0   U         0 0          0 ens160
192.168
```

The structure of the `route` command for entering the static route is as follows:
- **route:** The `route` command
- **add:** The option to indicate that you wish to add a route
- **-net:** The option to indicate that the destination of the route is a network
- **192.168.133.0:** The IP address of the destination network
- **netmask 255.255.255.0:** The netmask value for the destination network
- **gw 192.168.7.200:** The gateway IP address of where to send traffic that is destined for the 192.168.133.0 network

**Purpose:** Displays or modifies the IP routing table.

**Uses:**
	• **View Routing Table:** See the current routing table to understand how packets are routed.
	• **Add/Remove Routes:** Define custom routes or remove routes to control packet paths (route add and route del).
	• **Default Gateway:** Set a default gateway for outgoing packets.

# [[Managing Services in SysV Environments]]

| Command   | Description                                                                                          | Example                                                  |
| --------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| service   | Operates on files in /etc/init.d. Used with the old init system.                                     | `ps -ef \|grep [service]`                                |
| ""        | Starts, stops, or restarts a service.                                                                | `sudo service &lt;service name&gt; start\|stop\|restart` |
| systemctl | Operates on files in /lib/systemd. Falls back to /etc/init.d if a file is not found in /lib/systemd. | `systemctl [command] [unit name]`                        |
| ""        | Reloads the VS FTP daemon configuration files without stopping the service.                          | `sudo systemctl reload vsftpd`                           |
| ""        | Reloads the systemd configuration and dependencies without stopping services.                        | `sudo systemctl daemon-reload`                           |
# [[Viewing Running Network Services]]

#### netstat Command

| Command            | Description                                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| netstat            | List running services                                                                                                                        |
| netstat -a46       | Shows IPv4 and IPv6 connection information.                                                                                                  |
| netstat -lt        | Shows TCP connections in the listen state.                                                                                                   |
| netstat -lun       | Shows UDP connections in the listen state.                                                                                                   |
| sudo netstat -atnp | Shows TCP connections in any state, with host and port information in numeric format, and the program name and PID of the listening process. |

#### lsof Command

| Command                           | Description                                                         |
| --------------------------------- | ------------------------------------------------------------------- |
| sudo lsof -i                      | List files associated with an internet address.                     |
| sudo lsof -i tcp                  | List files associated with an internet address using TCP.           |
| sudo lsof -i tcp:80               | List files associated with an internet address using TCP port 80.   |
| sudo lsof -i udp:53 -P            | List files associated with an internet address using UDP port 53.   |
| sudo lsof -i @192.168.222.1       | List files associated with the specified internet address.          |
| sudo lsof -i @192.168.222.1:21 -P | List files associated with the specified internet address and port. |
# [[Name Resolution - DNS]]

## Name Resolution Configuration Files
#### **resolv.conf** 

| Directive                       | Description                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------- |
| Search domain                   | Lists domains to append when resolving a hostname with no domain.                       |
| Name server                     | Identifies the IP addresses of the DNS servers to use for resolving hostnames.          |
| **Security Consideration**      | **Description**                                                                         |
| Invalid Name Servers or Domains | Domains or DNS servers not associated with the organization.                            |
| Public DNS Servers              | Servers like Google (8.8.8.8, 8.8.4.4, 4.2.2.1) used to bypass enterprise DNS policies. |
#### **nsswitch.conf**

| Method | Description                                                                                                                        |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| files  | Represents local files on the host                                                                                                 |
| compat | Similar to files, but extends its capabilities by allowing entries in the files to grant users or user groups access to the system |
| dns    | Reference DNS servers                                                                                                              |
| db     | Do lookups in database files on the local system                                                                                   |
##### Security considerations  

1. A user on the system executes malware.
2. The malware creates an entry in the /etc/hosts file with the IP address of malicious web server.
    1. The malicious web server is configured to look like a banking website that is frequented by the operator of the system.
    2. The IP address of the entry in the /etc/hosts file maps to the hostname of the user’s banking website.
3. The malware also configures the **nsswitch.conf** file to do a file lookup first followed by a DNS lookup.
4. The next time that the user goes to visit the banking site, the host looks at the **/etc/hosts** file first and finds the name of the banking site in the file.
    1. The IP address that is mapped to the banking site is that of the malicious server that is disguised as the real banking site.
    2. Since the name was resolved with the **/etc/hosts** file, there is no need to reach out to DNS to resolve the name. 
5. The user is presented with a web page that looks exactly like his or her regular banking site’s page.
6. The user enters his or her banking credentials which the malicious server records.
7. Instead of granting the user access to his or her bank account, the malicious server pops up a message indicating that the banking site is down for maintenance and to try again later.
## Testing Name Resolution

### `nslookup` 

```
ed@ubuntu:/usr/lib/systemd$ nslookup 72.163.4.161

Server:127.0.1.1
Address:127.0.1.1#53

Non-authoritative answer:
161.4.163.72.in-addr.arpaname = www1.cisco.com
```
### `whois`

```
ed@ubuntu:/usr/lib/systemd$ whois 72.163.4.161

#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/whois_tou.html
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/public/whoisinaccuracy/index.xhtml
#
#
# The following results may also be obtained via:
# https://whois.arin.net/rest/nets;q=72.163.4.161?showDetails=true&showARIN=false&showNonArinTopLevelNet=false&ext=netref2
#
NetRange:       72.163.0.0 - 72.163.255.255
CIDR:           72.163.0.0/16
NetName:        CISCO-GEN-7
NetHandle:      NET-72-163-0-0-1
Parent:         NET72 (NET-72-0-0-0-0)
NetType:        Direct Allocation
OriginAS:       
Organization:   Cisco Systems, Inc. (CISCOS-2)
RegDate:        2006-10-24
Updated:        2015-08-13
Ref:            https://whois.arin.net/rest/net/NET-72-163-0-0-1
```
# [[Viewing Network Traffic]]

## Tcpdump Basics

`sudo tcpdump &lt;options&gt; &lt;filters&gt;`  
`sudo tcpdump –i ens33 –Xnns 0 host 192.168.222.1`

- -i: Specifies the listening interface. If omitted, tcpdump selects the first available interface. If there’s an inline device with bridged interfaces, list them as ens32:ens33.
- -X: Outputs payload in both hex and ASCII.
- -nn: Outputs host addresses and ports in numeric format.
- -s: Snap length. Refers to the number of bytes to include in the capture or output. Defaults to a local environment-based value, sometimes as small as 64 bytes. Entering 0 includes all payload bytes.
- host 192.168.222.1: Filters packets to or from the specified host.
## Refine
Further refine your filter by adding a port constraint as follows:
- `and [condition]` — add 
- `and not [condition]` — **negation** 
- `> dump.txt` to output into a file 
- `-r` read pcapfile
- `–X` to output in both hex and ASCII
- `-nn` for numeric IP addresses and port numbers
- `–s 0` for displaying the entire payload

# [[Configuring Remote Syslog]]

| Rule Syntax                                                   | Description                                                                                                 |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| \*.\* @&lt;remote host name or IP address&gt;:&lt;port&gt;    | Forwards all events to the specified remote host and port using UDP.                                        |
| \*.\* @@&lt;remote host name or IP address&gt;:&lt;port&gt;   | Forwards all events to the specified remote host and port using TCP.                                        |
| \*.emerg @&lt;remote host name or IP address&gt;:&lt;port&gt; | Forwards alerts with a severity of emerg from any facility to the specified remote host and port using UDP. |
## Testing Your Logging Configuration

**Example: `auth,authpriv.*   /var/log/auth.log`**
	This rule sends alerts from the **auth** or **authpriv** facilities with any severity to the **/var/log/auth.log** file. To , use the following command:

**Test: `logger –p auth.info “My auth.info logging test”`**
	After you execute the command, you open the **/var/log/auth.log** file and navigate to the end of the file to see the following entry if the rule worked correctly:

**Check: `[date/time][usr]: My auth.info logging test`**
	You can also use the `logger` command to send messages to remote syslog servers. The following example adds the `–n` parameter, which lets you specify a remote host, the `–P` (upper case) parameter to specify the port number and you can add `--UDP` to send as a UDP connection or `--TCP` to send it over TCP. If you do not specify a protocol, it will first try UDP and if that fails it will try TCP. Also, if you do not specify a port, it will use the default port 514.

`logger –p auth.info –n 192.168.222.1 –P 10514 --UDP “My auth.info logging test”`

# [[Running Software on Linux]]
Running software in a Linux installation requires two things:

| Requirement | Description                                                                     |
| ----------- | ------------------------------------------------------------------------------- |
| File Format | Must be in a format that allows it to run on its own or through an interpreter. |
| Permissions | The execute bit must be set in the file’s permission properties for the user.   |
GNU Compiler Collection (gcc), which is a popular, Open Source compiler for C source code.
## Overview of the Process for Compiling Code

1. obtain the source code of the program you wish to compile into a binary executable. 
2. make the source code yourself or obtain it from other sources.

Compiling locally ensures that the binary code that is produced takes platform-specific differences into account at compile time.
## Types of Files Used in Compiling Software

| File Type           | Description                                                                        | Example               |
| ------------------- | ---------------------------------------------------------------------------------- | --------------------- |
| Source files        | Actual program written in a programming language (e.g., C).                        | myprog.c              |
| Object files        | Compiled binary code libraries.                                                    | myobjectfile.o        |
| Archive files       | Contain multiple object files.                                                     | myarchivefile.a       |
| Shared object files | Contain code referenced by the application at runtime.                             | mysharedobjectfile.so |
| Header files        | Contain function declarations, macro definitions, constants, and system variables. | myheader.h            |
## Compiling Code
### GCC
The general process for compiling a program with gcc is as follows:
`gcc –o <output file> <source file>`
### Autotools

| Script              | Purpose                                                                        |
| ------------------- | ------------------------------------------------------------------------------ |
| `configure`         | Probes the system to ensure necessary components are present.                  |
| ``                  | Gathers information about the host system for binary compatibility.            |
| ``                  | Accepts parameters to customize the application.                               |
| ``                  | Often used to enable or include specific features.                             |
| `make`              | Invokes the compiler (gcc) to produce binary files for the application.        |
| `sudo make install` | Copies the application and supporting files to standard file system locations. |
With autotools, the general sequence to install an application in Linux is the following:

| Step                        | Description                         | Example Command                   |
| --------------------------- | ----------------------------------- | --------------------------------- |
| Obtain the archive package  | Download the source code archive.   | tar zxvf src/snort-2.9.5.3.tar.gz |
| Unpack the archive          | Extract the files from the archive. | cd snort-2.9.5.3                  |
| Run the configure script    | Configure the build environment.    | ./configure —enable-sourcefire    |
| Run the make script         | Compile the application.            | make                              |
| Run the make install script | Install the application.            | make install                      |
At this point, the application is installed and ready to use. The following example illustrates how to install Snort using autotools:

| Command                                                       | Description                                                 |
| ------------------------------------------------------------- | ----------------------------------------------------------- |
| [root@snortbox local]# tar zxvf src/snort-2.9.5.3.tar.gz      | Unpacks the archive file containing the software.           |
| [root@snortbox local]# cd snort-2.9.5.3                       | Enters the directory created when the archive was unpacked. |
| [root@snortbox snort-2.9.5.3]# ./configure —enable-sourcefire | Executes the configure script with command-line parameters. |
| [root@snortbox snort-2.9.5.3]# make                           | Executes the make script to compile the code.               |
| [root@snortbox snort-2.9.5.3]# make install                   | Copies the files to their destination directories.          |
# [[Executables vs. Interpreters]]

| Category     | Description                                                                                                                  |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| Executables  | Binary files Run CPU code Perform tasks independently                                                                        |
| Interpreters | An Application Reads instructions from source files Performs tasks on behalf of the source file Each source file is a script |
Scripting methods:

| Shell  | Description                                                      | Shebang            | File Extension |
| ------ | ---------------------------------------------------------------- | ------------------ | -------------- |
| Bash   | Bash is the command-line shell used in most Linux installations. | #!/bin/sh          | .sh            |
| Perl   | Perl is a powerful, interpreted programming language.            | #!/usr/bin/perl    | .pl            |
| Python | Python is another popular interpreted programming environment.   | #!/usr/bin/python3 | .py            |
# [[Using Package Managers to Install Software in Linux]]

| Package Manager            | Description                                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Red Hat Package Management | Used in Red Hat-based installations or Red Hat derivative distributions, such as Red Hat Enterprise Linux, Fedora Core, or CentOS. |
| .deb                       | Primarily used in Debian-based installations, including Ubuntu and any of its derivatives, for example Linux Mint or Knoppix.      |
## Package Managers

| Package Manager | Description                                                         | Install Command                |
| --------------- | ------------------------------------------------------------------- | ------------------------------ |
| yum             | Used for managing RPM-based packages on Redhat-based installations. | yum install <package name>     |
| apt             | Used for managing packages on Debian-based Linux installations.     | apt-get install <package name> |
# [[System Applications]]
## Web

| Feature                         | Description                                                            |
| ------------------------------- | ---------------------------------------------------------------------- |
| Data Compression                | Reduces bandwidth usage and speeds up page loading.                    |
| SSL Encryption                  | Secures web connections, ensuring data privacy and integrity.          |
| Server-Side Language Interfaces | Supports languages like Perl, Python, and PHP for dynamic web content. |
## Database

| **Category**              | **Description**                                                                                                   |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Linux-based platforms** | Offer various database services, both Open Source and commercial, including relational and NoSQL databases.       |
| **Relational databases**  | Use linked structures or tables to store information, utilizing SQL for interaction and data extraction.          |
| **NoSQL databases**       | Lack strict data structures, allowing free data storage, requiring large space but enabling faster retrieval.     |
| **MySQL**                 | A structured, relational database system using SQL for interaction, widely installed.                             |

| **Database log files** | Provide valuable security information, varying between products, typically in `/var/log` or subdirectory.         |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Error log**          | Stores information on system errors, starts, and stops, commonly at `/var/log/mysql/mysql_error.log`.             |
| **General query log**  | Contains general information about database access, typically found at `/var/log/mysql/mysql.log`.                |
| **Slow queries log**   | Lists slow or incomplete queries, indicating potential system issues, usually at `/var/log/mysql/mysql-slow.log`. |
# [[Lightweight Directory Access Protocol]]

- Used for accessing directory services, such as:
	- ﻿﻿Users
	- ﻿﻿Groups
	- ﻿﻿Password
	- ﻿﻿Additional resources

Syntax uses x.500 standard for identifying objects in the LDAP
Attributes consist of an attribute name followed by the attribute value.

| Attribute | Value           |
| --------- | --------------- |
| telephone | +1 222 333 4455 |

| Attribute               | Value                           |
| ----------------------- | ------------------------------- |
| distinguished name (DN) | dn: cn=ed smith,dc=MyOrg,dc=com |
| canonical name (CN)     | cn: ed smith                    |
| given name              | ed                              |
| sn                      | smith                           |
| mail                    | esmith@MyOrg.com                |

# Endpoint Security Technologies
___ 
# [[Host-Based Personal Firewall]]

| Firewall Type        | Description                                                                   | Implementation                                                      |
| -------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Personal Firewall    | Protect individual hosts by controlling traffic arriving at and leaving them. | Individual hosts                                                    |
| Distributed Firewall | Pervasive use of personal firewalls, controlled by a centralized system.      | Centralized system controlling personal firewalls on multiple hosts |
Crucial for protecting access in
- Mobile systems 
- Split tunnelling for remote-access VPNs

| Feature                  | Description                                                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| NGFW Features            | Provide protocol and port-based policies, application-level traffic control, and network-specific policy definitions. |
| Application Control      | Allow and deny traffic based on application lists, with options for user-defined rules and malware protection.        |
| Monitoring and Reporting | Monitor incoming and outgoing connections, track traffic handling, and potentially alert users to suspicious activity |
#### Firewall logs 
Logs are configurable but typically include: 
- Blocked connections / packets
- Related 5Tuple information of connections.

| Log File                       | Use                                                         |
| ------------------------------ | ----------------------------------------------------------- |
| Outbound / Inside connections  | Potential attack on other computers                         |
| Repeated unsuccessful attempts | Possible brute-force attack                                 |
| Suspicious IP activity + WHOIS | Note: Attackers often use spoofed IPs                       |
| Host-based firewall logs       | Requires specialized correlation tools for optimal analysis |

### Windows firewall host-based firewall

| Rule Type        | Description                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------- |
| Program rules    | Control connections for an application or program                                        |
| Port rules       | Control connections for specific ports and protocols                                     |
| Predefined rules | Apply to specific Windows services and features                                          |
| Custom rules     | Combine several different parameters, including programs, protocols, ports, and services |
To create a rule in Windows Firewall with Advanced Security, follow these steps:

| Step | Action                                                                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Select the category for which you want to create a new rule: Inbound Rules, Outbound Rules, or Connection Security Rules.                      |
| 2    | Click New Rule in the Action pane.                                                                                                             |
| 3    | Select the rule type in the Rule Type screen.                                                                                                  |
| 4    | Follow the wizard to create the rule.                                                                                                          |
| 5    | Specify the action to be taken when a connection matches the specified conditions.                                                             |
| 6    | Specify when you want the rule to apply (when your computer is connected to its corporate domain, a private network, and/or a public network). |
Windows Firewall **logging** can help you identify malicious activity. Logging is disabled by default. To create a log file, complete the following steps:

| Step | Action                                                              |
| ---- | ------------------------------------------------------------------- |
| 1    | Click Properties in the right panel.                                |
| 2    | In the dialog box, select the Private Profile tab.                  |
| 3    | In the Logging area, click Customize.                               |
| 4    | In the new window, set the maximum log size, location, and content. |

To view your log file, complete the following steps:

| Step | Action                                                                   |
| ---- | ------------------------------------------------------------------------ |
| 1    | Open the main Windows Firewall with Advanced Security window.            |
| 2    | Click Monitoring.                                                        |
| 3    | In the Monitoring pane, click the file path link under Logging Settings. |
| 4    | To the right of File Name, click the file path link.                     |
| 5    | The log opens in Notepad.                                                |
The log file contains the following information (and much more) about each event:

- Date
- Time
- Action taken
- Protocol used
- Source IP address
- Destination IP address
- Source port
- Destination port
### Linux host-based firewalls

| Firewall Type                | Description                                                            | Notes                                                                                                     |
| ---------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| IPtables                     | Implemented in the Linux kernel, typically works at the network layer. | Modified using the iptables command.                                                                      |
| Uncomplicated firewall (UFW) | A simplified front end for IPtables.                                   |                                                                                                           |
| TCPwrappers                  | Implemented in the Linux user space, works at the application layer.   | Used to permit or deny access to a specific service. Can only be used with Xinetd-based network services. |
# [[Host-Based Antivirus]]


HIPS combines the capabilities of antivirus, antispyware, and personal firewall software.

Host-Based Intrusion Prevention Systems can be Any combination of these:

| IPS Type                | How it Works                                   | Strengths                                        | Weaknesses                                                         |
| ----------------------- | ---------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------ |
| **Signature-Based IPS** | Compare traffic to signatures                  | Signatures detect attacks & vulnerabilities      | Must update signatures<br><br>Need signatures for new threats      |
| **Anomaly-Based IPS**   | Relies on a base-line<br><br>Evaluates traffic | Uncharacteristic traffic patterns trigger alerts |                                                                    |
| **Policy-Based IPS**    | Policies are strictly followed                 | Policy defined what traffic is acceptable        | Policies can be modified<br><br>Policy violations will send alerts |
# Host-Based Malware Protection
Commercial products for malware detection can realistically achieve about ==40 percent success== in detection. AMP = Advanced Malware Protection

#### Cisco AMP for Endpoints

| Feature                     | Description                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------- |
| Malware Detection           | Cloud-based detection using Cisco Talos Threat Intelligence Cloud                     |
| Threat Intelligence         | Uses SHA-256 hashes for rapid detection of known malware                              |
| Unknown File Analysis       | Utilizes cloud resources to test files with uncertain dispositions                    |
| Machine Learning            | Continuously updates to stay current with evolving threats                            |
| Historical Perspective      | Tracks file and device trajectories to aid in infection tracing                       |
| Network Connection Blocking | Blocks malicious connections based on security intelligence feeds and custom IP lists |
| Retrospective Alerting      | Identifies previously unknown files as malicious and quarantines them                 |
| Custom Detections           | Supports simple and advanced custom detections, including custom signature creation   |
| Host Grouping               | Allows creation of host groups with tailored detection policies                       |
| Reporting                   | Provides comprehensive reporting tools                                                |
Cisco AMP for Endpoints consists of the following elements:

| Component                             | Description                                                                                                        |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Cisco Talos Threat Intelligence Cloud | Provides real-time threat intelligence and houses Cisco malware detection and analytic engines.                    |
| Client Connectors                     | Endpoint components that communicate with the cloud to send file information and receive disposition instructions. |
| Cisco AMP for Networks                | Enables Firepower devices to query the cloud for file disposition information.                                     |

## [Cisco Talos Threat Intelligence Cloud](https://www.talosintelligence.com/docs/Talos_WhitePaper.pdf)

| Feature                         | Description                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------- |
| **Detection publishing**        | Signatures are in the cloud, reducing client connector size and processing load. |
| - Custom signatures             | Administrators can create and push custom signatures to endpoints.               |
| - Cross-referencing             | Cloud-based cross-referencing of files and signatures ensures self-updating.     |
| **Large-scale data processing** | Cloud processes data from various sources, including file samples.               |
| - Malicious file handling       | Malicious file samples are stored and reported to endpoints.                     |
| - Performance                   | Designed for low latency to provide quick results.                               |
| - Analytics                     | Advanced analytic engines correlate incoming data to update signatures.          |
| - Machine learning              | Machine-learning engines refine signatures and reevaluate detections.            |
| **Real-time decision making**   | The cloud evolves based on incoming data.                                        |
| **Reporting**                   | Robust reporting capabilities are provided.                                      |

## Next-Generation Endpoint Security
>A Next-Generation Endpoint Security Solution Like Cisco AMP Combines EPP with EDR

### EPP
Endpoint protection platform provides integrated endpoint security with personal firewall, port and device control, and anti-malware capabilities. EPP is often described as a traditional antivirus solution that scans files for malicious threats in a threat intelligence database.
- Cannot protect against signatureless and fileless malware threats. 

Effective EPP Lacks:
- **Machine learning** 
- **Threat intelligence** 
- **Sandboxing**

>EPP focuses solely on prevention and should be paired with an EDR solution.
### EDR
Endpoint detection and response solutions detect threats across a network environment, investigating the entire threat lifecycle to provide insights into its origin, behavior, and prevention strategies.
![2](/Course-Notes/.assets/Screenshot_2024-11-11_at_18.44.08.png)
EDR Features:
- **Detection**
- **Containment**
- **Investigation**
- **Elimination**

### Compair

| Feature             | Endpoint Protection Platform (EPP)                                             | Endpoint Detection and Response (EDR)                                      |
| ------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Focus               | Prevention                                                                     | Detection and Response                                                     |
| Threats Covered     | Known Malware                                                                  | Advanced and Persistent Threats                                            |
| Key Capabilities    | Integrated Endpoint Security (Firewall, Port and Device Control, Anti-malware) | Continuous Monitoring, Rapid Time to Detection, Architectural Integrations |
| Threat Intelligence | Limited                                                                        | Expansive                                                                  |
| Machine Learning    | Limited                                                                        | Advanced                                                                   |
| Sandboxing          | Limited                                                                        | Critical                                                                   |
| Detection           | File-based                                                                     | Continuous File Analysis                                                   |
| Containment         | Limited                                                                        | Critical                                                                   |
| Investigation       | Limited                                                                        | Critical (Sandboxing)                                                      |
| Elimination         | Limited                                                                        | Actionable Data, Automatic Remediation                                     |
| Scope               | Endpoint                                                                       | Network                                                                    |
### Cisco AMP for Endpoints

Cisco AMP for Endpoints provides next-generation capabilities by ==combining EPP with EDR== to prevent attacks and quickly detect and respond to ==advanced malware==. 

# [[Sandboxing]]

| Technology                | Description                                                                            | Benefits                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Sandboxing                | Emulates an environment to detonate files and analyze behavior.                        | Detects malicious files by observing their actions in a safe environment. |
| Packers                   | Change the outer appearance of a threat, but its underlying behavior remains the same. | Sandboxes can detect threats that have been packed.                       |
| Signature-based detection | Identifies files based on known patterns or signatures.                                | Sandboxes provide a more comprehensive view of file behavior.             |
#### Limitations

| Deficiency                         | Description                                                                                                                                                                  |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inherent efficacy                  | Running a file in a sandbox is no guarantee that the disposition will show the threat that it poses to your environment.                                                     |
| Evasion tactics                    | Malware authors deploy several techniques to bypass sandbox analysis.                                                                                                        |
| Means to an end, not an end itself | Sandboxing is a great tool for addressing malware in an environment, but sandboxing needs to be coupled with other capabilities to provide comprehensive malware protection. |
### Cisco ThreatGrid solution
(Cloud, Prem, or App)
Sandboxing analysis results
Behaviours and generated outbound HTTP traffic. Including the exact URI path
![1](/Course-Notes/.assets/Screenshot_2024-11-11_at_19.04.57.png)
# File Integrity Checking
### Cisco ASA

| Command              | Description                           |
| -------------------- | ------------------------------------- |
| verify \<image-name> | Used to validate the Cisco ASA image. |
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

# [[Recap]]

**Endpoint Security Technologies:**

1. **Host-based Personal Firewall**: Controls incoming and outgoing network traffic for a host, useful for blocking unwanted connections.

2. **Host-based Antivirus**: Detects and removes viruses and other malware from the system.

3. **Endpoint Malware Protection**: Provides real-time protection against malware, including detection, prevention, and removal of malicious files.

4. **Application Allowed Lists**: Only allows specified applications to run on the host; all others are blocked (whitelisting).

5. **File Sandboxing**: Isolates potentially malicious files to analyze their behavior in a safe environment.

6. **File Integrity Checks**: Monitors critical system files for unauthorized changes, providing tamper detection.

| Endpoint Security Technologies | Description                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Host-based Personal Firewall   | Controls incoming and outgoing network traffic for a host, useful for blocking unwanted connections.            |
| Host-based Antivirus           | Detects and removes viruses and other malware from the system.                                                  |
| Endpoint Malware Protection    | Provides real-time protection against malware, including detection, prevention, and removal of malicious files. |
| Application Allowed Lists      | Only allows specified applications to run on the host; all others are blocked (whitelisting).                   |
| File Sandboxing                | Isolates potentially malicious files to analyze their behavior in a safe environment.                           |
| File Integrity Checks          | Monitors critical system files for unauthorized changes, providing tamper detection.                            |


**File Analysis & Malware Protection:**

• **AMP for Endpoints**: Submits unknown files to the cloud for analysis and uses advanced malware protection to detect and block threats in real time.

• **Malware from Browsing**: To prevent malware infections from malicious websites, **endpoint malware protection** is most effective.

• **HIPS vs. NIPS**: HIPS is installed on the endpoint and can detect and block threats locally, while NIPS operates at the network level, monitoring traffic.

|                    |                                                           |                                                  |
| ------------------ | --------------------------------------------------------- | ------------------------------------------------ |
| Feature            | AMP for Endpoints                                         | Traditional Endpoint Malware Protection          |
| Threat Detection   | Submits unknown files to the cloud for analysis           | Relies on signature-based detection              |
| Threat Blocking    | Blocks threats in real time                               | May require manual intervention to block threats |
| Malware Prevention | Effective against malware from browsing and other sources | Most effective against malware from browsing     |
| Architecture       | Cloud-based with local endpoint protection                | Local endpoint protection only                   |
| Threat Visibility  | Provides insights into file reputation and threat trends  | Limited visibility into threat trends            |


**Logs & Incident Response:**

• **MySQL Logs**: /var/log/mysql/mysql-slow.log records slow queries that can be indicative of potential attacks or system abuse.

• **Device Trajectory**: AMP tracks the sequence of actions performed on a compromised host, useful in investigating malicious activity.

• **Quarantining Malicious Files**: After detecting a malicious file, isolate it immediately to prevent further damage.

| Logs & Incident Response     | Description                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------- |
| MySQL Logs                   | /var/log/mysql/mysql-slow.log records slow queries that can be indicative of potential attacks or system abuse. |
| Device Trajectory            | AMP tracks the sequence of actions performed on a compromised host, useful in investigating malicious activity. |
| Quarantining Malicious Files | After detecting a malicious file, isolate it immediately to prevent further damage.                             |


**System Configuration & Networking:**

• **/etc/hosts vs /etc/nsswitch.conf**: /etc/nsswitch.conf controls the order of name resolution methods, determining if the system looks in /etc/hosts first or queries DNS servers.

• **SCP Command**: Use scp evidence user@192.168.1.33:evidence to copy a file to a remote Linux host.

| Topic                            | Description                                                                                                    |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| /etc/hosts vs /etc/nsswitch.conf | nsswitch.conf controls the order of name resolution methods.                                                   |
| SCP Command                      | Use scp evidence [user@192.168.1.33](mailto:user@192.168.1.33):evidence to copy a file to a remote Linux host. |


**Security Controls:**

• **Permissive Security Control**: Application allowed lists allow only specified applications to run on a system, blocking others.

• **HIPS**: Can protect a mobile host on an unsecured network, while NIPS monitors network traffic.

| Security Controls                                      | Description                                                            |
| ------------------------------------------------------ | ---------------------------------------------------------------------- |
| Permissive Security Control: Application allowed lists | Allow only specified applications to run on a system, blocking others. |
| HIPS                                                   | Protects a mobile host on an unsecured network.                        |
| NIPS                                                   | Monitors network traffic.                                              |
  

**Best Practices:**

• **Detecting Malicious Files**: After detecting a malicious file, submit it for analysis, quarantine it, and track any related behaviors across other systems.

• **Preventing Infections**: Use **endpoint malware protection** to prevent malware from websites and other attack vectors.

| Best Practices            | Description                                                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Detecting Malicious Files | After detecting a malicious file, submit it for analysis, quarantine it, and track any related behaviors across other systems. |
| Preventing Infections     | Use endpoint malware protection to prevent malware from websites and other attack vectors.                                     |
