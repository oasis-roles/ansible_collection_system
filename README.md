[![Build Status](https://travis-ci.com/oasis-roles/users_and_groups.svg?branch=master)](https://travis-ci.com/oasis-roles/users_and_groups)

users_and_groups
===========

Ansible role that creates/deletes groups and adds/removes users to those groups.

Requirements
------------

Ansible 2.6 or higher, however some options require up to 2.8

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General
* `users_and_groups_add_groups` - A list of groups to create on remote hosts
* `users_and_groups_remove_groups` - A list of groups to remove/delete from remote hosts
* `users_and_groups_add_users` - A list of users to add to specified groups
* `users_and_groups_remove_users` - A list of users to remove from specified groups
* `users_and_groups_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `users_and_groups_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

This example adds groups to remote hosts while removing others

```yaml
- hosts: users_and_groups-servers
  roles:
    - role: oasis_roles.users_and_groups
  vars:
    users_and_groups_add_groups:
      - "test_group1"
      - "test_group2"
      - "test_group3"
    users_and_groups_remove_groups:
      - "test_group4"
      - "test_group5"
```

This example adds groups then adds users to those new groups while removing them from other groups

```yaml
- hosts: users_and_groups-servers
  roles:
    - role: oasis_roles.users_and_groups
  vars:
    users_and_groups_add_groups:
      - "new_group1"
      - "new_group2"
    users_and_groups_add_users:
      - {name: "john_doe", groups: ["new_group1", "new_group2"]}
      - {name: "jane_smith", groups: ["new_group2"]}
    users_and_groups_remove_users:
      - {name: "jane_smith", groups: ["old_group1", "old_group2"]}
```

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>