def test_enabled_repos(expected_repos, enabled_repos):
    """Test that expected repos are enabled (subscribed)"""
    # While it is generally expected that the rhsm_repository module will work,
    # this test asserts that the role repository handling is handing inputs to
    # the module correctly.
    assert set(expected_repos) == set(enabled_repos)
