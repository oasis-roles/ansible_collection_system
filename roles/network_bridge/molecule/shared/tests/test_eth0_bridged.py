def test_eth0_on_bridge(host):
    with host.sudo():
        result = host.run("brctl show br0")
    assert "eth0" in result.stdout
