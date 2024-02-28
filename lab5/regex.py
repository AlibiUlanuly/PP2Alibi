import re

with open('row.txt', 'r', encoding='utf-8') as file:
    content = file.read()

#TASK 1
"""
pattern = re.compile(r'ab*')
matches = re.findall(pattern, content)
for match in matches:
    print(match)
"""

#TASK 2
"""
pattern = re.compile(r'ab{2,3}')
matches = re.findall(pattern, content)
for match in matches:
    print(match)
"""

#TASK 3
"""
pattern = re.compile(r'[a-z]+_[a-z]+')
matches = re.findall(pattern, content)
for match in matches:
    print(match)
"""

#TASK 4
"""
pattern = re.compile(r'[A-Z]{1}[a-z]+')
matches = re.findall(pattern, content)
for match in matches:
    print(match)
"""

#TASK 5

"""
pattern = re.compile(r'a.*b$')
matches = re.findall(pattern, content)
for match in matches:
    print(matches)
"""

#TASK 6

"""
pattern = r'[ ,.]'
upd = re.sub(pattern, ':', content)
print(upd)
"""

#TASK 7

"""
def snake_to_camel(snake):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake)
print(snake_to_camel(content))
"""

#TASK 8

"""
pattern = r'[A-Z]'
upd = re.split(pattern, content)
print(upd)
"""

#TASK 9

"""
pattern = r'([a-z])([A-Z])'
upd = re.sub(pattern, r'\1 \2', content)
print(upd)
"""

#TASK 10

"""
def camel_to_snake(camel):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', camel)
print(camel_to_snake(content))
"""