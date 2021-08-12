rp\_filter
===========

Sets the kernel parameter rp\_filter value. Will also set the value
in /etc/sysctl.d/20-rp\_filter.conf so that it will persist across
reboots.

In future, that filepath might be configurable.

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Role Variables
--------------

Currently the following variables are supported:

### General

* `rp_filter_value` - Default: '0'. The value to set in the rp\_filter
  of the kernel.
* `rp_filter_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `rp_filter_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: rp_filter-servers
  roles:
    - role: oasis_roles.system.rp_filter
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
