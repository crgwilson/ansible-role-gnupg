import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('package', [
    ('haveged'),
    ('gnupg2')
])
def test_default_packages(host, package):
    p = host.package(package)
    assert p.is_installed
