import os

lista_alunos = []

def exibir_nome_do_programa():
    '''Exibe o nome do programa'''
    print('''
╭━━━┳╮╱╱╱╱╱╱╭━╮╱╭╮╱╱╭╮
┃╭━╮┃┃╱╱╱╱╱╱┃┃╰╮┃┃╱╭╯╰╮
┃┃╱┃┃┃╭╮╭┳╮╭┫╭╮╰╯┣━┻╮╭╯
┃╰━╯┃┃┃┃┃┃╰╯┃┃╰╮┃┃┃━┫┃
┃╭━╮┃╰┫╰╯┃┃┃┃┃╱┃┃┃┃━┫╰╮
╰╯╱╰┻━┻━━┻┻┻┻╯╱╰━┻━━┻━╯\n''')

def mensagem_opcoes():
    '''Exibe a mensagem de opcoes do usuario'''
    print('''1 - Cadastrar aluno
2 - Listar todos os alunos
3 - Calcular a media de um aluno
4 - Sair''')

def voltar_ao_menu():
    '''Volta ao menu inicial'''
    input('\nDigite qualquer tecla para voltar ao menu: ')
    main()

def cadastrar_aluno():
    '''Recebe nome e data de um aluno e adiciona na lista de alunos
    
    inputs:
    - nome do aluno
    - quantidade de notas que deseja cadastrar
    - respectivas notas
    
    outputs:
    - adiciona nome e nota no dicionario
    - exibe mensagem de cadastro com sucesso
    '''
    nome = input('Digite o nome do aluno: ')
    notas_lista = []
    notas = int(input(f'Quantas notas deseja adicionar para {nome}? '))
    for i in range(notas):
        nota = float(input(f'Adicione a {i + 1} nota: '))
        notas_lista.append(nota)
    lista_alunos.append({'nome': nome, 'notas': notas_lista, 'media': ''})
    print(f'\nAluno {nome} cadastrado com sucesso!')
    voltar_ao_menu()

def listar_alunos():
    '''Percorre cada aluno da lista e pega seu nome'''
    for aluno in lista_alunos:
        nome_aluno = aluno['nome']
        print(nome_aluno)
    voltar_ao_menu()

def calcular_media():
    aluno_media = input('De qual aluno você deseja calcular a média? ')
    for aluno in lista_alunos:
        if aluno['nome'] == aluno_media:
            notas = aluno['notas']
            media = sum(notas) / len(notas)
            aluno['media'] = media
            print(f'\nA média de {aluno_media} é {media}')
            break
        else:
                print('Aluno não encontrado no nosso banco de dados!')
    voltar_ao_menu()

def finalizar_app():
    '''Limpa o terminal e finaliza o programa'''
    os.system('cls')
    print('Finalizando o programa...')

def opcao_invalida():
    '''Mensagem de erro para opcoes invalidas/erro'''
    print('Parece que você escolheu uma opção inválida, tente novamente!')
    voltar_ao_menu()

def opcao_usuario():
    '''Trata as opcoes do usuario, mandando para suas respectivas funcoes'''
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_aluno()
            case 2:
                listar_alunos()
            case 3:
                calcular_media()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Todas as funcoes que devem ser executadas ao iniciar o programa'''
    exibir_nome_do_programa()
    mensagem_opcoes()
    opcao_usuario()

if __name__ == '__main__':
    main()