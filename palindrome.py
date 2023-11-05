import string
# DESCOBRINDO SE UMA FRASE OU PALAVRA É UM PALÍNDROMO EM LÍNGUA PORTUGUESA
texto = str(input("Digite uma frase ou palavra: "))
# É uma boa prática nomear as variáveis em inglês, isso vai te ajudar no futuro
# quando você tiver usando algum framework
textojunto = texto.replace(" ","").lower().translate(str.maketrans('', '', string.punctuation))

# soma = len(texto) coloquei esse método dentro das {}
# COMO O PYTHON DEVOLVE O PALÍNDROMO SOMENTE SE FOR ESCRITO COM LETRAS MÍNUCULAS É NECESSÁRIO A ALTERAÇÃO A SEGUIR:
# Não é SOMENTE. Posso fazer isso com letras maisculas por exemplo.
# o Python é case sensitive (Python é diferente de python)
# a gente usa esse método para ficar python = python

print(f"A frase ou palavra '{texto}' tem {len(texto)} caracteres ;D")
# Eu recomendo que você use a variável texto para preservar a string original
# Pois a frase entre aspas sera exibida do jeito que ele digitou (sem tratametos)
print('Essa frase/palavra é um Palíndromo?')

if (textojunto.lower()) == (textojunto.lower()[::-1]):
    print("Sim, é um palíndromo! =)")
else:
    print("Não, não é um palíndromo! =(")

# para funcionar a frase não pode ter acentuação, para resolver isso
# de forma simples, é necessário usar o pip e isso já um assunto mais avançado.