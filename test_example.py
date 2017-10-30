#test_example.py



#################################INITIALISE################################
import dynamixel
import time
import math
import sys

settings={}
settings['port']="COM3"
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
S3.goal_position = 702
S4.goal_position = 322
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
    time.sleep(t)
    Xold=X
    Yold=Y
    A1old=A1
    A2old=A2
        
###########################################

def SetX(b,a):
        d=3
        c=2-b
        xd=22
        Position(138,0,180)
        Position(a*70+68-xd ,c*70+20-xd, 25)
        time.sleep(1.1)
        Position(a*70+68-xd ,c*70+20-xd, d)
        time.sleep(0.5)#
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20+xd, d)
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20+xd, 25)
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20-xd, 25)
        time.sleep(0.3)
        Position(a*70+68+xd ,c*70+20-xd, d)
        time.sleep(0.5)#
        time.sleep(0.3)
        Position(a*70+68-xd ,c*70+20+xd, d)
        time.sleep(0.3)
        Position(a*70+68-xd ,c*70+20+xd, 25)
        time.sleep(0.3)
        Position(138,0,180)

def SetO(b,a):
        d=3
        c=2-b
        xd=22
        Position(138,0,180)
        Position(a*70+68-0.5*xd ,c*70+20-0.87*xd, 25)
        time.sleep(1.2)
        Position(a*70+68-0.26*xd ,c*70+20-0.97*xd, d)
        time.sleep(0.5)#
        Position(a*70+68 ,c*70+20-xd, d)
        Position(a*70+68+0.26*xd ,c*70+20-0.97*xd, d)
        Position(a*70+68+0.5*xd ,c*70+20-0.87*xd, d)
        Position(a*70+68+0.71*xd ,c*70+20-0.71*xd, d)
        Position(a*70+68+0.87*xd ,c*70+20-0.5*xd, d)
        Position(a*70+68+0.97*xd ,c*70+20-0.26*xd, d)
        Position(a*70+68+xd ,c*70+20, d)
        Position(a*70+68+0.97*xd ,c*70+20+0.26*xd, d)
        Position(a*70+68+0.87*xd ,c*70+20+0.5*xd, d)
        Position(a*70+68+0.71*xd ,c*70+20+0.71*xd, d)
        Position(a*70+68+0.5*xd ,c*70+20+0.87*xd, d)
        Position(a*70+68+0.26*xd ,c*70+20+0.97*xd, d)
        Position(a*70+68 ,c*70+20+xd, d)
        Position(a*70+68-0.26*xd ,c*70+20+0.97*xd, d)
        Position(a*70+68-0.5*xd ,c*70+20+0.87*xd, d)
        Position(a*70+68-0.71*xd ,c*70+20+0.71*xd, d)
        Position(a*70+68-0.87*xd ,c*70+20+0.5*xd, d)
        Position(a*70+68-0.97*xd ,c*70+20+0.26*xd, d)
        Position(a*70+68-1*xd ,c*70+20, d)
        Position(a*70+68-0.97*xd ,c*70+20-0.26*xd, d)
        Position(a*70+68-0.87*xd ,c*70+20-0.5*xd, d)
        Position(a*70+68-0.71*xd ,c*70+20-0.71*xd, d)
        Position(a*70+68-0.5*xd ,c*70+20-0.87*xd, d)
        Position(a*70+68-0.26*xd ,c*70+20-0.97*xd, d)
        Position(a*70+68 ,c*70+20-xd, d)
        Position(a*70+68+0.26 ,c*70+20-0.97*xd, d)
        Position(a*70+68+0.5*xd ,c*70+20-0.87*xd, 25)
        Position(138,0,180)
def DrawGrid():
        d=3
        u=25
        Position(138,0,180)
        Position(103,-15,u)
        
        time.sleep(1.1)
        Position(103,-15,d)
        time.sleep(0.5) #
        Position(103,20,d)
        Position(103,55,d)
        Position(103,90,d)
        Position(103,125,d)
        Position(103,160,d)
        Position(103,195,d)
        Position(103,195,u)
        time.sleep(0.5)

        Position(173,-15,u)
        time.sleep(0.3)
        Position(173,-15,d)
        time.sleep(0.5) #
        Position(173,20,d)
        Position(173,55,d)
        Position(173,90,d)
        Position(173,125,d)
        Position(173,160,d)
        Position(173,195,d)
        Position(173,195,u)
        time.sleep(0.5)

