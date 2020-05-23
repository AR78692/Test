#-------------------------------------------
import re
str='HellO world 7856'
pattern=r"[o]+"
a=re.search(pattern,str)
if a:
    print('Search():',a.group())
else:
    print('Not Match')
a=re.match(pattern,str)
if a:
    print('Match:',a.group())
else:
    print('Not Match')
a=re.findall(pattern,str)
print('Findall:',a)
