# -*-coding: utf-8 -*-

from lark import Lark
import sys

fileName = sys.argv[1:][0]

f = open(fileName,"r")
fileContents = f.read()
f.close()

parser = Lark.open("ruby.lark", "lalr")

#try:
tree = parser.parse("%s\n"%fileContents)

for child in tree.children:
    print("\n\n%s\n\n"%child)

#except Exception:
#    print(Exception)