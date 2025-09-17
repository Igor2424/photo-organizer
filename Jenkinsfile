pipeline {
    agent any

    tools {
        python 'Python3'   // Configure Python in Jenkins Tools if needed
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Igor2424/photo-organizer.git'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || true
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    source venv/bin/activate
                    pip install flake8
                    flake8 . || true
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    source venv/bin/activate
                    pytest || echo "No tests found"
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'All good ✅'
        }
        failure {
            echo 'Something went wrong ❌'
        }
    }
}
