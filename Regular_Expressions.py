"""Regex"""
import re

log = "July, blah blah blah [12345]: blah"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

"""Get the Time"""
ola = "blah blah 12:10 pm blah blah"
ola1 = "blah blah 9:10pm blah blah"
tricks = r"[1-9][0-2]?:[0-5][0-9] ?(pm|am)"
out_c = re.search(tricks, ola)
out_d = re.search(tricks, ola1)
print(out_c)
print(out_d)
