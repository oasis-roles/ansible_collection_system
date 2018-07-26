[![Build Status](https://travis-ci.org/oasis-roles/chrony.svg?branch=master)](https://travis-ci.org/oasis-roles/chrony)

ROLE NAME
===========

Basic description for chrony

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `chrony_var_name` - var_name description

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: chrony-servers
  roles:
    - role: chrony
```

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>
