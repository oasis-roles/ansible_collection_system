library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/docker.git'
  molecule_role_name = 'docker'
  molecule_scenarios = ['default', 'rhel']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
