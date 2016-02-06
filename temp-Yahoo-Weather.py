#!/usr/bin/python
# This program is feed customized for RasPI(2)

import httplib
import json as simplejson
from random import randint
import time
import os
import glob
import urllib
from xml.etree.ElementTree import parse
from pprint import pprint

ZIP = '49506'
WEATHER_URL = 'http://xml.weather.yahoo.com/forecastrss?p=%s'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_opensense(zip_code):
    url = WEATHER_URL % zip_code
    rss = parse(urllib.urlopen(url)).getroot()
    forecasts = []
    ycondition = rss.find('channel/item/{%s}condition' % WEATHER_NS)
    print ycondition.get('temp')

weather_for_opensense(ZIP)

