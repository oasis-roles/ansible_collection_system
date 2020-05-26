libvirtd
===========

Installs and configures libvirtd on a target system

Requirements
------------

Ansible 2.8 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `libvirtd_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `libvirtd_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: libvirtd-servers
  roles:
    - role: oasis_roles.system.libvirtd
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
