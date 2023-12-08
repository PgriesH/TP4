L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]




def element_plus_frequent(liste):
    # Initialiser un dictionnaire pour stocker les fréquences
    frequences = {}
    
    # Parcourir la liste et mettre à jour les fréquences
    for element in liste:
        if element in frequences:
            frequences[element] += 1
        else:
            frequences[element] = 1
    
    # Trouver l'élément le plus fréquent et sa fréquence
    max_frequence = 0
    element_max_frequence = None
    for element, frequence in frequences.items():
        if frequence > max_frequence:
            max_frequence = frequence
            element_max_frequence = element
    
    return element_max_frequence, max_frequence

# Exemple d'utilisation
element, frequence = element_plus_frequent(L1)
print(f"L'élément le plus fréquent est le {element} et sa fréquence d'apparition est {frequence}.")






""" ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
* Ne rien modifier apres cette ligne.
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** * /
"""
