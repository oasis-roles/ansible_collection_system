[![Build Status](https://travis-ci.com/oasis-roles/vmware_provision.svg?branch=master)](https://travis-ci.com/oasis-roles/vmware_provision)

vmware_provision
===========

Provisions VMWare hosts and adds them to inventory groups

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `vmware_provision_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `vmware_provision_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: vmware_provision-servers
  roles:
    - role: oasis_roles.vmware_provision
```

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>