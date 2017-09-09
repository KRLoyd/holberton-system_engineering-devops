# 0x15. Web stack debugging #3

## Description
Holberton's fourth assigned debugging task.
* Problem: A Wordpress website running on a LAMP (Linux, Apache, MySQL, and PHP) stack is returning a 500 error from Apache.
* Solution: Provided in Puppet manifest [0-strace_is_your_friend.pp](0-strace_is_your_friend.pp).

### Project Notes
#### Environment
This Puppet manifest has been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).

#### Style
`puppet-lint` was used to check the Puppet manifest. Written in Puppet v3.4.


## Files

##### [0-strace_is_your_friend](0-strace_is_your_friend.pp)
Puppet manifest that fixes the provided web stack.
* Usage: `puppet apply 0-strace_is_your_friend.pp`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection
