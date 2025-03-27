- ==Functionality==: Used to query, operate, and administer relational database management systems.
- ==Usage==: Consistent across database systems that support it, but with specific intricacies for each system.
- ==SQL in Web Applications==: Often used to dynamically build SQL statements for interacting with databases, utilizing user-supplied web input data.

![1](/Course-Notes/.assets/Pasted_image_20241118194043.png)

- ==SQL Injection Attack==: An attack that alters SQL statements in a web application using attacker-supplied data.
- ==Vulnerability==: Insufficient input validation in web applications.
- ==Impact==: Varies based on the targeted application and its data processing.

SQL functions include the following:

- Create databases and tables. The data in a database is stored in the tables. The table is a collection of related data entries and it consists of columns and rows. Columns contain the column name, data type, and any other attributes for the column. Rows contain the records or data for the columns.
- Define the data in the database and manipulate that data.
- Access the data in the database.
- Set the database permissions.

## SQL Commands

The following SQL commands are grouped according to the attacker's goals:

**Exfiltrating data**:
```
SELECT [fields] FROM [table] [...]
```

 **Modifying data:**
```
UPDATE [table] SET [field] = [value] WHERE [condition]
INSERT INTO [table] VALUES [...]

TRUNCATE TABLE [table]
```

**Modifying database structure**:
```
1. `DROP TABLE [table]`
2. `ALTER TABLE [table] [...]
3. `DROP DATABASE`
```

- Data Exfiltration Response: Analyze SQL operation results and search for abnormal traffic to identify data exfiltration.

- Data Modification Detection: Compare data with an offline backup to identify potential data deletion or modification.

- SQL Syntax and Commands: SQL commands, particularly the SELECT command, must follow specific syntax to retrieve data from tables.

```
SELECT * from Users where (username = 'submittedUser' and password = 'submittedPassword');
```

This type of web application should accept and process the user-supplied data (in this example, the username and password) with validation to ensure attackers can't craft the username and password inputs to create malicious SQL SELECT statements.