# 0x12. Firewall

## Description
The tasks in this project are about firewalls. One file contains answers to a quiz, while the other contains the commands used to configure my firewall.


### Project Notes
#### Environment
These Bash scripts have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
`Shellchecker` was used to check all Bash scripts.


## Files
All Bash scripts must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-firewall_ABC](0-firewall_ABC)
Answer file for the following quiz.
* What is a firewall?
    1. A hardware security system
    2. A hardware or software security system
    3. A software security system
* What are the 2 types of firewall:
    1. Soft and hard firewall
    2. Incoming and outgoing firewall
    3. Network and host-based firewall
* What is the main function of a firewall?
    1. To filter incoming and outgoing network traffic
    2. To filter incoming and outgoing TCP traffic
    3. To filter outgoing traffic

#### [1-block_all_incoming_traffic_but](1-block_all_incoming_traffic_but)
File containing the `ufw` commands to setup some rules on one of my web servers.
* Specifications:
    * Block all incoming traffic except the following TCP ports
        * 22 (SSH)
        * 443 (HTTPS SSL)
        * 80 (HTTP)


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
