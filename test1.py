print('Programming-------------(6)')
import re
number='123 Hi This Is A No 482'
pattern=r'[i-s]+' #i,j,k,l,m,n,o,p,q,r,s
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