#!/usr/bin/env python
import subprocess
import multiprocessing
from multiprocessing import Pool
import os

home = os.path.expanduser('~')
src = home + "/data/prod/"
dest = home + "/data/prod_backup/"
cpus = multiprocessing.cpu_count()
print("Handling shit with {} CPUs ...".format(cpus))
if __name__ == "__main__":
        p = Pool(cpus)
        p.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))

"""Now that you understand how multiprocessing works, let's fix CPU bound so that it doesn't take more than 20 hours to finish. Try applying multiprocessing, which takes advantage of the idle CPU cores for parallel processing.

Open the dailysync.py Python script in the nano editor that needs to be modified. It's similar to multisync.py that utilizes idle CPU cores for the backup.
Here, you have to use multiprocessing and subprocess module methods to sync the data from /data/prod to /data/prod_backup folder."""