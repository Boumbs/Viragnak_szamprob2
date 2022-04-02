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
