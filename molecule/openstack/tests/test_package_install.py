import pytest


@pytest.mark.parametrize('name', [
    ('jenkins')
])
def test_package(host, name):
    assert host.package(name).is_installed
