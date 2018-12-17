# Make sure localectl set's LANG= test value.
def test_localectl_locale(host):
    host.run('localectl set-locale LANG=test')
    assert host.run('cat /etc/locale.conf').stdout == \
        'LANG=test'


# Make sure localectl sets KEYMAP test value.
def test_localectl_keymap(host):
    host.run('localectl set-keymap --no-convert test')
    assert host.run('head -1 /etc/vconsole.conf').stdout == \
        'KEYMAP=test'


# Make sure localectl does not overide x11_keymap value.
def test_localectl_x11_keymap(host):
    assert host.run(
        'grep test /etc/X11/xorg.conf.d/00-keyboard.conf')\
        .stdout != 'test'
