hostPath="/private/etc/hosts"
redirect="127.o.0.1"
WEBSITEa=row[0]
WEBSITEb= row[4]
WEBSITEc= row[8]

""" sample row: 1,https//www.youtube.com,18:00,23:30,https://www.hbo.com,17:30,21:00,https//www.netflix.com,15:30,19:00 """
while True:
	if theTime>row[2] and nowtime<row[3] and nowWeekday == row[0]: #starts plan function when kid opens in time span
        print("Sorry Not Allowed...")
        with open(hostsPath, 'r+') as file:
            content = file.read()
            if WEBSITEa in content:
                pass
            else:
                file.write(redirect+" "+site+"/n")
    else:
            with open(hostsPath, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(WEBSITEa):
                    file.write(line)
                file.truncate()

    print("allowed access!")
    time.sleep(5)



	if theTime>row[5] and nowtime<row[6] and nowWeekday == row[0]:#starts plan function when kid opens
	        print("this site is blocked")
	        with open(hostsPath, 'r+') as file:
	            content = file.read()
	            if WEBSITEb in content:
	                pass
	            else:
	                file.write(redirect+" "+site+"/n")
	    else:
	            with open(hostsPath, 'r+') as file:
	            content = file.readlines()
	            file.seek(0)

	            for line in content:
	                if not any(WEBSITEb):
	                    file.write(line)
	                file.truncate()

	    print("allowed access!")
	    time.sleep(5)


	if theTime>row[8] and nowtime<row[9] and nowWeekday == row[0]:#starts plan function when kid opens
	        print("Sorry Not Allowed...")
	        with open(hostsPath, 'r+') as file:
	            content = file.read()
	            if WEBSITEc in content:
	                pass
	            else:
	                file.write(redirect+" "+site+"/n")
	    else:
	            with open(hostsPath, 'r+') as file:
	            content = file.readlines()
	            file.seek(0)

	            for line in content:
	                if not any(WEBSITEc):
	                    file.write(line)
	                file.truncate()

	    print("allowed access!")
	    time.sleep(5)


webblock()




for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY
for row in readCSV:
    	if (row[0] == nowWeekday):
	    	print(row[0])
	    	for i in row:
	    		put all indexes of row into testV #make a nested for loop that checks each comumb in the sigular row and puts it into a new array.
	    	testV = row[0]	## this isn't working WHY


print(testV)