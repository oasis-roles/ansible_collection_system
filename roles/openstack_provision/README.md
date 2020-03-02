[![Build Status](https://travis-ci.org/oasis-roles/openstack_provision.svg?branch=master)](https://travis-ci.org/oasis-roles/openstack_provision)

OPENSTACK PROVISION
===========

This role will provision resources in OpenStack per your directions
and add them to the inventory for the currently running system, as
indicated by the variables you pass in.

Servers will be provisioned using the name you give, appended by a count
of numbers, in case multiple servers are being provisioned from a single
call. Thus, if you request 4 servers named "webserver" then after calling
this role you will have four servers in your OpenStack tenant that are
named "webserver1", "webserver2", "webserver3", and "webserver4". This is
true even if you are requesting 1 server.

This should only be run on a single host, to avoid provisioning nightmares
where multiple hosts are calling into the OpenStack API to create the same
host names multiple times. Doing so is an exercise left to the user, rather than
leveraging the Ansible local\_task command as sometimes it might be beneficial
for that command to be run on a single remote host (or have multiple provision
jobs split across multiple hosts to effectively parallelize the provisioning).
If you wish to run locally you will need to limit running this role to the
local machine with an appropriate `hosts` directive.

Shade will need to be installed on each system where this role is executed,
as well. That is an exercise left to the user to install the shade package in
a manner that best suits you.

Most of the authentication arguments to individual OpenStack modules are not
leveraged in this role. Authentication configuration is left to the os-client-config
method of configuring a default cloud in the user's `~/.config/openstack/clouds.yaml`
on Linux hosts (see the documentation for the os-client-config package in OpenStack
for more information about configuring and where that file might live in other
operating systems).

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `openstack_provision_volumes` - An array of volumes to provision. These will
  be provisioned before the servers, so if you are attaching the volumes to the
  server, you are safe to create them with this array and immediately use them
  in the `openstack_provision_servers` array, provided you do not override the
  default value of `wait` being set to `true`. Elements in this array should have
  key/value pairs that match the arguments to the os\_volume module for Ansible.
* `openstack_provision_keypairs` - An array of keypair values to provision into
  the configured OpenStack tenant. See the documentation of `os_keypair` module
  in Ansible to find information on the arguments allowed.
* `openstack_provision_servers` - array of servers to provision, elements of
  the array should be hashes with keys matching the acceptable arguments from
  the standard os\_server module. Two additional arguments are also accepted -
  "count" and "groups". "Count" will provision multiple servers, each with a
  number appended (1, 2, 3, ...) while "groups" will place the provisioned
  hosts into the specified groups in your currently running Ansible inventory.
  Both "count" and "groups" are optional arguments, with default values of "1"
  and and empty array being assumed.
* `openstack_provision_wait_for_ssh` - Default: true. Set to false if you do not
  want to wait until SSH is accessible before exiting this role. Probably
  something to consider if you're dealing with Windows hosts or hosts with a
  non-standard SSH service running

Dependencies
------------

shade

Example Playbook
----------------

Raw role inclusion

```
- hosts: openstack_provision-servers
  roles:
    - role: openstack_provision
```

Role inclusion with network access to created instances through SSH

```
- hosts: openstack_provision-servers
  roles:
    - role: openstack_provision
      openstack_provision_servers:
        - name: test_server
          flavor: m3.medium
          image: 'CentOS-7-x86_64-GenericCloud-released-latest'
          count: 2
          key: path/to/your/private/key.pem
          key_name: <name of your ssh keypair>
          security_groups:
            - <name of security group you want to use>
          groups:
            - test_group
```

**Note: The local private key should have read/write access for the user group only. This can be achieved with `sudo chmod 600 <keyname>.pem`**

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
