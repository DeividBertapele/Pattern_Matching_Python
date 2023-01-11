lista = [1, 2, 3, 4,]

match lista:
    case [] | [_]:
        print('Vazio ou somente com 1')
        
    case [1, 2]:
        print('Lista = [1, 2]')
        
    case [1, *resto]:
        print(f'Primeiro de uma lista é 1 e o resto {resto}')

