pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/GokulanPM/jenkins_1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Test Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name test-app flask-app'
                sh 'sleep 5'
                sh 'curl -f http://localhost:5000 || exit 1'
                sh 'docker stop test-app && docker rm test-app'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
    }
}
