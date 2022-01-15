"""
* Criar variaveis para nome (str), idade(int)
* altura(float) e peso (float) de uma pessoa
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura (duas casas decimais após o ponto): ")
peso = input("Digite seu peso (uma casa decimal após ponto): ")
ano_atual = input("Digite o ano atual: ")

try:
    ano_nascimento = int(ano_atual) - int(idade)
except:
    print("Erro no preenchimento do ano atual ou idade")

try:
    peso = float(peso)
    altura = float(altura)
    IMC = peso / (altura ** 2)
except:
    print("Erro no preenchimento do peso ou altura")

print(f'\n{nome} tem {idade} anos, {altura:.2f} de altura e peso {peso}')
print(f'{nome} nasceu em {ano_nascimento}')
print(f'O IMC de {nome} é {IMC:.2f}')

