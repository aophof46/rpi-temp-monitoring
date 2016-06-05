#!/usr/bin/python

DEVICE = "/sys/bus/w1/devices/28-0000075341e3/w1_slave"
import commands
import sys
 
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    #return float(cpu_temp)/1000
    # Uncomment the next line if you want the temp in Fahrenheit
    return (1.8*(float(cpu_temp)/1000))+32
 
def get_gpu_temp():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    # return  float(gpu_temp)
    # Uncomment the next line if you want the temp in Fahrenheit
    return (1.8* float(gpu_temp))+32

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

def main():
    #print "CPU temp: ", str(get_cpu_temp())
    #print "GPU temp: ", str(get_gpu_temp())
    #print "Probe temp: ", get_probe_temp()
    temp = float(get_probe_temp())	
    #print temp 
    sys.exit(temp)
 
if __name__ == '__main__':
    main()
