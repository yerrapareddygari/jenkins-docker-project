pipeline {
    agent any

    stages {

        stage('Build') {
            parallel {
                stage('Build Backend') {
                    steps {
                        sh 'docker build -t todo-backend ./backend'
                    }
                }
                stage('Build Frontend') {
                    steps {
                        sh 'docker build -t todo-frontend ./frontend'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop backend frontend || true
                    docker rm backend frontend || true

                    docker run -d --name backend \
                        -p 5000:5000 \
                        todo-backend

                    docker run -d --name frontend \
                        -p 3000:3000 \
                        todo-frontend
                '''
            }
        }
    }

    post {
        success { echo '✅ Containers are running!' }
        failure { echo '❌ Pipeline failed!' }
        always  { sh 'docker image prune -f' }
    }
}
