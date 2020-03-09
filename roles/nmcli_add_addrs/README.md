[![Build Status](https://travis-ci.org/oasis-roles/nmcli_add_addrs.svg?branch=master)](https://travis-ci.org/oasis-roles/nmcli_add_addrs)

# nmcli_add_addrs

Add IP addresses to a NetworkManager connection using the `nmcli` tool.

This is intended to be used on connections that are already managed by
NetworkManager, and also already "up". Initial setup of connections should
be done during system install, or using the ansible
[nmcli module](https://docs.ansible.com/ansible/latest/modules/nmcli_module.html).

## Requirements

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent with NetworkManager

## Role Variables

Currently the following variables are supported:

### General

* `nmcli_add_addrs_connection` - Name of NetworkManager connection to modify.
* `nmcli_add_addrs_interface` - Name of physical interface to modify,
  if connection name is not known.
* `nmcli_add_addrs_ipv4` - Array of IPv4 CIDR addresses to add, see notes below.
* `nmcli_add_addrs_ipv6` - Array of IPv6 CIDR addresses to add, see notes below.
* `nmcli_add_addrs_become_user` - User to "become" when modifying connections,
  default "root".

#### connection vs. interface

One of `nmcli_add_addrs_connection` or `nmcli_add_addrs_interface` must be
set. If both the connection name and interface are known, only the connection
name should be used. `nmcli_add_addrs_connection` takes precedence over
`nmcli_add_addrs_interface`, and the ability to determine the NetworkManager
connection name from an interface is not guaranteed. This role will fail in
the case where the connection name cannot be determined based on the connection
name; specifying the connection name is more reliable.

## Notes

### Picking the default interface

If the `ip` command is available when ansible gathers facts about the system
(provided by the `iproute` package on RHEL/CentOS 7), two facts will be set
that correspond to the system's default route, `ansible_default_ipv4` and
`ansible_default_ipv6`. Depending on which IP stack applies, the "interface"
property of these facts can be used for the value of `nmcli_add_addrs_interface`
to help use this role even when the interface or NetworkManager connection name
is not known.

Example vars:

- `nmcli_add_addrs_interface: "{{ ansible_default_ipv4.interface }}"`
- `nmcli_add_addrs_interface: "{{ ansible_default_ipv6.interface }}"`

### Address Formatting

Addresses must be in 
[CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation),
normalized to be their shortest form, in lowercase, particularly in the case
of IPv6. Idempotence will be broken if input addresses are not normalized.

Good:

- `10.0.0.0/24`
- `2001:db8::1/64`

Bad:

- `010.000.000.000/24` - Including leading zeros is the best way to cause
  idempotence to break with IPv4 addresses.
- `2001:0DB8:0:0::1/64` - IPv6, with the inclusion of hexadecimal letters and
  the zero-collapsing double colon, is a little more tricky. Use lowercase
  letters, do not use leading zeros in any colon-separate address component,
  and collapse zero-valued address components in the middle of the address
  with a double colon.

## Dependencies

- NetworkManager must be installed, and configured to manage the interface
  to which addresses will be added.

## Example Playbook

```yaml
- hosts: all
  roles:
    - role: oasis_roles.system.nmcli_add_addrs
  vars:
    nmcli_add_addrs_interface: eth0
    nmcli_add_addrs_ipv4:
      - '192.0.2.1/24'
      - '198.51.100.1/24'
    nmcli_add_addrs_ipv6:
      - '2001:db8::1/64'
      - '2001:db8:1::1/64'
```

## License

GPLv3

## Author Information

Sean Myers <sean.myers@redhat.com>
