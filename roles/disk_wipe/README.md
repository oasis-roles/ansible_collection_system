[![Build Status](https://travis-ci.org/oasis-roles/disk_wipe.svg?branch=master)](https://travis-ci.org/oasis-roles/disk_wipe)

disk_wipe
===========

This role is not idempotent and it is recommended that it be run in an isolated
playbook to prevent disks from getting re-wiped during additional runs.
The role is intended to be used when you are preparing nodes for deployment
to ensure there is no stale, unwanted, or pre-existing data.

It will perform the following tasks:
1. Overwrite the disk(s) with zeros using shred command with specified byte size.
2. Erase the the disk signature(s) using wipefs.

IMPORTANT:
Extreme caution must be used to avoid running this role against the wrong disk(s).
Specifying the wrong disk or disks can lead to corruption and data loss.
Do not specify any disk that hosts your operating system or contains any data you may need.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `disk_wipe_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).

* `disk_wipe_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

* `disk_wipe_write_size` - Default: 200M.  The amount of bytes you would like to
  have overwritten on the disks. (suffixes like K, M, G accepted)

* `disk_wipe_disks` - Default: [] empty list.
  Specify the path(s) to disk block devices not partitions.
  Extreme caution must be used to avoid running this role against the wrong disk(s)
  Specifying the wrong disk or disks can lead to corruption and data loss.
  Do not specify any disk that hosts your operating system or contains any data you may need.

Dependencies
------------

None

Example Playbook
----------------

This example will run against a list of disks.

```yaml

- hosts: disk_wipe-servers
  roles:
    - role: oasis_roles.system.disk_wipe
      disk_wipe_write_size: 200M
      disk_wipe_disks:
        - /dev/vdb
        - /dev/vdc
        - /dev/vdd

```

License
-------

GPLv3

Author Information
------------------

Steven Murray <stmurray@redhat.com>
