import sys, getopt, urllib2
from socket import *

def main(argv):
	# Grab command-line arg for url
	try:
		opts, args = getopt.getopt(argv, "")
	except getopt.GetoptError:
	  	print 'test.py -i <inputfile> -o <outputfile>'
	  	sys.exit(2)
	print args	
	siteName = args[0]

	if not siteName.startswith('http'):
		siteName = "http://" + siteName

	# Add http: if not there
	print siteName
	response = urllib2.urlopen(siteName)
	html = response.read()

	# Print results
	print html
if __name__ == "__main__":
   main(sys.argv[1:])