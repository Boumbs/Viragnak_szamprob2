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

binfa=TBinfa()
if binfa.Ures_e():
    print("ures")
else:
    print("nem ures")
binfa.Egyelemufa(7)
if binfa.Ures_e():
    print("ures")
else:
    print("nem ures")
bfa=TBinfa()
bfa.Egyelemufa(5)
bbfa=TBinfa()
bbfa.Egyelemufa(3)
bfa.Balrailleszt(bbfa)
bjfa=TBinfa()
bjfa.Egyelemufa(6)
bfa.Jobbrailleszt(bjfa)

jfa=TBinfa()
jfa.Egyelemufa(9)
jbfa=TBinfa()
jbfa.Egyelemufa(8)
jjfa=TBinfa()
jjfa.Egyelemufa(10)
if jjfa.Level():
    print("Level")
else:
    print("nem level")
jfa.Balrailleszt(jbfa)
jfa.Jobbrailleszt(jjfa)
if jfa.Level():
    print("Level")
else:
    print("nem level")
binfa.Balrailleszt(bfa)
binfa.Jobbrailleszt(jfa)

#binfa.KBJ()
#bfa2=binfa.Balgyerek()
#print(bfa2.Gyokerelem())
#jfa2=binfa.Jobbgyerek()
#print(jfa2.Gyokerelem())
binfa.BKJ()
print(binfa.Levelszam())