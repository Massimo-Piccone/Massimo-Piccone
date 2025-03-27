- Used for accessing directory services
 ﻿﻿Directory includes:
	- ﻿﻿Users
	- ﻿﻿Groups
	- ﻿﻿Password
	- ﻿﻿Additional resources

- ﻿﻿Syntax uses x.500 standard for identifying objects in the LDAP structure by way of a series of attributes. Attributes consist of an attribute name followed by the attribute value. For example:
	telephone: +1 222 333 4455

An entity in the LDAP structure is uniquely identified by its distinguished name (DN). For example, the user Ed Smith that works for MyOrg may have the following DN:

`dn: cn=ed smith,dc=MyOrg,dc=com`

The component that is called **cn** is known is the canonical name. 
The dc components are known as domain components. In the example, the first dc entry is the organization’s primary domain name: MyOrg. The second is the top-level domain that the organization is registered as: com.

An LDAP record for this user may appear as follows:
```
dn: cn=ed smith,dc=MyOrg,dc=com
cn: ed smith
given name: ed
sn: smith
mail: esmith@MyOrg.com
```

most common LDAP implementation in Linux is OpenLDAP. 
Its configuration and log files are referred to as **slapd**, 
stands for "stand-alone LDAP daemon"