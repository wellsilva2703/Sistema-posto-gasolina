print('=== Bem vindos ao posto WS ===')

print('Preço da gasolina é de R$8,89(G)\nPreço do alcool é de R$6,59(A)')

Liquido_escolhido = input('Qual das duas opções acima foi a escolhida?\n')
Qntd_litros = int(input('Qual a quantidade de litros colocar no tanque?\n'))
preço = float(input('Preço do liquido escolhido:\n'))

if Qntd_litros < 10:
    Total = Qntd_litros * preço
    print(f'O valor sem desconto ficou: {Total:.2f}')
    print('Tenha um otimo dia e volte sempre!')
print('-'* 65)

if Qntd_litros >= 20:
    Preço_Bruto = Qntd_litros * preço
    print(f'O valor bruto ficou: R${Preço_Bruto:.2f}.')
    Valor_do_desconto = Preço_Bruto * 0.05
    print(f'O valor do desconto é de: R${Valor_do_desconto:.2f}')
    Valor_final = Preço_Bruto - Valor_do_desconto
    print(f'O valor final é de: R${Valor_final:.2f}')


 


