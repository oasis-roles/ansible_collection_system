[![Build Status](https://travis-ci.com/oasis-roles/sshd.svg?branch=master)](https://travis-ci.com/oasis-roles/sshd)

sshd
===========

Installs and configures basic options for sshd

Requirements
------------

Ansible 2.8 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `sshd_allow_password_login` - Default: false. If set to false, then password
  auth logins will be disabled. Set to true to allow users to login with
  passwords.
* `sshd_allow_root_login` - Default: true. If set to false, then the root user
  will not be allowed to login. Set to true to enable direct root access.
* `sshd_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `sshd_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: sshd-servers
  roles:
    - role: oasis_roles.system.sshd
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
