# -*-coding:Latin-1 -*

# Une ann�e est dite bissextile si elle est un multiple de 4,
# SAUF si elle est un multiple de 100.
# Toutefois, elle est bissextile si elle est un multiple de 400.

# Demander l'ann�e
annee = raw_input("Quelle ann�e veux-tu tester, cher utilisateur ?\n")
# Convertir la chaine en integer
annee = int(annee)
# La variable du r�sultat
bissextile = (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0


# Afficher le r�sultat
if bissextile:
    print(str(annee) + " est bissextile !")
else:
    print("Pas d'bol, " + str(annee) + " n'est pas bissextile !")
