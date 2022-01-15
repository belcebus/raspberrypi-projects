# Ansible: Raspberry preparation

## Description

This project contains the files used by Ansible to configure the Raspberry after the image installation.

## Prerrequisites

A Raspberrypi running in the same network with the raspbian default system installed. Create a file named `wpa_supplicant.conf` in the image root filesystem before starting it. Instructions [here](https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line).

The SSH service up and running in the Raspberrypi: create an empty file named `ssh` in the image root before starting it.

## Inventory file

### `hosts.yml`

Only one host is defined in this file: `raspberrypi`. We can leverage into the [Multicast DNS](https://en.wikipedia.org/wiki/Multicast_DNS) service to locate the Raspberrypi server in the intranet by its _dot-local_ name: `raspberrypi.local`.

## Playbooks files

### `prerrequisites-playbook.yml`

The playbook to prepare the control node and the raspberry to use Ansible. It creates the ssh keys and send the public one to the raspberry and add it to the `authorized_keys` file.

It could be executed with the following command:

    ansible-playbook playbooks/prerequisites-playbook.yml -i hosts.yml

It use de default raspberrypi configuration so it access using password.

### `raspberry-playbook.yml`

The playbook to change all the default configurations to avoid security problems to configure it the way I like, that is:

* Change ssh default port to another defined in the inventory file vars section.
* Create a new sudoer user
* Add the control node public key created in the prerrequisites playbook becuase it disables the password access through ssh.
* Update the system and install `git`, `pip` and `oh-my-zsh`.
* Remove default `pi` user.
* Configure an static ip

It could be executed with the following command:

    ansible-playbook playbooks/raspberry-playbook.yml -i hosts.yml --vault-password-file=passwords/vault-pass-file

### `funny-stuff-playbook.yml`

Extra things to _play_ with the Raspberrypi

It could be executed with the following command:

    ansible-playbook playbooks/funny-stuff-playbook.yml -i hosts.yml