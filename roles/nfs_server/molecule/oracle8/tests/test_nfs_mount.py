def test_mount(host):
    # by using a routable IP address for the NFS mount we are able to test the
    # firewall configuration even from localhost
    ip_addr = host.ansible.get_variables()['ansible_host']
    with host.sudo():
        cmd = host.run('mount {}:/srv/share1 /mnt'.format(ip_addr))
        assert cmd.rc == 0


def test_file_write(host):
    assert host.run('echo "test" > /mnt/test_file.txt').rc == 0


def test_file_read(host):
    assert host.run('cat /mnt/test_file.txt').stdout[:-1] == 'test'


def test_umount(host):
    with host.sudo():
        assert host.run('umount /mnt').rc == 0
