def test_unsubscribed(host):
    with host.sudo():
        result = host.run('subscription-manager status')
    # system should be unsubscribed
    assert result.rc == 1
