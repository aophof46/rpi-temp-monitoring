#!/usr/bin/python

import MySQLdb

import os
import time
import glob

# global variables
speriod=(15*60)-1
# Locations
# 1 | Garage
# 2 | Freezer  
# 3 | Basement 
# 4 | attic 

#Descriptions
# 1 | Garage Door Open 
# 2 | Garage Door Closed 
# 3 | Temperature 


locationVar='' 
descriptionVar='3'

w1path = '/sys/bus/w1/devices/*identifier*'
user = ''
password = ''
host = ''
database = ''

# store the temperature in the database
def log_temperature(locationVar,temperature):
	cnx = MySQLdb.connect(host=host,user=user,passwd=password,db=database)
	curs=cnx.cursor()

	#print("mysql values")
	#print(locationVar)
	#print(temperature)

	insert_stmt = (
		"INSERT INTO events (location_id, description_id, data) "
		"VALUES (%s, %s, %s)"
	)

	data = (locationVar, descriptionVar, temperature)

	curs.execute(insert_stmt, data)

	# commit the changes
	cnx.commit()
	cnx.close()


# get temerature
# returns None on error, or the temperature as a float
def get_temp(devicefile):

	try:
		fileobj = open(devicefile,'r')
		lines = fileobj.readlines()
		fileobj.close()
	except:
		return None


        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = tempFile.readlines()
                tempFile.close()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                return (1.8*(float(temp_string)/1000))+32


# main function
# This is where the program starts 
def main():

	# enable kernel modules
	os.system('sudo modprobe w1-gpio')
	os.system('sudo modprobe w1-therm')

	# search for a device file that starts with 28
	devicelist = glob.glob(w1path)
	if devicelist=='':
		return None
	else:
		# append /w1slave to the device file
		w1devicefile = devicelist[0] + '/w1_slave'


	# get the temperature from the device file
	temperature = get_temp(w1devicefile)
	if temperature == None:
		# Sometimes reads fail on the first attempt
		# so we need to retry
		temperature = get_temp(w1devicefile)
		#print "temperature="+str(temperature)

	# Store the temperature in the database
	log_temperature(locationVar,temperature)


if __name__=="__main__":
	main()




