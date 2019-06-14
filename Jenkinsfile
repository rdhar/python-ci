pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo 'Nothing to Build'
      }
    }

    stage('Test') {
      steps {
        echo 'START: Test'
        bat 'pytest'
        bat 'pytest --junitxml=results.xml'
        echo 'END: Test'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Nothing to Deploy'
      }
    }
  }
}
