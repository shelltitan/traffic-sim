#-*- coding: utf-8 -*-
"""
Created on Sun Mar  3 21:50:12 2019

@author: Istvan
"""
from PIL import Image
import numpy as np

v_max = 5
time_elapsed = 0
flux = 0.5
on = True
double_flux_on = True
cars = 0

tile_number = 1000
density = 0.1
error = 0
lane = []
picture_lane = []
for i in range(tile_number):
    if np.random.uniform() > 0.5:
        lane.append(-1)
    else:
        lane.append(np.random.randint(0,v_max))
        cars += 1
while time_elapsed < 10000:
    if lane[0] == -1 and 0.5 > np.random.uniform():
        lane[0] = 1
        cars += 1
    if lane[1] == -1 and 0.4 > np.random.uniform() and double_flux_on:
        lane[1] = 1
        cars += 1
    for i in range(tile_number):
        if lane[i] != -1 and lane[i] < v_max:
            summ = 0
            if lane[i]+ 1 + i >= tile_number:
                z = tile_number - i -1
                for k in range(z):
                    summ += lane[i+k+1]
                if summ == z*-1:
                    lane[i] = lane[i]+1
            else:
                for k in range(lane[i]+1):
                    summ += lane[i+k+1]
                if summ == (lane[i]+1)*-1:
                    lane[i] = lane[i]+1
        if lane[i] > 0:
            summ = 0
            if lane[i] + i >= tile_number:
                z = tile_number - i -1
                for k in range(z):
                    summ += lane[i+k+1]
                if summ > z*-1:
                    for k in range(z):
                        if (lane[k+i+1]) > -1:
                            lane[i] = k
                            break
            else:
                for k in range(lane[i]):
                    summ += lane[i+k+1]
                if summ > (lane[i])*-1:
                    for k in range(lane[i]):
                        if (lane[k+i+1]) > -1:
                            lane[i] = k
                            break
    for i in range(tile_number):
        if i > tile_number/4 and i < tile_number *3/4 and 0.3 > np.random.uniform() and lane[i] > 0 and on and time_elapsed > 5000 and time_elapsed < 5500:
            lane[i] = lane[i] - 1
        if lane[i] > 0 and 0.2 > np.random.uniform():
            lane[i] = lane[i] - 1
    for i in range(tile_number):
        if lane[tile_number -1 - i] > 0 and i >= v_max:
            temp = lane[tile_number -1 - i]
            if lane[tile_number - 1 - i + temp] != -1:
                error +=1
            lane[tile_number - 1 - i + temp] = temp
            lane[tile_number -1 - i] = -1
        if i < v_max and lane[tile_number -1 - i] > 0:
            temp = lane[tile_number -1 - i]
            if temp > i:
                cars -= 1
                lane[tile_number -1 - i] = -1
            else:
                if lane[tile_number - 1 - i + temp] != -1:
                    error +=1
                lane[tile_number -1 - i+temp] = temp
                lane[tile_number -1 - i] = -1
    time_elapsed += 1
    if time_elapsed % 100 == 0:
        print(time_elapsed)
        print(cars)
    if time_elapsed % 1 == 0:
        picture_lane.append(lane.copy())
    if cars >= tile_number:
        print("can't happen")
        break
array2 = []
for i in picture_lane:
    temp_array = []
    for k in i:
        if(k == -1):
            temp_array.append(255) #white
        else:
            temp_array.append(0) #black
    array2.append(temp_array)
pic_array = np.array(array2)
img = Image.fromarray(pic_array)
print(error)