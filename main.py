
print('1- soma')
print('2- subtração')
opcao1 = int(input('1-soma , 2-multiplicação , 3-subtração  , 4-divisão ')) 

print('1- soma')
if opcao == 1:
    num1 = float(input('primeiro número: '))
    num2 = float(input('segundo número: '))
    res = num1 + num2
    print(f'O resultado é {res}')

elif opcao == 2:
    num1 = float(input('primeiro número: '))
    num2 = float(input('segundo número: '))
    res = num1 * num2

    print(f'O resultado é {res}')
elif opcao == 3:
    num1 = float(input('primeiro número: '))
    num2 = float(input('segundo número: '))
    res = num1 - num2 
    print(f'O resultado é {res}')
if opcao == 4:
    num1 = float(input('primeiro número: '))
    num2 = float(input('segundo número ')) 
    res = num1 / num2
    print(f'O resultado é {res}')
else:
    print('Número Inválido')

        
