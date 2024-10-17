def menu ():
    menu_title = "MENU"
    options = ["1.Novo livro ", "2.Livros ", "3.pesquisar ", "4.Atualizar", "5. Sair"]

#adicionar subcamadas no atualizar

    print("╔══════════════════════════╗")
    print(f"║          {menu_title}            ║")
    print("╠══════════════════════════╣")
    for option in options:
        print(f" {option}")
    print("╚══════════════════════════╝")

def add ():
        livro = {}

        livro['Título'] = input("Título: ")
        livro['Autor(a)'] = input("Autor(a): ")
        livro['Editor(a)'] = input("Editor(a): ")
        livro['Data de publicação'] = input("Data de publicação (dd/mm/aaaa): ")
        livro['Número de páginas'] = int(input("Número de páginas: "))
        livro['Gênero'] = input("Gênero: ")
        livro['Valor'] = float(input("Valor (R$): "))

        banco_de_dados.append(livro)

banco_de_dados = []
livro = []

while True:
    menu()
    escolha_menu = int(input("Selecione uma opção:"))
  
    if escolha_menu == 1: 
        if len(banco_de_dados) >= 51:
            print("Número máximo de registros atigido")
        else:
            add()
            continuar = int(input("Deseja adicionar outro registro? Sim(1) Não(2): "))
            if continuar == 1: 
                add()
            else:    
                continue
    elif escolha_menu == 2:
        for x in range (len(banco_de_dados)):
            print(f"{livro[x]}")
#adicionar cod pra ser um de baixo do outro (estética)

    elif escolha_menu == 3:
        pesquisa = input("Área de pesquisa: ")
        if pesquisa == 2:
            print(f"{pesquisa}")
#não sei como pesquisar

    else:
        sair2 = int(input("Tem certeza que deseja sair? Todos os registros serão apagados permanentemente. Sim(1) Não(2): "))
        if sair2 == 2:
            continue
        else:
            print("Volte Sempre!")
            break
#usar true or false