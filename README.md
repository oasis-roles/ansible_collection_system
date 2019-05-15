[![Build Status](https://travis-ci.org/oasis-roles/rhsm.svg?branch=master)](https://travis-ci.org/oasis-roles/rhsm)

RHSM
=====

This role will register or unregister a system using `subscription-manager`, and can also enable or disable
repositories available via subscription.

Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent

Valid Red Hat Subscriptions

Role Variables
--------------

Currently the following variables are supported:

### Subscription Management

Vars in this section directly correspond to the args available to the
[redhat_subscription module](http://docs.ansible.com/ansible/latest/modules/redhat_subscription_module.html).

* `rhsm_username` - access.redhat.com or Satellite (RHSM Provider) username
* `rhsm_password` - access.redhat.com or Satellite (RHSM Provider) password
* `rhsm_org_id` - RHSM Provider organization ID
* `rhsm_activationkey` - RHSM Provider activation key
* `rhsm_server_hostname` - hostname for alternate RHSM provider
* `rhsm_server_insecure` - disable certificate verification when connecting to RHSM Provider (bool, default false)
* `rhsm_baseurl` - Alternate base URL of package repositories if not using Red Hat CDN
* `rhsm_server_proxy_hostname` - HTTP proxy hostname
* `rhsm_server_proxy_port` - HTTP proxy port
* `rhsm_server_proxy_user` - HTTP proxy username
* `rhsm_server_proxy_password` - HTTP proxy password
* `rhsm_auto_attach` - automatically consume from available subscriptions if registration succeeds (bool, default false, requires ansible >= 2.5)
* `rhsm_environment` - Register with a specific environment in the destination org. (Used with Red Hat Satellite 6 or Katello)
* `rhsm_pool` - Specific pool name to consume (regex can be used as input). Use `rhsm_pool_ids` when possible as it is much faster. Mutually exclusive with `rhsm_pool_ids`
* `rhsm_pool_ids` - List of pool IDs to consume, or a list of dicts with pool IDs as keys and quantity of entitlements to consume as values. Mutually exclusive with `rhsm_pool`
* `rhsm_consumer_type` - The type of unit to register (defaults to "system")
* `rhsm_consumer_name` - Name of the system to register (defaults to system hostname)
* `rhsm_consumer_id` - Existing consumer ID to resume a previous registration
* `rhsm_force_register` - Register the system even if it is already registered (bool, default false)
* `rhsm_unregister` - Unregister a system if true. The system will be unregistered. System registration *will not be attempted*
  (bool, default false)

### Repository Management

Note:
> Using variables related to repository management may result in the role reporting a failure if the system is not registered.
> Subscription tasks are run before repository management tasks to facilitate registration state before processing these variables.

* `rhsm_release` - Set which operating system release version to use. Remember to quote this for release versions that look like
  floats to the YAML parser, e.g.  set the value to something like `"7.4"`, not `7.4`. Values like `6Server` and `7Server` do not
  need to be quoted.
* `rhsm_release_unset` - Unset which operating system release version to use (bool, default false)
* `rhsm_repositories` - Specifies which repositories to enable/disable, details below

To enable/disable specific repositories:

```yaml
rhsm_repositories:
  enabled:
    - enabled-repository
  disabled:
    - disabled-repository
```

The list of repositories in `disabled` is processed before `enabled`.

To enable only specific repositoryies and disable all others:

```yaml
rhsm_repositories:
  only:
    - enabled-repository-1
    - enabled-repository-2
```

Using `only` is an idempotence-friendly version of the following:

```yaml
rhsm_repositories:
  disabled:
    - "*"
  enabled:
    - enabled-repository-1
    - enabled-repository-2
```

Note that globbing in repository names is supported.
Use of `only` is mutually exclusive with the use of `enabled` and `disabled`, and the use of `only` takes precedence.

To set a specific minor version of RHEL repositories to use:

```yaml
rhsm_release: "7.1"
```

To default to the latest available minor version of repositories:

```yaml
rhsm_release_unset: true
```

Role Output
-----------

> **DEPRECATION WARNING** Role outputs are deprecated, no longer supported, and will be removed
> in a future version of this role.

### oasis\_role\_rhsm

The `oasis_role_rhsm` fact will be set by this role, containing the following outputs:

- `subscribed` - Whether or not the system is registered. (bool)
- `subscribed_pool_ids` - A list of pool IDs current attached to the system. Will be an empty list if no pools are attached,
  or if the system is not currently registered.

Dependencies
------------

Requires a system that supports the installation and usage of `subscription-manager`, e.g.  Red Hat Enterprise Linux.

Privilege escalation (sudo) is required for this role to function.

Example Playbooks
-----------------

This example registers a system with a username and password, auto-attaches,
enables three RHEL 7 repositories, and explictly sets the repository release
version of enabled repositories to "7Server".

```yaml
- hosts: rhsm-servers
  roles:
    - role: rhsm
  vars:
    rhsm_username: your_username
    rhsm_password: your_password
    rhsm_auto_attach: true
    rhsm_repositories:
      only:
        - rhel-7-server-rpms
        - rhel-7-server-optional-rpms
        - rhel-7-server-extras-rpms
    rhsm_release: 7Server
```

---

This example registers a system to Red Hat Satellite 6 using an organization ID and activation key,
and attaches to a specific pool by ID.

```yaml
- hosts: rhsm-servers
  roles:
    - role: rhsm
  vars:
    rhsm_org_id: your_organization_id
    rhsm_activitionkey: activation_key
    rhsm_pool_ids:
      - poolid
    rhsm_server_hostname: your.satellite6.hostname
```

CA Certificates for Satellite 6 or Katello host should be installed first for HTTPS to work
when being used as the RHSM Provider.

License
-------

[GPLv3](LICENSE)

Author Information
------------------

Sean Myers <semyers@redhat.com>
