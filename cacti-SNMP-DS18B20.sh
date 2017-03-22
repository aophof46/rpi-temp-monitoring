#!/bin/bash
# this calls the temp-DS18B20 python script and wraps it in the cacti necessary info

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

if [ "$1" = "-g" ]
  then
    echo .1.3.6.1.2.1.25.1.8.1
    echo integer
    #python /opt/rpi-temp-monitoring/temp-DS18B20.py
    python $DIR/temp-DS18B20.py
fi
exit 0
~

