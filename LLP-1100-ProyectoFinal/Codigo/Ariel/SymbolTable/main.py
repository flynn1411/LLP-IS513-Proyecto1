# -*-coding: utf-8 -*-

from lark import Lark, Tree, Token, Transformer
from tabulate import tabulate
from tableGenerator import TableGenerator
from Grammar import *
import sys

fileName = sys.argv[1:][0]

f = open(fileName,"r")
fileContents = f.read()
f.close()

tableGen = TableGenerator()
parser = Lark(grammar, parser="lalr", transformer=tableGen)

#try:
parseTree = parser.parse("%s\n"%fileContents)

print(tableGen.variables)

"""
def getTokenInstances(tree, type, value):
    results =[]

    if isinstance(tree, Tree):
        for child in tree.children:

            if isinstance(child, Tree):
                childArray = getTokenInstances(child, type, value)
                if len(childArray) > 0:
                    results += childArray

            elif isinstance(child, Token) and ( child.type == type and child.value == value):
                results.append(child)

    elif isinstance(child, Token) and ( child.type == type and child.value == value):
        results.append(child)

    return results

tokens = getTokenInstances(parseTree, "IDENTIFIER", "hola")

table = []

for token in tokens:
    row = []

    row.append(token.value)
    row.append(token.line)
    row.append(token.type)

    table.append(row)

print(tabulate(table, headers=["nombre", "linea", "valor"]))"""