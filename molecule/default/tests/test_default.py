"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_backports(host):
    """Verify that the backports package repository was added."""
    distribution = host.system_info.distribution
    codename = host.system_info.codename

    supported_distributions = ["debian", "ubuntu"]
    unsupported_releases = ["bullseye"]

    # The backports package repo should be present for any Debian or Ubuntu
    # release other than those found in `unsupported_releases`.
    if distribution in supported_distributions:
        cmd = host.run("apt-cache policy")
        assert cmd.rc == 0

        if codename not in unsupported_releases:
            assert f"{codename}-backports" in cmd.stdout
        else:
            assert f"{codename}-backports" not in cmd.stdout
