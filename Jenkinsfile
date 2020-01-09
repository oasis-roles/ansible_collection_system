library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/reboot.git'
  molecule_role_name = 'reboot'
  molecule_scenarios = ['default']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
