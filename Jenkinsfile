pipeline {
    agent {
        docker {
            image 'python:3.8-slim' // Use a suitable Python Docker image
            args '-u root' // Run as root user inside the container
        }
    }

    environment {
        DEVICE_IP = '10.235.3.50' // Replace this with the actual IP of your Cisco device
    }

    stages {
        stage('Checkout Main') {
            steps {
                // Checkout the main branch to get the Jenkinsfile
                checkout([$class: 'GitSCM', branches: [[name: 'refs/heads/main']], userRemoteConfigs: [[url: 'https://github.com/nirakh123/netmiko-script.git']]])
            }
        }
        
        stage('Checkout Master') {
            steps {
                // Checkout the master branch to get the Python script
                checkout([$class: 'GitSCM', branches: [[name: 'refs/heads/master']], userRemoteConfigs: [[url: 'https://github.com/nirakh123/netmiko-script.git']]])
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
