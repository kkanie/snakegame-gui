pipeline {
    agent any
    
    triggers {
        pollSCM('* * * * *')
    }
    
    stages{
        stage('Checkout'){
            steps{
                git 'https://github.com/kkanie/snakegame-gui.git'
            }
        }
        
        stage('Build'){
            steps{
                echo "Build..."
                sh '''
                cd build
                docker build -t snake -f ./Dockerfile .
                '''
            }
        }
        stage('Test'){
            steps{
                echo "Test..."
                sh '''
                cd test
                docker build -t test -f ./Dockerfile .
                '''
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploy..."
                sh '''
                docker-compose up
                docker-compose logs builder > log.txt
                docker-compose logs tester >> log.txt
                '''
            }
        }
        stage('Publish') {
            steps {
                echo "Publishing..."
                sh '''
                TIMESTAMP=$(date +%Y%m%d%H%M%S)
                tar -czf Artifact_$TIMESTAMP.tar.gz ./docker-compose.yml ./tests ./build ./log.txt
                docker compose down
                '''
                echo "Archiving the artifact..."
                archiveArtifacts artifacts: 'Artifact_*.tar.gz', fingerprint: true
            }
        }
    }
}
