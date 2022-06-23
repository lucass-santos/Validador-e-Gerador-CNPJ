import re
from random import randint

def verifica_sequencia_cnpj(string):
    while string[0] * 14 == string:
        print(f'Você digitou uma sequência de números iguais.')
        string = input('Digite novamente o CNPJ: ')
    return string


def retira_caracteres(string):
    return re.sub(r'\D', '', verifica_sequencia_cnpj(string))


def verifica_quantidade_caracteres(string):
    while len(string) != 14:
        print('Foi digitada uma quantidade diferente de 14 números para verificação do CNPJ.')
        string = retira_caracteres(input('Digite novamente o CNPJ: '))
    return string


def retira_digito_cnpj(string):
    return string[0:12]


def calcula_digitos_cnpj(string):
    soma = 0
    inicio = 5 if len(string) == 12 else 6
    for indice, posicao in enumerate(range(inicio, -7, -1)):
        if posicao <= 1:
            posicao += 8

        soma += posicao * int(string[indice])

    string += '0' if (11 - (soma % 11)) > 9 else str((11 - (soma % 11)))
    return string


def valida_cnpj(string):
    cnpj = verifica_quantidade_caracteres(retira_caracteres(string))
    novo_cnpj = calcula_digitos_cnpj(calcula_digitos_cnpj(retira_digito_cnpj(cnpj)))
    resultado = True if novo_cnpj == cnpj else False
    return resultado, novo_cnpj

def mascara_cnpj(string):
    cnpj =f'{string[:2]}.{string[2:5]}.{string[5:8]}/{string[8:12]}-{string[12:14]}'
    return cnpj

def gera_cnpj():
    primeiro = randint(00, 99)
    segundo = randint(100, 999)
    terceiro = randint(100, 999)
    cnpj = f'{primeiro}.{segundo}.{terceiro}/0001-00'
    _, cnpj = valida_cnpj(cnpj)
    return mascara_cnpj(cnpj)