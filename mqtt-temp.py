#!/usr/bin/python

#import commands
import subprocess
from glob import glob
import sys
import time
import socket
from conf import *
import paho.mqtt.client as mqtt

hostname=socket.gethostname()
#DEVICE = "/sys/bus/w1/devices/" + w1folder + "/w1_slave"
DEVICE = device_file

#print(hostname)
#print(w1folder)
#print(mqttuser)
#print(mqttpass)
#print(mqttbroker)
#print(mqttport)
#print(mqtttopic)


def get_probe_temp():
        tempFile = open(DEVICE)
        lines = tempFile.readlines()
        tempFile.close()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = tempFile.readlines()
                tempFile.close()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                return (1.8*(float(temp_string)/1000))+32

temp = float("{:.2f}".format(get_probe_temp()))
#print(temp)
client = mqtt.Client(client_id=hostname, clean_session=True, userdata=None)

client.username_pw_set(mqttuser,password=mqttpass)
client.connect(mqttbroker, mqttport, 60)
client.publish(mqtttopic,temp)
