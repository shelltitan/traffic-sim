import numpy as np

#algorithm for roundabout
def alg2(road, road1, road2, road3, road4, pnew, pred, limit1, limit2):
    #acceleration
    for i in range(20):
        if road[i]!=-1:
            if road[i]!=limit1:
                road[i]+=1
    
    for i in range(50):
        if road1[i]!=-1:
            if road1[i]!=limit2:
                road1[i]+=1
        if road2[i]!=-1:
            if road2[i]!=limit2:
                road2[i]+=1
        if road3[i]!=-1:
            if road3[i]!=limit2:
                road3[i]+=1
        if road4[i]!=-1:
            if road4[i]!=limit2:
                road4[i]+=1
                
    #cars at end of roads join roundabout if there is space
    if road1[49]!=-1 and road[4]==-1 and road[3]==-1 and road[2]==-1:
        road1[49]=-1
        road[4]=1
    if road1[49]!=-1 and road[9]==-1 and road[8]==-1 and road[7]==-1:
        road2[49]=-1
        road[9]=1
    if road1[49]!=-1 and road[14]==-1 and road[13]==-1 and road[12]==-1:
        road3[49]=-1
        road[14]=1
    if road1[49]!=-1 and road[19]==-1 and road[18]==-1 and road[17]==-1:
        road4[49]=-1
        road[19]=1
        
    #deceleration depending on spacing and random deleceration
    for i in range(20):
        if road[i]!=-1:
            rand=np.random.uniform()
            j=i+1
            if j<20:
                d=0
                while road[j]==-1:
                    d+=1
                    j+=1                 
                    if j==20:
                        j=0               
                if d<road[i]:
                    road[i]=d
                    if road[i]>0:
                        if pred>rand:
                            road[i]-=1
                elif d>=road[i]:
                    if road[i]>0:
                        if pred>rand:
                            road[i]-=1
            elif j==20:
                d=0
                j=0
                while road[j]==-1:
                    d+=1
                    j+=1
                if d<road[i]:
                    road[i]=d
                    if road[i]>0:
                        if pred>rand:
                            road[i]-=1
                elif d>=road[i]:
                    if road[i]>0:
                        if pred>rand:
                            road[i]-=1    

    #movement of cars with chance to exit
    count=0
    road0=np.array([])
    for i in range(20):
        road0=np.append(road0, -1)
    for i in range(20):
        if road[i]!=-1:
            j=i+int(road[i])
            if j<20:
                road0[j]=road[i]                
                if i<3 and j>=3:
                    if np.random.uniform()<(1/3):
                        road0[j]=-1
                        count+=1
                elif i<8 and j>=8:
                    if np.random.uniform()<(1/3):
                        road0[j]=-1
                        count+=1
                elif i<13 and j>=13:
                    if np.random.uniform()<(1/3):
                        road0[j]=-1
                        count+=1
                elif j==18:
                    if np.random.uniform()<(1/3):
                        road0[j]=-1
                        count+=1
            elif j>=20:
                road0[j-20]=road[i]
                if np.random.uniform()<(1/3):
                    road0[j-20]=-1
                    count+=1
                    
    #algorithm applied to other roads
    for i in range(50):
        if road1[i]!=-1:
            rand=np.random.uniform()
            j=i+1
            if j<50:
                d=0
                while road1[j]==-1:
                    d+=1
                    j+=1 
                    if j==50:
                        break 
                if d<road1[i]:
                    road1[i]=d
                    if road1[i]>0:
                        if pred>rand:
                            road1[i]-=1
                elif d>=road1[i]:
                    if road1[i]>0:
                        if pred>rand:
                            road1[i]-=1    

    for i in range(50):
        if road2[i]!=-1:
            rand=np.random.uniform()
            j=i+1
            if j<50:
                d=0
                while road2[j]==-1:
                    d+=1
                    j+=1 
                    if j==50:
                        break 
                if d<road2[i]:
                    road2[i]=d
                    if road2[i]>0:
                        if pred>rand:
                            road2[i]-=1
                elif d>=road2[i]:
                    if road2[i]>0:
                        if pred>rand:
                            road2[i]-=1 

    for i in range(50):
        if road3[i]!=-1:
            rand=np.random.uniform()
            j=i+1
            if j<50:
                d=0
                while road3[j]==-1:
                    d+=1
                    j+=1 
                    if j==50:
                        break 
                if d<road3[i]:
                    road3[i]=d
                    if road3[i]>0:
                        if pred>rand:
                            road3[i]-=1
                elif d>=road3[i]:
                    if road3[i]>0:
                        if pred>rand:
                            road3[i]-=1 
                            
    for i in range(50):
        if road4[i]!=-1:
            rand=np.random.uniform()
            j=i+1
            if j<50:
                d=0
                while road4[j]==-1:
                    d+=1
                    j+=1 
                    if j==50:
                        break 
                if d<road4[i]:
                    road4[i]=d
                    if road4[i]>0:
                        if pred>rand:
                            road4[i]-=1
                elif d>=road4[i]:
                    if road4[i]>0:
                        if pred>rand:
                            road4[i]-=1
                            
    road12=np.array([])
    for i in range(50):
        road12=np.append(road12, -1)
    for i in range(50):
        if road1[i]!=-1:
            j=i+int(road1[i])
            if j<50:
                road12[j]=road1[i]
            elif j>=50:
                road12[49]=road1[i]

    if road12[0]==-1:
        if pnew>np.random.uniform():
            road12[0]=np.random.randint(0,limit2+1)
            
    road22=np.array([])
    for i in range(50):
        road22=np.append(road22, -1)
    for i in range(50):
        if road2[i]!=-1:
            j=i+int(road2[i])
            if j<50:
                road22[j]=road2[i]
            elif j>=50:
                road22[49]=road2[i]

    if road22[0]==-1:
        if pnew>np.random.uniform():
            road22[0]=np.random.randint(0,limit2+1)
            
    road32=np.array([])
    for i in range(50):
        road32=np.append(road32, -1)
    for i in range(50):
        if road3[i]!=-1:
            j=i+int(road3[i])
            if j<50:
                road32[j]=road3[i]
            elif j>=50:
                road32[49]=road3[i]

    if road32[0]==-1:
        if pnew>np.random.uniform():
            road32[0]=np.random.randint(0,limit2+1)
            
    road42=np.array([])
    for i in range(50):
        road42=np.append(road42, -1)
    for i in range(50):
        if road4[i]!=-1:
            j=i+int(road4[i])
            if j<50:
                road42[j]=road4[i]
            elif j>=50:
                road42[49]=road4[i]

    if road42[0]==-1:
        if pnew>np.random.uniform():
            road42[0]=np.random.randint(0,limit2+1)
                            
    return road0, road12, road22, road32, road42, count

