pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/KanupriyaPrachande/change-approval-cloud-native'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}