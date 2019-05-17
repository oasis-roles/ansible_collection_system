library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/{{ role_name }}.git'
  molecule_role_name = '{{ role_name }}'
  molecule_scenarios = ['docker', 'openstack']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
