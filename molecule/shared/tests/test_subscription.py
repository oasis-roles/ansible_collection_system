def test_subscription_manager_installed(host):
    """Ensure subscription-manager is installed"""
    assert host.exists('subscription-manager')
