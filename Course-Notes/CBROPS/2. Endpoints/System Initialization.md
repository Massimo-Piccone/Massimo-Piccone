The Linux boot process:
1. Hardware checks
2. Device bus discovery
3. Device discovery
4. Kernel subsystem initializes
5. Root file system mounts
6. Start user processes

Boot parameters that are processed by the bootloader are called **/proc/cmdline**. An example of its contents follows:

```
BOOT_IMAGE=/boot/vmlinuz-4.4.0-22-generic root=UUID=339228c9-cbc3-4503-950f-40415e03779f ro quiet splash
```

## How Linux Controls the Boot Process

- **System V init:** The traditional init process, which is called init, reads and executes a series of scripts that are located in a startup directory. Each script starts a process or service one at a time until all the scripts in the directory have been executed.

- **Systemd:** The newer initialization system initializes services and processes in parallel and can support on-demand services.

## Run Levels

Linux systems use run levels from 0 to 6 to manage processes, with 0 halting the system and 6 rebooting it. Run levels 1-2 are for emergency repairs, while 3 and 5 are default run levels for starting the system with or without a graphical interface.

## Common Boot Management Processes

Two boot management systems are commonly used in Linux: System V init and systemd:

- If the system contains the directory **/etc/systemd**, then it is using the systemd method.

- If the system contains the file **/etc/inittab**, then it is using the System V init method

Traditional System V Bootup

System V boot, or SysVinit, is the traditional method for initializing user-space processes and services. It starts a process called init, which controls starting the remaining user processes. init runs until the system is rebooted or shut down. It consults /etc/inittab to get instructions for starting up, including the run level it should start in. Once the run level is determined, it executes start and stop scripts in that run level’s directory.


/proc/cmdline - can be referenced to show the boot parameters
