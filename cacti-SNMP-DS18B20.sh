#!/bin/bash
# this calls the temp-DS18B20 python script and wraps it in the cacti necessary info


if [ "$1" = "-g" ]
then
echo .1.3.6.1.2.1.25.1.8.2
echo gauge
python ./temp-DS18B20.py
fi
exit 0
