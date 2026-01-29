import random
n=1000
l = [random.randint(1,1000) for _ in range(n)]
for i in range (n):
    for j in range (n-i-1):
        if(l[j]>l[j+1]):
            l[j+1],l[i]=l[i],l[j+1]

print(l)

    
           