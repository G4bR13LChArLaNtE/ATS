# Nome: Julio Gabriel Charlante Barbosa Moreira da Silva
# RA: 2101478 Turma: SI


def converte_romano(simbolo):
    dicionario = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    valor = 0

    for i in range(len(simbolo)):
        if i > 0 and dicionario[simbolo[i]] > dicionario[simbolo[i-1]]:
            valor += dicionario[simbolo[i]] - 2 * dicionario[simbolo[i-1]]
        else:
            valor += dicionario[simbolo[i]]
    return valor
