list = []

for i in range(10):
    n = int(input("Digite um número: "))
    list.append(n)

pares = 0
impares = 0

for num in list:
    if num % 2 == 0:
        pares += 1
    else:    
        impares += 1

print("A. Pares: {}".format(pares))
print("B. Impares: {}".format(impares))
print("C. Maior Número:  {}".format(max(list)))
print("D. Menor Número: {}".format(min(list)))