from __future__ import print_function, unicode_literals
import random

"""
2.  Create a function that randomly generates an IP address for a network. The default base network should 
be '10.10.10.'. For simplicity the network will always be a /24.

You should be able to pass a different base network into your function as an argument.

Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

You can use the following to randomly generate the last octet:
import random
random.randint(1, 254)

Call your function using no arguments.
Call your function using a positional argument.
Call your function using a named argument.

For each function call print the returned IP address to the screen.
"""


# Create a function that randomly generates an IP address for a network. The default base network should
# be '10.10.10.'. For simplicity the network will always be a /24.
# You should be able to pass a different base network into your function as an argument.

def gen_ip(network_base='10.10.10.'):
    num = str(random.randint(1, 254))
    ip_addr = network_base + num
    return ip_addr

# Randomly pick a number between 1 and 254 for the last octet and return the full IP address.

# You can use the following to randomly generate the last octet:
# import random
# random.randint(1, 254)

# For each function call print the returned IP address to the screen.
# Call your function using no arguments.
print(gen_ip())

# Call your function using a positional argument.
print(gen_ip('192.168.100.'))

# Call your function using a named argument.
print(gen_ip(network_base='100.64.10.'))


