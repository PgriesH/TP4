N = float(input("Vous cherchez la table de multiplication de quel nombre ?"))

i = 0



table = [N * 0, N * 1, N * 2, N * 3, N * 4 , N * 5, N * 6, N * 7, N * 8, N * 9]

for i in range (0 , len(table)):
        print(N ,'*', i ,'=' , round(table[i], 1))
        i = i + 1

        
