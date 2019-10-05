import sys
import os

import psutil
from psutil._common import bytes2human
import json

def disk_details():

    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                   "Mount"))
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom
                continue
        usage = psutil.disk_usage(part.mountpoint)

        print(templ % (
                part.device,
                bytes2human(usage.total),
                bytes2human(usage.used),
                bytes2human(usage.free),
                int(usage.percent),
                part.fstype,
                part.mountpoint))

disk_details()