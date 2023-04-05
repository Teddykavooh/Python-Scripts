#!/usr/bin/env python3
from multiprocessing import Pool
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)

  """Now, you'll get the Python script multisync.py for practice in order to understand how multiprocessing works.
  We used the Pool class of the multiprocessing Python module. Here, we define a run method to perform the tasks.
  Next, we have a few tasks.
  Create a pool object of the Pool class of a specific number of CPUs your system has by passing a number of tasks
  you have.
  Start each task within the pool object by calling the map instance method, and pass the run function and the list
  of tasks as an argument."""