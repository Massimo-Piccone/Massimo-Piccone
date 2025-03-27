- Attack Vector: Social engineering exploits human vulnerabilities.
- Email Attack Sophistication: Malicious email attachments remain a primary attack vector, with attackers employing sophisticated tactics.
- Security Analyst’s Role: Investigate email proxy logs to identify senders, receivers, and timestamps of malicious emails.

- Malware Distribution Campaign Example: A campaign using UPS delivery notification emails to deceive targets into installing malware.
- Campaign Goal: To trick recipients into installing malware for financial gain.
- Malware Distribution Method: Initial attack vector installation followed by further malware distribution.

![1](/Course-Notes/.assets/Pasted_image_20241122143322.png)

The following is an example of the Cisco ESA log:
```
Thu Sep 18 16:17:38 2019 Info: Start MID 1653 ICID 16488
Thu Sep 18 16:17:38 2019 Info: MID 1653 ICID 16488 From: <auto-notify@ups.com>
Thu Sep 18 16:17:38 2019 Info: MID 1653 ICID 16488 RID 0 To: <any.one@mylocal_domain.com>
Thu Sep 18 16:17:38 2019 Info: MID 1653 Message-ID '<BLU437-SMTP10E1315A60354F2906677B9DB70@phx.gbl>'
Thu Sep 18 16:17:38 2019 Info: MID 1653 Subject 'Package delivery notification''
Thu Sep 18 16:17:38 2019 Info: MID 1653 ready 8313 bytes from <auto-notify@ups.com>
Thu Sep 18 16:17:38 2019 Info: MID 1653 matched all recipients for per-recipient policy DEFAULT in the inbound table
Thu Sep 18 16:17:38 2019 Info: ICID 16488 close
Thu Sep 18 16:17:39 2019 Info: MID 1653 interim verdict using engine: CASE spam negative
Thu Sep 18 16:17:39 2019 Info: MID 1653 using engine: CASE spam negative
Thu Sep 18 16:17:39 2019 Info: MID 1653 AMP file reputation verdict : MALWARE
Thu Sep 18 16:17:39 2019 Info: Message aborted MID 1653 Dropped by amp
Thu Sep 18 16:17:39 2019 Info: Message finished MID 1653 done
```

- Malware Detection: Cisco ESA with Cisco AMP detected and dropped a malware attachment in an email from auto-notify@ups.com.
- Email Proxy Logs: Email proxies typically log incoming spam, emails with detected viruses, and outgoing emails with sensitive content.
- DLP Policy Violation: An email from user1@exampleone.com violated the DLP policy and was quarantined by the email proxy.

```
2019 Sep 28 16:13:51 ironport_server mail [info] splunk_maillogs:nopid Info: MID 6509657 quarantined to "Policy" (DLP violation)

2019 Sep 28 16:13:51 ironport_server mail [info] splunk_maillogs:nopid Info: MID 6509657 DLP violation

2019 Sep 28 16:13:38 ironport_server mail [info] splunk_maillogs:nopid Info: MID 6509657 ready 53 bytes from user1@exampleone.com

2019 Sep 28 16:13:38 ironport_server mail [info] splunk_maillogs:nopid Info: MID 6509657 ICID 6237668 RID 0 To: johndoe@exampletwo.com
```

