pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'  // Ensure you have your tests defined
            }
        }
        // stage('Deploy') {
        //     steps {
        //         // Deploy to Azure
        //         sh 'az webapp up --name YourAppName --resource-group YourResourceGroup --plan YourAppServicePlan'
        //     }
        // }
    }
}
