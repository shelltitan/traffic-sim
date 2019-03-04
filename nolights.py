import numpy as np
import matplotlib.pyplot as plt

#apply cellular automaton algorithm
def alg(road, sites, pnew, pred, limit):
    #acceleration
    for i in range(sites):
        if road[i]!=-1:
            if road[i]!=limit:
                road[i]+=1

    #deceleration depending on spacing and random deleceration
    for i in range(sites):
        if road[i]!=-1:
            rand=np.random.uniform()
            j=i+1
            if j<sites:
                d=0
                while road[j]==-1:
                    if j==sites-1:
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
    for i in range(sites):
        road2=np.append(road2, -1)
    for i in range(sites):
        if road[i]!=-1:
            j=i+int(road[i])
            if j<sites:
                road2[j]=road[i]                        

def func(sites, pnew, pred, limit, steps):
    
    road=np.array([])
    for i in range(sites):
        rand=np.random.uniform()
        if pnew>=rand:
            road=np.append(road, np.random.randint(0,limit+1))
        elif pnew<rand:
            road=np.append(road, -1)
    
    roads=[road]
    for i in range(steps-1):
        road=alg(road, sites, pnew, pred, limit)
        roads.append(road)
    roads=np.asarray(roads)
    roads=roads.astype(int)
    roads=np.ndarray.tolist(roads)
    for i in range(steps):
        for j in range(sites):
            roads[i][j]=str(roads[i][j])
            if roads[i][j]=='-1':
                roads[i][j]='.'            
    for i in range(steps-1):
        str1=''.join(roads[i])
        print(str1)
    #randomly, new car introduced
    if road2[0]==-1:
        if pnew>np.random.uniform():
            road2[0]=np.random.randint(0,limit+1)
    
    return road2

func(100,0.4,0.3,5,40)
