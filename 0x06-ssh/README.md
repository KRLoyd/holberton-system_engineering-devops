# 0x06. SSH

## Description
Tasks in this folder include the following: connecting to a server with `ssh`, creating a key pair, and manipulating an SSH congiguration file.

### Project Notes
#### Environment
These files have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

[0-use_a_private_key](0-use_a_private_key)
Bash script that uses `ssh` to connect a server using the private key `~/.ssh/holberton` with user `ubuntu`.
Usage: `./0-use_a_private_key`

[1-create_ssh_key_pair](1-create_ssh_key_pair)
Bash script that creates a RSA key pair with the following specifications:
- name: "holberton"
- number of bits in the created key: 4096
- protected by a passphrase
Usage: `./1-create_ssh_key_pair`

[2-ssh_config](2-ssh_config)
File contains a copy of my SSH client configuration file.
Notes: Configured to use the private key `~/.ssh/holberton` and to refuse to authenticate using a password.

## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
