pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo "---Checkout----"
                git url: "https://github.com/EugenMol/test_jenkins.git", branch: "main"
                sh '''
                ls -la
                '''
                }
            }
        stage('Check_Dockerfile') {
            steps {
                echo "-----Check_Dockerfile-----"
                sh '''
                    docker info
                    docker run --rm -i hadolint/hadolint < Dockerfile
                    echo $?
                '''
            }
        }
        stage('Build_Docker_Image') {
            steps {
                echo "---Build_Docker_Image---"
                sh '''
                    docker build -t eugenmol86/test_docker_image .
                    echo $?
                '''
            }
        }
        stage('Docker_Run') {
            steps {
                echo "----Docker_Run----"
                sh '''
                    docker run -d --rm -p 8081:80 --name test-jenkins eugenmol86/test_docker_image
                    echo $?
                    sleep 10
                    curl http://127.0.0.1:8081
                    docker stop $(docker ps -qf 'name=test-jenkins')
                '''
            }
        }
        stage('Docker_Push') {
            steps {
                echo "----Docker_Push----"
                sh '''
                    docker login -u eugenmol86 -p EO01mini!
                    docker push eugenmol86/test_docker_image
                    echo $?
                '''
            }
        }
        stage('Deploying app in K8s') {
            steps {
                withKubeConfig([credentialsId: 'user-k8s') {
                    sh 'kubectl apply -f deployment.yml'
                }
            }
        }
        stage('Test'){
            steps {
               echo "-----Test------"
            }
        }
        stage('Deploy') {
            steps {
                echo "-----Deploy----"
            }
        }
    }
}
