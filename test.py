print('Programme -------(4) in re modouls')
import re
print('Enter some world for find something in this sentence!')
str=input()
pattern=r'[^o]+'
result=re.search(pattern,str)
if result:
    print('Search is():',result.group())
else:
    print('Not Match!')
result=re.match(pattern,str)
if result:
    print('Search is():',result.group())
else:
    print('Not Match!')
result=re.findall(pattern,str)
print('Findall is():',result)