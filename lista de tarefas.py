import json
import os
arquivo='tarefas.json'

def carregar():
    if not os.path.exists(arquivo) or os.stat(arquivo).st_size==0:
        return []
    with open(arquivo,'r',encoding='utf-8') as f:
        return json.load(f)
    
def salvar(tarefas):
    with open(arquivo,'w',encoding='utf-8') as f:
        json.dump(tarefas,f,indent=4,ensure_ascii=False)

def listar(tarefas):
    if not tarefas:
        print('\nNenhuma terefa encontrada.')
        return
    for i, tarefa in enumerate(tarefas, start=1):
        status='☑'  if tarefa['concluida'] else'☒'
        print(f'{i}. {status} {tarefa['descricao']}')
    
def adicionar(tarefas):
    descricao=input('Digite a descrição da tarefa:').strip()
    if descricao:
        tarefas.append({'descricao':descricao,'concluida':False})
        salvar(tarefas)
        print('Tarefa adicionada!')
    
def concluir(tarefas):
    listar(tarefas)
    try:
        i=int(input('Digite o número da tarefa concluída:'))-1
        if 0<=i<len(tarefas):
            tarefas[i]['concluida']=not tarefas[i]['concluida']
            salvar(tarefas)
            print('Status de tarefa salvo com sucesso!')
        else:
            print('Número inválido.')
    except ValueError:
        print('Entrada inválida. Digite um número.\n')
       

def remover(tarefas):
    listar(tarefas)
    try:
        num=int(input('Digite o número da tarefa a remover:'))
        if 1<=num<=len(tarefas):
            remocao=tarefas.pop(num-1)
            salvar(tarefas)
            print(f'Tarefa removida:{remocao['descricao']}\n')
        else:
            print('Número inválido.\n')
    except ValueError:
        print('Entrada inválida.\n')

def apagar_tudo(tarefas):
    confirmacao=input('Tem certeza que deseja apagar TODAS as tarefas? (s/n)')
    if confirmacao=='s':
        tarefas.clear()
        salvar(tarefas)
    else:
        print('Operação cancelada.')

def menu():
    tarefas=carregar()
    while True:
        print('------->LISTA DE TAREFAS<-------')
        print('1- Listar tarefas')
        print('2- Adicionar tarefa')
        print('3- Marcar como concluída')
        print('4- Remover tarefa')
        print('5- Remover TODAS as tarefas')
        print('0- Sair')
        opcao=int(input('Escolha uma opção:'))
        if opcao==1:
            listar(tarefas)
        elif opcao==2:
            adicionar(tarefas)
        elif opcao==3:
            concluir(tarefas)
        elif opcao==4:
            remover(tarefas)
        elif opcao==5:
            apagar_tudo(tarefas)
        elif opcao==0:
            print('Saindo...até mais')
            break
        else:
            print('Opção inválida. Digite novamente.')
            opcao=int(input('Escolha uma opção:'))

if __name__=='__main__':
    menu()