#!/usr/bin/env python3

"""Check Computer Health"""

import shutil
import psutil

#New
from network import *

"""Disk Usage"""
# du = shutil.disk_usage("/")
# print(du)
# print(du.free/du.total*100)

"""CPU Usage"""
# ab = psutil.cpu_percent(0.5)
# print(ab)

"""My Script"""
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage:
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")
