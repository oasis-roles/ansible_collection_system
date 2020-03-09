[![Build Status](https://travis-ci.org/oasis-roles/hostname.svg?branch=master)](https://travis-ci.org/oasis-roles/hostname)

Hostname
===========

Sets the hostname to a specified value, and optionally injects that value and
other aliases into the /etc/hosts file

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `hostname` - The (probably FQDN) hostname to set for the host
* `hostname_aliases` - An optional array of shortened hostnames to set into
  the /etc/hosts file.
* `hostname_inject_hosts_files` - Set to false if you do not wish to inject
  lines into the hosts files. Defaults to `true`.
* `hostname_become` - Set to false if you do not wish to sudo/become a
  privileged user for the hostname injection (does not affect becoming root
  to set the hostname). Defaults to `true`.
* `hostname_become_user` - Set to the value of user who should inject the lines
  into the hosts files. Defaults to `root`.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: hostname-servers
  roles:
    - role: oasis_roles.system.hostname
      hostname: dev.example.com
      hostname_aliases:
        - dev
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
