Linux systems experiencing issues may require a safe configuration or external boot for a clean environment.
![3](/Course-Notes/.assets/Screenshot_2024-11-10_at_13.05.43.png)

The steps for entering single user mode are as follows:

1. First, as you boot your system, you will typically see the BIOS screen as the BIOS performs its power-on self-test and identifies the peripheral devices that are attached to the host at boot time.
2. When the BIOS splash screen turns off, press the left shift key which will force the system to display the **GRUB** menu.
3. In the GRUB menu, use the up/down arrow keys to highlight **Advanced Options** and press **Enter** 
4. A list of the kernels that are available to boot will be displayed. Normally, the newest kernel which will be located at the top of the list. Use the arrow keys to highlight the kernel to boot with the string **(recovery mode)** after it.
5. With the selection highlighted, press the **Enter** key to get to the recovery mode menu.
6. The recovery mode screen gives you access to several tools you might find useful in an emergency situation. Of them, **root** brings you to a single user mode command prompt. 
7. From here, press **Enter** as prompted to execute commands for navigating the file system, or to investigate files on the host without disturbing it. The file system is mounted as read-only so you can’t alter much of it in this state. However, you can remount the file system in read/write mode if you need to make edits. Once you complete your single user mode session, you can type **reboot** at the prompt to restart the system. The system should restart normally at this point.

## Live Boot

![2](/Course-Notes/.assets/Screenshot_2024-11-10_at_13.07.59.png)

## Shutting Down the System
![1](/Course-Notes/.assets/Screenshot_2024-11-10_at_13.09.17.png)
- **hh:mm:** The hour in 24-hour format followed by the number of minutes.
- **+m:** The number of minutes from the time the command was issued. 
- **now:** The time parameter will also accept the keyword “now” to indicate that the command will execute immediately.
