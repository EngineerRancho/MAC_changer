#!usr/bin/env python

import subprocess
import optparse

def get_argumnets():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the MAC, eth0, wlan0")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC to change the MAC")
    (options, argruments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the Interface, use --help for more information")
    elif not options.new_mac:
        parser.error("[-] Please specify the MAC, use --help for more information")
    return options

def change_mac(interface, new_mac):
    print("[+] Chnaging MAC address for", interface, "to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

options = get_argumnets()
change_mac(options.interface,options.new_mac)
