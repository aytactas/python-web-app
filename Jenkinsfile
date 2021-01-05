pipeline {
    agent any

    
    stages {
        stage('Git') {
            steps {
                git credentialsId: 'Aytac', url: 'https://github.com/aytactas/python-web-app'
            }
        }
        stage('Build Docker Image'){
            steps {
                sh '''
                docker build . -t my-simple-web-app
                '''
            }
        }
                stage('Run Docker Image'){
            steps {
                sh '''
                docker run -d -p 5000:8085 my-simple-web-app
                '''
            }
        }
                        


        
    }
}
