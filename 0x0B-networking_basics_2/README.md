# 0x0B. Networking basics #1

## Description
The following files include answer files and Bash scripts that configure Ubuntu servers.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
All Bash scripts are checked with Shellcheck, version 0.3.3

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-localhost](0-localhost)
Answer file to the following question:

What is localhost?
1. A hostname that means this IP
2. A hostname that means this computer
3. An IP attached to a computer

##### [1-wildcard](1-wildcard)
Answer file to the following question:

What is 0.0.0.0?
1. All IPv4 addresses on the local machine
2. All the IPs
3. It means null in networking

#### [2-change_your_home_IP](2-change_your_home_IP)
Bash script that configures a Ubunutu server with the below requirements:
- localhost resolves to 127.0.0.2
- facebook.com resolves to 8.8.8.8

#### [3-show_attached_IPs](3-show_attached_IPs)
Bash script that displays all active IPv4 IPs on the machine it's executed on.

#### [4-port_listening_on_localhost](4-port_listening_on_localhost)
Bash script to listen on port 98 on localhost.


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
