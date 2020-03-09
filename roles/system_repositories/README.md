[![Build Status](https://travis-ci.org/oasis-roles/system_repositories.svg?branch=master)](https://travis-ci.org/oasis-roles/system_repositories)

Configure system repositories
===========

Configures and installs certain system repositories, primarily
targeting a yum or dnf based system.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 6+ or equivalent
Most versions of Fedora

Role Variables
--------------

Currently the following variables are supported:

### General

* `system_repositories_configs` - list of respoitories configurations
  in line with http://docs.ansible.com/ansible/latest/modules/yum_repository_module.html#yum-repository
  Most of the important options there are supported here. Any that are missing
  are welcome to be added through a PR.
* `system_repositories_repo_files` - list of remote URLs to repo files that
  should be downloaded to the destination directory. Use this argument with
  care for all the problems that can come with downloading remote URLs!
* `system_repositories_rpm_keys` - list of RPM keys that need to be installed
  to the system
* `system_repositories_validate_certs` - Defaults to true, but can be set to
  false if repo files or RPM keys are being downloaded via HTTPS from hosts where
  certificates are not valid on the target system

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: system_repositories_servers
  roles:
    - role: oasis_roles.system.system_repositories
      system_repositories_configs:
        - name: My Repo Name
          baseurl: http://somedomain.tld/some/path
      system_repositories_repo_files:
        - http://somedomain.tld/some/repo/my_repo.repo
        - http://otherdomain.net/path/to/repo_file.repo
```

License
-------

BSD

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
