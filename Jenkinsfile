pipeline {
    agent any
    environment {
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        IMAGE_NAME = "lakshitha119/patient-records"
        TAG = "v1" 
    }
    stages {
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%TAG% .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                bat 'docker login -u %DOCKERHUB_CREDS_USR% -p %DOCKERHUB_CREDS_PSW%'
                bat 'docker push %IMAGE_NAME%:%TAG%'
            }
        }
    }
    post {
        always {
            bat 'docker logout'
        }
    }
}