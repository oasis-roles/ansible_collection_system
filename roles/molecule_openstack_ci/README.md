[![Build Status](https://travis-ci.org/oasis-roles/molecule_openstack_ci.svg?branch=master)](https://travis-ci.org/oasis-roles/molecule_openstack_ci)

molecule_openstack_ci
===========

Role to manage the creation and destruction of openstack resources for running
molecule in a shared CI environment. A hash of the molecule role name, the
current scenario, and the executing user to appended to generated resources to
prevent naming conflicts when a given role scenario is tested by two users
simultaneously in the shared environment.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `molecule_openstack_ci_ssh_user` - Username used to log in to provisioned instance,
  defaults to "cloud-user".
* `molecule_openstack_ci_ssh_port` - SSH port to connect to provisioned instance,
  defaults to 22.
* `molecule_openstack_ci_security_group_name` - Security group name prefix to use
 when generating security group. Defaults to "molecule". The actual security
 group(s) created will have the run hash appended to their name.
* `molecule_openstack_ci_security_group_description` - Security group description,
 defaults to "Security group for testing Molecule"
* `molecule_openstack_ci_security_group_rules` - Array of argument dictionaries passed to
 (os_security_group_rule)[https://docs.ansible.com/ansible/latest/modules/os_security_group_rule_module.html]
 module, defaults to `[{"ethertype": "IPv4"}, {"ethertype": "IPv6"}]`, effectively allowing
 all access to molecule instances by default.
* `molecule_openstack_ci_keypair_name` - molecule_key
* `molecule_openstack_ci_security_group_name` - SSH keypair name prefix to use
 when generating keypair. Defaults to "molecule_key". The actual keypair
 created will have the run hash appended to its name.
* `molecule_openstack_ci_cloud` - name of the OpenStack cloud to connect to. This defaults to the value
 of the environment variable "`OS\_CLOUD`" if it is set, or "`default`" if not.
* `molecule_openstack_ci_state` - Whether to create (`present`) or destroy (`absent`) molecule resources.
 Defaults to `present`.

Dependencies
------------

- `python-openstacksdk` must be installed on the machine running molecule,
  as the openstack config is loaded using the `openstack.config` module.

Example Playbooks
-----------------

Molecule scenario `create.yml`:
```yaml
- name: Create
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: oasis_roles.system.molecule_openstack_ci
      # other vars can be set here, e.g.
      # molecule_openstack_ci_ssh_user: yourcloudusername
```

Molecule scenario `destroy.yml`:
```yaml
- name: Destroy
  hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: oasis_roles.system.molecule_openstack_ci
      molecule_openstack_ci_state: absent
```

**Note:** Remember to add `oasis_roles.system.molecule_openstack_ci` to your
molecule scenario dependencies.

License
-------

GPLv3

Author Information
------------------

Sean Myers <sean.myers@redhat.com>
