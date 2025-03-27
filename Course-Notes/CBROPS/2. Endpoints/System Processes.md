Processes, identified by PIDs, are managed by the system to ensure resource allocation. New processes are created in Linux using the fork-and-exec mechanism, where a parent process duplicates itself and can replace itself with a new program.

## Displaying Processes and Process Threads

The **top** application screen is divided into two sections. The upper portion lists general information regarding system resource utilization as follows: 

- The first row lists system up time and system load average. The load average is represented as three decimal numbers which, from left to right, show the load on the CPU over the last 1, 5, and 15 minutes. 
- The second row gives you general information about the processes running on the host. 
- The third row lists various aspects of how the CPU is being utilized. In a multi-CPU system, you will see one row per CPU. Some of the statistics you may find useful at a glance include the following:
    - **us:** user space processes 
    - **sy:** system/kernel processes
    - **id:** system idle time
- The remaining rows provide information on how memory and swap space is being utilized. The first of the two rows shows system memory utilization and the second is for swap utilization.

The columns of information that is displayed by **top** are as follows:
- **PID:** Process ID number. When a process is started, it is given a unique PID that identifies that process to the system. If you ever need to kill a process, you can refer to the process by its PID.
- **User:** The user name of the process’s owner
- **PR:** The scheduling priority of the process
- **NI:** The process’s **nice** value.
	Nice in Linux sets process priority, with negative values indicating higher priority. Superusers can adjust nice values to prevent resource-intensive processes from slowing down the system.
