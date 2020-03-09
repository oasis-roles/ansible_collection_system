[![Build Status](https://travis-ci.org/oasis-roles/package_updater.svg?branch=master)](https://travis-ci.org/oasis-roles/package_updater)

package_updater
===========

This role:
Updates all packages. Updating specific packages is not supported.
Is not idempotent.
Intended to be used during initial installation of software.
Will perform the common "Update all packages" step found in many product installation guides.


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
This example would update all packages to the latest version and update the cache.

```yaml
- hosts: package_updater-servers
  roles:
    - role: oasis_roles.system.package_updater
```

License
-------

GPLv3

Author Information
------------------

Steven Murray <stmurray@redhat.com>
