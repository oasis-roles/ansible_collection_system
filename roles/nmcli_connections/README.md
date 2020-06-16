nmcli\_connections
===========

Create or remove connections with NetworkManager. Hopefully it's
obvious that this only works on systems where network connections
are actually managed by NetworkManager! If your system doesn't use
it, then this is not the role you are looking for. Maybe check out
the network\_scripts role.

It should be noted that, due to issues with the nmcli module in Ansible 2.9
and earlier, this module will not properly report "changed" for the creation
or removal of the connection. If this is resolved in later versions of
Ansible than this role can be updated so it does not always report
changed as `false`, the way it currently does. The relevant bug is on
[github](https://github.com/ansible-collections/community.general/issues/481)
and should be tracked. When it's resolved, then this role should be
updated.

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `nmcli_connections` - Default: []. A list of connections to create. Each
  element in the list needs to be in the attributes:
  * `ifname` - **Required**. The name of the interface to use in creating
    the connection.
  * `conn_name` - **Default: ifname**. The NetworkManager compatible name
    for the connection you're trying to create
  * `type` - **Default: 'ethernet'**. The type of connection to create
  * `state` - **Default: 'present'**. "present" or "absent" to tell the
    module what action to take
* `nmcli_connections_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `nmcli_connections_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: nmcli_connections-servers
  roles:
    - role: oasis_roles.system.nmcli_connections
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
