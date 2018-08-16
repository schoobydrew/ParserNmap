#edit by Andrew Schoonmaker
#credit to Alton Johnson for the searching function that is used in this
#parses grepable nmap output and puts into spreadsheet
#or you know just output nmap as an xml
#!/usr/bin/python
import re
from sys import argv
def information():
	print "*"*50
	print "Usage: python [script] [file]"
	print "*"*50
	print "Suggested: I use an alias for this i.e. alias parser='python [script]'"
	exit()
def searcher(a, file):
	spreadsheet = open('{}.csv'.format(file), 'a+')
	ip_addr = a[a.find(":")+2:a.find("(")-1]
	info = re.findall("(?<=Ports: )(.*?)(?=Ignored)", a)
	if len(info) == 0:
		info = re.findall("(?<=Ports: )(.*?)(?=Seq Index)", a)
	if len(info) == 0:
		info = re.findall("(?<=Ports: )(.*?)(?=$)", a)
	if len(info) != 0:
		for i in info:
			result = i.split(',')
			for x in result:
				port = re.findall("([0-9]+/open/.*?)/", x)
				if "[]" in str(port):
					continue
				port = port[0].replace("/open", "")
				service = re.findall("(?<=//)(.*?)(?=/)", x)[0]
				version = x.split("/")[-2]
				if len(version) > 40:
					version = version[:40]
				if len(version) == 0:
					version = "-"
				print >> spreadsheet, "{},{},{},{}".format(ip_addr, port, service, version)
	spreadsheet.close()
def start(argv):
	if len(argv) == 0:
		information()
	contents = sorted(open(argv[0]).read().split('\n'))
	for item in contents:
		searcher(item, argv[0])
start(argv[1:])
