def test_subscribed(rhsm_output):
    assert rhsm_output['subscribed']


def test_pool_ids(rhsm_output, expected_pool_ids):
    assert set(expected_pool_ids) == set(rhsm_output['subscribed_pool_ids'])
