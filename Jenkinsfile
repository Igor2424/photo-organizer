pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checkout the source code
            }
        }

        stage('Install Dependencies') {
            steps {
                // Assuming you're using pip and have a requirements.txt file
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Assuming you're using pytest for testing
                sh 'pytest'
            }
        }
    }

    post {
        always {
            echo 'Test completed'
        }
    }
}
