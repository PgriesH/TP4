T = [5, 2, 4, 8, 1, 3]
i = 0

print(T)

for i in range(1, len(T)):
    val = T[i]
    pos = i
    while pos > 0 and T[pos - 1] > val:
        T[pos] = T[pos - 1]
        pos -= 1
    T[pos] = val
    print(T)
