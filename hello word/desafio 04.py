# Solicita ao usuário que digite dois valores
n1 = int(input('Digite um valor para somar: '))
n2 = int(input('Digite outro valor: '))

# Realiza a soma dos dois números
resul = n1 + n2

# Exibe o resultado da soma
print('A soma entre {} e {} é igual a {}'.format(n1, n2, resul))

# Pergunta se a resposta está correta
correto = input('Essa resposta realmente está certa? (sim/não): ').strip().lower()

if correto == 'sim':
    print('Ótimo! Fico feliz que esteja certo.')
elif correto == 'não':
    print('Que pena! Vamos revisar então.')
else:
    print('Resposta inválida. Por favor, responda com "sim" ou "não".')
