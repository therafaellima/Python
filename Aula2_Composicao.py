#Existe 3 maneira de se fazer composição

#Composição com marcadores de posição
nota = 8.5
s1 = 'Você tirou %.2f na disciplina de Algoritmos.' % nota
print(s1)

#Composição moderna (Derivada da Linguagem C)
nota = 8.5
disciplina = 'Disciplina'
s1 = 'Você tirou {} na {} de Algoritmos.' .format(nota,disciplina)
print(s1)

#Composição com f-String
nota = 8.5
disciplina = 'Disciplina'
s1 = f'Você tirou {nota} na {disciplina} de Algoritmos.'
print(s1)

#Crie três variáveis distintas: uma contendo o nome da sua comida favorita;
#outra contendo o seu ano de nascimento; e a terceira contendo o
#resultado da divisão do seu ano de nascimento pela sua idade.

#Armazene, em uma quarta variável, do tipo string, uma mensagem que
#contenha todas as informações das variáveis anteriores.

#Resolva o exercício pela maneira clássica de composição e também pela
#maneira moderna e com f-string.

comida = 'strogonoff'
nascimento = 1996
idade = nascimento / 29

s1 = 'Minha comida favorita é: %s \nMeu ano de nascimento é: %i \nO resultado da divisão do meu ano de nascimento pela minha idade é: %i' % (comida,nascimento,idade)

print(s1)