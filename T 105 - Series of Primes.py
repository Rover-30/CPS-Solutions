n=int(input())
i=1
while(n!=0):
    i=i+1
    if(i==2):
        n=n-1
    else:
        def isPrime(n):
            for i in range(2,int(n**0.5)+1):
                if (n%i==0):
                    return False
        
            return True
   
        if(isPrime(i)):
            n=n-1
        
if(n==0):
    print(i)