import time
#def Paros(N):
#    if N==0:
#        return True
#    else:
#        if N==1:
#            return False
#        else:
#            return Paratlan(N-1)

#def Paratlan(N):
#    if N==1:
#        return True
#    else:
#        if N==0:
#            return False
#        else:
#            return Paros(N-1)

#N=int(input())
#if Paros(N):
#    print("paros")
#else:
#    print("paratlan")

#Fibonacci 1, 1,2,3,5,8,13,
#from typing import ParamSpec


def Fibonacci(N):
    if N<3:
        return 1
    else:
        return Fibonacci(N-1)+Fibonacci(N-2)
def FibonacciIter(N):
    if N<3:
        return 1
    else:
        fibo=[1,1]
        for i in range(N-2):
            fibo.append(fibo[-1]+fibo[-2])
        return fibo[-1]
def FibonacciIter2(N):
    if N<3:
        return 1
    else:
        fibo=[1,1]
        i=2
        while i!=N:
            szam=fibo[0]+fibo[1]
            fibo=[fibo[1],szam]
            i=i+1
        return szam
#N=int(input())
#print(Fibonacci(N))
#print(FibonacciIter(N))
kezd=time.time()
#print(Fibonacci(N))
#print(FibonacciIter(N))
#print(FibonacciIter2(N))
vege=time.time()
#print(vege-kezd)

# N alatt a K 
#def Binom(n,k):
#    if k==1 or k==n:
#        return 1
#    else:
#        return Binom(n-1,k)+Binom(n-1,k-1)
#n=int(input())
#k=int(input())
#print(Binom(n,k))

#def FelA(N):
#    if N == 1:
#        return 2
#    elif N == 2:
#        return 7
#    else:
#        return 2*FelA(N-1)+3*FelA(N-2)
#N=int(input())
#print(FelA(N))

#szo=input()
#def Forditva(szo):
#    if len(szo)==0:
#        return ""
#    else:
#        return szo[-1]+Forditva(szo[0:len(szo)-1])

#print(Forditva(szo))


#N=int(input())
#def SzoGeneralas(aktszo,N):
#    if len(aktszo)==N+1:
#        print(aktszo)
#    else:
#        SzoGeneralas(aktszo+"a",N)
#        SzoGeneralas(aktszo+"c",N)
#        if aktszo[-1]!="b":
#            SzoGeneralas(aktszo+"b",N)

#print(SzoGeneralas(" ",N))
#---------------------------------------------------------------
def Osszefesules(A,B):
    ia=0
    ib=0
    C=[]
    while ia<len(A) or ib<len(B):
        if (ia<len(A) and (((ib<len(B) and A[ia]<B[ib]) or (ib>=len(B))))):
            #if ia < len(A) and (ib >= len(B) or A[ia] < B[ib]):
            C.append(A[ia])
            ia+=1
        else:
            C.append(B[ib])
            ib+=1
    return C

#A=[1,2,5,7,9]
#B=[3,6,10,13]
#C=Osszefesules(A,B)
#print(C)

def Rendez(A):
    if len(A)>1:
        K=len(A)//2
        return Osszefesules(Rendez(A[:K]),Rendez(A[K:]))
    else:
        return A

#X=[1,8,3,9,5,7,2]
#R=Rendez(X)
#print(R)

def Szetvalogatas(A,E,V):
    seged=A[E]
    while E<V:
        while E<V and A[V]>seged:
            V-=1
        if E<V:
            A[E]=A[V]
            E+=1
            while E<V and A[E]<seged:
                E+=1
            if E<V:
                A[V]=A[E]
                V-=1
    A[E]=seged
    K=E
    return K #E

Y=[6, 1, 9, 4, 7, 8, 5, 3]
Er=Szetvalogatas(Y,0,7)
print(Y)
print(Er)
