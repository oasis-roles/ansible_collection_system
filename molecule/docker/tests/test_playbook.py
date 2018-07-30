def test_kdump_running_and_enabled(host):
    chronyd = host.service("chronyd")
    assert chronyd.is_running
    assert chronyd.is_enabled
