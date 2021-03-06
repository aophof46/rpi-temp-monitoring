#!/usr/bin/python

import MySQLdb

import os
import time
import glob
from conf import *

# global variables
speriod=(15*60)-1

# store the temperature in the database
def log_temperature(locationVar,temperature):
	try:
		cnx = MySQLdb.connect(host=dbhost,user=dbuser,passwd=dbpassword,db=dbdatabase)
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit (1)


	curs=cnx.cursor()

	#print("mysql values")
	#print(sensorloc)
	#print(temperature)

	insert_stmt = (
		"INSERT INTO events (location_id, description_id, data) "
		"VALUES (%s, %s, %s)"
	)

	data = (sensorloc, sensordesc, temperature)

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

	# get the temperature from the device file
	temperature = get_temp(device_file)
	if temperature == None:
		# Sometimes reads fail on the first attempt
		# so we need to retry
		temperature = get_temp(device_file)
		#print "temperature="+str(temperature)

	# Store the temperature in the database
	log_temperature(sensorloc,temperature)


if __name__=="__main__":
	main()




