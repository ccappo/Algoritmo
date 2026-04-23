# Dado los valores de n y m, imprimir
# de cuantas formas se pueden agrupar n objetos 
# en grupos de m (combinación de n tomados de a m)

def fact (n) -> int :
    fn = 1
    for k in range(1,n+1):
        fn *= k
    return fn

# programa principal

n = int(input('N:'))
m = int(input('M:'))

comb = fact(n)//(fact(m)*fact(n-m))

print(f'Combinación ({n},{m})= es {comb}')