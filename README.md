[![Build Status](https://travis-ci.com/oasis-roles/timezone.svg?branch=master)](https://travis-ci.com/oasis-roles/timezone)

timezone
===========

Basic description for timezone

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `timezone_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `timezone_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: timezone-servers
  roles:
    - role: oasis_roles.timezone
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>