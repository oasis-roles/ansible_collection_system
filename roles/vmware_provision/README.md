[![Build Status](https://travis-ci.com/oasis-roles/vmware_provision.svg?branch=master)](https://travis-ci.com/oasis-roles/vmware_provision)

vmware_provision
===========

Provisions VMWare hosts and adds them to inventory groups. This role also
provides the information for newly provisioned instances through the variable
`vmware_provisioned_vms` for use elsewhere in the playbook

Requirements
------------

Ansible 2.8 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Python package `pyvmomi`

Role Variables
--------------

Currently the following variables are supported:

### Required

* `vmware_provision_hostname` - The hostname or IP address of the vSphere vCenter or ESXi server. **REQUIRED**
* `vmware_provision_username` - The username of the vSphere vCenter or ESXi server. **REQUIRED**
* `vmware_provision_password` - The password of the vSphere vCenter or ESXi server. **REQUIRED**

### Optional

* `vmware_provision_port` - The port of the vSphere vCenter or ESXi server.
* `vmware_provision_validate_certs` - Whether or not to allow connecting to the vSphere vCenter
* `vmware_provision_custom_vms` - A list of custom VM configurations to deploy
to a vSphere vCenter or ESXi server. Each list item represents a VM to be
provisioned. Parameters of each list item should have key/value pairs that match
the arguments to the
[vmware_guest](https://docs.ansible.com/ansible/latest/modules/vmware_guest_module.html#vmware-guest-module)
module for Ansible.
* `vmware_provision_ovfs` - A list of configurations using an OVA file to
deploy to a vSphere vCenter or ESXi server. Each list item represents a VM to
be provisioned. Parameters of each list item should have key/value pairs that
match the arguments to the
[vmware_deploy_ovf](https://docs.ansible.com/ansible/latest/modules/vmware_deploy_ovf_module.html)
module for Ansible.
  or ESXi server when its TLS/SSL certificates are invalid.
* `vmware_provision_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `vmware_provision_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.

Dependencies
------------

Python package `pyvmomi`

Example Playbook
----------------

This example shows a playbook used to provision VMs with custom configurations

Note that these examples are explicitly targeting `localhost` as the playbook host
assuming that `pyvmomi` was previously installed on the ansible control system.

To run on another host, ensure that the `pyvmomi` package is installed and available
in the environment in which this role will run (e.g. install it in a prior play, or
in this play's `pre_tasks`).

```yaml
- hosts: localhost
  roles:
    - role: oasis_roles.system.vmware_provision
  vars:
    # required
    vmware_provision_hostname: "vCenter.hostname.com"
    vmware_provision_username: "username"
    vmware_provision_password: "password"

    # optional
    vmware_provision_port: 443
    vmware_provision_validate_certs: true

    vmware_provisioned_custom_vms:
      - name: custom_VM-1
        validate_certs: false
        folder: my_vm_folder
        state: poweredon
        datacenter: myDatacenter
        datastore: myDatastore
        cluster: myCluster
        guest_id: centos64Guest
        hardware:
          memory_mb: 2048
          num_cpus: 4
        networks:
          - name: VM Network
            start_connected: true
        wait_for_ip_address: true
      - name: custom_VM-2
        folder: test_vms
        state: present
        datacenter: default-datacenter
        guest_id: fedora30-Guest
        esxi_hostname: "esxi-hostname"
        disk:
          - size_gb: 10
            type: thin
            datastore: datastore1
        hardware:
          memory_mb: 512
          num_cpus: 4
          scsi: paravirtual
        networks:
          - name: VM Network
            mac: aa:bb:dd:aa:00:14
            ip: 10.10.10.100
            netmask: 255.255.255.0
            device_type: vmxnet3
```

This example shows a playbook used to provision VMs using OVA templates located on the host machine

**Note that the `ovf` parameter only accepts `.ova` files.
You can use VMware's [ovftool](https://code.vmware.com/web/tool/4.3.0/ovf)
to convert an ovf template with its supporting files to an ova template**

```yaml
- hosts: localhost
  roles:
    - role: oasis_roles.system.vmware_provision
  vars:
    vmware_provision_hostname: "vCenter.hostname.com"
    vmware_provision_username: "username"
    vmware_provision_username: "password"

    vmware_provision_ovfs:
      - name: ova_VM-1
        ovf: "path/to/local/template.ova"
        validate_certs: false
        datacenter: myDatacenter
        datastore: myDatastore
        cluster: myCluster
        power_on: false
        allow_duplicates: false
        networks:
          'VM Network': 'VM Network'
      - name: ova_VM-2
        ovf: "path/to/another/local/template.ova"
        wait_for_ip_address: true
```

License
-------

GPLv3

Author Information
------------------

Andrew Euredjian <aeuredji@redhat.com>
