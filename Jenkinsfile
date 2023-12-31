pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Tests') {
            when {
                expression { 
                    return env.BRANCH_NAME ==~ /(feature|develop)/
                }
            }
            steps {
                sh 'python3 -m unittest employees.tests.test_employees'
            }
        }

        // Add more stages as needed
        // For example, you can include stages for building Docker images, pushing to a repository, etc.

        stage('Build Docker Image') {
            when {
                expression { 
                    return env.BRANCH_NAME ==~ /(feature|develop)/
                }
            }
            steps {
                sh 'docker build -t your-docker-repo/your-flask-app:${env.BRANCH_NAME} .'
            }
        }

        stage('Push to Repository') {
            when {
                expression { 
                    return env.BRANCH_NAME == 'master'
                }
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'your-docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                        sh 'docker push your-docker-repo/your-flask-app:${env.BRANCH_NAME}'
                    }
                }
            }
        }
    }

    post {
        always {
            // Additional post-build actions if needed
        }
    }
}
