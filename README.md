[![Build Status](https://travis-ci.com/oasis-roles/register_idm.svg?branch=master)](https://travis-ci.com/oasis-roles/register_idm)

register_idm
===========

Basic description for register_idm

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `register_idm_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `register_idm_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: register_idm-servers
  roles:
    - role: oasis_roles.register_idm
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>