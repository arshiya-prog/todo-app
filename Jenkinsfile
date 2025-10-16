pipeline {
    agent any

    environment {
        APP_NAME = "todo-app"
        IMAGE_NAME = "todo-app:latest"
        KUBE_DIR = "kubernetes"
        MINIKUBE_DOCKER_ENV = "eval \$(minikube docker-env)"
    }

    stages {

        stage('Prepare') {
            steps {
                echo "Cleaning previous builds..."
                sh 'docker image rm -f $IMAGE_NAME || true'
            }
        }

        stage('Set Docker Env to Minikube') {
            steps {
                echo 'Configuring Docker to use Minikube Docker daemon...'
                script {
                    def dockerEnv = sh(script: "${MINIKUBE_DOCKER_ENV} && env", returnStdout: true).trim()
                    def envVars = dockerEnv.split("\n").collect { it.split("=", 2) }.findAll { it.size() == 2 }
                    envVars.each { envVar ->
                        env[envVar[0]] = envVar[1]
                    }
                }
            }
        }

        stage('Build Docker Image Inside Minikube') {
            steps {
                echo 'Building Docker image using Minikube Docker daemon...'
                sh '''
                    eval $(minikube docker-env)
                    /usr/local/bin/docker build -t $IMAGE_NAME .
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
                echo 'Waiting for pods to be ready...'
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
            echo "❌ Deployment failed. Check logs for details."
        }
    }
}
