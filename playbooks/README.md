# Playbooks

 ## Prerrequisitos

1.- Copiar el fichero ssh a la imagen para que active el servidor ssh en el primer arranque con los valores por defecto.

2.- Copiar el fichero wpa_supplicant.conf a la imagen con los datos de la red wifi para conectarse.
    
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=ES
    
    network={
     ssid="SSID"
     psk="TU-CONTRASEÑA-DE-RED"
     priority=1
    }

3.- Arrancar la imagen que será accesible mediante el dns: raspberrypi.local

4.- Generar un par de claves ssh con el comando ssh-keygen y de nombre raspberrypi.local

```yaml
    - name: Remove known hosts
    ansible.builtin.lineinfile:
    path: ~/.ssh/known_hosts
    regexp: "raspberrypi"
    state: absent

    - name: Generate SSH key "{{ssh_key_filename}}"
    openssh_keypair:
    path: "~/.ssh/{{raspberry_default_ssh_key_name}}"
    type: rsa
    size: 4096
    state: present
    force: no
```
5.- Copiar la clave pública a las raspberry y añadirla a la lista de claves autorizadas

```yaml
    - name: Send control node ssh publick key to raspberry
        ansible.builtin.command:
        argv:
            - "scp"
            - "-P {{raspberry_default_ssh_port}}"
            - "~/.ssh/{{raspberry_default_ssh_key_name}}.pub"
            - "{{raspberry_default_ssh_user}}@raspberrypi.local:/home/{{raspberry_default_ssh_user}}/"
    - name: Add public key to the allow keys in the raspberry
        ansible.builtin.command:
        argv:
            - "ssh"
            - "{{raspberry_default_ssh_user}}@raspberrypi.local"
            - "-p {{raspberry_default_ssh_port}}" 
            - "mkdir /home/{{raspberry_default_ssh_user}}/.ssh ; cat /home/{{raspberry_default_ssh_user}}/{{raspberry_default_ssh_key_name}}.pub >> /home/{{raspberry_default_ssh_user}}/.ssh/authorized_keys"
```

 ## Preparar la instalación

6.- Update system
    
    apt-get update -f

```yaml
    - name: Run the equivalent of "apt-get update" as a separate step
      become: yes
      apt:
        update_cache: yes
    - name: Update all packages to their latest version
      become: yes
      apt:
        name: "*"
        state: latest
``` 

7.- Instalar los paquetes necesarios: git y pip

    apt-get install pip git

```yaml
    - name: Install git and pip
      become: yes
      ansible.builtin.apt:
        pkg:
          - git
          - pip
```

8.- Crear un nuevo usuario davidh que pertenezca al grupo sudo
    
    sudo adduser <username>

```yaml
    - name: Create new user <davidh>
      become: yes
      ansible.builtin.user:
        append: yes
        comment: "Created with ansible"
        groups: "sudo"
        name: "{{ ansible_user }}"
        password: "{{new_user_pass}}"
```

Notas: La contraseña debe pasarse codificada en el comando de ansible: https://docs.ansible.com/ansible/latest/reference_appendices/faq.html#how-do-i-generate-encrypted-passwords-for-the-user-module y al mismo tiempo encriptada mediante ansible-vault

9.- Añadir al usuario a la lista de usuario permitidos para la conexión ssh en el fichero /etc/ssh/sshd_config

	AllowUsers <username> 

```yaml
    - name: Allow new user to use ssh
      become: yes
      ansible.builtin.lineinfile:
        path: "/etc/ssh/sshd_config"
        line: "AllowUsers {{ ansible_user }}"
        state: present
```

10.- Añadir la clave de autorizacion al nuevo usuario:

Leer el contenido de la clave pública generada en el playbook de prerrequisitos y almacenarla en una variable mediante el uso de lookups.

```yaml
    vars:
    	control_machine_public_cert: "{{ lookup('file', '/Users/davidh/.ssh/raspberrypi.local.pub') }}"
```

