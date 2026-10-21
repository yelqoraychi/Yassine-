notes=[12,9,15,8,17,13,19,10]
total=0
seuil=12
nb_notes=len(notes)
for note in notes:
    total +=note
moyenne=total/nb_notes
print(f"Moyenne:{moyenne:.2f}")
notes_bonus=[min(note +1,20) for note in notes]
print("Notes aprés bonus:",notes_bonus)
notes_valides=[note for note in notes if note>=12]
print(f"Notes>=12:",notes_valides)
moyenne_initiale = sum(notes) / nb_notes
moyenne_bonus = sum(notes_bonus) / len(notes_bonus)
lignes = []
lignes.append("=== Rapport des notes ===")
lignes.append(f"Nombre d'étudiants : {nb_notes}")
lignes.append(f"Notes originales : {notes}")
lignes.append(f"Notes après bonus : {notes_bonus}")
lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
lignes.append("Détails par étudiant :")
for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1]
    lignes.append(f"  Étudiant {index:02d} — note {note:>5.2f} → bonus {bonus:>5.2f}")
rapport = "\n".join(lignes)
print(rapport)