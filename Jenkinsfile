pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-app"
    }

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/Sandeepmandial/cicd-k8-mini.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                bat 'docker run --rm %IMAGE_NAME% python test_app.py'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get pods'
                bat 'kubectl get services'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed! Check logs.'
        }
    }
}