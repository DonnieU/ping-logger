###############################################################################
#  Simple ping and logging script to monitor packet loss between source and target
#  Requires python 3.6 or later and icmplib (https://pypi.org/project/icmplib/)
#  Only tested on Ubuntu 20.04.1 LTS via Windows Subsystem for Linux (WSL) w/ Python 3.8.5
#  Install icmplib with: pip3 install icmplib
#  May require privileged (sudo) access. If so, at prompt run this first:
#    sudo sysctl -w net.ipv4.ping_group_range='0 2147483647'
###############################################################################

from icmplib import ping
from datetime import datetime, time

fname = 'ping_results.txt'

target = '8.8.8.8'
# count = 10 # 10 seconds at interval=1
count = 60 # 60 seconds at interval=1

while True:
  host = ping(target, count=count, interval=1, privileged=False)
  # print('packet loss (%): ', 100*host.packet_loss)
  f = open(fname, 'a')
  f.write(datetime.today().isoformat() + '\tpackets sent: ' + str(host.packets_sent) + '\tpackets received: ' + str(host.packets_received) + '\tpacket loss (%): ' + str(round(100*host.packet_loss, 1)) + '\n')
  f.close()
