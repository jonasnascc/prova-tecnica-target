string = "0987654321"

invertida = ""

n = len(string)
for i in range(n-1, -1 ,-1):
    invertida+=string[i]

print(invertida)

