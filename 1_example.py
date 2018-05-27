import re

re.findall(r'(?i)yes','yes? Yes. YES') #(?i) 不区分大小写
re.findall(r'(?im)(^th[\w ]+)','''
	This is the first,
	another line,
	that line, it's the best.
	''')#(?im)不区分大小写并且支持多行，(^...)以...为开头

re.findall(r'(?s)th.+','''
	The first line,
	the second line,
	the third line.
	''')#(?s)表示“.”可以用来匹配\n

re.search(r'''(?x)
	\((\d{3})\)
	[ ]
	(\d{3})
	-
	(\d{4})
	''','(800) 555-1212').groups()

re.findall(r'http://(?:\w+\.)*(\w+\.com)',\
           'http://google.com http://www.google.com http://code.google.com')
#(?:\w+\.)表示这个分组不用于检索或应用
#这个例子的返回结果：['google.com', 'google.com', 'google.com']

re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://www.google.com http://code.google.com http://google.com')
#这个例子应该返回结果['google.com', 'google.com', 'google.com']

re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})',
	'(800) 555-1212').groupdict()
#这个例子返回结果{'areacode': '800', 'prefix': '555'}以字典形式返回

re.search(r"\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})','(800) 555-1212").group()
#这个例子返回结果'(800) 555-1212'

re.findall(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212')
#这个例子返回结果[('800', '555')]
#因为(?:\d{4})表示不用于后续搜索与应用