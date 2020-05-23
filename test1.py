import re
string='Hello 123 Hello'
result=re.match(r"(\w+)\ (\d+)\ (\w+)",string)
print('Group():',result.group())
print('Group(0):',result.group(0))
print('Group(1):',result.group(1))
print('Group(2):',result.group(2))
print('Group(3):',result.group(3))
