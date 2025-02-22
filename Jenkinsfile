pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Kishor-Malakar/Flask-assignment.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t kishor03/flask-api .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push kishor03/flask-api'
                }
            }
        }

        stage('Deploy to Azure') {
            steps {
                sh 'az webapp create --resource-group myResourceGroup --plan myAppServicePlan --name myFlaskApp --deployment-container-image-name kishor03/flask-api'
            }
        }
    }
}
