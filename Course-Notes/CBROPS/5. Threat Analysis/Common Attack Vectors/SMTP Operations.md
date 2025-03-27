- ==Email System Threats==: Spam and malicious email (embedded attacks like viruses and malware, and targeted attacks like phishing).
- ==Malicious Email Impact==: Wastes employee time, consumes resources, and can lead to data breaches.
- ==Mitigating Email Attacks==: Understanding the mail delivery process and SMTP conversations is crucial for effective security measures.

## SMTP Terminology

- ==Mail Transfer Agent==(MTA), also known as SMTP daemon, is a computer program that transfers electronic mail messages between computers. Personal computers use client applications like Microsoft Outlook to send mail to groupware servers, which relay it through the MTA to other mail domains. Another name for an MTA is an email gateway. The Cisco Email Security Appliance (ESA) serves this role in the network.
- ==DNS MX record== specifies the mail server (MTA) responsible for accepting email for a domain. It includes a preference value to prioritize the chosen mail server.
- ==DNS A record== locates the IP address of the MTA specified by the MX record.
- ==Groupware server== accepts, forwards, delivers, and stores messages for users. It also manages collaborative schedules and calendars.
- ==SMTP client== initiates a connection request to an SMTP server, either within the enterprise or on the Internet.
- ==SMTP server== receives the connection request and initiates the mail transfer.
- ==Mail user agent== (MUA) is a software client application that accesses a groupware server to send or receive mail.
- ==Post Office Protocol== (POP): POP, an application-layer protocol, retrieves email from a mail server using TCP port 110. It downloads new messages, deletes them from the server, and is the last common standard version.
- ==Internet Message Access Protocol== (IMAP): IMAP, also an application-layer protocol, retrieves email from a mail server on TCP port 143. It supports accessing email from anywhere and is widely used. IMAP and POP3 are the most prevalent email retrieval protocols.  
- ==Messaging Application Programming Interface== (MAPI): MAPI, primarily associated with Microsoft Exchange and Outlook, retrieves email from a mail server and provides groupware functions. It performs similar services to IMAP.

## SMTP Flow

The figure illustrates mail delivery stages:

![3](/Course-Notes/.assets/Pasted_image_20241118201749.png)

Secure-x.public’s MTA receives an email from Alejandro to Emily. It’s the sending MTA.

The sending MTA resolves Emily’s domain to the Cisco MTA’s IP address using DNS.

It sends the email to mx.cisco.com, the receiving MTA.

Assuming Secure-x.public’s reputation is good, the receiving MTA looks up Emily’s LDAP user and forwards the email.

The exchange server sends the email to Emily’s MUA using protocols like POP, IMAP, or MAPI, with MAPI used by the MUA.

The following figure shows the mail delivery process when Emily replies to the received email. Here, IMAP is used by Alejandro to retrieve the email from the exchange mail server instead of MAPI.

![2](/Course-Notes/.assets/Pasted_image_20241118201850.png)

## SMTP Conversation

The figure shows the three parts of the SMTP conversation.

The events occur sequentially:

![1](/Course-Notes/.assets/Pasted_image_20241118202105.png)  

1. ==Envelope==: Specifies the recipient and sender.
2. ==Headers==: Sent after receiving a 354 reply code. Contain sender and recipient’s display names and emails, and the subject and date. A blank line separates headers from message content.
3. ==Body==: An optional text region transmitted after the DATA command is accepted, before the end of data indication. A null line or a period indicates the end of data transmission.

SMTP commands transfer requests from the client to the SMTP server. Here are the most common commands:
- The **HELLO (HELO)** or **EHLO (Extended HELLO)** commands are used to identify the SMTP client to the SMTP server. The FQDN or the IP address of the SMTP client is usually sent as an argument together with `HELO` or `EHLO` commands. The `HELO` command is used to establish an SMTP session with another host. The `EHLO` command is used to establish an Extended Simple Mail Transfer Protocol (ESMTP) session with another host. ESMTP specifies extensions to the SMTP standard to support additional commands. For example, ESMTP supports the `SIZE` command, which allows the receiving host to tell the sending host the maximum message size before the message is transmitted. Both the sending host and the receiving host must support the ESMTP protocol for the extended ESMTP capabilities to be utilized.
    
- The **MAIL FROM** command is used to initiate a mail transaction in which the mail data is delivered to an SMTP server which may, in turn, deliver it to one or more mailboxes. The `MAIL FROM` command specifies who the mail originator is.
    
- The **RCPT TO** command is used to identify an individual recipient of the mail data. Use multiples of this command to specify multiple recipients.
    
- The **DATA** command signifies that the email message body will follow. The receiver normally sends a 354 go ahead response, then treats the lines (strings ending in `<CRLF>` sequences) as mail data from the sender.
    
- The **QUIT** command specifies that the receiver must send an OK reply, and then close the transmission channel. The receiver must not intentionally close the transmission channel until it receives and replies to a `QUIT` command (even if there was an error). The sender must not intentionally close the transmission channel until it sends a `QUIT` command and should wait until it receives the reply (even if there was an error response to a previous command)


The three-digit SMTP reply codes define the server response to the SMTP client:

- The first digit denotes the success or failure of the SMTP command.
    1 = command accepted but pending confirmation (example, 101 can’t open connection)        
    2 = success (example, 250 OK)
    3 = okay so far (example, 354 go ahead, also called start mail input)
    4 = temporary failure (example, 452 mailbox full)
    5 = permanent failure (example, 550 user unknown)
- The second digit categorizes the result.
    0 = syntax
    1 = information
    2 = connection
    3 = unspecified
    4 = unspecified
    5 = mail system
- The third digit adds finer detail.

The following are a few more SMTP reply code examples:
- 211 = system status, or system help reply
- 220 (FQDN of server) = service ready
- 421 (FQDN of server) = service not available
- 451 = local error in processing
- 500 = command not recognized
- 502 = command not implemented