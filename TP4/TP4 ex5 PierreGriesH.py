
date = input("Entrez une date sous la forme jjmmaaaa: ")

if len(date) != 8:
    print("incorrecte")
else:
    
    jour = int(date[:2])
    mois = int(date[2:4])
    annee = int(date[4:])

    jours_par_mois = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        
        jours_par_mois[2] = 29

    if mois < 1 or mois > 12:
        print("incorrecte")
    else:
        if jour < 1 or jour > jours_par_mois[mois]:
            print("incorrecte")
        else:
            print("correcte")
