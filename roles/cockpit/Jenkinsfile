library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/cockpit.git'
  molecule_role_name = 'cockpit'
  molecule_scenarios = ['openstack']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
