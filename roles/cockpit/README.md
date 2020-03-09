[![Build Status](https://travis-ci.org/oasis-roles/cockpit.svg?branch=master)](https://travis-ci.org/oasis-roles/cockpit)

COCKPIT
===========

Installs cockpit to a set of hosts and starts the service

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `cockpit_additional_packages` - Default []. A list of additional cockpit packages in order to install
  cockpit-adjacent packages.
* `cockpit_become_user` - the user to execute tasks through
* `cockpit_become` - Default: true. Wether to use Ansible's "become" to escalate privileges

**Note: To use the default value for `cockpit_version`, your system must have several default
packages installed. Specifically, rhel-7-server-rpms, rhel-7-server-extras-rpms,
rhel-7-server-optional-rpms**

Dependencies
------------

None

Example Playbook
----------------

Since the cockpit service is dependent on other services being configured
before installation, this example will include the use of the rhsm and
firewalld roles located in ansible galaxy under oasis\_roles to configure the
hosts for cockpit installation.

First, include the required roles

```
- hosts: all
  roles:
    - oasis_roles.system.rhsm
    - oasis_roles.system.cockpit
    - oasis_roles.system.firewalld
```

Second, configure Red Hat Subscription Manager using the [rhsm](https://galaxy.ansible.com/oasis_roles.system/rhsm) role.

```
  vars:
    rhsm_username: user@company.com
    rhsm_password: password
    rhsm_pool_ids:
      - abcdefghijklmnopqrstuvwxyz1234567890
    rhsm_repositories:
      only:
        - rhel-7-server-rhv-4-mgmt-agent-rpms
        - rhel-7-server-ansible-2-rpms
        - rhel-7-server-rpms

```

**Note: These repositories are necessary to install the cockpit service**

Third, configure the firewall with the [firewalld](https://galaxy.ansible.com/oasis_roles.system/firewalld) role in one of two ways:
1. Allow direct access to cockpit through port 9090
2. Setup port forwarding from port 443 (HTTPS port) to port 9090 (cockpit port)

Method 1:

```
    firewalld_zone: public
    firewalld_ports_open:
      - proto: tcp
        port: 9090
```

Method 2:

```
    firewalld_zone: public
    firewalld_ports_open:
      - proto: tcp
        port: 443
    firewalld_ports_forward:
      - proto: tcp
        port: 443
        to_port: 9090
```

**Note: Each of these code snippets are part of a single file**

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>
