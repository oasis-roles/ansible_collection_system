podTemplate(
  cloud: 'openshift',
  containers: [
    containerTemplate(name: 'jnlp',
      image: 'image-registry.openshift-image-registry.svc:5000/oasis/jenkins-agent-oasis:latest',
      args: '${computer.jnlpmac} ${computer.name}',
      envVars: [
        secretEnvVar(key: 'OASIS_RHSM_USERNAME', secretName: 'oasis-rhsm', secretKey: 'username'),
        secretEnvVar(key: 'OASIS_RHSM_PASSWORD', secretName: 'oasis-rhsm', secretKey: 'password'),
        secretEnvVar(key: 'OASIS_RHSM_POOL_IDS', secretName: 'oasis-rhsm', secretKey: 'pool_ids'),
        secretEnvVar(key: 'OASIS_RHSM_SERVER_HOSTNAME', secretName: 'oasis-rhsm', secretKey: 'hostname'),
        secretEnvVar(key: 'OCP_PULL_SECRETS_OFFLINE_TOKEN', secretName: 'oasis-ci-pull-secrets', secretKey: 'offline_token')
      ],
      alwaysPullImage: true)
  ]
) {
  node(POD_LABEL) {
    def collectionDir = 'ansible_collections/oasis_roles/system'
    def builders = [:]
    def String[] openstackTestEnvs
    checkout scm
    openstackTestEnvs = sh(
      script: 'tox --ansible-driver openstack -l',
      returnStdout: true
    ).trim().split()
    for (testEnv in openstackTestEnvs) {
      // bind testEnv into the local scope to ensure the correct value ends up in the build closure
      def boundTestEnv = testEnv
      def ghContext = "tox-ansible/${boundTestEnv}"
      githubNotify(
        credentialsId: 'gh-status-update',
        status: 'PENDING',
        description: 'Build Scheduled',
        context: ghContext
      )
      builders["${boundTestEnv}"] = {
        node(POD_LABEL) {
          stage("Checkout ${boundTestEnv}") {
            sh "mkdir -p ${collectionDir}"
            dir(collectionDir) {
              checkout scm
            }
          }
          stage("Test ${boundTestEnv}") {
            dir(collectionDir) {
              warnError(message: "tox env ${boundTestEnv} failed") {
                gitStatusWrapper(
                  credentialsId: 'gh-status-update',
                  description: 'Building',
                  failureDescription: 'Build Failed',
                  successDescription: 'Build Succeeded',
                  gitHubContext: ghContext
                ) { sh "tox -e '${boundTestEnv}'" }
              }
            }
          }
        }
      }
    }
    throttle(['throttled']) {
      parallel builders
    }
  }
}
