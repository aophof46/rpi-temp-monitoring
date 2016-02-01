# rpi-temp-monitoring
Using a Raspberry Pi to monitor temps around the house

Script created to query Yahoo weather based on zip code and push the temperature in F to open.sen.se

opensense-Yahoo-Weather.py

Script created to query locally attached DS18B20 temperature sensor on a Raspberry Pi and push the
temperature in F to open.sen.se

opensense-DS18B20.py

Scripts created to make the temperature in F of a Raspberry Pi attached DS18B20 sensors availabel via SNMP
so that the temperature can be captured by Cacti using the generic SNMP template.

cacti-SNMP_DS18B20.sh

temp_DS18B20.py

