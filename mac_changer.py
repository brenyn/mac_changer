#!/usr/bin/env python

##########################################################################################################
#
# Author: Brenyn Kissoondath
# Course: Learn Python and Ethical Hacking From Scratch - StationX
# Instructor: Zaid Al Quraishi
# Purpose: Change MAC address
# Input(s): User input for target device and desired MAC address
# Output(s): Changes MAC address according to user input
#
# Notes to self: Course uses ifconfig but this command is deprecated in 2020. Change to use ip command.
#
##########################################################################################################

import subprocess
import optparse

def change_mac(interface,desiredMAC):
	print("[+] Changing MAC address for " + interface + " to " + desiredMAC)

	subprocess.call(['sudo', 'ifconfig', interface, 'down'])
	subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', desiredMAC])
	subprocess.call(['sudo', 'ifconfig', interface, 'up'])

#original MAC for eth0 = 08:00:27:23:ff:90 test MAC address 00:11:22:33:44:55


parser = optparse.OptionParser()

parser.add_option("-i", "--interface" , dest="interface", help="Interface having MAC changed")
parser.add_option("-m", "--mac", dest="desiredMAC", help="Desired MAC address")

(options, arguments) = parser.parse_args() 

change_mac(options.interface, options.desiredMAC)