network_bridge
===========

Basic description for network_bridge

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `network_bridge_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `network_bridge_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: network_bridge-servers
  roles:
    - role: oasis_roles.system.network_bridge
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>