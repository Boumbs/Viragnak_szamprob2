#def szulo(i):
#    return i//2

#def bal(i):
#    return 2*i

#def jobb(i):
#    return 2*i+1

#def kupacbaBeszur(K,e):
#    K.append(e)
#    i=len(K)-1
#    while i>1 and K[szulo(i)]<e:
#        K[i]=K[szulo(i)]
#        i=szulo(i)
#    K[i]=e

#def kupacbolElso(K):
#    elso=K[1]
#    K[1]=K[len(K)-1]
#    del K[-1]
#    kupacol(K,1)
#    return elso

#def kupacol(K,i):
#    b=bal(i)
#    j=jobb(i)
#    if b<len(K) and K[b] > K[i]:
#        legnagyobb=b
#    else:
#        legnagyobb=i
#    if j<len(K) and K[j]>K[legnagyobb]:
#        legnagyobb=j
#    if legnagyobb!=i:
#        cs=K[i]
#        K[i]=K[legnagyobb]
#        K[legnagyobb]=cs
#        kupacol(K,legnagyobb)
#def rendez(K):
#    er=[]
#    while len(K)>1:
#        #print(K)
#        er.append(kupacbolElso(K))
#    return er

#K=[0]
#for i in range(4):
#    e=int(input())
#    kupacbaBeszur(K,e)

#print(rendez(K))

#---------------------------------------------------------------
# zárójelezés
#-------------------------------------------------------------------

import queue

szotar={"{":"}","[":"]","(":")"}
kezdo="([{"
csuko=")]}"

def zarojelEllenorzes(kifejezes):
    verem=queue.deque()
    jo=True
    i=0
    while i<len(kifejezes) and jo:
        if kifejezes[i] in kezdo:
            verem.append(kifejezes[i])
        if kifejezes[i] in csuko:
            if len(verem)==0:
                jo=False
            else:
                if szotar[verem.pop()]!=kifejezes[i]:
                    jo=False
        i+=1
    if jo:
        if len(verem)!=0:
            jo=False
    return jo


kifejezes=input()
print(zarojelEllenorzes(kifejezes))