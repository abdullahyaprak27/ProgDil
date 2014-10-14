#!/usr/bin/python
import random
class RandomName:
    def __init__(self,language="tr",again=1):
        
        self.language=language
        self.again=int(again)
        self.ValueControl(self.again)



    def ValueControl(self,count):
        i = 0
        while count > i:
            string=self.CreateName()
            flag1=self.check(string)

            if flag1==False:
                f1=open("storage.txt","a")
                f1.writelines(string+"\n")
                f1.close()
                print string
                i += 1
            else:
                pass
            
            
    def CreateName(self):
    
        names=["adem","veli","mahmut","hakan","orhan","fatih","cem","can"]
        adjectives=["iyi","guzel","hizli","yavas","yakisikli","mert","cimri","kel"]
        i= random.choice(adjectives)," ",random.choice(names)
        i = ( "".join(i))
        return i
    def check(self,string):
        flag=False
        f1=open("storage.txt","r")

        for j in f1:
            if j==(string+"\n"):
                flag= True
        f1.close()
        return flag


            
    
