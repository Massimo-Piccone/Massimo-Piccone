# Overview of Secure Shell Protocol

SSH is the preferred tool for remotely accessing Linux hosts due to its encrypted channel, mitigating security risks. SSH allows users to authenticate with login credentials or public/private key pairs, and can also be used to tunnel non-encrypted protocols over SSH.

```
scp <source> <user@host>: <remote dst>
```

# Networking


![1](/Course-Notes/.assets/Screenshot_2024-11-10_at_16.34.54.png)

### **netstat**

View network connections and stats Check active connections, routing tables, interface statistics, and protocol usage

**Purpose:** Displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

**Uses:**
	• **Active Connections:** List all active network connections and listening ports (netstat -tuln).
	• **Routing Tables:** View current routing tables (netstat -r).
	• **Interface Statistics:** Check statistics for each network interface, including errors and dropped packets (netstat -i).
	• **Network Protocols:** Monitor the usage and statistics of network protocols like TCP, UDP, and ICMP (netstat -s).  

```
ed@ned:~$ **netstat -rn**
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.7.1     0.0.0.0         UG        0 0          0 ens160
192.168.7.0     0.0.0.0         255.255.255.0   U         0 0          0 ens160
```

`–rn` options as shown displays the routing table with numeric IP addresses. If you prefer to see hostnames, you can remove the `n` option.

The IP address 0.0.0.0 with a netmask of 0.0.0.0 represents any IP address.
____
### **ifconfig**

**ifconfig** Configure network interfaces View or change IP, netmask, broadcast address; activate/deactivate interfaces (replaced by ip command)

**Purpose:** Configures and displays the status of network interfaces.

**Uses:**
	• **Interface Information:** View information such as IP address, MAC address, netmask, and broadcast address for each network interface.
	• **Activate/Deactivate Interfaces:** Bring network interfaces up or down (ifconfig eth0 up/down).
	• **Modify IP Configuration:** Change IP address, netmask, and other configuration settings for network interfaces.

**Note**: ifconfig is largely deprecated and replaced by ip in newer Linux distributions.  

**Typical Example:**

The `ifconfig` (or ip) command accepts many options, but with the syntax shown in the following example, a lot of information is retrieved about the interfaces.
- `–a` option instructs the system to output information on all the interfaces even if they are down
HWaddr = mac

##### Configuring Basic Properties (IP, Subnet Mask, Gateway)

```
ed@carl:~$ sudo ifconfig ens160 192.168.7.73 netmask 255.255.255.0 broadcast 192.168.7.255
```


____
### **route**

**route** Modify/view IP routing table View routing table, set default gateway, add/remove specific routes

**add gateway**
`ed@ned:~$ sudo route add default gw 192.168.7.1`

If you need to statically set a route to a network, you can set up the `route` command as follows:

```
ed@ned:~$ sudo route add -net 192.168.133.0 netmask 255.255.255.0 gw 192.168.7.200

ed@ned:~$ netstat -rn

Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.7.1     0.0.0.0         UG        0 0          0 ens160
192.168.7.0     0.0.0.0         255.255.255.0   U         0 0          0 ens160
192.168.133.0   192.168.7.200   255.255.255.0   UG        0 0          0 ens160
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

**Typical Example:**

route add default gw 192.168.1.1  _# Sets default gateway_

