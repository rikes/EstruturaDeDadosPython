#Fatorial

def fatorial(n):
    if(n == 1):
        return 1
    return n * fatorial(n-1)
print(fatorial(3))

#Fibonacci 1,1,2,3,5,8,13
def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))

#Fibonacci sem recursividade
def fib(n):
    if (n == 1 or n == 2):
        return 1
    p1 = 1
    p2 = 1 
    
    for i in range(2,n):
        x = p1 + p2
        p1 = p2
        p2 = x                   
    return x
print(fib(7))        


#Potencia
def potencia(base, expoente):
    if(expoente == 0):
        return 1
    return base * potencia(base,expoente-1)
    
print(potencia(2,1))    

#Potencia sem Recursividade
def pot(base, expoente):
    if(expoente == 0):
        return 1 
    x = 1
    for i in range(1,expoente+1):        
        x = base * x
    return x
             
print(pot(2,10))                


print("Corrigido às 14:06")
print("Ok");
Cacete!!
