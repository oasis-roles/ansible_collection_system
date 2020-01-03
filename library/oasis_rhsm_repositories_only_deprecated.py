#!/usr/bin/python
# This module only exists to inform users about the deprecation of the 'only'
# key in the rhsm_repositories var used by this role.
from ansible.module_utils.basic import AnsibleModule

msg = '''Use of the 'only' key in the rhsm_repositories variable for the
oasis_roles.rhsm role is deprecated. Please change your playbooks to use the
'enabled' and 'disabled' keys accordingly to suppress this warning'''


def main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    module.deprecate(msg)
    module.exit_json(changed=False)


if __name__ == '__main__':
    main()
