def test_running(host):
    host = host.get_host('local://')  # Force to connect to localhost
    virsh = host.check_output("virsh list")
    assert "foo.example.com" in virsh
