import re

def rearrange_name(name):
  result = re.search(r"^(\w*), (\w*)$", name)
  if result is None:
      return name
  return "{} {}".format(result[2], result[1])

def rearrange_name1(name):
  result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
  if result is None:
      return name
  return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))
print(rearrange_name1("Hopper, Grace M."))


"""Repetition qualifiers"""
print(re.search(r"[a-zA-Z]{5}", "a ghost"))
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.search(r"[a-zA-Z]{5,10}", "I really like strawberries"))
print(re.findall(r"[a-zA-Z]{5,10}", "I really like strawberries"))
"""Control full words"""
print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5,}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))
print(re.search(r"s\w{,4}", "I really like strawberries"))

def multi_vowel_words(text):
  pattern = r"[\w]*[a+e+i+o+u+]{3,}[\w]*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []
