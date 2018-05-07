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
				dir('system_repositories') {
					checkout scm
				}
				virtualenv('.venv', ['molecule', 'shade'])
			}
		}
		stage('Run molecule in the environment') {
			steps {
				dir('system_repositories') {
					venvSh('.venv', ['molecule test -s openstack'])
				}
			}
		}
	}
}
