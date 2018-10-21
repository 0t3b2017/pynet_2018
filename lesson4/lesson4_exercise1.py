from __future__ import print_function, unicode_literals

"""1. Create a dictionary representing a network device. The dictionary should have key-value pairs representing the 
'ip_addr', 'vendor', 'username', and 'password' fields. 

Print out the 'ip_addr' key from the dictionary.

If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the 
'platform' to 'junos'.

Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as', 
'peer_as', and 'peer_ip'. 

Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.

Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.

Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
"""

# Create a dictionary representing a network device. The dictionary should have key-value pairs representing the
# 'ip_addr', 'vendor', 'username', and 'password' fields.
device = {
    'ip_addr': 'router1',
    'vendor': 'juniper',
    'username': 'roberto',
    'password': 'P@ssw0rd',
}

# Print out the 'ip_addr' key from the dictionary.
print(device['ip_addr'])

# If the 'vendor' key is 'cisco', then set the 'platform' to 'ios'. If the 'vendor' key is 'juniper', then set the
# 'platform' to 'junos'.
if device['vendor'] == 'cisco':
    device['platform'] = 'ios'
elif device['vendor'] == 'juniper':
    device['platform'] = 'junos'
else:
    device['platform'] = None

print(device['platform'])

# Create a second dictionary named 'bgp_fields'. The 'bgp_fields' dictionary should have a keys for 'bgp_as',
# 'peer_as', and 'peer_ip'.

bgp_fields = {
    'bgp_as': '65000',
    'peer_as': '65010',
    'peer_ip': '100.64.10.100',
}

print(bgp_fields)
print()
print(device)
print()
device.update(bgp_fields)
print(device)

# Using the .update() method add all of the 'bgp_fields' dictionary key-value pairs to the network device dictionary.
bgp_fields.update()

# Using a for-loop, iterate over the dictionary and print out all of the dictionary keys.
for value in device.values():
    print(value)

# Using a single for-loop, iterate over the dictionary and print out all of the dictionary keys and values.
for v, k in device.items():
    print('key {} => value {}'.format(k, v))
