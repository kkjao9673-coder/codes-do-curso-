# NUMBER 1
idade= int(input("Digite uma idade: "))

cursor.execute(f"SELECT * FROM usuário WHERE idade >= {idade}")
resultado= cursor.fetchall()
for linha in resultado:
    print (f"O {linha[1]} tem {linha[4]} anos, possui o CPF {linha[6]}, email {linha[2]} e a senha é {linha[3]}.-")

for registro in resultado:
    print(registro)

# ativandela 2

print('==========Senha==========\n')

reemail = input("Digite seu Email: \n")
resenha = input("Digite sua Senha: \n")

cursor.execute(f"SELECT * FROM usuario WHERE email = '{reemail}'")
res = cursor.fetchall()

if len(res) > 0:
    if resenha == res[0][3]:
        print('Acesso Concedido')
        cursor.execute(f"DELETE FROM usuario WHERE email = '{reemail}'")
        banco.commit()
    else:
        print('Acesso Negado')
else:
    print('Esse email não tem')