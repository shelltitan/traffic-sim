import numpy as np
import matplotlib.pyplot as plt
import math

def alg2(road, sites, sep, pnew, ppass, pred, limit):
    #acceleration
    for i in range(sites):
        if road[i]!=[-1,-1]:
            if road[i][1]!=limit:
                road[i][1]+=1

    #deceleration depending on spacing and random deleceration
    for i in range(sites):
        if road[i][0]>-1 and road[i][1]>-1:
            rand=np.random.uniform()
            j=i+1
            if j<sites:
                d=0
                while road[j]==[-1,-1]:
                    if j==sites-1:
                        d='end'
                        break
                    d+=1
                    j+=1
                if d!='end':
                    if d<road[i][1]:
                        road[i][1]=d
                        if road[i][1]>0:
                            if pred>rand:
                                road[i][1]-=1
                    elif d>=road[i][1]:
                        if road[i][1]>0:
                            if pred>rand:
                                road[i][1]-=1

    #movement of buses
    road2=[[-1,-1] for i in range(sites)]
    count2=0
    for i in range(stops-1):
        if stop[i]==True:
            road2[(i+1)*sep]=[-2,-2]
        elif stop[i]==False:
            road2[(i+1)*sep]=[-3,-3]
            stop[i]=True
    for i in range(sites):
        if road[i][0]>-1 and road[i][1]>-1:
            j=i+int(road[i][1])
            if j<sites:
                if road2[i+1]==[-3,-3]:
                    road2[i+2]=road[i]
                else:
                    road2[j]=road[i]
            elif j>=sites:
                count2+=1
                
    #randomly, new bus introduced
    if road2[0]==[-1,-1]:
        if pnew>np.random.uniform():
            road2[0][0]=np.random.randint(0, int(ppass*100))
            road2[0][1]=np.random.randint(0,limit+1)
    
    return road2, count2

def func2(sites, sep, pnew, ppass, pred, limit, steps):
    
    road=[[-1,-1] for i in range(sites)]
    road[0]=[np.random.randint(0, int(ppass*100)), np.random.randint(0,limit+1)]
    global stops
    stops=math.floor(sites/sep)
    global stop
    stop=[]
    count=[]
    vals=[]
    for i in range(stops-1):
        road[(i+1)*sep]=[-2,-2]
        stop.append(True)
        count.append(-1)
        vals.append(np.random.randint(1, int(ppass*100)))
     
    count2=0
    for i in range(steps-1):
        [a,b]=alg2(road, sites, sep, pnew, ppass, pred, limit)
        road=a
        count2+=b
        for i in range(stops-1):
            if road[((i+1)*sep)-1][0]>-1 and road[((i+1)*sep)-1][1]>-1:
                if count[i]==-1:
                    off=np.random.randint(0,road[((i+1)*sep)-1][0]+1)   
                    on=np.random.randint(0,vals[i])
                    if (road[((i+1)*sep)-1][0]-off)+on>100:
                        on=100-(road[((i+1)*sep)-1][0]-off)
                    count[i]=off+on
                    road[((i+1)*sep)-1][0]=road[((i+1)*sep)-1][0]-off+on
                    vals[i]-=on
                elif count[i]==0:
                    stop[i]=False
                    count[i]=-1
                else:
                    count[i]-=1
            if (ppass/10)>np.random.uniform():
                vals[i]+=1
                
    return count2/(steps/60)
