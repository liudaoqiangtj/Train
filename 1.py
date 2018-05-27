import re
#1-6
ma = re.match(r'http://www\..*\.(edu|net|com)$','http://www.tj.edu')
#1-7
ma = re.match(r'-?\d+','-101')
#1-8
ma = re.match(r'[-+]?\d[L]','123L')
#1-9
ma = re.match(r'-?\d+(\.\d*)?','-10.12')
#1-10
ma = re.match(r'-?\d*([-\+][1-9]+j|)','1')
#1-11
ma = re.match(r'[\w_]+@(\w+\.)?(163|126|qq|gmail|139)\.(com|net)','liu188017@163.126.com')
#1-12
