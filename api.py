from flask import request, send_from_directory, send_file
from flask_restful import Resource, Api, reqparse
from solve import *

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
                if(ans[3][i]==-10000000000000000000000):
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
                if(mans[3][i]==-10000000000000000):
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
                if(ans[3][i]==-10000000000000000):
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
                if(ans[3][i]==-10000000000000000000000):
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
                if(mans[3][i]==-10000000000000000000000):
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
                if(ans[3][i]==-10000000000000000000000):
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
