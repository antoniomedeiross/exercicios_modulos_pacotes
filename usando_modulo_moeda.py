
import moeda

valor = float(input('informe o valor: '))



#### teste exercício 107 ####
print(f'o dobro de {valor} é {moeda.dobro(valor)}')
print(f'a metade de {valor} é {moeda.metade(valor)}')
print(f'aumentando em 10% passará a ser {moeda.aumenta(valor, 10)}')
print(f'diminuindo em 30% passará a ser {moeda.diminui(valor, 30)}')
########################
print (''' 

//////////////////////////////////////////////////

''')
#### teste exercício 108 ####

print(f'o dobro de {valor} é {moeda.moeda(moeda.dobro(valor))}')
print(f'a metade de {valor} é {moeda.moeda(moeda.metade(valor))}')
print(f'aumentando em 10% passará a ser {moeda.moeda(moeda.aumenta(valor, 10))}')
print(f'diminuindo em 30% passará a ser {moeda.moeda(moeda.diminui(valor, 30))}')

########################
print(''' 

//////////////////////////////////////////////////

''')

#### teste exercício 109 ####

print(f'o dobro de {valor} é {moeda.dobro(valor, moeda = True)}')
print(f'a metade de {valor} é {moeda.metade(valor, moeda = True)}')
print(f'aumentando em 10% passará a ser {moeda.aumenta(valor, 10, moeda = True)}')
print(f'diminuindo em 30% passará a ser {moeda.diminui(valor, 30, moeda = True)}')


print(moeda.resumo(100, 10, 15))