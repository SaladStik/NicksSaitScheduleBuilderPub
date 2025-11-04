pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'sait-schedule-builder'
        CONTAINER_NAME = 'sait-schedule-builder'
        NETWORK_NAME = 'nickssaitschedulebuilderpub_app-network'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest code from GitHub...'
                checkout scm
            }
        }
        
        stage('Stop Old Container') {
            steps {
                echo 'Stopping and removing old container...'
                script {
                    sh '''
                        docker stop ${CONTAINER_NAME} || true
                        docker rm ${CONTAINER_NAME} || true
                    '''
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building new Docker image...'
                script {
                    sh '''
                        docker build -t ${DOCKER_IMAGE}:latest .
                        docker tag ${DOCKER_IMAGE}:latest ${DOCKER_IMAGE}:${BUILD_NUMBER}
                    '''
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying new container...'
                script {
                    sh '''
                        docker run -d \
                            --name ${CONTAINER_NAME} \
                            --network ${NETWORK_NAME} \
                            -p 8501:8501 \
                            -e STREAMLIT_SERVER_PORT=8501 \
                            -e STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
                            --restart unless-stopped \
                            ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }
        
        stage('Cleanup Old Images') {
            steps {
                echo 'Cleaning up old Docker images...'
                script {
                    sh '''
                        # Keep last 3 builds, remove older ones
                        docker images ${DOCKER_IMAGE} --format "{{.ID}} {{.Tag}}" | \
                        grep -v latest | \
                        tail -n +4 | \
                        awk '{print $1}' | \
                        xargs -r docker rmi || true
                    '''
                }
            }
        }
    }
    
    post {
        success {
            echo '✅ Deployment successful! App is running at http://localhost:8501'
        }
        failure {
            echo '❌ Deployment failed! Check the logs above.'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
