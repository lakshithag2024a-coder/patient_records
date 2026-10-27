pipeline {
    agent any
    environment{
        DOCKERHUB_CREDS = credentials('dockerhub-creds')
        IMAGE_NAME = "lakshitha119/patient-records"
        TAG = "v1" 
    }
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'
                sh 'docker push $IMAGE_NAME:$TAG'
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}