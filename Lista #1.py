 #Exercicio 1

metros = int(input("Digite um valor em metros: "))
milimetros = metros*1000
print(f"Em metros: {metros} em milimetros: {milimetros}")

Exercicio 2
dias=int(input("Quantos dias você ja viveu? "))
horas=int(input("Quantos horas você ja viveu? "))
minutos=int(input("Quantos minutos você ja viveu? "))
segundos=int(input("Quartos segundos você ja viveu? "))
print(f'A sua vida inteira em segundos foi de: {(dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos}')

#Exercicio 3

valor = int(input("Digite o valor do seu salario: "))
aumento = int(input("Digite o valor do aumento: "))
salario = valor + (valor/100)*aumento
print((f"O valor do seu salario era de:{valor} e com o aumento de {aumento} foi para R${salario}"))

#Exercicio 4

preco = float(input("Digite o preço da mercadoria: "))
desconto = int(input("Digite o percentual do desconto: "))
precofinal = preco - (preco/100)*desconto
print(f"O valor da mercadoria com o desconto foi de: R${precofinal}")

#Exercicio 5

distancia = int(input("Digite a distancia que vai ser percorrida: "))
velocidademedia = int(input("Digite a velocidade media: "))
tempo = distancia/velocidademedia
print(tempo)

#Exercicio 6

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
soma = numero1 + numero2
while soma !=50:
    soma +=1
    print(soma)
print(soma)

#Exercicio 7

soma = 0
while soma != 100:
    soma += 1
    print(soma)

Exercicio 8
n = int(input("Digite um limite: "))
soma = 0
while soma != n:
    soma += 1
    print(soma)

#Exercicio 9
lista = []

while len(lista) < 5 :
    n = str(input("Digite um funcionario: "))
    lista.append(n)
print(lista[0])

#Exercicio 10

resposta = "sim"
while resposta == "sim":
    numero1=int(input('Digite um número: '))
    numero2=int(input('Digite outro número: '))
    print(f"{numero1} + {numero2} = {numero1 + numero2}")
    resposta = str(input("Deseja continuar? (s/n)"))
    if resposta == "sim":
        continue
    else:
        break


#Exercicio 12

lista = []
n = str()
while n != "0":
    n = str(input("Digite um funcionario: "))
    if n!="0":
        lista.append(n)
    else: break
print(lista)

#Exercicio 13

sexo = input("Qual o seu genero? ")
while sexo not in ("F", "M"):
    sexo = input("Digite novamente por favor! ")
if sexo == "F":
    sexo.lower()
    print("Parabéns, seu genero é feminino!")
if sexo == "M":
    sexo.lower()
    print("Parabéns, seu genero é masculino!")








