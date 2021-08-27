def test_service(host):
    service = host.service('docker')
    assert service.is_running
    assert service.is_enabled
