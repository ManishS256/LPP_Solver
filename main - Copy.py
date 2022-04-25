from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify, send_file
from flask_restful import Resource, Api, reqparse
from werkzeug.exceptions import HTTPException
import json
import os
app=None
api=None
app =Flask(__name__,template_folder='templates',static_folder='static')
api=Api(app)
app.app_context().push()

@app.route("/",methods=["GET"])
def homepage():
  if request.method=="GET":
    return render_template("index.html")

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
    pc=int()
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
            theta+=[10000]
    mini=10000
    pr=0
    for k in range(len(theta)):
        if(mini>theta[k] and theta[k]!=10000 and theta[k]>0):
            mini=theta[k]
            pr=k
    if(mini==10000):
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




def convert():
    bv=[]
    rhs=[]
    f=open('input.txt','r')
    qnt=f.readline().strip()
    if(qnt=="max"):
        cc=[]
        tempcc=f.readline().strip().split(' ')
        for i in tempcc:
            cc.append(int(i))

    else:
        cc=[]
        tempcc=f.readline().strip().split(' ')
        for i in tempcc:
            cc.append(-1*int(i))

    acc=[]
    f.readline()
    tbv=f.readline().strip().split(' ')
    while (tbv[0] != 'end'):
        trhs=f.readline().strip().split(' ')
        if (int(trhs[1])<0):
            tempbv=[]
            rhs.append(-1*int(trhs[1]))
            if(trhs[0]=="gt"):
                acc.append("lt")
            elif(trhs[0]=="lt"):
                acc.append("gt")
            else:
                acc.append(trhs[0])
            for i in tbv:
                tempbv.append(-1*int(i))
        else:
            tempbv=[]
            rhs.append(int(trhs[1]))
            acc.append(trhs[0])
            for i in tbv:
                tempbv.append(int(i))
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
            cc.append(-10000)
            for j in range(len(acc)):
                if(j!=i):
                    bv[j].append(0)
        elif (acc[i] == 'eq'):
            bv[i].append(1)
            cc.append(-10000)
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

def solve():
    a=convert()
    while(a[0]=="Continue"):
        a=iterator(a[1],a[2],a[3],a[4],a[5])
    star=-1
    for i in range(len(a[3])):
        if(a[3][i]==-10000):
            star=i
            break

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
                star=10000
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

class SolvetypeAPI(Resource):
    def put(self):
        qn=request.data
        f=open('input.txt','wb')
        f.write(qn)
        f.close()
        ans,mans,tc=solve()
        answer=""
        print (ans)
        print("")
        if (ans[0]=="Algorithm Terminated" and mans[0]=="Continue"):
            answer+="Optimal Solution\n"
            star=-1
            for i in range(len(ans[3])):
                if(ans[3][i]==-10000):
                    star=i
                    break
            if(star==-1):
                star=len(ans[3])
            vn=1
            for i in range(star):
                answer+="X"+str(vn)+" = "
                if((vn-1) in ans[5]):
                    pos=ans[5].index(vn-1)
                    answer+=str(ans[2][pos])+"\n"
                else:
                    answer+="0\n"
                vn+=1
            answer+="Optimal Cost = "+str(tc)+"\n\n"
            answer+="Alternate Solution\n"
            for i in range(len(mans[3])):
                if(mans[3][i]==-10000):
                    star=i
                    break
            if(star==-1):
                star=len(mans[3])
            vn=1
            for i in range(star):
                answer+="X"+str(vn)+" = "
                if((vn-1) in mans[5]):
                    pos=mans[5].index(vn-1)
                    answer+=str(mans[2][pos])+"\n"
                else:
                    answer+="0\n"
                vn+=1
            answer+="Optimal Cost = "+str(tc)+"\n"
            print(answer)
            return answer

        elif (ans[0]=="Algorithm Terminated"):

            answer+="Optimal Solution\n"
            star=-1
            for i in range(len(ans[3])):
                if(ans[3][i]==-10000):
                    star=i
                    break
            if(star==-1):
                star=len(ans[3])
            vn=1
            for i in range(star):
                answer+="X"+str(vn)+" = "
                if((vn-1) in ans[5]):
                    pos=ans[5].index(vn-1)
                    answer+=str(ans[2][pos])+"\n"
                else:
                    answer+="0\n"
                vn+=1
            answer+="Optimal Cost = "+str(tc)

            print(answer)
            return answer
        elif (ans=="Infeasible Solution"):
            return "Infeasible Solution"
        elif (ans=="Unbounded Problem"):
            return "Unbounded Problem"

class SolvefileAPI(Resource):
    def put(self):
        fil=request.files["impfile"]
        text=fil.read()
        f=open('input.txt','wb')
        f.write(text)
        f.close()
        ans,mans,tc=solve()
        answer=""
        print (ans)
        print("")
        if (ans[0]=="Algorithm Terminated" and mans[0]=="Continue"):
            answer+="Optimal Solution\n"
            star=-1
            for i in range(len(ans[3])):
                if(ans[3][i]==-10000):
                    star=i
                    break
            if(star==-1):
                star=len(ans[3])
            vn=1
            for i in range(star):
                answer+="X"+str(vn)+" = "
                if((vn-1) in ans[5]):
                    pos=ans[5].index(vn-1)
                    answer+=str(ans[2][pos])+"\n"
                else:
                    answer+="0\n"
                vn+=1
            answer+="Optimal Cost = "+str(tc)+"\n\n"
            answer+="Alternate Solution\n"
            for i in range(len(mans[3])):
                if(mans[3][i]==-10000):
                    star=i
                    break
            if(star==-1):
                star=len(mans[3])
            vn=1
            for i in range(star):
                answer+="X"+str(vn)+" = "
                if((vn-1) in mans[5]):
                    pos=mans[5].index(vn-1)
                    answer+=str(mans[2][pos])+"\n"
                else:
                    answer+="0\n"
                vn+=1
            answer+="Optimal Cost = "+str(tc)+"\n"
            print(answer)
            return answer

        elif (ans[0]=="Algorithm Terminated"):

            answer+="Optimal Solution\n"
            star=-1
            for i in range(len(ans[3])):
                if(ans[3][i]==-10000):
                    star=i
                    break
            if(star==-1):
                star=len(ans[3])
            vn=1
            for i in range(star):
                answer+="X"+str(vn)+" = "
                if((vn-1) in ans[5]):
                    pos=ans[5].index(vn-1)
                    answer+=str(ans[2][pos])+"\n"
                else:
                    answer+="0\n"
                vn+=1
            answer+="Optimal Cost = "+str(tc)

            print(answer)
            return answer
        elif (ans=="Infeasible Solution"):
            return "Infeasible Solution"
        elif (ans=="Unbounded Problem"):
            return "Unbounded Problem"


api.add_resource(SolvetypeAPI,"/api/solve/type")
api.add_resource(SolvefileAPI,"/api/solve/file")

if __name__ =="__main__":
  app.debug=True
  app.run(host='0.0.0.0',port='5000')