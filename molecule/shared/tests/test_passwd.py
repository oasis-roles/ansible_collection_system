def test_passwd_hash(host):
    """Ensure password hash matches what was set via passwd_password var"""
    pw_hash = '$6$aCI4uLaYjEOmu19b$jqI/2h.edztO9AsZO1vG0owuRcGWmhwM9hIcD2X0EDdiLSsIidPZ5RaQJ53ZMPFReTvkQwMmi4ckFaWA.1JWQ0' # noqa
    with host.sudo():
        assert host.user('root').password == pw_hash
