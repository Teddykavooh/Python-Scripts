import re

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    #do sth when no matches
    if result is None:
        return "No shit found"
    return result[1]

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
log_1 = "99 elephants in a [cage]"
print(extract_pid(log_1))

"""Get the CAPS text as well"""
def get_two(log_line):
    
