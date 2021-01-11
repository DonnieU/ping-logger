# Ping and Packet Loss Logger (IPv4)

Simple ping and logging script to monitor packet loss between source and target.


Requires python 3.6 or later and `icmplib`: https://pypi.org/project/icmplib/


Only tested on Ubuntu 20.04.1 LTS via Windows Subsystem for Linux (WSL) w/ Python 3.8.5.


## Installation

Install icmplib with: `pip3 install icmplib`


May require privileged (sudo) access. If so, at prompt run this first:
`sudo sysctl -w net.ipv4.ping_group_range='0 2147483647'`


## Usage

Change `target` within the script to desired target IP
