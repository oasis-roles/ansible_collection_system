def test_glusterd_running(host):
    gluster = host.service('glusterd')
    assert gluster.is_running
    assert gluster.is_enabled
