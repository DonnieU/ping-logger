###############################################################################
#
#  Simple ping and logging script to monitor packet loss between source and
#  target but this also checks a control and nearer target (see comments below).
#
#  Requires python 3.6 or later and icmplib (https://pypi.org/project/icmplib/).
#
#  Only tested on Ubuntu 20.04.1 LTS via Windows Subsystem for Linux (WSL)
#  w/ Python 3.8.5 and Raspbian 10 (buster) w/ Python 3.7.3.
#
#  Install icmplib with: pip3 install icmplib.
#
#  May require privileged (sudo) access. If so, at prompt run this first:
#    sudo sysctl -w net.ipv4.ping_group_range='0 2147483647'
#
###############################################################################

from icmplib import ping, multiping
from datetime import datetime, time
import variables

# end_target: the gateway/router closest to client's router
end_target_IP = variables.end_target_IP

# near_target: a gateway/router as close as possible to where the ISP
#              connects to its (backhaul) provider. i.e. subnet change
near_target_IP = variables.near_target_IP

# control_IP: a neutral target to validate source IP is not issue
control_IP = variables.control_IP

# count = 1 # 1 second at interval=1
# count = 10 # 10 seconds at interval=1
count = 60 # 60 seconds at interval=1


end_target_IP_with_dashes = end_target_IP.replace( '.','-' )
fname = f'{end_target_IP_with_dashes}-ping_results_with_control.csv'
f = open( fname, 'a' )

# Header
f.write( f'date,'
         f'control_IP,sent,received,loss(%),rtt_min,rtt_avg,rtt_max,'
         f'near_target_IP,sent,received,loss(%),rtt_min,rtt_avg,rtt_max,'
         f'end_control_IP,sent,received,loss(%),rtt_min,rtt_avg,rtt_max\n' )
f.close()

while True:
  control,end_target,near_target = multiping( [control_IP,end_target_IP,near_target_IP], count=count, interval=1, privileged=False )
  f = open( fname, 'a' )

  f.write( f'{datetime.today().isoformat()},'
           f'{control_IP},'
           f'{str(control.packets_sent)},'
           f'{str(control.packets_received)},'
           f'{str(round(100*control.packet_loss,0))},'
           f'{str(round(control.min_rtt,1))},'
           f'{str(round(control.avg_rtt,1))},'
           f'{str(round(control.max_rtt,1))},'
           f'{near_target_IP},'
           f'{str(near_target.packets_sent)},'
           f'{str(near_target.packets_received)},'
           f'{str(round(100*near_target.packet_loss,0))},'
           f'{str(round(near_target.min_rtt,1))},'
           f'{str(round(near_target.avg_rtt,1))},'
           f'{str(round(near_target.max_rtt,1))},'
           f'{end_target_IP},'
           f'{str(end_target.packets_sent)},'
           f'{str(end_target.packets_received)},'
           f'{str(round(100*end_target.packet_loss, 0))},'
           f'{str(round(end_target.min_rtt, 1))},'
           f'{str(round(end_target.avg_rtt, 1))},'
           f'{str(round(end_target.max_rtt, 1))}\n' )

  f.close()
