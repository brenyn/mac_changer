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
#				 Also wouldnt use sudo in subprocess call but had to because it is deprecated.
##########################################################################################################

import subprocess
import optparse
import re

#original MAC for eth0 = 08:00:27:23:ff:90 test MAC address 00:11:22:33:44:55

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface" , dest="interface", help="Interface having MAC changed")
	parser.add_option("-m", "--mac", dest="desiredMAC", help="Desired MAC address")
	(options,arguments) = parser.parse_args()
	# options: an object containing values for all of your options
	# arguments: the list of arguments to process / remaining arguments (unfilled) after parsing options
	# https://docs.python.org/2/library/optparse.html

	if not (options.interface): # if an interface is not submitted
		parser.error("Please specify an interface, use -h or --help for more info.")
	elif not (options.desiredMAC): # or if a MAC address is not submitted
		parser.error("Please specify a MAC address, use -h or --help for more info.")
	else:
		return options

def change_mac(interface,desiredMAC):
	print("[+] Changing MAC address for " + interface + " to " + desiredMAC)

	subprocess.call(['sudo', 'ifconfig', interface, 'down']) #executes as -> sudo ifconfig "interface" down
	subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', desiredMAC])
	subprocess.call(['sudo', 'ifconfig', interface, 'up'])

def get_mac(interface):
	ifconfig_result = subprocess.check_output(["sudo", "ifconfig", interface])

	mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

	if (mac_search_result.group(0)):
		return mac_search_result.group(0)

	else:
		print ("[-] Could not read MAC address")


options = get_arguments()

current_mac = get_mac(options.interface)
print("[+] Current MAC address is " + current_mac)

change_mac(options.interface, options.desiredMAC)
current_mac = get_mac(options.interface)

if (current_mac == options.desiredMAC):
	print("[+] MAC address for " + options.interface + " successfully changed to: " + current_mac)
else:
	print("[-] Unable to change MAC address")