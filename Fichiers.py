#creer un fichier 
myfile = open("fichierText.txt", "w")
myfile.write(" maimouna \n diallo \n supdeco \n")
myfile.close()
             



def nbMotsAvecVoyelle(nomf):
  voyelles = ["a","o","i","u" ,"e"] 
  count = 0
   
try :
       with open(nomf, 'r') as fichier:
           for line in fichier:
               mot = line.strip().lower()
               if mot and mot[o] in voyelles:
                   count +=1
except FileNotFoundError :
       print("le fichier " , nomf , " n'a pas ete trouve ")   
return count                  
nomf = "fichierText.txt "
nbMotsAvecVoyelle(nomf)           