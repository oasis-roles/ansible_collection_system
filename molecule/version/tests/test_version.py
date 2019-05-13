def test_version_is_correct(host):
    version = host.command('rpm -q --qf "%{version}" redhat-storage-server')
    assert version.stdout == "3.1.3.0"
