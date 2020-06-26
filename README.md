# Ansible role: GnuPG

![Molecule Test](https://github.com/crgwilson/ansible-role-gnupg/workflows/Molecule%20Test/badge.svg)

Install and manage [GnuPG packages](https://gnupg.org/)


## Variables

### `gnupg_install_entropy_daemon` - bool

Install [haveged](https://www.issihosts.com/haveged/) to supply enough entropy to facilitate generating GPG keys on virtual machines


### `gnupg_entropy_daemon_packages` - list(str)

The list of packages to install haveged


### `gnupg_packages` - list(str)

The list of packages to install GnuPG (defaults to `gnupg2`)


## TODO

* Manage keys, trust, and keyrings


## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
