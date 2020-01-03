from __future__ import absolute_import, division, print_function

import netmiko
import json
import getpass

##user = raw_input("Username: ")
##pw = getpass.getpass("Password: ")


devices = '''
192.168.1.84
'''.strip().splitlines()

device_type = 'cisco_ios'

for device in devices:
    print('~' * 79)
    print('Connecting to device:' + device)
    username = input('Username: ')
    password = getpass.getpass()
    connection = netmiko.ConnectHandler(ip=device, device_type=device_type, username=username, password=password,
                                        secret="")
    print(connection.send_command('show clock'))
    #connection.config_mode()
   # connection.send_command('copy running-config tftp://192.168.1.68/ ' + device + '.txt')
    connection.config_mode()
    connection.send_command_timing('archive')
    connection.send_command('path tftp://192.168.1.68/CCP/$h-$t')
    connection.send_command('write-memory')
    connection.exit_config_mode()
    connection.send_command('write memory')
    connection.disconnect()



