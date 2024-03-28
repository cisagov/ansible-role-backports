# ansible-role-backports #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-backports/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-backports/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-backports/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-backports/actions/workflows/codeql-analysis.yml)

This Ansible role adds the [backports](https://backports.debian.org/)
[package repositories](https://backports.debian.org/Instructions/) for
supported Debian releases.  It does the same for
[Ubuntu backports](https://help.ubuntu.com/community/UbuntuBackports) with
supported releases.

## Requirements ##

None.

## Role Variables ##

None.

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: skeleton
  src: https://github.com/cisagov/skeleton-ansible-role
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Add backports repository
      ansible.builtin.include_role:
        name: backports
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
