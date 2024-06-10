pipeline {
    agent any

    environment {
        DEVICE_IP = '192.168.1.1'
        DEVICE_USERNAME = credentials('cisco-username')
        DEVICE_PASSWORD = credentials('cisco-password')
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Checkout the repository containing the Python script
                git 'https://github.com/yourusername/yourrepo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Install dependencies
                sh 'pip install netmiko'
            }
        }

        stage('Run Script') {
            steps {
                // Execute the Python script
                sh """
                python -c "
                import netmiko
                from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

                device_info = {
                    'device_type': 'autodetect',
                    'host': '${DEVICE_IP}',
                    'username': '${DEVICE_USERNAME}',
                    'password': '${DEVICE_PASSWORD}',
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
                        print(f'\\nOutput for command: {command}')
                        print(output)

                except NetmikoTimeoutException as e:
                    print('Connection timed out. Please check the IP address and network connectivity.')
                except NetmikoAuthenticationException as e:
                    print('Authentication failed. Please check the username and password.')
                except Exception as e:
                    print(f'An error occurred: {e}')
                finally:
                    if 'net_connect' in locals():
                        net_connect.disconnect()

                print('Script execution completed.')
                "
                """
            }
        }
    }
}
