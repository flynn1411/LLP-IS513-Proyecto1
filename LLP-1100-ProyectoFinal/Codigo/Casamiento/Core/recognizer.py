# -*- coding: utf-8 -*-
"""
Poner comentarios aquí
"""
from Core.lark import Lark
from tabulate import tabulate

class Recognizer:
    def __init__(self):
        self.fileContents = ""
        self.header = [
            ["Intérprete de Lenguajes ILANG"],
            ["@authors: Ana Hernández, Fernando Córtes, Gabriel Escobar, Josué Izaguirre (Dream Team)"],
            ["@version: 0.1.0"],
            ["@fecha: 16/08/2020"]
            ]
        self.result = []

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

    def checkWithParser(self, parser):
        try:
            parser.parse(self.fileContents)
            return True
        except Exception:
            return False

    def printResult(self):
        print("\n"*2)
        print(tabulate(self.header, stralign="center", tablefmt="fancy_grid"))
        print("\n"*2)
        print(tabulate(self.result, stralign="left", tablefmt="grid"))