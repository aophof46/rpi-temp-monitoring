#!/bin/bash
# this calls the temp-DS18B20 python script and wraps it in the cacti necessary info

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

if [ "$1" = "-t" ]
  then
    echo .1.3.6.1.2.1.25.1.8.1
    echo gauge
    python $DIR/sensor-AM2302.py -t
fi
if [ "$1" = "-h" ]
  then
    echo .1.3.6.1.2.1.25.1.8.2
    echo gauge
    python $DIR/sensor-AM2302.py -h
fi
if [ "$1" = "-b" ]
  then
    echo .1.3.6.1.2.1.25.1.8.3
    echo gauge
    python $DIR/sensor-AM2302.py -b
fi
exit 0
~

