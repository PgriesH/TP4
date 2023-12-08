nMax = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))

v1 = []
v2 = []
pscalaire = 0
i = 0

print("Saisie du 1er vecteur :")

for i in range(0, nMax):

    v1.append(int(input('v1[' + str(i) + ']=')))

print("Saisie du second vecteur :")

for i in range(0, nMax):

    v2.append(int(input('v2[' + str(i) + ']=')))

for i in range(0, nMax): pscalaire = pscalaire + v1[i] * v2[i]

print(pscalaire)
