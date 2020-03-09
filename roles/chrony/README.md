[![Build Status](https://travis-ci.org/oasis-roles/chrony.svg?branch=master)](https://travis-ci.org/oasis-roles/chrony)

CHRONY
===========

Role to setup the chronyd service

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `chrony_package` - The package name to install on remote hosts (set to `chrony` by default)
* `chrony_become_user` - The user to sign into when running commands on remote hosts (set to `root` by default)
* `chrony_servers` - A list of servers and their options to be used with the chrony service (set to public servers from the pool.ntp.org project by default)
* `chrony_driftfile_path` - Path in which to store files on the remote hosts that record the rate at which the systems' clocks gain/lose time (set to `/var/lib/chrony/drift` by default)
* `chrony_makestep_args` - arguments to pass into the makestep option for chrony (set to `1.0 3` by default)
* `chrony_enable_rtcsync` - Enable/disable kernel synchronization of the real-time clock (RTC) (set to `true` by default)
* `chrony_hwtimestamp_interfaces` - A list of interfaces in which to enable hardware timestamping. Entered as a string separating each interface with a space (not configured by default)
* `chrony_num_minsources` - The minimum number of select-able sources required to adjust the system clock (not configured by default)
* `chrony_ntp_client` - The local network from which to allow NTP client access (not configured by default)
* `chrony_keyfile_path` - Path to a key file on the remote hosts for NTP authentication (not configured by default)
* `chrony_logdir_path` - Path to a directory on the remote hosts in which to store log files (set to `/var/log/chrony` by default)
* `chrony_logged_information` - A list of information to log. Entered as a string separating each piece of information with a space (not configured by default)

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: chrony-servers
  roles:
    - role: oasis_roles.system.chrony
```

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>
