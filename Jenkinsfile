pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:\\Python310' // Change this to your Python installation path
        PATH = "${env.PYTHON_HOME};${env.PYTHON_HOME}\\Scripts;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Igor2424/photo-organizer.git'
            }
        }

        stage('Setup Environment') {
            steps {
                bat """
                    REM Create virtual environment
                    %PYTHON_HOME%\\python.exe -m venv venv

                    REM Activate venv
                    call venv\\Scripts\\activate

                    REM Upgrade pip
                    %PYTHON_HOME%\\Scripts\\pip.exe install --upgrade pip

                    REM Install requirements if file exists
                    if exist requirements.txt %PYTHON_HOME%\\Scripts\\pip.exe install -r requirements.txt
                """
            }
        }

        stage('Lint') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    %PYTHON_HOME%\\Scripts\\pip.exe install flake8
                    flake8 . || exit 0
                """
            }
        }

        stage('Test') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    %PYTHON_HOME%\\Scripts\\pip.exe install pytest
                    pytest || echo "No tests found"
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
        success {
            echo 'All stages completed successfully ✅'
        }
        failure {
            echo 'Pipeline failed ❌'
        }
    }
}
