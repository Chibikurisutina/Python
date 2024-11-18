#O que está acontecendo?
#1. Mostra opções na tela;
#2. Pede digitação de opção e armazena valor da variável;
#3. Mostra opção escolhida;
#4. Função que finaliza o app se for escolhida opção 4;

import os #importar biblioteca de funcionalidades que são dependentes de sistema operacional

restaurantes = [{'nome':'DandanDan', 'categoria':'Italiana','ativo':False},
                {'nome':'Bebop','categoria':'Fusion','ativo':True},
                {'nome':'Nana Cafe','categoria':'Café','ativo':False}]

#Print mostra opções na tela
#\n é usado para quebra de linha
def exibir_nome_do_programa():
    print("""
    SABOR EXPRESS
    """)

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair \n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante: ')
    dados_do_restaurante = {'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    
    for restaurante in restaurantes:
       nome_restaurante = restaurante['nome']
       categoria = restaurante['categoria']
       ativo = restaurante['ativo']
       print(f'-{nome_restaurante} | {categoria} | {ativo}')
    voltar_ao_menu_principal()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app() #chamando a função
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()