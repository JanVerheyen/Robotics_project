#test_example.py



#################################INITIALISE################################
import dynamixel
import time
import math

settings={}
settings['port']="COM7"
settings['baudRate']=1000000
highestServoId= 10
settings['highestServoId']=highestServoId
serial=dynamixel.SerialStream(port=settings['port'],
		baudrate=settings['baudRate'],
		timeout=1)
net=dynamixel.DynamixelNetwork(serial)
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
	

####################################START POSITION####################################        
net = dynamixel.DynamixelNetwork(serial)

for servoId in settings['servoIds']:
	newDynamixel = dynamixel.Dynamixel(servoId, net)
	net._dynamixel_map[servoId] = newDynamixel

if not net.get_dynamixels():
	print 'No Dynamixels'
else:
	print "setup done, test can begin"

for actuator in net.get_dynamixels():
	actuator.moving_speed = 55
	actuator.torque_enable = True
	actuator.torque_limit = 800
	actuator.max_torque = 800
net.synchronize()
S1 = net.get_dynamixels()[2]
S2 = net.get_dynamixels()[0]
S3 = net.get_dynamixels()[3]
S4 = net.get_dynamixels()[1]
S1.goal_position = 746
S2.goal_position = 248
S3.goal_position = 732
S4.goal_position = 292
net.synchronize()
time.sleep(3)
print "ready"

####################################MOVEMENT####################################
#Variables
d=0
t=0

x=130
y=0

X=0
Y=0
Z=0

Xold=0
Yold=0

A1=0
A2=0
A1old=0
A2old=0

dA1=0
dA2=0

S1v=0
S2v=0

S1s=0
S2s=0

theta1=0
theta2=0
phi1=0
phi2=0


#Constants
vmax=60

#### POSITION FUNCTION #####################################

def Position(X,Y,Z):
    global Xold
    global Yold
    global A1old
    global A2old

    #Change coordinate system
    x=X-65
    y=Y+130

    #DETERMINE POSITION    
    #Calculate angles
    theta1 = math.atan2(y,x)/math.pi*180
    phi1   = math.acos((x**2+y**2-29400)/(350*math.sqrt(x**2+y**2)))/math.pi*180
    theta2 = math.atan2(y,x-130)/math.pi*180
    phi2   = math.acos(((x-130)**2+y**2-29400)/(350*math.sqrt((x-130)**2+y**2)))/math.pi*180

    #Total angle
    A1=theta1+phi1
    A2=theta2-phi2

    #Servo position
    S1g=int((A1+60)*1024/300)
    S2g=int((A2+60)*1024/300)
    S1.goal_position = S1g
    S2.goal_position = S2g   

    #DETERMINE VELOCITY
    #Travel time
    d=math.sqrt((X-Xold)**2+(Y-Yold)**2)
    t=d/vmax

    #Angular velocity
    dA1=abs(A1-A1old)

    dA2=abs(A2-A2old)
    S1s=int(dA1*3/(t+0.0001))
    S2s=int(dA2*3/(t+0.0001))
    S1.moving_speed = S1s
    S2.moving_speed = S2s

    #Z POSITION STUFF
    S3g=int(512+Z)
    S4g=int(512-Z)
    S3.goal_position = S3g
    S4.goal_position = S4g

    net.synchronize()
    #PRINT
    #print "Servo 1 end position ", S1g
    #print "Servo 1 velocity     ", S1s
    #print "Servo 2 end position ", S2g
    #print "Servo 2 velocity     ", S2s
    #print t
    time.sleep(t-0.1)
    Xold=X
    Yold=Y
    A1old=A1
    A2old=A2
        
###########################################

def SetX(a,b):
        c=2-b
        xd=22
        Position(138,0,220)
        Position(a*70+68-xd ,c*70+20-xd, 25)
        time.sleep(1.1)
        Position(a*70+68-xd ,c*70+20-xd, 5)
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20+xd, 5)
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20+xd, 25)
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20-xd, 25)
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20-xd, 5)
        time.sleep(0.3)
        Position(a*70+68-xd ,c*70+20+xd, 5)
        time.sleep(0.3)
        Position(a*70+68-xd ,c*70+20+xd, 25)
        time.sleep(0.3)
        Position(138,0,220)

def SetO(a,b):
        c=2-b
        xd=22
        Position(138,0,220)
        Position(a*70+68 ,c*70+20-xd, 25)
        time.sleep(0.8)
        Position(a*70+68 ,c*70+20-xd, 5)
        Position(a*70+68+0.26*xd ,c*70+20-0.97xd, 5)
        Position(a*70+68+0.5*xd ,c*70+20-0.87*xd, 5)
        Position(a*70+68+0.71*xd ,c*70+20-0.71*xd, 5)
        Position(a*70+68+0.87*xd ,c*70+20-0.5*xd, 5)
        Position(a*70+68+0.97*xd ,c*70+20-0.26*xd, 5)
        Position(a*70+68+xd ,c*70+20, 5)
        Position(a*70+68+0.97*xd ,c*70+20+0.26*xd, 5)
        Position(a*70+68+0.87*xd ,c*70+20+0.5*xd, 5)
        Position(a*70+68+0.71*xd ,c*70+20+0.71*xd, 5)
        Position(a*70+68+0.5*xd ,c*70+20+0.87*xd, 5)
        Position(a*70+68+0.26*xd ,c*70+20+0.97*xd, 5)
        Position(a*70+68 ,c*70+20+xd, 5)
        Position(a*70+68-0.26*xd ,c*70+20+0.96*xd, 5)
        Position(a*70+68-0.5*xd ,c*70+20+0.87*xd, 5)
        Position(a*70+68-0.71*xd ,c*70+20+0.71*xd, 5)
        Position(a*70+68-0.87*xd ,c*70+20+0.5*xd, 5)
        Position(a*70+68-0.97*xd ,c*70+20+0.26*xd, 5)
        Position(a*70+68-1*xd ,c*70+20, 5)
        Position(a*70+68-0.97*xd ,c*70+20-0.26*xd, 5)
        Position(a*70+68-0.87*xd ,c*70+20-0.5*xd, 5)
        Position(a*70+68-0.71*xd ,c*70+20-0.71*xd, 5)
        Position(a*70+68-0.5*xd ,c*70+20-0.87*xd, 5)
        Position(a*70+68-0.26*xd ,c*70+20-0.97*xd, 5)
        Position(a*70+68 ,c*70+20-xd, 5)
        Position(a*70+68 ,c*70+20-xd, 25)
        Position(138,0,220)
