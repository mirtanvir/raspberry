from time import sleep
import serial
#ser = serial.Serial('/dev/ttyACM0', 9600)
#ser.write('3')
#sleep(2)
#ser.write('5')
ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
	name = raw_input("press keys: ")
	ser = serial.Serial('/dev/ttyACM0', 9600)
	#ser.write('3')
	print '{} type{}'.format(name, type(name))
	ser.write(name)
