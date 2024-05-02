pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                // Установка зависимостей
                sh 'echo "Settings up requirements"'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Data Creation') {
            steps {
                sh 'python3 data_creation.py'
            }
        }

        stage('Data Preprocessing') {
            steps {
                sh 'python3 model_preprocessing.py'
            }
        }

        stage('Model Preparation') {
            steps {
                sh 'python3 model_preparation.py'
            }
        }

        stage('Model Testing') {
            steps {
                sh 'python3 model_testing.py'
            }
        }

    }

    post {
        always {
            echo 'Cleaning up...'
            cleanWs()
        }
        success {
            sh 'echo "Pipeline completed successfully"'
        }
        failure {
            echo 'Pipeline failed.'
            sh 'echo "Pipeline failed"'
        }
    }
}
