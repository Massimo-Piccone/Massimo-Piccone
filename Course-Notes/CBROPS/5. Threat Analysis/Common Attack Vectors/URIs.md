
In addition to URLs, there are other types of URIs. Broadly, URIs can be classified into **URLs**, **URNs**, and sometimes hybrid forms. Here’s a breakdown:

  

**1. URL (Uniform Resource Locator)**

  

• **Purpose**: Specifies the location of a resource and provides a way to retrieve it.

• **Example**:

• https://www.example.com/page.html

• ftp://ftp.example.com/file.txt

  

**2. URN (Uniform Resource Name)**

  

• **Purpose**: Identifies a resource by a persistent name, independent of its location.

• Does not include access or location details (e.g., no protocol or host).

• Often used for abstract or permanent identifiers.

• **Example**:

• urn:isbn:0451450523 (Identifies a book by its ISBN)

• urn:uuid:123e4567-e89b-12d3-a456-426614174000 (Universally unique identifier)

  

**3. Data URIs**

  

• **Purpose**: Embeds small data directly within the URI.

• Often used for embedding images or other media into HTML or CSS.

• **Example**:

  

data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA...

  

**4. File URIs**

  

• **Purpose**: References files stored locally on a computer or network.

• **Example**:

• file:///C:/Users/Carlos/Documents/report.txt

• file:///home/user/docs/report.txt

  

**5. Mailto URIs**

  

• **Purpose**: Specifies an email address, optionally with subject or body details.

• **Example**:

  

mailto:contact@example.com?subject=Hello&body=Message

  

**6. Tel URIs**

  

• **Purpose**: Refers to a telephone number for making calls or sending messages.

• **Example**:

  

tel:+1234567890

  

**7. SIP URIs (Session Initiation Protocol)**

  

• **Purpose**: Used in VoIP (Voice over IP) systems for initiating multimedia sessions.

• **Example**:

  

sip:username@domain.com

  

**8. JavaScript URIs**

  

• **Purpose**: Contains JavaScript code to be executed.

• Often used in browsers (though increasingly discouraged for security reasons).

• **Example**:

  

javascript:alert('Hello World')

  

**9. FTP URIs**

  

• **Purpose**: Identifies resources using the File Transfer Protocol.

• **Example**:

  

ftp://ftp.example.com/resource.txt

  

| Type            | Purpose                              | Example                               |
|-----------------|--------------------------------------|---------------------------------------|
| URL             | Locate and access a resource.       | https://www.example.com/page.html     |
| URN             | Identify a resource by name.        | urn:isbn:0451450523                   |
| Data URI        | Embed small data directly in the URI.| data:image/png;base64,...             |
| File URI        | Reference a local file.             | file:///C:/path/to/file.txt           |
| Mailto URI      | Specify an email address.           | mailto:someone@example.com            |
| Tel URI         | Specify a phone number.             | tel:+123456789                        |
| SIP URI         | Initiate multimedia sessions.       | sip:user@domain.com                   |
| JavaScript URI  | Execute JavaScript code.            | javascript:alert('Hello')             |
| FTP URI         | Reference files using FTP.          | ftp://ftp.example.com/file.txt        |