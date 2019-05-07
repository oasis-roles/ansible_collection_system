library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/kdump.git'
  molecule_role_name = 'kdump'
  molecule_scenarios = ['openstack']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