# first -5 last -5
        Position(28,124,u)
        time.sleep(0.5)
        Position(28,123,d)
        Position(88,122,d)
        time.sleep(0.5) #
        Position(103,121,d)
        Position(138,121,d)
        Position(173,122,d)
        Position(208,123,d)
        Position(238,124,d)
        Position(238,125,u)
        time.sleep(0.5)

        Position(238,55,u)
        time.sleep(0.5)
        Position(238,54,d)
        time.sleep(0.5)
        Position(208,53,d)
        Position(173,52,d)
        Position(138,51,d)
        Position(103,52,d)
        Position(68,53,d)
        Position(28,57,d)
        Position(28,59,u)
        time.sleep(0.5)
        Position(138,0,180)

def Victory(c,w):
        if c==0:
                if w==2:
                        #Victory
                        Position(138,0,180)
                        time.sleep(0.5)
                        Position(58,80,180)
                        Position(138,160,180)
                        Position(218,80,180)
                        Position(138,0,180)
                        Position(58,80,180)
                        Position(138,160,180)
                        Position(218,80,180)
                        Position(138,0,180)
                        Position(58,80,180)
                        Position(138,160,180)
                        Position(218,80,180)
                        Position(138,0,180)
                        


                if w==1:
                        #Lost

                if w==3:
                        """"
                        #Draw
                        Position(138,50,25)
                        Position(138,50,3)
                        time.wait(0.5)
                        Position(88,100,3)
                        Position(88,150,3)
                        Position(138,150,3)
                        Position(188,150,3)
                        Position(188,100,3)
                        Position(188,50,3)
                        Position(138,50,3)
                        Position(138,50,25)
                        
                        Position(108,70,25)
                        Position(108,70,3)
                        time.wait(0.5)
                        Position(168,70,3)
                        Position(168,70,25)
                        Position(113,125,25)
                        Position(113,125,3)
                        Position(112,125,3)
                        Position(113,124,3)
                        Position(114,125,3)
                        Position(113,126,3)
                        Position(113,125,3)
                        Position(113,125,25)
                        """" 
        if c==1:
                if w==1:
                        #Victory
                        Position(138,0,180)
                        time.sleep(0.5)
                        Position(58,80,180)
                        Position(138,160,180)
                        Position(218,80,180)
                        Position(138,0,180)
                        Position(58,80,180)
                        Position(138,160,180)
                        Position(218,80,180)
                        Position(138,0,180)
                        Position(58,80,180)
                        Position(138,160,180)
                        Position(218,80,180)
                        Position(138,0,180)

                if w==2:
                        #Lost

                if w==3:
                        #Draw
                        

"""
DrawGrid()

for i in range(3):
        for j in range(3):
                SetX(i,j)
                SetO(i,j)


def SetChineseThing():
        d=8
        u=25
        Position(138,0,220)
        Position(20,80,u)
        time.sleep(1)
        Position(20,80,d)
        Position(20,0,d)
        Position(20,0,u)
        Position(0,60,u)
        Position(0,60,d)
        Position(40,60,d)
        Position(40,60,u)
        Position(20,50,u)
        Position(20,50,d)
        Position(0,30,d)
        Position(0,30,u)
        Position(20,50,u)
        Position(20,50,d)
        Position(40,30,d)
        Position(40,30,u)
        Position(45,80,u)
        Position(45,80,d)
        Position(45,40,d)
        Position(35,0,d)
        Position(35,0,u)
        Position(45,80,u)
        Position(45,80,d)
        Position(65,80,d)
        Position(65,10,d)
        Position(85,10,d)
        Position(85,25,d)
        Position(85,25,u)
        Position(138,0,220)
        
def DrawGrid():
        d=8
        u=25
        Position(138,0,220)
        Position(103,-15,u)
        time.sleep(1)
        Position(103,-15,d)
        Position(103,20,d)
        Position(103,55,d)
        Position(103,90,d)
        Position(103,125,d)
        Position(103,160,d)
        Position(103,195,d)
        Position(103,195,u)
        time.sleep(0.3)

        Position(173,-15,u)
        time.sleep(0.8)
        Position(173,-15,d)
        Position(173,20,d)
        Position(173,55,d)
        Position(173,90,d)
        Position(173,125,d)
        Position(173,160,d)
        Position(173,195,d)
        Position(173,195,u)
        time.sleep(0.3)
        
        Position(33,125,u)
        time.sleep(0.8)
        Position(33,125,d)
        Position(68,125,d)
        Position(103,125,d)
        Position(138,125,d)
        Position(173,125,d)
        Position(208,125,d)
        Position(243,125,d)
        Position(243,125,u)
        time.sleep(0.3)
        
        Position(33,55,u)
        time.sleep(0.8)
        Position(33,55,d)
        Position(68,55,d)
        Position(103,55,d)
        Position(138,55,d)
        Position(173,55,d)
        Position(208,55,d)
        Position(243,55,d)
        Position(243,55,u)
        time.sleep(0.3)
        
        Position(138,0,220)
"""
