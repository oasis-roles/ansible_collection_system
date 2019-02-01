def test_subscribed(rhsm_output):
    assert rhsm_output['subscribed']


def test_pool_ids(rhsm_output):
    assert 'subscribed_pool_ids' in rhsm_output
