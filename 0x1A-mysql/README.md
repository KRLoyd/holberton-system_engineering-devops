# 0x1A. Mysql

## Description
The files in this directory correlate with the Holberton School project to set up a Primary-Replica infrastructure and backup using MySQL.


### Project Notes
#### Environment
Bash scripts have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).
#### Style
`Shellchecker` was used to check all Bash scripts.


## Files
All scripts must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

##### [0-mysql_configuration_primary](0-mysql_configuration_primary)
A copy of my MySQL primary server configuration file.

##### [0-mysql_configuration_replica](0-mysql_configuration_replica)
A copy of my MySQL replica server configuration file.

##### [1-mysql_backup](1-mysql_backup)
Bash script that generates a MySQL dump and creates a compressed archive out of it.
* Notes:
  * The MySQL dump is named `backup.sql` and contains all MySQL databases in the server
  * The MySQL dump is compressed to a `tar.gz` archive named in the following format:
    * `day-month-year.tar.gz`
  * The user `root` is used to connect to the MySQL database
* Usage: `./1-mysql_backup <password>`


## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection