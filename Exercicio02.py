peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura**2)

print("Seu IMC é {:.2f}".format(imc))

if imc < 16:
    print("Magreza Grave")
elif 16 <= imc < 17:
    print("Magreza Moderada")
elif 17 <= imc < 18.5:
    print("Magreza Leve")
elif 18.5 <= imc < 25:
    print("Saudável")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade Grau I")
elif 35 <= imc < 40:
    print("Obesidade Grau II")
else: 
    print("Obesidade Grau III")