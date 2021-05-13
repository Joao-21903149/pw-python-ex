import fileinput


def calcula_linhas(ficheiro):
    return len(open(ficheiro, "r").readline())

def calcula_carateres(ficheiro):
    return len(open(ficheiro, "r").read().replace("\n", ""))

def calcula_palavra_comprida(ficheiro):
    filename = open(ficheiro, "r").read().replace(",", "").split()
    return max(filename, key=len)

def calcula_correncia_de_letras(ficheiro):
    filename = open(ficheiro, "r").read().replace("\n", "")
    letras = {}
    for a in filename.lower():
        if a not in letras:
            letras[a] = filename.lower().count(a)
    return letras

