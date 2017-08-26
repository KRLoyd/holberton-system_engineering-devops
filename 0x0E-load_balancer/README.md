# 0x0E. Load Balancer

## Description
Holberton provides 2 more servers to add redundancy for my web servers. The files in the repository are Bash scripts to configure a new Ubuntu server to match task requirements.  


### Project Notes
#### Environment
These Bash scripts have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
`Shellchecker` was used to check all Bash scripts.

 
## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-custom_http_response-header](0-custom_http_response-header)
Bash script to configure Nginx so its HTTP response contains a custom header.
* Specifications:
    * Name of custom header: "X-Served-By"
    * Value of custom header is the hostname of the server Nginx is running on
* Usage: `./0-custom_http_response-header`

#### [1-install_load_balancer](1-install_load_balancer)
Bash script to install and configure HAProxy on my load balaning server.
* Specifications:
    * Configure HAProxy with version >=1.5 to send traffic to my 2 web servers
    * Distribute resquests using roundrobin algorithm
    * HAProxy must be able to be managed via the init script
* Usage: `./1-install_load_balancer`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
