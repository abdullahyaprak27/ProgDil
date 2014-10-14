#!/usr/bin/python
import random
class RandomName:
    def __init__( self,language = "tr",again = 1):
        
        self.language = language
        self.again = int(again)
        self.ValueControl(self.again)



    def ValueControl(self,count):
        i = 0
        while count > i:
            string=self.CreateName(self.language)
            flag1=self.check(string)

            if flag1 == False:
                f1=open("storage.txt", "a")
                f1.writelines(string+"\n")
                f1.close()
                print string
                i += 1
            else:
                pass
            
            
    def CreateName(self,language):
    
        isim=["kedi","insan","deniz","masa","dolap","bilgisayar","kapi","pencere","hafta","gece","gunduz","marti","kazak",
	"sarisin","sahil","merdiven","ahmet","yol","araba","agac","yaprak","dal","adam","konuk","ahmet","koca","kadin"]
        sifat=["iyi","guzel","hizli","yavas","yakisikli","mert","cimri","kel","masmavi","ucan","kac","yarim","bu","su"]

        names = ["baby","child","man","main","house","sea","car","computer","pencil","pen","doctor","window","line"]
        adjectives = ["good","beatiful","long","small","nice","micke","bad","slow","green","blue","hard"]

        sozluk = {"tr":{"adjectives":sifat , "names":isim} , "en":{"adjectives":adjectives , "names":names}}
        
        i= random.choice(sozluk[language]["adjectives"])," ", random.choice(sozluk[language]["names"])
        i = ( "".join(i))
        return i
    def check(self,string):
        flag = False
        f1=open("storage.txt","r")

        for j in f1:
            if j == (string+"\n"):
                flag = True
        f1.close()
        return flag


            
    
