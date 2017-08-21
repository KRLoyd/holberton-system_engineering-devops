# 0x09. Web server

## Description
The following files are Bash scripts that automatically perform commands to configure a Ubuntu machine.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
All Bash scripts are checked with Shellcheck, version 0.3.3.
 
## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

#### [0-transfer_gile](0-transfer_file)
Bash script that transfers a file from a client to a server.

Parameters accepted:
    - Path to the file to be transferred
    - IP of the server to transfer to
    - The username `scp` connects with
    - Path to the SSH private key that `scp` uses

Requirements:
- The file is transferred to the user home directory `~/`
- Displays `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters are passed
- Strict host key checking must be disabled

Usage: `./0-transfer_file <path-to-file> <IP> <username> <path-to-ssh-key>`

#### [1-install_nginx_web_server](1-install_nginx_web_server)
Bash script that configures a new Ubuntu machine to the following requirements:
- Install `nginx`
- Nginx must listen on port 80
- When querying Nginx at its root (`/`) with a GET request using `curl`, it returns a page containing the string "Holberton School"

#### [2-setup_a_domain_name](2-set_up_a_domain_name)
File with the domain name I registered from [Gandi](http://beta.gandi.net/).

#### [3-redirection](3-redirection)
Bash script to configure a brand new machine to the following requirements:
- All from task 1 and;
- Redirection must be a "301 Moved Permanently"

#### [4-not_found_page_404](4-not_found_page_404)
Bash script to configure a brand new machine with a custom 404 error page and with the following requirements:
- All from task 3 and;
- 404 page contains the string "Ceci n'est pas une page"

## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
