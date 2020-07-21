testinfra_hosts = ["gluster_gdeploy_default0"]


def test_is_mounted(host):
    fs = host.mount_point("/mnt/gluster_mount")
    # test-gluster_gdeploy0 is artibrarily used to mount the exported
    # volume for the purpose of this test. Therefore, we only want to
    # assert that this mount has the appropriate characteristics on that
    # particular host
    assert fs.exists
    assert fs.filesystem == 'fuse.glusterfs'
