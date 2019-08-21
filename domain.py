import re

deck=r"C:\Users\Deepjyot Singh\Desktop\MyProjects\DomainNameExtractor\urls.txt";
f=open(deck,'r')

f1=open(r"C:\Users\Deepjyot Singh\Desktop\MyProjects\DomainNameExtractor\domains.txt",'w')

str1=f.read()

pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w{3})(.*)')

matches=pattern.finditer(str1)

for match in matches:
    l1=match.group(2)+''+match.group(3)
    f1.write(l1+'\n')
f.close()
f1.close()
