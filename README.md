[![Build Status](https://travis-ci.org/oasis-roles/wipefs.svg?branch=master)](https://travis-ci.org/oasis-roles/wipefs)

wipefs
===========

Basic description for wipefs

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `wipefs_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `wipefs_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: wipefs-servers
  roles:
    - role: oasis_roles.wipefs
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>