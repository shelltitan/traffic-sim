import numpy as np
import matplotlib.pyplot as plt

road_t = []
road_dt = []
road_ev = []
size = 100
time_elapsed = 0
v_max = 5
max_density = 30

def v(density):
    return (1-density/max_density)*v_max

bc_rho = 0

for i in range(size):
    if i < size/2:
        road_t.append(30)
        road_dt.append(30)
    else:
        road_t.append(15)
        road_dt.append(15)
while time_elapsed < 1000:
    for i in range(size):
        if i == size - 1:
            road_dt[i] += 0.01/2 * (v(road_t[i]) * (road_t[i] - bc_rho) + road_t[i] * (v(road_t[i]) - v(bc_rho)))
        else:
            road_dt[i] += 0.01/2 * (v(road_t[i]) * (road_t[i] - road_t[i+1]) + road_t[i] * (v(road_t[i]) - v(road_t[i+1])))
            
    time_elapsed += 1
    road_t = road_dt.copy()
    if time_elapsed % 1 == 0:
        road_ev.append(road_t.copy())
    if time_elapsed % 100 == 0:
        print(time_elapsed)
array2 = []
#for i in road_ev:
#    temp_array = []
#    for k in i:
#        if(k < 0):
##            temp_array.append([0,0,-1*k*255/10]) #white
#            temp_array.append(0)
#        else:
#            temp_array.append(k*255/10) #black
#    array2.append(temp_array)

#pic_array = np.array(array2)
#img = Image.fromarray(pic_array)
x = range(0, 100)
for i in range(100):
    if i % 1 == 0:
        y = np.array(road_ev[i])
        plt.plot(x,y)
        plt.xlabel('Position')
        plt.ylabel('Density')
        plt.savefig('plot' + str(i) + '.png')
        plt.clf()