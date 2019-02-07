library('oasis-pipeline')

oasisMultistreamMoleculePipeline {
  upstream_git_url = 'https://github.com/oasis-roles/rhsm.git'
  molecule_role_name = 'rhsm'
  molecule_scenarios = ['basic_subscription', 'sub_unsub', 'release_set_unset']
  properties = [pipelineTriggers([cron('H H * * *')])]
}
