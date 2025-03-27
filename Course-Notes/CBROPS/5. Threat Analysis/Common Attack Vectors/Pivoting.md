- ==Definition==: A method used by attackers to bypass network restrictions and attack other computers.
- ==Purpose==: To exploit computers on inaccessible networks by using a compromised computer as a proxy.
- ==How Pivoting Works==: Utilizes an existing session on a dual-homed computer to act as a bridge between networks.

The attack box (192.168.81.125) lacks direct access to the 192.168.63.0/24 network. However, the web server can access both networks. Compromising the web server allows the attack computer to access the 192.168.63.0/24 network via pivoting.

![1](/Course-Notes/.assets/Pasted_image_20241120113933.png)