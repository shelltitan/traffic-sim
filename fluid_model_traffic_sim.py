from PIL import Image
import numpy as np
from mpl_toolkits import mplot3d
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

bc_rho1 = 0
bc_rho2 = 0
#bc_v1 = v(bc_rho1)
bc_v2 = v(bc_rho2)
bc_v1 = 0

for i in range(size):
    if i < size/2:
        road_t.append(29)
        road_dt.append(29)
    else:
        road_t.append(15)
        road_dt.append(15)
while time_elapsed < 1000:
    for i in range(size):
        if i == 0:
            road_dt[i] = road_t[i] + (road_t[i] * 0.01/2 * (bc_v1 - v(road_t[i+1]))) + (v(road_t[i]) * 0.01/2 * (bc_rho1 - road_t[i+1]))
        elif i == size - 1:
            road_dt[i] = road_t[i] + (road_t[i] * 0.01/2 * (v(road_t[i-1]) - bc_v2)) + (v(road_t[i]) * 0.01/2 * (road_t[i-1] - bc_rho2))
        else:
            road_dt[i] = road_t[i] + (road_t[i] * 0.01/2 * (v(road_t[i-1]) - v(road_t[i+1]))) +( v(road_t[i]) * 0.01/2 * (road_t[i-1] - road_t[i+1]))
            
    road_t = road_dt.copy()
#    road_ev.append(road_t.copy())
    time_elapsed += 1
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
y = range(0, 1000)
X, Y = np.meshgrid(x, y)
Z = np.array(road_ev)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(90, 0)
    