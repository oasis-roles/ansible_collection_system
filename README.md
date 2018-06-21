[![Build Status](https://travis-ci.org/oasis-roles/cockpit.svg?branch=master)](https://travis-ci.org/oasis-roles/cockpit)

COCKPIT
===========

Installs cockpit to a set of hosts and starts the service

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `cockpit_version` - the cockpit version the user wants to have installed and run on their instance

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: cockpit-servers
  roles:
    - role: cockpit
```

License
-------

GPLv3

Author Information
------------------

Author Name <authoremail@domain.net>
