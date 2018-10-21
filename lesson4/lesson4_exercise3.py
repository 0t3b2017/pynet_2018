from __future__ import print_function, unicode_literals
import re

"""
3.  Read in the 'show_version.txt' file. From this file, use regular expressions to extract the OS version, 
serial number, and configuration register values.

Your output should look as follows:
OS Version: 15.4(2)T1      
Serial Number: FTX0000038X    
​Config Register: 0x2102 
"""

with open('show_version.txt') as f:
    show_ver = f.read()

os_version = re.search(r'^.* Version\s([\d\.\(\)\w]+)', show_ver).group(1)
serial_number = re.search(r'Processor board ID (\w+)', show_ver).group(1)
config_register = re.search(r'Configuration register is (\w+)', show_ver).group(1)

print('OS Version: ' + os_version)
print('Serial Number: ' + serial_number)
print('Config Register: ' + config_register)
