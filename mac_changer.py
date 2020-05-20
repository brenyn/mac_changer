#!/usr/bin/env python

import subprocess

interface = input("Interface = ")
desiredMAC = input("New MAC address = ") 	#original MAC for eth0 = 08:00:27:23:ff:90 test MAC address 00:11:22:33:44:55

print("[+] Changing MAC address for " + interface + " to " + desiredMAC)

subprocess.call('sudo ifconfig ' + interface + ' down', shell = True)
subprocess.call('sudo ifconfig ' + interface + ' hw ether ' + desiredMAC, shell = True)
subprocess.call('sudo ifconfig ' + interface + ' up', shell = True)