# Web infrastructure design \#0

## Purpose
To be able to do the following:
* Draw a diagram for a simple web stack
* Explain what each compenent is doing
* Explain system redundancy
* Know these acronyms: LAMP, SPOF, QPS

### Files
[0-simple_web_stack](0-simple_web_stack) Design for a simple web infrastructure with the following components:
* 1 server
* 1 web server (Nginx)
* 1 code base
* 1 database (MySQL)
* 1 domain name (foobar.com) configured with a www record to server IP

[1-distributed_web_infrastructure](1-distributed_web_infrastructure) Design for a distributed web infrastructure that builds on the previous, adding the following:
* 2 servers
* 1 web server (Nginx)
* 1 load-balancer (HAproxy)
* 1 code base
* 1 database (MySQL)

[2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure) Design for a distributed, secured, and monitored web infrastructure that builds on the previous, adding the following:
* 3 firewalls
* 1 SSL certificate (for www.foobar.com)
* 3 monitoring clients (data collector for Sumologic or other monitoring services)
