#Função
from Conversor import c_f, f_c

while True:
    #Apresentação

    print('\n','-' * 5,' • Conversor • ','-' * 5,'\n')

    #Entrada

    print('1. Celsius para Fahrenheit')
    print('2. Fahrenheit para Celsius')
    print('3. Sair \n')

    opcao = int(input('Escolha uma opção: ').strip())
    #Processamento - Saida
    if opcao == 1:
        celsius = float(input('Digite a temperatura em Celsius: '))
        fahrenheit = c_f(celsius)
        print(f"{celsius}ºC é igual a {fahrenheit}ºF")
    elif opcao == 2:
        fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
        celsius = f_c(fahrenheit)
        print(f'{fahrenheit}ºF é igual a {celsius}ºC')
    elif opcao == 3:
        print('Tchauuu')
        break
    else:
        print('\nOpção Invalida,Tente novamente!')