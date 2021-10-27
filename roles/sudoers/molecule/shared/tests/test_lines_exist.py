def test_wheel_line_exists(host):
    with host.sudo():
        cont = host.file("/etc/sudoers.d/groups_no_password")
        assert cont.contains("%wheel ALL=(ALL) NOPASSWD: ALL")


def test_cloud_user_line_exists(host):
    with host.sudo():
        cont = host.file("/etc/sudoers.d/sudoers_no_password")
        assert cont.contains("cloud-user ALL=(ALL) NOPASSWD: ALL")
