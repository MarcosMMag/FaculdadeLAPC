# O WHILE repete o código enquanto for verdadeiro.
# Usado quando a repetições sem saber exatamente a quantidade das repetições.

# Variavel Idade
entrada_idade = ''

# Loop enquanto a entrada for diferente de "0"
while str(entrada_idade) != '0':
    entrada_idade = input("Digite um número ou 0 para sair: ")
    print("Número digitado:", entrada_idade)
