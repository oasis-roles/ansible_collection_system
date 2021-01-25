import pytest


@pytest.mark.parametrize("protocol, port", [
    ("tcp", 80),  # Web traffic
    ("tcp", 443),  # Secure web traffic
    ("tcp", 5432),  # Postgres
])
def test_port(host, protocol, port):
    sock = host.socket("{0}://{1}".format(protocol, port))
    assert sock.is_listening
