libvirt
===========

Spins up a RHEL/CentOS VM on the local host

Requirements
------------

Ansible 2.8 or higher

Role Variables
--------------

Currently the following variables are supported:

### General

* `libvirt_rhel_vm_storage` - Default: `/var/lib/libvirt/images`. The path on
  the remote system to upload VM images to. Currently there is no support for
  storage pools other than the local directories.
* `libvirt_rhel_vm_domain` - Default:
```yaml
libvirt_rhel_vm_domain:
  name: foo.example.com
  img_path: ~/CentOS-7-x86_64-GenericCloud.qcow2
  os-variant: rhel7.7

  ram: 4096
  vcpus: 1
  disk: 20G

  root_passwd: "$6$Fa84yQfpK0gpluDJ$sdfdsfdsfdsfdsfdfdsfdsfddsfdaQpO6MKgioTOV5\
    lRy.2tdA9IexTnvYNK3mP8clpC/sdsfdsfdsfdsfdsfsd60"
  root_ssh_pub_keys:
    - "ssh-rsa AAAdsfdfdsfdfdEAAAADAQABAAABAQD0yXYYdsfdAOSdIjcRp\
      8TVOPnFplYJEY8VST+bQeW1Fosdfddfsdfmpmd/RdV9W/0d7sRfymL1diDm6ml3kwddff5Xn7A\
      edsztdRahvZsBD9ADBqnQBli0adop6+PDRsdfdsfBjpFnrwVoe9QZPJVqZle6HBeJYIffffEY6\
      1vhC8JXyGGDIJi7pdSjPdsfdsfdsfdsfdsfdsfsxTbAp4ddkEuS/9NR8JZ3HJg+h6mKoNffffq\
      RUiikG98dfdfdsfdsfdfdfdfdfdfdsfdsfdsfdsfdsfyPMXK7nD+R0Jx4mmRlFWKmYTjffffSq\
      sdfadfdsfdsfdsf"

  bridges:
    - br0

  nics:  # NICs to provision on the VM, using the network_scripts role
    - filename: ifcfg-eth0
      NAME: eth0
      DEVICE: eth0
      TYPE: Ethernet
      BOOTPROTO: static
      IPADDR: 192.168.1.10
      GATEWAY: 192.168.1.1
      NETMASK: 255.255.255.0
      DEFROUTE: !!str yes
      IPV6INIT: !!str no
      ONBOOT: !!str yes
      DNS1: 8.8.8.8
```
  The VM to spin up. The image pointed to by `libvirt_rhel_vm_domain.img_path`
  must already exist on the local system. It will be uploaded to the remote host
  in the `libvirt_rhel_vm_storage` directory, resized to the value of `disk`,
  spun up with the specified hardware options, fed the `nics` list as config files
  from the `network_scripts` role, and configured with the provided passwords
  and pubkeys. The provisioning script is relatively tightly bound with RHEL or
  CentOS 7, hence the naming of this role.
* `libvirt_become` - Default: true. If this role needs administrator
  privileges, then use the Ansible become functionality (based off sudo).
* `libvirt_become_user` - Default: root. If the role uses the become
  functionality for privilege escalation, then this is the name of the target
  user to change to.
* `libvirt_rhel_vm_nic_config_path` - Default: `null`. Path on the
  remote host to install the nic-config scripts into before uploading them to
  the VM. If left as `null`, then a tempdir will be created on the remote host
  for uploading. If you set this value, then you are responsible to ensure that
  the path exists before calling this role.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: libvirt-servers
  roles:
    - role: oasis_roles.system.libvirt
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
