def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            # print(f"({a} * {x}) % {m}")
            return x 
    return 1

  
# Driver Program 
for a in range(0,90):
    k = modInverse(a, 91)
    if k != 0 and k != 1: 
        print(a)

print("____________________________________________________________")

for a in range(0,90):
    k = modInverse(a, 91)
    if k != 0 and k != 1: 
        print(k)

