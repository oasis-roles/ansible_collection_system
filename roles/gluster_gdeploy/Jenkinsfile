library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/gluster_gdeploy.git'
  molecule_role_name = 'gluster_gdeploy'
  molecule_scenarios = ['default']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
