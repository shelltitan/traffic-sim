import numpy as np
import matplotlib.pyplot as plt

#traffic light
#apply cellular automaton algorithm
#road=road setup array, sites=numbers of cells, pnew=probability of new car (traffic density)
#pred=probability of speed reduction, limit=speed limit (in cells/timestep), position=position of traffic light
#stop=True or False
def alg2(road, sites, pnew, pred, limit, position, stop):
    #acceleration
    for i in range(sites+1):
        if road[i]>-1:
            if road[i]!=limit:
                road[i]+=1

    #deceleration depending on spacing and random deleceration
    for i in range(sites+1):
        if road[i]>-1:
            rand=np.random.uniform()
            j=i+1
            if j<sites:
                d=0
                while road[j]==-1 or road[j]==-3:
                    if j==sites:
                        d='end'
                        break
                    d+=1
                    j+=1   
                if d!='end':
                    if d<road[i]:
                        road[i]=d
                        if road[i]>0:
                            if pred>rand:
                                road[i]-=1
                    elif d>=road[i]:
                        if road[i]>0:
                            if pred>rand:
                                road[i]-=1

    #movement of cars
    road2=np.array([])
    if stop==True:
        light=-2
    elif stop==False:
        light=-3
    for i in range(position):
        road2=np.append(road2, -1)
    road2=np.append(road2, light)
    for i in range(sites-position):
        road2=np.append(road2, -1)
    count=0
    for i in range(sites+1):
        if road[i]>-1:
            j=i+int(road[i])                
            if j<sites+1:
                road2[j]=road[i]
            elif j>sites+1:
                count+=1

    #randomly, new car introduced
    if road2[0]==-1:
        if pnew>np.random.uniform():
            road2[0]=np.random.randint(0,limit+1)
    
    return road2, count

#function for 2 single direction roads with intersecting traffic lights
#outputs average traffic flow per second over whole duration
#position of traffic light is set to middle of road
#assumed 3 second delay time with both sets of lights red
def func4(sites, pnew, pred, limit, loops, on):
    
    road1=np.array([])
    road2=np.array([])
    position=int(sites/2)
    off=on-6
    stop1=True
    stop2=False
    light1=-2
    light2=-3
   
    for i in range(position):
        rand=np.random.uniform()
        if pnew/2.0>=rand:
            road1=np.append(road1, np.random.randint(0,limit+1))
        elif pnew/2.0<rand:
            road1=np.append(road1, -1)
    road1=np.append(road1, light1)
    for i in range(sites-position):
        rand=np.random.uniform()
        if pnew/2.0>=rand:
            road1=np.append(road1, np.random.randint(0,limit+1))
        elif pnew/2.0<rand:
            road1=np.append(road1, -1)
    
    for i in range(position):
        rand=np.random.uniform()
        if pnew/2.0>=rand:
            road2=np.append(road2, np.random.randint(0,limit+1))
        elif pnew/2.0<rand:
            road2=np.append(road2, -1)
    road2=np.append(road2, light2)
    for i in range(sites-position):
        rand=np.random.uniform()
        if pnew/2.0>=rand:
            road2=np.append(road2, np.random.randint(0,limit+1))
        elif pnew/2.0<rand:
            road2=np.append(road2, -1)   
    
    total=1
    count=0

    dura1=on
    dura2=off
    for i in range(loops):
        for j in range(dura1):
            [a1,b1]=alg2(road1, sites, pnew, pred, limit, position, stop1)
            road1=a1
            total+=1
            count+=b1
        for j in range(dura2):
            [a2,b2]=alg2(road2, sites, pnew, pred, limit, position, stop2)
            road2=a2
            count+=b2
        if stop1==True:
            stop1=False
            dura1=off
            road1[position]=-3
        elif stop1==False:
            stop1=True
            dura1=on
            road1[position]=-2
        if stop2==True:
            stop2=False
            dura2=off
            road2[position]=-3
        elif stop2==False:
            stop2=True
            dura2=on
            road2[position]=-2
    
    return count/total

func4(100, 0.2, 0.3, 5, 30, 30)
