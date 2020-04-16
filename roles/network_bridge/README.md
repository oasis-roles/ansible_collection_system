network\_bridge
===========

Basic description for network\_bridge

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent, for Fedora based
system

Tries to work for Ubuntu, but seems to have issues with DHCP addresses
on those hosts.

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
* `network_bridge_devices` - Default: `{}`. A dictionary that takes the form
of:
```yaml
bridge_name:
  device: eth0
  nm_controlled: "no"  # optional, default "yes"
  onboot: "yes"  # optional, default "yes"
  ipaddr: 192.168.1.1  # optional, if ignored, DHCP will be set
  netmask: 255.255.255.0  # required if ipaddr set, else ignored
  gateway: 10.0.0.1  # required if ipaddr set, else ignored
  ipv6: 1::1  # optional, no IPv6 configured if absent
  dns:  # optional
    - 8.8.8.8
    - 8.8.4.4
```

Dependencies
------------

To run on an Ubuntu system, the remote system will need the Python YAML
library.

Example Playbook
----------------

```yaml
- hosts: network_bridge-servers
  roles:
    - role: oasis_roles.system.network_bridge
  vars:
    network_bridge_devices:
      br0:
        device: eth0
        ipaddr: 192.168.1.10
        netmask: 255.255.255.0
        gateway: 192.168.1.1
      br1:
        device: eth1
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
