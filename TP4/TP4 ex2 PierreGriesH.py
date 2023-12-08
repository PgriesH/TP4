# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants

notes = []
i = 0

somme = 0

for loop in range(nombreEtudiants):
    note = float(input("Entrez une note entre 0 et 20 : "))
    notes.append(note)
    somme = somme + note
for i in range(0, len(notes)):
    print('Note etudiant' ,i,  ':', notes[i])
    i = i + 1
print('Moyenne de classe : ',somme/nombreEtudiants)
moyenne = somme/nombreEtudiants


print("Numéro de l'étudiant | note | ecart a la moyenne")
for i in range(0 ,len(notes)):
    print(i, '|', notes[i], '|', moyenne - notes[i]) 
    
             
               




    
