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

* Add the control node public key becuase it disables the password access through ssh.
* Update the system and install `git`, `pip` and `oh-my-zsh`.
* Configure an static ip
* Configure git
* Remote GPIO and gpiod install
* Prepare git with signed commits

This playbook uses sshpass program to send the password to the raspberry. It is not installed by the default in mac, so it is necessary to install it with brew:

    brew install hudochenkov/sshpass/sshpass

It could be executed with the following command:

    ansible-playbook playbooks/prerequisites-playbook.yml -i hosts.yml --vault-password-file=passwords/vault-pass-file

It use de default raspberrypi configuration so it access using password.

### `funny-stuff-playbook.yml`

Extra things to _play_ with the Raspberrypi

* pihole unnatended installation

It could be executed with the following command:

    ansible-playbook playbooks/funny-stuff-playbook.yml -i hosts.yml --vault-password-file=passwords/vault-pass-file

## Ansible Vault codification

    ansible-vault encrypt_string --vault-password-file ./passwords/vault-pass-file 'YOUR_NEW_PASSORD' --name ansible_var_name 

## Ansible Vault decodification

    export cypheredsecret='$ANSIBLE_VAULT;1.1;AES256
    66336438653312345630373464663933343939393036613161316530323435666634663932346637
    6432393535651212123734623465663430656531666332660a383536616165636333626464663934
    63336236633861366437356534616636675335613036306634653364383137663530646331393439
    3361656262613638660a623136376264653564353035638768636132386231373633363538323233
    3233'
    
    echo $cypher | ansible-vault decrypt --vault-password-file ./passwords/vault-pass-file     
