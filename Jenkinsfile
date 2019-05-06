library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/system_repositories.git'
  molecule_role_name = 'system_repositories'
  molecule_scenarios = ['openstack']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
