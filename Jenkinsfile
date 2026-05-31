pipeline {
    agent any

    environment {
        ECR_URI = '374356571014.dkr.ecr.us-east-1.amazonaws.com/python-todo-app'
        REGION  = 'us-east-1'
    }

    stages {

        stage('Build Image') {
            steps {
                sh 'docker build -t $ECR_URI:$BUILD_NUMBER ./backend'
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                    aws ecr get-login-password --region $REGION | \
                    docker login --username AWS --password-stdin $ECR_URI
                    docker push $ECR_URI:$BUILD_NUMBER
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker stop python-app || true
                    docker rm python-app || true
                    docker run -d --name python-app \
                        -p 5000:5000 \
                        $ECR_URI:$BUILD_NUMBER
                '''
            }
        }
    }

    post {
        success { echo '✅ Image pushed to ECR and container running!' }
        failure { echo '❌ Pipeline failed!' }
        always  { sh 'docker image prune -f' }
    }
}
