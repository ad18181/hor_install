pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                sh '''
                curl -fsSL https://raw.githubusercontent.com/ZupIT/horusec/master/deployments/scripts/install.sh | bash -s latest
                horusec version
                horusec start -p="./src" -o json --json-output-file ${WORKSPACE}/report.json --disable-docker="true"
                '''
                
            }
        }
    }
}
