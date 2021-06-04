import pytest


@pytest.mark.parametrize('name', [
    ('gcc-debuginfo')
])
def test_package(host, name):
    assert host.package(name).is_installed
