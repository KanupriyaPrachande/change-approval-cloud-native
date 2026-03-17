pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Change Approval') {
            steps {
                bat 'python change_gate.py sample.yaml'
            }
        }
    }
}