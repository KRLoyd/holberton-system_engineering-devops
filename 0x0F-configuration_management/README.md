# 0x0F. COnfiguration management

## Description



### Project Notes
#### Environment
These Puppet manifests have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
Puppet manifests have been written so they pass `puppet-lint` and using Puppet version 3.4.


## Files
##### [0-create_a_file.pp](0-create_a_file.pp)
Puppet manifest to create a file in `/tmp`.
* Specifications:
    * File path is `/tmp/holberton`
    * File permission is `0744`
    * File owner is `www-data`
    * File group is `www-data`
    * File contains `I love Puppet`
* Usage: `puppet apply 0-create_a_file.pp`

#### [1-install_a_package.pp](1-install_a_package.pp)
Puppet maifest to install `puppet-lint` version 2.1.1.
* Usage: `puppet apply 1-install_a_package.pp`

#### [2-execute_a_command.pp](2-execute_a_command.pp)
Puppet manifest that kills a process named `killmenow` using Puppet's `exec` resource and `pkill`.
* Usgae: `puppet apply 2-execute_a_command.pp`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
