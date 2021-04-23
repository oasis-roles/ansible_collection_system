def test_upload_settings(host):
    derp = host.file('/derp')
    assert derp.contains('DERP!')
    assert derp.user == 'root'
    assert derp.group == 'wheel'


def test_root_not_changed(host):
    root = host.file('/')
    assert root.group == 'root'
    assert root.user == 'root'


def test_upload_minimal(host):
    authors = host.file('/main.yml')
    assert authors.contains('-')
