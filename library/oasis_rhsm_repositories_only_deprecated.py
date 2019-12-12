#!/usr/bin/python

# (c) 2018, Sean Myers <sean.myers@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# This module only exists to inform users about the deprecation of the 'only'
# key in the rhsm_repositories var used by this role.

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

msg = '''Use of the 'only' key in the rhsm_repositories variable for the
oasis_roles.rhsm role is deprecated. Please change your playbooks to use the
'enabled' and 'disabled' keys accordingly to suppress this warning'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    module.deprecate(msg)

    module.exit_json(changed=False)


if __name__ == '__main__':
    main()
