pipeline {
    agent {
        docker {
            image 'python:3.8-slim'
            args '-u root'
        }
    }
    environment {
        CUSTOM_WORKSPACE = '/home/jenkins/workspace'
    }
    stages {
        stage('Checkout SCM') {
            steps {
                dir(env.CUSTOM_WORKSPACE) {
                    git url: 'https://github.com/nirakh123/netmiko-script', credentialsId: 'CISCO_SWITCH_CREDENTIALS'
                }
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
                // Use withCredentials to inject the username and password
                withCredentials([usernamePassword(credentialsId: 'CISCO_SWITCH_CREDENTIALS', passwordVariable: 'DEVICE_PASSWORD', usernameVariable: 'DEVICE_USERNAME')]) {
                    script {
                        def deviceIp = "${DEVICE_IP}"
                        def deviceUsername = "${DEVICE_USERNAME}"
                        def devicePassword = "${DEVICE_PASSWORD}"

                        sh """
                        python retrieve_config.py ${deviceIp} ${deviceUsername} ${devicePassword}
                        """
                    }
                }
            }
        }
    }
}
