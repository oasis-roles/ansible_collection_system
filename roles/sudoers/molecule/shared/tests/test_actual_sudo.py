def test_sudo_as_fedora(host):
    with host.sudo("fedora"):
        with host.sudo():
            who = host.check_output("whoami")
            assert who == "root"


def test_sudo_as_arya(host):
    with host.sudo("arya"):
        with host.sudo():
            who = host.check_output("whoami")
            assert who == "root"
