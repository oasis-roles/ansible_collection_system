import pytest


@pytest.mark.parametrize('name', [
    ('google-chrome-stable')
])
def test_package(host, name):
    assert host.package(name).is_installed
