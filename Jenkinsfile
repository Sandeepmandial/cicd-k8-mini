pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Sandeepmandial/cicd-k8-mini.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-app .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pip install flask'
                bat 'python test_app.py'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
}
