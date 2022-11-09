# ATTENTION: This code is to show off torrenting in python for educational purposes only. 
# Torrenting is illegal in many countries and should not be used for illegal purposes.
# I am not responsible for your download of illegal content or without permission.
# Please respect the internet usage laws of your country.

import libtorrent as lt
import time, sys

# starts torrent download
def start_torrent():
    ses = lt.session({'listen_interfaces': '0.0.0.0:6881'})
    link = sys.argv[1]
    params = lt.parse_magnet_uri(link)
    handle = ses.add_torrent(params)
    count = 0
    while (handle.status().state != lt.torrent_status.seeding):
        s = handle.status()
        state_str = ['queued', 'checking', 'downloading metadata', 'downloading', 'finished', 'seeding', 'allocating']
        if(count == 5):
            print("No download.\n")
            sys.exit(1)
        if(s.download_rate == 0):
            print("[Attempt %d] Missing peers. Please wait..." % (count + 1))
            count += 1
        else:
            print('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
            count = 0
        time.sleep(5)
    print('Download Complete.')

# check input - returns true if three or more, returns false otherwise
def check_input():
    if(len(sys.argv) < 2):
        print("Usage: python3 torrTest.py \"<magnet link>\"\n")
        return False
    return True

# ensures user VPN enabled by prompting question
def enabled_vpn():
    ans = input("Do you have an active VPN running? [Y/N]:")
    if(ans == "y" or ans == "Y"):
        return True
    else:
        print("Please enable a VPN before continuing to use this tool.\n")
        return False

if __name__ == "__main__":
    print()
    if((check_input() is True) and (enabled_vpn() is True)):
        start_torrent()
    else:
        sys.exit(0)


# work in progress
