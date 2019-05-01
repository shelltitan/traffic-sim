import numpy as np
import matplotlib.pyplot as plt

road_t = []
road_dt = []
road_ev = []
size = 2000
time_elapsed = 0
v_max = 30
max_density = 0.25

rho_l = 0.15
rho_r = 0.15
dx = 2000/size

for i in range(size):
    if 1000 < i:
        road_t.append(0.25)
        road_dt.append(0.25)
    else:
        road_t.append(0.15)
        road_dt.append(0.15)
while time_elapsed < 10000:
    for i in range(size):
        if i == 0:
            road_dt[i] = 1/2 * (road_t[i+1] + rho_l) - 0.003/2 * v_max * (1 - 2 * (road_t[i] / max_density)) * (road_t[i+1] - rho_l)
        elif i == size - 1:
            road_dt[i] = 1/2 * (rho_r + road_t[i-1]) - 0.003/2 * v_max * (1 - 2 * (road_t[i] / max_density)) * (rho_r - road_t[i-1])
        else:
            road_dt[i] = 1/2 * (road_t[i+1] + road_t[i-1]) - 0.003/2 * v_max * (1 - 2 * (road_t[i] / max_density)) * (road_t[i+1] - road_t[i-1])
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
#x = range(0, 2000)
#for i in range(10000):
 #   if i % 100 == 0:
#        y = np.array(road_ev[i])
#        plt.plot(x,y)
#        plt.xlabel('Position')
#        plt.ylabel('Density')
#        plt.savefig('plot' + str(i) + '.png')
#        plt.clf()
#y = range(0, 10000)
#X, Y = np.meshgrid(x, y)
#Z = np.array(road_ev)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                cmap='viridis', edgecolor='none')
#ax.set_xlabel('x')
#ax.set_ylabel('y')
#ax.set_zlabel('z')
#ax.view_init(90, 0)
#file = open('data.txt','w')
#file.write("%s\n" % road_ev[0])
#file.close()
#def make_image(data, outputname, size=(1, 1), dpi=800):
#    fig = plt.figure()
#    fig.set_size_inches(size)
#    ax = plt.Axes(fig, [0., 0., 1., 1.])
#    ax.set_axis_off()
#    fig.add_axes(ax)
#    plt.rcParams["axes.grid"] = True
#    plt.set_cmap('gray_r')
#    ax.imshow(data, aspect='equal')
#    plt.savefig(outputname, dpi=dpi)

# data = mpimg.imread(inputname)[:,:,0]
#data = np.arange(1,10).reshape((3, 3))
plt.imshow(road_ev, cmap='gray_r', interpolation='none')
#make_image(road_ev, 'out.png')