# 0x10. HTTPS SSL

## Description
These tasks are all about HTTPS! Tasks include a quiz, a script to show information about subdomains, and my HAProxy configuration file.


### Project Notes
#### Environment
These Bash scripts have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
`Shellchecker` was used to check all Bash scripts.

 
## Files
Bash files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-https_abc](0-https_abc)
Answer file for the following quiz.
* What is HTTPS?
    1. A secure version of HTTP
    2. A faster version of HTTP
    3. A superior version of HTTP
* Why do you need HTTPS?
    1. To encrypt credit card and social security number information going between the client and the website servers
    2. To encrypt all communication between the client and the website servers
    3. To accelerate the communication between the client and the website servers
* You want to setup HTTPS on your website, where shall you place the certificate?
    1. In a secure location where nobody can access it
    2. You can host it anywhere but you have to share the link to it on your website
    3. On your website web server(s)

#### [1-world_wide_web](1-world_wide_web)
Bash script to display information about subdomains.
* Usage: `./1-world_wide_web <domain name> [<subdomain name>]`
    * If no subdomain is provided, the script will print information for the subdomains `www`, `lb-01`, `web-01`, and `web-2`.
    * If a subdomain is provided, the script will print information for only the specified subdomain.

#### [2-haproxy_ssl_termination](2-haproxy_ssl_termination)
Copy of my `/etc/haproxy/haproxy.cfg` configuration file.
* Specifications:
    * HAProxy listens on port TCP 443
    * HAProxy accepts SSL traffic
    * HAProxy serves encrypted traffic that will return root of web server
    * When querying the root of `uppercase.space`, the page returned contains "Holberton School"


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
