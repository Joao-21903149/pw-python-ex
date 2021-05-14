import sys
import os


def pede_nome():
    while True:
        try:
            name = input(f"Insira o nome do ficheiro (pasta {os.getcwd()}): ")
            f = open(name, 'r')
            return name
        except IOError:
            print("Ficheiro nao existe")

def gera_nome(filename):
    filename_output = filename[0:-4]
    filename_output += ".json"
    return filename_output