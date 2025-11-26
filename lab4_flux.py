seuil=10
try:
    note=float(input("Entrer la note de l'étudiant:"))
except  ValueError:


    print("Saisie invalide")

    exit(1) 
if note>=seuil:
    print("admis")
else:
    print("Refudé")

#ETAPE 2
mot_cle="stop"
message=""
while message.lower()!=mot_cle:
    message=input("Taper un message ou stop pour quitter:")
    if message.lower()!=mot_cle:
        print("Vous avez saisie ",message)
print("Boucle terminer,mot clé détecté")
#etape3
for i in range(1,6):
    print(i)
#ETAPE 4    
fruits=["pomme",'banane',"cerise"]
for index,fruit in enumerate(fruits):
    print(index ,"==>",fruit)
#ETAPE 5
seuil=10
notes=[]
compteur=1
while compteur<=10:
    entree=input("Entrer une note ou stop").strip()
    if entree.lower()=="stop":
        break
    try:
        note=float(entree)
        notes.append(note)
        compteur+=1
        
        
    except ValueError:
        print("Valeur incorrecte,merci de saisir un nombre.")
for index,note in enumerate(notes,start=1):
    status="admis" if note>=seuil else "refusé"
    print(f"ETUDIANT:{index} : note{note}==>{status}")
somme=0
for i,n in enumerate (notes,start=1):
    somme=somme+n
print(f"le moyenne de classe de {len(notes)} etudiants est :{somme/len(notes)}")