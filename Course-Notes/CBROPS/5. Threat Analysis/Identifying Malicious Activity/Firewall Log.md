
- System Log Importance: Provide insight into and context for security events.
- Firewall Log Analysis: Understand communication relationships, timing, and attacker’s motives/tools.
- ACL-Denied Logs: May indicate potential unauthorized attempts to access the network.

- Potential Security Threat: Footprinting or port scanning attempt from the 209.165.200.233 outside host to the hosts in the dmz.
- Impact on IPS: IPS placed behind the firewall will not be able to detect the port scanning traffic.
- Firewall Log Message: Log messages from the Cisco ASA syslog show the 209.165.200.233 outside host attempting to connect to different dmz hosts over different ports and being denied by the “outside_access_in” ACL.

```
Aug 13 2019 11:00:11: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(23000) -> dmz/192.168.1.1(22) hit-cnt 1 ......
Aug 13 2019 11:00:12: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(23001) -> dmz/192.168.1.1(23) hit-cnt 1 ......
Aug 13 2019 11:00:13: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(23002) -> dmz/192.168.1.1(53) hit-cnt 1 ......
Aug 13 2019 11:00:14: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(23003) -> dmz/192.168.1.1(80) hit-cnt 1 ......

<etc>

Aug 13 2019 11:02:51: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(24000) -> dmz/192.168.1.2(22) hit-cnt 1 ......
Aug 13 2019 11:02:52: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(24001) -> dmz/192.168.1.2(23) hit-cnt 1 ......
Aug 13 2019 11:02:53: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(24002) -> dmz/192.168.1.2(53) hit-cnt 1 ......
Aug 13 2019 11:02:54: %ASA-4-106100: access-list outside_access_in denied tcp outside/209.165.200.233(24003) -> dmz/192.168.1.2(80) hit-cnt 1 ......

<etc>
```

- Firewall Log Messages: Track NATs and connection events.
- Connection Event Example: 209.165.200.236 initiated a TCP connection to 10.1.1.1 port 80.
- Cisco ASA Appliance Syslog: Example of tracking connection events.

```
Aug 14 2019 12:38:51 %ASA-6-302013: Built inbound TCP connection 855 for outside:209.165.200.236/1107 (209.165.200.236/1107) to dmz:10.1.1.1/80 (10.1.1.1/80)
```

- Source IP Translation: Cisco ASA appliance translates the 172.16.1.1 inside host private source IP address to the public IP address of 198.51.100.1 on the outside interface.
- Device: Cisco ASA appliance.
- Translation Type: Dynamic translation.

```
%ASA-6-305009: Built dynamic translation from inside:172.16.1.1 to outside:198.51.100.1
```

- Initial Log Message Focus: A small subset of log messages will provide the most benefit initially.
- Log Message Severity: The severity level of a log message is indicated by a number, such as 3 for the %ASA-3-106014 log.
- Expanding Analysis: After examining the initial log messages, administrators can expand their analysis to include additional details.

| **Syslog Mnemonic** | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `%ASA-3-106014`     | Deny inbound ICMP from `src interface_name: IP_address` to `dst interface_name: IP_address` (type `dec`, code `dec`) - The ASA denied an inbound ICMP packet.                                                                                                                                                                                                                                                                                                                                                         |
| `%ASA-6-106015`     | `Deny TCP (no connection) from IP_address/port to IP_address/port flags tcp_flags on interface interface_name` The ASA discarded a TCP packet that has no associated connection in the ASA connection table. The ASA looks for a SYN flag in the packet, which indicates a request to establish a new connection. If the SYN flag is not set, and there is no existing connection, the ASA discards the packet                                                                                                        |
| `%ASA-1-106021`     | `Deny protocol reverse path check from source_address to dest_address on interface interface_name` Someone is attempting to spoof an IP address on an inbound connection. Unicast RPF, also known as reverse route lookup, detected a packet that does not have a source address that is represented by a route in the ASA routing table                                                                                                                                                                              |
| `%ASA-6-302014`     | `Teardown TCP connection id for interface : real-address / real-port [(``idfw_user``)] to interface : real-address` / `real-port` [`(``idfw_user``)] duration` `hh``:``mm``:``ss` `bytes bytes [` `reason` `] [(` `user` `)]` A TCP connection between two hosts was deleted.<br><br>Reasons for the deleted connection:<br>- **Conn-timeout:** The connection ended when a flow is closed because of the expiration of its inactivity timer.<br>- **Deny terminate:** Flow was terminated by application inspection. |
| `%ASA-6-302016`     | `Teardown UDP connection number for interface : real-address / real-port [(``idfw_user``)] to interface : real-address / real-port [(``idfw_user``)] duration` `hh``:``mm``:``ss` `bytes bytes [(``user``)]` A UDP connection between two hosts was deleted.                                                                                                                                                                                                                                                          |
| `%ASA-6-302021`     | `Teardown ICMP connection for faddr { faddr \| icmp_seq_num} [(``idfw_user``)] gaddr { gaddr \| cmp_type } laddr laddr [(``idfw_user``)]` An ICMP session is removed in the fast-path when stateful ICMP is enabled using the `inspect icmp` command.                                                                                                                                                                                                                                                                 |

