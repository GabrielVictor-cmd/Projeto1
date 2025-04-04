import os
restaurantes = [{"nome": "Temperaria Salgada", "categoria": "Salgada", "ativo": False},
                {"nome": "Tempero Mexicano", "categoria": "Picante", "ativo": True},
                {"nome": "Sushi Mano", "categoria": "Sushi", "ativo": False}
                ]

def exibir_nome_do_programa():
    ''''Exibe o nome do programa'''
    
    print("Salgado Tempero\n")

def exibir_opçoes():
    ''''Exibe as opções'''

    print("1- Cadastrar restaurante")
    print("2- Listar Restaurante")
    print("3- Alternar estado do restaurante")
    print("4- Sair\n")

def Encerrando_programa():
    ''''Encerra o programa'''

    os.system("cls")
    print("Encerrando programa...")
    exibir_subtitulo("Encerrando o programa")

def voltar_menu_principal():
    ''''Volta para o menu principal'''

    input("\nDigite ENTER para valtar para o menu principal")
    main()

def opçao_invalida():
    ''''Mostra quando é digitado uma opção inválida'''

    print("Opção inválida!")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    ''''Exibe subtitulos'''

    os.system("cls")
    linha = "=" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''''Cadastra um novo restaurante'''

    os.system("cls")
    print("Cadastro de novos restaurantes")
    exibir_subtitulo("Cadastro de novos restaurantes")

    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante que deseja cadastrar: ")
    dados_do_restaurante = {"nome": nome_restaurante, "categoria": categoria, "ativo": False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")

    voltar_menu_principal()

def listar_restaurantes():
    ''''Exibe uma lista de restaurantes'''

    exibir_subtitulo("Listanto restaurantes: ")

    for restaurante in restaurantes:
        nome_restaurantes = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f" - {nome_restaurantes.ljust(20)} | {categoria.ljust(20)} | {ativo}")
        
    input("Digite ENTER para voltar ao menu principal")
    main()

def alterar_estado_restaurante():
    ''''Altera o estado de atividade do restaurante'''

    exibir_subtitulo("Alterando")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante ["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)

    if not restaurante_encontrado:
        print("O Restaurante não foi encontrado")

    voltar_menu_principal()

def escolher_opçao():
    ''''Para o usuário escolher uma das opções'''

    try:
        opçao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção: {opçao_escolhida}\n")

        if opçao_escolhida == 1:
            cadastrar_novo_restaurante()
        
        elif opçao_escolhida == 2:
            listar_restaurantes()
        
        elif opçao_escolhida == 3:
            alterar_estado_restaurante()

        elif opçao_escolhida == 4:
            Encerrando_programa()

        else:
            opçao_invalida()

    except:
        opçao_invalida()

def main():
    '''Deixa o programa aberto até o usuário determinar que deseja encerrar'''

    os.system("cls")
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opçao()

if __name__ == "__main__":
    ''''Como eu disse acima, mantém o programa funcionando'''

    main()