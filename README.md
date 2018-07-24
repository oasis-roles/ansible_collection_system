[![Build Status](https://travis-ci.org/oasis-roles/kdump.svg?branch=master)](https://travis-ci.org/oasis-roles/kdump)

KDUMP
===========

Role to setup Kernel dump files

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `kdump_version` - the version of kernel tools to install
* `kdump_conf_path` - the path to the remote host's kernel dump config file
* `kdump_become_user` - the user to run tasks as on the remote host
* `kdump_crash_path` - the path in which to store kernel crash dump files
* `kdump_core_collector_args` - parameters/options to pass into the core collector configuration (not configured by default)
* `kdump_dracut_device` - the location of a device to mount onto a specified mountpoint (not configured by default)
* `kdump_dracut_mountpoint` - the location a specified device is to be mounted (not configured by default)
* `kdump_dracut_filesystem_type` - the type of filesystem of the device in its initramfs (not configured by default)
* `kdump_dracut_filesystem_options` - configuration options for the filesystem (not configured by default)

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: setup_kdump-servers
  roles:
    - role: oasis-roles.kdump
      kdump_package: kexec-tools
      kdump_conf_path: /etc/kdump.conf
      kdump_become_user: root
      kdump_crash_path: /var/crash
      kdump_core_collector_args: makedumpfile -l --message-level 1 -d 31
      kdump_dracut_mountpoint: /mnt/vmcore
```

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>
