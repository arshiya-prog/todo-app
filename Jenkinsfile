pipeline {
    agent any

    environment {
        APP_NAME = "todo-app"
        IMAGE_NAME = "todo-app:latest"
        KUBE_DIR = "kubernetes"

        // Full paths to binaries
        DOCKER = "/usr/local/bin/docker"
        MINIKUBE = "/opt/homebrew/bin/minikube"
    }

    stages {

        stage('Clean Previous Image') {
            steps {
                echo "Cleaning old image (if exists)..."
                sh '''
                    eval $("${MINIKUBE}" docker-env)
                    ${DOCKER} image rm -f ${IMAGE_NAME} || true
                '''
            }
        }

        stage('Build Docker Image (Inside Minikube)') {
            steps {
                echo 'Building Docker image using Minikube Docker daemon...'
                sh '''
                    eval $("${MINIKUBE}" docker-env)
                    ${DOCKER} build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                echo 'Applying Kubernetes manifests...'
                sh 'kubectl apply -f $KUBE_DIR/deployment.yaml'
                sh 'kubectl apply -f $KUBE_DIR/service.yaml'
            }
        }

        stage('Verify Deployment') {
            steps {
                echo 'Verifying deployment...'
                sh 'kubectl rollout status deployment/${APP_NAME}-deployment'
                sh 'kubectl get pods'
                sh 'kubectl get svc'
            }
        }
    }

    post {
        success {
            echo "✅ Successfully deployed $APP_NAME to Minikube!"
        }
        failure {
            echo "❌ Deployment failed. Check logs above for errors."
        }
    }
}
