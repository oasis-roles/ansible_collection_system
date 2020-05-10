firewalld
===========

This role provides basic hole punching and local port forwarding for the
firewalld service, to aid in the task of running application stacks deployed
using the OASIS roles.  It provides a simple interface to the Ansible
[firewalld
module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html).

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `firewalld_zone` - firewall zone for all rules
* `firewalld_ports_open` - permanently open ports (IPv4+IPv6) for given
  firewall zone
* `firewalld_services` - a list of named services for firewalld to enable
* `firewalld_ports_forward` - permanently forward local ports (IPv4+IPV6) for
  given firewall zone, e.g. TCP 80->8080 for webapps
* `firewalld_become` - use Ansible "become" for proper authorization to manage
  the firewall

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: firewalld-servers
  roles:
    - role: firewalld
      firewalld_zone: public
      firewalld_ports_open:
        - proto: tcp
          port: 8080
        - proto: udp
          port: 9990-9999
      firewalld_services:
        - ssh
      firewalld_ports_forward:
        - proto: tcp
          port: 80
          to_port: 8080
      firewalld_become: true
```

License
-------

GPLv3

Author Information
------------------

David Roble <droble@redhat.com>
