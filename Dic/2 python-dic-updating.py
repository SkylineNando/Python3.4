#Foram apresentados os dados em que o aluno estuda
dict = {'Nome': 'Rafael', 'Idade': 7, 'Classe': 'Primeira', 'Escola': 'Colégio Dom Bosco'};

print("Quando o valor não alterou")

print("dict['Idade']: ", dict['Idade'])
print("dict['Escola']: ", dict['Escola'])

print("")
print("Quando o valor muda")

dict['Idade'] = 8; # update existing entry
dict['Escola'] = "Colégio Joaquim de Souza Fagundes"; # Add new entry

#Essa nova atribuição substitui o valor anterios colocando novos valores ao print

print ("dict['Idade']: ", dict['Idade'])
print ("dict['Escola']: ", dict['Escola'])
