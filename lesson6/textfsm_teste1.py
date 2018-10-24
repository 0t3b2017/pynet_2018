from netmiko import Netmiko
#from netmiko import ConnectHandler
from getpass import getpass

my_switch = {
        'host': '192.168.122.71',
        'username': 'roberto',
        'password': getpass(),
        'device_type': 'cisco_ios',
        }

net_conn = Netmiko(**my_switch)
net_conn.open_session_log('{}-2018_new'.format(my_switch['host']))

cmd = 'show ip arp'
output = net_conn.send_command(cmd, use_textfsm=True)

print(output)

net_conn.disconnect
