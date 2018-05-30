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
ma = re.match(r'(http(s?)://)?(w{3}\.)?(\w+\.)+(com|net|org)','http://www.baidu.com')
#1-13
ma = re.match(r'\A<type\s\'\w+\'>\Z',"<type 'int'>")
#1-14
ma = re.match(r'(1[0-2]|0?[0-9])-\d{2}-\d{4}','12-05-2018')
#1-15
r'(\d{4}-\d{6}-\d{5}|(?P<mark>\d{4})(?P=mark)(?P=mark)(?P=mark))'
#1-16
from random import randrange,choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ('com','edu','net','org','gov')
with open('redata.txt','w') as fp:
	for i in range(randrange(5,11)):
		dtint = randrange(2**32)
		dtstr = ctime(dtint)
		llen = randrange(4,8)
		login = ''.join(choice(lc) for j in range(llen))
		dlen = randrange(llen,13)
		dom = ''.join(choice(lc) for j in range(dlen))
		print('%s::%s@%s.%s::%d-%d-%d' %(dtstr,login,dom,choice(tlds),dtint,llen,dlen))
		str = '%s::%s@%s.%s::%d-%d-%d' %(dtstr,login,dom,choice(tlds),dtint,llen,dlen)
		fp.write(str)

#1-17
import re
week = {'Mon':0,'Tue':0,'Wed':0,'Thu':0,'Fri':0,'Sat':0,'Sun':0}
with open('redata.txt','w') as fp:
	data = fp.readlines()
	for line in data:
		day = re.match('^\w{3}',line)
		key = day.group()
		week[key] += 1

print(week)
#1-18
import re
from time import ctime
number_pattern = r'.+::(\d+)-'
time_stamp_pattern = r'^(.{24})::.+'
try:
	f = open('redata.txt','w')
	for i,eachline in enumerate(f):
		second = re.search(num_pattern,eachline.strip()).group(1)
		time_stamp_pattern = re.search(time_stamp_pattern,eachline.strip().group(1))
		if time_stamp_pattern != str(ctime(int(second))):
			print('Line %d is not WRONG! Correct Timestamp is %s' %(i, time_stamp_pattern))
		else:
			print('This line is OK!')
except ValueError as valueerror:
	print('First Num is not the Type of INT:'+valueerror.message)
except IOError as ioerror:
	print('File Error:'+ioerror.message)
finally:
	f.close()
#1-28
ma = re.match(r'(\d{3}-)?\d{3}-\d{4}','555-1212')
#1-29
ma = re.match(r'(\d{3}-|\(\d{3}\)\s)?\d{3}-\d{4}','800-555-1212')
#1-30





