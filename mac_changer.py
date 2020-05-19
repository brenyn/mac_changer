#!/usr/bin/env python

import subprocess

subprocess.call('sudo ifconfig eth0 down', shell = True)
subprocess.call('sudo ifconfig eth0 hw ether 08:00:27:23:ff:90', shell = True)
subprocess.call('sudo ifconfig eth0 up', shell = True)