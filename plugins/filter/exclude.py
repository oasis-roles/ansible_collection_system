from jinja2.runtime import Undefined


def exclude_join(value):
    '''Return a string representation of the list of values in the
    exclude field of the passed dict.

    Ansible does not provide us an easy way to omit the value directly in
    existing Jinja filters if there is no list while also joining the
    values together when there is a list. Returning "Undefined" from here
    allows us to default to omitting the value while stlil getting the
    joined string if the value is defined'''
    if 'exclude' in value:
        return ' '.join(value['exclude'])
    return Undefined()


def get_rpm_keys(value):
    '''Extracts values from the passed list and returns a new list that is
    a combination of those values.

    Both the keys 'gpgkey' and 'gpgcakey' are optional configurations for
    yum repositories. This method transforms the provided list into a single
    list that includes every value of those two keys from the original list,
    flattened together. If no elements of the original list include either
    key, then an empty list is returned.'''
    keys = [k['gpgkey'] for k in value if 'gpgkey' in k]
    cakeys = [k['gpgcakey'] for k in value if 'gpgcakey' in k]
    return keys + cakeys


class FilterModule(object):
    def filters(self):
        return {
            'system_repositories_exclude_join': exclude_join,
            'system_repositories_gpgkeys': get_rpm_keys
        }
