[![Build Status](https://travis-ci.org/oasis-roles/passwordless_ssh.svg?branch=master)](https://travis-ci.org/oasis-roles/passwordless_ssh)

Passwordless SSH
===========

This role configures all hosts in the current play to allow password-free
(pubkey based) SSH authentication amongst themselves. Additional hosts may be
added to the circuit by setting the hostnames/IP addresses in the appropriate
variables documented below.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `passwordless_ssh_private_key` - REQUIRED - the private key file to use for the
  pubkey based authentication process. This file should NOT be the current user's
  normal private key, unless that key is not considered a secure secret
* `passwordless_ssh_public_key` - REQUIRED - the public key that matches the private
  key on the previous line. Same warning applies here.
* `passwordless_ssh_user` - The user that will be used for SSHing between the hosts in
  this play. This defaults to "root" but should probably be changed, as direct root
  access is usually considered A Bad Idea.
* `passwordless_ssh_user_home` - The home directory of the user in the above variable,
  where the user's `.ssh` directory is to be found
* `passwordless_ssh_remote_key_file` - name of the remote public key file. Defaults
  to "id\_rsa", as that is the most popular type of key to use
* `passwordless_ssh_extra_hosts` - an array of hostnames and/or IP addresses that
  ought to be configured to join in the pubkey auth round-robin fun. Defaults to
  an empty list
* `passwordless_ssh_update_known_hosts` - Defaults to true. Whether or not to add
  known host keys to `known_hosts` file in the configured dir on all hosts in the play.
* `passwordless_ssh_host_keys` - Defaults to empty array (`[]`). Should be set to an
  array of host keys to add to hosts if `passwordless_ssh_update_known_hosts` is true.
  See the "Host Key Notes" section below for details on the format for this array.
* `passwordless_ssh_hash_known_hosts` - Defaults to false. Whether or not to
  hash hostnames when adding entries to the `known_hosts` file.
* `passwordless_ssh_gather_host_keys` - Defaults to false. Whether or not to
  automatically gather host keys from all hosts (play hosts + extra hosts).
  **This is insecure, as no host key fingerprint validation is done.** Host keys
  are gathered using the `ssh-keyscan` tool, bundled with ssh. Each host is
  implicitly trusted to be honest when asked what its host keys are, which makes
  this vulnerable to man-in-the-middle attacks. Use of `passwordless_ssh_host_keys`
  is recommended, but this is extremely useful for e.g. testing clusters and other
  ephemeral or non-production use-cases. Gathered keys will be appended to
  `passwordless_ssh_host_keys`.
* `passwordless_ssh_become` - Defaults to true. Use sudo/become to change to an
  admin user. This is necessary if you are not logging in as the user who will be
  setup with the access.
* `passwordless_ssh_become_user` - Defaults to `passwordless_ssh_user`. The user to
  sudo/become to in order to access the files for `passwordless_ssh_user`. If this
  is changed to not match `passwordless_ssh_user` then unpredictable results can
  be seen when the user later attempts to connect due to potential mismatches in
  the pubkeys inserted to `.ssh/known_hosts`.

Host Key Notes
--------------

The format of host keys is as seen in an actual `known_hosts` file, or in the output
of the `ssh-keyscan` command. The input format expected by this role is the basic
`hostname keytype pubkey` format, with unhashed host names. All other host key lines
in `passwordless_ssh_host_keys` should match the key formats supported by the
[known_hosts](https://docs.ansible.com/ansible/latest/modules/known_hosts_module.html)
ansible module.

Dependencies
------------

None

Example Playbook
----------------

```
- hosts: passwordless_ssh_servers
  roles:
    - role: oasis_roles.system.passwordless_ssh
      passwordless_ssh_private_key: "{{ lookup('env', 'HOME') }}/mytestkeys/id_rsa"
      passwordless_ssh_public_key: "{{ lookup('env', 'HOME') }}/mytestkeys/id_rsa.pub"
      passwordless_ssh_user: testuser
      passwordless_ssh_user_dir: /home/testuser
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
