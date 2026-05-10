#1

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))

if a > b:
    print("O maior valor é:", a)
else:
    print("O maior valor é:", b)

#2

ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = 2025
idade = ano_atual - ano_nasc

if idade >= 16:
    print("Você pode votar este ano.")
else:
    print("Você ainda não pode votar este ano.")


#3


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]
numeros.sort()

print("Números em ordem crescente:", numeros)


#45


lados = int(input("Digite o número de lados: "))
medida = float(input("Digite a medida do lado (em cm): "))

if lados < 3:
    print("NÃO É UM POLÍGONO")
elif lados == 3:
    area = (medida ** 2) * (3 ** 0.5) / 4
    print("TRIÂNGULO - Área:", (area, 2), "cm²")
elif lados == 4:
    area = medida ** 2
    print("QUADRADO - Área:",  (area, 2), "cm²")
elif lados == 5:
    print("PENTÁGONO")
else:
    print("POLÍGONO NÃO IDENTIFICADO")


#6
a1 = float(input("Digite o primeiro ângulo: "))
a2 = float(input("Digite o segundo ângulo: "))
a3 = float(input("Digite o terceiro ângulo: "))

if a1 == 90 or a2 == 90 or a3 == 90:
    print("Triângulo Retângulo")
elif a1 > 90 or a2 > 90 or a3 > 90:
    print("Triângulo Obtusângulo")
else:
    print("Triângulo Acutângulo")

#7

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)

print("As notas digitadas foram:", notas)


#8

notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Média:", (media, 2))

if media >= 60:
    print("Aprovado!")
else:
    print("Reprovado.")


#desafio manjado


produtos = {}

while True:
    print("=== MENU PRINCIPAL ===")
    print("1 - Cadastrar produtos")
    print("2 - Realizar compra")
    print("3 - Listar produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            nome = input("Digite o nome do produto (ou 'voltar' para sair): ").lower()
            if nome == "voltar":
                break
            preco = float(input("Digite o preço do produto: "))
            produtos[nome] = preco
            print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        if not produtos:
            print("Nenhum produto cadastrado ainda.")
        else:
            while True:
                compra = input("Digite o nome do produto que deseja comprar (ou 'finalizar' para sair): ").lower()
                if compra == "finalizar":
                    break
                if compra in produtos:
                    qtd = int(input("Quantidade: "))
                    total = produtos[compra] * qtd
                    print(f"{qtd}x {compra} - Total: R${total:.2f}")
                else:
                    print("Produto não encontrado!")

    elif opcao == "3":
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("=== PRODUTOS CADASTRADOS ===")
            for nome, preco in produtos.items():
                print(f"{nome.capitalize()} - R${preco:.2f}")

    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")