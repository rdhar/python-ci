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
        bat 'pytest --pep8 --junitxml=results.xml'
        // bat 'pytest -v'
        // bat 'python test_primes.py &&  test_random-module.py'
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
