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
* `rhsm_password` - access.redhat.com or Satellite (RHSM Provider) username
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
* `rhsm_pool_ids` - list of pool IDs to consume, or a list of dicts with pool IDs as keys and quantity of entitlements to consume as values
* `rhsm_consumer_type` - The type of unit to register (defaults to "system")
* `rhsm_consumer_name` - Name of the system to register (defaults to system hostname)
* `rhsm_consumer_id` - Existing consumer ID to resume a previous registration
* `rhsm_force_register` - Register the system even if it is already registered (bool, default false)
* `rhsm_unregister` - Unregister a system if true (bool, default false, system will be unsubscribed before subscription is attempted)

### Repository Management

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

Role Output
-----------

### oasis_role_rhsm

The `oasis_role_rhsm` fact will be set by this role, containing the following outputs:

- `repositories` - The complete list of subscribable repositories known to the system, as well as their enabled status.
  This value will be `false` if the `rhsm_repositories` input var is not used.
- `subscribed` - Whether or not the system is registered. (bool)
- `subscribed_pool_ids` - A list of pool IDs current attached too the system. Will be an empty list if no pools or attached,
  or if the system is not currently registered.

Dependencies
------------

Requires a system that supports the installation and usage of `subscription-manager`, e.g.  Red Hat Enterprise Linux.

Privilege escalation (sudo) is required for this role to function.

Example Playbooks
-----------------

This example registers a system with a username and password, auto-attaches,
and enables three RHEL 7 repositories.

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

BSD

Author Information
------------------

Sean Myers <semyers@redhat.com>
