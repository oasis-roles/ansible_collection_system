[![Build Status](https://travis-ci.org/oasis-roles/upload_files.svg?branch=master)](https://travis-ci.org/oasis-roles/upload_files)

UPLOAD FILES
===========

A role that simply encapsulates the `copy` module from Ansible to upload
files to the remote destination

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### General

* `upload_files` - An array of files that should be uploaded to the remote
  host. Items in this array should be composed of hashes with the values from
  the [copy](https://docs.ansible.com/ansible/latest/modules/copy_module.html#copy-module)
  module from Ansible. Any parameters that are not supported by that module
  should be reported as issues against this role

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: upload_files-servers
  roles:
    - role: oasis_roles.system.upload_files
      upload_files:
        - src: /my/local/file
          dest: /home/me/file_name
        - content: "derp\nWAZZAP"
          dest: /var/lib/derp/derp
          owner: root
          group: derp
```

License
-------

GPLv3

Author Information
------------------

Greg Hellings <greg.hellings@gmail.com>
