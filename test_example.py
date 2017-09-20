#test_example.py

#a testing script for dynamixel python module

#import os
import dynamixel

def validateInput(userInput, rangeMin, rangeMax):
	'''
	Returns valid user input or None
	'''
	try:
		inpTest = int(userInput)
		if inpTest < rangeMin or inpTest > rangeMax:
			print 'error:value out of range[' + str(rangeMin)+'-'+str(rangeMax)+']'
			return None
	except ValueError:
		print 'ERROR: Please enter an integer'
		return None
	return inpTest

def main(settings):
	#Establish a serial connection to the dynamixel network.
	#This usually requires a USB2Dynamixel
	#serial = dynamixel.SerialStream(port=settings['port'], baudrate=settings['baudRate'], timeout=1)
	#Instantiate our network object
	net = dynamixel.DynamixelNetwork(serial)

	for servoId in settings['servoIds']:
		newDynamixel = dynamixel.Dynamixel(servoId, net)
		net._dynamixel_map[servoId] = newDynamixel

	if not net.get_dynamixels():
		print 'No Dynamixels'
		sys.exit(0)
	else:
		print "setup done, test can begin"

	for actuator in net.get_dynamixels():
		actuator.moving_speed = 50
		actuator.torque_enable = True
		actuator.torque_limit = 800
		actuator.max_torque = 800
	net.synchronize()
	while 1:
		answer=None
		while not answer:
			answer_test=raw_input('input the position you want to move all dynamixel(1~1023)')
			answer=validateInput(answer_test,1,1023)
		for actuator in net.get_dynamixels():
			actuator.goal_position=answer
		net.synchronize()
		
if __name__=='__main__':
	settings={}
	portPrompt='Please enter the port name to which the USB2Dynamixel is connected:'
	portChoice=raw_input(portPrompt)
	settings['port']=portChoice

	# Baud rate
	baudRate=None
	while not baudRate:
		brTest=raw_input('enter baudrate [default:1000000]')
		if not brTest:
			baudRate=1000000
		else:
			baudRate=validateInput(brTest,9600,1000000)
	settings['baudRate']=baudRate

	# Servo ID
	highestServoId=None
	while not highestServoId:
		hsiTest=raw_input('pls enter the highest ID of the connected servos:')
		highestServoId= validateInput(hsiTest,1,255)
	settings['highestServoId']=highestServoId

	serial=dynamixel.SerialStream(port=settings['port'],
			baudrate=settings['baudRate'],
			timeout=1)

	#instantiate our network object
	net=dynamixel.DynamixelNetwork(serial)

	#Ping the range of servos that are attached
	print 'scanning for dynamixels...'
	net.scan(1,highestServoId)

	settings['servoIds']=[]
	print 'found the following dynamixels IDs:'
	for dyn in net.get_dynamixels():
		print dyn.id
		settings['servoIds'].append(dyn.id)
	if not settings['servoIds']:
		print 'No Dynamixels Found!'
		sys.exit(0)
	
	main(settings)




