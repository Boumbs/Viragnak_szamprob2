class TBinfa:
    def __init__(self):
        self.gyoker=None
    def Ures(self):
        self.gyoker=None
    def Ures_e(self):
        return self.gyoker==None
    def Egyelemufa(self,ertek):
        self.gyoker=ertek
        self.balfa=None
        self.jobbfa=None
    def Balrailleszt(self,bfa):
        self.balfa=bfa
    def Jobbrailleszt(self,jfa):
        self.jobbfa=jfa
    def Balgyerek(self):
        return self.balfa
    def Jobbgyerek(self):
        return self.jobbfa
    def Gyokerelem(self):
        return self.gyoker
    def Gyokermodosit(self,ertek):
        self.gyoker=ertek
    def KBJ(self):
        if not self.Ures_e():
            print(self.Gyokerelem())
            if self.Balgyerek()!=None:
                self.Balgyerek().KBJ()
            if self.Jobbgyerek()!=None:
                self.Jobbgyerek().KBJ()
    def BKJ(self):
        if not self.Ures_e():
            if self.Balgyerek()!=None:
                self.Balgyerek().BKJ()
            print(self.Gyokerelem())
            if self.Jobbgyerek()!=None:
                self.Jobbgyerek().BKJ()
    def Level(self):
        return self.balfa==None and self.jobbfa==None
    def Levelszam(self):
        if self==None:
            return 0
        else:
            if self.gyoker==None:
                return 0
            else:
                if self.Level():
                    return 1
                else:
                    if not self.Balgyerek().Ures_e() and not self.Jobbgyerek().Ures_e():
                        return self.Balgyerek().Levelszam()+self.Jobbgyerek().Levelszam()
                    else:
                        if not self.Balgyerek().Ures_e():
                            return self.Balgyerek().Levelszam()
                        else:
                            return self.Jobbgyerek().Levelszam()
    def Fafelepites(self,elemek):
        for elem in elemek:
            self.BeszurElem(elem)
    def BeszurElem(self,elem):    
        if self.gyoker==None:
            self.Egyelemufa(elem)
            
        else:
            
            if elem<self.gyoker:
                if self.balfa==None:
                    self.balfa=TBinfa()
                    #self.balfa.Egyelemufa(elem)                
                self.balfa.BeszurElem(elem)
            else:
                if self.jobbfa==None:
                    self.jobbfa=TBinfa()
                self.jobbfa.BeszurElem(elem)

    def Kereses(self,mit):
        if self.gyoker==None:
            return False
        else:
            if self.gyoker==mit:
                return True
            else:
                if self.gyoker>mit:
                    if self.balfa==None:
                        return False
                    return self.balfa.Kereses(mit)
                else:
                    if self.jobbfa==None:
                        return False
                    return self.jobbfa.Kereses(mit)

    def Beszurhelyre(self,hova,melyiket,A):
        if self!=None:
            if self.gyoker==hova:
                if A=="A":
                    if self.balfa==None:
                        self.balfa=TBinfa()
                        self.balfa.Egyelemufa(melyiket)
                else:
                    if self.jobbfa==None:
                        self.jobbfa=TBinfa()
                        self.jobbfa.Egyelemufa(melyiket)
            else:
                if self.balfa!=None:
                    self.balfa.Beszurhelyre(hova,melyiket,A)
                if self.jobbfa!=None:
                    self.jobbfa.Beszurhelyre(hova,melyiket,A)

    def afel(self):
        if self!=None:
            if self.balfa==None and self.jobbfa==None:
                return 2
            else:
                if self.balfa!=None and self.jobbfa!=None:
                    return 0
                else:
                    return 1

tarsasag=TBinfa()
tarsasag.Egyelemufa(1)
N=int(input())
for i in range(2,2+N):
    adat=input().split()
    tarsasag.Beszurhelyre(int(adat[0]),i,adat[1])
tarsasag.BKJ()
print(tarsasag.afel())

#----------------------------------------------------------------
#binfa=TBinfa()
##binfa.Egyelemufa(5)
#elemek=[6,1,5,3,4,8,7,9]
#binfa.Fafelepites(elemek)
#binfa.BKJ()
#if binfa.Kereses(7):
#    print("Van")
#else:
#    print("nincs")

#if binfa.Ures_e():
#    print("ures")
#else:
#    print("nem ures")
#binfa.Egyelemufa(7)
#if binfa.Ures_e():
#    print("ures")
#else:
#    print("nem ures")
#bfa=TBinfa()
#bfa.Egyelemufa(5)
#bbfa=TBinfa()
#bbfa.Egyelemufa(3)
#bfa.Balrailleszt(bbfa)
#bjfa=TBinfa()
#bjfa.Egyelemufa(6)
#bfa.Jobbrailleszt(bjfa)

#jfa=TBinfa()
#jfa.Egyelemufa(9)
#jbfa=TBinfa()
#jbfa.Egyelemufa(8)
#jjfa=TBinfa()
#jjfa.Egyelemufa(10)
#if jjfa.Level():
#    print("Level")
#else:
#    print("nem level")
#jfa.Balrailleszt(jbfa)
#jfa.Jobbrailleszt(jjfa)
#if jfa.Level():
#    print("Level")
#else:
#    print("nem level")
#binfa.Balrailleszt(bfa)
#binfa.Jobbrailleszt(jfa)

##binfa.KBJ()
##bfa2=binfa.Balgyerek()
##print(bfa2.Gyokerelem())
##jfa2=binfa.Jobbgyerek()
##print(jfa2.Gyokerelem())
#binfa.BKJ()
#print(binfa.Levelszam())