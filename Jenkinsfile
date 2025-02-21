pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'capstone-img'
        AZURE_APP_NAME = 'capstone'
        AZURE_RESOURCE_GROUP = 'ResourceGroup'
        AZURE_PLAN = 'AppServicePlan'
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git
                git branch: 'main', url: 'https://github.com/Kishor-Malakar/Flask-assignment.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install npm dependencies
                sh 'npm install'
            }
        }
        stage('Run Tests') {
            steps {
                // Run Jest tests
                sh 'npm test'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }
        // stage('Deploy to Azure') {
        //     steps {
        //         script {
        //             // Login to Azure
        //             sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID'

        //             // Deploy Docker image to Azure App Service
        //             sh 'az webapp create --resource-group $AZURE_RESOURCE_GROUP --plan $AZURE_PLAN --name $AZURE_APP_NAME --deployment-container-image-name $DOCKER_IMAGE'
        //         }
        //     }
        // }
    }
    post {
        always {
            // Cleanup
            cleanWs()
        }
    }
}
