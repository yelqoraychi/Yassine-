a=15
b=4
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}//{b}={a//b}")
print(f"{a}%{b}={a%b}")
print(f"{a}**{b}={a**b}")

x=20
y=15
print(x==y)
print(x!=y)
print(x<y)
print(x>=y)
try:
  prix_initial=float(input("prix du produit:"))
except ValueError:
  print("saisie invalid pour le prix .")
  exit(1)
statut=input("Etes-vous étudiant(o\n)").strip().lower()
fidelite=input("fidelité en années").strip()

try:
  fidelite=int(fidelite)
except ValueError:
  print("il faut tapez des entiers pour les années")
  exit(1)

reduction=0.0
if statut=="o":
  reduction=reduction + prix_initial*0.1
if fidelite>=5:
  reduction=reduction + prix_initial*0.15
if prix_initial>100:
  reduction+=5.0
prix_finale=prix_initial-reduction
if prix_finale<0:
  prix_finale=0.0
print(f"Reduction totale:{reduction:.2f}")
print("Prix finale est :",prix_finale)
