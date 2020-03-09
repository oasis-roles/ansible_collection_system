[![Build Status](https://travis-ci.org/oasis-roles/localectl.svg?branch=master)](https://travis-ci.org/oasis-roles/localectl)

localectl
=========

Ansible role to manage system locale settings with localectl.


Requirements
------------

Ansible 2.4 or higher

Red Hat Enterprise Linux 7 or equivalent using systemd-localed

Role Variables
--------------

Currently the following variables are supported:

### General

#### Settings

* `localectl_locales` - A dictionary of locale settings to pass to locale settings.
* `localectl_vc_keymap` - Virtual console keymap to set.
* `localectl_vc_keymap_toggle` - Virtual console toggle keymap to set.
* `localectl_x11_layout` - X11 XkbLayout option value to set.
* `localectl_x11_model` - X11 XkbModel option value to set.
* `localectl_x11_variant` - X11 XkbVariant value to set.
* `localectl_x11_options` - X11 XkbOptions value to set.

All settings default to `null`, which means that this role will do nothing by
default. With the exception of `localectl_locales`, vars can be set to an empty string
to cause that setting to be unset.

See below for more detailed information about using these variables.
For more information about localectl itself, see the `localectl(1)` manpage.

#### Privilege Escalation

* `localectl_become` - Use ansible's "become" facility to gain privileges
  required to modify system locale settings with `localectl`, default `true`.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: localectl-servers
  vars:
    localectl_locales:
      LANG: en_US.utf8
      LC_NUMERIC: en_UK.utf8
    localectl_vc_keymap: us
    localectl_x11_layout: us
  roles:
    - role: oasis_roles.system.localectl
```

System Locale Setting Notes
---------------------------

Valid locale setting values can be determined by running `localectl list-locales`
in the target environment. Those values can be used with any of the following
keys in the `localectl_locales` mapping:

```yaml
localectl_locales:
  LANG: <locale>
  LC_CTYPE: <locale>
  LC_NUMERIC: <locale>
  LC_TIME: <locale>
  LC_COLLATE: <locale>
  LC_MONETARY: <locale>
  LC_MESSAGES: <locale>
  LC_PAPER: <locale>
  LC_NAME: <locale>
  LC_ADDRESS: <locale>
  LC_TELEPHONE: <locale>
  LC_MEASUREMENT: <locale>
  LC_IDENTIFICATION: <locale>
```

`LANG` is the default locale setting used by `localectl`, so the command
`localectl set-locale en_US.utf8`, would be represented in yaml as follows:

```yaml
localectl_locales:
  LANG: en_US.utf8
```

`localectl` does not allow unsetting the system locale, so attempting
the following will result in an error:

```yaml
localectl_locales: {}
```

Virtual Console Locale Setting Notes
------------------------------------

Valid virtual console keymap setting values can be determine/d by running
`localectl list-keymaps` in the target environment. Those values can
be used with either the `localectl_vc_keymap` or the
`localectl_vc_keymap_toggle` variables.

Contrary to the `localectl` default behavior, a value given for
`localectl_vc_keymap` will not automatically be converted to
`localectl_x11_layout`. See the "`--no-convert` behavior" section below
for more details.

X11 Locale Setting Notes
------------------------

Valid X11 locale setting values can be determind by running
`localectl list-x11-layouts`, `localectl list-x11-models`,
`localectl list-x11-variants`, or `locatectl list-x11-options`
in the target environment, for the respective `localectl` role variable.

Contrary to the `localectl` default behavior, a value given for
`localectl_x11_layout` will not automatically be converted to
`localectl_vc_keymap`. See the "`--no-convert` behavior" section below
for more details.

`--no-convert` behavior
-----------------------

By default, `localectl` will "convert" a given virtual console keymap to
the x11 layout value, and vice-versa. Effectively, this means that calling
`localectl set-keymap foo` implicitly calls `localectl set-x11-keymap foo`,
and `localectl set-x11-keymap foo` implicitly calls `localectl set-keymap foo`.

To ensure accurate handling of the user-provided vars to this role, and to
ensure that this role does not do unexpected things when run, the
`set-keymap` and `set-x11-keymap` subcommands of localectl are called with
the `--no-convert` flag to disable this behavior. To emulate the default
localectl behavior, both vars should be set:

```yaml
localectl_vc_keymap: us
localectl_x11_layout: us
```

`localectl` option dependencies
-------------------------------

Both the `set-keymap` and `set-x11-keymap` subcommands of `localectl` take
multiple positional arguments, and are unable to change subsequent values
without changing all values.

This role is not opinionated with regard to how you set your locale options,
and so it will happily run with the following vars defined:

```yaml
localectl_vc_keymap_toggle: us
```

This will result in localectl being called on the target system as follows:
```
localectl --no-convert '' 'us'
```

`localectl` will succeed, will unset the virtual console keymap, and will set
the virtual console toggle keymap to 'us', resulting in an `/etc/vconsole.conf`
that looks something like this:

```
KEYMAP_TOGGLE=us
```

Note the lack of a `KEYMAP=` entry.

This is also true for the `localectl_x11_*` variables. The order of positional
arguments is `layout`, `model`, `variant`, `options`. As a result, setting
only `localectl_x11_options` will result in `layout`, `model`, and `variant`
being unset.

Furthermore, `localectl` defaults all positional arguments for the virtual
console and x11 to an empty string, which means that (for example) only
setting `layout` will result in any existing values for `model`, `variant`, or
`options` being unset.

To prevent unexpected results, explicitly defining all `localectl_vc_*` or
`localectl_x11_*` vars is recommended to ensure the intended changes are made
in an idempotent manner.

```yaml
# explicitly set virtual console keymap options
localectl_vc_keymap: us
localectl_vc_keymap_toggle: ''

# explicitly set x11 keymap options
localectl_x11_layout: ''
localectl_x11_model: ''
localectl_x11_variant: 'foo'
localectl_x11_options: ''
```

-------

GPLv3

Author Information
------------------

Sean Myers <sean.myers@redhat.com>
