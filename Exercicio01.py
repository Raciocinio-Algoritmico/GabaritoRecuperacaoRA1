nome = str(input("Nome: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

ano_atual = 2022

if ano_atual - ano >= 18:
    print("{} está apto para iniciar a auto escola.".format(nome))
elif ano_atual - ano == 17 and mes < 6:
    print("{} fez 18 anos antes de junho, então está apto para iniciar a auto escola.".format(nome))
else:
    print("{} ainda não completou 18 anos, então não poderá inciar as aulas da auto escola.".format(nome)) 