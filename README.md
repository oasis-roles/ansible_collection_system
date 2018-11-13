[![Build Status](https://travis-ci.org/oasis-roles/localectl.svg?branch=master)](https://travis-ci.org/oasis-roles/localectl)

localectl
===========

This role will set systmctl; System Locale, VC Keymap, and X11 Layout settings

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `localectl_system_locale` - Defaults to LANG=en_US.UTF-8. Use this to set the desired language System locale designation for your system.

* `localectl_vc_keymap` - Defaults to US.  Use this to set the the desired VC Keymap designation for your system.

* `localectl_x11_layout` Defaults to US.  Use this to set the desired X11 Layout designation for your system.

* `reboot_become` - Defaults to 'true'.  Whether or not to use the    `become` feature of Ansible to gain admin privileges.`

* `reboot_become_user` - Defaults to 'root'.  The user to sudo/become

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: localectl-servers
  roles:
    - role: oasis-roles.localectl
      localectl_system_locale: LANG=en_US.UTF-8
      localectl_vc_keymap: us
      localectl_x11_layout: us
      localectl_become: true
      localectl_become_user: root
```

License
-------

GPLv3

Author Information
------------------

Author Name <stmurray@redhat.com>
