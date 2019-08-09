library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/vmware_provision.git'
  molecule_role_name = 'vmware_provision'
  molecule_scenarios = ['default']
  properties = [pipelineTriggers([cron('H H * * *')])]
}