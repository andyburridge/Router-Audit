# Router Audit

## Description 
Using Netmiko, SSH to a list of routers taken from a given text file and perform an audit, returning the following information on each router:
- Router hostname
- IOS image currently running on the router
- MTU value configured on the tunnel.  This tunnel is Tu100 for 'primary' routers, Tu200 for 'secondary' routers
- Whether dead peer detection (DPD) configuration is present in the running config
- Whether 'ip tcp adjust-mss' has been set on the tunnel.  This tunnel is Tu100 for 'primary' routers, Tu200 for 'secondary' routers
- IP fragmentation statistics	

Python 2.7


## Prerequisites

Netmiko, Paramiko


## Usage

./routerAudit.py <textfile> <username> <password>
where:
- <textfile> a list of router IP addresses to connect to.  Any lines that start with a '#' are igorned as comments.	
- <username> the username used for authentication to the devices
- <password> the password used for authentication to the devices

Script outputs a text file in the /Output/ subdirectory that contains the audit information in a comma separated format.		


## Author

Andrew Burridge
