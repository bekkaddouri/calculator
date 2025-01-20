pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/votre-repo/app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('calculateur-moyenne')
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-credentials-id') {
                        docker.image('calculateur-moyenne').push('latest')
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f flask-deployment.yaml'
                sh 'kubectl apply -f database-deployment.yaml'
            }
        }
    }
}
