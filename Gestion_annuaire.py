#1ere partie 
#declaration du tableau 
Annulaire = []
#Definition de la fonction de saisie 
def saisie_tab(nom,prenom,numero_rue,nom_rue,numero_telephone,code_postal,ville):
    nom = str(input("veuillez saisir votre nom :"))
    prenom = str(input("Veuillez saisir votre prenom :"))
    numero_rue = int(input("Veuillez indiquer le numero de rue :"))
    nom_rue = str(input("Veuillez indiquer le nom de la rue : ")) 
    numero_telephone = int(input("Veuillez saisir votre numero de telephone : "))
    code_postal = int(input("Veuillez saisir votre code postal : "))
    ville = str(input("Veuillez saisir le nom de votre ville : "))
    Annulaire = [nom,prenom,numero_rue,nom_rue ,numero_telephone,code_postal,ville]
    return Annulaire

#definition de la fonction critere de recherche 
def critere_recherche():
    choix = input("veuillez entrer votre choix : "  )
    return choix 
 
 #definition de la fonction de recherche 
def Recherche(Annulaire, critere_recherche):
     taille = len(Annulaire)
     resultat = [False] * taille
     for i in range(taille):
         if Annulaire[i] == critere_recherche:
             resultat[i] = True         
     return resultat 
 
 #procedure d'affichage d'un tableau 
def affiche_tab(Annulaire,resultat):
     taille = len(Annulaire)
     for i in range(taille):
         if resultat [i] :
             print(Annulaire[i], end="")
         else:
             print("null", end=" ")
     return resultat            
    
  
  
  #Programme principale   
print("les informations renseignees sont : " , saisie_tab(nom=any,prenom=any,numero_rue=any,
        nom_rue=any, numero_telephone=any  ,code_postal = any,ville = any))
print("Votre choix est : ", critere_recherche())
resultat_recherche = Recherche(Annulaire, critere_recherche)
print("le ressultat de la recherche est : ", resultat_recherche)
print("Affichage : " ,affiche_tab(Annulaire=[],resultat=[]))