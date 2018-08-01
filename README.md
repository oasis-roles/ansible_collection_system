[![Build Status](https://travis-ci.org/oasis-roles/hostname.svg?branch=master)](https://travis-ci.org/oasis-roles/hostname)

ROLE NAME
===========

Basic description for hostname

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `hostname_var_name` - var\_name description

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: hostname-servers
  roles:
    - role: oasis-roles.hostname
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>