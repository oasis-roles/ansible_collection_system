[![Build Status](https://travis-ci.org/oasis-roles/localectl.svg?branch=master)](https://travis-ci.org/oasis-roles/localectl)

localectl
===========

Basic description for localectl

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `localectl_var_name` - var\_name description

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: localectl-servers
  roles:
    - role: oasis-roles.localectl
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>