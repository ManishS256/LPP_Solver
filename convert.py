
def convert():
    bv=[]
    rhs=[]
    f=open('input.txt','r')
    qnt=f.readline().strip()
    if(qnt=="max"):
        cc=[]
        tempcc=f.readline().strip().split(' ')
        for i in tempcc:
            cc.append(float(i))

    else:
        cc=[]
        tempcc=f.readline().strip().split(' ')
        for i in tempcc:
            cc.append(-1*float(i))

    acc=[]
    f.readline()
    tbv=f.readline().strip().split(' ')
    while (tbv[0] != 'end'):
        trhs=f.readline().strip().split(' ')
        if (float(trhs[1])<0):
            tempbv=[]
            rhs.append(-1*float(trhs[1]))
            if(trhs[0]=="gt"):
                acc.append("lt")
            elif(trhs[0]=="lt"):
                acc.append("gt")
            else:
                acc.append(trhs[0])
            for i in tbv:
                tempbv.append(-1*float(i))
        else:
            tempbv=[]
            rhs.append(float(trhs[1]))
            acc.append(trhs[0])
            for i in tbv:
                tempbv.append(float(i))
        bv.append(tempbv)
        tbv=f.readline().strip().split(' ')
    for i in range(len(acc)):
        if (acc[i] == 'gt'):
            bv[i].append(-1)
            cc.append(0)
            for j in range(len(acc)):
                if(j!=i):
                    bv[j].append(0)
        elif(acc[i] == 'lt'):
            bv[i].append(1)
            cc.append(0)
            for j in range(len(acc)):
                if(j!=i):
                    bv[j].append(0)

    for i in range(len(acc)):
        if (acc[i] == 'gt'):
            bv[i].append(1)
            cc.append(-10000000000000000000000)
            for j in range(len(acc)):
                if(j!=i):
                    bv[j].append(0)
        elif (acc[i] == 'eq'):
            bv[i].append(1)
            cc.append(-10000000000000000000000)
            for j in range(len(acc)):
                if(j!=i):
                    bv[j].append(0)   

    bvcc=[]
    v=[]
    bvlength=len(bv)
    cclength=len(cc)
    diff=cclength-bvlength
    for i in range(diff,cclength):
        bvcc.append(cc[i])
        v.append(i)
    f.close()

    return("Continue", bv, rhs, cc, bvcc, v)