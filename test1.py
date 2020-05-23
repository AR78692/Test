print('Programming-------------(3)')
import re
str='HellO World 4556 welcome'
pattern=r'[o]+'
result=re.search(pattern,str,re.I)
if result:
    print('Search():',result.group())
else:
    print('Not Match!():')
result=re.match(pattern,str,re.I)
if result:
    print('Match():',result.group())
else:
    print('Not Match!():')
result=re.findall(pattern,str,re.I)
print('Findall():',result)