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
				scm checkout
				virtualenv('molecule', ['molecule', 'shade'])
			}
		}
		stage('Run molecule in the environment') {
			steps {
				venvSh('molecule', ['molecule test -s openstack'])
			}
		}
	}
}
