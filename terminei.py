#1

negativos = 0

for i in range(5):
    n = float(input("Digite um número: "))
    if n < 0:
        negativos += 1

print("Quantidade de números negativos:", negativos)


#2

soma = 0
cont = 0

while True:
    n = float(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    soma += n
    cont += 1
    media = soma / cont
    print("Média até agora:", media)


#3

soma = 0
cont = 0

while True:
    op = input("Deseja digitar um número? (s/n): ").lower()
    if op == 'n':
        break
    n = float(input("Digite o número: "))
    if 15 <= n <= 73:
        soma += n
        conta += 1

if cont > 0:
    print("Média dos números entre 15 e 73:", soma / conta)
else:
    print("Nenhum número no intervalo informado.")


#4

chico = 1.50
ze = 1.10
anos = 0

while ze <= chico:
    chico += 0.02
    ze += 0.03
    anos += 1

print("Serão necessários", anos, "anos para Zé ser maior que Chico.")

#6

soma_salario = 0
soma_filhos = 0
qtd_pessoas = 0
maior_salario = 0
qtd_minimo = 0

while True:
    salario = float(input("Salário : R$ "))
    if salario < 0:
        break
    filhos = int(input("Quantidade de filhos: "))

    soma_salario += salario
    soma_filhos += filhos
    qtd_pessoas += 1

    if salario > maior_salario:
        maior_salario = salario
    if salario <= 1518:
        qtd_minimo += 1

if qtd_pessoas > 0:
    print("Média de salário:", soma_salario / qtd_pessoas)
    print("Média de filhos:", soma_filhos / qtd_pessoas)
    print("Maior salário:", maior_salario)
    print("Percentual com salário até R$1518:", (qtd_minimo / qtd_pessoas) * 100, "")
else:
    print("Nenhum dado informado.")


