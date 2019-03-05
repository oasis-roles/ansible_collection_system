"""
Filters for interfacing with busctl for the localectl role

This role uses the `busctl` tool, part of systemd, to inspect localectl
properties via dbus, as recommended by the systemd-localed docs:

    https://www.freedesktop.org/wiki/Software/systemd/localed/

The filters in this module serve to simplify this role's tasks by formatting
busctl's output into objects usable in ansible tasks, and to make reasonable
decisions for the purposes of idempotence. This could all be done as "pure"
ansible tasks, but those tasks would be nigh unreadable.
"""
# Normal ansible py2/py3 boilerplate
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError


def localectl_busctl_s(fields):
    # split on fields, and return the second field from the (s, value) return
    # It's possible for this value to contain escaped quotes, e.g.
    # '"\"foo\""', in which case .strip('"') will be overeager.
    # Instead, slice the string to extract everything between the first and
    # last character, thus stripping the quotes.
    return fields[1][1:-1]


def localectl_busctl_as(fields):
    # split on fields, and use the returned len to build the return

    # If we ever go py3-only, this works (proptype would be ignored):
    # proptype, proplen, *propvalues = busctl_stdout.split()
    # And there would be no need to offset the field iterator below
    values = []
    # field 0 is the return type ("as"), handled by busctl_localectl_parse
    # field 1 is the array length as returned from busctl
    # fields 2+ are the array string values
    proplen, propvalues = int(fields[1]), fields[2:]
    # could also 'for value in propvalues' here, but this makes use of the
    # length in the return string from busctl
    for i in range(proplen):
        # strip off the quotes, similar to localectl_busctl_s, but extracts
        # the "i"th field value instead of just the first field value.
        values.append(propvalues[i][1:-1])

    # special handler for the Locale property return, which explodes
    # the values list from localectl_busctl_as into a dict, and handles
    # the special "LANG" case, where if a Locale array value does not
    # contain a key, the key should default to "LANG".
    ret = {}
    for value in values:
        try:
            # split on the first equals sign only
            k, v = value.split('=', 1)
        except ValueError:
            # string did not contain '=', default to LANG
            # it's not clear if this can actually happen with the values
            # coming out of dbus for this property, but it's effectively
            # free to be paranoid here.
            k, v = 'LANG', value
        ret[k] = v
    return ret


def localectl_busctl_parse(busctl_stdout_lines, localectl_properties):
    # The actual filter, which explodes busctl_stdout to a list, and then
    # parses the value from the correct handler based on the declared type.
    # The parsed values are then zipped with the properties used to query
    # busctl, mapping the properties to their values.
    parsed = []
    for line in busctl_stdout_lines:
        fields = line.split()
        if fields[0] == 's':
            # returned stdout for a string property is: 's "<value>"'
            parsed.append(localectl_busctl_s(fields))
        elif fields[0] == 'as':
            # returned stdout for an array of string properties is:
            #  'as <len> "<value>" ["<value>" ...]'
            parsed.append(localectl_busctl_as(fields))
        else:
            raise AnsibleFilterError(
                'Unknown DBus return type: "{}"'.format(fields[0]))

    return dict(zip(localectl_properties, parsed))


def localectl_arglist(locales):
    # turns a dict of locales settings into a list of string
    # arguments for passing to 'localectl set-locale'
    # For example, '{"LANG": "foo", "LC_COLLATE": "bar"}' becomes
    # '"LANG=foo" "LC_COLLATE=bar"'
    values = []
    for k, v in locales.items():
        values.append('"{}={}"'.format(k, v))
    return ' '.join(values)


class FilterModule(object):
    def filters(self):
        return {
            'localectl_busctl_parse': localectl_busctl_parse,
            'localectl_arglist': localectl_arglist
        }
