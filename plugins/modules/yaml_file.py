#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO: The following items are nice-to-haves that have not yet been found to
# be necessary, but could be beneficial in the future:
# * append to list vs replace. A use case might call for modifying the contents
#   of a list rather than needing to replace it every time. An option could be
#   added to append to a list
# * truncate a list. Reduce the length of a list to only equal to a given size
# * allow special characters in an identifier, such as ".", with an escape

from __future__ import (absolute_import, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ['preview']}

DOCUMENTATION = '''
---
module: yaml_file
short_description: add or modify fields in a YAML file
description:
    - Modify YAML files programmatically
options:
  create:
    description:
      - Create the file, if not found. Only has meaning if `state` is set to
        `present`.
    type: bool
    default: true
  key:
    description:
      - The key in the file to modify. Child objects should be referenced
        with a '.', elements of a list with a '[...]'. Use '[2]' to indicate
        the particular index within the list or '[]' to indicate all elements
        within the list should be modified.
    required: true
  path:
    description:
      - Path of the file to modify
    required: true
    type: path
    aliases: ['file', 'dest']
  state:
    description:
      - `present` to add/modify values, `absent` to delete them
    default: 'present'
    choices: ['absent', 'present']
  value:
    description:
      - The value of the key(s) to set. Required if `state` is `present`
'''

from ansible.module_utils.basic import AnsibleModule  # noqa: E402
from yaml import load, dump  # noqa: E402
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import os  # noqa: E402
import re  # noqa: E402
# Used to deep-compare two dictionaries
import json  # noqa: E402


class Yaml(object):
    def __init__(self, args):
        self.create = args['create']
        self.path = os.path.expanduser(args['path'])
        self.state = args['state']
        self.key = args['key']
        self.value = args['value']

    def check_module_arguments(self):
        """Execute a basic set of sanity checks.

        Checks some basic pre-conditions before the module attempts to run so
        that these things don't need to be checked for later on.

        :returns: (boolean, string) where the first element says whether the
        check passed and the second includes an appropriate error message if it
        did not."""
        # Check that file exists if state is 'present'
        if self.state == 'present' and not self.create:
            if not os.path.isfile(self.path):
                return (False, "File not found when state is 'present'. Create"
                        " disabled")
        # Be sure proper arguments are specified
        if self.state == 'present' and self.value is None:
            return False, 'When state is "present", a value must be specified'
        # Parse the key value
        try:
            self.key_list = re.findall(r'([-\w]+|\[\d*\])', self.key)
            if len(self.key_list) == 0:
                return False, "No key value parsed. Please check the syntax."
        except Exception as ex:
            return False, ex.msg
        # Massage "value" into expected type
        if self.value is not None:
            self.value = json.loads(self.value)
        self.read_file()
        return True, ''

    def read_file(self):
        """Read the current state of the file.

        Reads the current YAML file into memory, returns an empty dict if
        the file does not exist or the parsed object if it does."""
        if not os.path.isfile(self.path):
            self.obj = dict()
        else:
            with open(self.path, 'r') as stream:
                self.obj = load(stream, Loader=Loader)
                if self.obj is None:
                    self.obj = dict()

    def write_file(self):
        """Write the object to the target file.

        Writes the value of data to the YAML file.

        :param data: A dict of values to write out
        :returns: nothing"""
        with open(self.path, 'w') as stream:
            dump(self.obj, stream, default_flow_style=False, Dumper=Dumper)

    def present(self):
        return self._present(self.obj, self.key_list)

    def _present(self, obj, keys):
        """Recursively walks to a specified key in the file.

        :param obj: The current level of the object that is being walked
        :param keys: A list of key fragments to walk to
        :param value: The value to assign to the given key
        :returns: True if changes were made, False otherwise"""
        if len(keys) == 1:
            if json.dumps(obj.get(keys[0], None), sort_keys=True) == \
                    json.dumps(self.value):
                return False
            else:
                obj[keys[0]] = self.value
                return True
        else:
            if keys[0] not in obj:
                obj[keys[0]] = dict()
            return self._present(obj[keys[0]], keys[1:])

    def absent(self):
        return self._absent(self.obj, self.key_list)

    def _absent(self, obj, keys):
        if len(keys) == 1:
            if isinstance(obj, dict) and keys[0] in obj:
                del obj[keys[0]]
                return True
            elif not isinstance(obj, dict):
                raise Exception("Cannot subscript type found: {}".format(obj))
            else:
                return False
        else:
            if keys[0] in obj:
                return self._absent(obj[keys[0]], keys[1:])
            else:
                return False


def main():
    module = AnsibleModule(
        argument_spec=dict(
            create=dict(type='bool', default=False),
            key=dict(type='str', required=True),
            path=dict(type='str', aliases=['file', 'dest'], required=True),
            state=dict(type='str', choices=['absent', 'present'],
                       default='present'),
            value=dict(type='json')
        )
    )
    yaml = Yaml(module.params)
    check = yaml.check_module_arguments()
    if not check[0]:
        module.fail_json(msg=check[1])
    else:
        if module.params['state'] == 'present':
            changes = yaml.present()
        else:
            changes = yaml.absent()
        if changes:
            yaml.write_file()
        module.exit_json(changed=changes)


if __name__ == '__main__':
    main()
