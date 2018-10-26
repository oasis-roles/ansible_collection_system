[![Build Status](https://travis-ci.org/oasis-roles/update_ca_trust.svg?branch=master)](https://travis-ci.org/oasis-roles/update_ca_trust)

update_ca_trust
===========

Basic description for update_ca_trust

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `update_ca_trust_var_name` - var\_name description

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: update_ca_trust-servers
  roles:
    - role: oasis-roles.update_ca_trust
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>