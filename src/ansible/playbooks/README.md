# Playbooks

 ## Prerrequisitos

1.- Crear una imagen en una tarjeta de memoria usando el programa Raspberry Pi Imager. Esta imagen debe estar configurada el usuario por defecto de raspberry `pi` y su contraseña por defecto `raspberrypi`. También debe estar configurada la red wifi. Se ddeberá establecer el nombre del servidor como `raspberrypi.local` para que sea accesible mediante el servicio de Multicast DNS. Finalmente activar el servicio ssh con autenticación por contraseña.

2.- Arrancar la imagen que será accesible mediante el dns: raspberrypi.local

3.- Generar un par de claves ssh con el comando ssh-keygen y de nombre raspberrypi.local

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
4.- Copiar la clave pública a las raspberry y añadirla a la lista de claves autorizadas. Este proceso se realiza mediante el uso de sshpass para enviar la contraseña al comando scp y ssh. Justo debajo se muestra el código necesario para realizar esta tarea en dos formatos diferentes: mediante el uso de los módulos de ansible y mediante el uso de comandos de shell.

```yaml
    - name: Send control node ssh publick key to raspberry
      ansible.builtin.shell: sshpass -v -p {{raspberry_default_user_password}} scp -o StrictHostKeyChecking=no -P {{raspberry_default_ssh_port}} ~/.ssh/{{raspberry_default_ssh_key_name}}.pub {{raspberry_default_ssh_user}}@raspberrypi.local:/home/{{raspberry_default_ssh_user}}/
    - name: Add public key to the allow keys in the raspberry
      ansible.builtin.command:
        argv:
          - "sshpass" 
          - "-v" 
          - "-p"
          - "{{raspberry_default_user_password}}"
          - "ssh"
          - "{{raspberry_default_ssh_user}}@raspberrypi.local"
          - "-p {{raspberry_default_ssh_port}}" 
          - "mkdir /home/{{raspberry_default_ssh_user}}/.ssh ; cat /home/{{raspberry_default_ssh_user}}/{{raspberry_default_ssh_key_name}}.pub >> /home/{{raspberry_default_ssh_user}}/.ssh/authorized_keys"
```

 ## Preparar la instalación

6.- Update system
    
    apt-get update -f

```yaml
    - name: Run the equivalent of "apt-get update" as a separate step
      become: true
      apt:
        update_cache: yes
    - name: Update all packages to their latest version
      become: true
      apt:
        name: "*"
        state: latest
``` 

7.- Instalar los paquetes necesarios: git y pip

    apt-get install pip git

```yaml
    - name: Install git and pip
      become: true
      ansible.builtin.apt:
        pkg:
          - git
          - pip
```

8.- Crear un nuevo usuario davidh que pertenezca al grupo sudo
    
    sudo adduser <username>

```yaml
    - name: Create new user <davidh>
      become: true
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
      become: true
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
      become: true
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
      become: true
      ansible.builtin.lineinfile:
        path: "/etc/ssh/sshd_config"
        line: "PasswordAuthentication no"
        state: present
```

12.- Cambiar el puerto por defecto del servicio ssh en el fichero /etc/ssh/sshd_config

    Port 2222

```yaml
    - name: Change default ssh port to {{ new_ssh_port }}
      become: true
      ansible.builtin.lineinfile:
        path: "/etc/ssh/sshd_config"
        line: "Port {{new_ssh_port}}"
        state: present
```

13.- Eliminar el usuario por defecto pi
    
    sudo deluser pi

```yaml
    - name: Delete default pi user
      become: true
      ansible.builtin.user:
        name: pi
        state: absent
        remove: yes
```

14.- Reiniciar el servicio ssh

```yaml
    - name: Reload ssh service
      become: true
      ansible.builtin.service:
        name: ssh
        state: reloaded
```

15.- Establecer la dirección ip estática

```yaml
    - name: Set static ip
      become: true
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
      become: true
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
	User davidh


Para la configuración de la red:

https://www.raspberrypi.com/documentation/computers/configuration.html#wireless-networking-command-line



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

En el cliente hay que exportar la variable de entorno con la dirección de la raspberrypi o en el programa python cambiar la factoria que genera los pins:

```python
from gpiozero.pins.pigpio import PiGPIOFactory
factory = PiGPIOFactory('192.168.1.5')
led = LED(17, pin_factory=factory) # remote pin
```

    COMMANDS
    --------
    ping raspberrypi.local
    export PIGPIO_ADDR=192.168.0.22

Y si fuera necesario un puerto sin el valor por defecto.

    export PIGPIO_PORT=8888

ansible-playbook playbooks/prerequisites-playbook.yml -i hosts.yml

ansible-playbook playbooks/raspberry-playbook.yml -i hosts.yml --vault-password-file=passwords/vault-pass-file

