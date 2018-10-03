[![Build Status](https://travis-ci.org/oasis-roles/reboot.svg?branch=master)](https://travis-ci.org/oasis-roles/reboot)

REBOOT
===========

This role performs a reboot of the target system

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `reboot_seconds_before_reboot` - Defaults to 2.  Delay (in seconds) after issuing the reboot command before the reboot will begin. This allows ansible to
terminate it's ssh session before sshd is shut down during reboot.

* `reboot_wait_for_connection_delay` - Defaults to 60.  Time before ansible
starts polling the system after the reboot command has been issued.  Please be careful lowering this value as if it is too low the role may fail.

* `reboot_wait_for_connection_timeout` - Defaults to 300.  The time this role
will wait for connection to the target before exiting.

* `reboot_become` - Defaults to 'true'.  Whether or not to use the `become`
  feature of Ansible to gain admin privileges.

* `reboot_become_user` - Defaults to 'root'.  The user to sudo/become

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: reboot-servers
  roles:
    - role: oasis-roles.reboot
      reboot_seconds_before_reboot: "2"
      reboot_wait_for_connection_delay: "60"
      reboot_wait_for_connection_timeout: "300"
      reboot_become: true
      reboot_become_user: root
```

License
-------

GPLv3

Author Information
------------------

Steve Murray <stmurray@redhat.com>
