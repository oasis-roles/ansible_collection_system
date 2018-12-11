[![Build Status](https://travis-ci.org/devroles/docker.svg?branch=master)](https://travis-ci.org/devroles/docker)

Docker
===========

Installs the Docker service on a host. Additionally, it configures the "docker"
system user group. When the Docker daemon detects a group named "docker" then it
allows any user in that group access, instead of limiting access to only the
root user.

Because this configures a Docker group, consider carefully if it matches the
security requirements of your own deployment plans.

Requirements
------------

Ansible 2.4 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `docker_access_users` - A list of users ought to have access to the Docker
  daemon. Defaults to only the login user for this role. Users in this group
  will not require sudo access in order to use the Docker service.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: docker-servers
  roles:
    - role: greg_hellings.docker
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
