# -*- coding:utf-8 -*-

import re
from lark import Transformer, v_args

"""
    Tabla:

    ID: nombre de variable (donde fue declarada)
    Tipo de Dato
    Dimension: 0
    Linea de código donde fue declarada
    Referencia: todas las lineas donde se les hacen un llamado
    Dirección en memoría. id(variable)

"""

@v_args(inline=True)


class TableGenerator(Transformer):
    def __init__(self):
        self.variables = {}

    def assignvalue(self, name, value):
        print("%s,%s"%(name,value))
        #self.variables[name] = self.tokenize(value)
        #print("\n%s\n"%self.variables)

    def getvalue(self, name):
        if(self.variables[name]):
            return self.variables[name]["value"]

        else:
            quit("La variable %s no existe."%name)

    def tokenize(self, lexeme):
        tokenType = ""

        if re.match(r"\d+(\.\d+)?",lexeme):
            tokenType = "number"
            lexeme = float(lexeme)

        elif re.match(r"((\"[^\"]*\")|('[^']*'))", lexeme):
            tokenType = "string"

        elif re.match(r"((true)|(false))", lexeme):
            tokenType = "boolean"

        elif re.match(r"(null)|(undefined)", lexeme):
            tokenType = "undefined"

        return {"value": lexeme, "tokenType": tokenType}