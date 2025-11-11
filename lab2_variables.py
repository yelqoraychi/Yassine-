entier=42
flottant=3.14
texte="python"
vrai_ou_faux=True
print(entier,"==>",type(entier))
print(flottant,"==>",type(flottant))
print(texte,"==>",type(texte))
print(vrai_ou_faux,"==>",type(vrai_ou_faux))
print(id(entier))
nombre=5
print(id(nombre))
nombre=5+12
print(id(nombre))  
print(isinstance(5,int))

print(bool("False"))

a=float(input("donner le nombre 1:"))
b=float(input("donner le nombre 2:"))
print("choisir un de ses opérations:* + - /")
print("1 pour addition")
print("2 pour soutraction")
print("3 pour multiplication")
print("4 pour division")
choix=int(input("votre choix est:"))
if choix== 1:
    print(a+b)
elif choix== 2 :
    print(a-b)
elif choix==4:
    if b== 0 :
        print("division impossible")
    else :
     print(a/b)
elif choix==3:
   print(a*b)
else:
   print("s'il vous plait entrer 1 ou 2 ou3 ou 4")
