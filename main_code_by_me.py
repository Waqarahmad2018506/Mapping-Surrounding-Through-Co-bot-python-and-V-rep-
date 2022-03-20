# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 12:26:46 2022

@author: Pc
"""
import sim
from time import sleep
import sys
import numpy as np
import matplotlib.pyplot as plt

sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

A=[]

if clientID!=-1:
    print ('Connected to remote API server')

else:
    print ('Failed connecting to remote API server')
    sys.exit("could not connect")
print ('Program ended')

error1, leftMotor = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_leftMotor', sim.simx_opmode_oneshot_wait)
error2, rightMotor = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_rightMotor', sim.simx_opmode_oneshot_wait)

error3, sensor1 = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor1', sim.simx_opmode_oneshot_wait)
error3, sensor4 = sim.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor4', sim.simx_opmode_oneshot_wait)


sim.simxSetJointTargetVelocity(clientID, leftMotor , 0.5, sim.simx_opmode_oneshot)
sim.simxSetJointTargetVelocity(clientID, rightMotor , 0.4, sim.simx_opmode_oneshot)



Error4,detectionState1,D1, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor1,sim.simx_opmode_streaming)
Error4,detectionState4,D4, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor4,sim.simx_opmode_streaming)


sleep(1)
for x in range(50):
    
    Error4,detectionState1,D1, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor1,sim.simx_opmode_buffer)
    Error4,detectionState4,D4, detectedObjectHandle, detectedSurfaceNormalVector=sim.simxReadProximitySensor(clientID,sensor4,sim.simx_opmode_buffer)
    
    
    print(x,"  S1  " , np.linalg.norm(np.array(D1)), "  " ,detectionState1, "  S4  " , np.linalg.norm(np.array(D4)), "  " ,detectionState4 )
    
    sleep(1)

    