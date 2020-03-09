[![Build Status](https://travis-ci.com/oasis-roles/molecule_docker_ci.svg?branch=master)](https://travis-ci.com/oasis-roles/molecule_docker_ci)

molecule_docker_ci
===========

Creates and destroys Docker containers running on the local system for use
in a molecule playbook. Can also be used to create and destroy docker containers
in a more general sense, but that is not the purpose of this role nor is it a
particularly supported use case

This role is adapted from the built-in playbooks created by molecule's init methods.
By externalizing this functionality as a role, updates to the playbooks can be made
in one central location and updated to account for bugs, etc, etc. Basically, for
all the same reasons that playbooks should be composed by roles and that Ansible
Galaxy exists at all are the reasons this role should be used for provisioning and
destroying resources from Molecule playbooks.

To use the role, you'll need to add it to your requirements.yml file or however
you are pulling Ansible roles during your test execution.

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `molecule_docker_ci_state` - Default: present. Valid options are 'present' and
'absent'. If set to 'absent', it will tear down the molecule instances. Set to
'present' in order to create them.

All other variables are pulled from the molecule context or the molecule.yml file
in your scenario. For that reason, this role is very tightly integrated with Molecule
and shouldn't really be used elsewhere.

Dependencies
------------

Molecule

Example Playbook
----------------

The following two playbooks should be sufficient to bring up and tear down
containers in your molecule.yml

create.yml
```yaml
- hosts: localhost
  roles:
    - role: oasis_roles.system.molecule_docker_ci
```

destroy.yml
```yaml
- hosts: localhost
  roles:
    - role: oasis_roles.system.molecule_docker_ci
      molecule_docker_ci_state: absent
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
