[![Build Status](https://travis-ci.com/oasis-roles/users_and_groups.svg?branch=master)](https://travis-ci.com/oasis-roles/users_and_groups)

users_and_groups
===========

Basic description for users_and_groups

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `users_and_groups_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `users_and_groups_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: users_and_groups-servers
  roles:
    - role: oasis_roles.users_and_groups
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>