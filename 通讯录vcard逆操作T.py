import re
import urllib.request
with open('newdata.vcf') as file:
    vcf = file.read()
vcf = vcf.replace('=\n=','=')
names = re.findall('(=[\w=]+)',vcf)
for name in names:
    if name[3:4]=='=':
        name_new = name.replace('=','%')
        name_new = urllib.request.unquote(name_new)
        vcf = vcf.replace(name,name_new,1)
print(vcf)

