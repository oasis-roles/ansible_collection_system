def test_hostname_set(host):
    assert host.run("hostname -f").stdout.strip() == "dev.example.com"


def test_hostname_resolves(host):
    cmd = _call(host, 'dev.example.com')
    assert cmd == '1.2.3.4'


def test_hostname_aliases_resolve(host):
    cmd = _call(host, 'dev')
    assert cmd == '1.2.3.4'


def _call(host, name):
    cmd = host.run("ping -c 1 dev.example.com")
    lines = cmd.stdout.split("\n")
    line = lines[0]
    line = line[line.find('(') + 1:line.find(')')]
    return line
