#coding: utf-8

#Potencia
potencia = lambda x: x**2;
print(potencia(5))

#Fatoriaç
def fat (n):
    if(n == 0):
        return 1
    return (n * fat(n-1))    
print(fat(5))

fatLambda = lambda n: n*fat(n-1) if n > 1 else 1
print(fatLambda(5))       

# Map - Aplicar uma função em vários itens

lista = [1,2,3]
m = map(lambda x: x**2, lista)
print("Map")
for i in m:
    print(i)
    
# Reduce - Aplica uma função que se vai acumulando
print("Reduce")
print(reduce(lambda x,y: x+y, lista))

#Filter - Filtra uma determinada condição
f = filter(lambda x: x%2 == 0, range(10))
print("Filter:")
for i in f:
    print(i)

print("Foi no baile, que ela lançou!! 14:07");
mar oi