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
				dir('openstack_provision') {
					checkout scm
				}
				virtualenv('.venv', ['molecule', 'shade'])
			}
		}
		stage('Run molecule in the environment') {
			steps {
				dir('openstack_provision') {
					venvSh('.venv', ['molecule test'])
				}
			}
		}
		stage('Run additional molecule scenario') {
			steps {
				dir('openstack_provision') {
					venvSh('.venv', ['molecule test -s with_volumes'])
				}
			}
		}
	}
}
