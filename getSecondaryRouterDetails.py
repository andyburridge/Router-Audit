# module imports
from runRemoteCommand import runRemoteCommand


def getSecondaryRouterDetails(ip, username, password):
	###########################################################################
	# function to gather router details from a given IOS device	  			  #
	#																		  #
	# input parameters:														  #
	#	ip: 		the ip address of the device to target					  #
	#	username:	the username used for authentication to the device		  #
	# 	password:	the password used for authentication to the device		  #
	###########################################################################
	
	# call fuction 'runRemoteCommand' in order to get the router hostname
	routerHostname = runRemoteCommand(ip,username,password,"show run | i hostname")
	
	# edit the return string to include only interesting data
	# hostname string returns in the format:
	# hostname <hostname>
	
	# split string into an array on a whitespace delimeter and use the second argument in the array
	routerHostname = routerHostname.split(' ')
	routerHostname = routerHostname[1]
	
	
	# call fuction 'runRemoteCommand' in order to get the router image
	routerImage = runRemoteCommand(ip,username,password,"show ver | i image")
	
	#edit the return string to include only interesting data
	# image string returns in the format:
	# System image file is "bootflash:/<image>"
	# or
	# System image file is "bootflash:<image>"
	# or
	# System image file is "flash0:<image>"
	
	# whichever format is returned, split string into an array on a whitespace delimeter and use the fifth argument in the array
	routerImage = routerImage.split(' ')
	try:
		routerImage = routerImage[4]
	except IndexError:
		routerImage = "Array Out Of Bounds"
	
	# split that new string into an array on a ':' delimeter and use the second element in the array
	routerImage = routerImage.split(':')
	try:
		routerImage = routerImage[1]
	except IndexError:
		routerImage = "Array Out Of Bounds"
	
	# clean up strings by stripping extreneous characters
	
	# if the string contains '"', strip it
	if '"' in routerImage:
		routerImage = routerImage.strip('"')
	
	# if the string contains '/', strip it
	if '/' in routerImage:
		routerImage = routerImage.strip('/')
		
		
		
	# call fuction 'runRemoteCommand' in order to get the MTU value from Tunnel 200
	tunnelMTU = runRemoteCommand(ip,username,password,"sh run int tu200 | i mtu")
	
	# edit the return string to include only interesting data
		
	# hostname string returns in the format:
	# ip mtu <MTU>
	
	# split string into an array on a whitespace delimeter and use the third argument in the array
	tunnelMTU = tunnelMTU.split(' ')
	try:
		tunnelMTU = tunnelMTU[3].rstrip()
	except IndexError:
		routerImage = "Array Out Of Bounds"
	
		
	# call fuction 'runRemoteCommand' in order to get the current ip fragmentation & reassembly statistics
	fragmentStats = runRemoteCommand(ip,username,password,"sh ip traffic | i frag")
	reassemblyStats = runRemoteCommand(ip,username,password,"sh ip traffic | i reass")
	
	# strip leading whitespace from the strings
	fragmentStats = fragmentStats.lstrip()
	reassemblyStats = reassemblyStats.lstrip()

	# strip commas from the strings
	fragmentStats = fragmentStats.replace(",","")
	reassemblyStats = reassemblyStats.replace(",","")

	# combine the strings
	fragmentStats = fragmentStats + "," + reassemblyStats
	

	# call fuction 'runRemoteCommand' in order to check if DPD configuration is in place
	dpd = runRemoteCommand(ip,username,password,"sh run | i dpd").lstrip()
	if dpd == "":
		dpd = ("No DPD Configured")
		
		
	# call fuction 'runRemoteCommand' in order to check if MSS configuration is in place on tunnel interface
	mss = runRemoteCommand(ip,username,password,"sh run | i mss").lstrip()
	if mss == "":
		mss = ("No MSS Configured on tunnel interface")	
	
	
	
	# create composite, comma separated string to return to calling process
	detailsOutput = routerHostname + "," + routerImage + "," + tunnelMTU + "," + dpd + "," + mss + "," + fragmentStats 
	
	
	
	return detailsOutput