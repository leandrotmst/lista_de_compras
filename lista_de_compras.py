"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros dce índices inexistentes na lista.
"""
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os 

lista = []

while True:
    print('Selecione uma opção.')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system('cls')
        nome = input('Digite o produto que você quer inserir: ')
        valor = input('Valor: ')
        
        if nome.isnumeric():
            print('Você digitou alguma coisa errada.')
        
        if valor.isdigit():
            print('Produto inserido com sucesso.')
            lista.append(nome)
            os.system('cls')
        
        else:
            print('Você digitou alguma coisa errada.')
            break
    
    elif opcao == 'a':
        apagar = input('Digite o índice que você deseja apagar: ')

        try:
            indice = int(apagar)
            del lista[indice]
        
        except ValueError:
            print('Por favor digite número int.')
        
        except IndexError:
            print('Índice não existe na lista')
        
        except Exception:
            print('Erro desconhecido')
    
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar.')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')