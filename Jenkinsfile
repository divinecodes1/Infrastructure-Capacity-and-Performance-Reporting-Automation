pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source'
            }
        }
        stage('Lint Python') {
            steps {
                sh 'python -m pytest -q'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest -q'
            }
        }
        stage('Generate Reports') {
            steps {
                sh 'python src/main.py'
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'reports/*', fingerprint: true
            }
        }
    }
}
