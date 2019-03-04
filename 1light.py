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

def func2(sites, pnew, pred, limit, loops, position, stop, on, off):
#loops=number of light changes, on=stop duration, off=go duration    
    road=np.array([])
    if stop==True:
        light=-2
    elif stop==False:
        light=-3
    for i in range(position):
        rand=np.random.uniform()
        if pnew>=rand:
            road=np.append(road, np.random.randint(0,limit+1))
        elif pnew<rand:
            road=np.append(road, -1)
    road=np.append(road, light)
    for i in range(sites-position):
        rand=np.random.uniform()
        if pnew>=rand:
            road=np.append(road, np.random.randint(0,limit+1))
        elif pnew<rand:
            road=np.append(road, -1)
     
    roads=[road]
    total=1
    count=0
    if stop==True:
        dura=on
    elif stop==False:
        dura=off
    for i in range(loops):
        for j in range(dura):
            [a,b]=alg2(road, sites, pnew, pred, limit, position, stop)
            road=a
            roads.append(road)
            total+=1
            count+=b
        if stop==True:
            stop=False
            dura=off
            road[position]=-3
        elif stop==False:
            stop=True
            dura=on
            road[position]=-2
   
    roads=np.asarray(roads)
    roads=roads.astype(int)
    roads=np.ndarray.tolist(roads)
    for i in range(total):
        for j in range(sites+1):
            roads[i][j]=str(roads[i][j])
            if roads[i][j]=='-1':
                roads[i][j]='.'
            elif roads[i][j]=='-2':
                roads[i][j]='|'
            elif roads[i][j]=='-3':
                roads[i][j]='.'
    for i in range(total):
        str1=''.join(roads[i])
        print(str1)
        
    return print('Number of cars passed = ', count)

func2(100,0.2,0.3,5,10,50,False,40,30)
