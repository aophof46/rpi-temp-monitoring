#!/usr/bin/python
# This program is feed customized for RasPI(2)

import httplib
import json as simplejson
from random import randint
import glob
import urllib
from xml.etree.ElementTree import parse
from pprint import pprint

ZIP = '49506'

WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

SENSE_API_KEY = "API KEY IN QUOTES HERE"
FEED_ID1 = 12345  # five digit sen.se channel code.  note it is NOT in quotes

def send_to_opensense(data):
	try:
		datalist = [{"feed_id" : FEED_ID1, "value" :data['F']},]
		headers = {"sense_key": SENSE_API_KEY,"content-type": "application/json"}
		conn = httplib.HTTPConnection("api.sen.se")
		conn.request("POST", "/events/", simplejson.dumps(datalist), headers)
		response = conn.getresponse()
		conn.close()
	except:
		pass

def weather_for_opensense(zip_code):
	try:
		url = WEATHER_URL % zip_code
		rss = parse(urllib.urlopen(url)).getroot()
		forecasts = []
		ycondition = rss.find('channel/item/{%s}condition' % WEATHER_NS)
		return {
			'F': ycondition.get('temp'),
		}
	except:
		Pass

data = weather_for_opensense(ZIP)
send_to_opensense(data)
#print data
