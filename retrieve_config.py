import netmiko
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import getpass  

IP = input("Enter IP: ")
Username = input("Username: ")
Password = getpass.getpass("Password: ")  

device_info = {
    'device_type': 'autodetect', 
    'host': IP,
    'username': Username,
    'password': Password,
    'port': 22 
}

try:
    net_connect = ConnectHandler(**device_info)

    commands = [
        'term length 0',
        'show running-config',
        'show cdp neighbors',
        'show version'
    ]
    for command in commands:
        output = net_connect.send_command(command)
        print(f"\nOutput for command: {command}")
        print(output)

except NetmikoTimeoutException as e:
    print("Connection timed out. Please check the IP address and network connectivity.")
except NetmikoAuthenticationException as e:
    print("Authentication failed. Please check the username and password.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'net_connect' in locals():
        net_connect.disconnect()

print("Script execution completed.")