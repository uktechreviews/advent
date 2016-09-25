calendar = open('config.advent','r')

for days in range (1,25):
	content = calendar.readline()
	if "open" in content:
		print ("Door open on day " + str(days))
calendar.close()
	

