#!/usr/bin/python
# WhiskeyTangoHotel.Com
# June 2013
# Program reads DS18B20 temp sensor and plots value to sen.se
# DS18B20 connections via AdaFruit tutorial
# With thanks to @Rob_Bishop
# This program is feed customized for RasPI(2)

import httplib
import json as simplejson
from random import randint
import time
import os
import glob

# Pass os commands to set up I2C bus 
#os.system('modprobe w1-gpio')  
#os.system('modprobe w1-therm')

device_file = '/sys/bus/w1/devices/**DEVICE ID**/w1_slave'

run_number = 0

SENSE_API_KEY = "api key in quotes here"
FEED_ID1 = id number not in quotes here  # five digit sen.se channel code.  note it is NOT in quotes

def read_temp_raw():  #read the DS18B20 function
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(): #process the raw temp file output and convert to F
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(1)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        ambC = float(temp_string) / 1000.0
        ambF = ambC * 9.0 / 5.0 + 32.0
        return ambF

def send_to_opensense(data):
 try:
  # prepare data 
  datalist = [{"feed_id" : FEED_ID1, "value" :data['F']},]
  headers = {"sense_key": SENSE_API_KEY,"content-type": "application/json"}
  conn = httplib.HTTPConnection("api.sen.se")
  # format a POST request with JSON content
  conn.request("POST", "/events/", simplejson.dumps(datalist), headers)
  response = conn.getresponse()
  conn.close()
 except:
  pass

ambF = read_temp()
data = { 'F' : ambF}
send_to_opensense(data)