```yaml
    - name: Add control machine public key to authorized_key
      become: yes
      remote_user: "{{ ansible_user }}"
      ansible.builtin.lineinfile: 
        path: "/home/{{ansible_user}}/.ssh/authorized_keys"
        line: "{{control_machine_public_cert}}"
        create: yes
        state: present
        group: "{{ ansible_user}}"
        owner: "{{ ansible_user}}"
        mode: "0600"
```

11.- Denegar el acceso a la raspberry mediante ssh con clave en el fichero /etc/ssh/sshd_config

    PasswordAuthentication no 

```yaml
    - name: Disable password access via ssh
      become: yes
      ansible.builtin.lineinfile:
        path: "/etc/ssh/sshd_config"
        line: "PasswordAuthentication no"
        state: present
```

12.- Cambiar el puerto por defecto del servicio ssh en el fichero /etc/ssh/sshd_config

    Port 2222

```yaml
    - name: Change default ssh port to {{ new_ssh_port }}
      become: yes
      ansible.builtin.lineinfile:
        path: "/etc/ssh/sshd_config"
        line: "Port {{new_ssh_port}}"
        state: present
```

13.- Eliminar el usuario por defecto pi
    
    sudo deluser pi

```yaml
    - name: Delete default pi user
      become: yes
      ansible.builtin.user:
        name: pi
        state: absent
        remove: yes
```

14.- Reiniciar el servicio ssh

```yaml
    - name: Reload ssh service
      become: yes
      ansible.builtin.service:
        name: ssh
        state: reloaded
```

15.- Establecer la dirección ip estática

```yaml
    - name: Set static ip
      become: yes
      ansible.builtin.lineinfile:
        path: "/etc/dhcpcd.conf"
        line: "{{ item }}"
        state: present
      with_items:
        - "interface wlan0"
        - "static ip_address={{ new_static_ip }}"
        - "static routers={{ new_static_router }}"
        - "static domain_name_servers={{ new_static_dns }}"
```

16.- Reiniciar para aplicar los cambios

```yaml
    - name: Unconditionally reboot the machine with all defaults
      become: yes
      reboot:
```

17.- Instalar oh my zsh y sus plugins. Lo hacemos aplicando un rol de Ansible

```yaml
    - role: gantsign.antigen
      users:
        - username: "{{ new_user }}"
          antigen_libraries:
            - name: oh-my-zsh
          antigen_theme:
            name: "gnzh"
          antigen_bundles:
            - name: git
            - name: pip
            - name: command-not-found
            - name: zsh-syntax-highlighting # `name` is required (any valid file name will do so long as it's unique for the bundles)
              url: zsh-users/zsh-syntax-highlighting
```

## Trabajo posterior en el nodo de control

Añadir la nueva configuración ssh al usuario en el host en el fichero ~/.ssh/config
Host raspberrypi.local
	HostName raspberrypi.local
	Port 2222
	IdentityFile ~/.ssh/raspberrypi.local
	User dhernandez


Para la configuración de la red:

https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line


En la raspberry hay que configurar el acceso remoto a GPIO:

    COMMAND
    ------
    sudo raspi-config
        3 Interface Options
        I8 Remote GPIO

Demonio para el control del GPIO como un demonio:

	COMMAND
	-----------
	sudo pigpiod

	DESCRIPTION
	--------------
	pigpiod is a utility which launches the pigpio library as a daemon.
	Once launched the pigpio library runs in the background accepting commands from the pipe and socket interfaces.
	The pigpiod utility requires sudo privileges to launch the library but thereafter the
	pipe and socket commands may be issued by normal users.

En el cliente hay que exportar la variable de entorno con la dirección de la raspberrypi

    COMMANDS
    --------
    ping raspberrypi.local
    export PIGPIO_ADDR=192.168.0.22

Y si fuera necesario un puerto sin el valor por defecto.

    export PIGPIO_PORT=8888

ansible-playbook playbooks/prerequisites-playbook.yml -i hosts.yml

ansible-playbook playbooks/raspberry-playbook.yml -i hosts.yml --vault-password-file=passwords/vault-pass-file

