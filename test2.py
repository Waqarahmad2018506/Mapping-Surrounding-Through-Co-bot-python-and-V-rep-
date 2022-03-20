# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 21:03:45 2022

@author: Pc
"""
import sim
from time import sleep
import sys
import numpy as np
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

if clientID!=-1:
    print ('Connected to remote API server')

else:
    print ('Failed connecting to remote API server')
    sys.exit("could not connect")

data2=[]
error1, sensor1 = sim.simxGetObjectHandle(0, 'SICK_TiM310_sensor1', sim.simx_opmode_oneshot_wait)
# error2, sensor2 = sim.simxGetObjectHandle(0, 'SICK_TiM310_sensor2', sim.simx_opmode_oneshot_wait)

error3, data = sim.simxGetStringSignal(clientID, "sensor1", sim.simx_opmode_streaming)
print("1")
for i in range(3):
    error4, data = sim.simxGetStringSignal(clientID,'sensor1',sim.simx_opmode_buffer)
    print("2")
    array =sim.simxUnpackFloats(data)
    data2.append(array)

# print(array)

# error1, sensor1 = sim.simxGetObjectHandle(0, 'velodyneVPL_16_sensor1', sim.simx_opmode_oneshot_wait)
# returnCode,signalValue=sim.simxGetStringSignal(clientID, sensor1,sim.simx_opmode_streaming)
# # returnCode2,signalValue=sim.simxGetStringSignal(clientID,sensor1,sim.simx_opmode_buffer) 