n = int(input("Enter n: "))
k = int(input("Enter k: "))

C = [[0 for j in range(k+1)] for i in range(n+1)]

for i in range(n+1):
    for j in range(min(i, k)+1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i-1][j-1] + C[i-1][j]

print("Binomial Coefficient:", C[n][k])


#INPUT
#Enter n: 5
#Enter k: 2
#C(n,k)=C(n-1,k-1)+C(n-1,k)
