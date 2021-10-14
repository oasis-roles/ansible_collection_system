
sudoers
===========

Basic description for sudoers

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `sudoers_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `sudoers_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.
* `sudoers` - Defaults: `[]`. A list of users who should be given
  sudo access but still be required to use passwords
* `sudoers_no_password` - Defaults: `[]`. A list of users who should be given
  sudo access without the need to enter passwords.
* `sudoers_groups` - Defaults: `[]`. A list of groups that should be
  given sudo access, but be required to enter passwords.
* `sudoers_groups_no_password` - Default: `[]`. A list of groups that should
  be given sudo access without the need to enter passwords.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: sudoers-servers
  roles:
    - role: greg_hellings.sudoers
  vars:
    sudoers_password:
      - greg
      - jenkins
    sudoers_groups_no_password:
      - wheel
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
