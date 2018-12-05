from jinja2.runtime import Undefined


def exclude_join(value):
    if 'exclude' in value:
        return ' '.join(value['exclude'])
    return Undefined()


def get_rpm_keys(value):
    keys = [k['gpgkey'] for k in value if 'gpgkey' in k]
    cakeys = [k['gpgcakey'] for k in value if 'gpgcakey' in k]
    return keys + cakeys


class FilterModule(object):
    def filters(self):
        return {
            'system_repositories_exclude_join': exclude_join,
            'system_repositories_gpgkeys': get_rpm_keys
        }
