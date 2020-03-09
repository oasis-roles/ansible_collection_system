[![Build Status](https://travis-ci.com/oasis-roles/register_idm.svg?branch=master)](https://travis-ci.com/oasis-roles/register_idm)

register\_idm
===========

Installs and configures Red Hat IDM client

If a host is already configured (meaning that /etc/ipa/default.conf already exists on the host),
run this role with the `register_idm_client_reconfigure` value set to `true` in order to
regenerate configuration with new settings.

Requirements
------------

None

Role Variables
--------------

Currently the following variables are supported:

### General

* `register_idm_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `register_idm_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

### Server settings

* `reigster_idm_server_admin_username` - **REQUIRED**. Username to log in to server
* `register_idm_server_admin_password` - **REQUIRED**. Password to log in to server
* `register_idm_domain` - **REQUIRED**. The IDM domain to be registered with.
* `register_idm_server_realm` - Default: upper-case transformation of
  `register_idm_domain`.
* `register_idm_server_domain` - Default: copy of `register_idm_domain`.

### Client settings

* `register_idm_hostname` - Default: ansible\_fqdn. The full hostname of this system
  to register with the IPA server.
* `register_idm_client_reconfigure` - Default: false. If the system already has a file in
  /etc/ipa/default.conf
* `register_idm_client_configure_ssh` - Default: true. Have IPA manage your system's
  ssh configuration
* `register_idm_client_configure_sshd` - Default: true. Have IPA manage the SSHD on the
  system
* `register_idm_client_mkhomedir` - Default: true. Have IPA create home directories
* `register_idm_client_ssh_trust_dns` - Default: true. Enable the IPA SSH trust DNS
  functionality.
* `register_idm_client_setup_ntp` - Default: true. Have IPA setup NTP on the host.
  This will not overwrite an existing service, such as chronyd.
* `register_idm_client_base_command` - Default: `ipa-client-install -U`. This should probably
  be left as is, unless you want to bake in additional flags or options on every
  run of this role.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: register_idm-servers
  roles:
    - role: oasis_roles.system.register_idm
```

License
-------

GPLv3

Author Information
------------------

Marcos Amorim <marcosmamorim@gmail.com>
Greg Hellings <greg.hellings@gmail.com>
