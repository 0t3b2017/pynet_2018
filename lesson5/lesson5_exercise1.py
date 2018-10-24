from __future__ import print_function, unicode_literals

"""
1a. Create an ssh_conn function. This function should have three parameters: ip_addr, username,
 and password. The function should print out each of these three variables and clearly indicate which 
 variable it is printing out.

Call this ssh_conn function using entirely positional arguments.

Call this ssh_conn function using entirely named arguments.

Call this ssh_conn function using a mix of positional and named arguments.


1b. Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type' 
with a default value of 'cisco_ios'. Print all four of the function variables out as part of the 
function's execution.

Call the 'ssh_conn2' function both with and without specifying the device_type

Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using 
the **kwargs technique.
"""

# Create an ssh_conn function. This function should have three parameters: ip_addr, username,
# and password. The function should print out each of these three variables and clearly indicate which
# variable it is printing out.


def ssh_conn(ip_addr, username, password):
    print()
    print('IP ADDRESS: {}'.format(ip_addr))
    print('USERNAME: {}'.format(username))
    print('PASSWORD: {}'.format(password))
    print()

# Call this ssh_conn function using entirely positional arguments.
ssh_conn('10.1.1.1', 'roberto', 'P@ssw0rd')

# Call this ssh_conn function using entirely named arguments.
ssh_conn(ip_addr='172.21.10.1', username='roberto', password='myP@ssw0rd')

# Call this ssh_conn function using a mix of positional and named arguments.
ssh_conn('192.168.0.1', 'User', password='MyPass')

# Expand on the ssh_conn function from exercise1 except add a fourth parameter 'device_type'
# with a default value of 'cisco_ios'. Print all four of the function variables out as part of the
# function's execution.


def ssh_conn2(ip_addr, username, password, device_type='cisco_ios'):
    print()
    print('IP ADDRESS: {}'.format(ip_addr))
    print('USERNAME: {}'.format(username))
    print('PASSWORD: {}'.format(password))
    print('DEVICE TYPE: {}'.format(device_type))
    print()

# Call the 'ssh_conn2' function both with and without specifying the device_type
ssh_conn2('5.5.5.5', 'roberto', 'MyP@ss')
ssh_conn2('5.5.5.5', 'roberto', 'MyP@ss', 'junos')

# Create a dictionary that maps to the function's parameters. Call this ssh_conn2 function using
# the **kwargs technique.

dev_dict = {
    'ip_addr': '9.9.9.9',
    'username': 'roberto',
    'password': 'myP@ss3',
    'device_type': 'eos'
}

ssh_conn2(**dev_dict)
