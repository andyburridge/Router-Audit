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

# open the file for reading
ipAddressesFile = open(textFile)

# open the relevant output file for audit output
if textFile == "DMVPNRouterIPAddressesPrimary.txt":
	auditOutputFilePrimary = open("Output\\auditOutputFilePrimary.txt","w")

if textFile == "DMVPNRouterIPAddressesSecondary.txt":
	auditOutputFileSecondary = open("Output\\auditOutputFileSecondary.txt","w")



for line in ipAddressesFile:
	# if the line begins with a '#' then it is a comment, and we don't want to process it, otherwise go ahead
	if not line.startswith("#"):
		# remove the carriage return from the line by splitting it and just taking the first array element
		ipAddress = line.splitlines()
		ipAddress = ipAddress[0]
		# call the getRouterDetails function on the IP address read in from the file.   Audit details required
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
			

	
ipAddressesFile.close()

# close the relevant text file
if textFile == "DMVPNRouterIPAddressesPrimary.txt":
	auditOutputFilePrimary.close()

if textFile == "DMVPNRouterIPAddressesSecondary.txt":
	auditOutputFileSecondary.close()