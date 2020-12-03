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

    # The backports package repo should be present for any Debian
    # other than Debian testing, which is currently bullseye.
    if distribution == "debian":
        cmd = host.run("apt-cache policy")
        assert cmd.rc == 0

        if codename != "bullseye":
            assert f"{codename}-backports" in cmd.stdout
        else:
            assert f"{codename}-backports" not in cmd.stdout
