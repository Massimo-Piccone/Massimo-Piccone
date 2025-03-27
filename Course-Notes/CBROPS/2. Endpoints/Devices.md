Devices can be classified in one of the following categories:

- **Block:** Devices that process data in fixed chunks, for example, disk drives or other forms of storage devices.
    
- **Character:** Devices that work with data streams. One such device is **/dev/null**. Directly connected printers are another example.
    
- **Pipe:** Sometimes referred to as “named pipes.” These devices operate in a manner similar to character devices. However, the data stream is directed to another process rather than a device file or driver.
    
- **Sockets:** These devices are unique in that they are not usually found in the **/dev** directory. They are used for interprocess communication such as network communication.


You can tell a device’s type by listing the files in the **/dev** directory with file details. The following command lists files in a directory


### Permissions
#### Symbolic Permissions
![1](/Course-Notes/.assets/Pasted_image_20241220152657.png)
#### Symbolic permissions 

| Access Class | Operator             | Access Type |
| ------------ | -------------------- | ----------- |
| u (user)     | + (add access)       | r (read)    |
| g (group)    | - (remove access)    | w (write)   |
| o (other)    | = (set exact access) | x (execute) |
| a (All)      | user, group, other   | rwx         |
## Disk and File Systems
inside /dev (Devices)

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

- ext2, ext3, and ext4: Native Linux file systems, ext4 is the latest. Linux maintains backward compatibility.

- NTFS: Used by modern Windows, it supports versatile permissions, large disks, and advanced features.

- FAT16, FAT32, exFAT: Native to older Windows, it’s mostly replaced by NTFS but remains common on USB storage devices. Linux is compatible but lacks permissions and large disk support.

- ISO 9660 and JOLIET: Optical media file system standards.

- HFS+: Apple’s file system for X. Linux has drivers for read/write compatibility.

- Swap: A special file system used in Linux swap partitions. It’s disk space reserved for the system to use when it needs to free memory. RAM is faster than disk drives, so ideally, everything should run in RAM. However, if the system runs low on RAM, it can move data to the swap partition. Swap space isn’t a file system; it’s directly addressable disk space for temporarily dumping content from RAM. When main memory is oversubscribed, system performance degrades because data moves more frequently between RAM and the swap disk.

### Mounting Devices

To manually mount a device, use the `mount` command. The basic syntax is as follows:
`mount -t <_type_> <_device name_> <_mount point_>`

Understanding disk management involves determining how they connect to the file system and what’s mounted. Linux attempts to mount disks on boot and references /etc/fstab for mount configuration. You can override configuration parameters in /etc/fstab with the –o option.

Newer /etc/fstab implementations list devices by their universally unique identifier (UUID) numbers instead of device names for better device identification. The following example shows an entry in /etc/fstab.

```
# / was on /dev/sda1 during installation
UUID=339228c9-cbc3-4503-950f-40415e03779f / ext4 errors=remount-ro 0 1
```

- UUID of the device: The comment above it refers to the device file. In the example, it’s /dev/sda1. When the filesystem is created, the UUID is generated and stored on the device. Names like /dev/sda may change, but the UUID helps Linux track the device.

- Mount point: The mount point indicates where the root of the file system is located. In the example, it’s root (/).

- File system type: The example lists it as ext4.

- Options: The options specify operating parameters. In the example, it indicates what to do if the device encounters errors. If errors occur, Linux will remount the device in read-only mode.

- Dump frequency: This column is deprecated and no longer relevant in modern Linux environments.

- Pass number: The final column configures the order devices should be mounted. The root file system is marked with a one, indicating it’s the first partition to be loaded. Other file systems are configured with a two, indicating they can be mounted after the root filesystem.