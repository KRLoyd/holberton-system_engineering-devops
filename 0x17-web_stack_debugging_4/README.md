# 0x17. Web stack debugging #4

## Description
Holberton's fifth assigned debugging task.
* Problem: When testing how well a web server setup with Nginx is doing under pressure, there is a large amount of failed requests.
* Solution: Provided in Puppet manifest [0-the_sky_is_the_limit_not.pp](0-the_sky_is_the_limit_not.pp).

### Project Notes
#### Environment
This Puppet manifest has been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).

#### Style
`puppet-lint` was used to check the Puppet manifest. Written in Puppet v3.4.


## Files

##### [0-the_sky_is_the_limit_not.pp](0-the_sky_is_the_limit_not.pp)
Puppet manifest that fixes the provided web stack by updating the `ulimit` in file `/etc/default/nginx`.
* Usage: `puppet apply 0-the_sky_is_the_limit_not.pp`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
