def test_tmp_file(host):
    script = host.file("/tmp/network-scripts/ifcfg-eth0")
    assert script.contains("TYPE=Ethernet")
