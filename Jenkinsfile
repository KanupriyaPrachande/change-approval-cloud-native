pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'apt-get update && apt-get install -y python3 python3-pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run') {
            steps {
                sh 'python3 change_gate.py sample.yaml'
            }
        }
    }
}