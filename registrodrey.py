def menu ():
    menu_title = "MENU"
    options = ["1.Novo livro ", "2.Livros ", "3.comming soon ", "4. Sair"]

    print("╔══════════════════════════╗")
    print(f"║          {menu_title}            ║")
    print("╠══════════════════════════╣")
    for option in options:
        print(f" {option}")
    print("╚══════════════════════════╝")

#WHILE TRUE:
menu()
escolha_menu = int(input("Selecione uma opção:"))
banco_de_dados = []
 
if escolha_menu == 1: 
    if len(banco_de_dados) >= 51:
        print("Não")
    else:
        livro = {}

        banco_de_dados.append(livro)

        livro['Título'] = input("Título: ")
        livro['Autor(a)'] = input("Autor(a): ")
        livro['Editor(a)'] = input("Editor(a): ")
        livro['Data de publicação'] = input("Data de publicação (dd/mm/aaaa): ")
        livro['Número de páginas'] = int(input("Número de páginas: "))
        livro['Gênero'] = input("Gênero: ")
        livro['Valor'] = float(input("Valor (R$): "))
    for i in banco_de_dados:  
        print(f"{livro}")
        
elif escolha_menu == 2:
    print(banco_de_dados)

elif escolha_menu == 3:
    print("comming soon")

else:
    sair2 = int(input("Tem certeza que deseja sair? sim(1) não(2)"))