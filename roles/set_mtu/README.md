set\_mtu
===========

Sets the MTU on a given IP connection through NetworkManager

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Role Variables
--------------

Currently the following variables are supported:

### General

* `set_mtu_value` - Default: 1400. The value to set the connection MTU
  to.
* `set_mtu_interface` - Default: eth0. The name of the connection in NetworkManager
  to set the MTU on. Note that this might not be the same as the physical connection
  name. If no connection with that name and type exists, one will be created, so
  be sure to get the value correct.
* `set_mtu_type` - Default: generic. The type of connection that you are setting
  the connection for. Values such as 'ethernet' are likely what you are looking
  for.
* `set_mtu_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `set_mtu_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: set_mtu-servers
  roles:
    - role: oasis_roles.system.set_mtu
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
