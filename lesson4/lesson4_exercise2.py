from __future__ import print_function, unicode_literals

'''
2. Create three separate lists of IP addresses. The first list should be the IP addresses of the Houston data center 
routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

The second list should be the IP addresses of the Atlanta data center routers, and it should have at least eight RFC1918
 IP addresses (including some addresses that overlap with the Houston data center).

The third list should be the IP addresses of the Chicago data center routers, and it should have at least eight RFC1918
 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston and Atlanta.

Convert each of these three lists to a set.

Using a set operation, find the IP addresses that are duplicated between Houston and Atlanta.

Using set operations, find the IP addresses that are duplicated in all three sites.

Using set operations, find the IP addresses that are entirely unique in Chicago.
'''

# Create three separate lists of IP addresses. The first list should be the IP addresses of the Houston data center
# routers, and it should have over ten RFC1918 IP addresses in it (including some duplicate IP addresses).

# The second list should be the IP addresses of the Atlanta data center routers, and it should have at least eight
# RFC1918 IP addresses (including some addresses that overlap with the Houston data center).

# The third list should be the IP addresses of the Chicago data center routers, and it should have at least eight
# RFC1918 IP addresses. The Chicago IP addresses should have some overlap with both the IP addresses in Houston
# and Atlanta.

houston_dc = ['172.20.1.1',
              '172.20.1.2',
              '172.20.1.3',
              '172.20.1.4',
              '172.20.1.5',
              '172.20.1.4',
              '172.20.1.7',
              '172.20.1.9',
              '192.168.10.14',
              '172.20.1.8',
              '172.20.1.10']

atlanta_dc = ['192.168.10.1',
              '192.168.10.12',
              '192.168.10.13',
              '192.168.10.14',
              '192.168.10.14',
              '192.168.10.15',
              '172.20.1.4',
              '10.10.10.208',
              '192.168.10.16',
              '192.168.10.101',
              ]

chigago_dc = ['172.20.1.4',
              '172.20.1.8',
              '192.168.10.1',
              '10.10.10.20',
              '10.10.10.21',
              '10.10.10.25',
              '10.10.10.208',
              '10.10.10.205',
              '10.10.10.210',
              '10.10.10.90',
              '10.10.10.100',
              ]

# Convert each of these three lists to a set.
houston_dc_set = set(houston_dc)
atlanta_dc_set = set(atlanta_dc)
chigago_dc_set = set(chigago_dc)


# Set Operations #
# set1 | set2 => set1.union(set2) - shows all unique elements the comes from set1 and set2
# set1 & set2 => set1.intersection(set2) - show all values present in both sets
# set1 - set2 => set1.difference(set2) - remove from set1 all elements that are also present in set2, in other words, shows only uniques elements on set1.
# set1 ^ set2 => set1.symmetric_difference(set2) - shows uniques elements on both set1 and set2

# Using a set operation, find the IP addresses that are duplicated (intersection) between Houston and Atlanta.
print(houston_dc_set.intersection(atlanta_dc_set))

# Using set operations, find the IP addresses that are duplicated in all three sites.
print(chigago_dc_set.intersection(houston_dc_set.intersection(atlanta_dc_set)))

# Using set operations, find the IP addresses that are entirely unique in Chicago.
print(chigago_dc_set - (houston_dc_set | atlanta_dc_set))
print(chigago_dc_set.difference(houston_dc_set.union(atlanta_dc_set)))
