pipeline {
    agent any

    environment {
        APP_NAME = "todo-app"
        IMAGE_TAG = "latest"
        IMAGE_NAME = "todo-app"
        KUBE_DIR = "kubernetes"
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
                script {
                    def imageTag = "${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                    sh "docker build -t ${imageTag} ."
                    sh "minikube image load ${imageTag}"
                    sh "kubectl set image deployment/${env.K8S_DEPLOYMENT} ${env.IMAGE_NAME}=${imageTag}"
                }
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
