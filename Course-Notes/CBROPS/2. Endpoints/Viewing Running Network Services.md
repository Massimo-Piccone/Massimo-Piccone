#### netstat 
>list running services 
- To get the most information from netstat, run it with root privileges.
- netstat –a46: Shows IPv4 and IPv6 connection information.
- netstat –lt: Shows TCP connections in the listen state.
- netstat –lun: Shows UDP connections in the listen state.
- sudo netstat –atnp: Shows TCP connections in any state, with host and port information in numeric format, and the program name and PID of the listening process.

#### lsof Command
>LSOF stands for "list open files."
- sudo lsof –i: List files associated with an internet address.
- sudo lsof –i tcp: List files associated with an internet address using TCP.
- sudo lsof –i tcp:80: List files associated with an internet address using TCP port 80.
- sudo lsof –i udp:53 -P: List files associated with an internet address using UDP port 53.
- sudo lsof –i @192.168.222.1: List files associated with the specified internet address.
- sudo lsof –i @192.168.222.1:21 -P: List files associated with the specified internet address and port.
