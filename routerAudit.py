# module imports
import sys
import time
from getPrimaryRouterDetails import getPrimaryRouterDetails
from getSecondaryRouterDetails import getSecondaryRouterDetails


# ensure that the correct amounts of arguments are passed when the script is called
if len(sys.argv) != 4:
    sys.exit("Usage: ./routerAudit.py <textfile> <username> <password>")


# pass script arguments into an array to be referenced later
cliArguments = sys.argv


# grab the name of the text file containing the IP addresses from the argument passed to the script
textFile = cliArguments[1]


# open the file that contains all the router IP addresses for reading
try:
	ipAddressesFile = open(textFile)
except IOError:
	sys.exit("The filename that you entered does not exist in the current working directory. Please ensure it is present, and that it was entered as the first argument passed to the script.")


# open the relevant file for writing out the audit output
if textFile == "DMVPNRouterIPAddressesPrimary.txt":
	try:
		auditOutputFilePrimary = open("Output\\auditOutputFilePrimary.txt","w")
	except IOError:
		sys.exit("Unable to create the output file. Please check that the directory 'Output' exists in the current working directory, and that you have permission to write to it.")

if textFile == "DMVPNRouterIPAddressesSecondary.txt":
	try: 
		auditOutputFileSecondary = open("Output\\auditOutputFileSecondary.txt","w")
	except IOError:
		sys.exit("Unable to create the output file. Please check that the directory 'Output' exists in the current working directory, and that you have permission to write to it.")


# iterate through the lines in the text file that contains all the router IP addresses
for line in ipAddressesFile:
	# if the line begins with a '#' then it is a comment, and we don't want to process it, otherwise go ahead
	if not line.startswith("#"):
		# remove the carriage return from the line by splitting it and just taking the first array element
		ipAddress = line.splitlines()
		ipAddress = ipAddress[0]
		# call the getRouterDetails function on the IP address read in from the file. Audit details required
		# are subtly different between primary and secondary routers, so separate functions are required.
		# The function called depends on which list of routers is passsed at the command line.
		if textFile == "DMVPNRouterIPAddressesPrimary.txt":
			primaryRouter = getPrimaryRouterDetails(ipAddress,cliArguments[2],cliArguments[3])
			auditOutputFilePrimary.write(primaryRouter)
			auditOutputFilePrimary.write("\n")
			print primaryRouter
		if textFile == "DMVPNRouterIPAddressesSecondary.txt":
			secondaryRouter = getSecondaryRouterDetails(ipAddress,cliArguments[2],cliArguments[3])
			auditOutputFileSecondary.write(secondaryRouter)
			auditOutputFileSecondary.write("\n")
			print secondaryRouter
			

# close down the files that were opened, for both reading and writing	
ipAddressesFile.close()

if textFile == "DMVPNRouterIPAddressesPrimary.txt":
	auditOutputFilePrimary.close()

if textFile == "DMVPNRouterIPAddressesSecondary.txt":
	auditOutputFileSecondary.close()