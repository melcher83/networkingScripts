from __future__ import absolute_import, division, print_function

import netmiko
import json
import getpass

##user = raw_input("Username: ")
##pw = getpass.getpass("Password: ")


devices = '''
192.168.1.1
192.168.1.2
'''.strip().splitlines()

device_type = 'cisco_ios'

for device in devices:
    print('~' * 79)
    print('Connecting to device:' + device)
    username = raw_input('Username: ')
    password = getpass.getpass()
    connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password,
                                        secret="")
    print(connection.send_command('show clock'))
    # connection.config_mode()
    # connection.send_command('ip name-server 10.200.10.22')
    # connection.send_command('ntp server 0.pool.ntp.org')
    # connection.exit_config_mode()
    connection.send_command('write memory')
    connection.disconnect()



