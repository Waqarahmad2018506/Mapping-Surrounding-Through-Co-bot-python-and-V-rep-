import sim
from time import sleep
import sys
import numpy as np
import matplotlib.pyplot as plt

sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

c=0.08726646
D=[]
E=[]
X=[]
Y=[]
P=[]
if clientID!=-1:
    print ('Connected to remote API server')

else:
    print ('Failed connecting to remote API server')
    sys.exit("could not connect")
print ('Program ended')

error1, leftMotor = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
error2, rightMotor = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)

error, sensor1 = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor1', sim.simx_opmode_oneshot_wait)
error, sensor2 = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor2', sim.simx_opmode_oneshot_wait)
error, sensor3 = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor3', sim.simx_opmode_oneshot_wait)
error, sensor4 = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor4', sim.simx_opmode_oneshot_wait)
error, sensor5 = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor5', sim.simx_opmode_oneshot_wait)
error3, Cobot = sim.simxGetObjectHandle(0, 'Pioneer_p3dx', sim.simx_opmode_oneshot_wait)


sim.simxSetJointTargetVelocity(clientID, leftMotor , 0.6, sim.simx_opmode_oneshot)
sim.simxSetJointTargetVelocity(clientID, rightMotor , 0.4, sim.simx_opmode_oneshot)



Error,detectionState1,D1, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor1,sim.simx_opmode_streaming)
Error,detectionState2,D2, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor2,sim.simx_opmode_streaming)
Error,detectionState3,D3, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor3,sim.simx_opmode_streaming)
Error,detectionState4,D4, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor4,sim.simx_opmode_streaming)
Error,detectionState5,D5, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor5,sim.simx_opmode_streaming)

error2,position = sim.simxGetObjectPosition(clientID, Cobot, -1, sim.simx_opmode_streaming)
error, angle = sim.simxGetObjectOrientation(clientID, Cobot, -1, sim.simx_opmode_streaming)
sleep(1)

for x in range(500):
    Error4,E1,D1, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor1,sim.simx_opmode_buffer)
    Error4,E2,D2, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor2,sim.simx_opmode_buffer)
    Error4,E3,D3, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor3,sim.simx_opmode_buffer)
    Error4,E4,D4, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor4,sim.simx_opmode_buffer)
    Error4,E5,D5, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor5,sim.simx_opmode_buffer)
    
    error2,position = sim.simxGetObjectPosition(clientID, Cobot, -1, sim.simx_opmode_buffer)
    error, angle = sim.simxGetObjectOrientation(clientID, Cobot, -1, sim.simx_opmode_buffer)
    
    # E.append([E1,E2,E3,E4,E5]) 
    # D.append([D1[2] , D2[2] , D3[2] , D4[2] , D5[2] , angle[2], position[0],position[1] ])
    # print(angle[2] , " x",position[0],"y",position[1])
    E = [E1,E2,E3,E4,E5]
    D=[D1[2] , D2[2] , D3[2] , D4[2] , D5[2]]
    gamma=  angle[2]
    x0 = position[0]
    y0 = position[1]
    for i in range(0,5):
        if E[i]==True:
            x=D[i]*np.cos(gamma+0.174532952-c*i)+x0
            y=D[i]*np.sin(gamma+0.174532952-c*i)+y0
            print(y,"  ",x)
            X.append(x)
            Y.append(y)
            P.append([x,y])
    plt.scatter(X, Y)
    plt.show()
    sleep(0.005)

    