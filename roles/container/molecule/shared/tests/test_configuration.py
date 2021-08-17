# def test_user_in_group(host):
#     user = host.user('fedora')
#     assert 'docker' in user.groups


def test_service(host):
    service = host.service('docker')
    assert service.is_running
    assert service.is_enabled
