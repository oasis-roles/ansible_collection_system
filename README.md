[![Build Status](https://travis-ci.org/oasis-roles/package_updater.svg?branch=master)](https://travis-ci.org/oasis-roles/package_updater)

package_updater
===========

Basic description for package_updater

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `package_updater_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `package_updater_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: package_updater-servers
  roles:
    - role: oasis_roles.package_updater
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>