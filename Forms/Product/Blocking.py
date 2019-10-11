
import sys, csv
from datetime import datetime
import time

hosts_path="/etc/hosts"
redirect="127.0.0.1"

rightnow = datetime.now()
nowtime = rightnow.time()
nowHour = nowtime.hour
nowMinute = nowtime.minute
nowDate= rightnow.date()
nowWeekday = str(nowDate.weekday()) #0
#print(nowWeekday)
WEBSITEa= ""
WEBSITEb= ""
WEBSITEc= ""
theTime = str(nowtime.hour) + ":" + str(nowtime.minute)
#print(theTime)
#row =rowatindex[0]#makes row an array
#j = 0
testV = ["0","1","2","3","4","5", "6", "7", "8", "9"]

with open('datalogs.csv') as csvfile:

	readCSV = csv.reader(csvfile, delimiter=',')

	for row in readCSV:
		if (row[0] == nowWeekday): # '0' # makes it able to check the day that its open because it equals weekday
			WEBSITEa= row[1]
			WEBSITEb= row[4]
			WEBSITEc= row[7]
			for j in range(9):
				print("j is:",j)
				print(row[j])
				testV[j] = row[j]
				print("row[",j,"]",row[j])
				print("row:", row)

print("testV:", testV)

website_list = ["WEBSITEa", "WEBSITEb","WEBSITEc"]
concc = str(nowHour) + ":" + str(nowMinute)
print(concc)
if ((concc > testV[2] and concc<testV[3]) or (concc> testV[6] and concc<testV[7]) or (concc> testV[9] and concc<testV[10])): #starts plan function when kid opens

	print("Sorry Not Allowed...")
	with open(hosts_path, 'r+') as file:
		content = file.read()
		for website in website_list:
			if website in content:
				pass
			else:
					# mapping hostnames to your localhost IP address
				file.write(redirect + " " + website + "\n")
else:
	with open(hosts_path, 'r+') as file:
		content=file.readlines()
		file.seek(0)
		for line in content:
			if not any(website in line for website in website_list):
					file.write(line)

			# removing hostnmes from host file
		file.truncate()
	print("time to relax")
	print("allowed access!")
	time.sleep(10)
