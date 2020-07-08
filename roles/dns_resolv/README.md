dns_resolv
===========

Adds nameservers to a system's resolv.conf file

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `dns_resolv_servers` - Default: `['208.67.222.222', '1.1.1.1', '8.8.8.8']`.
  A list of the IP addresses for DNS servers to set as the default servers
  for the system.
* `dns_resolv_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `dns_resolv_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: dns_resolv-servers
  roles:
    - role: oasis_roles.system.dns_resolv
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
