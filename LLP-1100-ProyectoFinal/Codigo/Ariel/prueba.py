# -*- coding: utf-8 -*-

import sys
from Reader import Reader
from lark import Lark
from tabulate import tabulate

#reader = (Reader()).read()
parser = Lark.open('ruby.lark', parser='lalr')

fileName = sys.argv[1:][0]

file1 = open("ruby.lng", "r")
content = file1.read()
file1.close()

parser.parse(content)

"""
lines = file1.readlines()

result = []

count = 1

for line in lines:
    try:
        parser.parse(line)
        result.append([count, line])
    
    except Exception:
        result.append([count, "Linea Desconocida"])
    
    count += 1


print(tabulate(result))
"""