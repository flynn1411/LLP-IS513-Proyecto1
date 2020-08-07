# -*- coding: utf-8 -*-
"""
Poner comentarios aquí
"""
from lark import Lark
from tabulate import tabulate

class Recognizer:
    def __init__(self):
        self.fileContents = ""
        self.message = """ """

    def recognize(self, fileContents):
        self.fileContents = fileContents
        rubyParser = Lark.open("Core/Grammars/ruby.lark", "lalr")
        bashParser = Lark.open("Core/Grammars/grammarBash.lark", "lalr")

        if(self.checkWithParser(rubyParser)):
            self.message = """
            \n\n
            Lenguaje Encontrado: Ruby
            \n\n
            Programa:
            \n\n
            %s
"""% self.fileContents

        elif(self.checkWithParser(bashParser)):
            self.message = """
            \n\n
            Lenguaje Encontrado: Bash
            \n\n
            Programa:
            \n\n
            %s
"""% self.fileContents

        else:
            self.message = """
            \n\n
            El Lenguaje no ha podido ser identificado. 
            \n\n
"""

        return self

    def checkWithParser(self, parser):
        try:
            parser.parse(self.fileContents)
            return True
        except Exception:
            return False

    def printResult(self):
        print(self.message)


"""
#reader = (Reader()).read()
parser = Lark.open('ruby.lark', parser='lalr')

fileName = sys.argv[1:][0]

file1 = open(fileName, "r")
content = file1.read()
file1.close()

print("\n\n%s\n\n"%content)

parser.parse("%s\n"%content)
"""