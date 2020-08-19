# -*- coding: utf-8 -*-
from Core.lark import Lark
from tabulate import tabulate

"""
! Clase que reconoce gramáticas
? Obtiene los contenidos de un archivo y reconoce gramáticalmente si es Ruby o Bash.
? Retorna una impresión en pantalla determinando si ´detectó o nó el algún lenguaje de programación
"""
class Recognizer:
    def __init__(self):
        self.fileContents = ""
        self.header = [
            ["Intérprete de Lenguajes Rosetta"],
            ["@authors:\nAna Hernández(its_anaehm),\nFernando Córtes(Ferloxc),\nGabriel Escobar(Lersgeeb),\nJosué Izaguirre (flynn1411)"],
            ["@version: 0.1.0"],
            ["@fecha: 16/08/2020"]
            ]
        self.result = []

    """
    ! Método para reconocer lenguajes de manera gramátical
    ? Obtiene los contenidos de un archivo para poder determinar el lenguaje del archivo.
    ? Prueba los distíntos casos para saber si es o no un lenguaje aceptado.
    """
    def recognize(self, fileContents):
        self.fileContents = fileContents
        rubyParser = Lark.open("Core/Grammars/ruby.lark", "lalr")
        bashParser = Lark.open("Core/Grammars/grammarBash.lark", "lalr")

        if(self.checkWithParser(rubyParser)):
            self.result.append(["\tLenguaje Detectado:"])
            self.result.append(["\tRuby"])
            self.result.append(["\tPrograma Leído:"])
            self.result.append([fileContents])

        elif(self.checkWithParser(bashParser)):
            self.result.append(["Lenguaje Detectado"])
            self.result.append(["Bash"])
            self.result.append(["Programa Leído:"])
            self.result.append([fileContents])

        else:
            self.result.append("\nPrograma No Encontrado\n")

        return self

    """
    ! Método para analizar gramáticalmente un texto
    ? Recibe un parser con una gramática en específico. De existir gramática desconocida, se devuelve Falso, de lo contrario verdadero. 
    """
    def checkWithParser(self, parser):
        try:
            parser.parse(self.fileContents)
            return True
        except Exception:
            return False

    """
    ! Método que imprime los resultados del reconocimiento gramátical
    """
    def printResult(self):
        print("\n"*2)
        print(tabulate(self.header, tablefmt="fancy_grid"))
        print("\n"*2)
        print(tabulate(self.result, stralign="left", tablefmt="grid"))