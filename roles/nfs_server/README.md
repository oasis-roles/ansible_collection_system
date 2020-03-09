[![Build Status](https://travis-ci.org/oasis-roles/nfs_server.svg?branch=master)](https://travis-ci.org/oasis-roles/nfs_server)

nfs_server
===========

Install NFS server and configure shares, and optionally create share directories

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `nfs_server_shares` - List of NFS shares to create in
  `nfs_server_exports_file`, defined as an empty list by default. See
  [Example Playbook](#example-playbook) for syntax.

* `nfs_server_services` - List of services to enable and start for the NFS
  server.  Defaults to `nfs` and `rpcbind` to support NFSv3.  Note that
  `rpcbind` is not used for NFSv4.

* `nfs_server_exports_file` - Path to exports file to add shares to.  NOTE:
  Files in `/etc/exports.d` must be named with a `.exports` suffix.  Defaults
  to `/etc/exports.d/nfs.exports`.

* `nfs_server_become` - Whether or not to use the `become` feature of Ansible
  to gain admin privileges.  Defaults to `true`.

* `nfs_server_become_user` - The user to sudo/become.  Defaults to `root`.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: nfs_server-servers
  roles:
    - role: oasis_roles.system.nfs_server
      nfs_server_shares:
          # path to share (required)
        - share_path: /srv/share1
          # IP networks for which to allow access (required)
          host_allow: '*'
          # Comma-separated list of mount options (required)
          opts: rw,sync,all_squash
          # create the share directory (optional)
          create_dir: true
          # owner of the NFS share directory (optional)
          owner: nfsnobody
          # group of the NFS share directory (optional)
          group: nfsnobody
          # mode of the NFS share directory (optional)
          # NOTE: Even though this is an integer value, it still must be quoted
          # here due to the linked issue below:
          # https://github.com/ansible/ansible/issues/31952
          mode: '0755'
        - share_path: /srv/share2
          host_allow: '192.168.0.0/24'
          opts: ro,sync
    - role: oasis_roles.system.firewalld
      firewalld_zone: public
      firewalld_ports_open:
        # rpc-bind /usr/lib/firewalld/services/rpc-bind.xml
        - proto: tcp
          port: 111
        - proto: udp
          port: 111
        # mountd /usr/lib/firewalld/services/mountd.xml
        - proto: tcp
          port: 20048
        - proto: udp
          port: 20048
        # NFSv4 /usr/lib/firewalld/services/nfs.xml
        - proto: tcp
          port: 2049
```

License
-------

GPLv3

Author Information
------------------

David Roble <droble@redhat.com>
