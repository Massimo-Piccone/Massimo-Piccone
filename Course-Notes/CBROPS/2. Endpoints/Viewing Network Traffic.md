## Tcpdump Basics

`sudo tcpdump <options> <filters>`
`sudo tcpdump –i ens33 –Xnns 0 host 192.168.222.1`

- -i: Specifies the listening interface. If omitted, tcpdump selects the first available interface. If there’s an inline device with bridged interfaces, list them as ens32:ens33.
- -X: Outputs payload in both hex and ASCII.
- -nn: Outputs host addresses and ports in numeric format.
- -s: Snap length. Refers to the number of bytes to include in the capture or output. Defaults to a local environment-based value, sometimes as small as 64 bytes. Entering 0 includes all payload bytes.
- host 192.168.222.1: Filters packets to or from the specified host.
### Output:

```
ed@ubuntu:/usr/lib/systemd$ sudo tcpdump -i ens33 -Xnns 0 host 192.168.222.1 

tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on ens33, link-type EN10MB (Ethernet), capture size 262144 bytes

14:15:43.238436 IP 192.168.222.135.40678 > 192.168.222.1.21: Flags [S], seq 1428615420, win 29200, options [mss 1460,sackOK,TS val 53618902 ecr 0,nop,wscale 7], length 0
    0x0000:  4500 003c d82a 4000 4006 24b7 c0a8 de87  E..<.*@.@.$.....
    0x0010:  c0a8 de01 9ee6 0015 5526 f0fc 0000 0000  ........U&......
    0x0020:  a002 7210 3e09 0000 0204 05b4 0402 080a  ..r.>...........
    0x0030:  0332 28d6 0000 0000 0103 0307            .2(.........

14:15:43.238772 IP 192.168.222.1.21 > 192.168.222.135.40678: Flags [S.], seq 2389988806, ack 1428615421, win 65535, options [mss 1460,nop,wscale 5,nop,nop,TS val 1399261396 ecr 53618902,sackOK,eol], length 0
    0x0000:  4500 0040 9d88 4000 4006 5f55 c0a8 de01  E..@..@.@._U....
    0x0010:  c0a8 de87 0015 9ee6 8e74 55c6 5526 f0fd  .........tU.U&..
    0x0020:  b012 ffff a774 0000 0204 05b4 0103 0305  .....t..........
    0x0030:  0101 080a 5367 08d4 0332 28d6 0402 0000  ....Sg...2(.....

14:15:43.238860 IP 192.168.222.135.40678 > 192.168.222.1.21: Flags [.], ack 1, win 229, options [nop,nop,TS val 53618902 ecr 1399261396], length 0
    0x0000:  4500 0034 d82b 4000 4006 24be c0a8 de87  E..4.+@.@.$.....
    0x0010:  c0a8 de01 9ee6 0015 5526 f0fd 8e74 55c7  ........U&...tU.
    0x0020:  8010 00e5 3e01 0000 0101 080a 0332 28d6  ....>........2(.
    0x0030:  5367 08d4
```

## Refine

Further refine your filter by adding a port constraint as follows:
- `and [condition]` — add 
- `and not [condition]` — **negation** 
- `> dump.txt` to output into a file 
- `-r` read pcapfile
- `–X` to output in both hex and ASCII
- `-nn` for numeric IP addresses and port numbers
- `–s 0` for displaying the entire payload
