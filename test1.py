print('Programming-------------(5)')
import re
number='123 hi this is a no 879'
pattern=r'[0-9]+'
result=re.search(pattern,number)
if result:
    print('Search():',result.group())
else:
    print('Not Match!')
result=re.match(pattern,number)
if result:
    print('Match():',result.group())
else:
    print('Not Match')
result=re.findall(pattern,number)
print('Findall():',result)