"""pytest fixtures common to all downstream test scenarios"""
import re

import pytest
import yaml


@pytest.fixture(scope='session')
def expected_repos():
    return (
        'rhel-7-server-rpms',
        'rhel-7-server-extras-rpms',
        'rhel-7-server-optional-rpms',
    )


@pytest.fixture(scope='module')
def subscribed_pool_ids(host):
    with host.sudo():
        stdout = host.check_output(
            'subscription-manager list --consumed --pool-only')
    # pool IDs are 32-char hex
    return re.findall(r'([\da-z]{32})', stdout, re.IGNORECASE)


@pytest.fixture(scope='module')
def enabled_repos(host):
    with host.sudo():
        stdout = host.check_output(
            'subscription-manager repos --list-enabled')

    enabled_repos = []
    for line in stdout.splitlines():
        if line.lower().startswith("repo id:"):
            enabled_repos.append(line.split()[-1])
    return enabled_repos


@pytest.fixture(scope='module')
def rhsm_output(request):
    # this is relative to the path to this test file, effectively assuming that
    # the output.yml file is in the same directory as any test using this
    # fixture. If we start using subdirs and such, this will need to be
    # improved.
    output_file = request.fspath.join('../output.yml')
    with output_file.open() as output:
        return yaml.load(output)
