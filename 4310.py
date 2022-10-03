def pascal():
    n = int(input())
    pt = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
           if j != 0 and j != i:
               row[j] = pt[i-1][j-1] + pt[i-1][j]
        pt.append(row)
    print(pt[n])


pascal()

