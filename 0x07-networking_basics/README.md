# 0x07. Networking basics #0

## Description
The files in this folder are answer file to questions about the OSI model and it's various layers, as well as some Bash scripts.

### Project Notes
#### Environment
These functions have been tested on Ubuntu 14.04.5 LTS.
Tests and development are done in VirtualBox on Ubuntu via Vagrant(1.8.1).

## Files
All files must be executable to run. To add executable permissions to any file: `chmod u+x file_name`

[0-OSI_model](0-OSI_model)
File containing the answers to the following questions:
What is the OSI model?
1. Set of specifications that network hardware manufacturers must respect
2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard to their underlying internal structure and technology

How is the OSI model organized?
1. Alphabetically
2. From the lowest to the highest level
3. Randomly

[1-types_of_network](1-types_of_network)
File containing the answers to the following questions:
On what type of network are Holberton iMacs connected to?
1. Internet
2. WAN
3. LAN

What type of network could connect the Holberton HQ office with the Holberton-Gandi office?
1. Internet
2. WAN
3. LAN

What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?
1. Internet
2. WAN
3. LAN

[2-MAC_and_IP_address](2-MAC_and_IP_address)
File containing the answers to the following questions:
What is a MAC address?
1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface

What is an IP address?
1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

[3-UDP_and_TCP](3-UDP_and_TCP)
![Comic of UDP and TCP](http://i.imgur.com/bg9rSUy.jpg)
File containing the answers to the following questions about the above comic:

Which statement is correct for the TCP box:
1. Is a protocol that is transferring data in a slow way but surely
2. Is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the UDP box:
1. Is a protocol that is transferring data in a slow way but surely
2. Is a protocol that is transferring data in a fast way and might loss data along in the process

Which statement is correct for the TCP worker:
1. Have you received boxes x, y, z?
2. May I increase the rate at which I am sending you boxes?

[4-TCP_and_UDP_ports](4-TCP_and_UDP_ports)
Bash script that displays listening ports with the following specifications:
- only listening ports are shown
- PID name and name of the program to which each socket belongs are shown
Usage: `sudo ./4-TCP_and_UDP_ports`

[5-is_the_host_on_the_network](5-is_the_host_on_the_network)
Bash script that pings an IP address passed as an argument 5 times.
Usage: `./5-is_the_host_on_the_network <ip_address>`

## Authors
Kristen Loyd        [Github](https://github.com/KRLoyd) |  [LinkedIn](https://www.linkedin.com/in/kristen-loyd-34984a92)

## License
Public Domain, no copyright protection