- **VIRT:** Virtual memory
- **RES:** Resident, non-swapped physical memory
- **SHR:** Shared memory
- **S:** Process status
    1. **D:** Uninterruptible sleep (stuck waiting for input or output)
    2. **R:** Running (executing normally)        
    3. **S:** Sleeping (waiting internally)
    4. **T:** Stopped by job control (stopped with a signal from the kernel)
    5. **t:** Stopped by debugger (another process has full control)
    6. **Z:** Zombie (completed processes that are not yet removed from the kernel's process table)
- **%CPU:** The estimated percentage of CPU resources being consumed by the process
- **%MEM:** The percentage of physical memory being consumed by the process
- **TIME+/–:** The total CPU time the process has consumed since it started
- **COMMAND:** The name of the process

## The ps Command
Extract specific information about processes.
- **UNIX:** Options can be grouped and must be preceded by a dash.
- **BSD:** Options can be grouped and must not be preceded by a dash.
- **GNU:** Long form where options are preceded by double dashes.

-e — all users
-f — full (UID, PPID, C:, STIME)
aux — displays an overview of all the processes that are running
-C — Specify processes related to Damon
-o — specify information that you want about a process

## Displaying Open Files
lsof

```
ed@carl:~$ sudo lsof /var/log/syslog
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
rsyslogd 651 syslog    5w   REG    8,1   161355 4063351 /var/log/syslog
```

Some of the key features of this output include the following:

- **Command:** The name of the process using the file.
- **PID:** The process ID of the command using the file.
- **User:** The user running the process.
- **FD:** File descriptor: a reference number that is used by the kernel to identify an open file. File descriptors may be followed by a code letter to further describe the state of the file. In the example, the letter “w” indicates that the process has a write block on a portion of the file.
- **Type:** Identifies the type of file. For example, DIR represents a directory, inet is a network connection or BLK to represent a block device such as a disk drive. The example lists the type as REG which represents a regular file.
- **Device:** Device number that represents the device being called to perform the I/O.
- **Size/Off:** The file size or memory offset. The `lsof` command will display whichever one is appropriate for the file being listed.
- **Node:** The file’s INODE number, which is used to uniquely identify the file on the file system.
- **Name:** The path and filename

To list the processes that are accessing log files in a directory, use the +D option:

```
ed@carl:~$ sudo lsof +D /var/log
COMMAND    PID   USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
rsyslogd   651 syslog    5w   REG    8,1   161355 4063351 /var/log/syslog
rsyslogd   651 syslog    6w   REG    8,1   277134 4063734 /var/log/kern.log
rsyslogd   651 syslog    7w   REG    8,1    29819 4076255 /var/log/auth.log
Xorg       911   root    0w   REG    8,1    34655 40632
```

- Find the files that a particular process has opened, you can use the `–p` option
- Uses the “-i” option to filter output by network characteristics (e.g., TCP-based services).
- The “-s” option allows specifying a protocol and state (separated by a colon) to filter output.
## Monitoring CPU and Memory Utilization

top -p [PID]

```
ed@carl:~$ top -p 892
top - 09:26:27 up 6 days, 23:43,  2 users,  load average: 0.03, 0.07, 0.05
Tasks:   1 total,   0 running,   1 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.6 us,  0.2 sy,  0.0 ni, 97.3 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  8175228 total,  6910576 free,   208780 used,  1055872 buff/cache
KiB Swap:  8386556 total,  8386556 free,        0 used.  7844280 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
  892 root      20   0   65612   6176   5468 S   0.0  0.1   0:00.15 sshd
```

vmstat — top with refresh time parameter 

The categories are as follows:

- **procs:** Lists the number of processes in either a runnable state (r) or in uninterruptible sleep (b).
- **memory**
    1. **swpd:** Virtual memory used
    2. **free:** Available memory
    3. **buff:** The amount of memory that the kernel is using for buffering
    4. **cache:** The amount of memory that is reserved as cache
- **swap** 
    1. **si:** Swapped in 
    2. **so:** Swapped out
- **io**
    1. **bi:** Blocks that are received from block device
    2. **bo:** Blocks that are sent to block device
- **system**
    1. **in:** Number of interrupts
    2. **cs:** Number of context switches
- **cpu**
    - **us:** CPU time spent processing non-kernel (user) processes
    - **sy:** CPU time spent processing kernel processes
    - **id:** CPU idle time
    - **wa:** Time spent waiting for I/O
    - **st:** Time that is stolen from virtual machine

## Monitoring I/O

A good tool to give you an idea of the amount of I/O taking place on a system is the `iostat` command. Get a snapshot of current I/O activity. You can use it with a time delay parameter in seconds.

```
ed@carl:~$ iostat 2

Linux 4.4.0-22-generic (carl) 06/11/2016 _x86_64_(4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
			1.88    0.00    0.22    0.00    0.00   97.90

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.18         1.14         4.89     691475    2978716
```

# Other Useful Command-Line Tools

```
u@test:~$ history | less (grep maybe?)
	732  [command]
# You can recall this command using its number
u@test:~$ !732
	[command outupt]
u@test:~$ !! 
	[previous command]
```

## The awk command

**awk** is a powerful text processing tool that ships with the Linux operating system. It is actually a text processing language unto itself. It can be utilized in several ways, such as **awk** can take its input from files, STDIN, or even devices. The basic workflow is as follows:

1. Read a line of input. Lines are typically terminated with newline characters. When **awk**encounters a newline character, that signals the end of the line.
2. Execute commands on the line.
3. Move on to the next line if it has not reached the end of the file.

## The sed Command
The `sed` command is a stream editing tool that performs the action you configure on lines of text that are read in from files or STDIN. Lines are determined when `sed` encounters a newline character. One of the most common uses of `sed` is to perform string substitutions. The general syntax of the `sed` command is as follows:

`sed –e ‘s/<input pattern>/<output pattern/<options>’`

The following example illustrates how to implement `sed` for simple text substitution:

```
ed@carl:~$ echo "left" | sed -e 's/left/right/'
right
```

## The vi Command
- Vi Command Usage: Open a file in vi by entering the vi command followed by the file name.
- Vi Availability: Vi is present in virtually every UNIX and Linux-based system.
- Vi Purpose: Vi is a full-screen visual interface for editing text files, especially useful for remote administration tasks.

- Application Modes: vi operates in two modes: command mode for issuing commands and insert mode for text entry and editing.
- Insert Mode: Accessed from command mode by pressing “i”, indicated by “Insert” in the status area, and exited by pressing “Esc”.
- Saving Edits: In command mode, press “:” to display a colon, then “w” followed by Enter to save the edits.

- Quitting the Application: Press colon (:), then q (quit), then exclamation point (!), to override the warning message and exit without saving.
- Saving Edits: Enter :, then w (write), then q (quit) to save and exit.
- Deleting Characters: Press x in command mode to delete the character under the cursor. Use dd to delete the entire line, dw to delete from the cursor to the end of the word, and yw to yank a word.

- Text Manipulation: Yanked or deleted text can be recovered, and text can be inserted or appended at specific locations.
- Navigation: Commands like “h”, “j”, “k”, “l”, “w”, “b”, “$”, “^”, “gg”, and “G” allow for moving the cursor within a file.
- Search and Replace: The “:” command, followed by `“/<search pattern>/<replacement text>/g”`, enables searching and replacing text in a file.

