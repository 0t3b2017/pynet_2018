from netmiko import ConnectHandler
from getpass import getpass

my_switch = {
        'host': '192.168.122.71',
        'username': 'roberto',
        'password': 'cisco',
        'device_type': 'cisco_ios',
        }

net_conn = ConnectHandler(**my_switch)
net_conn.open_session_log('{}-2018'.format(my_switch['host']))

filename = 'show_running.0t3B'
cmd = 'delete flash0:{}'.format(filename)
#output = net_conn.send_command(cmd)
output = net_conn.send_command_timing(cmd)

if 'Delete filename' in output:
    output += net_conn.send_command_timing("\n")
    output += net_conn.send_command_timing("\n")

print(output)

net_conn.disconnect
