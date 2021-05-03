import math
from random import randint
#ex1
'''def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
 
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

N=11

if(isPrime(N)):print("Numarul este prim")

for i in range(2,N-1):
    if(isPrime(i) and isPrime(N/i) and math.floor(N/i)==N/i):
        print(i,math.floor(N/i))
        break '''

#ex2
N=21
r=0
while(True):
    x=randint(2,N-1)
    if(math.gcd(x,N)==1):
        for i in range(1,N-1):
            if(pow(x,i)%N==1):
                r=i
                break
        if(r%2==0):
            y=math.floor(pow(x,r/2)%N)
            if(0<y-1 and y-1<y+1 and y+1<N):
                print(math.gcd(y-1,N))
                print(math.gcd(y+1,N))
                break      





