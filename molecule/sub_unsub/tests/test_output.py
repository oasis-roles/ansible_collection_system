def test_subscribed(rhsm_output):
    assert not rhsm_output['subscribed']


def test_pool_ids(rhsm_output):
    assert set() == set(rhsm_output['subscribed_pool_ids'])
