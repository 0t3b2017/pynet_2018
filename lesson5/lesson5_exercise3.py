from __future__ import print_function, unicode_literals
import re

"""
3. Similar to lesson3, exercise4 write a function that normalizes a MAC address to the following format:

01:23:45:67:89:AB

This function should handle the lower-case to upper-case conversion.

It should also handle converting from '0000.aaaa.bbbb' and from '00-00-aa-aa-bb-bb' formats.

The function should have one parameter, the mac_address. It should return the normalized MAC address

Single digit bytes should be zero-padded to two digits. In other words, this:

a:b:c:d:e:f

should be converted to:

0A:0B:0C:0D:0E:0F

Write several test cases for your function and verify it is working properly.

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


print(mac_converter('0000.aaaa.bbbb'))
print(mac_converter('00-00-aa-aa-bb-bb'))
print(mac_converter('0-0-a-a-b-b'))
print(mac_converter('02:42:44:a1:f9:eb'))
print(mac_converter('ffff.ffff.ffff'))
print(mac_converter('ff-ff-ff-ff-ff-ff'))
