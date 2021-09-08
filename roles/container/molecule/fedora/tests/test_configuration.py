def test_service(host):
    service = host.service('podman')
    assert service.is_enabled
