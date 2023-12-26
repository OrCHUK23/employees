pipeline {
    agent { label 'workers' }
    stages {
        stage('hello') {
            steps {
                echo 'Hello World!!!'
            }
        }
        stage {
            when {
                branch 'dev*'
            }
            steps {
                sh '''
                cat README.md
                '''
            }
        }
    }
}
