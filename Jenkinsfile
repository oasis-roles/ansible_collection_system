#!groovy
@Library('jenkinsfile-helpers') _

pipeline {
	agent { label 'master' }
	options {
		disableConcurrentBuilds()
	}
	stages {
		stage('Fetch code and setup environment') {
			steps {
				cleanWs()
				dir('open_stack_provision') {
					checkout scm
				}
				virtualenv('.venv', ['molecule', 'shade'])
			}
		}
		stage('Run molecule in the environment') {
			steps {
				dir('open_stack_provision') {
					venvSh('.venv', ['molecule test'])
				}
			}
		}
	}
}
