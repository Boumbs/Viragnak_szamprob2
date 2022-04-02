#class Ember:
#    nev=""
#    lakcim=""
#    def __init__(self, nev,lakcim):
#        self.nev=nev
#        self.lakcim=lakcim
#    def kiir(self):
#        print(self.nev+" "+self.lakcim)
#vki=Ember("Gipsz Jakab","Budapest")
#vki.kiir()
    
#class Sor:
#    elemek=[]
#    def __init__(self):
#        self.elemek=[]
#    def ures(self):
#        self.elemek=[]
#    def ures_e(self):
#        return len(self.elemek)==0
#    def sorba(self,elem):
#        self.elemek.append(elem)
#    def sorbol(self):
#        eredmeny=self.elemek[0]
#        self.elemek=self.elemek[1:]
#        return eredmeny
#    def elso(self):
#        return self.elemek[0]

#s=Sor()
#s.sorba(3)
#if s.ures_e():
#    print("Ures")
#else:
#    print("Nem")
#for i in range(10,15):
#    s.sorba(i)
#print(s.elso())
#while not s.ures_e():
#    print(s.sorbol())

#import queue

#sor=queue.Queue()
#sor.put(3)
#if sor.qsize()==0:
#    print("ures")
#else:
#    print("nem")
#for i in range(10,15):
#    sor.put(i)
#while sor.qsize()!=0:
#    print(sor.get())

#import queue
#verem=queue.deque()
#for i in range(10):
#    verem.append(i)
#while len(verem)!=0:
#    print(verem.pop())

a=2
b=(1,3,"alma")
##b[0]=6
c=["korte",8]
c[0]="fa"
d={"alma":"apple","kutya":"dog"}
print(d["alma"])
print(d.keys())
print(d.values())
e=[1,2,3,4,4,4,3,3]
f=set(e)
print(f)
