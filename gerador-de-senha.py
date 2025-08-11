import random
import string

def gerar_completa(tamanho):
    caracteres=string.ascii_letters+string.digits+string.punctuation
    senha=''.join(random.choice(caracteres)for _ in range(tamanho))
    return senha

def apenas_letras(tamanho):
    caracteres=string.ascii_letters
    senha=''.join(random.choice(caracteres)for _  in range(tamanho))
    return senha

def apenas_numeros(tamanho):
    caracteres=string.digits
    senha=''.join(random.choice(caracteres)for _ in range(tamanho))
    return senha

def numeros_letras(tamanho):
    caracteres=string.digits+string.ascii_letters
    senha=''.join(random.choice(caracteres)for _ in range(tamanho))
    return senha

def escolher_tamanho():
    while True:
        try:
            return int(input('Digite o tamanho da senha:'))
        except ValueError:
            print('Digite um número válido para a senha.')


try:
    tamanho=int(input("Digite o tamanho da senha:"))
    while True:
        print('------> Gerador de Senhas Aleatórias <------')
        print('1- Senha com números, letras e símbolos especiais.')
        print('2- Senha com apenas letras.')
        print('3- Senha com apenas números.')
        print('4- Senha com letras e números.')
        opcao=int(input('Escolha uma opção de senha:'))
        if opcao==1:
            print('Sua senha gerada foi:',gerar_completa(tamanho))
        elif opcao==2:
            print('Sua senha gerada foi:',apenas_letras(tamanho))
        elif opcao==3:
            print('Sua senha gerada foi:',apenas_numeros(tamanho))
        elif opcao==4:
            print('Sua senha gerada foi:',numeros_letras(tamanho))
        else:
            print('Opção inválida. Escolha novamente.')
            opcao=int(input('Escolha uma opção de senha:'))

        mudar=input('Quer mudar o tamanho da senha? (s/n)').lower()
        if mudar=='s':
            tamanho=escolher_tamanho()
        elif mudar=='n':
            print(f'Tamanho de senha mantido em {tamanho} caracteres.')


except ValueError:
    print('Digite um número válido de tamanho de senha.')


