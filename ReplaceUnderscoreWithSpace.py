#!/usr/bin/python
import sys
def main( string ):
    liste = list(string) 
    first_index = FirstAndLastControl(liste)
    last_index = FirstAndLastControl(liste[::-1])
    character_control = "".join(liste[first_index:len(liste)-last_index]).replace("_"," ")

    for i in range(len(character_control)):
        liste[first_index+i] = character_control[i]

    print "".join(liste)

def Control(harf):
    
    if harf == "_":
        return False
    else:
        return True
        
def FirstAndLastControl(liste):
    
    state = Control(liste[0])
    
    for i in range(len(liste)):
        if liste[i] == "_" and state==False:
            pass
        elif liste[i] != "_" :
            return i
        
    
        
args = sys.argv[1:]

main(args[0])       
    
        
      
