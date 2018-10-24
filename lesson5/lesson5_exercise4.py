from __future__ import print_function, unicode_literals
import re
import pdb

"""
4. Copy your solution from exercise3 to exercise4. Add an 'import pdb' and pdb.set_trace() statement outside of your 
function (i.e. where you have your function calls).

Inside of pdb, experiment with:
Listing your code.
(Pdb) list .
Using 'next' and 'step' to walk through your code. Make sure you understand the difference between next and step.
(Pdb) next
(Pdb) step # show inside function (each step)
Experiment with 'up' and 'down' to move up and down the code stack.
(Pdb) up
(Pdb) down
Use p <variable> to inspect a variable.

Set a breakpoint and run your code to the breakpoint.
Use '!command' to change a variable (for example !new_mac = [])
"""

def mac_converter(mac_address):
    s = re.compile('\.|-|:')
    mac_address_split = s.split(mac_address)
    for p, i in enumerate(mac_address_split):
        if len(i) < 2:
            mac_address_split[p] = '0{}'.format(i)

    mac_addr = ''.join(mac_address_split).upper()

    new_mac = ''
    while len(mac_addr) > 0:
        new_mac += mac_addr[:2] + ':'
        mac_addr = mac_addr[2:]

    new_mac = new_mac.rstrip(':')
    return new_mac


pdb.set_trace()
print(mac_converter('0000.aaaa.bbbb'))
print(mac_converter('00-00-aa-aa-bb-bb'))
print(mac_converter('0-0-a-a-b-b'))
print(mac_converter('02:42:44:a1:f9:eb'))
print(mac_converter('ffff.ffff.ffff'))
print(mac_converter('ff-ff-ff-ff-ff-ff'))