def roundabout(pnew, pred, limit1, limit2, steps):
    
    road=np.array([])
    for i in range(20):
        rand=np.random.uniform()
        if pnew>=rand:
            road=np.append(road, np.random.randint(0,limit1+1))
        elif pnew<rand:
            road=np.append(road, -1)
            
    road1=np.array([])
    for i in range(50):
        rand=np.random.uniform()
        if pnew>=rand:
            road1=np.append(road1, np.random.randint(0,limit2+1))
        elif pnew<rand:
            road1=np.append(road1, -1)
            
    road2=np.array([])
    for i in range(50):
        rand=np.random.uniform()
        if pnew>=rand:
            road2=np.append(road2, np.random.randint(0,limit2+1))
        elif pnew<rand:
            road2=np.append(road2, -1)
            
    road3=np.array([])
    for i in range(50):
        rand=np.random.uniform()
        if pnew>=rand:
            road3=np.append(road3, np.random.randint(0,limit2+1))
        elif pnew<rand:
            road3=np.append(road3, -1)
            
    road4=np.array([])
    for i in range(50):
        rand=np.random.uniform()
        if pnew>=rand:
            road4=np.append(road4, np.random.randint(0,limit2+1))
        elif pnew<rand:
            road4=np.append(road4, -1)
    
    count=0
    roads=[road]
    for i in range(steps-1):
        [a,b,c,d,e,f]=alg2(road, road1, road2, road3, road4, pnew, pred, limit1, limit2)
        road=a
        road1=b
        road2=c
        road3=d
        road4=e
        roads.append(road)
        count+=f
    roads=np.asarray(roads)
    roads=roads.astype(int)
    roads=np.ndarray.tolist(roads)
    for i in range(steps):
        for j in range(20):
            roads[i][j]=str(roads[i][j])
            if roads[i][j]=='-1':
                roads[i][j]='.'            
    for i in range(steps-1):
        str1=''.join(roads[i])
        print(str1)
        
    return print(count/steps)

roundabout(0.3, 0.3, 3, 5, 300)
