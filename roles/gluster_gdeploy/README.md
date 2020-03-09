[![Build Status](https://travis-ci.com/oasis-roles/gluster_gdeploy.svg?branch=master)](https://travis-ci.com/oasis-roles/gluster_gdeploy)

Gluster Gdeploy
===========

This role will create a [GlusterFS](https://www.gluster.org/) installation on
the selected nodes. This role uses the older GDeploy tool to automate the
setup and management of backend volumes. Newer roles are being developed by
the Gluster project directly to manage Gluster from an entirely native
Ansible role configuration.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

**IMPORTANT** This role can only be used to set up a single cluster per invocation.
Because of the way GDeploy works, being run from only a single host across all of
the hosts in the Gluster cluster, this role makes use of the `ansible_play_hosts`
variable to build the cluster. Thus, if you are setting up multiple Gluster clusters
from a single playbook, you will need to call this role multiple times in your
playbook with each play setting up a single cluster. Future improvements to this
role might lift that restriction, but for the time being that limit remains.

Role Variables
--------------

Currently the following variables are supported:

### General

* `gluster_gdeploy_peers` - A list of hostnames, IP addreses, or similar network
  addresses that should be probed into the Gluster cluster. This defaults to all
  the hosts in the current play, but can be customized. Doing so is likely to be
  beneficial for production HA or high performance cases where the cluster should
  use a dedicated network that is not the same as the management addresses over
  which Ansible would normally connect.
* `gluster_gdeploy_configuration_file` - REQUIRED: Path to the configuration file
  for use with gdeploy. Consult documentation on GDeploy to learn more about the
  types of files that should be used
* `gluster_gdeploy_rpm_version` - Optional value to specify a version string for
  the RPM of Gluster to install. If specified, this must begin with the "-" character
  as that is how RPM versions are specified (e.g. "redhat-storage-server-3.1.4.0"
  would lead to this variable being specified as "-3.1.4.0")
* `gluster_gdeploy_become` - Default: true. Whether to use Ansible become for
  administrative tasks in this role
* `gluster_gdeploy_become_user` - Default: root. User to become when performing
  administrative tasks in this role
* `gluster_gdeploy_gstatus_enable` - Default: false. Set to true in order to
  enable installation of the gstatus tool across the cluster
* `gluster_gdeploy_samba_enable` - Default: false. Set to true in order to enable
  installation of Samba support in Gluster. See the Dependencies section and the
  Gluster documentation for more information on additional repositories to enable
  in order to be able to install this
* `gluster_gdeploy_nfs_ganesha_enable` - Default: false. Set to true in order to
  enable installation of NFS-Ganesha support in Gluster. See the Dependencies
  section and the Gluster documentation for more information on additional
  repositories to enable in order to be able to install this

Dependencies
------------

Each of the hosts in the Gluster Cluster should be configured to be mutually
accessible via SSH from one another. This can be done with the
[passwordless\_ssh](https://github.com/oasis-roles/passwordless_ssh) role from
OASIS.

Once the system is subscribed to RHN, certain repos are reqiured. This can be
configured with the [rhsm](https://github.com/oasis-roles/rhsm) role from OASIS.
Check the Gluster docs for which repositories are required, but at the time of
writing of this document, the only required repo is "rhel-7-server-ansible-2-rpms".

If you want to enable Samba, then you need to install the
"rh-gluster-3-samba-for-rhel-7-server-rpms" repository in addition to setting the
appropriate variable. If you want to enable NFS-Ganesha, then you need to configure the
"rh-gluster-3-nfs-for-rhel-7-server-rpms" repository in addition to setting the
appropriate variable. Currently, the role does not support any configuration related
to either of these optional packages. If there are options needed, then file issues
against the GitHub [repository](https://github.com/oasis-roles/gluster_gdeploy)
requesting those options be added to the role.

Due to limitations of Gluster, the system must be set to the "en\_US" locale.
This can be accomplished with the [localectl](https://github.com/oasis-roles/localctl)
role.

Example Playbook
----------------

```yaml
- hosts: gluster_gdeploy-servers
  roles:
    - role: oasis_roles.system.gluster_gdeploy
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
