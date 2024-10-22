banco_de_dados = []

def menu ():
    opções = ["1.Novo livro ", "2.Livros ", "3.pesquisar ", "4.Atualizar", "5. Sair"]

#adicionada as subcamadas
#adicionar categoria de cod da biblioteca central ufpa
#adicionar mensagem de enbtrada do sistema 
    print()
    print("╔══════════════════════════╗")
    print(f"║          MENU            ║")
    print("╠══════════════════════════╣")
    for opção in opções:
        print(f" {opção}")
    print("╚══════════════════════════╝")

def submenu2 ():
    subopções2 = ["1.Imprimir tudo", "2.Imprimir trecho","3.Voltar"]
    print()
    print("╔══════════════════════════╗")
    print(f"║          MENU            ║")
    print("╠══════════════════════════╣")
    for opção in subopções2:
        print(f" {opção}")
    print("╚══════════════════════════╝")

def submenu3 ():
    subopções3 = ["1.Pesquisa geral", "2.Pesquisa especifica","3.Voltar"]
    print()
    print("╔══════════════════════════╗")
    print(f"║          MENU            ║")
    print("╠══════════════════════════╣")
    for opção in subopções3:
        print(f" {opção}")
    print("╚══════════════════════════╝")   

def adicionar_livro ():
        livro = {}

        livro['Título'] = input("Título: ")
        livro['Autor(a)'] = input("Autor(a): ")
        livro['Editor(a)'] = input("Editor(a): ")
        livro['Data de publicação'] = input("Data de publicação (dd/mm/aaaa): ")
        livro['Número de páginas'] = int(input("Número de páginas: "))
        livro['Gênero'] = input("Gênero: ")
        livro['Valor'] = float(input("Valor (R$): "))

        banco_de_dados.append(livro)

def mostar_registro(inicio,fim):

#consegui o objetivo de fazer apenas uma função para msotar os registros tanto ao todo quanto em trecho 
    if inicio == 0:
        fim = len(banco_de_dados)
        tamanho = range(fim)
    else:
        tamanho = (inicio-1,fim-1)
 
    for i in tamanho:
#colocar _/_/_ , pgs, sugestão de genero ou outros.
        print()
        print("╔══════════════════════════╗")
        print(f"Livro {i+1}".center(25))
        print(f"Título: {banco_de_dados[i]['Título']}")
        print(f"Autor(a): {banco_de_dados[i]['Autor(a)']}")
        print(f"Editor(a): {banco_de_dados[i]['Editor(a)']}")
        print(f"Data de publicação: {banco_de_dados[i]['Data de publicação']}")
        print(f"Número de páginas: {banco_de_dados[i]['Número de páginas']}")
        print(f"Gênero: {banco_de_dados[i]['Gênero']}")
        print(f"Valor: R${banco_de_dados[i]['Valor']:.2f}")

def pesquisa_geral(pesquisa):
        resultados = []

        for livro in banco_de_dados:
            pesquisa = str(pesquisa_convertida)
            titulo_encontrado = pesquisa.lower() in livro['Título']
            autor_encontrado = pesquisa.lower() in livro['Autor(a)']
            editora_encontrada = pesquisa.lower() in livro['Editor(a)']
            genero_encontrado = pesquisa.lower() in livro['Gênero'] 
            pesquisa_convertida = int(pesquisa)  
            data_de_publicacao_encontrada = pesquisa_convertida in livro['Data de publicação']
            numero_de_paginas_encontrada = pesquisa_convertida in livro['Número de páginas']
            valor_encontrado = pesquisa_convertida in livro['Valor']

        if titulo_encontrado or autor_encontrado or editora_encontrada or genero_encontrado or data_de_publicacao_encontrada or numero_de_paginas_encontrada or valor_encontrado :
            resultados.append(livro)
        
        if len(resultados) > 0:
            print(f"{len(resultados)} resultado(s) encontrado(s) para '{pesquisa}':")
            for i, livro in enumerate(resultados, 1):
                print(f"Livro {i} - Título: {livro['Título']} | Autor(a): {livro['Autor(a)']} | Editor(a): {livro['Editor(a)']}")
                print(f"| Data de publicação: {livro['Data de publicação']} | Número de páginas: {livro['Número de páginas']}") 
                print(f"| Gênero: {livro['Gênero']} | Valor: {livro['Valor']} | ")
        else:
            print(f"Nenhum resultado encontrado para '{pesquisa}'.")

def pesquisa_especifica(pesquisa):
    print("A    ")
#

while True:
    menu()
    escolha_menu = int(input("Selecione uma opção:"))
  
    if escolha_menu == 1: 
        if len(banco_de_dados) >= 51:
            print("Número máximo de registros atigido")
        else:
            adicionar_livro()
            while True:
                continuar = int(input("Deseja adicionar outro registro? Sim(1) Não(2): "))
                if continuar == 1: 
                    adicionar_livro()
                else:    
                    break

    elif escolha_menu == 2:
# nesse submenu eu fiz um while true dentro do outro while true principal para simular melhor um sistema de registro real
        while True:
            submenu2()
            escolha_menu2 = int(input("Selecione uma opção: "))
            if escolha_menu2 == 1:

                mostar_registro(0,0)
                continue

            if escolha_menu2 == 2:
                trecho_inico = int(input("Informe de onde deve começar seu trecho: "))
                trecho_fim = int(input("Informe de onde deve terminar seu trecho: "))

                mostar_registro(trecho_inico,trecho_fim)
                continue

            else:
                break

#concertar função 3
    elif escolha_menu == 3:
        while True:
            submenu3()
            escolha_menu3 = int(input("Selecione uma opção: "))

            if escolha_menu3 == 1:
                pesquisa = input("Digite o termo para pesquisa geral: ")
                pesquisa_geral(pesquisa)
            elif escolha_menu3 == 2:
                print("1 = Título, 2 = Autor(a), 3 = Editor(a), 4 = Data de publicação, 5 = Número de páginas, 6 = Gênero, 7 = Valor")
                pesquisa = (input("Digite o termo para pesquisa: "))
                pesquisa_especifica(pesquisa)
            else:
                break

    elif escolha_menu == 4:
        print()
    #falta a função atualizar com outro submenu
    else:
        sair2 = int(input("Tem certeza que deseja sair? Todos os registros serão apagados permanentemente. Sim(1) Não(2): "))
        if sair2 == 2:
            continue
        else:
            print("Volte Sempre!")
            break
#usar true or false