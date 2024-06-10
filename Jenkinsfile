pipeline {
    agent any

    environment {
        DEVICE_IP = '10.235.3.50' // Replace this with the actual IP of your Cisco device
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Checkout the repository containing the Python script
                git 'https://github.com/nirakh123/netmiko-script' // Replace with your repository URL
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
                    // Execute the Python script with the environment variables
                    sh """
                    python retrieve_config.py ${DEVICE_IP} ${DEVICE_USERNAME} ${DEVICE_PASSWORD}
                    """
                }
            }
        }
    }
}
