# ATTENTION: This code is to show off torrenting in python for educational purposes only. 
# Torrenting is illegal in many countries and should not be used for illegal purposes.
# I am not responsible for your download of illegal content or without permission.
# Please respect the internet usage laws of your country.

import libtorrent as lt
import time, sys

if(len(sys.argv) < 2):
    print("\nUsage: python3 torrTest.py \"<magnet link>\"\n")
    sys.exit(1)

ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})
link = sys.argv[1]
params = lt.parse_magnet_uri(link)
handle = ses.add_torrent(params)

while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating']
    print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    time.sleep(5)

print('Download Complete.')

# work in progress
