import re
//Author : ramazantufekci
//
//apache log dosyası da kullanılabilir veya baska bir log dosyasıda

log = open("/var/log/nginx/access.log", "r")
d = log.read()
pat =(r''
	'(\d+.\d+.\d+.\d+)\s-\s-\s'
	'\[(.+)\]\s'
)
l=re.findall(pat,d)

for item in l:
	print item[0]
