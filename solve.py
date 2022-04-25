from iterator import *
from convert import *

def solve():
    a=convert()
    while(a[0]=="Continue"):
        a=iterator(a[1],a[2],a[3],a[4],a[5])
    star=-1
    for i in range(len(a[3])):
        if(a[3][i]==-10000000000000000000000):
            star=i
            break
            
    print(star)

    ifs=False

    if(a[0]=="Unbounded Problem"):
        return ("Unbounded Problem","Algorithm Terminated",0)

    elif(a[0]=="Algorithm Terminated"):
        b=("Single Solution")
        if(star!=-1):
            for i in a[5]:
                if(i >= star):
                    ifs=True
                    return ("Infeasible Solution","Algorithm Terminated",0)
            
        if(not(ifs)):
            if(star==-1):
                star=10000000000000000000000
            for i in range(len(a[6])):
                if(a[6][i]==0 and not(i in a[5]) and i<star):
                    b=iterator(a[1],a[2],a[3],a[4],a[5],i)
            tc=0
            j=0
            for i in range(len(a[2])):
                tc+=a[2][i]*a[4][i]
                j+=1
            f=open("input.txt",'r')
            stype=f.readline().strip()
            f.close()
            if(stype=="min"):
                tc=(-1*tc)
            else:
                tc=tc
    return(a, b, tc)