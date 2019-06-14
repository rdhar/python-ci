pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo 'START: Build'
        sh 'python --version'
        echo 'END: Build'
      }
    }

    stage('Test') {
      steps {
        echo 'START: Test'
        bat 'python test_primes.py'
        echo 'END: Build'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Nothing to Deploy'
      }
    }
  }
}
