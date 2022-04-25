
def iterator(bv, rhs, cc, bvcc, v, another=False):
    cjzj=[]
    cclen=len(cc)
    bvcclen=len(bvcc)
    for i in range(cclen):
        temp=0
        for j in range(bvcclen):
            temp=temp+(bv[j][i]*bvcc[j])
        cjzj+=[cc[i]-temp]
    if(another):
        cjzj[another]=1
    if(type(another)==int and another==0):
        cjzj[0]=1
    maxcjzj=max(cjzj)
    if(maxcjzj<=0):
        return("Algorithm Terminated",bv, rhs, cc, bvcc, v, cjzj)    
    maxi=0
    pc=float()
    for k in range(len(cjzj)):
        if(maxi<cjzj[k]):
            maxi=cjzj[k]
            pc=k
    theta=[]
    for i in range(len(bv)):
        try:
            temp=rhs[i]/bv[i][pc]
            theta+=[temp]
        except:
            theta+=[10000000000000000]
    mini=10000000000000000
    pr=0
    for k in range(len(theta)):
        if(mini>theta[k] and theta[k]!=10000000000000000 and theta[k]>0):
            mini=theta[k]
            pr=k
    if(mini==10000000000000000):
        return("Unbounded Problem",bv, rhs, cc, bvcc, v)
    pe=bv[pr][pc]
    nbv=[]
    nrhs=[]
    for i in range(len(rhs)):
        nrhs.append(0)
    for i in range(len(bv)):
        nbv+=[[]]
    for i in range(len(bv[pr])):
        temp=bv[pr][i]/pe
        nbv[pr].append(temp)
    nrhs[pr]=rhs[pr]/pe
    for i in range(len(bv)):
        epr=nbv[pr]
        if(i!=pr):
            for j in range(len(bv[i])):
                nbv[i].append(bv[i][j]-(bv[i][pc]*nbv[pr][j]))
            nrhs[i]=rhs[i]-(bv[i][pc]*nrhs[pr])

    nbvcc=[]
    nv=[]
    for j in range(len(bvcc)):
        nbvcc.append(0)
        nv.append(0)
    for i in range(len(bvcc)):
        if (i==pr):
            nbvcc[i]=cc[pc]
            nv[i]=pc
        else:
            nbvcc[i]=bvcc[i]
            nv[i]=v[i]
    return("Continue",nbv,nrhs,cc,nbvcc,nv)