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

parser = optparse.OptionParser()

parser.add_option("-i", "--interface" , dest="interface", help="Interface having MAC changed")
parser.add_option("-m", "--mac", dest="desiredMAC", help="Desired MAC address")

(options, arguments) = parser.parse_args() 

interface = options.interface
desiredMAC = options.desiredMAC

#for raw user input (command line prompt)
#interface = input("Interface = ")
#desiredMAC = input("New MAC address = ") 	#original MAC for eth0 = 08:00:27:23:ff:90 test MAC address 00:11:22:33:44:55

print("[+] Changing MAC address for " + interface + " to " + desiredMAC)


# this way can be hijacked because user can input anything for interface/desiredMAC
# example: eth0;ls;
# would allow the user to input any linux commands they want into the shell

#subprocess.call('sudo ifconfig ' + interface + ' down', shell = True)
#subprocess.call('sudo ifconfig ' + interface + ' hw ether ' + desiredMAC, shell = True)
#subprocess.call('sudo ifconfig ' + interface + ' up', shell = True)

# more secure way (although ifconfig is deprecated, change to use ip command later)
# this way if someone tries to hijack, commands will only be executed as if part of ifconfig command

subprocess.call(['sudo', 'ifconfig', interface, 'down'])
subprocess.call(['sudo', 'ifconfig', interface, 'hw', 'ether', desiredMAC])
subprocess.call(['sudo', 'ifconfig', interface, 'up'])