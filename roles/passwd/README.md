[![Build Status](https://travis-ci.org/oasis-roles/passwd.svg?branch=master)](https://travis-ci.org/oasis-roles/passwd)

PASSWD
===========

This role changes the password for a user account.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `passwd_username` - REQUIRED - The username for which to change the password

* `passwd_password` - REQUIRED - Password hash to pass to Ansible's
  [user module](https://docs.ansible.com/ansible/latest/modules/user_module.html).
  IMPORTANT: See
  [Ansible's documentation](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-crypted-passwords-for-the-user-module)
  for properly and securely generating and storing this hash.

* `passwd_become` - Defaults to `true`. Whether or not to use the `become`
  feature of Ansible to gain admin privileges.  This will be necesssary for
  changing the `root` password, or the password of a user other than Ansible's
  `remote_user`.

* `passwd_become_user` - Defaults to `root`.  The user to sudo/become

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: passwd-servers
  roles:
    - role: oasis_roles.system.passwd
      passwd_username: root
      passwd_password: "<password_hash>"
      passwd_become: true
      passwd_become_user: root
```

License
-------

GPLv3

Author Information
------------------

David Roble <droble@redhat.com>
