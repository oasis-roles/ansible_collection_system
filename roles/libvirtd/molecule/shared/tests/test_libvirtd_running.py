def test_daemon_running(host):
    libvirtd = host.service("libvirtd")
    assert libvirtd.is_running
