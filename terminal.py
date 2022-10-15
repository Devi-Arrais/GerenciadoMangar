from bancodedados import *


menu = """Bem vindo ao organizaodr de mangas: 
Digite a opção
1 - Adicionar novo mangar a lista
2 - Verificar se a novo capitulo
3 - Deletar manga na lista
4 - Listar os mangas
0 - Sair
"""

sair = True

while sair:
    Criandobanco()
    op = int(input(menu))

    if op == 1:
        titulo = input("Qual o titulo do manga: ")
        link = input("Qual o link do manga(O site deve ser mangakakalot): ")
        capitulo = input("Qual o ultimo capitulo: ")
        adicinarmanga(titulo, link, capitulo)
    elif op == 2:
        verifica()
    elif op == 3:
        name = input("Dgite o nome do manga para excluir: ")
        excluindomanga(name)
    elif op == 0:
        print("Saindo")
        sair = False
    elif op == 4:
        listarmangas()
    else:
        print("opção invalida")
