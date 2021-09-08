iptables
===========

Installs and configures iptables firewall and its rules.

Requirements
------------

Ansible 2.9 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `iptables_flush` - Default: `false`. Set to true in order to flush all
  existing rules before configuring the ones when you call this rule.
* `iptables_started` - Default: `true`. Set to false if you want the iptables
  service to be stopped after running this role.
* `iptables_enabled` - Default: `true`. Set to false if you want the service to
  be disabled after running this role.
* `iptables_rules` - Default: `[]`. A list of the rules to configure.
* `iptables_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `iptables_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: iptables-servers
  roles:
    - role: oasis_roles.system.iptables
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>
