[![Build Status](https://travis-ci.org/oasis-roles/update_ca_trust.svg?branch=master)](https://travis-ci.org/oasis-roles/update_ca_trust)

update_ca_trust
===========

Install certificates using the `update-ca-trust` command

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `update_ca_trust_urls` - List of URLs from which to retrieve and install
  certificates

* `update_ca_trust_validate_certs` - Perform TLS validation during download of
  certificates when using `update_ca_trust_urls`.  Useful when downloading
  certificates from a webserver via TLS and ensuring that they have not been
  tampered with during transport.  Defaults to `true`.

* `update_ca_trust_files` -  List of local files on the Ansible control machine
  from which to install certificates

* `update_ca_trust_become` - Whether or not to use the `become` feature of
  Ansible to gain admin privileges.  Defaults to `true`.

* `update_ca_trust_become_user` - The user to sudo/become.  Defaults to `root`.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: update_ca_trust-servers
  roles:
    - role: oasis_roles.system.update_ca_trust
      update_ca_trust_urls:
        - https://raw.githubusercontent.com/oasis-roles/update_ca_trust/master/molecule/shared/localhost.localdomain.crt
      update_ca_trust_files:
        - /path/to/local/files/localhost.localdomain.crt
```

License
-------

GPLv3

Author Information
------------------

David Roble <droble@redhat.com>
