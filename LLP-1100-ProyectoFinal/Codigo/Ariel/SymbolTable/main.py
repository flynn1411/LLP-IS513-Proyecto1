# -*-coding: utf-8 -*-

from lark import Lark, Tree, Token, Transformer
from tabulate import tabulate
from tableGenerator2 import TableGenerator2
from grammar2 import *
import sys

fileName = sys.argv[1:][0]

f = open(fileName,"r")
fileContents = f.read()
f.close()

tableGen = TableGenerator2("Table")
parser = Lark(grammar, parser="lalr", transformer=tableGen)

#try:
parseTree = parser.parse("%s\n"%fileContents)

#print(parseTree)

def getTokenInstances(tree, type, value):
    results = ""

    if isinstance(tree, Tree):
        for child in tree.children:

            if isinstance(child, Tree):
                innerSearch = getTokenInstances(child, type, value)
                if len(innerSearch) > 0:
                    results += innerSearch

            elif isinstance(child, Token) and ( child.type == type and child.value == value):
                results += "%s," % child.line

    elif isinstance(child, Token) and ( child.type == type and child.value == value):
        results += "%s," % child.line

    return results

table = []
for key in tableGen.variables.keys():
    row = []

    row.append(key)
    row.append(
        getTokenInstances(
            parseTree, "IDENTIFIER", key
        )
    )

    row.append(tableGen.variables[key]["value"])
    row.append(tableGen.variables[key]["type"])
    row.append(0)

    table.append(row)


print(tabulate(table, headers=["Nombre", "Lineas", "Valor", "Tipo de Dato","Función"]))