[![Build Status](https://travis-ci.org/oasis-roles/reboot.svg?branch=master)](https://travis-ci.org/oasis-roles/reboot)

Reboot
======

This role reboots systems in plays where it is invoked.

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

These role variables directly correspond to the similarly-named module parameters of the
[reboot](https://docs.ansible.com/ansible/latest/modules/reboot_module.html) module, and
default to the same default values seen in the reboot module documentation.

All role variables are optional.

* `reboot_connect_timeout` - Maximum seconds to wait for a successful connection to the managed
  hosts before trying again. If unspecified, the default setting for the underlying connection
  plugin is used.

* `reboot_msg` - Message to display to users before reboot.

* `reboot_post_delay` - Seconds to wait after the reboot was successful and the connection was
  re-established.  This is useful if you want wait for something to settle despite your connection
  already working.

* `reboot_pre_delay` - Seconds for shutdown to wait before requesting reboot.
  On Linux, macOS, and OpenBSD this is converted to minutes and rounded down. If less than 60,
  it will be set to 0.  On Solaris and FreeBSD this will be seconds.

* `reboot_timeout` - Maximum seconds to wait for machine to reboot and respond to a test command
  once the connection is established.

* `reboot_search_paths` - List of paths to search for the `shutdown` command, in the event that
  the `reboot` module defaults are insufficient.

* `reboot_test_command` - Command to run on the rebooted host and expect success from to
  determine the machine is ready for further tasks.

### Privilege Escalation

Privilege escalation as `root` is enabled by default.

* `reboot_become` - Defaults to 'true'.  Whether or not to use the `become`
  feature of Ansible to gain admin privileges.

* `reboot_become_user` - Defaults to 'root'.  The user to sudo/become

#### Deprecated variables

These variables were used in earlier versions of the reboot role, and are now mapped to the
newer variable names based on those of the reboot module above. Support for these variables
may be removed in a future version of the reboot role, and users are encouraged to switch to
the new variable names. Defaults for these variables have been altered to match the defaults
used in the reboot module.

* `reboot_seconds_before_reboot` - Value will be used in the `reboot_pre_delay` variable.
  This value was previously in seconds, but is now bound by the constraints of the
  `reboot_pre_delay` variable on Linux, macOS, and OpenBSD. On these platforms, values less than
   60 seconds will be rounded down to 0, includng the previous default value of `2`.
* `reboot_wait_for_connection_delay` - Value will be used in the `reboot_post_delay` variable.
  The previous behavior was to delay *before* waiting for the connection to resume, but the new
  behavior is slightly different, in that it will now wait *after* the connection resumes. In
  both cases, the system is allowed this  much time, in seconds, to quiesce before the reboot
  task finishes. The previous default of `60` seconds has been changed to `0` seconds.
* `reboot_wait_for_connection_timeout` - Value will be used in the `reboot_timeout` variable.
  This variable serves the same function as in previous versions of this role, but the default
  has been changed from `300` seconds to `600` seconds.

In cases where both the current variable and deprecated variables are used, variable precedence
is undefined. Please update to using the current variables.

Notes
-----

For compatibility with older versions of ansible (2.4 and higher, but less than 2.8), version
[1.0.0](https://github.com/oasis-roles/reboot/releases/tag/1.0.0) of this role can be used.

Dependencies
------------

None

Example Playbooks
-----------------

Rebooting a system when ansible is already a privileged user:

```yaml
- hosts: reboot-servers
  roles:
    - role: oasis_roles.system.reboot
```

Explicitly `become` root to reboot:

```yaml
- hosts: reboot-servers
  roles:
    - role: oasis_roles.system.reboot
  vars:
      reboot_become: true
      reboot_become_user: root
```

Using the deprecated vars:

```yaml
- hosts: reboot-servers
  roles:
    - role: oasis_roles.system.reboot
  vars:
    # Wait two minutes before requesting reboot
    # Becomes the "reboot_pre_delay" variable
    reboot_seconds_before_reboot: 120
    # Give the system 30 seconds to quiesce after rebooting.
    # Becomes the "reboot_post_delay" variable
    reboot_wait_for_connection_delay: 30
    # Fail if the system does not respond within 300 seconds.
    # Becomes the "reboot_timeout" variable
    reboot_wait_for_connection_timeout: 300
```

This role can of course be invoked as a task or handler in playbooks or roles:

```yaml
- name: Reboot
  include_role:
    name: oasis_roles.system.reboot
```

All vars defined, for reference:

```yaml
- hosts: reboot-servers
  roles:
    - role: oasis_roles.system.reboot
  vars:
      # Override the underlying connection plugin's connection timeout value,
      # setting it to 10 seconds
      reboot_connect_timeout: 10
      # Show a custom message to users on the system being rebooted
      reboot_msg: 'A custom message displayed to users on the system being rebooted.'
      # Give the system 30 seconds to quiesce after rebooting.
      reboot_post_delay: 30
      # Wait two minutes before requesting reboot
      reboot_pre_delay: 120
      # Find the "shutdown" command in very strange places
      reboot_search_paths:
        - '/opt/customshutdown/bin'
        - '/tmp/'
      # Test responsiveness with the "uptime" command instead of the default "whoami"
      reboot_test_command: uptime
      # Fail if the system is not responsive without 300 seconds of issuing the reboot
      reboot_timeout: 300
      # Become the "reboot_user" instead of root to issue the reboot command
      reboot_become: true
      reboot_become_user: reboot_user
```

License
-------

GPLv3

Author Information
------------------

Sean Myers <sean.myers@redhat.com>
