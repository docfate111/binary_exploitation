#!/usr/bin/python3
import os
for i in range(0, 25):
	os.system('ping -c 1 10.11.1.'+str(i))
