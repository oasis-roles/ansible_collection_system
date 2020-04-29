network\_scripts
===========

Basic description for network\_scripts

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `network_scripts_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `network_scripts_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.
* `network_scripts_dest_path` - Default: /etc/sysconfig/network-scripts. Set
  this to a different path if your distro puts scripts in a different location
  or if you want to use the scripts in another manner (e.g. to upload to a VM).
  The directory must already exist prior to calling this role
* `network_scripts_restart` - Default: false. Set this to true if networking
  should be restarted after detecting a change in the uploaded scripts.
* `network_scripts_clear_existing` - Default: false. Set this to true if you
  want this role to remove existing script files in the target location that
  match the passed values in the next variable.
* `network_scripts_clear_patterns` - Default: `['ifcfg-*', 'route-*']`. A list
  of shell-expanded wildcard patterns for scripts to remove if `network_scripts_clear_existing`
  is set to true.
* `network_scripts_nics` - Default: `[]`. A list of the network scripts to create.
  Takes a form like the following:

```yaml
network_scripts_nics:
  - filename: ifcfg-eth0
    NAME: eth0
    DEVICE: eth0
    TYPE: Ethernet
    BOOTPROTO: static
    IPADDR: 192.168.1.10
    GATEWAY: 192.168.1.1
    NETMASK: 255.255.255.0
    DEFROUTE: !!str yes
    IPV6INIT: !!str no
    ONBOOT: !!str yes
    DNS1: 8.8.8.8
```
  All supported arguments are passed into the template file and match arguments
  in the ifcfg syntax of the same name. Check the file `templates/ifcfg` for
  any that are supported. If the option you need isn't present, open an issue
  or a PR for it

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: network_scripts-servers
  roles:
    - role: oasis_roles.system.network_scripts
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
