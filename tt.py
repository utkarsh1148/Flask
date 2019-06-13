import math as m
import random as r
def FitnessFunction(x):
    s=0
    s= x[0]*x[0] + 2*x[1]*x[1] - .3*m.cos(3*m.pi*x[0]) -.4*m.cos(4*m.pi*x[1]) + 0.7
    return s


x=0
if(x==0):
    CBEST=[1,1]
    x=1
    for i in range(1000000):
      
            
        C=[]
        C.append(r.randint(-100,100))
        C.append(r.randint(-100,100))
        for i in range(1):
            if(FitnessFunction(C)<999999):
                
                if(FitnessFunction(C)>FitnessFunction(CBEST)):
                    CBEST=C
                    
                else:
                    continue

    print(FitnessFunction(CBEST),CBEST)
