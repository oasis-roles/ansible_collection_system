ansible\_tower
===========

Deploys Ansible Tower using the underlying `ansible-playbook` command found in the  [installation
documentation](https://docs.ansible.com/ansible-tower/latest/html/quickinstall/install_script.html).
The `setup.sh` script from the documentation is not used because it exists to
add database backup and restore features, which this role is not intended to
support.


Requirements
------------

Ansible 2.8 or higher

Ansible Tower <= 3.7 (due to changes in Tower 3.8's licensing scheme, support
for 3.8+ to be added in the future)

Red Hat Enterprise Linux 8

Valid Red Hat Subscriptions

Ansible Tower License

[awx.awx](https://docs.ansible.com/ansible/latest/collections/awx/awx/) Ansible
collection (`ansible-galaxy collection install awx.awx`).  This is optional for
having Tower run playbooks using its API after deployment of Tower itself.

Role Variables
--------------

Currently the following variables are supported:

* `ansible_tower_install_package` Default:
  `https://releases.ansible.com/ansible-tower/setup-bundle/ansible-tower-setup-bundle-3.7.4-1.tar.gz`
* `ansible_tower_inventory_file` Default:  the inventory file provided by the
   Ansible Tower installation package is used.  This is recommended for most
   single-node deployments.  To provide a customized inventory file, set this
   variable to the local path on the Ansible control machine where the inventory
   file is located.  See the [Ansible Tower
   documentation](https://docs.ansible.com/ansible-tower/latest/html/quickinstall/install_script.html)
   for configuring this file.
* `ansible_tower_extra_vars` Dictionary of extra vars to pass to the
  `ansible-playbook` command that deploys Ansible Tower.  This variable is
   **required** if `ansible_tower_inventory_file` is left at default, and it's
   recommended to set the `admin_username`, `admin_password`, `pg_password`
   variables at a minimum.
* `ansible_tower_no_log` Default: `true`.  Hide sensitive credentials from the
   Ansible output log.  Set to `false` to aid in debugging.
* `ansible_tower_become` Default: `true`. If this role needs administrator
   privileges, then use the Ansible become functionality (based off sudo).
* `ansible_tower_become_user` - Default: `root`. If the role uses the become
   functionality for privilege escalation, then this is the name of the target
   user to change to.

Example Playbooks
----------------

Basic single-node deployment:

```yaml
- hosts: ansible_tower-servers
  roles:
    - role: oasis_roles.system.ansible_tower
  vars:
    ansible_tower_extra_vars:
      admin_username: admin
      admin_password: notsecure
      pg_password: notsecure
```

Single-node deployment with additional tasks to add the license and have Tower
run a playbaook from Git SCM:

```yaml
- hosts: ansible_tower-servers
  roles:
    - role: oasis_roles.system.ansible_tower
  vars:
    ansible_tower_extra_vars:
      admin_username: admin
      admin_password: notsecure
      pg_password: notsecure
    ansible_tower_license_path: ../default/license.json
    ansible_tower_host: "{{ ansible_default_ipv4.address }}"
    ansible_tower_validate_certs: false
    ansible_tower_organization: oasis
    ansible_tower_inventory: oasis-test
    ansible_tower_scm_url: https://github.com/ansible/test-playbooks.git
    ansible_tower_scm_branch: master
    ansible_tower_project: test-playbooks
    ansible_tower_job_template: test-ansible_env
    ansible_tower_playbook: ansible_env.yml
    ansible_tower_job_timeout: 120

  tasks:
    - name: Set the license using a file
      awx.awx.tower_license:
        data: "{{ lookup('file', '{{ ansible_tower_license_path }}') }}"
        eula_accepted: true
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"

    - name: Create tower organization
      tower_organization:
        name: "{{ ansible_tower_organization }}"
        state: present
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"

    - name: Add tower inventory
      tower_inventory:
        name: "{{ ansible_tower_inventory }}"
        organization: "{{ ansible_tower_organization }}"
        state: present
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"

    - name: Add tower host
      tower_host:
        name: localhost
        inventory: "{{ ansible_tower_inventory }}"
        state: present
        variables:
          ansible_connection: local
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"

    - name: Add tower project
      tower_project:
        name: "{{ ansible_tower_project }}"
        organization: "{{ ansible_tower_organization }}"
        state: present
        scm_update_on_launch: true
        scm_branch: "{{ ansible_tower_scm_branch }}"
        scm_type: git
        scm_url: "{{ ansible_tower_scm_url }}"
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"

    - name: Create tower job template
      tower_job_template:
        name: "{{ ansible_tower_job_template }}"
        job_type: "run"
        inventory: "{{ ansible_tower_inventory }}"
        project: "{{ ansible_tower_project }}"
        playbook: "{{ ansible_tower_playbook }}"
        state: "present"
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"

    - name: Launch the test job
      tower_job_launch:
        job_template: "{{ ansible_tower_job_template }}"
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"
      register: _ansible_tower_job
      changed_when: false

    - name: Wait for job
      tower_job_wait:
        job_id: "{{ _ansible_tower_job.id }}"
        timeout: "{{ ansible_tower_job_timeout }}"
        validate_certs: "{{ ansible_tower_validate_certs }}"
        tower_host: "{{ ansible_tower_host }}"
        tower_username: "{{ ansible_tower_extra_vars.admin_username }}"
        tower_password: "{{ ansible_tower_extra_vars.admin_password }}"
      register: _ansible_tower_job_status

    - name: Display job status
      debug:
        msg: "{{ _ansible_tower_job_status }}"
```

License
-------

GPLv3

Author Information
------------------

David Roble <droble@redhat.com>
