[![Build Status](https://travis-ci.org/oasis-roles/reboot.svg?branch=master)](https://travis-ci.org/oasis-roles/reboot)

reboot
===========

Basic description for reboot

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `reboot_var_name` - var\_name description

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: reboot-servers
  roles:
    - role: oasis-roles.reboot
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>