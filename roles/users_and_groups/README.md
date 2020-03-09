[![Build Status](https://travis-ci.com/oasis-roles/users_and_groups.svg?branch=master)](https://travis-ci.com/oasis-roles/users_and_groups)

users_and_groups
===========

Ansible role that manages groups and users

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

Sub-field format guide: `parameter` - [input type] (application scenario) Description. **Importance|Default value**

**OPTIONAL** tags means there is no default value.

* `users_and_groups_add_modify_groups` - A list of groups to create/modify on remote hosts. Each list entry has the following parameters (in depth descriptions of some parameters can be found in the [group module docs](https://docs.ansible.com/ansible/latest/modules/group_module.html)):
  * `name` - [string] (add|modify) The name of the group. **REQUIRED**
  * `gid` - [int] (add|modify) GID to set for the group. **OPTIONAL**
  * `local` - [bool] (add) Forces the use of "local" command alternatives on platforms that implement it. **Default is `false`**
  * `non_unique` - [bool] (add|modify) Allows admin to change the GID to a non-unique value. Requires gid to be defined. **Default is `false`**
  * `system` - [bool] (add) Indicates the group is a system group if set to `true`. **Default is `false`**
* `users_and_groups_remove_groups` - A list of groups to remove/delete from remote hosts
* `users_and_groups_add_modify_users` - A list of users to create/modify on remote hosts. Each list entry has the following parameters (in depth descriptions of some parameters can be found in the [user module docs](https://docs.ansible.com/ansible/latest/modules/user_module.html)):
  * `name` - [string] (add|modify) The name of the user to manage. **REQUIRED**
  * `authorization` - [string list] (add|modify) Sets the authorization of the user. **OPTIONAL**
  * `comment` - [string] (add|modify) Sets the description of the user account. **OPTIONAL**
  * `create_home` - [bool] (add) Unless set to `false`, a home directory will be made for the user upon creation. **Default is `true`**
  * `expires` - [float] (add|modify) An expiry time for the user in epoch. Specify a negative value to remove an existing expiry time. **OPTIONAL**
  * `force` - [bool] (add|modify) Used with `generate_ssh_key` to force the overwrite of an existing ssh key. **Default is `false`**
  * `generate_ssh_key` - [bool] (add|modify) Whether or not to generate a ssh key for the specified user. Will not overwrite an existing key unless `force: true` is specified. **Default is `false`**
  * `home` - [path] (add) Set the user's home directory **OPTIONAL**
  * `local` - [bool] (add) Forces the use of "local" command alternatives on platforms that implement it. **Default is `false`**
  * `login_class` - [string] (add) Set the user's login class. **OPTIONAL**
  * `move_home` - [bool] (modify) When `true` and `home: ` is defined, attempts to move the user's old home to the new path specified in `home: `. **Default is `false`**
  * `non_unique` - [bool] (modify) Allows the user's UID to change to a non-unique value. **Default is `false`**
  * `password` - [string] (add|modify) Set the user's password to this crypted value. See the [ansible docs](https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module) for generating password values. **OPTIONAL**
  * `password_lock` - [bool] (add|modify) Lock the user's password. **OPTIONAL**
  * `profile` - [string list] (add|modify) Sets the profile of the user. **OPTIONAL**
  * `role` - [string list] (add|modify) Sets the role of the user. **OPTIONAL**
  * `seuser` - [string] (add|modify) Sets the seuser type on selinux enabled systems. **OPTIONAL**
  * `shell` - [string] (add|modify) Sets the user's shell. **OPTIONAL**
  * `skeleton` - [string] (add) Set a home skeleton directory. Requires `create_home` to be defined. **OPTIONAL**
  * `ssh_key_bits` - [int] (add|modify) Specify number of bits in SSH key to create. **OPTIONAL**
  * `ssh_key_comment` - [string] (add|modify) Description for a SSH key. **OPTIONAL**
  * `ssh_key_file` - [path] (add|modify) Specify the SSH key filename. Relative filenames are relative to the user's home directory. **Default is `.ssh/id_rsa`**
  * `ssh_key_passphrase` - [string] (add|modify) Set a passphrase for a SSH key. **OPTIONAL**
  * `ssh_key_type` - [string] (add|modify) The type of SSH key to generate. **Default is `"rsa"`**
  * `system` - [bool] (add) When `true`, the user becomes a system account. **Default is `false`**
  * `uid` - [int] (add|modify) Sets the UID of the user. **OPTIONAL**
  * `update_password` - [string] (add|modify) When `"always"`, user's password will be updated if `password` differs from the current password. When `"on_create"`, user's password will be set to `password` for newly created users only. **Default is `"always"`**
* `users_and_groups_remove_users` - A list of users to remove/delete from remote hosts. Each list entry has the following parameters (in depth descriptions of some parameters can be found in the [user module docs](https://docs.ansible.com/ansible/latest/modules/user_module.html))
  * `name` - [string] The name of the user to be removed. **REQUIRED**
  * `force` - [bool] Forces the removal of the user and associated directories when `true`. **Default is `false`**
  * `remove` - [bool] Attempts to remove directories associated with the user when `true`. **Default is `false`**
* `users_and_groups_add_group_members` - A list of users to grant/modify membership to specified groups. Each list entry has the following parameters (in depth descriptions of some parameters can be found in the [user module docs](https://docs.ansible.com/ansible/latest/modules/user_module.html))
  * `name` - [string] (add|modify) Name of the user whose group membership is being modified. **REQUIRED**
  * `append` - [bool] (add|modify) When `true`, adds specified groups to current membership. When `false`, replaces current membership with specified groups. **Default is `false`**
  * `primary_group` - [string] (add|modify) Assign a primary group for the specified user. **OPTIONAL** (listed as `group` in module docs)
  * `groups` - [string list] (add|modify) List of groups user will become a member of. **REQUIRED**
* `users_and_groups_remove_group_members` - A list of users to revoke membership to specified groups. Each list entry has the following parameters (in depth descriptions of some parameters can be found in the [user module docs](https://docs.ansible.com/ansible/latest/modules/user_module.html))
  * `name` - [string] Name of the user whose group membership is being modified. **REQUIRED**
  * `primary_group` - [string] Reassign a primary group for the specified user. **OPTIONAL** (listed as `group` in module docs)
  * `groups` - [string list] List of groups user will be removed from. **REQUIRED**
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

This example adds/modifies groups to remote hosts while removing/deleting others

```yaml
- hosts: users_and_groups-servers
  roles:
    - role: oasis_roles.system.users_and_groups
  vars:
    users_and_groups_add_modify_groups:
      - name: "test_group1"
        gid: 30
        system: true
      - name: "test_group2"
        gid: 31
        local: true
      - name: "test_group3"
    users_and_groups_remove_groups:
      - "test_group4"
      - "test_group5"
```

This example adds/modifies users to the remote host while removing/deleting others

```yaml
- hosts: users_and_groups-servers
  roles:
    - role: oasis_roles.system.users_and_groups
  vars:
    users_and_groups_add_modify_users:
      - name: "john_doe"
        comment: "This is John Doe's user description"
        password: "EnCrYpTeD Pa$$W0Rd"
        uid: 1200
      - name: "laura_smith"
        role:
          - administrator
          - tester
          - developer
        ssh_key_bits: 256
        ssh_key_file: /path/to/ssh/key/file
        ssh_key_passphrase: "my_SSH^passPhrasE"
        system: true
    users_and_groups_remove_users:
      - name: "brad_cooper"
        remove: true
        force: true
      - name: "thomas"
```

This example adds new members to groups while removing members from other groups. When removing "alex" from "old_group2", the user's `primary_group` is reassigned as the user's previous `primary_group` was old_group2

```yaml
- hosts: users_and_groups-servers
  roles:
    - role: oasis_roles.system.users_and_groups
  vars:
    users_and_groups_add_group_members:
      - name: "john_doe"
        groups:
          - "group1"
          - "group2"
        primary_group: "group1"
        append: false
      - name: "jane_smith"
        groups:
          - "new_group2"
        append: true
    users_and_groups_remove_group_members:
      - name: "jane_smith"
        groups:
          - "old_group1"
          - "old_group2"
      - name: "alex"
        groups:
          - "old_group2"
        primary_group: "group2"
```

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>