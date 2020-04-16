def test_running(host):
    with host.sudo():
        virsh = host.check_output("virsh list")
    assert "foo.example.com" in virsh
