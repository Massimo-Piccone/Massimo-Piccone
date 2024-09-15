# Python - Update a File
> This project is a simulated exercise, and all information presented is purely fictional for educational purposes.

## Description
As a security professional at a healthcare company, your job involves regularly updating a file that lists employees who can access restricted content, based on their work with personal patient records. Access to the restricted subnetwork is managed using an allow list of IP addresses. There's also a remove list specifying which IP addresses should be removed from the allow list.

Your task is to write a Python algorithm that checks if any IP addresses in the allow list match those in the remove list. If a match is found, the IP address should be removed from the allow list. The IPs to be removed are:
* `192.168.97.225`
* `192.168.158.170`
* `192.168.201.40`
* `192.168.58.57`

> Please see my [previous entry.]()

## Import and Read the File Contents
```python
# Import the file 
import_file = "allow_list.txt"

# Open the file
with open(import_file, "r") as file: 
    ip_addresses = file.read()

# Display the ip_addresses
print(ip_addresses)
```
Line 1 imported the `allow_list.txt` file,  line 2 read its contents using the `open()` function with the "`r`" (read) mode.<br>
The contents were stored in the `ip_addresses` variable were printed in line 3, showing 17 IP addresses:

```
ip_address
192.168.25.68
192.168.205.12
192.168.97.225
192.168.6.9
192.168.52.90
192.168.158.178
192.168.98.124
192.168.186.176
192.168.133.188
192.168.203.198
192.168.201.48
192.168.218.219
192.168.52.37
192.168.156.224
192.168.60.153
192.168.58.57
192.168.69.116
```

## Convert the String into a List
```python
# String into a list
import_file = "allow_list.txt"

# `with` statement to read the contents
with open(import_file, "r") as file: 
    ip_addresses = file.read()

# Convert from a string to a list
ip_addresses = ip_addresses.split()

# Display the `ip_addresses`
print(ip_addresses)
```
To facilitate removing specific IP addresses, convert the string format of `ip_addresses` into a list using the `split()` method.<br> The resulting list was printed, showing the individual IP addresses:

```
 ['ip_address', '192.168.25.60', '192.168.205.12', '192.168.97.225', '192.168.6.9', '192.168.52.90', '192.168.158.170', '192.168.90.124', '192.168.186.176', '192.168.133.188', '192.168.203.198', '192.168.201.40', '192.168.218.219', '192.168.52.37', '192.168.156.224', '192.168.60.153', '192.168.58.57', '192.168.69.116']
```

## Remove IP Addresses That Are on the Remove List
```python
# Import the file 
import_file = "allow_list.txt"

# Define `remove_list` with IP addresses to remove
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Read the file contents
with open(import_file, "r") as file: 
    ip_addresses = file.read()

# Convert from a string to a list
ip_addresses = ip_addresses.split()

# Loop through `ip_addresses` and remove those in `remove_list`
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

# Display the updated `ip_addresses` 
print(ip_addresses)
```
This loops through the `ip_addresses` list and checks if any addresses were in the `remove_list`. If a match was found, the address was removed. After this process, the updated list, now containing 13 IP addresses, was printed:

```
['ip_address', '192.168.25.60', '192.168.205.12', '192.168.6.9', '192.168.52.90', '192.168.90.124', '192.168.186.176', '192.168.133.188', '192.168.203.198', '192.168.218.219', '192.168.52.37', '192.168.156.224', '192.168.60.153', '192.168.69.116']
```

## Update the File With the Revised List of IP Addresses
```python
import_file = "allow_list.txt"

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

with open(import_file, "r") as file:
    ip_addresses = file.read()

ip_addresses = ip_addresses.split()

for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

# Convert `ip_addresses` back to a string
ip_addresses = " ".join(ip_addresses)

# Rewrite the file with the updated `ip_addresses`
with open(import_file, "w") as file:
    file.write(ip_addresses)

# Read and display the updated file
with open(import_file, "r") as file:
    text = file.read()

print(text)
```
Finally, convert the updated list of IP addresses back into a string using `join()` and overwrite the original `allow_list.txt` file with this revised list. The final content of the file, containing the 13 remaining IP addresses, was printed.

```
ip address 192.168.25.60 192.168.205.12 192.168.6.9 192.168.52.98 192.118.219 192.168.52.37 192.168.156.224 192.168.60.153 192.168.69.116
```

## Summary
The process involved reading the file, converting the string to a list, removing the specified IP addresses, and updating the file with the revised list.

> Here is my [certificate.](https://www.coursera.org/account/accomplishments/certificate/82RLLNC8G7NE) Please visit [Automate tasks with python](https://www.coursera.org/learn/automate-cybersecurity-tasks-with-python?specialization=google-cybersecurity) for more information.
