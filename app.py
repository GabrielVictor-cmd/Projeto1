import os
restaurantes = [{"nome": "Temperaria Salgada", "categoria": "Salgada", "ativo": False},
                {"nome": "Tempero Mexicano", "categoria": "Picante", "ativo": True},
                {"nome": "Sushi Mano", "categoria": "Sushi", "ativo": False}
                ]

def exibir_nome_do_programa():
    print("Salgado Tempero\n")

def exibir_opçoes():
    print("1- Cadastrar restaurante")
    print("2- Listar Restaurante")
    print("3- Ativar restaurante")
    print("4- Sair\n")

def Encerrando_programa():
    os.system("cls")
    print("Encerrando programa...")
    exibir_subtitulo("Encerrando o programa")

def voltar_menu_principal():
    input("\nDigite ENTER para valtar para o menu principal")
    main()

def opçao_invalida():
    print("Opção inválida!")
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    print(texto)
    print()

def cadastrar_novo_restaurante():
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
    exibir_subtitulo("Listanto restaurantes: ")

    for restaurante in restaurantes:
        nome_restaurantes = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f" - {nome_restaurantes} | {categoria} | {ativo}")
        
    input("Digite ENTER para voltar ao menu principal")
    main()

def escolher_opçao():
    try:
        opçao_escolhida = int(input("Escolha uma opção: "))
        print(f"Você escolheu a opção: {opçao_escolhida}\n")

        if opçao_escolhida == 1:
            cadastrar_novo_restaurante()
        
        elif opçao_escolhida == 2:
            listar_restaurantes()
        
        elif opçao_escolhida == 3:
            print("Ativar restaurantes")

        elif opçao_escolhida == 4:
            Encerrando_programa()

        else:
            opçao_invalida()

    except:
        opçao_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opçao()

if __name__ == "__main__":
    main()