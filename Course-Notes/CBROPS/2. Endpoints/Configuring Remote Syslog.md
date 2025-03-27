To send all events to the remote server over UDP, you can add the following rule:

`*.* @<remote host name or IP address>:<port>`

For TCP, use two at symbols (`@@`) rather than one.

`*.* @@<remote host name or IP address>:<port>`

Another option is to selectively send alerts by specifying a facility and severity. In the example, any facility with a severity of **emerg** will be forwarded to the host 192.168.222.1 over UDP port 10514.

`*.emerg @<192.168.222.1>:<10514>`

Note:
If you don’t specify a port, the default UDP or TCP 514 would be used. Also, any logging configuration changes require a restart logging service to read the changes.

## Testing Your Logging Configuration

For example, your configuration file contains the following rule:

`auth,authpriv.*   /var/log/auth.log`

This rule sends alerts from the **auth** or **authpriv** facilities with any severity to the **/var/log/auth.log** file. To test, use the following command:

`logger –p auth.info “My auth.info logging test”`

After you execute the command, you open the **/var/log/auth.log** file and navigate to the end of the file to see the following entry if the rule worked correctly:

`[date/time][usr]: My auth.info logging test`

You can also use the `logger` command to send messages to remote syslog servers. The following example adds the `–n` parameter, which lets you specify a remote host, the `–P` (upper case) parameter to specify the port number and you can add `--UDP` to send as a UDP connection or `--TCP` to send it over TCP. If you do not specify a protocol, it will first try UDP and if that fails it will try TCP. Also, if you do not specify a port, it will use the default port 514.

`logger –p auth.info –n 192.168.222.1 –P 10514 --UDP “My auth.info logging test”`
