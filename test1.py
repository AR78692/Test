#-------------------------------------
import re
str='Hello World World 2335'
pattern=r'[W]+'
result=re.search(pattern,str)
if result:
    print('Search!',result.group())
else:
    print('No Match!')
result=re.match(pattern,str)
if result:
    print('Match():',result.group())
else:
    print('No Match!')
result=re.findall(pattern,str)
print(result)