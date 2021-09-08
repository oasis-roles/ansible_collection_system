Container
===========

Installs a container service on a host. Additionally, it configures the appropriate
system user group. In most container driver systems, there is only support for the
root user executing by default. However, if the service detects a named group that
matches its expectations, it will permit users in that group to connect to the
service as well.

The role currently supports both Docker and Podman providers. However, it does not
support every combination of Linux operating systems to set that up. It attempts to
support Fedora, RedHat 7/8, and OracleLinux 7/8. However, it does not, currently,
attempt to follow the directions to get the actual Docker service running on an
EL8 host.

Later, the role can be updated to support
[these directions](https://oracle-base.com/articles/linux/docker-install-docker-on-oracle-linux-ol8)
if the need arises. However, Docker is considered less secure than alternatives like
podman and should only be used when the need is great.

Requirements
------------

Ansible 2.9 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `container_provider` - Default: varies. Set the name of the container provider service
  you want to install. Current values aceepted are `['podman', 'docker']`. On Fedora
  and EL8 this defaults to 'podman', while on EL7 it defaults to 'docker'.  Currently,
  crossing those values is not supported. However, if enhancements are needed, there is
  no reason it cannot be expanded.
* `container_access_users` - A list of users ought to have access to the container
  daemon. Defaults to only the login user for this role. Users in this group
  will not require sudo access in order to use the container service.
* `container_become` - Default: true. Whether to use the Ansible "become" functionality
  to escalate privileges.
* `container_become_user` - Default: root. User to become when performing sysadmin tasks

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: container-servers
  roles:
    - role: oasis_roles.system.container
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
