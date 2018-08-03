[![Build Status](https://travis-ci.org/oasis-roles/nfs_server.svg?branch=master)](https://travis-ci.org/oasis-roles/nfs_server)

ROLE NAME
===========

Basic description for nfs_server

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `nfs_server_var_name` - var\_name description

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: nfs_server-servers
  roles:
    - role: oasis-roles.nfs_server
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>