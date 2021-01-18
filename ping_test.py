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

fname = '139-60-77-193-ping_results.csv'

# target = '8.8.8.8'
target = '139.60.77.193'
# count = 10 # 10 seconds at interval=1
count = 60 # 60 seconds at interval=1

f = open(fname, 'a')
# Header
f.write('date,sent,received,loss(%),rtt_min,rtt_avg,rtt_max\n')
f.close()

while True:
  host = ping(target, count=count, interval=1, privileged=False)
  # print('packet loss (%): ', 100*host.packet_loss)
  f = open(fname, 'a')
  #f.write( datetime.today().isoformat()
  #        + '  sent: ' + str(host.packets_sent)
  #        + '  received: ' + str(host.packets_received)
  #        + '  loss (%): ' + str(round(100*host.packet_loss, 0))
  #        + '    rtt min/avg/max: '
  #        + str(round(host.min_rtt, 1)) + '/'
  #        + str(round(host.avg_rtt, 1)) + '/'
  #        + str(round(host.max_rtt, 1)) + '\n' )


  f.write( datetime.today().isoformat()
          + ',' + str(host.packets_sent)
          + ',' + str(host.packets_received)
          + ',' + str(round(100*host.packet_loss, 0))
          + ',' + str(round(host.min_rtt, 1))
          + ',' + str(round(host.avg_rtt, 1))
          + ',' + str(round(host.max_rtt, 1)) + '\n' )

  f.close()
