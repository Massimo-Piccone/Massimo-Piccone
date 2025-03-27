- Logging Functionality: Linux systems offer comprehensive logging for system events and application events.
- Logging Process: Handled by syslogd or its variant rsyslogd, which provides additional functionality.

## Log File Locations and Log Files

- Log File Location: The primary log file is typically /var/log/messages or /var/log/syslog, but the configuration file determines which files are used.
- Logging Options: Logs can be sent to the console, forwarded to a remote syslog server, or aggregated to a central location for analysis.
- rsyslogd Configuration: The rsyslogd configuration file lists all the files used for logging and can be customized to match specific event types.

## Configuring Syslog

- Configuration File Location: /etc/syslog.conf or /etc/rsyslog.conf (or multiple files in rsyslogd).
- Configuration File Structure: Comments, sample configurations, notes, and rules defining event types and log destinations.
- Rule Components: Selector (source of the event) and action (where to send the event).

The following excerpt shows some sample rules from a **rsyslogd** configuration file:

|Log Facility/Severity|Log File Path|
|---|---|
|`auth,authpriv.*`|`/var/log/auth.log`|
|`*.*;auth,authpriv.none`|`-/var/log/syslog`|
|`cron.*`|`/var/log/cron.log`|
|`daemon.*`|`-/var/log/daemon.log`|
|`kern.*`|`-/var/log/kern.log`|
|`lpr.*`|`-/var/log/lpr.log`|
|`mail.*`|`-/var/log/mail.log`|
|`user.*`|`-/var/log/user.log`|
Understanding the syntax of a rule is important, so review some of the more critical syntactical elements.

## Selector Syntax

The selector is the first column, which consists of two components that are separated by a dot (`.`): the facility and the severity.

- The facility indicates the component reporting the event.
- The severity establishes a priority for the event. The following severity labels are listed from least severe to most severe:
    1. **Debug:** Debug information from running processes.
    2. **Info:** Simple informational messages.
    3. **Notice:** A condition that may require some attention.
    4. **Warn:** A warning.
    5. **Err:** An error condition
    6. **Crit:** A critical condition
    7. **Alert:** A condition that requires immediate attention
    8. **Emerg:** An emergency condition
    9. The following are examples:
        - `mail.info`**:** Translates to the mail facility with a severity of info. This format will include severity of info or greater (notice, warn, err …).
        - `=mail.info`**:** Translates to the mail facility with a severity of info. This format means only include the info severity.
- You can list multiple facilities in front of the dot. Each facility is separated with a comma.
	- `**auth,authpriv.**`***:** Translates to facility auth and authpriv with a priority of any.
- You can list multiple facility.severity pairs that are separated by semi-colons.
    - `***.*;auth,authpriv.none**`**:** Translates to any facility with any severity, except auth and authpriv facilities with no severity. Basically, everything except auth and authpriv.
## Action Syntax

The action portion of the syslog rule indicates which file should receive the event that is based on the facility and severity that is specified in the selector.

`mail.info /var/log/maillog`**:** Translates to: Send events with a facility of mail and a severity of info or greater to the **/var/log/maillog** file.

Some action entries start with a dash, a remnant from syslogd’s sync after logging. In recent syslog implementations, this functionality is disabled for performance, so the dash is meaningless. For instance:

`-/var/log/messages`: The dash has no effect.

Alerts can also be sent to the console instead of a file, which is a good way to get user attention if needed.

`kern.* /dev/console`: This configuration sends alerts from the kernel facility with any priority to the console.

```
#  /etc/rsyslog.conf    Configuration file for rsyslog.  
#  
#           For more information see  
#           /usr/share/doc/rsyslog-doc/html/rsyslog_conf.html  
...  
...  
auth,authpriv.*             /var/log/auth.log  
*.*;auth,authpriv.none      -/var/log/syslog  
#cron.*                     /var/log/cron.log  
daemon.*                    -/var/log/daemon.log  
kern.*                      -/var/log/kern.log  
lpr.*                       -/var/log/lpr.log  
mail.*                      -/var/log/mail.log  
user.*                      -/var/log/user.log  

#
# Logging for the mail system.  Split it up so that  
# it is easy to write scripts to parse these files.  
#  
mail.info                  -/var/log/mail.info  
mail.warn                  -/var/log/mail.warn  
mail.err                   /var/log/mail.err  
#  
# Logging for INN news system.  
#  
news.crit                  /var/log/news/news.crit  
news.err                   /var/log/news/news.err  
news.notice                -/var/log/news/news.notice
```
