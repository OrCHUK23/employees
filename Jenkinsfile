pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout all branches
                    checkout scm
                }
            }
        }

        stage('Unit Tests') {
            when {
                anyOf {
                    branch 'feature'
                    branch 'develop'
                }
            }
            steps {
                script {
                    // Run unit tests using Python unittest.
                    sh 'python3 -m unittest test_employees.py'
                }
            }
        }

        // stage('API Tests') {
        //     when {
        //         branch 'develop'
        //     }
        //     steps {
        //         script {
        //             // Run API tests using Python requests
        //             sh 'python3 api_tests.py'
        //         }
        //     }
        // }

        stage('Create Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t orchuk/employees:${BRANCH_NAME} .'
                }
            }
        }

        stage('Push to Repository') {
            when {
                branch 'master'
            }
            steps {
                script {
                    // Push Docker image to Docker Hub
                    sh 'docker push orchuk/employees:${BRANCH_NAME}'
                }
            }
        }
    }
}
