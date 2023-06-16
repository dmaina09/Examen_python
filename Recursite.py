# Fonction recursive de la fonction iterative divin (a,b)

a =int(input("donnez une valeur pour  a : "))
b =int(input("donnez une valeur pour  b : "))
def recursive_divin(a,b):
   
    if a < b: 
        return 0
    else : 
        return 1 + recursive_divin(a-b,b)
d = recursive_divin(a,b)
    
print(" la division de ", a ,"par",  b, "est :" , d)   
    
 #Fonction recursive qui prend deux parametres a un reel et b un entier et retourne une valeur reelle a!  
a=float(input("donner un reel a : " ))
b=int(input("donner un entier b : " ))
def factoriel(a, b):
    if b== 0:
        return 1.0
    else : return a * factoriel(a,b-1)
resultat = 8
factoriel(a,b)    
print("le factoriel de ",a, " par un entier ", b, " est : " ,resultat)   
    