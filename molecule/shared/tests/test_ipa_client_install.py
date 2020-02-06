def test_command_exists(host):
    assert host.find_command('ipa-client-install') != ''
