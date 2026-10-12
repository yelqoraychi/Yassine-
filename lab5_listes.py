def afficher_classe(classe):
    if not classe:
        print("La classe est vide")
        return
    for index,(nom,age,note) in enumerate(classe,start=1):
        print(f"{index}.{nom}-{age} ans -note{note}")
              
def ajouter_etudiant(classe):
    nom=input("Nom:").strip()
    try:
        age=int(input("Age:"))
        note=float(input("Note:"))
    except ValueError:
        print("Saisie invalide")
        return
    classe.append([nom,age,note])
    print(f"{nom} ajouté.")
def supprimer_etudiant(classe):
    if not classe:
        print("Rien a supprimer")
        return
    try:
        index=int(input("Numéro de l'etudiant:"))
        etudiant=classe.pop(index)
        print(f"{etudiant[0]} supprimé")
    except (ValueError,IndexError):
        print("sasie invalide")

def mettre_a_jour_etudiant(classe):
    if not classe:
        print("Rien à modifier")
        return
    try:
        index=int(input("Numéro de l'etudiant:"))
        etudiant=classe[index]
    except (ValueError,IndexError):
        print("Numero invalide")
        return
    nouveau_nom=input("Nouveau nom:").strip()
    if nouveau_nom:
        etudiant[0]=nouveau_nom
  
    nouveau_age=int(input("Nouveau age:"))
    if nouveau_age:
        etudiant[1]=nouveau_age
  
    nouveau_note=float(input("Nouveau note:"))
    if nouveau_note:
        etudiant[2]=nouveau_note
def afficher_statistique(classe):
    if not classe:
        print("Pas de données")
        return
    notes=[etudiant[2] for etudiant in classe]
    moyenne=sum(notes)/len(notes)
    meilleure=max(classe,key=lambda e:e[2])
    pire=min(classe,key=lambda e:e[2])
    print(f"Moyenne des notes:{moyenne:.2f}")
    print(f"Meilleure note:{meilleure[2]}")
    print(f"Min  note:{pire[2]}")
classe=[["Alice",20,15.5],["Bob",19,12.0],["Charlie",22,16.0]]
while True:
    print("\n Gestion de la classe")
    print("1.Afficher tous les étudiants")
    print("2.Ajouter un étudiant")
    print("3.Supprimer un étudiant")
    print("4.Modifier un étudiant")
    print("5.Statistiques")
    print("q.Quitter")
    choix=input("Choix:").strip().lower()
    if choix=="1":
        afficher_classe(classe)
    elif choix=="2":
        ajouter_etudiant(classe)
    elif choix=="3":
        supprimer_etudiant(classe)
    elif choix=="4":
        mettre_a_jour_etudiant(classe)
    elif choix=="5":
       afficher_statistique(classe)
    elif choix=="q":
        print("Au revoir")
        break
    else:
        print("Option inconnue")