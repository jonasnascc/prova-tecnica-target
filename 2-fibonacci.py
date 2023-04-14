n = int(input("Informe um número: "))

if(n==0 or n==1):
    print("   O número inserido pertence à sequência Fibonacci")

    
else:
    atual = 1
    prev = 0

    fib = 1
    i=0
    while(fib <= n):
        fib = atual + prev

        if(fib == n):
            print("   O número inserido pertence à sequência Fibonacci")
            break
        elif(fib > n):
            print("   O número inserido NÃO pertence à sequência Fibonacci")
            break
        
        prev = atual
        atual = fib
          
        i+=1

