def test_running(host):
    host = host.get_host('local://')  # Force to connect to localhost
    with host.sudo():
        virsh = host.check_output("virsh list | grep foo.example.com")
    assert "running" in virsh
